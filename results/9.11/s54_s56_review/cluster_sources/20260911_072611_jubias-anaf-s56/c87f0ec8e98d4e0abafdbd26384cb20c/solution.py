import html
import json
import os
import re
import shutil
import unicodedata

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from engine.candidate_runtime import CandidateSession
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

RANDOM_SEED = 2025
INPUT_DIR = "./input"
WORKING_DIR = "./working"

MAX_SEQUENCE_LENGTH = 256
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 32
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 4
NUM_WORKERS = 2
INTERMEDIATE_NEGATIVE_TO_POSITIVE_RATIO = 3

os.makedirs(WORKING_DIR, exist_ok=True)

np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)

session = CandidateSession.from_env()

raw_train_df = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    low_memory=False,
)
raw_test_df = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

if "comment_text" not in train_df.columns or "comment_text" not in valid_df.columns:
    raise ValueError("Training and validation partitions must contain comment_text.")
if "comment_text" not in test_df.columns:
    raise ValueError("Test partition must contain comment_text.")
if "target" not in train_df.columns or "target" not in valid_df.columns:
    raise ValueError("Training and validation partitions must contain target.")

_URL_RE = re.compile(r"(?i)\b(?:https?://|ftp://|www\.)[^\s<>()\[\]{}]+")
_USER_RE = re.compile(r"(?<![\w@])@[\w_]{1,64}")
_HTML_TAG_RE = re.compile(r"<[^>\n]{1,200}>")
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_WHITESPACE_RE = re.compile(r"\s+")

SCORING_IDENTITY_PATTERNS = {
    "male": r"\b(?:male|man|men|boy|boys|gentleman|gentlemen)\b",
    "female": r"\b(?:female|woman|women|girl|girls|lady|ladies)\b",
    "homosexual_gay_or_lesbian": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|"
        r"lgbt|lgbtq|queer|queers)\b"
    ),
    "christian": r"\b(?:christian|christians|christianity|catholic|catholics)\b",
    "jewish": r"\b(?:jew|jews|jewish|judaism)\b",
    "muslim": r"\b(?:muslim|muslims|islam|islamic)\b",
    "black": r"\b(?:black|blacks|african[\s-]?american)\b",
    "white": r"\b(?:white|whites|caucasian)\b",
    "psychiatric_or_mental_illness": (
        r"\b(?:mental(?:ly)?\s+(?:ill|illness)|psychiatric|"
        r"depression|depressed|schizophren(?:ia|ic)|bipolar|autis(?:m|tic))\b"
    ),
}
COMPILED_IDENTITY_PATTERNS = {
    name: re.compile(pattern, flags=re.IGNORECASE)
    for name, pattern in SCORING_IDENTITY_PATTERNS.items()
}


def normalize_comment_text(value):
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", html.unescape(str(value)))
    text = _HTML_TAG_RE.sub(" ", text)
    text = _URL_RE.sub(" URLTOKEN ", text)
    text = _USER_RE.sub(" USERTOKEN ", text)
    text = _CONTROL_RE.sub(" ", text)
    text = _WHITESPACE_RE.sub(" ", text).strip()
    return text


def uppercase_letter_ratio(text):
    letters = [character for character in text if character.isalpha()]
    if not letters:
        return 0.0
    return float(sum(character.isupper() for character in letters) / len(letters))


