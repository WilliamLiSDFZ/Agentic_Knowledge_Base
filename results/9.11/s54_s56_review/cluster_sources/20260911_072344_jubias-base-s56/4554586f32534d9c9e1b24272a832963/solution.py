import os
import re
import json
import html
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
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)
from engine.candidate_runtime import CandidateSession


SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

OFFICIAL_IDENTITY_COLUMNS = [
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

TEXT_FEATURE_COLUMNS = [
    "char_count",
    "word_count",
    "unique_word_ratio",
    "uppercase_ratio",
    "digit_ratio",
    "newline_count",
    "url_count",
    "email_count",
    "mention_count",
    "hashtag_count",
    "exclamation_count",
    "question_count",
    "punctuation_ratio",
    "non_ascii_ratio",
]

URL_PATTERN = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"\b[\w.\-+]+@[\w.\-]+\.\w+\b", flags=re.IGNORECASE)
MENTION_PATTERN = re.compile(r"(?<!\w)@\w+")
HASHTAG_PATTERN = re.compile(r"(?<!\w)#\w+")
WHITESPACE_PATTERN = re.compile(r"\s+")
WORD_PATTERN = re.compile(r"\b[\w']+\b", flags=re.UNICODE)
PUNCTUATION_PATTERN = re.compile(r"[^\w\s]", flags=re.UNICODE)
CONTROL_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")


