import json
import os
import re
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertConfig,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

IDENTITY_COLUMNS = [
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

TRAIN_COLUMNS = ["id", "target", "comment_text"] + IDENTITY_COLUMNS

# The runtime owns the contract split and the official Jigsaw bias-aware metric.
session = CandidateSession.from_env()

raw_train_df = pd.read_csv(INPUT_DIR / "train.csv", usecols=TRAIN_COLUMNS)
raw_test_df = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
)

# Split before any stateful transformation or fitting.
train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
train_df = train_df.reset_index(drop=True)
valid_df = valid_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

del raw_train_df, raw_test_df

IDENTITY_LEXICONS = [
    (
        "male",
        r"\b(?:male|man|men|boy|boys|gentleman|gentlemen|father|fathers|husband|husbands)\b",
    ),
    (
        "female",
        r"\b(?:female|woman|women|girl|girls|lady|ladies|mother|mothers|wife|wives)\b",
    ),
    (
        "gay_lesbian",
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbt|lgbtq|queer)\b",
    ),
    (
        "christian",
        r"\b(?:christian|christians|christianity|catholic|catholics|protestant|protestants)\b",
    ),
    (
        "jewish",
        r"\b(?:jew|jews|jewish|judaism|judaic)\b",
    ),
    (
        "muslim",
        r"\b(?:muslim|muslims|islam|islamic|islamist)\b",
    ),
    (
        "black",
        r"\b(?:black|blacks|african[\s-]?american|african[\s-]?americans)\b",
    ),
    (
        "white",
        r"\b(?:white|whites|caucasian|caucasians)\b",
    ),
    (
        "mental_illness",
        r"\b(?:mental(?:ly)?[\s-]?ill|mental[\s-]?illness|psychiatric|depression|depressed|autistic|autism|schizophren(?:ic|ia)|bipolar)\b",
    ),
]

IDENTITY_PATTERNS = [
    (name, re.compile(pattern, flags=re.IGNORECASE))
    for name, pattern in IDENTITY_LEXICONS
]

COUNTERFACTUAL_REPLACEMENTS = {
    1: "woman",
    2: "man",
    3: "christian",
    4: "muslim",
    5: "jewish",
    6: "white",
    7: "black",
    8: "person",
    9: "person",
}


def normalize_comment_text(text_series: pd.Series) -> pd.Series:
    """Stateless normalization shared across train, validation, and test."""
    text = text_series.fillna("").astype("string").str.normalize("NFKC")
    text = text.str.replace(r"<[^>\n]{1,120}>", " ", regex=True)
    text = text.str.replace(
        r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
        " emailtoken ",
        regex=True,
    )
    text = text.str.replace(
        r"\b(?:https?://|www\.)\S+\b",
        " urltoken ",
        regex=True,
    )
    text = text.str.replace(r"[\r\n\t\f\v]+", " ", regex=True)
    text = text.str.replace(r"\s{2,}", " ", regex=True).str.strip().str.lower()
    return text.fillna("")


def build_counterfactual_text(text: str, identity_code: int) -> str:
    """Create a training-only identity substitution paired example."""
    if identity_code <= 0 or identity_code not in COUNTERFACTUAL_REPLACEMENTS:
        return text

    _, source_pattern = IDENTITY_PATTERNS[identity_code - 1]
    return source_pattern.sub(COUNTERFACTUAL_REPLACEMENTS[identity_code], str(text))