def engineer_text_features(frame):
    cleaned_text = frame["comment_text"].map(normalize_comment_text)
    frame["model_text"] = cleaned_text

    char_count = cleaned_text.str.len().astype(np.float32)
    word_count = cleaned_text.str.count(r"\S+").astype(np.float32)

    frame["feat_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["feat_log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["feat_uppercase_ratio"] = cleaned_text.map(uppercase_letter_ratio).astype(
        np.float32
    )
    frame["feat_exclamation_rate"] = (
        cleaned_text.str.count(r"!").astype(np.float32) / (char_count + 1.0)
    ).astype(np.float32)
    frame["feat_question_rate"] = (
        cleaned_text.str.count(r"\?").astype(np.float32) / (char_count + 1.0)
    ).astype(np.float32)
    frame["feat_punctuation_rate"] = (
        cleaned_text.str.count(r"[!?,.;:\-]").astype(np.float32) / (char_count + 1.0)
    ).astype(np.float32)
    frame["feat_url_count"] = cleaned_text.str.count(r"\bURLTOKEN\b").astype(np.float32)
    frame["feat_user_mention_count"] = cleaned_text.str.count(r"\bUSERTOKEN\b").astype(
        np.float32
    )
    frame["feat_quote_count"] = cleaned_text.str.count(r"[\"']").astype(np.float32)

    identity_feature_columns = []
    for identity_name, identity_pattern in COMPILED_IDENTITY_PATTERNS.items():
        feature_name = f"feat_text_mentions_{identity_name}"
        frame[feature_name] = cleaned_text.str.contains(
            identity_pattern,
            na=False,
        ).astype(np.float32)
        identity_feature_columns.append(feature_name)

    frame["feat_text_identity_count"] = (
        frame[identity_feature_columns].sum(axis=1).astype(np.float32)
    )
    frame["feat_text_mentions_any_scored_identity"] = (
        frame["feat_text_identity_count"] > 0
    ).astype(np.float32)

    return identity_feature_columns


train_identity_feature_columns = engineer_text_features(train_df)
valid_identity_feature_columns = engineer_text_features(valid_df)
test_identity_feature_columns = engineer_text_features(test_df)

if train_identity_feature_columns != valid_identity_feature_columns:
    raise RuntimeError(
        "Validation identity feature schema differs from training schema."
    )
if train_identity_feature_columns != test_identity_feature_columns:
    raise RuntimeError("Test identity feature schema differs from training schema.")

continuous_feature_columns = [
    "feat_log_char_count",
    "feat_log_word_count",
    "feat_uppercase_ratio",
    "feat_exclamation_rate",
    "feat_question_rate",
    "feat_punctuation_rate",
    "feat_url_count",
    "feat_user_mention_count",
    "feat_quote_count",
]

train_continuous_values = train_df[continuous_feature_columns].to_numpy(
    dtype=np.float64
)
feature_mean = np.nanmean(train_continuous_values, axis=0)
feature_std = np.nanstd(train_continuous_values, axis=0)
feature_std = np.where(feature_std < 1e-6, 1.0, feature_std)

scaled_feature_columns = []
for column_index, feature_name in enumerate(continuous_feature_columns):
    scaled_name = f"{feature_name}_z"
    scaled_feature_columns.append(scaled_name)

    for frame in (train_df, valid_df, test_df):
        values = frame[feature_name].to_numpy(dtype=np.float64)
        values = np.nan_to_num(values, nan=feature_mean[column_index])
        frame[scaled_name] = (
            (values - feature_mean[column_index]) / feature_std[column_index]
        ).astype(np.float32)

model_feature_columns = (
    scaled_feature_columns
    + train_identity_feature_columns
    + ["feat_text_identity_count", "feat_text_mentions_any_scored_identity"]
)

train_targets = train_df["target"].astype(np.float32).to_numpy()
valid_targets = valid_df["target"].astype(np.float32).to_numpy()
train_binary_targets = (train_targets >= 0.5).astype(np.int64)
valid_binary_targets = (valid_targets >= 0.5).astype(np.int64)

validation_identity_columns = [
    identity_name
    for identity_name in SCORING_IDENTITY_PATTERNS
    if identity_name in valid_df.columns
]
training_identity_columns = [
    identity_name
    for identity_name in SCORING_IDENTITY_PATTERNS
    if identity_name in train_df.columns
]

if training_identity_columns != validation_identity_columns:
    raise RuntimeError(
        "Training and validation official identity annotation schemas differ."
    )

train_identity_masks = (
    train_df[training_identity_columns]
    .fillna(0.0)
    .ge(0.5)
    .to_numpy(dtype=np.float32)
)

train_model_inputs = train_df[["id", "model_text"] + model_feature_columns]
valid_model_inputs = valid_df[["id", "model_text"] + model_feature_columns]
test_model_inputs = test_df[["id", "model_text"] + model_feature_columns]

if train_model_inputs["id"].duplicated().any():
    raise ValueError(
        "Training IDs must be unique within the runtime training partition."
    )
if valid_model_inputs["id"].duplicated().any():
    raise ValueError(
        "Validation IDs must be unique within the runtime validation partition."
    )
if test_model_inputs["id"].duplicated().any():
    raise ValueError("Test IDs must be unique within the runtime test partition.")

feature_state = {
    "cleaning_version": "nfkc_html_url_user_whitespace_v1",
    "continuous_feature_columns": continuous_feature_columns,
    "scaled_feature_columns": scaled_feature_columns,
    "identity_feature_columns": train_identity_feature_columns,
    "model_feature_columns": model_feature_columns,
    "validation_identity_columns": validation_identity_columns,
    "feature_mean": feature_mean.astype(float).tolist(),
    "feature_std": feature_std.astype(float).tolist(),
    "identity_patterns": SCORING_IDENTITY_PATTERNS,
    "target_definition": (
        "target is retained as a fractional toxicity target; target >= 0.5 "
        "defines the official binary AUC class."
    ),
}

with open(
    os.path.join(WORKING_DIR, "data_processing_state.json"),
    "w",
    encoding="utf-8",
) as state_file:
    json.dump(feature_state, state_file, indent=2)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    num_labels=1,
    problem_type="regression",
    ignore_mismatched_sizes=True,
)