def normalize_comment(value):
    """Conservative normalization retaining lexical toxicity and identity evidence."""
    if pd.isna(value):
        return ""

    text = html.unescape(str(value))
    text = unicodedata.normalize("NFKC", text)
    text = CONTROL_PATTERN.sub(" ", text)
    text = URL_PATTERN.sub(" [URL] ", text)
    text = EMAIL_PATTERN.sub(" [EMAIL] ", text)
    text = MENTION_PATTERN.sub(" [USER] ", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text


def add_text_features(frame):
    """Apply identical stateless processing to train, validation, and test."""
    output = frame.copy()
    output["comment_text_model"] = output["comment_text"].map(normalize_comment)

    text = output["comment_text_model"]
    char_count = text.str.len().astype(np.float32)
    word_count = text.str.findall(WORD_PATTERN).str.len().astype(np.float32)
    unique_word_count = text.map(
        lambda value: len(set(token.lower() for token in WORD_PATTERN.findall(value)))
    ).astype(np.float32)

    output["char_count"] = char_count
    output["word_count"] = word_count
    output["unique_word_ratio"] = (
        unique_word_count / np.maximum(word_count, 1.0)
    ).astype(np.float32)
    output["uppercase_ratio"] = (
        text.str.count(r"[A-Z]") / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    output["digit_ratio"] = (
        text.str.count(r"\d") / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    output["newline_count"] = text.str.count(r"\n").astype(np.float32)
    output["url_count"] = text.str.count(r"\[URL\]").astype(np.float32)
    output["email_count"] = text.str.count(r"\[EMAIL\]").astype(np.float32)
    output["mention_count"] = text.str.count(r"\[USER\]").astype(np.float32)
    output["hashtag_count"] = text.str.count(HASHTAG_PATTERN).astype(np.float32)
    output["exclamation_count"] = text.str.count("!").astype(np.float32)
    output["question_count"] = text.str.count(r"\?").astype(np.float32)
    output["punctuation_ratio"] = (
        text.str.count(PUNCTUATION_PATTERN) / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    output["non_ascii_ratio"] = (
        text.str.count(r"[^\x00-\x7F]") / np.maximum(char_count, 1.0)
    ).astype(np.float32)

    return output


def make_fairness_weights(frame, identity_columns):
    """
    Build per-official-identity fairness weights for the subgroup, BPSN, and
    BNSP ranking regions. Per-identity candidates are max-combined so comments
    mentioning multiple identities do not receive compounded weight inflation.
    """
    base_weight = 0.25
    subgroup_negative_weight = 0.75
    background_positive_weight = 0.75
    subgroup_positive_weight = 0.50
    background_negative_weight = base_weight

    target_binary = frame["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
    available_identities = [
        column for column in identity_columns if column in frame.columns
    ]
    weights = np.full(len(frame), base_weight, dtype=np.float32)

    for column in available_identities:
        subgroup = frame[column].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
        candidate_weights = np.full(
            len(frame),
            background_negative_weight,
            dtype=np.float32,
        )
        candidate_weights[subgroup & ~target_binary] = subgroup_negative_weight
        candidate_weights[~subgroup & target_binary] = background_positive_weight
        candidate_weights[subgroup & target_binary] = subgroup_positive_weight
        weights = np.maximum(weights, candidate_weights)

    weights /= max(float(weights.mean()), 1e-8)

    return target_binary.astype(np.int8), weights.astype(np.float32)


session = CandidateSession.from_env()

train_header = pd.read_csv(INPUT_DIR / "train.csv", nrows=0).columns.tolist()
train_columns = ["id", "target", "comment_text"] + OFFICIAL_IDENTITY_COLUMNS
train_columns = [column for column in train_columns if column in train_header]

train_raw = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=train_columns,
    low_memory=False,
)
test_raw = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_raw, test_raw)

train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

train_df["target"] = train_df["target"].fillna(0.0).astype(np.float32)
valid_df["target"] = valid_df["target"].fillna(0.0).astype(np.float32)

train_df["target_binary"], train_df["sample_weight"] = make_fairness_weights(
    train_df,
    OFFICIAL_IDENTITY_COLUMNS,
)

available_region_identities = [
    column for column in OFFICIAL_IDENTITY_COLUMNS if column in train_df.columns
]
train_identity_membership = (
    train_df[available_region_identities]
    .fillna(0.0)
    .to_numpy(dtype=np.float32)
    >= 0.5
)
train_identity_mention = train_identity_membership.max(axis=1)
train_target_binary = train_df["target_binary"].to_numpy(dtype=np.int8).astype(bool)

identity_bpsn_pools = {
    column: np.flatnonzero(
        train_identity_membership[:, identity_position] & ~train_target_binary
    ).astype(np.int64)
    for identity_position, column in enumerate(available_region_identities)
}
background_positive_pool = np.flatnonzero(
    ~train_identity_mention & train_target_binary
).astype(np.int64)
identity_subgroup_positive_pools = {
    column: np.flatnonzero(
        train_identity_membership[:, identity_position] & train_target_binary
    ).astype(np.int64)
    for identity_position, column in enumerate(available_region_identities)
}

valid_df["target_binary"], valid_df["sample_weight"] = make_fairness_weights(
    valid_df,
    OFFICIAL_IDENTITY_COLUMNS,
)

numeric_scaler = StandardScaler()
X_train_numeric = numeric_scaler.fit_transform(
    train_df[TEXT_FEATURE_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
).astype(np.float32)
X_valid_numeric = numeric_scaler.transform(
    valid_df[TEXT_FEATURE_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
).astype(np.float32)
X_test_numeric = numeric_scaler.transform(
    test_df[TEXT_FEATURE_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
).astype(np.float32)

np.savez_compressed(
    WORKING_DIR / "text_numeric_features.npz",
    train_ids=train_df["id"].to_numpy(),
    valid_ids=valid_df["id"].to_numpy(),
    test_ids=test_df["id"].to_numpy(),
    X_train_numeric=X_train_numeric,
    X_valid_numeric=X_valid_numeric,
    X_test_numeric=X_test_numeric,
    y_train_soft=train_df["target"].to_numpy(dtype=np.float32),
    y_train_binary=train_df["target_binary"].to_numpy(dtype=np.int8),
    y_valid_soft=valid_df["target"].to_numpy(dtype=np.float32),
    y_valid_binary=valid_df["target_binary"].to_numpy(dtype=np.int8),
    train_sample_weight=train_df["sample_weight"].to_numpy(dtype=np.float32),
)

with open(
    WORKING_DIR / "feature_engineering_state.json", "w", encoding="utf-8"
) as handle:
    json.dump(
        {
            "feature_columns": TEXT_FEATURE_COLUMNS,
            "mean": numeric_scaler.mean_.tolist(),
            "scale": numeric_scaler.scale_.tolist(),
            "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
            "identity_bpsn_pool_counts": {
                identity: int(len(positions))
                for identity, positions in identity_bpsn_pools.items()
            },
            "background_positive_pool_count": int(len(background_positive_pool)),
            "identity_subgroup_positive_pool_counts": {
                identity: int(len(positions))
                for identity, positions in identity_subgroup_positive_pools.items()
            },
            "text_column": "comment_text_model",
        },
        handle,
    )

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Disable ModernBERT's optional torch.compile reference path: it invokes Triton,
# which requires a system C compiler unavailable in the execution environment.
model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    reference_compile=False,
)

NUMERIC_FEATURE_DIM = len(TEXT_FEATURE_COLUMNS)
IDENTITY_TARGET_DIM = len(OFFICIAL_IDENTITY_COLUMNS)
FINE_TUNE_LAST_N_LAYERS = 8


class FairnessAwareModernBert(nn.Module):
    """
    Shared ModernBERT encoder with a soft toxicity head, auxiliary identity head,
    and structural text feature fusion.
    """

    def __init__(
        self,
        pretrained_sequence_classifier,
        numeric_feature_dim,
        identity_target_dim,
        numeric_hidden_dim=128,
        dropout=0.15,
    ):
        super().__init__()
        self.backbone = pretrained_sequence_classifier.model
        hidden_size = pretrained_sequence_classifier.config.hidden_size

        self.numeric_encoder = nn.Sequential(
            nn.LayerNorm(numeric_feature_dim),
            nn.Linear(numeric_feature_dim, numeric_hidden_dim),
            nn.SiLU(),
            nn.Dropout(dropout),
            nn.Linear(numeric_hidden_dim, hidden_size),
        )
        self.fusion_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )
        self.shared_norm = nn.LayerNorm(hidden_size)
        self.shared_dropout = nn.Dropout(dropout)

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )
        self.identity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, identity_target_dim),
        )

    def forward(self, input_ids, attention_mask, numeric_features=None):
        encoder_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        text_embedding = encoder_outputs.last_hidden_state[:, 0, :]

        if numeric_features is None:
            numeric_features = torch.zeros(
                (text_embedding.shape[0], self.numeric_encoder[1].in_features),
                dtype=text_embedding.dtype,
                device=text_embedding.device,
            )
        else:
            numeric_features = numeric_features.to(
                device=text_embedding.device,
                dtype=text_embedding.dtype,
            )

        numeric_embedding = self.numeric_encoder(numeric_features)
        fusion_gate = self.fusion_gate(
            torch.cat([text_embedding, numeric_embedding], dim=-1)
        )
        shared_embedding = self.shared_norm(
            text_embedding + fusion_gate * numeric_embedding
        )
        shared_embedding = self.shared_dropout(shared_embedding)

        return {
            "toxicity_logits": self.toxicity_head(shared_embedding).squeeze(-1),
            "identity_logits": self.identity_head(shared_embedding),
        }


class FairnessAwareMultitaskLoss(nn.Module):
    """Weighted soft toxicity BCE plus masked auxiliary identity BCE."""

    def __init__(self, identity_loss_weight=0.20):
        super().__init__()
        self.identity_loss_weight = float(identity_loss_weight)

    def forward(
        self,
        outputs,
        toxicity_targets,
        sample_weights=None,
        identity_targets=None,
    ):
        toxicity_logits = outputs["toxicity_logits"].reshape(-1)
        toxicity_targets = (
            toxicity_targets.reshape(-1)
            .to(
                device=toxicity_logits.device,
                dtype=toxicity_logits.dtype,
            )
            .clamp(0.0, 1.0)
        )

        toxicity_losses = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
            reduction="none",
        )

        if sample_weights is None:
            sample_weights = torch.ones_like(toxicity_losses)
        else:
            sample_weights = (
                sample_weights.reshape(-1)
                .to(
                    device=toxicity_logits.device,
                    dtype=toxicity_logits.dtype,
                )
                .clamp_min(0.0)
            )

        toxicity_loss = (toxicity_losses * sample_weights).sum() / (
            sample_weights.sum().clamp_min(1e-8)
        )

        identity_loss = toxicity_loss.new_zeros(())
        if identity_targets is not None:
            identity_logits = outputs["identity_logits"]
            identity_targets = identity_targets.to(
                device=identity_logits.device,
                dtype=identity_logits.dtype,
            )
            valid_identity_mask = torch.isfinite(identity_targets)

            if bool(valid_identity_mask.any()):
                safe_identity_targets = torch.nan_to_num(
                    identity_targets,
                    nan=0.0,
                    posinf=1.0,
                    neginf=0.0,
                ).clamp(0.0, 1.0)

                identity_losses = F.binary_cross_entropy_with_logits(
                    identity_logits,
                    safe_identity_targets,
                    reduction="none",
                )

                identity_loss = (
                    identity_losses * valid_identity_mask.to(identity_losses.dtype)
                ).sum() / valid_identity_mask.sum().clamp_min(1)

        total_loss = toxicity_loss + self.identity_loss_weight * identity_loss
        return total_loss, {
            "toxicity_loss": toxicity_loss.detach(),
            "identity_loss": identity_loss.detach(),
        }


