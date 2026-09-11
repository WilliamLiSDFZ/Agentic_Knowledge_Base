import os
import re
import html
import json
import math
import random
import pickle
import shutil
import unicodedata

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession


RANDOM_SEED = 2025
INPUT_DIR = "./input"
WORKING_DIR = "./working"
os.makedirs(WORKING_DIR, exist_ok=True)

EVALUATED_IDENTITIES = [
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

AUXILIARY_TARGETS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

IDENTITY_PATTERN_SOURCES = {
    "male": (
        r"\b(?:male|males|man|men|boy|boys|father|fathers|son|sons|husband|husbands|"
        r"he|him|his)\b"
    ),
    "female": (
        r"\b(?:female|females|woman|women|girl|girls|mother|mothers|daughter|daughters|"
        r"wife|wives|she|her|hers)\b"
    ),
    "homosexual_gay_or_lesbian": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|queer|queers|"
        r"lgbt|lgbtq|lgbtqia|same[\s-]?sex)\b"
    ),
    "christian": (
        r"\b(?:christian|christians|christianity|catholic|catholics|"
        r"protestant|protestants)\b"
    ),
    "jewish": r"\b(?:jew|jews|jewish|judaism|zionist|zionists)\b",
    "muslim": r"\b(?:muslim|muslims|islam|islamic|islamist|islamists)\b",
    "black": r"\b(?:black|blacks|african[\s-]?american|african[\s-]?americans)\b",
    "white": r"\b(?:white|whites|caucasian|caucasians)\b",
    "psychiatric_or_mental_illness": (
        r"\b(?:mental[\s-]?illness|mental[\s-]?health|mentally[\s-]?ill|psychiatric|"
        r"depression|depressed|schizophren(?:ia|ic)|bipolar|autis(?:m|tic)|"
        r"anxiety|ptsd|disabled)\b"
    ),
}
IDENTITY_PATTERNS = {
    name: re.compile(pattern, flags=re.IGNORECASE)
    for name, pattern in IDENTITY_PATTERN_SOURCES.items()
}

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|ftp://|www\.)[^\s<>()]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b")
USER_PATTERN = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,}")
CONTROL_PATTERN = re.compile(r"[\r\n\t]+")
WHITESPACE_PATTERN = re.compile(r"\s+")
REPEATED_PUNCT_PATTERN = re.compile(r"([!?.,])\1{3,}")
REPEATED_CHAR_PATTERN = re.compile(r"([A-Za-z])\1{5,}", flags=re.IGNORECASE)

MAX_LENGTH = 192
TRAIN_BATCH_SIZE = 8 if torch.cuda.is_available() else 2
INFERENCE_BATCH_SIZE = 32 if torch.cuda.is_available() else 4
GRADIENT_ACCUMULATION_STEPS = 2
NUM_WORKERS = 2
NUM_AUXILIARY_TARGETS = len(AUXILIARY_TARGETS)
NUM_MODEL_OUTPUTS = 1 + NUM_AUXILIARY_TARGETS
PAIRWISE_BIAS_WEIGHT = 0.22
AUXILIARY_LOSS_WEIGHT = 0.16


def normalize_comment_text(value):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text) if "&" in text else text
    text = URL_PATTERN.sub(" URLTOKEN ", text)
    text = EMAIL_PATTERN.sub(" EMAILADDRESS ", text)
    text = USER_PATTERN.sub(" USERMENTION ", text)
    text = CONTROL_PATTERN.sub(" NEWLINE ", text)
    text = REPEATED_PUNCT_PATTERN.sub(r"\1\1\1", text)
    text = REPEATED_CHAR_PATTERN.sub(r"\1\1\1", text)
    return WHITESPACE_PATTERN.sub(" ", text).strip()


def build_identity_lexical_mask(texts):
    normalized_lower = texts.fillna("").astype(str).str.lower()
    mask = np.zeros(len(normalized_lower), dtype=np.uint16)

    for bit_index, identity_name in enumerate(EVALUATED_IDENTITIES):
        mentioned = normalized_lower.str.contains(
            IDENTITY_PATTERNS[identity_name],
            na=False,
            regex=True,
        ).to_numpy(dtype=bool)
        mask |= mentioned.astype(np.uint16) << np.uint16(bit_index)

    return mask


