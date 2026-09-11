import html
import json
import os
import pickle
import re
import shutil
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

RANDOM_SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

EVALUATED_IDENTITY_COLUMNS = [
    "male",
    "female",
    "homosexual_gay_or_lesbian",
    "christian",
    "jewish",
    "muslim",
    "black",
    "white",
    "psychiatric_or_mental_illness",
]

TRAIN_COLUMNS = [
    "id",
    "target",
    "comment_text",
    "toxicity_annotator_count",
    "identity_annotator_count",
] + EVALUATED_IDENTITY_COLUMNS

MAX_SEQUENCE_LENGTH = 384
TRAIN_BATCH_SIZE = 8 if torch.cuda.is_available() else 2
INFERENCE_BATCH_SIZE = 16 if torch.cuda.is_available() else 2
GRADIENT_ACCUMULATION_STEPS = 2
MAX_EPOCHS = 3
NUM_WORKERS = 2

np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)

session = CandidateSession.from_env()

train_source = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=lambda column: column in TRAIN_COLUMNS,
    low_memory=False,
)
test_source = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_source, test_source)

url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]{}]+")
email_pattern = re.compile(r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
control_pattern = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
whitespace_pattern = re.compile(r"\s+")
long_repeat_pattern = re.compile(r"(.)\1{3,}")
word_pattern = re.compile(r"\S+")


def normalize_comment(value):
    if pd.isna(value):
        return ""

    text = html.unescape(str(value))
    text = unicodedata.normalize("NFKC", text)
    text = control_pattern.sub(" ", text)
    text = url_pattern.sub(" [URL] ", text)
    text = email_pattern.sub(" [EMAIL] ", text)
    text = whitespace_pattern.sub(" ", text).strip()

    if len(text) > 12000:
        text = text[:9000] + " [TRUNCATED] " + text[-3000:]

    return text


def add_text_features(frame, train_text_counts=None):
    frame = frame.copy()
    normalized = frame["comment_text"].map(normalize_comment)
    frame["model_text"] = normalized

    char_count = normalized.str.len().astype(np.float32)
    word_count = normalized.str.count(word_pattern).astype(np.float32)
    letter_count = normalized.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = normalized.str.count(r"[A-Z]").astype(np.float32)
    digit_count = normalized.str.count(r"\d").astype(np.float32)

    frame["log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["uppercase_ratio"] = np.divide(
        uppercase_count,
        np.maximum(letter_count, 1.0),
        dtype=np.float32,
    )
    frame["digit_ratio"] = np.divide(
        digit_count,
        np.maximum(char_count, 1.0),
        dtype=np.float32,
    )

    frame["exclamation_count"] = (
        normalized.str.count("!").clip(upper=100).astype(np.float32)
    )
    frame["question_count"] = (
        normalized.str.count(r"\?").clip(upper=100).astype(np.float32)
    )
    frame["newline_count"] = (
        frame["comment_text"]
        .fillna("")
        .astype(str)
        .str.count("\n")
        .clip(upper=100)
        .astype(np.float32)
    )
    frame["has_url"] = normalized.str.contains(r"\[URL\]", regex=True).astype(
        np.float32
    )
    frame["has_email"] = normalized.str.contains(r"\[EMAIL\]", regex=True).astype(
        np.float32
    )
    frame["has_long_character_repeat"] = normalized.str.contains(
        long_repeat_pattern,
        regex=True,
    ).astype(np.float32)
    frame["quote_count"] = (
        normalized.str.count(r"""["']""").clip(upper=100).astype(np.float32)
    )

    text_key = pd.util.hash_pandas_object(normalized, index=False).astype("uint64")
    if train_text_counts is None:
        train_text_counts = pd.Series(text_key).value_counts(dropna=False)

    frame["log_train_exact_text_frequency"] = np.log1p(
        pd.Series(text_key, index=frame.index)
        .map(train_text_counts)
        .fillna(0)
        .astype(np.float32)
    ).astype(np.float32)

    return frame, train_text_counts


train_df, text_frequency_counts = add_text_features(train_df)
valid_df, _ = add_text_features(valid_df, text_frequency_counts)
test_df, _ = add_text_features(test_df, text_frequency_counts)

train_df["target_soft"] = train_df["target"].clip(0.0, 1.0).astype(np.float32)
valid_df["target_soft"] = valid_df["target"].clip(0.0, 1.0).astype(np.float32)

EXACT_TEXT_PRIOR_SMOOTHING = 5.0
EXACT_TEXT_PRIOR_CLIP_BOUNDS = (1e-4, 1.0 - 1e-4)

exact_text_statistics = (
    train_df.groupby("model_text", sort=False)["target_soft"]
    .agg(["sum", "count"])
)
exact_text_sums = exact_text_statistics["sum"]
exact_text_counts = exact_text_statistics["count"]
exact_text_prior_lookup = {
    text: (float(total), int(count))
    for text, total, count in zip(
        exact_text_statistics.index,
        exact_text_sums,
        exact_text_counts,
    )
}
exact_text_prior_global_mean = float(train_df["target_soft"].mean())


def add_exact_text_prior(frame, leave_one_out=False):
    text_keys = frame["model_text"]
    group_sum = text_keys.map(exact_text_sums).fillna(0.0).to_numpy(
        dtype=np.float64,
        copy=False,
    )
    group_count = text_keys.map(exact_text_counts).fillna(0.0).to_numpy(
        dtype=np.float64,
        copy=False,
    )

    if leave_one_out:
        group_sum = group_sum - frame["target_soft"].to_numpy(
            dtype=np.float64,
            copy=False,
        )
        group_count = group_count - 1.0

    prior_mean = (
        group_sum + EXACT_TEXT_PRIOR_SMOOTHING * exact_text_prior_global_mean
    ) / (group_count + EXACT_TEXT_PRIOR_SMOOTHING)
    prior_mean = np.clip(prior_mean, *EXACT_TEXT_PRIOR_CLIP_BOUNDS)
    frame["exact_text_prior_logit"] = np.log(
        prior_mean / (1.0 - prior_mean)
    ).astype(np.float32)


add_exact_text_prior(train_df, leave_one_out=True)
add_exact_text_prior(valid_df)
add_exact_text_prior(test_df)

available_identity_columns = [
    column for column in EVALUATED_IDENTITY_COLUMNS if column in train_df.columns
]

for frame in (train_df, valid_df):
    identity_values = frame[available_identity_columns].fillna(0.0).astype(np.float32)
    frame["identity_mentioned"] = (identity_values.max(axis=1) >= 0.5).astype(
        np.float32
    )
    frame["identity_mention_strength"] = identity_values.max(axis=1).astype(np.float32)

for frame in (test_df,):
    frame["identity_mentioned"] = np.float32(0.0)
    frame["identity_mention_strength"] = np.float32(0.0)

for frame in (train_df, valid_df, test_df):
    if "toxicity_annotator_count" in frame.columns:
        frame["log_toxicity_annotator_count"] = np.log1p(
            frame["toxicity_annotator_count"].fillna(0).astype(np.float32)
        ).astype(np.float32)
    else:
        frame["log_toxicity_annotator_count"] = np.float32(0.0)

    if "identity_annotator_count" in frame.columns:
        frame["log_identity_annotator_count"] = np.log1p(
            frame["identity_annotator_count"].fillna(0).astype(np.float32)
        ).astype(np.float32)
    else:
        frame["log_identity_annotator_count"] = np.float32(0.0)

numeric_feature_columns = [
    "log_char_count",
    "log_word_count",
    "uppercase_ratio",
    "digit_ratio",
    "exclamation_count",
    "question_count",
    "newline_count",
    "has_url",
    "has_email",
    "has_long_character_repeat",
    "quote_count",
    "log_train_exact_text_frequency",
    "identity_mentioned",
    "identity_mention_strength",
    "log_toxicity_annotator_count",
    "log_identity_annotator_count",
]

raw_train_identity_mentioned = train_df["identity_mentioned"].to_numpy(
    dtype=np.float32,
    copy=True,
)

numeric_scaler = StandardScaler()
train_df[numeric_feature_columns] = numeric_scaler.fit_transform(
    train_df[numeric_feature_columns].fillna(0.0)
).astype(np.float32)

valid_df[numeric_feature_columns] = numeric_scaler.transform(
    valid_df[numeric_feature_columns].fillna(0.0)
).astype(np.float32)

test_df[numeric_feature_columns] = numeric_scaler.transform(
    test_df[numeric_feature_columns].fillna(0.0)
).astype(np.float32)

train_df["target_binary"] = (train_df["target_soft"] >= 0.5).astype(np.int8)
valid_df["target_binary"] = (valid_df["target_soft"] >= 0.5).astype(np.int8)

identity_memberships = (
    train_df[available_identity_columns]
    .fillna(0.0)
    .to_numpy(dtype=np.float32)
    >= 0.5
)
is_toxic = train_df["target_binary"].to_numpy(dtype=bool)
has_evaluated_identity = identity_memberships.any(axis=1)

fairness_sample_weight = np.ones(len(train_df), dtype=np.float32)
for identity_membership in identity_memberships.T:
    fairness_sample_weight[identity_membership & ~is_toxic] += 3.0
    fairness_sample_weight[identity_membership & is_toxic] += 1.5

fairness_sample_weight[~has_evaluated_identity & is_toxic] += 0.5
fairness_sample_weight /= fairness_sample_weight.mean()

train_df["fairness_sample_weight"] = fairness_sample_weight
valid_df["fairness_sample_weight"] = np.ones(len(valid_df), dtype=np.float32)

feature_state = {
    "random_seed": RANDOM_SEED,
    "text_column": "model_text",
    "target_column": "target_soft",
    "binary_target_column": "target_binary",
    "sample_weight_column": "fairness_sample_weight",
    "numeric_feature_columns": numeric_feature_columns,
    "identity_columns": available_identity_columns,
    "text_frequency_counts": text_frequency_counts.to_dict(),
    "exact_text_prior_lookup": exact_text_prior_lookup,
    "exact_text_prior_global_mean": exact_text_prior_global_mean,
    "exact_text_prior_smoothing": EXACT_TEXT_PRIOR_SMOOTHING,
    "exact_text_prior_clip_bounds": EXACT_TEXT_PRIOR_CLIP_BOUNDS,
    "exact_text_prior_keying": {
        "key_column": "model_text",
        "normalization": "normalize_comment",
        "leave_one_out_for_training": True,
    },
    "numeric_scaler": numeric_scaler,
}

with open(WORKING_DIR / "feature_state.pkl", "wb") as feature_file:
    pickle.dump(feature_state, feature_file, protocol=pickle.HIGHEST_PROTOCOL)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)