model = FairnessAwareModernBert(
    pretrained_sequence_classifier=model,
    numeric_feature_dim=NUMERIC_FEATURE_DIM,
    identity_target_dim=IDENTITY_TARGET_DIM,
)

layer_indices = []
for parameter_name, _ in model.named_parameters():
    match = re.search(r"(?:^|\.)layers\.(\d+)\.", parameter_name)
    if match is not None:
        layer_indices.append(int(match.group(1)))

if layer_indices:
    first_trainable_layer = max(layer_indices) - FINE_TUNE_LAST_N_LAYERS + 1
    for parameter_name, parameter in model.named_parameters():
        match = re.search(r"(?:^|\.)layers\.(\d+)\.", parameter_name)
        if match is not None and int(match.group(1)) < first_trainable_layer:
            parameter.requires_grad = False

criterion = FairnessAwareMultitaskLoss(identity_loss_weight=0.20)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
backbone_decay = []
backbone_no_decay = []
head_decay = []
head_no_decay = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = parameter_name.endswith(no_decay_terms)
    is_backbone = parameter_name.startswith("backbone.")

    if is_backbone and is_no_decay:
        backbone_no_decay.append(parameter)
    elif is_backbone:
        backbone_decay.append(parameter)
    elif is_no_decay:
        head_no_decay.append(parameter)
    else:
        head_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": backbone_decay, "lr": 8e-6, "weight_decay": 0.01},
        {"params": backbone_no_decay, "lr": 8e-6, "weight_decay": 0.0},
        {"params": head_decay, "lr": 1e-4, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 1e-4, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

if amp_enabled:
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

np.random.seed(SEED)
torch.manual_seed(SEED)
if amp_enabled:
    torch.cuda.manual_seed_all(SEED)

model.to(device)

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()

TRAIN_BATCH_SIZE = 8
EVAL_BATCH_SIZE = 32
GRADIENT_ACCUMULATION_STEPS = 2
MAX_SEQUENCE_LENGTH = 256
MAX_EPOCHS = 1
WARMUP_UPDATES = 200
NUM_WORKERS = 2

assert len(train_df) == len(X_train_numeric)
assert len(valid_df) == len(X_valid_numeric)
assert len(test_df) == len(X_test_numeric)

feature_archive = np.load(WORKING_DIR / "text_numeric_features.npz")
assert np.array_equal(train_df["id"].to_numpy(), feature_archive["train_ids"])
assert np.array_equal(valid_df["id"].to_numpy(), feature_archive["valid_ids"])
assert np.array_equal(test_df["id"].to_numpy(), feature_archive["test_ids"])
feature_archive.close()

train_texts = (
    train_df["comment_text_model"]
    .fillna("")
    .to_numpy(
        dtype=object,
        copy=False,
    )
)
valid_texts = (
    valid_df["comment_text_model"]
    .fillna("")
    .to_numpy(
        dtype=object,
        copy=False,
    )
)
test_texts = (
    test_df["comment_text_model"]
    .fillna("")
    .to_numpy(
        dtype=object,
        copy=False,
    )
)

train_identity_targets = train_df.reindex(columns=OFFICIAL_IDENTITY_COLUMNS).to_numpy(
    dtype=np.float32
)

train_soft_targets = train_df["target"].to_numpy(dtype=np.float32)
train_weights = train_df["sample_weight"].to_numpy(dtype=np.float32)


class ToxicityTextDataset(Dataset):
    def __init__(
        self,
        texts,
        numeric_features,
        toxicity_targets=None,
        sample_weights=None,
        identity_targets=None,
        positions=None,
    ):
        self.texts = texts
        self.numeric_features = numeric_features
        self.toxicity_targets = toxicity_targets
        self.sample_weights = sample_weights
        self.identity_targets = identity_targets
        self.positions = positions

    def __len__(self):
        return len(self.texts) if self.positions is None else len(self.positions)

    def __getitem__(self, index):
        row_index = index if self.positions is None else int(self.positions[index])

        item = (
            str(self.texts[row_index]),
            self.numeric_features[row_index],
        )

        if self.toxicity_targets is not None:
            item += (
                self.toxicity_targets[row_index],
                self.sample_weights[row_index],
                self.identity_targets[row_index],
            )

        return item


def toxicity_collate(samples):
    texts = [sample[0] for sample in samples]
    encoded = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )

    batch = {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "numeric_features": torch.from_numpy(
            np.stack([sample[1] for sample in samples]).astype(np.float32, copy=False)
        ),
    }

    if len(samples[0]) == 5:
        batch["toxicity_targets"] = torch.tensor(
            [sample[2] for sample in samples],
            dtype=torch.float32,
        )
        batch["sample_weights"] = torch.tensor(
            [sample[3] for sample in samples],
            dtype=torch.float32,
        )
        batch["identity_targets"] = torch.from_numpy(
            np.stack([sample[4] for sample in samples]).astype(np.float32, copy=False)
        )

    return batch