def counterfactualize_identity_mentions(text):
    transformed = str(text)
    for pattern in IDENTITY_PATTERNS.values():
        transformed = pattern.sub(" IDENTITYTOKEN ", transformed)
    return WHITESPACE_PATTERN.sub(" ", transformed).strip()


def build_raw_style_features(texts):
    series = texts.fillna("").astype(str)
    char_count = series.str.len().to_numpy(dtype=np.float32)
    safe_char_count = np.maximum(char_count, 1.0)

    word_count = series.str.count(r"\S+").to_numpy(dtype=np.float32)
    upper_count = series.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = series.str.count(r"\d").to_numpy(dtype=np.float32)
    exclamation_count = series.str.count("!").to_numpy(dtype=np.float32)
    question_count = series.str.count(r"\?").to_numpy(dtype=np.float32)
    newline_token_count = series.str.count(r"\bNEWLINE\b").to_numpy(dtype=np.float32)
    url_token_count = series.str.count(r"\bURLTOKEN\b").to_numpy(dtype=np.float32)
    repeated_punct_count = series.str.count(r"[!?]{2,}|\.{3,}").to_numpy(
        dtype=np.float32
    )
    non_ascii_count = series.map(
        lambda x: sum(ord(character) > 127 for character in x)
    ).to_numpy(dtype=np.float32)

    return np.column_stack(
        [
            np.log1p(char_count),
            np.log1p(word_count),
            upper_count / safe_char_count,
            digit_count / safe_char_count,
            np.log1p(exclamation_count),
            np.log1p(question_count),
            np.log1p(newline_token_count),
            np.log1p(url_token_count),
            np.log1p(repeated_punct_count),
            non_ascii_count / safe_char_count,
        ]
    ).astype(np.float32)


def prepare_text_split(frame):
    prepared = frame.copy()
    prepared["comment_text"] = prepared["comment_text"].fillna("").astype(str)
    prepared["model_text"] = prepared["comment_text"].map(normalize_comment_text)
    prepared["identity_lexical_mask"] = build_identity_lexical_mask(
        prepared["model_text"]
    )
    prepared["counterfactual_eligible"] = (
        prepared["identity_lexical_mask"].to_numpy(dtype=np.uint16) > 0
    ).astype(np.int8)
    return prepared


def derive_bias_aware_training_weights(train_frame):
    target_binary = train_frame["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
    identity_values = train_frame.reindex(columns=EVALUATED_IDENTITIES).to_numpy(
        dtype=np.float32
    )
    membership = np.isfinite(identity_values) & (identity_values >= 0.5)

    stratum_counts = np.zeros((len(EVALUATED_IDENTITIES), 2), dtype=np.int64)
    for identity_index in range(len(EVALUATED_IDENTITIES)):
        for target_value in (0, 1):
            stratum_counts[identity_index, target_value] = int(
                np.sum(
                    membership[:, identity_index]
                    & (target_binary == bool(target_value))
                )
            )

    nonzero_counts = stratum_counts[stratum_counts > 0]
    reference_count = float(np.median(nonzero_counts)) if len(nonzero_counts) else 1.0
    stratum_boosts = np.ones_like(stratum_counts, dtype=np.float32)

    for identity_index in range(len(EVALUATED_IDENTITIES)):
        for target_value in (0, 1):
            count = max(int(stratum_counts[identity_index, target_value]), 1)
            scarcity = np.sqrt(reference_count / count)
            stratum_boosts[identity_index, target_value] = np.clip(scarcity, 1.0, 3.0)

    row_boost = np.ones(len(train_frame), dtype=np.float32)
    for identity_index in range(len(EVALUATED_IDENTITIES)):
        applicable = membership[:, identity_index]
        class_boost = stratum_boosts[identity_index, target_binary.astype(np.int8)]
        row_boost[applicable] = np.maximum(
            row_boost[applicable],
            class_boost[applicable],
        )

    sample_weight = 1.0 + 0.70 * (row_boost - 1.0)
    sample_weight = np.clip(sample_weight, 1.0, 2.4).astype(np.float32)

    return (
        target_binary.astype(np.float32),
        sample_weight,
        stratum_counts,
        stratum_boosts,
    )


random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

session = CandidateSession.from_env()

train_header = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    nrows=0,
).columns.tolist()

