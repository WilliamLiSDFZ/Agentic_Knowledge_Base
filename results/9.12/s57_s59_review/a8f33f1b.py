import gc
import html
import json
import math
import os
import random
import re
import shutil
import unicodedata
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from engine.candidate_runtime import CandidateSession
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from torch.cuda.amp import GradScaler, autocast
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)


# =============================================================================
# Configuration
# =============================================================================

SEED = 2025
MODEL_SEED = 2025

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

SCORED_IDENTITY_COLUMNS = [
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

TEXT_FEATURE_NAMES = [
    "log_char_count",
    "log_word_count",
    "mean_word_length",
    "unique_word_ratio",
    "uppercase_letter_ratio",
    "digit_ratio",
    "punctuation_ratio",
    "exclamation_ratio",
    "question_ratio",
    "log_newline_count",
    "log_url_count",
    "log_email_count",
    "log_user_mention_count",
    "log_repeated_punctuation_count",
    "log_repeated_character_count",
    "non_ascii_ratio",
    "quote_ratio",
    "whitespace_ratio",
]

MAX_LENGTH = 256
POINTWISE_LOSS_WEIGHT = 0.25
PAIRWISE_LOSS_WEIGHT = 0.75
BACKBONE_LEARNING_RATE = 8e-6
HEAD_LEARNING_RATE = 4e-5
WEIGHT_DECAY = 0.01

TRAIN_MICRO_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 48
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 2
MAX_OPTIMIZER_STEPS_FOR_SCHEDULE = 20_000
WARMUP_OPTIMIZER_STEPS = 200
MAX_GRADIENT_NORM = 1.0
LOSS_STATE_LOG_INTERVAL_STEPS = 100

NUM_WORKERS = max(2, min(4, os.cpu_count() or 2))

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(MODEL_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(MODEL_SEED)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
PIN_MEMORY = device.type == "cuda"

if device.type == "cuda":
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

if hasattr(torch, "set_float32_matmul_precision"):
    torch.set_float32_matmul_precision("high")

if TRAIN_MICRO_BATCH_SIZE < 5:
    raise ValueError(
        "Training batches require at least four metric-cell rows and one "
        "global-partition row."
    )


# =============================================================================
# Runtime-owned split
# =============================================================================

session = CandidateSession.from_env()

train_path = INPUT_DIR / "train.csv"
test_path = INPUT_DIR / "test.csv"

if not train_path.exists():
    raise FileNotFoundError(f"Missing training file: {train_path}")
if not test_path.exists():
    raise FileNotFoundError(f"Missing test file: {test_path}")

train_df = pd.read_csv(train_path, low_memory=False)
test_df = pd.read_csv(test_path, low_memory=False)

# The runtime contract owns the only validation split. This occurs before any
# fitted transformation or training-derived statistic is computed.
train_df, valid_df, test_df = session.split(train_df, test_df)

required_train_columns = {"id", "comment_text", "target"}
required_test_columns = {"id", "comment_text"}

missing_train_columns = required_train_columns.difference(train_df.columns)
missing_valid_columns = required_train_columns.difference(valid_df.columns)
missing_test_columns = required_test_columns.difference(test_df.columns)

if missing_train_columns:
    raise ValueError(
        f"Training partition is missing columns: {sorted(missing_train_columns)}"
    )
if missing_valid_columns:
    raise ValueError(
        f"Validation partition is missing columns: {sorted(missing_valid_columns)}"
    )
if missing_test_columns:
    raise ValueError(
        f"Test partition is missing columns: {sorted(missing_test_columns)}"
    )

missing_train_identities = [
    column for column in SCORED_IDENTITY_COLUMNS if column not in train_df.columns
]
missing_valid_identities = [
    column for column in SCORED_IDENTITY_COLUMNS if column not in valid_df.columns
]

if missing_train_identities or missing_valid_identities:
    raise ValueError(
        "Missing scored identity columns. "
        f"train={missing_train_identities}, valid={missing_valid_identities}"
    )


# =============================================================================
# Text normalization and leakage-safe style features
# =============================================================================

URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b")
WORD_RE = re.compile(r"\b[\w']+\b", flags=re.UNICODE)
USER_MENTION_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_]{1,32}")
REPEATED_PUNCT_RE = re.compile(r"([!?.,;:])\1+")
REPEATED_CHAR_RE = re.compile(r"([A-Za-z])\1{2,}", flags=re.IGNORECASE)
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
WHITESPACE_RE = re.compile(r"\s+")


def normalize_text_and_extract_features(text):
    if text is None or (isinstance(text, float) and np.isnan(text)):
        text = ""
    elif not isinstance(text, str):
        text = str(text)

    text = unicodedata.normalize("NFKC", html.unescape(text))
    text = CONTROL_RE.sub(" ", text)

    char_count = len(text)
    safe_char_count = max(char_count, 1)

    words = WORD_RE.findall(text)
    word_count = len(words)

    if word_count:
        total_word_characters = sum(len(word) for word in words)
        mean_word_length = total_word_characters / word_count
        unique_word_ratio = len({word.casefold() for word in words}) / word_count
    else:
        mean_word_length = 0.0
        unique_word_ratio = 0.0

    letter_count = 0
    uppercase_count = 0
    digit_count = 0
    punctuation_count = 0
    non_ascii_count = 0
    quote_count = 0
    whitespace_count = 0

    for character in text:
        if character.isalpha():
            letter_count += 1
            if character.isupper():
                uppercase_count += 1

        if character.isdigit():
            digit_count += 1

        if unicodedata.category(character).startswith("P"):
            punctuation_count += 1

        if ord(character) > 127:
            non_ascii_count += 1

        if character in "\"'`“”‘’":
            quote_count += 1

        if character.isspace():
            whitespace_count += 1

    url_count = len(URL_RE.findall(text))
    email_count = len(EMAIL_RE.findall(text))
    mention_count = len(USER_MENTION_RE.findall(text))
    repeated_punctuation_count = len(REPEATED_PUNCT_RE.findall(text))
    repeated_character_count = len(REPEATED_CHAR_RE.findall(text))

    features = np.asarray(
        [
            np.log1p(char_count),
            np.log1p(word_count),
            min(mean_word_length, 30.0),
            unique_word_ratio,
            uppercase_count / max(letter_count, 1),
            digit_count / safe_char_count,
            punctuation_count / safe_char_count,
            text.count("!") / safe_char_count,
            text.count("?") / safe_char_count,
            np.log1p(text.count("\n")),
            np.log1p(url_count),
            np.log1p(email_count),
            np.log1p(mention_count),
            np.log1p(repeated_punctuation_count),
            np.log1p(repeated_character_count),
            non_ascii_count / safe_char_count,
            quote_count / safe_char_count,
            whitespace_count / safe_char_count,
        ],
        dtype=np.float32,
    )

    # Preserve case, punctuation, profanity, identity expressions, and common
    # obfuscations while canonicalizing transport-related tokens.
    normalized_text = URL_RE.sub(" [URL] ", text)
    normalized_text = EMAIL_RE.sub(" [EMAIL] ", normalized_text)
    normalized_text = USER_MENTION_RE.sub(" [USER] ", normalized_text)
    normalized_text = WHITESPACE_RE.sub(" ", normalized_text).strip()

    return normalized_text, features


def process_text_partition(frame):
    row_count = len(frame)
    normalized_texts = np.empty(row_count, dtype=object)
    feature_matrix = np.empty(
        (row_count, len(TEXT_FEATURE_NAMES)),
        dtype=np.float32,
    )

    text_values = frame["comment_text"].to_numpy(copy=False)

    for row_index, text in enumerate(text_values):
        normalized_text, features = normalize_text_and_extract_features(text)
        normalized_texts[row_index] = normalized_text
        feature_matrix[row_index] = features

    frame["comment_text"] = normalized_texts
    return feature_matrix


train_text_features_raw = process_text_partition(train_df)
valid_text_features_raw = process_text_partition(valid_df)
test_text_features_raw = process_text_partition(test_df)

# The scaler is fitted only on the runtime-provided training partition.
text_feature_scaler = StandardScaler(copy=True)

train_text_features = text_feature_scaler.fit_transform(train_text_features_raw).astype(
    np.float32, copy=False
)

valid_text_features = text_feature_scaler.transform(valid_text_features_raw).astype(
    np.float32, copy=False
)

test_text_features = text_feature_scaler.transform(test_text_features_raw).astype(
    np.float32, copy=False
)

del train_text_features_raw
del valid_text_features_raw
del test_text_features_raw
gc.collect()


# =============================================================================
# Targets and exact evaluator-defined metric cells
# =============================================================================

train_soft_targets = (
    pd.to_numeric(train_df["target"], errors="coerce")
    .fillna(0.0)
    .clip(0.0, 1.0)
    .to_numpy(dtype=np.float32)
)

valid_soft_targets = (
    pd.to_numeric(valid_df["target"], errors="coerce")
    .fillna(0.0)
    .clip(0.0, 1.0)
    .to_numpy(dtype=np.float32)
)

# Hard labels are used only to reproduce evaluator masks and pair pools.
train_binary_targets = (train_soft_targets >= 0.5).astype(np.uint8)
valid_binary_targets = (valid_soft_targets >= 0.5).astype(np.uint8)


def build_metric_cell_codes(frame, binary_targets):
    """
    Cell codes for every row and scored identity:

      0 = identity annotation unavailable
      1 = subgroup positive: identity >= 0.5 and toxic
      2 = subgroup negative: identity >= 0.5 and non-toxic
      3 = background positive: known identity < 0.5 and toxic
      4 = background negative: known identity < 0.5 and non-toxic

    Unannotated identities are not treated as confirmed background examples.
    """

    identity_values = (
        frame[SCORED_IDENTITY_COLUMNS]
        .apply(pd.to_numeric, errors="coerce")
        .to_numpy(dtype=np.float32)
    )

    identity_known = np.isfinite(identity_values)
    subgroup = identity_known & (identity_values >= 0.5)
    background = identity_known & ~subgroup

    toxic = binary_targets.astype(bool)[:, None]
    non_toxic = ~toxic

    cell_codes = np.zeros(identity_values.shape, dtype=np.uint8)
    cell_codes[subgroup & toxic] = 1
    cell_codes[subgroup & non_toxic] = 2
    cell_codes[background & toxic] = 3
    cell_codes[background & non_toxic] = 4

    identity_values = np.nan_to_num(
        identity_values,
        nan=-1.0,
        posinf=1.0,
        neginf=0.0,
    ).astype(np.float32, copy=False)

    return cell_codes, identity_values


train_metric_cell_codes, train_identity_values = build_metric_cell_codes(
    train_df,
    train_binary_targets,
)

valid_metric_cell_codes, valid_identity_values = build_metric_cell_codes(
    valid_df,
    valid_binary_targets,
)

if "toxicity_annotator_count" in train_df.columns:
    train_toxicity_annotator_count = (
        pd.to_numeric(
            train_df["toxicity_annotator_count"],
            errors="coerce",
        )
        .fillna(0)
        .clip(lower=0)
        .to_numpy(dtype=np.float32)
    )
else:
    train_toxicity_annotator_count = np.zeros(
        len(train_df),
        dtype=np.float32,
    )

if "toxicity_annotator_count" in valid_df.columns:
    valid_toxicity_annotator_count = (
        pd.to_numeric(
            valid_df["toxicity_annotator_count"],
            errors="coerce",
        )
        .fillna(0)
        .clip(lower=0)
        .to_numpy(dtype=np.float32)
    )
else:
    valid_toxicity_annotator_count = np.zeros(
        len(valid_df),
        dtype=np.float32,
    )


# =============================================================================
# Persist preprocessing artifacts
# =============================================================================

joblib.dump(
    text_feature_scaler,
    WORKING_DIR / "text_feature_scaler.joblib",
)

np.save(
    WORKING_DIR / "train_text_features.npy",
    train_text_features,
)
np.save(
    WORKING_DIR / "valid_text_features.npy",
    valid_text_features,
)
np.save(
    WORKING_DIR / "test_text_features.npy",
    test_text_features,
)

np.savez(
    WORKING_DIR / "train_supervision_and_cells.npz",
    target_soft=train_soft_targets,
    target_binary=train_binary_targets,
    metric_cell_codes=train_metric_cell_codes,
    identity_values=train_identity_values,
    toxicity_annotator_count=train_toxicity_annotator_count,
)

np.savez(
    WORKING_DIR / "valid_supervision_and_cells.npz",
    target_soft=valid_soft_targets,
    target_binary=valid_binary_targets,
    metric_cell_codes=valid_metric_cell_codes,
    identity_values=valid_identity_values,
    toxicity_annotator_count=valid_toxicity_annotator_count,
)

artifact_manifest = {
    "seed": SEED,
    "text_column": "comment_text",
    "target_column": "target",
    "target_training_semantics": "fractional_soft_target",
    "metric_target_threshold": 0.5,
    "identity_threshold": 0.5,
    "scored_identity_columns": SCORED_IDENTITY_COLUMNS,
    "text_feature_names": TEXT_FEATURE_NAMES,
    "metric_cell_codes": {
        "0": "identity_unknown",
        "1": "subgroup_positive",
        "2": "subgroup_negative",
        "3": "background_positive",
        "4": "background_negative",
    },
    "partition_rows": {
        "train": int(len(train_df)),
        "validation": int(len(valid_df)),
        "test": int(len(test_df)),
    },
    "partition_id_order_preserved": True,
    "scaler_fit_partition": "train_only",
    "normalization": {
        "unicode": "NFKC",
        "html_unescape": True,
        "control_characters_replaced": True,
        "urls_replaced_with": "[URL]",
        "emails_replaced_with": "[EMAIL]",
        "user_mentions_replaced_with": "[USER]",
        "whitespace_collapsed": True,
    },
}

with open(
    WORKING_DIR / "data_processing_manifest.json",
    "w",
    encoding="utf-8",
) as manifest_file:
    json.dump(
        artifact_manifest,
        manifest_file,
        indent=2,
        sort_keys=True,
    )

# Keep compact independent arrays, allowing the original wide frames and
# unused diagnostic arrays to be released before model training.
train_texts = train_df["comment_text"].to_numpy(dtype=object, copy=True)
valid_texts = valid_df["comment_text"].to_numpy(dtype=object, copy=True)
test_texts = test_df["comment_text"].to_numpy(dtype=object, copy=True)
train_ids_for_session = train_df["id"].astype(str).tolist()
valid_ids_for_metric = valid_df["id"].astype(str).to_numpy(copy=True)

del train_text_features
del valid_text_features
del test_text_features
del train_identity_values
del valid_identity_values
del train_toxicity_annotator_count
del valid_toxicity_annotator_count
del train_binary_targets
del valid_soft_targets
del train_df
del valid_df
del test_df
gc.collect()


# =============================================================================
# ModernBERT model
# =============================================================================

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Choose one model class according to your task:
model = ModernBertForSequenceClassification.from_pretrained(
    model_id
)  # for classification
# model = ModernBertForMaskedLM.from_pretrained(model_id)  # for masked language modeling
# model = ModernBertForTokenClassification.from_pretrained(model_id)  # for token classification/NER
# model = ModernBertForQuestionAnswering.from_pretrained(model_id)  # for question answering
# model = ModernBertForMultipleChoice.from_pretrained(model_id)  # for multiple choice tasks

tokenizer.model_max_length = MAX_LENGTH
tokenizer.padding_side = "right"
tokenizer.truncation_side = "right"

if not hasattr(model, "classifier"):
    raise AttributeError(
        "ModernBERT sequence classifier does not expose a classifier layer."
    )

if not hasattr(model.classifier, "in_features"):
    raise AttributeError(
        "ModernBERT classifier does not expose its input feature dimension."
    )

classifier_input_features = model.classifier.in_features
model.classifier = nn.Linear(classifier_input_features, 1)

nn.init.normal_(
    model.classifier.weight,
    mean=0.0,
    std=float(getattr(model.config, "initializer_range", 0.02)),
)
nn.init.zeros_(model.classifier.bias)

classifier_dropout = 0.15

model.config.num_labels = 1
model.config.id2label = {0: "TOXICITY"}
model.config.label2id = {"TOXICITY": 0}
model.config.problem_type = None
model.config.classifier_dropout = classifier_dropout

if hasattr(model, "num_labels"):
    model.num_labels = 1

if hasattr(model, "drop"):
    model.drop = nn.Dropout(classifier_dropout)
elif hasattr(model, "dropout"):
    model.dropout = nn.Dropout(classifier_dropout)

model.gradient_checkpointing_enable()
model.to(device)


# =============================================================================
# Metric-aligned group-robust pairwise objective
# =============================================================================


class GroupRobustPairwiseAUCLoss(nn.Module):
    """
    Stateful combined objective:

      * Bernoulli BCE using fractional toxicity votes.
      * Overall toxic/non-toxic logistic pair ranking.
      * Subgroup, BPSN, and BNSP logistic pair ranking.
      * Persistent exponentiated-gradient weights normalized within each
        nine-identity bias family.

    Every forward call caches detached observations. Persistent score
    statistics, risks, and dual logits are changed only by commit_state(),
    which the training loop calls after a successful optimizer step.

    Expected metric-cell codes:

      0 = identity unknown
      1 = subgroup positive
      2 = subgroup negative
      3 = background positive
      4 = background negative
    """

    def __init__(
        self,
        pointwise_weight=POINTWISE_LOSS_WEIGHT,
        pairwise_weight=PAIRWISE_LOSS_WEIGHT,
        pair_temperature=1.0,
        robust_temperature=0.25,
        max_examples_per_pool=24,
        score_ema_rate=0.05,
        risk_ema_rate=0.05,
        dual_learning_rate=0.025,
        minimum_dual_support=8,
        maximum_dual_logit=1.5,
    ):
        super().__init__()

        if pointwise_weight < 0.0 or pairwise_weight < 0.0:
            raise ValueError("Loss weights must be non-negative.")

        if pointwise_weight + pairwise_weight <= 0.0:
            raise ValueError("At least one loss weight must be positive.")

        if pair_temperature <= 0.0:
            raise ValueError("Pair temperature must be positive.")

        if robust_temperature <= 0.0:
            raise ValueError("Robust temperature must be positive.")

        if max_examples_per_pool < 1:
            raise ValueError("max_examples_per_pool must be positive.")

        if not 0.0 < score_ema_rate <= 1.0:
            raise ValueError("score_ema_rate must be in (0, 1].")

        if not 0.0 < risk_ema_rate <= 1.0:
            raise ValueError("risk_ema_rate must be in (0, 1].")

        if dual_learning_rate < 0.0:
            raise ValueError("dual_learning_rate must be non-negative.")

        if minimum_dual_support < 1:
            raise ValueError("minimum_dual_support must be positive.")

        if maximum_dual_logit <= 0.0:
            raise ValueError("maximum_dual_logit must be positive.")

        weight_sum = pointwise_weight + pairwise_weight

        self.pointwise_weight = float(pointwise_weight / weight_sum)
        self.pairwise_weight = float(pairwise_weight / weight_sum)
        self.pair_temperature = float(pair_temperature)
        self.robust_temperature = float(robust_temperature)
        self.max_examples_per_pool = int(max_examples_per_pool)
        self.score_ema_rate = float(score_ema_rate)
        self.risk_ema_rate = float(risk_ema_rate)
        self.dual_learning_rate = float(dual_learning_rate)
        self.minimum_dual_support = int(minimum_dual_support)
        self.maximum_dual_logit = float(maximum_dual_logit)
        self.identity_count = len(SCORED_IDENTITY_COLUMNS)
        self.cell_count = 1 + 3 * self.identity_count
        self.last_components = {}

        self.register_buffer(
            "positive_score_means",
            torch.zeros(self.cell_count, dtype=torch.float32),
        )
        self.register_buffer(
            "negative_score_means",
            torch.zeros(self.cell_count, dtype=torch.float32),
        )
        self.register_buffer(
            "positive_score_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
        )
        self.register_buffer(
            "negative_score_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
        )
        self.register_buffer(
            "running_surrogate_risks",
            torch.zeros(self.cell_count, dtype=torch.float32),
        )
        self.register_buffer(
            "running_risk_variances",
            torch.zeros(self.cell_count, dtype=torch.float32),
        )
        self.register_buffer(
            "risk_support_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
        )
        self.register_buffer(
            "cell_update_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
        )
        self.register_buffer(
            "family_dual_logits",
            torch.zeros(3, self.identity_count, dtype=torch.float32),
        )

        self.register_buffer(
            "pending_positive_score_sums",
            torch.zeros(self.cell_count, dtype=torch.float32),
            persistent=False,
        )
        self.register_buffer(
            "pending_negative_score_sums",
            torch.zeros(self.cell_count, dtype=torch.float32),
            persistent=False,
        )
        self.register_buffer(
            "pending_positive_score_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
            persistent=False,
        )
        self.register_buffer(
            "pending_negative_score_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
            persistent=False,
        )
        self.register_buffer(
            "pending_risk_sums",
            torch.zeros(self.cell_count, dtype=torch.float32),
            persistent=False,
        )
        self.register_buffer(
            "pending_risk_counts",
            torch.zeros(self.cell_count, dtype=torch.long),
            persistent=False,
        )

    def _pair_loss_from_scores(self, positive_scores, negative_scores):
        score_differences = (
            positive_scores[:, None] - negative_scores[None, :]
        ) / self.pair_temperature

        return F.softplus(-score_differences).mean()

    def _cell_pair_loss(self, scores, positive_mask, negative_mask, cell_index):
        positive_scores = scores[positive_mask]
        negative_scores = scores[negative_mask]

        with torch.no_grad():
            if positive_scores.numel():
                self.pending_positive_score_sums[cell_index].add_(
                    positive_scores.detach().sum()
                )
                self.pending_positive_score_counts[cell_index].add_(
                    positive_scores.numel()
                )

            if negative_scores.numel():
                self.pending_negative_score_sums[cell_index].add_(
                    negative_scores.detach().sum()
                )
                self.pending_negative_score_counts[cell_index].add_(
                    negative_scores.numel()
                )

        positive_scores = positive_scores[: self.max_examples_per_pool]
        negative_scores = negative_scores[: self.max_examples_per_pool]

        loss_terms = []
        loss_weights = []

        if positive_scores.numel() and negative_scores.numel():
            loss_terms.append(
                self._pair_loss_from_scores(
                    positive_scores,
                    negative_scores,
                )
            )
            loss_weights.append(
                float(positive_scores.numel() * negative_scores.numel())
            )

        if (
            positive_scores.numel()
            and self.negative_score_counts[cell_index].item() > 0
        ):
            running_negative_score = self.negative_score_means[
                cell_index
            ].detach().reshape(1)

            loss_terms.append(
                self._pair_loss_from_scores(
                    positive_scores,
                    running_negative_score,
                )
            )
            loss_weights.append(float(positive_scores.numel()))

        if (
            negative_scores.numel()
            and self.positive_score_counts[cell_index].item() > 0
        ):
            running_positive_score = self.positive_score_means[
                cell_index
            ].detach().reshape(1)

            loss_terms.append(
                self._pair_loss_from_scores(
                    running_positive_score,
                    negative_scores,
                )
            )
            loss_weights.append(float(negative_scores.numel()))

        if not loss_terms:
            return None

        total_weight = sum(loss_weights)
        cell_loss = sum(
            loss_term * loss_weight
            for loss_term, loss_weight in zip(loss_terms, loss_weights)
        ) / total_weight

        with torch.no_grad():
            self.pending_risk_sums[cell_index].add_(cell_loss.detach())
            self.pending_risk_counts[cell_index].add_(1)

        return cell_loss

    def _family_aggregate(self, family_losses, family_index):
        family_weights = torch.softmax(
            self.family_dual_logits[family_index],
            dim=0,
        )

        weighted_loss = family_weights.new_zeros(())
        available_weight = family_weights.new_zeros(())
        available_count = 0

        for identity_index, cell_loss in enumerate(family_losses):
            if cell_loss is None:
                continue

            weighted_loss = (
                weighted_loss + family_weights[identity_index] * cell_loss
            )
            available_weight = (
                available_weight + family_weights[identity_index]
            )
            available_count += 1

        if available_count == 0:
            return None

        return weighted_loss / available_weight.clamp_min(1e-12)

    @torch.no_grad()
    def discard_pending_state(self):
        self.pending_positive_score_sums.zero_()
        self.pending_negative_score_sums.zero_()
        self.pending_positive_score_counts.zero_()
        self.pending_negative_score_counts.zero_()
        self.pending_risk_sums.zero_()
        self.pending_risk_counts.zero_()

    @torch.no_grad()
    def commit_state(self):
        positive_observed = self.pending_positive_score_counts > 0
        negative_observed = self.pending_negative_score_counts > 0
        risk_observed = self.pending_risk_counts > 0

        positive_window_means = (
            self.pending_positive_score_sums
            / self.pending_positive_score_counts.clamp_min(1).to(torch.float32)
        )
        negative_window_means = (
            self.pending_negative_score_sums
            / self.pending_negative_score_counts.clamp_min(1).to(torch.float32)
        )

        positive_initialized = self.positive_score_counts > 0
        negative_initialized = self.negative_score_counts > 0

        positive_ema_means = (
            self.positive_score_means
            + self.score_ema_rate
            * (positive_window_means - self.positive_score_means)
        )
        negative_ema_means = (
            self.negative_score_means
            + self.score_ema_rate
            * (negative_window_means - self.negative_score_means)
        )

        positive_updates = torch.where(
            positive_initialized,
            positive_ema_means,
            positive_window_means,
        )
        negative_updates = torch.where(
            negative_initialized,
            negative_ema_means,
            negative_window_means,
        )

        self.positive_score_means.copy_(
            torch.where(
                positive_observed,
                positive_updates,
                self.positive_score_means,
            )
        )
        self.negative_score_means.copy_(
            torch.where(
                negative_observed,
                negative_updates,
                self.negative_score_means,
            )
        )

        self.positive_score_counts.add_(
            self.pending_positive_score_counts
        )
        self.negative_score_counts.add_(
            self.pending_negative_score_counts
        )

        risk_window_means = (
            self.pending_risk_sums
            / self.pending_risk_counts.clamp_min(1).to(torch.float32)
        )
        risk_initialized = self.risk_support_counts > 0
        risk_differences = (
            risk_window_means - self.running_surrogate_risks
        )

        risk_ema_updates = (
            self.running_surrogate_risks
            + self.risk_ema_rate * risk_differences
        )
        variance_ema_updates = (
            (1.0 - self.risk_ema_rate)
            * (
                self.running_risk_variances
                + self.risk_ema_rate * risk_differences.square()
            )
        )

        self.running_surrogate_risks.copy_(
            torch.where(
                risk_observed,
                torch.where(
                    risk_initialized,
                    risk_ema_updates,
                    risk_window_means,
                ),
                self.running_surrogate_risks,
            )
        )
        self.running_risk_variances.copy_(
            torch.where(
                risk_observed,
                torch.where(
                    risk_initialized,
                    variance_ema_updates,
                    torch.zeros_like(variance_ema_updates),
                ),
                self.running_risk_variances,
            )
        )
        self.risk_support_counts.add_(self.pending_risk_counts)
        self.cell_update_counts.add_(risk_observed.to(torch.long))

        for family_index in range(3):
            cell_start = 1 + family_index * self.identity_count
            cell_stop = cell_start + self.identity_count

            family_support = self.risk_support_counts[cell_start:cell_stop]
            family_positive_support = self.positive_score_counts[
                cell_start:cell_stop
            ]
            family_negative_support = self.negative_score_counts[
                cell_start:cell_stop
            ]

            eligible = (
                (family_support >= self.minimum_dual_support)
                & (family_positive_support > 0)
                & (family_negative_support > 0)
            )

            if not bool(eligible.any()):
                continue

            family_risks = self.running_surrogate_risks[
                cell_start:cell_stop
            ]
            eligible_risk_mean = family_risks[eligible].mean()
            centered_risks = family_risks - eligible_risk_mean

            eligible_indices = torch.nonzero(
                eligible,
                as_tuple=False,
            ).flatten()
            delta = (
                (
                    self.dual_learning_rate
                    / self.robust_temperature
                )
                * centered_risks[eligible]
            )
            family_logits = self.family_dual_logits[family_index]
            family_logits.index_add_(
                0,
                eligible_indices,
                delta,
            )

            self.family_dual_logits[family_index].sub_(
                self.family_dual_logits[family_index].mean()
            )
            self.family_dual_logits[family_index].clamp_(
                min=-self.maximum_dual_logit,
                max=self.maximum_dual_logit,
            )

        self.discard_pending_state()

    @torch.no_grad()
    def assert_nonuniform_dual_transition(
        self,
        risk_tolerance=1e-6,
        equality_tolerance=1e-9,
    ):
        transition_diagnostics = []

        for family_index in range(3):
            cell_start = 1 + family_index * self.identity_count
            cell_stop = cell_start + self.identity_count

            family_support = self.risk_support_counts[cell_start:cell_stop]
            family_positive_support = self.positive_score_counts[
                cell_start:cell_stop
            ]
            family_negative_support = self.negative_score_counts[
                cell_start:cell_stop
            ]
            eligible = (
                (family_support >= self.minimum_dual_support)
                & (family_positive_support > 0)
                & (family_negative_support > 0)
            )

            eligible_count = int(eligible.sum().item())
            family_risks = self.running_surrogate_risks[
                cell_start:cell_stop
            ]
            family_logits = self.family_dual_logits[family_index]
            family_weights = torch.softmax(family_logits, dim=0)

            if eligible_count:
                eligible_risks = family_risks[eligible]
                eligible_logits = family_logits[eligible]
                eligible_weights = family_weights[eligible]

                risk_range = float(
                    (eligible_risks.max() - eligible_risks.min()).item()
                )
                logit_range = float(
                    (eligible_logits.max() - eligible_logits.min()).item()
                )
                weight_range = float(
                    (eligible_weights.max() - eligible_weights.min()).item()
                )
            else:
                risk_range = 0.0
                logit_range = 0.0
                weight_range = 0.0

            transition_checked = (
                eligible_count >= 2
                and risk_range > float(risk_tolerance)
            )

            if transition_checked:
                if logit_range <= float(equality_tolerance):
                    raise AssertionError(
                        "Unequal eligible risks produced equal persisted "
                        f"dual logits in family {family_index}."
                    )

                if weight_range <= float(equality_tolerance):
                    raise AssertionError(
                        "Unequal eligible risks produced equal persisted "
                        f"softmax weights in family {family_index}."
                    )

            family_entropy = -torch.sum(
                family_weights
                * torch.log(family_weights.clamp_min(1e-12))
            )

            transition_diagnostics.append(
                {
                    "family_index": int(family_index),
                    "eligible_count": int(eligible_count),
                    "eligible_risk_range": float(risk_range),
                    "eligible_logit_range": float(logit_range),
                    "eligible_weight_range": float(weight_range),
                    "transition_checked": bool(transition_checked),
                    "family_weight_entropy": float(
                        family_entropy.item()
                    ),
                    "maximum_family_weight": float(
                        family_weights.max().item()
                    ),
                }
            )

        return transition_diagnostics

    @torch.no_grad()
    def diagnostics(self):
        family_weights = torch.softmax(
            self.family_dual_logits,
            dim=1,
        )
        family_entropies = -torch.sum(
            family_weights
            * torch.log(family_weights.clamp_min(1e-12)),
            dim=1,
        )

        cell_names = ["overall"]
        cell_names.extend(
            f"subgroup/{identity_name}"
            for identity_name in SCORED_IDENTITY_COLUMNS
        )
        cell_names.extend(
            f"bpsn/{identity_name}"
            for identity_name in SCORED_IDENTITY_COLUMNS
        )
        cell_names.extend(
            f"bnsp/{identity_name}"
            for identity_name in SCORED_IDENTITY_COLUMNS
        )

        support = self.risk_support_counts.detach().cpu().tolist()
        risks = self.running_surrogate_risks.detach().cpu().tolist()
        variances = self.running_risk_variances.detach().cpu().tolist()

        return {
            "cell_names": cell_names,
            "cell_update_counts": (
                self.cell_update_counts.detach().cpu().tolist()
            ),
            "risk_support_counts": support,
            "positive_score_counts": (
                self.positive_score_counts.detach().cpu().tolist()
            ),
            "negative_score_counts": (
                self.negative_score_counts.detach().cpu().tolist()
            ),
            "running_surrogate_risks": [
                float(risk) if cell_support > 0 else None
                for risk, cell_support in zip(risks, support)
            ],
            "running_risk_variances": [
                float(variance) if cell_support > 0 else None
                for variance, cell_support in zip(variances, support)
            ],
            "family_weights": family_weights.detach().cpu().tolist(),
            "family_weight_entropy": (
                family_entropies.detach().cpu().tolist()
            ),
            "maximum_family_weight": (
                family_weights.max(dim=1).values.detach().cpu().tolist()
            ),
        }

    def forward(self, logits, soft_targets, metric_cell_codes):
        scores = logits.reshape(-1).float()

        soft_targets = soft_targets.reshape(-1).to(
            device=scores.device,
            dtype=torch.float32,
        )

        metric_cell_codes = metric_cell_codes.to(
            device=scores.device,
            dtype=torch.long,
        )

        if scores.shape[0] != soft_targets.shape[0]:
            raise ValueError("Logits and targets must contain the same rows.")

        if metric_cell_codes.ndim != 2:
            raise ValueError("metric_cell_codes must have shape [batch, identities].")

        if metric_cell_codes.shape[0] != scores.shape[0]:
            raise ValueError("Metric-cell codes and logits must contain the same rows.")

        if metric_cell_codes.shape[1] != self.identity_count:
            raise ValueError("Metric-cell identity dimension is inconsistent.")

        pointwise_loss = F.binary_cross_entropy_with_logits(
            scores,
            soft_targets.clamp(0.0, 1.0),
        )

        binary_targets = soft_targets >= 0.5

        overall_pair_loss = self._cell_pair_loss(
            scores,
            positive_mask=binary_targets,
            negative_mask=~binary_targets,
            cell_index=0,
        )

        subgroup_losses = []
        bpsn_losses = []
        bnsp_losses = []

        for identity_index in range(self.identity_count):
            identity_cells = metric_cell_codes[:, identity_index]

            subgroup_losses.append(
                self._cell_pair_loss(
                    scores,
                    positive_mask=identity_cells == 1,
                    negative_mask=identity_cells == 2,
                    cell_index=1 + identity_index,
                )
            )
            bpsn_losses.append(
                self._cell_pair_loss(
                    scores,
                    positive_mask=identity_cells == 3,
                    negative_mask=identity_cells == 2,
                    cell_index=1 + self.identity_count + identity_index,
                )
            )
            bnsp_losses.append(
                self._cell_pair_loss(
                    scores,
                    positive_mask=identity_cells == 1,
                    negative_mask=identity_cells == 4,
                    cell_index=1 + 2 * self.identity_count + identity_index,
                )
            )

        subgroup_robust_loss = self._family_aggregate(
            subgroup_losses,
            family_index=0,
        )
        bpsn_robust_loss = self._family_aggregate(
            bpsn_losses,
            family_index=1,
        )
        bnsp_robust_loss = self._family_aggregate(
            bnsp_losses,
            family_index=2,
        )

        zero_ranking_loss = scores.sum() * 0.0
        pairwise_loss = 0.25 * (
            (
                overall_pair_loss
                if overall_pair_loss is not None
                else zero_ranking_loss
            )
            + (
                subgroup_robust_loss
                if subgroup_robust_loss is not None
                else zero_ranking_loss
            )
            + (
                bpsn_robust_loss
                if bpsn_robust_loss is not None
                else zero_ranking_loss
            )
            + (
                bnsp_robust_loss
                if bnsp_robust_loss is not None
                else zero_ranking_loss
            )
        )

        total_loss = (
            self.pointwise_weight * pointwise_loss
            + self.pairwise_weight * pairwise_loss
        )

        family_weights = torch.softmax(
            self.family_dual_logits,
            dim=1,
        )

        self.last_components = {
            "total": float(total_loss.detach().cpu()),
            "pointwise": float(pointwise_loss.detach().cpu()),
            "pairwise": float(pairwise_loss.detach().cpu()),
            "overall_pair_available": int(overall_pair_loss is not None),
            "subgroup_identities_available": sum(
                cell_loss is not None for cell_loss in subgroup_losses
            ),
            "bpsn_identities_available": sum(
                cell_loss is not None for cell_loss in bpsn_losses
            ),
            "bnsp_identities_available": sum(
                cell_loss is not None for cell_loss in bnsp_losses
            ),
            "maximum_family_weight": (
                family_weights.max(dim=1).values.detach().cpu().tolist()
            ),
        }

        return total_loss


criterion = GroupRobustPairwiseAUCLoss(
    pointwise_weight=POINTWISE_LOSS_WEIGHT,
    pairwise_weight=PAIRWISE_LOSS_WEIGHT,
    pair_temperature=1.0,
    robust_temperature=0.25,
    max_examples_per_pool=24,
    score_ema_rate=0.05,
    risk_ema_rate=0.05,
    dual_learning_rate=0.025,
    minimum_dual_support=8,
    maximum_dual_logit=1.5,
).to(device)


@torch.no_grad()
def run_synthetic_dual_transition_test():
    synthetic_criterion = GroupRobustPairwiseAUCLoss(
        pointwise_weight=POINTWISE_LOSS_WEIGHT,
        pairwise_weight=PAIRWISE_LOSS_WEIGHT,
        pair_temperature=1.0,
        robust_temperature=0.25,
        max_examples_per_pool=24,
        score_ema_rate=0.05,
        risk_ema_rate=0.05,
        dual_learning_rate=0.025,
        minimum_dual_support=8,
        maximum_dual_logit=1.5,
    )

    cell_start = 1
    cell_stop = cell_start + synthetic_criterion.identity_count
    synthetic_risks = torch.linspace(
        0.1,
        0.9,
        steps=synthetic_criterion.identity_count,
        dtype=torch.float32,
    )

    synthetic_criterion.pending_positive_score_counts[
        cell_start:cell_stop
    ].fill_(8)
    synthetic_criterion.pending_negative_score_counts[
        cell_start:cell_stop
    ].fill_(8)
    synthetic_criterion.pending_positive_score_sums[
        cell_start:cell_stop
    ].fill_(4.0)
    synthetic_criterion.pending_negative_score_sums[
        cell_start:cell_stop
    ].fill_(-4.0)
    synthetic_criterion.pending_risk_counts[
        cell_start:cell_stop
    ].fill_(8)
    synthetic_criterion.pending_risk_sums[
        cell_start:cell_stop
    ].copy_(synthetic_risks * 8.0)

    logits_before = synthetic_criterion.family_dual_logits[0].clone()
    synthetic_criterion.commit_state()
    logits_after = synthetic_criterion.family_dual_logits[0].clone()
    state_dict_logits = synthetic_criterion.state_dict()[
        "family_dual_logits"
    ][0]
    family_weights = torch.softmax(logits_after, dim=0)
    uniform_weights = torch.full_like(
        family_weights,
        1.0 / synthetic_criterion.identity_count,
    )
    entropy = -torch.sum(
        family_weights
        * torch.log(family_weights.clamp_min(1e-12))
    )

    if torch.equal(logits_before, logits_after):
        raise AssertionError(
            "Synthetic commit_state test did not change dual logits."
        )

    if not torch.equal(logits_after, state_dict_logits):
        raise AssertionError(
            "Synthetic dual-logit update did not persist in state_dict."
        )

    if torch.allclose(
        family_weights,
        uniform_weights,
        atol=1e-8,
        rtol=0.0,
    ):
        raise AssertionError(
            "Synthetic unequal risks produced uniform family weights."
        )

    if not float(entropy.item()) < math.log(
        synthetic_criterion.identity_count
    ):
        raise AssertionError(
            "Synthetic family-weight entropy did not fall below log(9)."
        )

    if not float(family_weights.max().item()) > (
        1.0 / synthetic_criterion.identity_count
    ):
        raise AssertionError(
            "Synthetic maximum family weight did not exceed 1/9."
        )

    transition_diagnostics = (
        synthetic_criterion.assert_nonuniform_dual_transition()
    )

    print(
        json.dumps(
            {
                "synthetic_dual_transition_test": {
                    "family_dual_logits": logits_after.tolist(),
                    "family_weights": family_weights.tolist(),
                    "family_weight_entropy": float(entropy.item()),
                    "maximum_family_weight": float(
                        family_weights.max().item()
                    ),
                    "transition_diagnostics": transition_diagnostics,
                }
            },
            sort_keys=True,
        )
    )


run_synthetic_dual_transition_test()


# =============================================================================
# Differential-learning-rate optimizer
# =============================================================================

head_prefixes = ("head.", "classifier.")

optimizer_parameter_groups = {
    ("backbone", "decay"): [],
    ("backbone", "no_decay"): [],
    ("head", "decay"): [],
    ("head", "no_decay"): [],
}

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    component = "head" if parameter_name.startswith(head_prefixes) else "backbone"

    decay_type = (
        "no_decay"
        if parameter.ndim == 1 or parameter_name.endswith(".bias")
        else "decay"
    )

    optimizer_parameter_groups[(component, decay_type)].append(parameter)

optimizer_groups = []

for (component, decay_type), parameters in optimizer_parameter_groups.items():
    if not parameters:
        continue

    optimizer_groups.append(
        {
            "params": parameters,
            "lr": (
                HEAD_LEARNING_RATE if component == "head" else BACKBONE_LEARNING_RATE
            ),
            "weight_decay": (0.0 if decay_type == "no_decay" else WEIGHT_DECAY),
        }
    )

optimizer = AdamW(
    optimizer_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

model_design_config = {
    "model_id": model_id,
    "max_length": MAX_LENGTH,
    "num_outputs": 1,
    "output_semantics": "toxicity_logit",
    "inference_postprocessing": "sigmoid",
    "classifier_dropout": classifier_dropout,
    "gradient_checkpointing": True,
    "mixed_precision_required": True,
    "pointwise_loss_weight": POINTWISE_LOSS_WEIGHT,
    "pairwise_loss_weight": PAIRWISE_LOSS_WEIGHT,
    "pair_temperature": criterion.pair_temperature,
    "robust_temperature": criterion.robust_temperature,
    "max_examples_per_pair_pool": criterion.max_examples_per_pool,
    "persistent_auc_cell_count": criterion.cell_count,
    "score_ema_rate": criterion.score_ema_rate,
    "risk_ema_rate": criterion.risk_ema_rate,
    "dual_learning_rate": criterion.dual_learning_rate,
    "minimum_dual_support": criterion.minimum_dual_support,
    "maximum_dual_logit": criterion.maximum_dual_logit,
    "family_top_level_weight": 0.25,
    "loss_state_commit_boundary": "successful_optimizer_step",
    "backbone_learning_rate": BACKBONE_LEARNING_RATE,
    "head_learning_rate": HEAD_LEARNING_RATE,
    "weight_decay": WEIGHT_DECAY,
}


# =============================================================================
# Metric-cell-balanced batching
# =============================================================================


class MetricCellBatchSampler(Sampler):
    """
    Every mini-batch contains one example from each evaluator-defined cell for
    one uniformly rotated scored identity, plus examples from a shuffled global
    traversal of the training partition.

    This guarantees availability of Subgroup, BPSN, BNSP, and overall ranking
    pairs in each normal training batch while still traversing all train rows
    if the runtime permits a full epoch.
    """

    def __init__(self, metric_cells, batch_size, seed):
        self.metric_cells = np.asarray(metric_cells, dtype=np.uint8)

        if self.metric_cells.ndim != 2:
            raise ValueError("metric_cells must have shape [rows, identities].")

        self.row_count, self.identity_count = self.metric_cells.shape
        self.batch_size = int(batch_size)
        self.base_rows_per_batch = self.batch_size - 4
        self.seed = int(seed)
        self.epoch = 0

        if self.row_count == 0:
            raise ValueError("The training partition is empty.")

        if self.identity_count != len(SCORED_IDENTITY_COLUMNS):
            raise ValueError("Metric-cell identity dimension is inconsistent.")

        if self.base_rows_per_batch < 1:
            raise ValueError("Batch size must leave room for at least one global row.")

        self.cell_pools = []
        missing_pools = []

        for identity_index, identity_name in enumerate(SCORED_IDENTITY_COLUMNS):
            identity_pools = {}

            for cell_code in (1, 2, 3, 4):
                pool = np.flatnonzero(
                    self.metric_cells[:, identity_index] == cell_code
                ).astype(np.int32, copy=False)

                identity_pools[cell_code] = pool

                if pool.size == 0:
                    missing_pools.append((identity_name, cell_code))

            self.cell_pools.append(identity_pools)

        if missing_pools:
            missing_description = ", ".join(
                f"{identity}:cell_{cell_code}" for identity, cell_code in missing_pools
            )
            raise ValueError(
                f"Required metric-cell pools are empty: {missing_description}"
            )

        self.batch_count = math.ceil(self.row_count / self.base_rows_per_batch)

    def set_epoch(self, epoch):
        self.epoch = int(epoch)

    def __len__(self):
        return self.batch_count

    def __iter__(self):
        rng = np.random.default_rng(self.seed + 1_000_003 * self.epoch)

        global_order = rng.permutation(self.row_count)
        identity_order = rng.permutation(self.identity_count)

        for batch_index in range(self.batch_count):
            if batch_index % self.identity_count == 0:
                identity_order = rng.permutation(self.identity_count)

            identity_index = int(identity_order[batch_index % self.identity_count])

            base_start = batch_index * self.base_rows_per_batch
            base_stop = min(
                base_start + self.base_rows_per_batch,
                self.row_count,
            )

            batch_indices = global_order[base_start:base_stop].tolist()

            for cell_code in (1, 2, 3, 4):
                pool = self.cell_pools[identity_index][cell_code]
                sampled_position = int(rng.integers(0, pool.size))
                batch_indices.append(int(pool[sampled_position]))

            rng.shuffle(batch_indices)
            yield batch_indices


class ToxicityTrainingDataset(Dataset):
    def __init__(self, texts, targets, metric_cells):
        self.texts = texts
        self.targets = np.asarray(targets, dtype=np.float32)
        self.metric_cells = np.asarray(metric_cells, dtype=np.uint8)

        if not (len(self.texts) == len(self.targets) == len(self.metric_cells)):
            raise ValueError("Training arrays do not have matching row counts.")

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            str(self.texts[index]),
            self.targets[index],
            self.metric_cells[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts, positional_indices):
        self.texts = texts
        self.positional_indices = np.asarray(
            positional_indices,
            dtype=np.int64,
        ).reshape(-1)

        if self.positional_indices.size:
            if self.positional_indices.min() < 0:
                raise IndexError("Inference indices must be non-negative.")

            if self.positional_indices.max() >= len(self.texts):
                raise IndexError("Inference index exceeds partition size.")

    def __len__(self):
        return self.positional_indices.size

    def __getitem__(self, index):
        partition_position = int(self.positional_indices[index])
        return str(self.texts[partition_position])


class TrainingCollator:
    def __init__(self, tokenizer_object, max_length):
        self.tokenizer = tokenizer_object
        self.max_length = int(max_length)

    def __call__(self, samples):
        texts, targets, metric_cells = zip(*samples)

        encoded = self.tokenizer(
            list(texts),
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

        # ModernBERT does not use token type IDs.
        encoded.pop("token_type_ids", None)

        encoded["soft_targets"] = torch.as_tensor(np.asarray(targets, dtype=np.float32))

        encoded["metric_cell_codes"] = torch.as_tensor(
            np.stack(metric_cells).astype(np.int64, copy=False)
        )

        return encoded


class InferenceCollator:
    def __init__(self, tokenizer_object, max_length):
        self.tokenizer = tokenizer_object
        self.max_length = int(max_length)

    def __call__(self, texts):
        encoded = self.tokenizer(
            list(texts),
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

        encoded.pop("token_type_ids", None)
        return encoded


def seed_data_loader_worker(worker_id):
    worker_seed = (torch.initial_seed() + worker_id) % (2**32)
    np.random.seed(worker_seed)
    random.seed(worker_seed)


train_dataset = ToxicityTrainingDataset(
    train_texts,
    train_soft_targets,
    train_metric_cell_codes,
)

train_batch_sampler = MetricCellBatchSampler(
    train_metric_cell_codes,
    batch_size=TRAIN_MICRO_BATCH_SIZE,
    seed=MODEL_SEED,
)

training_collator = TrainingCollator(
    tokenizer,
    MAX_LENGTH,
)

loader_generator = torch.Generator()
loader_generator.manual_seed(MODEL_SEED)

training_loader = DataLoader(
    train_dataset,
    batch_sampler=train_batch_sampler,
    collate_fn=training_collator,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    prefetch_factor=2,
    worker_init_fn=seed_data_loader_worker,
    generator=loader_generator,
)


# =============================================================================
# Learning-rate schedule and mixed precision
# =============================================================================


def learning_rate_multiplier(optimizer_step):
    optimizer_step = int(optimizer_step)

    if optimizer_step < WARMUP_OPTIMIZER_STEPS:
        return max(
            optimizer_step / max(1, WARMUP_OPTIMIZER_STEPS),
            1.0 / max(1, WARMUP_OPTIMIZER_STEPS),
        )

    decay_progress = (optimizer_step - WARMUP_OPTIMIZER_STEPS) / max(
        1,
        MAX_OPTIMIZER_STEPS_FOR_SCHEDULE - WARMUP_OPTIMIZER_STEPS,
    )

    decay_progress = min(max(decay_progress, 0.0), 1.0)

    return 0.05 + 0.95 * 0.5 * (1.0 + math.cos(math.pi * decay_progress))


scheduler = LambdaLR(
    optimizer,
    lr_lambda=learning_rate_multiplier,
)

mixed_precision_enabled = device.type == "cuda"
gradient_scaler = GradScaler(enabled=mixed_precision_enabled)
optimizer_steps_completed = 0


# =============================================================================
# Identical validation and test inference
# =============================================================================

inference_collator = InferenceCollator(tokenizer, MAX_LENGTH)


def predict_partition(text_partition, positional_indices):
    positional_indices = np.asarray(
        positional_indices,
        dtype=np.int64,
    ).reshape(-1)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float32)

    inference_dataset = ToxicityInferenceDataset(
        text_partition,
        positional_indices,
    )

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        collate_fn=inference_collator,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=False,
        prefetch_factor=2,
        worker_init_fn=seed_data_loader_worker,
    )

    previous_training_mode = model.training
    predictions = np.empty(
        len(inference_dataset),
        dtype=np.float32,
    )
    write_position = 0

    model.eval()

    try:
        with torch.inference_mode():
            for encoded_batch in inference_loader:
                encoded_batch = {
                    key: value.to(
                        device,
                        non_blocking=PIN_MEMORY,
                    )
                    for key, value in encoded_batch.items()
                }

                with autocast(
                    enabled=mixed_precision_enabled,
                    dtype=torch.float16,
                ):
                    logits = model(**encoded_batch).logits.reshape(-1)

                batch_predictions = (
                    torch.sigmoid(logits.float())
                    .cpu()
                    .numpy()
                    .astype(np.float32, copy=False)
                )

                next_position = write_position + batch_predictions.size

                predictions[write_position:next_position] = batch_predictions

                write_position = next_position
    finally:
        model.train(previous_training_mode)

    if write_position != predictions.size:
        raise RuntimeError("Inference did not produce one prediction per row.")

    if not np.all(np.isfinite(predictions)):
        raise FloatingPointError("Inference produced non-finite predictions.")

    return predictions


def predict_validation(positional_indices):
    return predict_partition(
        valid_texts,
        positional_indices,
    )


def predict_test(positional_indices):
    return predict_partition(
        test_texts,
        positional_indices,
    )


# =============================================================================
# Runtime checkpoint callbacks
# =============================================================================


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    temporary_model_path = checkpoint_directory / "model_state.pt.tmp"
    final_model_path = checkpoint_directory / "model_state.pt"

    torch.save(
        model.state_dict(),
        temporary_model_path,
    )
    os.replace(
        temporary_model_path,
        final_model_path,
    )

    temporary_criterion_path = checkpoint_directory / "criterion_state.pt.tmp"
    final_criterion_path = checkpoint_directory / "criterion_state.pt"

    torch.save(
        criterion.state_dict(),
        temporary_criterion_path,
    )
    os.replace(
        temporary_criterion_path,
        final_criterion_path,
    )

    config_directory = checkpoint_directory / "model_config"
    tokenizer_directory = checkpoint_directory / "tokenizer"

    model.config.save_pretrained(config_directory)
    tokenizer.save_pretrained(tokenizer_directory)

    joblib.dump(
        text_feature_scaler,
        checkpoint_directory / "text_feature_scaler.joblib",
    )

    processing_manifest_path = WORKING_DIR / "data_processing_manifest.json"

    if processing_manifest_path.exists():
        shutil.copy2(
            processing_manifest_path,
            checkpoint_directory / "data_processing_manifest.json",
        )

    checkpoint_state = {
        "model_id": model_id,
        "max_length": int(MAX_LENGTH),
        "prediction_semantics": ("sigmoid_of_single_toxicity_logit"),
        "validation_metric": (
            "0.25 * overall_auc + "
            "0.25 * generalized_mean_p_minus_5(subgroup_auc) + "
            "0.25 * generalized_mean_p_minus_5(bpsn_auc) + "
            "0.25 * generalized_mean_p_minus_5(bnsp_auc)"
        ),
        "target_threshold_for_metric": 0.5,
        "identity_threshold_for_metric": 0.5,
        "scored_identity_columns": list(SCORED_IDENTITY_COLUMNS),
        "optimizer_steps_completed": int(optimizer_steps_completed),
        "gradient_accumulation_steps": int(GRADIENT_ACCUMULATION_STEPS),
        "training_micro_batch_size": int(TRAIN_MICRO_BATCH_SIZE),
        "inference_batch_size": int(INFERENCE_BATCH_SIZE),
        "model_design_config": model_design_config,
        "criterion_state_file": "criterion_state.pt",
        "criterion_diagnostics": criterion.diagnostics(),
        "criterion_dual_transition_diagnostics": (
            criterion.assert_nonuniform_dual_transition()
        ),
    }

    with open(
        checkpoint_directory / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as checkpoint_file:
        json.dump(
            checkpoint_state,
            checkpoint_file,
            indent=2,
            sort_keys=True,
        )


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)
    model_path = checkpoint_directory / "model_state.pt"
    criterion_path = checkpoint_directory / "criterion_state.pt"
    state_path = checkpoint_directory / "inference_state.json"

    if (
        not model_path.exists()
        or not criterion_path.exists()
        or not state_path.exists()
    ):
        raise FileNotFoundError(f"Incomplete checkpoint in {checkpoint_directory}.")

    with open(
        state_path,
        "r",
        encoding="utf-8",
    ) as checkpoint_file:
        checkpoint_state = json.load(checkpoint_file)

    if checkpoint_state["model_id"] != model_id:
        raise ValueError("Checkpoint model identifier does not match.")

    if checkpoint_state["prediction_semantics"] != ("sigmoid_of_single_toxicity_logit"):
        raise ValueError("Checkpoint prediction semantics do not match.")

    tokenizer.model_max_length = int(checkpoint_state["max_length"])

    saved_state_dict = torch.load(
        model_path,
        map_location=device,
    )

    model.load_state_dict(
        saved_state_dict,
        strict=True,
    )
    model.to(device)

    saved_criterion_state = torch.load(
        criterion_path,
        map_location=device,
    )

    criterion.load_state_dict(
        saved_criterion_state,
        strict=True,
    )
    criterion.to(device)
    criterion.discard_pending_state()

    saved_dual_logits = saved_criterion_state[
        "family_dual_logits"
    ].to(device=device)
    loaded_dual_logits = criterion.family_dual_logits.detach()

    if not torch.equal(saved_dual_logits, loaded_dual_logits):
        raise AssertionError(
            "Criterion dual logits changed during checkpoint load."
        )

    saved_nonuniform = bool(
        (
            saved_dual_logits.max(dim=1).values
            - saved_dual_logits.min(dim=1).values
            > 1e-9
        ).any().item()
    )
    loaded_nonuniform = bool(
        (
            loaded_dual_logits.max(dim=1).values
            - loaded_dual_logits.min(dim=1).values
            > 1e-9
        ).any().item()
    )

    if saved_nonuniform and not loaded_nonuniform:
        raise AssertionError(
            "Nonuniform criterion dual logits did not survive save/load."
        )

    loaded_diagnostics = criterion.diagnostics()
    saved_diagnostics = checkpoint_state.get("criterion_diagnostics")

    if not isinstance(saved_diagnostics, dict):
        raise ValueError(
            "Checkpoint is missing criterion diagnostics."
        )

    for diagnostic_key in (
        "family_weights",
        "family_weight_entropy",
        "maximum_family_weight",
    ):
        saved_values = np.asarray(
            saved_diagnostics[diagnostic_key],
            dtype=np.float64,
        )
        loaded_values = np.asarray(
            loaded_diagnostics[diagnostic_key],
            dtype=np.float64,
        )

        if not np.allclose(
            saved_values,
            loaded_values,
            atol=1e-8,
            rtol=1e-7,
        ):
            raise AssertionError(
                "Criterion diagnostic did not survive save/load: "
                f"{diagnostic_key}."
            )

    loaded_transition_diagnostics = (
        criterion.assert_nonuniform_dual_transition()
    )
    saved_transition_diagnostics = checkpoint_state.get(
        "criterion_dual_transition_diagnostics"
    )

    if saved_transition_diagnostics is not None:
        if len(saved_transition_diagnostics) != len(
            loaded_transition_diagnostics
        ):
            raise AssertionError(
                "Dual-transition diagnostic family count changed "
                "during save/load."
            )

        for saved_family, loaded_family in zip(
            saved_transition_diagnostics,
            loaded_transition_diagnostics,
        ):
            for diagnostic_key in (
                "family_index",
                "eligible_count",
                "transition_checked",
            ):
                if saved_family[diagnostic_key] != loaded_family[
                    diagnostic_key
                ]:
                    raise AssertionError(
                        "Dual-transition diagnostic changed during "
                        f"save/load: {diagnostic_key}."
                    )

            for diagnostic_key in (
                "eligible_risk_range",
                "eligible_logit_range",
                "eligible_weight_range",
                "family_weight_entropy",
                "maximum_family_weight",
            ):
                if not math.isclose(
                    float(saved_family[diagnostic_key]),
                    float(loaded_family[diagnostic_key]),
                    rel_tol=1e-7,
                    abs_tol=1e-8,
                ):
                    raise AssertionError(
                        "Dual-transition diagnostic changed during "
                        f"save/load: {diagnostic_key}."
                    )

    del saved_state_dict
    del saved_criterion_state
    gc.collect()

    if device.type == "cuda":
        torch.cuda.empty_cache()


# =============================================================================
# Candidate runtime binding and training
# =============================================================================

session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_ids_for_session)

model.train()
optimizer.zero_grad(set_to_none=True)

stop_requested = False

for epoch_index in range(MAX_EPOCHS):
    train_batch_sampler.set_epoch(epoch_index)

    for micro_batch_index, batch in enumerate(training_loader):
        soft_targets_batch = batch.pop("soft_targets").to(
            device,
            non_blocking=PIN_MEMORY,
        )

        metric_cells_batch = batch.pop("metric_cell_codes").to(
            device,
            non_blocking=PIN_MEMORY,
        )

        model_inputs = {
            key: value.to(
                device,
                non_blocking=PIN_MEMORY,
            )
            for key, value in batch.items()
        }

        with autocast(
            enabled=mixed_precision_enabled,
            dtype=torch.float16,
        ):
            logits = model(**model_inputs).logits

            loss = criterion(
                logits,
                soft_targets_batch,
                metric_cells_batch,
            )

            scaled_accumulation_loss = loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(loss.detach()):
            raise FloatingPointError("Training loss became non-finite.")

        gradient_scaler.scale(scaled_accumulation_loss).backward()

        accumulation_boundary = (
            micro_batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0

        final_batch_of_epoch = micro_batch_index + 1 == len(training_loader)

        if not accumulation_boundary and not final_batch_of_epoch:
            continue

        gradient_scaler.unscale_(optimizer)

        clip_grad_norm_(
            model.parameters(),
            max_norm=MAX_GRADIENT_NORM,
        )

        if mixed_precision_enabled:
            scale_before_update = gradient_scaler.get_scale()

            gradient_scaler.step(optimizer)
            gradient_scaler.update()

            scale_after_update = gradient_scaler.get_scale()

            optimizer_step_executed = scale_after_update >= scale_before_update
        else:
            optimizer.step()
            gradient_scaler.update()
            optimizer_step_executed = True

        optimizer.zero_grad(set_to_none=True)

        if not optimizer_step_executed:
            criterion.discard_pending_state()
            continue

        criterion.commit_state()
        dual_transition_diagnostics = (
            criterion.assert_nonuniform_dual_transition()
        )
        scheduler.step()
        optimizer_steps_completed += 1

        if (
            optimizer_steps_completed == 1
            or optimizer_steps_completed % LOSS_STATE_LOG_INTERVAL_STEPS == 0
        ):
            print(
                json.dumps(
                    {
                        "optimizer_step": int(optimizer_steps_completed),
                        "criterion_state": criterion.diagnostics(),
                        "dual_transition_diagnostics": (
                            dual_transition_diagnostics
                        ),
                    },
                    sort_keys=True,
                )
            )

        stop_requested = session.step()

        if stop_requested:
            break

    if stop_requested:
        break


# =============================================================================
# Runtime-owned official validation, best-checkpoint reload, and submission
# =============================================================================


def compute_exact_validation_metrics(predictions):
    predictions = np.asarray(
        predictions,
        dtype=np.float64,
    ).reshape(-1)

    if predictions.shape[0] != valid_binary_targets.shape[0]:
        raise ValueError(
            "Validation predictions and targets have different row counts."
        )

    if not np.all(np.isfinite(predictions)):
        raise FloatingPointError(
            "Validation predictions contain non-finite values."
        )

    def checked_auc(labels, scores, metric_name):
        labels = np.asarray(labels, dtype=np.uint8)
        scores = np.asarray(scores, dtype=np.float64)

        if np.unique(labels).size != 2:
            raise ValueError(
                f"Validation metric cell lacks both classes: {metric_name}."
            )

        return float(roc_auc_score(labels, scores))

    overall_auc = checked_auc(
        valid_binary_targets,
        predictions,
        "overall",
    )

    bias_aucs = {
        "subgroup": {},
        "bpsn": {},
        "bnsp": {},
    }

    for identity_index, identity_name in enumerate(
        SCORED_IDENTITY_COLUMNS
    ):
        identity_cells = valid_metric_cell_codes[:, identity_index]

        subgroup_mask = (
            (identity_cells == 1)
            | (identity_cells == 2)
        )
        bpsn_mask = (
            (identity_cells == 2)
            | (identity_cells == 3)
        )
        bnsp_mask = (
            (identity_cells == 1)
            | (identity_cells == 4)
        )

        bias_aucs["subgroup"][identity_name] = checked_auc(
            valid_binary_targets[subgroup_mask],
            predictions[subgroup_mask],
            f"subgroup/{identity_name}",
        )
        bias_aucs["bpsn"][identity_name] = checked_auc(
            valid_binary_targets[bpsn_mask],
            predictions[bpsn_mask],
            f"bpsn/{identity_name}",
        )
        bias_aucs["bnsp"][identity_name] = checked_auc(
            valid_binary_targets[bnsp_mask],
            predictions[bnsp_mask],
            f"bnsp/{identity_name}",
        )

    def power_mean_minus_five(values):
        values = np.asarray(
            list(values),
            dtype=np.float64,
        )

        if np.any(values <= 0.0):
            raise ValueError(
                "Power-mean AUC components must be positive."
            )

        return float(
            np.power(
                np.mean(np.power(values, -5.0)),
                -1.0 / 5.0,
            )
        )

    family_power_means = {
        family_name: power_mean_minus_five(
            family_metrics.values()
        )
        for family_name, family_metrics in bias_aucs.items()
    }

    exact_score = 0.25 * (
        overall_auc
        + family_power_means["subgroup"]
        + family_power_means["bpsn"]
        + family_power_means["bnsp"]
    )

    return {
        "exact_official_score": float(exact_score),
        "overall_auc": float(overall_auc),
        "power_means": family_power_means,
        "bias_aucs": bias_aucs,
    }


del training_loader
gc.collect()

if device.type == "cuda":
    torch.cuda.empty_cache()

result = session.finish()