train_dataset = ToxicityTextDataset(
    texts=train_texts,
    numeric_features=X_train_numeric,
    toxicity_targets=train_soft_targets,
    sample_weights=train_weights,
    identity_targets=train_identity_targets,
)

class FairnessStratifiedBatchSampler:
    """Identity-balanced replacement batches targeting BPSN and BNSP regions."""

    def __init__(
        self,
        identity_bpsn_pools,
        background_positive_pool,
        identity_subgroup_positive_pools,
        batch_size,
        seed,
    ):
        self.identity_bpsn_pools = {
            identity: np.asarray(positions, dtype=np.int64)
            for identity, positions in identity_bpsn_pools.items()
        }
        self.background_positive_pool = np.asarray(
            background_positive_pool,
            dtype=np.int64,
        )
        self.identity_subgroup_positive_pools = {
            identity: np.asarray(positions, dtype=np.int64)
            for identity, positions in identity_subgroup_positive_pools.items()
        }
        self.identity_names = tuple(self.identity_bpsn_pools)
        self.batch_size = int(batch_size)
        self.num_batches = int(
            np.ceil(len(train_dataset) / float(self.batch_size))
        )
        self.rng = np.random.default_rng(seed)

        if self.batch_size != 8:
            raise ValueError("FairnessStratifiedBatchSampler requires batch size 8.")

        missing_positive_pools = [
            identity
            for identity in self.identity_names
            if identity not in self.identity_subgroup_positive_pools
        ]
        empty_bpsn_pools = [
            identity
            for identity, positions in self.identity_bpsn_pools.items()
            if len(positions) == 0
        ]
        empty_subgroup_positive_pools = [
            identity
            for identity, positions in self.identity_subgroup_positive_pools.items()
            if len(positions) == 0
        ]

        if not self.identity_names or missing_positive_pools:
            raise ValueError(
                "Missing toxic subgroup pools for identities: "
                f"{missing_positive_pools}"
            )

        if (
            len(self.background_positive_pool) == 0
            or empty_bpsn_pools
            or empty_subgroup_positive_pools
        ):
            raise ValueError(
                "Cannot construct identity-balanced fairness batches with empty "
                f"pools: background_positive={len(self.background_positive_pool)}, "
                f"identity_bpsn={empty_bpsn_pools}, "
                f"identity_subgroup_positive={empty_subgroup_positive_pools}"
            )

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        for _ in range(self.num_batches):
            benign_identities = self.rng.choice(
                self.identity_names,
                size=4,
                replace=True,
            )
            toxic_identities = self.rng.choice(
                self.identity_names,
                size=2,
                replace=True,
            )

            benign_subgroup_positions = np.asarray(
                [
                    self.rng.choice(self.identity_bpsn_pools[identity])
                    for identity in benign_identities
                ],
                dtype=np.int64,
            )
            toxic_subgroup_positions = np.asarray(
                [
                    self.rng.choice(self.identity_subgroup_positive_pools[identity])
                    for identity in toxic_identities
                ],
                dtype=np.int64,
            )
            background_positive_positions = self.rng.choice(
                self.background_positive_pool,
                size=2,
                replace=True,
            )

            batch = np.concatenate(
                [
                    benign_subgroup_positions,
                    background_positive_positions,
                    toxic_subgroup_positions,
                ]
            )
            self.rng.shuffle(batch)
            yield batch.tolist()