model.config.problem_type = "regression"
model.config.num_labels = 1

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

criterion = nn.BCEWithLogitsLoss(reduction="mean")


def _pairwise_softplus_loss(logits, positive_mask, negative_mask):
    positive_logits = logits[positive_mask]
    negative_logits = logits[negative_mask]

    if positive_logits.numel() == 0 or negative_logits.numel() == 0:
        return None

    # Every directed pair penalizes a negative score exceeding a positive score.
    return torch.nn.functional.softplus(
        negative_logits.unsqueeze(0) - positive_logits.unsqueeze(1)
    ).mean()


def composite_toxicity_loss(logits, targets, binary_labels, identity_masks):
    flat_logits = logits.reshape(-1)
    flat_targets = targets.reshape(-1)
    binary_labels = binary_labels.reshape(-1).detach().bool()
    identity_masks = (identity_masks.detach() >= 0.5)

    bce_loss = criterion(flat_logits, flat_targets)
    zero = flat_logits.sum() * 0.0

    subgroup_cells = []
    bpsn_cells = []
    bnsp_cells = []

    for identity_index in range(identity_masks.shape[1]):
        identity_member = identity_masks[:, identity_index]
        non_identity_member = ~identity_member

        subgroup_loss = _pairwise_softplus_loss(
            flat_logits,
            binary_labels & identity_member,
            (~binary_labels) & identity_member,
        )
        if subgroup_loss is not None:
            subgroup_cells.append(subgroup_loss)

        bpsn_loss = _pairwise_softplus_loss(
            flat_logits,
            binary_labels & non_identity_member,
            (~binary_labels) & identity_member,
        )
        if bpsn_loss is not None:
            bpsn_cells.append(bpsn_loss)

        bnsp_loss = _pairwise_softplus_loss(
            flat_logits,
            binary_labels & identity_member,
            (~binary_labels) & non_identity_member,
        )
        if bnsp_loss is not None:
            bnsp_cells.append(bnsp_loss)

    ranking_components = []
    if subgroup_cells:
        ranking_components.append(torch.stack(subgroup_cells).mean())
    if bpsn_cells:
        ranking_components.append(torch.stack(bpsn_cells).mean())
    if bnsp_cells:
        ranking_components.append(torch.stack(bnsp_cells).mean())

    overall_loss = _pairwise_softplus_loss(
        flat_logits,
        binary_labels,
        ~binary_labels,
    )
    if overall_loss is not None:
        ranking_components.append(overall_loss)

    ranking_loss = (
        torch.stack(ranking_components).mean()
        if ranking_components
        else zero
    )
    total_loss = 0.5 * bce_loss + 0.5 * ranking_loss
    return total_loss, bce_loss, ranking_loss

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
optimizer_parameter_groups = [
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and not any(term in name for term in no_decay_terms)
        ],
        "weight_decay": 0.01,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad and any(term in name for term in no_decay_terms)
        ],
        "weight_decay": 0.0,
    },
]