def engineer_partition_features(frame: pd.DataFrame) -> pd.DataFrame:
    """
    Build text-only structural and lexicon features available identically for all
    partitions. The model consumes model_text; auxiliary fields support training.
    """
    result = frame.copy()
    raw_text = result["comment_text"].fillna("").astype("string")
    normalized_text = normalize_comment_text(raw_text)
    result["model_text"] = normalized_text

    raw_length = raw_text.str.len().fillna(0).to_numpy(dtype=np.float32)
    char_length = normalized_text.str.len().fillna(0).to_numpy(dtype=np.float32)
    word_count = normalized_text.str.count(r"\S+").fillna(0).to_numpy(dtype=np.float32)
    upper_count = raw_text.str.count(r"[A-Z]").fillna(0).to_numpy(dtype=np.float32)
    alpha_count = raw_text.str.count(r"[A-Za-z]").fillna(0).to_numpy(dtype=np.float32)

    features = {
        "feat_log_char_length": np.log1p(char_length),
        "feat_log_word_count": np.log1p(word_count),
        "feat_log_mean_word_length": np.log1p(
            char_length / np.maximum(word_count, 1.0)
        ),
        "feat_uppercase_fraction": upper_count / np.maximum(alpha_count, 1.0),
        "feat_exclamation_density": (
            raw_text.str.count("!").fillna(0).to_numpy(dtype=np.float32)
            / np.maximum(raw_length, 1.0)
        ),
        "feat_question_density": (
            raw_text.str.count(r"\?").fillna(0).to_numpy(dtype=np.float32)
            / np.maximum(raw_length, 1.0)
        ),
        "feat_punctuation_density": (
            raw_text.str.count(r"[!?.,;:]").fillna(0).to_numpy(dtype=np.float32)
            / np.maximum(raw_length, 1.0)
        ),
        "feat_newline_count": raw_text.str.count(r"[\r\n]")
        .fillna(0)
        .to_numpy(dtype=np.float32),
        "feat_url_present": raw_text.str.contains(
            r"\b(?:https?://|www\.)\S+",
            case=False,
            regex=True,
            na=False,
        ).to_numpy(dtype=np.float32),
        "feat_email_present": raw_text.str.contains(
            r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
            case=False,
            regex=True,
            na=False,
        ).to_numpy(dtype=np.float32),
        "feat_repeated_punctuation": raw_text.str.contains(
            r"([!?.,])\1{2,}",
            regex=True,
            na=False,
        ).to_numpy(dtype=np.float32),
        "feat_all_caps_token": raw_text.str.contains(
            r"\b[A-Z]{3,}\b",
            regex=True,
            na=False,
        ).to_numpy(dtype=np.float32),
        "feat_quote_present": raw_text.str.contains(
            r"""["']""",
            regex=True,
            na=False,
        ).to_numpy(dtype=np.float32),
    }

    identity_codes = np.zeros(len(result), dtype=np.int16)
    identity_count = np.zeros(len(result), dtype=np.float32)

    for code, (identity_name, pattern) in enumerate(IDENTITY_PATTERNS, start=1):
        mentioned = normalized_text.str.contains(pattern, na=False).to_numpy(
            dtype=np.float32
        )
        features[f"feat_identity_{identity_name}"] = mentioned
        identity_count += mentioned
        identity_codes[(identity_codes == 0) & (mentioned > 0)] = code

    features["feat_identity_mention_count"] = identity_count
    features["feat_any_identity_mention"] = (identity_count > 0).astype(np.float32)

    feature_frame = pd.DataFrame(features, index=result.index, dtype=np.float32)
    result[feature_frame.columns] = feature_frame
    result["counterfactual_identity_code"] = identity_codes

    return result


train_df = engineer_partition_features(train_df)
valid_df = engineer_partition_features(valid_df)
test_df = engineer_partition_features(test_df)

CONTINUOUS_FEATURE_COLUMNS = [
    "feat_log_char_length",
    "feat_log_word_count",
    "feat_log_mean_word_length",
    "feat_uppercase_fraction",
    "feat_exclamation_density",
    "feat_question_density",
    "feat_punctuation_density",
    "feat_newline_count",
    "feat_identity_mention_count",
]

IDENTITY_FEATURE_COLUMNS = [
    column for column in train_df.columns if column.startswith("feat_identity_")
] + ["feat_any_identity_mention"]