train_loader = DataLoader(
    train_dataset,
    batch_sampler=FairnessStratifiedBatchSampler(
        identity_bpsn_pools,
        background_positive_pool,
        identity_subgroup_positive_pools,
        batch_size=TRAIN_BATCH_SIZE,
        seed=SEED,
    ),
    num_workers=NUM_WORKERS,
    pin_memory=amp_enabled,
    persistent_workers=NUM_WORKERS > 0,
    collate_fn=toxicity_collate,
)

scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)
base_learning_rates = [float(group["lr"]) for group in optimizer.param_groups]


def move_batch_to_device(batch):
    return {
        name: value.to(device, non_blocking=amp_enabled)
        for name, value in batch.items()
    }


def run_inference(texts, numeric_features, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)

    if positions.min() < 0 or positions.max() >= len(texts):
        raise IndexError("Candidate runtime supplied out-of-range positional indices.")

    inference_dataset = ToxicityTextDataset(
        texts=texts,
        numeric_features=numeric_features,
        positions=positions,
    )

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=EVAL_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=amp_enabled,
        persistent_workers=False,
        collate_fn=toxicity_collate,
    )

    previous_training_state = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                batch = move_batch_to_device(batch)

                with torch.cuda.amp.autocast(enabled=amp_enabled):
                    outputs = model(
                        input_ids=batch["input_ids"],
                        attention_mask=batch["attention_mask"],
                        numeric_features=batch["numeric_features"],
                    )
                    probabilities = torch.sigmoid(outputs["toxicity_logits"])

                predictions.append(probabilities.float().cpu().numpy())
    finally:
        model.train(previous_training_state)

    return np.concatenate(predictions, axis=0).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return run_inference(valid_texts, X_valid_numeric, positional_indices)