optimizer = AdamW(
    optimizer_parameter_groups,
    lr=1.5e-5,
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_enabled = device.type == "cuda"
scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


class ToxicityTextDataset(Dataset):
    def __init__(self, texts, targets=None, identity_masks=None):
        self.texts = np.asarray(texts, dtype=object)
        self.targets = (
            None if targets is None else np.asarray(targets, dtype=np.float32)
        )
        self.identity_masks = (
            None
            if identity_masks is None
            else np.asarray(identity_masks, dtype=np.float32)
        )

        if self.targets is not None and len(self.targets) != len(self.texts):
            raise ValueError("Texts and targets must have matching lengths.")
        if (
            self.identity_masks is not None
            and len(self.identity_masks) != len(self.texts)
        ):
            raise ValueError("Texts and identity masks must have matching lengths.")

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = str(self.texts[index])
        if self.targets is None:
            return text
        if self.identity_masks is None:
            return text, float(self.targets[index])
        return text, float(self.targets[index]), self.identity_masks[index]


def training_collate(batch):
    if len(batch[0]) == 2:
        texts, labels = zip(*batch)
        return list(texts), torch.tensor(labels, dtype=torch.float32)

    texts, labels, identity_masks = zip(*batch)
    return (
        list(texts),
        torch.tensor(labels, dtype=torch.float32),
        torch.as_tensor(np.asarray(identity_masks), dtype=torch.float32),
    )


def inference_collate(batch):
    return list(batch)


def encode_text_batch(texts):
    encoded = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )
    return {
        name: tensor.to(device, non_blocking=True)
        for name, tensor in encoded.items()
        if name != "token_type_ids"
    }


def predict_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)
    if positions.min() < 0 or positions.max() >= len(frame):
        raise IndexError(
            "Inference callback received an out-of-range positional index."
        )

    texts = frame["model_text"].iloc[positions].fillna("").astype(str).to_numpy()
    dataset = ToxicityTextDataset(texts)
    loader = DataLoader(
        dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True,
        collate_fn=inference_collate,
    )

    previous_training_mode = model.training
    model.eval()
    predictions = []

    with torch.inference_mode():
        for batch_texts in loader:
            model_inputs = encode_text_batch(batch_texts)
            with torch.cuda.amp.autocast(enabled=amp_enabled):
                logits = model(**model_inputs).logits.reshape(-1)
            probabilities = torch.sigmoid(logits).float().cpu().numpy()
            predictions.append(probabilities)

    model.train(previous_training_mode)
    return np.concatenate(predictions).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_df, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
        },
        os.path.join(directory, "model_state.pt"),
    )
    model.config.save_pretrained(directory)
    tokenizer.save_pretrained(directory)

    inference_state = {
        "max_sequence_length": MAX_SEQUENCE_LENGTH,
        "tokenizer_padding": "longest_pad_to_multiple_of_8",
        "tokenizer_truncation": True,
        "probability_postprocessing": "sigmoid(single_toxicity_logit)",
        "model_was_training": bool(model.training),
    }
    with open(
        os.path.join(directory, "inference_state.json"),
        "w",
        encoding="utf-8",
    ) as state_file:
        json.dump(inference_state, state_file, indent=2)

    processing_state_path = os.path.join(WORKING_DIR, "data_processing_state.json")
    if os.path.isfile(processing_state_path):
        shutil.copy2(
            processing_state_path,
            os.path.join(directory, "data_processing_state.json"),
        )


def load_checkpoint(directory):
    checkpoint_path = os.path.join(directory, "model_state.pt")
    if not os.path.isfile(checkpoint_path):
        raise FileNotFoundError(f"Checkpoint weights not found: {checkpoint_path}")

    try:
        checkpoint = torch.load(
            checkpoint_path,
            map_location=device,
            weights_only=True,
        )
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location=device)

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)

    state_path = os.path.join(directory, "inference_state.json")
    if os.path.isfile(state_path):
        with open(state_path, "r", encoding="utf-8") as state_file:
            saved_state = json.load(state_file)
        model.train(bool(saved_state.get("model_was_training", True)))


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