MODEL_FEATURE_COLUMNS = CONTINUOUS_FEATURE_COLUMNS + IDENTITY_FEATURE_COLUMNS

# Fit scaling exclusively on training partition.
feature_mean = train_df[CONTINUOUS_FEATURE_COLUMNS].mean(axis=0).astype(np.float32)
feature_std = train_df[CONTINUOUS_FEATURE_COLUMNS].std(axis=0).astype(np.float32)
feature_std = feature_std.mask(feature_std < 1e-6, 1.0).fillna(1.0)

for partition in (train_df, valid_df, test_df):
    partition[CONTINUOUS_FEATURE_COLUMNS] = (
        (partition[CONTINUOUS_FEATURE_COLUMNS] - feature_mean) / feature_std
    ).astype(np.float32)
    partition[IDENTITY_FEATURE_COLUMNS] = partition[IDENTITY_FEATURE_COLUMNS].astype(
        np.float32
    )

train_targets_soft = train_df["target"].fillna(0.0).to_numpy(dtype=np.float32)
valid_targets_soft = valid_df["target"].fillna(0.0).to_numpy(dtype=np.float32)
train_targets_binary = (train_targets_soft >= 0.5).astype(np.int8)
valid_targets_binary = (valid_targets_soft >= 0.5).astype(np.int8)

train_identity_annotation_mask = (
    train_df[IDENTITY_COLUMNS].fillna(0.0).max(axis=1).to_numpy(dtype=np.float32) >= 0.5
)
train_counterfactual_mask = train_identity_annotation_mask & (
    train_df["counterfactual_identity_code"].to_numpy(dtype=np.int16) > 0
)

preprocessing_state = {
    "version": 1,
    "continuous_feature_columns": CONTINUOUS_FEATURE_COLUMNS,
    "identity_feature_columns": IDENTITY_FEATURE_COLUMNS,
    "model_feature_columns": MODEL_FEATURE_COLUMNS,
    "feature_mean": {key: float(value) for key, value in feature_mean.items()},
    "feature_std": {key: float(value) for key, value in feature_std.items()},
    "identity_lexicon_names": [name for name, _ in IDENTITY_LEXICONS],
}

with open(WORKING_DIR / "preprocessing_state.json", "w", encoding="utf-8") as f:
    json.dump(preprocessing_state, f, indent=2, sort_keys=True)


# ModernBERT is a contextual scalar toxicity scorer.
model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model_config = ModernBertConfig.from_pretrained(model_id, num_labels=1)
model_config.classifier_dropout = 0.15
model_config.hidden_dropout_prob = 0.10

model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    config=model_config,
    ignore_mismatched_sizes=True,
)

if hasattr(model, "gradient_checkpointing_enable"):
    model.gradient_checkpointing_enable()