class BiasAwareModernBert(nn.Module):
    def __init__(self, sequence_classifier):
        super().__init__()
        self.sequence_classifier = sequence_classifier
        self.prior_logit_scale = nn.Parameter(torch.zeros(()))

    def forward(self, input_ids, attention_mask=None, exact_text_prior_logit=None):
        outputs = self.sequence_classifier(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        class_logits = outputs.logits

        if class_logits.shape[-1] == 1:
            base_text_logit = class_logits.squeeze(-1)
        else:
            base_text_logit = class_logits[:, 1] - class_logits[:, 0]

        if exact_text_prior_logit is None:
            return base_text_logit

        exact_text_prior_logit = exact_text_prior_logit.to(
            device=base_text_logit.device,
            dtype=base_text_logit.dtype,
        )
        return base_text_logit + self.prior_logit_scale * exact_text_prior_logit


class FairnessWeightedSoftBCELoss(nn.Module):
    def forward(self, logits, targets, sample_weight=None):
        targets = targets.to(dtype=logits.dtype).clamp_(0.0, 1.0)
        per_example_loss = F.binary_cross_entropy_with_logits(
            logits,
            targets,
            reduction="none",
        )

        if sample_weight is None:
            return per_example_loss.mean()

        sample_weight = sample_weight.to(
            device=logits.device,
            dtype=logits.dtype,
        ).clamp_min_(0.0)

        return (per_example_loss * sample_weight).sum() / sample_weight.sum().clamp_min(
            1.0
        )


pretrained_classifier = model

for parameter in pretrained_classifier.parameters():
    parameter.requires_grad = False

encoder = getattr(pretrained_classifier, "model", None)
encoder_layers = list(getattr(encoder, "layers", []))
num_trainable_encoder_layers = min(6, len(encoder_layers))

for layer in encoder_layers[-num_trainable_encoder_layers:]:
    for parameter in layer.parameters():
        parameter.requires_grad = True

head_modules = []
for head_name in ("head", "classifier", "score"):
    head_module = getattr(pretrained_classifier, head_name, None)
    if isinstance(head_module, nn.Module):
        head_modules.append(head_module)
        for parameter in head_module.parameters():
            parameter.requires_grad = True

model = BiasAwareModernBert(pretrained_classifier)
criterion = FairnessWeightedSoftBCELoss()

head_parameter_ids = {
    id(parameter)
    for head_module in head_modules
    for parameter in head_module.parameters()
    if parameter.requires_grad
}
head_parameter_ids.add(id(model.prior_logit_scale))

encoder_decay_params = []
encoder_no_decay_params = []
head_decay_params = []
head_no_decay_params = []

for name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    no_decay = (
        parameter.ndim <= 1
        or name.endswith(".bias")
        or "norm" in name.lower()
        or "layernorm" in name.lower()
    )
    is_head_parameter = id(parameter) in head_parameter_ids

    if is_head_parameter and no_decay:
        head_no_decay_params.append(parameter)
    elif is_head_parameter:
        head_decay_params.append(parameter)
    elif no_decay:
        encoder_no_decay_params.append(parameter)
    else:
        encoder_decay_params.append(parameter)

optimizer = AdamW(
    [
        {
            "params": encoder_decay_params,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": encoder_no_decay_params,
            "lr": 1.5e-5,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_params,
            "lr": 5.0e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_params,
            "lr": 5.0e-5,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"
pin_memory = device.type == "cuda"

if use_amp:
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.set_float32_matmul_precision("high")

model.to(device)
criterion.to(device)


class ToxicityTextDataset(Dataset):
    def __init__(self, frame, include_labels=False, positional_indices=None):
        if positional_indices is None:
            positional_indices = np.arange(len(frame), dtype=np.int64)
        else:
            positional_indices = np.asarray(positional_indices, dtype=np.int64)

        selected = frame.iloc[positional_indices]
        self.texts = selected["model_text"].fillna("").astype(str).to_numpy(copy=False)
        self.include_labels = include_labels
        self.prior_logits = selected["exact_text_prior_logit"].to_numpy(
            dtype=np.float32,
            copy=True,
        )

        if include_labels:
            self.targets = selected["target_soft"].to_numpy(dtype=np.float32, copy=True)
            self.weights = selected["fairness_sample_weight"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.include_labels:
            return (
                self.texts[index],
                self.targets[index],
                self.weights[index],
                self.prior_logits[index],
            )
        return self.texts[index], self.prior_logits[index]


def training_collate(batch):
    texts, targets, weights, prior_logits = zip(*batch)
    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )
    encoded["exact_text_prior_logit"] = torch.as_tensor(
        prior_logits,
        dtype=torch.float32,
    )
    return (
        encoded,
        torch.as_tensor(targets, dtype=torch.float32),
        torch.as_tensor(weights, dtype=torch.float32),
    )


def inference_collate(batch):
    texts, prior_logits = zip(*batch)
    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )
    encoded["exact_text_prior_logit"] = torch.as_tensor(
        prior_logits,
        dtype=torch.float32,
    )
    return encoded


def make_inference_loader(frame, positional_indices):
    dataset = ToxicityTextDataset(
        frame=frame,
        include_labels=False,
        positional_indices=positional_indices,
    )
    return DataLoader(
        dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=pin_memory,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=inference_collate,
    )


def predict_frame_positions(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    previous_training_state = model.training
    model.eval()
    predictions = []

    try:
        loader = make_inference_loader(frame, positional_indices)

        with torch.inference_mode():
            for encoded in loader:
                encoded = {
                    name: tensor.to(device, non_blocking=pin_memory)
                    for name, tensor in encoded.items()
                }

                with torch.cuda.amp.autocast(enabled=use_amp):
                    logits = model(**encoded)

                probabilities = torch.sigmoid(logits).float().cpu().numpy()
                predictions.append(probabilities)

        return np.clip(
            np.concatenate(predictions, axis=0),
            1e-6,
            1.0 - 1e-6,
        ).astype(np.float64, copy=False)
    finally:
        model.train(previous_training_state)


def predict_validation(positional_indices):
    return predict_frame_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_df, positional_indices)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    trainable_state = {
        name: parameter.detach().cpu()
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    }

    torch.save(
        {
            "trainable_state_dict": trainable_state,
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
        },
        directory / "trainable_model_state.pt",
    )

    model.sequence_classifier.config.save_pretrained(directory / "model_config")
    tokenizer.save_pretrained(directory / "tokenizer")

    feature_state_source = WORKING_DIR / "feature_state.pkl"
    if feature_state_source.exists():
        shutil.copy2(feature_state_source, directory / "feature_state.pkl")

    with open(directory / "inference_state.json", "w", encoding="utf-8") as state_file:
        json.dump(
            {
                "text_column": "model_text",
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "probability_transform": "sigmoid",
                "model_class": model.__class__.__name__,
            },
            state_file,
            indent=2,
            sort_keys=True,
        )


def load_checkpoint(directory):
    directory = Path(directory)
    checkpoint = torch.load(
        directory / "trainable_model_state.pt",
        map_location=device,
        weights_only=False,
    )
    model.load_state_dict(checkpoint["trainable_state_dict"], strict=False)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

train_dataset = ToxicityTextDataset(train_df, include_labels=True)
train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=True,
    num_workers=NUM_WORKERS,
    pin_memory=pin_memory,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=training_collate,
)

scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_requested = False
optimizer_updates = 0

for epoch in range(MAX_EPOCHS):
    model.train()
    running_loss = 0.0
    observed_batches = 0
    epoch_updates = 0

    for batch_index, (encoded, targets, sample_weights) in enumerate(train_loader):
        encoded = {
            name: tensor.to(device, non_blocking=pin_memory)
            for name, tensor in encoded.items()
        }
        targets = targets.to(device, non_blocking=pin_memory)
        sample_weights = sample_weights.to(device, non_blocking=pin_memory)

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(**encoded)
            unscaled_loss = criterion(
                logits=logits,
                targets=targets,
                sample_weight=sample_weights,
            )
            loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(loss).backward()

        running_loss += float(unscaled_loss.detach().cpu())
        observed_batches += 1

        if (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS != 0:
            continue

        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        optimizer_updates += 1
        epoch_updates += 1
        stop_requested = session.step()

        if stop_requested:
            break

    mean_loss = running_loss / max(observed_batches, 1)
    print(
        f"epoch={epoch + 1} updates={epoch_updates} "
        f"total_updates={optimizer_updates} loss={mean_loss:.6f}"
    )

    if stop_requested:
        break

del train_loader

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")