train_texts = train_df["model_text"].fillna("").astype(str).to_numpy()
train_soft_targets = train_targets.astype(np.float32, copy=False)
train_labels = train_binary_targets.astype(np.int64, copy=False)

positive_indices = np.flatnonzero(train_labels == 1)
negative_indices = np.flatnonzero(train_labels == 0)
selected_indices = np.arange(len(train_df), dtype=np.int64)

if len(positive_indices) == 0 or len(negative_indices) == 0:
    sampler_weights = np.ones(len(selected_indices), dtype=np.float64)
else:
    sampler_weights = np.where(
        train_labels == 1,
        1.0 / len(positive_indices),
        1.0 / len(negative_indices),
    ).astype(np.float64)

samples_per_epoch = (
    len(selected_indices)
    // (TRAIN_BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS)
    * (TRAIN_BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS)
)

if samples_per_epoch == 0:
    raise RuntimeError("The mixture-balanced training subset is too small to train.")

selected_texts = train_texts[selected_indices]
selected_targets = train_soft_targets[selected_indices]
selected_identity_masks = train_identity_masks[selected_indices]
training_dataset = ToxicityTextDataset(
    selected_texts,
    selected_targets,
    selected_identity_masks,
)

stop_training = False
total_optimizer_updates = 0

for epoch in range(MAX_EPOCHS):
    sampler_generator = torch.Generator()
    sampler_generator.manual_seed(RANDOM_SEED + epoch)

    epoch_sampler = WeightedRandomSampler(
        weights=torch.as_tensor(sampler_weights, dtype=torch.double),
        num_samples=samples_per_epoch,
        replacement=True,
        generator=sampler_generator,
    )

    train_loader = DataLoader(
        training_dataset,
        batch_size=TRAIN_BATCH_SIZE,
        sampler=epoch_sampler,
        drop_last=True,
        num_workers=NUM_WORKERS,
        pin_memory=True,
        collate_fn=training_collate,
        persistent_workers=False,
    )

    model.train()
    optimizer.zero_grad(set_to_none=True)

    running_loss = 0.0
    running_bce_loss = 0.0
    running_ranking_loss = 0.0
    processed_batches = 0
    epoch_updates = 0

    for batch_index, (
        batch_texts,
        batch_targets,
        batch_identity_masks,
    ) in enumerate(train_loader):
        model_inputs = encode_text_batch(batch_texts)
        batch_targets = batch_targets.to(device, non_blocking=True).reshape(-1, 1)
        batch_identity_masks = batch_identity_masks.to(
            device,
            non_blocking=True,
        )
        batch_binary_labels = batch_targets >= 0.5

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            logits = model(**model_inputs).logits.reshape(-1, 1)
            loss, bce_loss, ranking_loss = composite_toxicity_loss(
                logits,
                batch_targets,
                batch_binary_labels,
                batch_identity_masks,
            )

        if not torch.isfinite(loss):
            raise FloatingPointError("Non-finite training loss encountered.")

        scaler.scale(loss / GRADIENT_ACCUMULATION_STEPS).backward()

        running_loss += float(loss.detach().cpu())
        running_bce_loss += float(bce_loss.detach().cpu())
        running_ranking_loss += float(ranking_loss.detach().cpu())
        processed_batches += 1

        if (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)

            total_optimizer_updates += 1
            epoch_updates += 1

            stop_training = session.step()
            if stop_training:
                break

    mean_epoch_loss = running_loss / max(processed_batches, 1)
    mean_epoch_bce_loss = running_bce_loss / max(processed_batches, 1)
    mean_epoch_ranking_loss = running_ranking_loss / max(processed_batches, 1)
    print(
        f"epoch={epoch + 1} loss={mean_epoch_loss:.6f} "
        f"bce={mean_epoch_bce_loss:.6f} "
        f"ranking={mean_epoch_ranking_loss:.6f} "
        f"optimizer_updates={epoch_updates} stopped={int(stop_training)}"
    )

    if stop_training:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")