EVALUATION_IDENTITY_COLUMNS = [
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


def build_identity_cell_membership(identity_values, binary_targets):
    """
    Construct identity-by-label membership for benign and toxic examples.
    These cells correspond directly to bias metric ranking failure patterns.
    """
    identity_tensor = torch.as_tensor(identity_values, dtype=torch.float32)
    target_tensor = torch.as_tensor(binary_targets, dtype=torch.bool).reshape(-1)

    if identity_tensor.ndim != 2:
        raise ValueError(
            "identity_values must have shape [batch_size, num_identities]."
        )
    if identity_tensor.shape[0] != target_tensor.shape[0]:
        raise ValueError("identity_values and binary_targets must share batch size.")

    identity_present = identity_tensor >= 0.5
    non_toxic = ~target_tensor[:, None]
    toxic = target_tensor[:, None]

    benign_identity_cells = identity_present & non_toxic
    toxic_identity_cells = identity_present & toxic

    return torch.cat(
        [
            benign_identity_cells.to(torch.float32),
            toxic_identity_cells.to(torch.float32),
        ],
        dim=1,
    )


class IdentityCellGroupDROLoss(nn.Module):
    """
    Soft-label BCE plus robust weighting of difficult identity/label training cells.
    """

    def __init__(
        self,
        num_identities,
        robust_weight=0.65,
        ema_decay=0.98,
        temperature=0.20,
        minimum_group_mass=1.0,
    ):
        super().__init__()

        if num_identities <= 0:
            raise ValueError("num_identities must be positive.")

        self.num_groups = int(num_identities) * 2
        self.robust_weight = float(robust_weight)
        self.ema_decay = float(ema_decay)
        self.temperature = float(temperature)
        self.minimum_group_mass = float(minimum_group_mass)

        self.register_buffer(
            "ema_group_loss",
            torch.full((self.num_groups,), 0.50, dtype=torch.float32),
        )

    def forward(self, logits, soft_targets, group_membership):
        logits = logits.reshape(-1)
        soft_targets = soft_targets.reshape(-1).to(dtype=logits.dtype)
        group_membership = group_membership.to(
            device=logits.device,
            dtype=logits.dtype,
        )

        if group_membership.ndim != 2:
            raise ValueError(
                "group_membership must have shape [batch_size, num_groups]."
            )
        if group_membership.shape != (logits.shape[0], self.num_groups):
            raise ValueError(
                "group_membership shape must match [batch_size, 2 * num_identities]."
            )

        per_example_loss = F.binary_cross_entropy_with_logits(
            logits,
            soft_targets.clamp(0.0, 1.0),
            reduction="none",
        )
        base_loss = per_example_loss.mean()

        group_mass = group_membership.sum(dim=0)
        active_groups = group_mass >= self.minimum_group_mass

        if not bool(active_groups.any()):
            return base_loss

        current_group_loss = (per_example_loss[:, None] * group_membership).sum(
            dim=0
        ) / group_mass.clamp_min(1.0)

        if self.training:
            with torch.no_grad():
                self.ema_group_loss[
                    active_groups
                ] = self.ema_decay * self.ema_group_loss[active_groups] + (
                    1.0 - self.ema_decay
                ) * current_group_loss.detach()[
                    active_groups
                ].to(
                    self.ema_group_loss.dtype
                )

        masked_ema = self.ema_group_loss.to(logits.dtype).masked_fill(
            ~active_groups,
            torch.finfo(logits.dtype).min,
        )
        group_weights = torch.softmax(masked_ema / self.temperature, dim=0)
        robust_loss = (group_weights * current_group_loss).sum()

        return (1.0 - self.robust_weight) * base_loss + self.robust_weight * robust_loss


criterion = IdentityCellGroupDROLoss(
    num_identities=len(EVALUATION_IDENTITY_COLUMNS),
    robust_weight=0.65,
    ema_decay=0.98,
    temperature=0.20,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
backbone_decay, backbone_no_decay = [], []
head_decay, head_no_decay = [], []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_backbone_parameter = parameter_name.startswith("model.")
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_backbone_parameter and has_no_decay:
        backbone_no_decay.append(parameter)
    elif is_backbone_parameter:
        backbone_decay.append(parameter)
    elif has_no_decay:
        head_no_decay.append(parameter)
    else:
        head_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": backbone_decay, "lr": 1.5e-5, "weight_decay": 0.01},
        {"params": backbone_no_decay, "lr": 1.5e-5, "weight_decay": 0.0},
        {"params": head_decay, "lr": 6.0e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 6.0e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)


DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
USE_AMP = DEVICE.type == "cuda"

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 24
GRADIENT_ACCUMULATION_STEPS = 2
MAX_EPOCHS = 4
COUNTERFACTUAL_PROBABILITY = 0.35
COUNTERFACTUAL_CONSISTENCY_WEIGHT = 0.18
NUM_WORKERS = 2

if USE_AMP:
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

model.to(DEVICE)
criterion.to(DEVICE)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame, enable_counterfactual=False):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=False)
        self.soft_targets = frame["target"].fillna(0.0).to_numpy(dtype=np.float32)
        self.binary_targets = (self.soft_targets >= 0.5).astype(np.int64)
        self.identity_values = (
            frame[EVALUATION_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
        )

        self.enable_counterfactual = bool(enable_counterfactual)
        if self.enable_counterfactual:
            self.counterfactual_allowed = np.asarray(
                train_counterfactual_mask,
                dtype=np.bool_,
            )
            self.identity_codes = frame["counterfactual_identity_code"].to_numpy(
                dtype=np.int16
            )
        else:
            self.counterfactual_allowed = np.zeros(len(frame), dtype=np.bool_)
            self.identity_codes = np.zeros(len(frame), dtype=np.int16)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        use_counterfactual = bool(self.counterfactual_allowed[index])

        if use_counterfactual:
            counterfactual_text = build_counterfactual_text(
                text,
                int(self.identity_codes[index]),
            )
        else:
            counterfactual_text = ""

        return {
            "text": text,
            "counterfactual_text": counterfactual_text,
            "counterfactual_allowed": use_counterfactual,
            "soft_target": self.soft_targets[index],
            "binary_target": self.binary_targets[index],
            "identity_values": self.identity_values[index],
        }


class ToxicityInferenceDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=False)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index]