required_train_columns = {
    "id",
    "target",
    "comment_text",
    "toxicity_annotator_count",
    *EVALUATED_IDENTITIES,
    *AUXILIARY_TARGETS,
}
train_usecols = [column for column in train_header if column in required_train_columns]

raw_train_df = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    usecols=train_usecols,
    low_memory=False,
)
raw_test_df = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df

train_df = train_df.reset_index(drop=True)
valid_df = valid_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

train_df = prepare_text_split(train_df)
valid_df = prepare_text_split(valid_df)
test_df = prepare_text_split(test_df)

for identity_name in EVALUATED_IDENTITIES:
    if identity_name not in train_df.columns:
        train_df[identity_name] = np.nan
    if identity_name not in valid_df.columns:
        valid_df[identity_name] = np.nan

for auxiliary_name in AUXILIARY_TARGETS:
    if auxiliary_name not in train_df.columns:
        train_df[auxiliary_name] = np.nan
    if auxiliary_name not in valid_df.columns:
        valid_df[auxiliary_name] = np.nan

style_scaler = StandardScaler(copy=True)
style_feature_matrix_train = style_scaler.fit_transform(
    build_raw_style_features(train_df["model_text"])
).astype(np.float32)
style_feature_matrix_valid = style_scaler.transform(
    build_raw_style_features(valid_df["model_text"])
).astype(np.float32)
style_feature_matrix_test = style_scaler.transform(
    build_raw_style_features(test_df["model_text"])
).astype(np.float32)

np.save(
    os.path.join(WORKING_DIR, "style_features_train.npy"), style_feature_matrix_train
)
np.save(
    os.path.join(WORKING_DIR, "style_features_valid.npy"), style_feature_matrix_valid
)
np.save(os.path.join(WORKING_DIR, "style_features_test.npy"), style_feature_matrix_test)

(
    y_train_binary,
    training_sample_weight,
    identity_stratum_counts,
    identity_stratum_boosts,
) = derive_bias_aware_training_weights(train_df)

y_train_soft = train_df["target"].fillna(0.0).to_numpy(dtype=np.float32)
identity_targets_train = train_df[EVALUATED_IDENTITIES].to_numpy(dtype=np.float32)
auxiliary_targets_train = train_df[AUXILIARY_TARGETS].to_numpy(dtype=np.float32)

preprocessing_state = {
    "style_scaler": style_scaler,
    "evaluated_identities": EVALUATED_IDENTITIES,
    "auxiliary_targets": AUXILIARY_TARGETS,
    "identity_pattern_sources": IDENTITY_PATTERN_SOURCES,
    "identity_stratum_counts": identity_stratum_counts,
    "identity_stratum_boosts": identity_stratum_boosts,
    "text_normalization_version": "nfkc_html_url_user_repeat_v1",
}
with open(os.path.join(WORKING_DIR, "preprocessing_state.pkl"), "wb") as state_file:
    pickle.dump(preprocessing_state, state_file, protocol=pickle.HIGHEST_PROTOCOL)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)

classifier_input_dim = model.classifier.in_features
model.classifier = torch.nn.Linear(classifier_input_dim, NUM_MODEL_OUTPUTS)
torch.nn.init.normal_(model.classifier.weight, mean=0.0, std=0.02)
torch.nn.init.zeros_(model.classifier.bias)
model.config.num_labels = NUM_MODEL_OUTPUTS
model.num_labels = NUM_MODEL_OUTPUTS
model.config.id2label = {
    0: "toxicity",
    1: "severe_toxicity",
    2: "obscene",
    3: "threat",
    4: "insult",
    5: "identity_attack",
    6: "sexual_explicit",
}
model.config.label2id = {label: index for index, label in model.config.id2label.items()}
model.gradient_checkpointing_enable()
if hasattr(model.config, "use_cache"):
    model.config.use_cache = False