def predict_test(positional_indices):
    return run_inference(test_texts, X_test_numeric, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
            "numeric_feature_dim": int(NUMERIC_FEATURE_DIM),
            "identity_target_dim": int(IDENTITY_TARGET_DIM),
        },
        checkpoint_dir / "model_state.pt",
    )

    model.backbone.config.to_json_file(str(checkpoint_dir / "backbone_config.json"))
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    feature_state_source = WORKING_DIR / "feature_engineering_state.json"
    if feature_state_source.exists():
        shutil.copy2(
            feature_state_source,
            checkpoint_dir / "feature_engineering_state.json",
        )
    else:
        with open(
            checkpoint_dir / "feature_engineering_state.json",
            "w",
            encoding="utf-8",
        ) as handle:
            json.dump(
                {
                    "feature_columns": TEXT_FEATURE_COLUMNS,
                    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
                },
                handle,
            )

    with open(checkpoint_dir / "inference_state.json", "w", encoding="utf-8") as handle:
        json.dump(
            {
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "numeric_feature_dim": int(NUMERIC_FEATURE_DIM),
                "identity_target_dim": int(IDENTITY_TARGET_DIM),
                "prediction_transform": "sigmoid(toxicity_logits)",
            },
            handle,
        )


def load_checkpoint(directory):
    global tokenizer

    checkpoint_dir = Path(directory)
    checkpoint = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=device,
        weights_only=False,
    )

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)

    tokenizer = AutoTokenizer.from_pretrained(
        checkpoint_dir / "tokenizer",
        local_files_only=True,
    )

    with open(checkpoint_dir / "inference_state.json", "r", encoding="utf-8") as handle:
        inference_state = json.load(handle)

    if int(inference_state["max_sequence_length"]) != MAX_SEQUENCE_LENGTH:
        raise ValueError(
            "Checkpoint sequence length does not match inference configuration."
        )

    if int(inference_state["numeric_feature_dim"]) != int(NUMERIC_FEATURE_DIM):
        raise ValueError("Checkpoint numeric feature dimension does not match.")

    if int(inference_state["identity_target_dim"]) != int(IDENTITY_TARGET_DIM):
        raise ValueError("Checkpoint identity target dimension does not match.")


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
optimizer_steps = 0
stop_requested = False

