import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import re
import html
import json
import math
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import AutoModel, AutoTokenizer

from engine.candidate_runtime import CandidateSession


# ----------------------------- reproducibility ----------------------------- #
SEED = 2027
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
USE_CUDA = DEVICE.type == "cuda"

MODEL_NAME = "answerdotai/ModernBERT-large"
MAX_LENGTH = 192
TRAIN_BATCH_SIZE = 8 if USE_CUDA else 2
INFER_BATCH_SIZE = 16 if USE_CUDA else 4
ACCUM_STEPS = 2 if USE_CUDA else 1
NUM_WORKERS = 2

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
SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]


# --------------------------- static text processing ------------------------ #
_url_re = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
_space_re = re.compile(r"\s+")


def normalize_text(x):
    """Deterministic, non-fitted normalization shared by train/valid/test."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return ""
    s = html.unescape(str(x))
    s = _url_re.sub(" [URL] ", s)
    s = s.replace("\u200b", " ").replace("\ufeff", " ")
    return _space_re.sub(" ", s).strip()


# ------------------------------ model -------------------------------------- #
class FairModernBERT(nn.Module):
    """
    Shared contextual encoder with toxicity, toxicity-context, and identity heads.
    The identity head is auxiliary only: test predictions always come from the
    learned toxicity head.
    """

    def __init__(self, model_name, n_identities):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden = self.encoder.config.hidden_size
        self.dropout = nn.Dropout(0.10)
        self.head = nn.Linear(hidden, 1 + len(SUBTYPE_COLUMNS) + n_identities)

        if hasattr(self.encoder, "gradient_checkpointing_enable"):
            self.encoder.gradient_checkpointing_enable()

    def forward(self, input_ids, attention_mask):
        out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        # ModernBERT's first token is its trained sequence representation.
        pooled = out.last_hidden_state[:, 0]
        return self.head(self.dropout(pooled))


class IndexDataset(Dataset):
    def __init__(self, n_rows):
        self.n_rows = n_rows

    def __len__(self):
        return self.n_rows

    def __getitem__(self, index):
        return index


def collate_indices(rows):
    return np.asarray(rows, dtype=np.int64)


# ------------------------------ losses ------------------------------------- #
def pair_ranking_loss(pos_logits, neg_logits, margin=0.15):
    """
    Logistic surrogate for AUC ordering: all positive examples should rank above
    all negative examples in a metric-critical slice.
    """
    if pos_logits.numel() == 0 or neg_logits.numel() == 0:
        return pos_logits.sum() * 0.0 + neg_logits.sum() * 0.0
    differences = neg_logits[:, None] - pos_logits[None, :] + margin
    return F.softplus(differences).mean()


def masked_bce(logits, labels, valid_mask):
    if valid_mask.sum().item() == 0:
        return logits.sum() * 0.0
    return F.binary_cross_entropy_with_logits(
        logits[valid_mask], labels[valid_mask], reduction="mean"
    )


# --------------------------- runtime and split ----------------------------- #
session = CandidateSession.from_env()

train_full = pd.read_csv("./input/train.csv", low_memory=False)
test_full = pd.read_csv("./input/test.csv", low_memory=False)

# Required split before any fitted transform or sampling statistic.
train_df, valid_df, test_df = session.split(train_full, test_full)

for frame in (train_df, valid_df, test_df):
    frame["comment_text"] = frame["comment_text"].fillna("").astype(str)

available_id_cols = [c for c in IDENTITY_COLUMNS if c in train_df.columns]
if len(available_id_cols) == 0:
    raise RuntimeError("Identity columns are required for fairness-aware training.")

available_subtype_cols = [c for c in SUBTYPE_COLUMNS if c in train_df.columns]

train_texts = train_df["comment_text"].to_numpy(dtype=object)
valid_texts = valid_df["comment_text"].to_numpy(dtype=object)
test_texts = test_df["comment_text"].to_numpy(dtype=object)

target_train = train_df["target"].fillna(0.0).to_numpy(dtype=np.float32)
id_train_raw = train_df[available_id_cols].to_numpy(dtype=np.float32)
id_train_finite = np.isfinite(id_train_raw)
id_train = np.nan_to_num(id_train_raw, nan=0.0)
id_known = id_train_finite.any(axis=1)
any_identity = (id_train >= 0.5).any(axis=1)

subtype_train = np.full((len(train_df), len(SUBTYPE_COLUMNS)), np.nan, dtype=np.float32)
for j, col in enumerate(SUBTYPE_COLUMNS):
    if col in train_df.columns:
        subtype_train[:, j] = train_df[col].to_numpy(dtype=np.float32)

# Four metric-oriented strata:
# benign identity, toxic non-identity, toxic identity, benign non-identity.
toxic_bin = target_train >= 0.5
group = np.full(len(train_df), 3, dtype=np.int64)
group[id_known & any_identity & ~toxic_bin] = 0
group[id_known & ~any_identity & toxic_bin] = 1
group[id_known & any_identity & toxic_bin] = 2

# Conservative desired exposure avoids repeatedly replaying scarce examples too
# aggressively, while improving the samples driving BPSN/BNSP.
desired_mix = np.array([0.16, 0.18, 0.12, 0.54], dtype=np.float64)
counts = np.bincount(group, minlength=4).astype(np.float64)
group_weight = desired_mix / np.maximum(counts, 1.0)
group_weight /= np.average(group_weight[group])

# Mild rare-identity support improves the -5 generalized mean without allowing
# a single scarce subgroup to dominate training.
identity_counts = np.maximum(id_train_finite.sum(axis=0), 1.0)
reference_count = np.median(identity_counts)
rarity_per_identity = np.clip((reference_count / identity_counts) ** 0.30, 0.75, 1.80)
row_rarity = np.ones(len(train_df), dtype=np.float64)
if len(available_id_cols):
    row_rarity = np.maximum(
        1.0, (id_train >= 0.5).astype(np.float64).dot(rarity_per_identity)
    )
    row_rarity = np.clip(row_rarity, 1.0, 1.65)

sample_weights = group_weight[group] * row_rarity
sample_weights = np.clip(sample_weights, 0.55, 3.25)
sample_weights = torch.as_tensor(sample_weights, dtype=torch.double)

sampler = WeightedRandomSampler(
    weights=sample_weights,
    num_samples=len(train_df),
    replacement=True,
)

train_loader = DataLoader(
    IndexDataset(len(train_df)),
    batch_size=TRAIN_BATCH_SIZE,
    sampler=sampler,
    num_workers=NUM_WORKERS,
    collate_fn=collate_indices,
    pin_memory=USE_CUDA,
    persistent_workers=True,
    prefetch_factor=2,
    drop_last=True,
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
model = FairModernBERT(MODEL_NAME, len(available_id_cols)).to(DEVICE)
optimizer = AdamW(model.parameters(), lr=1.5e-5, weight_decay=0.01)


def tokenize_batch(text_array):
    cleaned = [normalize_text(x) for x in text_array]
    encoded = tokenizer(
        cleaned,
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )
    return {
        "input_ids": encoded["input_ids"].to(DEVICE, non_blocking=True),
        "attention_mask": encoded["attention_mask"].to(DEVICE, non_blocking=True),
    }


def predict_text_positions(texts, positions):
    """
    Common learned-model inference used identically for validation and test.
    Positions are supplied by CandidateSession and are positional, not IDs.
    """
    positions = np.asarray(positions, dtype=np.int64)
    old_mode = model.training
    model.eval()
    output = []

    try:
        with torch.inference_mode():
            for start in range(0, len(positions), INFER_BATCH_SIZE):
                pos = positions[start : start + INFER_BATCH_SIZE]
                batch = tokenize_batch(texts[pos])
                with torch.autocast(
                    device_type="cuda",
                    dtype=torch.bfloat16,
                    enabled=USE_CUDA,
                ):
                    logits = model(**batch)[:, 0]
                output.append(torch.sigmoid(logits).float().cpu().numpy())
    finally:
        model.train(old_mode)

    if not output:
        return np.empty(0, dtype=np.float64)
    return np.concatenate(output).astype(np.float64, copy=False)


def predict_validation(positions):
    return predict_text_positions(valid_texts, positions)


def predict_test(positions):
    return predict_text_positions(test_texts, positions)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    torch.save(model.state_dict(), directory / "fair_modernbert_state.pt")
    model.encoder.config.save_pretrained(directory / "encoder_config")
    tokenizer.save_pretrained(directory / "tokenizer")

    with open(directory / "inference_config.json", "w") as f:
        json.dump(
            {
                "model_name": MODEL_NAME,
                "max_length": MAX_LENGTH,
                "identity_columns": available_id_cols,
                "subtype_columns": SUBTYPE_COLUMNS,
                "normalization": "html_unescape_url_token_whitespace",
            },
            f,
        )


def load_checkpoint(directory):
    global tokenizer
    directory = Path(directory)
    state = torch.load(
        directory / "fair_modernbert_state.pt",
        map_location=DEVICE,
    )
    # The existing model object is restored in place, preserving optimizer links.
    model.load_state_dict(state, strict=True)
    tokenizer = AutoTokenizer.from_pretrained(directory / "tokenizer", use_fast=True)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())


# ------------------------------ training ----------------------------------- #
optimizer_steps = 0
stop_training = False
model.train()
optimizer.zero_grad(set_to_none=True)

while not stop_training:
    for batch_indices in train_loader:
        batch = tokenize_batch(train_texts[batch_indices])

        y = torch.as_tensor(
            target_train[batch_indices], dtype=torch.float32, device=DEVICE
        ).clamp(0.0, 1.0)
        ids = torch.as_tensor(
            id_train[batch_indices], dtype=torch.float32, device=DEVICE
        ).clamp(0.0, 1.0)
        id_mask = torch.as_tensor(
            id_train_finite[batch_indices], dtype=torch.bool, device=DEVICE
        )
        subtype_y = torch.as_tensor(
            subtype_train[batch_indices], dtype=torch.float32, device=DEVICE
        )
        known = torch.as_tensor(
            id_known[batch_indices], dtype=torch.bool, device=DEVICE
        )
        has_identity = torch.as_tensor(
            any_identity[batch_indices], dtype=torch.bool, device=DEVICE
        )
        toxic = y >= 0.5

        # More certain soft labels are slightly emphasized, preserving the
        # fractional annotation semantics rather than converting all labels.
        confidence = 0.70 + torch.abs(y - 0.5)

        with torch.autocast(
            device_type="cuda",
            dtype=torch.bfloat16,
            enabled=USE_CUDA,
        ):
            logits = model(**batch)
            tox_logits = logits[:, 0]
            subtype_logits = logits[:, 1 : 1 + len(SUBTYPE_COLUMNS)]
            identity_logits = logits[:, 1 + len(SUBTYPE_COLUMNS) :]

            tox_per_row = F.binary_cross_entropy_with_logits(
                tox_logits, y, reduction="none"
            )
            toxicity_loss = (tox_per_row * confidence).mean()

            subtype_valid = torch.isfinite(subtype_y)
            subtype_loss = masked_bce(
                subtype_logits,
                torch.nan_to_num(subtype_y, nan=0.0).clamp(0.0, 1.0),
                subtype_valid,
            )

            identity_loss = masked_bce(identity_logits, ids, id_mask)

            # AUC-aligned fairness ranking terms:
            # BPSN: toxic background > benign subgroup
            bpsn = pair_ranking_loss(
                tox_logits[known & ~has_identity & toxic],
                tox_logits[known & has_identity & ~toxic],
            )
            # BNSP: toxic subgroup > benign background
            bnsp = pair_ranking_loss(
                tox_logits[known & has_identity & toxic],
                tox_logits[known & ~has_identity & ~toxic],
            )
            # Subgroup AUC: toxic subgroup > benign subgroup
            subgroup = pair_ranking_loss(
                tox_logits[known & has_identity & toxic],
                tox_logits[known & has_identity & ~toxic],
            )

            fairness_loss = (bpsn + bnsp + subgroup) / 3.0
            loss = (
                toxicity_loss
                + 0.16 * subtype_loss
                + 0.06 * identity_loss
                + 0.14 * fairness_loss
            ) / ACCUM_STEPS

        loss.backward()

        if (optimizer_steps + 1) % ACCUM_STEPS == 0:
            # Short warmup stabilizes the newly initialized multi-task heads.
            actual_update = optimizer_steps // ACCUM_STEPS + 1
            warmup_scale = min(1.0, actual_update / 100.0)
            for param_group in optimizer.param_groups:
                param_group["lr"] = 1.5e-5 * warmup_scale

            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)

            stop_training = session.step()
            if stop_training:
                break

        optimizer_steps += 1

    if stop_training:
        break

# CandidateSession performs official Jigsaw continuous-AUC validation, restores
# its chosen checkpoint, and writes ./submission/submission.csv.
result = session.finish()
print("Final Validation Score:", result["best_validation_score"])
print("Submission:", result["submission_path"])