model.to(device)


class ToxicityTrainingDataset(Dataset):
    def __init__(
        self,
        texts,
        soft_targets,
        binary_targets,
        sample_weights,
        identity_targets,
        auxiliary_targets,
    ):
        self.texts = texts.fillna("").astype(str).tolist()
        self.soft_targets = np.asarray(soft_targets, dtype=np.float32)
        self.binary_targets = np.asarray(binary_targets, dtype=np.float32)
        self.sample_weights = np.asarray(sample_weights, dtype=np.float32)
        self.identity_targets = np.asarray(identity_targets, dtype=np.float32)
        self.auxiliary_targets = np.asarray(auxiliary_targets, dtype=np.float32)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.soft_targets[index],
            self.binary_targets[index],
            self.sample_weights[index],
            self.identity_targets[index],
            self.auxiliary_targets[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts):
        self.texts = list(texts)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index]


def training_collate(batch):
    texts, soft_y, binary_y, weights, identities, auxiliary = zip(*batch)
    encoded = tokenizer(
        list(texts),
        max_length=MAX_LENGTH,
        truncation=True,
        padding=True,
        return_tensors="pt",
    )
    return (
        encoded,
        torch.tensor(soft_y, dtype=torch.float32),
        torch.tensor(binary_y, dtype=torch.float32),
        torch.tensor(weights, dtype=torch.float32),
        torch.tensor(np.asarray(identities), dtype=torch.float32),
        torch.tensor(np.asarray(auxiliary), dtype=torch.float32),
    )


def inference_collate(batch):
    return tokenizer(
        list(batch),
        max_length=MAX_LENGTH,
        truncation=True,
        padding=True,
        return_tensors="pt",
    )


def paired_logistic_ranking_loss(high_scores, low_scores):
    pair_count = min(high_scores.numel(), low_scores.numel())
    if pair_count == 0:
        return None

    high_indices = (
        torch.arange(pair_count, device=high_scores.device) % high_scores.numel()
    )
    low_indices = (
        torch.arange(pair_count, device=low_scores.device) % low_scores.numel()
    )
    margins = high_scores[high_indices] - low_scores[low_indices]
    return F.softplus(-margins).mean()


def official_bias_surrogate(toxicity_logits, binary_targets, identity_targets):
    finite_identity = torch.isfinite(identity_targets)
    subgroup_membership = (
        torch.nan_to_num(identity_targets, nan=0.0) >= 0.5
    ) & finite_identity
    is_positive = binary_targets >= 0.5
    losses = []

    for identity_index in range(subgroup_membership.shape[1]):
        member = subgroup_membership[:, identity_index]
        known = finite_identity[:, identity_index]
        background = known & ~member

        subgroup_positive = toxicity_logits[member & is_positive]
        subgroup_negative = toxicity_logits[member & ~is_positive]
        background_positive = toxicity_logits[background & is_positive]
        background_negative = toxicity_logits[background & ~is_positive]

        for loss_value in (
            paired_logistic_ranking_loss(subgroup_positive, subgroup_negative),
            paired_logistic_ranking_loss(background_positive, subgroup_negative),
            paired_logistic_ranking_loss(subgroup_positive, background_negative),
        ):
            if loss_value is not None:
                losses.append(loss_value)

    if not losses:
        return toxicity_logits.new_zeros(())
    return torch.stack(losses).mean()