for _ in range(MAX_EPOCHS):
    if stop_requested:
        break

    model.train()
    accumulated_batches = 0

    for batch in train_loader:
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
            )

            loss, _ = criterion(
                outputs=outputs,
                toxicity_targets=batch["toxicity_targets"],
                sample_weights=batch["sample_weights"],
                identity_targets=batch["identity_targets"],
            )

            scaled_loss = loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(scaled_loss):
            optimizer.zero_grad(set_to_none=True)
            accumulated_batches = 0
            continue

        scaler.scale(scaled_loss).backward()
        accumulated_batches += 1

        if accumulated_batches < GRADIENT_ACCUMULATION_STEPS:
            continue

        warmup_scale = min(1.0, float(optimizer_steps + 1) / WARMUP_UPDATES)
        for parameter_group, base_lr in zip(
            optimizer.param_groups,
            base_learning_rates,
        ):
            parameter_group["lr"] = base_lr * warmup_scale

        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        accumulated_batches = 0
        optimizer_steps += 1
        stop_requested = session.step()

        if stop_requested:
            break

    if not stop_requested and accumulated_batches > 0:
        residual_scale = GRADIENT_ACCUMULATION_STEPS / accumulated_batches
        warmup_scale = min(1.0, float(optimizer_steps + 1) / WARMUP_UPDATES)

        for parameter_group, base_lr in zip(
            optimizer.param_groups,
            base_learning_rates,
        ):
            parameter_group["lr"] = base_lr * warmup_scale

        scaler.unscale_(optimizer)

        for parameter in model.parameters():
            if parameter.grad is not None:
                parameter.grad.mul_(residual_scale)

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        optimizer_steps += 1
        stop_requested = session.step()

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