def training_collate(batch):
    return {
        "texts": [item["text"] for item in batch],
        "counterfactual_texts": [item["counterfactual_text"] for item in batch],
        "counterfactual_allowed": torch.tensor(
            [item["counterfactual_allowed"] for item in batch],
            dtype=torch.bool,
        ),
        "soft_targets": torch.tensor(
            [item["soft_target"] for item in batch],
            dtype=torch.float32,
        ),
        "binary_targets": torch.tensor(
            [item["binary_target"] for item in batch],
            dtype=torch.long,
        ),
        "identity_values": torch.tensor(
            np.stack([item["identity_values"] for item in batch]),
            dtype=torch.float32,
        ),
    }


def inference_collate(batch):
    return list(batch)


def tokenize_texts(texts):
    encoded = tokenizer(
        texts,
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )
    return {
        key: value.to(DEVICE, non_blocking=True)
        for key, value in encoded.items()
        if key != "token_type_ids"
    }


@torch.inference_mode()
def predict_partition(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)

    was_training = model.training
    model.eval()

    subset = frame.iloc[positions]
    inference_dataset = ToxicityInferenceDataset(subset)
    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=USE_AMP,
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=inference_collate,
    )

    prediction_chunks = []

    for texts in inference_loader:
        encoded = tokenize_texts(texts)
        with torch.cuda.amp.autocast(enabled=USE_AMP):
            logits = model(**encoded).logits.reshape(-1)
        prediction_chunks.append(torch.sigmoid(logits).float().cpu().numpy())

    if was_training:
        model.train()

    return np.concatenate(prediction_chunks).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_partition(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_partition(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(model.state_dict(), checkpoint_dir / "model_state.pt")
    torch.save(criterion.state_dict(), checkpoint_dir / "criterion_state.pt")

    model.config.save_pretrained(str(checkpoint_dir))
    tokenizer.save_pretrained(str(checkpoint_dir))

    preprocessing_source = WORKING_DIR / "preprocessing_state.json"
    if preprocessing_source.exists():
        shutil.copy2(
            preprocessing_source,
            checkpoint_dir / "preprocessing_state.json",
        )

    inference_state = {
        "max_length": MAX_LENGTH,
        "text_column": "model_text",
        "prediction_transform": "sigmoid(logit)",
        "identity_columns": EVALUATION_IDENTITY_COLUMNS,
    }

    with open(
        checkpoint_dir / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as output_file:
        json.dump(inference_state, output_file, indent=2, sort_keys=True)


def load_checkpoint(directory):
    checkpoint_dir = Path(directory)

    model_state = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=DEVICE,
    )
    model.load_state_dict(model_state, strict=True)
    model.to(DEVICE)

    criterion_state_path = checkpoint_dir / "criterion_state.pt"
    if criterion_state_path.exists():
        criterion_state = torch.load(
            criterion_state_path,
            map_location=DEVICE,
        )
        criterion.load_state_dict(criterion_state, strict=True)
        criterion.to(DEVICE)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

training_dataset = ToxicityTrainingDataset(
    train_df,
    enable_counterfactual=True,
)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=USE_AMP,
    persistent_workers=NUM_WORKERS > 0,
    drop_last=False,
    collate_fn=training_collate,
)

scaler = torch.cuda.amp.GradScaler(enabled=USE_AMP)
optimizer.zero_grad(set_to_none=True)

session.start_training(train_df["id"].astype(str).tolist())

stop_training = False
optimizer_updates = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    criterion.train()

    epoch_loss_sum = 0.0
    epoch_batches = 0
    epoch_updates = 0
    pending_accumulation = 0

    for batch in training_loader:
        encoded = tokenize_texts(batch["texts"])

        soft_targets = batch["soft_targets"].to(
            DEVICE,
            non_blocking=True,
        )
        binary_targets = batch["binary_targets"].to(
            DEVICE,
            non_blocking=True,
        )
        identity_values = batch["identity_values"].to(
            DEVICE,
            non_blocking=True,
        )

        group_membership = build_identity_cell_membership(
            identity_values,
            binary_targets,
        )

        with torch.cuda.amp.autocast(enabled=USE_AMP):
            logits = model(**encoded).logits.reshape(-1)
            primary_loss = criterion(
                logits,
                soft_targets,
                group_membership,
            )

            available_counterfactuals = batch["counterfactual_allowed"].to(
                DEVICE,
                non_blocking=True,
            )

            selected_counterfactuals = available_counterfactuals & (
                torch.rand(
                    available_counterfactuals.shape,
                    device=DEVICE,
                )
                < COUNTERFACTUAL_PROBABILITY
            )

            consistency_loss = logits.new_zeros(())

            if bool(selected_counterfactuals.any()):
                selected_indices = (
                    selected_counterfactuals.nonzero(as_tuple=False)
                    .reshape(-1)
                    .cpu()
                    .tolist()
                )

                selected_texts = [
                    batch["counterfactual_texts"][index] for index in selected_indices
                ]

                counterfactual_encoded = tokenize_texts(selected_texts)
                counterfactual_logits = model(**counterfactual_encoded).logits.reshape(
                    -1
                )

                original_probabilities = torch.sigmoid(logits[selected_counterfactuals])
                counterfactual_probabilities = torch.sigmoid(counterfactual_logits)

                consistency_loss = F.mse_loss(
                    counterfactual_probabilities,
                    original_probabilities.detach(),
                )

            total_loss = (
                primary_loss + COUNTERFACTUAL_CONSISTENCY_WEIGHT * consistency_loss
            )

        if not torch.isfinite(total_loss):
            optimizer.zero_grad(set_to_none=True)
            pending_accumulation = 0
            continue

        scaler.scale(total_loss / GRADIENT_ACCUMULATION_STEPS).backward()

        epoch_loss_sum += float(total_loss.detach().cpu())
        epoch_batches += 1
        pending_accumulation += 1

        if pending_accumulation < GRADIENT_ACCUMULATION_STEPS:
            continue

        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        pending_accumulation = 0
        optimizer_updates += 1
        epoch_updates += 1

        stop_training = session.step()
        if stop_training:
            break

    if not stop_training and pending_accumulation > 0:
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        optimizer_updates += 1
        epoch_updates += 1
        stop_training = session.step()

    average_epoch_loss = epoch_loss_sum / max(epoch_batches, 1)
    print(
        f"Epoch {epoch}: loss={average_epoch_loss:.6f}, "
        f"optimizer_updates={epoch_updates}"
    )

    if stop_training:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