def compute_training_loss(
    logits,
    soft_targets,
    binary_targets,
    sample_weights,
    identity_targets,
    auxiliary_targets,
):
    toxicity_logits = logits[:, 0]
    toxicity_bce = F.binary_cross_entropy_with_logits(
        toxicity_logits,
        soft_targets,
        reduction="none",
    )
    toxicity_bce = (
        toxicity_bce * sample_weights
    ).sum() / sample_weights.sum().clamp_min(1.0)

    auxiliary_logits = logits[:, 1:]
    auxiliary_known = torch.isfinite(auxiliary_targets)
    safe_auxiliary_targets = torch.nan_to_num(auxiliary_targets, nan=0.0)
    auxiliary_element_loss = F.binary_cross_entropy_with_logits(
        auxiliary_logits,
        safe_auxiliary_targets,
        reduction="none",
    )
    auxiliary_loss = (
        auxiliary_element_loss * auxiliary_known.float()
    ).sum() / auxiliary_known.float().sum().clamp_min(1.0)

    ranking_loss = official_bias_surrogate(
        toxicity_logits,
        binary_targets,
        identity_targets,
    )
    total_loss = (
        toxicity_bce
        + AUXILIARY_LOSS_WEIGHT * auxiliary_loss
        + PAIRWISE_BIAS_WEIGHT * ranking_loss
    )
    return total_loss


training_dataset = ToxicityTrainingDataset(
    texts=train_df["model_text"],
    soft_targets=y_train_soft,
    binary_targets=y_train_binary,
    sample_weights=training_sample_weight,
    identity_targets=identity_targets_train,
    auxiliary_targets=auxiliary_targets_train,
)

known_identity = np.isfinite(identity_targets_train).any(axis=1)
identity_mentioned = np.nan_to_num(identity_targets_train, nan=0.0).max(axis=1) >= 0.5
sampler_weights = np.asarray(training_sample_weight, dtype=np.float64).copy()
sampler_weights[known_identity & identity_mentioned] *= 2.0
sampler_weights[known_identity & identity_mentioned & (y_train_binary < 0.5)] *= 1.35
sampler_weights = np.clip(sampler_weights, 0.05, 8.0)

training_sampler = WeightedRandomSampler(
    weights=torch.as_tensor(sampler_weights, dtype=torch.double),
    num_samples=len(training_dataset),
    replacement=True,
    generator=torch.Generator().manual_seed(RANDOM_SEED),
)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    sampler=training_sampler,
    num_workers=NUM_WORKERS,
    pin_memory=amp_enabled,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=training_collate,
    drop_last=True,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")
parameter_groups = []
for is_head, base_lr in ((False, 1.25e-5), (True, 8.0e-5)):
    for use_weight_decay in (True, False):
        selected_parameters = []
        for parameter_name, parameter in model.named_parameters():
            if not parameter.requires_grad:
                continue
            belongs_to_head = parameter_name.startswith("classifier.")
            if belongs_to_head != is_head:
                continue
            has_no_decay = any(term in parameter_name for term in no_decay_terms)
            if has_no_decay != (not use_weight_decay):
                continue
            selected_parameters.append(parameter)

        if selected_parameters:
            parameter_groups.append(
                {
                    "params": selected_parameters,
                    "lr": base_lr,
                    "weight_decay": 0.01 if use_weight_decay else 0.0,
                }
            )

optimizer = AdamW(parameter_groups, betas=(0.9, 0.999), eps=1e-8)
WARMUP_UPDATES = 300
PLANNED_UPDATES = max(
    3000,
    math.ceil(len(training_loader) / GRADIENT_ACCUMULATION_STEPS),
)


def learning_rate_multiplier(update_index):
    if update_index < WARMUP_UPDATES:
        return float(update_index + 1) / float(max(1, WARMUP_UPDATES))
    remaining = max(1, PLANNED_UPDATES - WARMUP_UPDATES)
    progress = min(1.0, (update_index - WARMUP_UPDATES) / remaining)
    return max(0.08, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


def predict_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64)
    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    selected_texts = frame["model_text"].iloc[positions].fillna("").astype(str).tolist()
    loader = DataLoader(
        ToxicityInferenceDataset(selected_texts),
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=amp_enabled,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=inference_collate,
    )

    was_training = model.training
    model.eval()
    prediction_chunks = []

    with torch.inference_mode():
        for encoded in loader:
            encoded = {
                name: value.to(device, non_blocking=True)
                for name, value in encoded.items()
            }
            with torch.cuda.amp.autocast(enabled=amp_enabled):
                logits = model(**encoded).logits[:, 0]
            prediction_chunks.append(torch.sigmoid(logits).float().cpu().numpy())

    if was_training:
        model.train()

    return np.concatenate(prediction_chunks).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_df, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_length": MAX_LENGTH,
            "num_outputs": NUM_MODEL_OUTPUTS,
            "identity_ranking_weight": PAIRWISE_BIAS_WEIGHT,
            "auxiliary_loss_weight": AUXILIARY_LOSS_WEIGHT,
        },
        os.path.join(directory, "model_state.pt"),
    )
    model.config.save_pretrained(directory)
    tokenizer.save_pretrained(directory)

    with open(
        os.path.join(directory, "preprocessing_state.pkl"),
        "wb",
    ) as state_file:
        pickle.dump(preprocessing_state, state_file, protocol=pickle.HIGHEST_PROTOCOL)

    with open(
        os.path.join(directory, "inference_state.json"),
        "w",
        encoding="utf-8",
    ) as state_file:
        json.dump(
            {
                "max_length": MAX_LENGTH,
                "output_probability": "sigmoid(toxicity_logit)",
                "text_column": "model_text",
            },
            state_file,
        )


def load_checkpoint(directory):
    checkpoint = torch.load(
        os.path.join(directory, "model_state.pt"),
        map_location=device,
    )
    if int(checkpoint["num_outputs"]) != NUM_MODEL_OUTPUTS:
        raise RuntimeError("Checkpoint output schema does not match the active model.")

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)
session.start_training(train_df["id"].astype(str).tolist())

model.train()
optimizer.zero_grad(set_to_none=True)

completed_updates = 0
epoch_index = 0
stop_training = False
accumulation_steps = int(GRADIENT_ACCUMULATION_STEPS)

while not stop_training:
    epoch_index += 1
    epoch_loss_sum = 0.0
    epoch_microbatches = 0
    loader_length = len(training_loader)

    for batch_index, batch in enumerate(training_loader):
        (
            encoded,
            soft_targets,
            binary_targets,
            sample_weights,
            identity_targets,
            auxiliary_targets,
        ) = batch

        encoded = {
            name: value.to(device, non_blocking=True) for name, value in encoded.items()
        }
        soft_targets = soft_targets.to(device, non_blocking=True)
        binary_targets = binary_targets.to(device, non_blocking=True)
        sample_weights = sample_weights.to(device, non_blocking=True)
        identity_targets = identity_targets.to(device, non_blocking=True)
        auxiliary_targets = auxiliary_targets.to(device, non_blocking=True)

        accumulation_group_start = (
            batch_index // accumulation_steps
        ) * accumulation_steps
        accumulation_group_size = min(
            accumulation_steps,
            loader_length - accumulation_group_start,
        )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            output_logits = model(**encoded).logits
            total_loss = compute_training_loss(
                output_logits,
                soft_targets,
                binary_targets,
                sample_weights,
                identity_targets,
                auxiliary_targets,
            )
            scaled_loss = total_loss / float(accumulation_group_size)

        grad_scaler.scale(scaled_loss).backward()
        epoch_loss_sum += float(total_loss.detach().cpu())
        epoch_microbatches += 1

        is_update_boundary = (batch_index + 1) % accumulation_steps == 0 or (
            batch_index + 1
        ) == loader_length
        if not is_update_boundary:
            continue

        grad_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

        completed_updates += 1
        stop_training = session.step()
        if stop_training:
            break

    if epoch_microbatches:
        average_epoch_loss = epoch_loss_sum / epoch_microbatches
        print(
            f"Epoch {epoch_index} | updates={completed_updates} | "
            f"train_loss={average_epoch_loss:.6f}"
        )

score = session.finish()
print(f"Final Validation Score: {score}")
