import os
os.sched_setaffinity(0, {8, 9})
import gc
import html
import json
import math
import os
import random
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer


# ============================================================
# Configuration
# ============================================================
os.environ["TOKENIZERS_PARALLELISM"] = "false"

RANDOM_SEED = 2029
VALIDATION_TIME_QUANTILE = 0.85

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

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

IDENTITY_COLUMNS = [
    "male",
    "female",
    "transgender",
    "other_gender",
    "heterosexual",
    "homosexual_gay_or_lesbian",
    "bisexual",
    "other_sexual_orientation",
    "christian",
    "jewish",
    "muslim",
    "hindu",
    "buddhist",
    "atheist",
    "other_religion",
    "black",
    "white",
    "asian",
    "latino",
    "other_race_or_ethnicity",
    "physical_disability",
    "intellectual_or_learning_disability",
    "psychiatric_or_mental_illness",
    "other_disability",
]

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

STYLE_RAW_COLUMNS = [
    "style_log_char_count",
    "style_log_word_count",
    "style_caps_ratio",
    "style_punctuation_ratio",
    "style_log_exclamation_count",
    "style_log_question_count",
    "style_log_digit_count",
    "style_elongation_ratio",
]

MODEL_MAX_LENGTH = int(os.getenv("MODEL_MAX_LENGTH", "384"))
MAX_EPOCHS = int(os.getenv("MAX_EPOCHS", "1"))
EARLY_STOPPING_PATIENCE = int(os.getenv("EARLY_STOPPING_PATIENCE", "2"))
GRADIENT_ACCUMULATION_STEPS = int(os.getenv("GRADIENT_ACCUMULATION_STEPS", "8"))
TRAIN_BATCH_SIZE = int(os.getenv("TRAIN_BATCH_SIZE", "4"))
EVAL_BATCH_SIZE = int(os.getenv("EVAL_BATCH_SIZE", "16"))
COUNTERFACTUAL_BATCH_FREQUENCY = int(os.getenv("COUNTERFACTUAL_BATCH_FREQUENCY", "4"))
WARMUP_RATIO = float(os.getenv("WARMUP_RATIO", "0.06"))

BACKBONE_LEARNING_RATE = float(os.getenv("BACKBONE_LEARNING_RATE", "1.2e-5"))
HEAD_LEARNING_RATE = float(os.getenv("HEAD_LEARNING_RATE", "8e-5"))
WEIGHT_DECAY = float(os.getenv("WEIGHT_DECAY", "0.01"))

ADVERSARIAL_STRENGTH = float(os.getenv("ADVERSARIAL_STRENGTH", "0.10"))
AUXILIARY_LOSS_WEIGHT = float(os.getenv("AUXILIARY_LOSS_WEIGHT", "0.18"))
IDENTITY_ADVERSARIAL_LOSS_WEIGHT = float(
    os.getenv("IDENTITY_ADVERSARIAL_LOSS_WEIGHT", "0.08")
)
COUNTERFACTUAL_CONSISTENCY_WEIGHT = float(
    os.getenv("COUNTERFACTUAL_CONSISTENCY_WEIGHT", "0.06")
)

BEST_CHECKPOINT_PATH = WORKING_DIR / "best_bias_aware_deberta.pt"
BEST_METRICS_PATH = WORKING_DIR / "best_validation_metrics.json"
BEST_VALID_PREDICTIONS_PATH = WORKING_DIR / "best_validation_predictions.npy"


# ============================================================
# Reproducibility
# ============================================================
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True


# ============================================================
# Text preprocessing
# ============================================================
URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
USER_PATTERN = re.compile(r"(?<!\w)@[A-Za-z0-9_]+")
HTML_TAG_PATTERN = re.compile(r"<[^>\n]{1,200}>")
CONTROL_PATTERN = re.compile(r"[\u0000-\u0008\u000b-\u001f\u007f-\u009f]")
ZERO_WIDTH_PATTERN = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
WHITESPACE_PATTERN = re.compile(r"\s+")
ELONGATION_PATTERN = re.compile(r"(.)\1{3,}", flags=re.DOTALL)

COUNTERFACTUAL_MAP = {
    "women": "men",
    "men": "women",
    "woman": "man",
    "man": "woman",
    "female": "male",
    "male": "female",
    "black": "white",
    "white": "black",
    "christian": "muslim",
    "muslim": "christian",
    "gay": "straight",
    "straight": "gay",
    "homosexual": "heterosexual",
    "heterosexual": "homosexual",
}

COUNTERFACTUAL_PATTERN = re.compile(
    r"\b("
    + "|".join(sorted(map(re.escape, COUNTERFACTUAL_MAP), key=len, reverse=True))
    + r")\b",
    flags=re.IGNORECASE,
)


def normalize_comment_text(value):
    if pd.isna(value):
        return "[EMPTY]"

    text = str(value)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = ZERO_WIDTH_PATTERN.sub("", text)
    text = CONTROL_PATTERN.sub(" ", text)
    text = HTML_TAG_PATTERN.sub(" ", text)
    text = URL_PATTERN.sub(" [URL] ", text)
    text = EMAIL_PATTERN.sub(" [EMAIL] ", text)
    text = USER_PATTERN.sub(" [USER] ", text)
    text = ELONGATION_PATTERN.sub(r"\1\1\1", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text if text else "[EMPTY]"


def canonical_text_key(value):
    normalized = normalize_comment_text(value).casefold()
    return WHITESPACE_PATTERN.sub(" ", normalized).strip()


def preserve_case(source_word, replacement_word):
    if source_word.isupper():
        return replacement_word.upper()
    if source_word[:1].isupper():
        return replacement_word.capitalize()
    return replacement_word


def create_counterfactual_text(text):
    def replacement(match):
        source_word = match.group(0)
        replacement_word = COUNTERFACTUAL_MAP[source_word.casefold()]
        return preserve_case(source_word, replacement_word)

    return COUNTERFACTUAL_PATTERN.sub(replacement, text)


def make_style_features(text_series):
    text_series = text_series.fillna("[EMPTY]").astype(str)

    char_count = text_series.str.len().clip(lower=1).astype(np.float32)
    word_count = text_series.str.count(r"\S+").astype(np.float32)
    letter_count = text_series.str.count(r"[A-Za-z]").astype(np.float32)
    upper_count = text_series.str.count(r"[A-Z]").astype(np.float32)
    punctuation_count = text_series.str.count(r"[!?.,;:]").astype(np.float32)
    exclamation_count = text_series.str.count(r"!").astype(np.float32)
    question_count = text_series.str.count(r"\?").astype(np.float32)
    digit_count = text_series.str.count(r"\d").astype(np.float32)
    elongation_count = text_series.str.count(r"(.)\1{2,}").astype(np.float32)

    return pd.DataFrame(
        {
            "style_log_char_count": np.log1p(char_count),
            "style_log_word_count": np.log1p(word_count),
            "style_caps_ratio": upper_count / np.maximum(letter_count, 1.0),
            "style_punctuation_ratio": punctuation_count / np.maximum(char_count, 1.0),
            "style_log_exclamation_count": np.log1p(exclamation_count),
            "style_log_question_count": np.log1p(question_count),
            "style_log_digit_count": np.log1p(digit_count),
            "style_elongation_ratio": elongation_count / np.maximum(word_count, 1.0),
        },
        index=text_series.index,
    ).astype(np.float32)


# ============================================================
# Load data
# ============================================================
train_header = pd.read_csv(TRAIN_PATH, nrows=0).columns.tolist()
test_header = pd.read_csv(TEST_PATH, nrows=0).columns.tolist()

available_identity_columns = [c for c in IDENTITY_COLUMNS if c in train_header]
available_official_identity_columns = [
    c for c in OFFICIAL_IDENTITY_COLUMNS if c in train_header
]
available_auxiliary_columns = [c for c in AUXILIARY_TARGET_COLUMNS if c in train_header]

required_train_columns = (
    [
        "id",
        "comment_text",
        "target",
        "created_date",
        "identity_annotator_count",
    ]
    + available_identity_columns
    + available_auxiliary_columns
)

required_train_columns = [c for c in required_train_columns if c in train_header]
required_test_columns = [c for c in ["id", "comment_text"] if c in test_header]

train_dtypes = {
    "id": "int64",
    "target": "float32",
    "identity_annotator_count": "int32",
}

for column in available_identity_columns + available_auxiliary_columns:
    train_dtypes[column] = "float32"

train_source = pd.read_csv(
    TRAIN_PATH,
    usecols=required_train_columns,
    dtype=train_dtypes,
    low_memory=False,
)

test_source = pd.read_csv(
    TEST_PATH,
    usecols=required_test_columns,
    dtype={"id": "int64"},
    low_memory=False,
)


# ============================================================
# Duplicate-safe temporal validation split
# ============================================================
raw_text_for_split = train_source["comment_text"].fillna("").astype(str)
text_keys = raw_text_for_split.map(canonical_text_key)

text_group_hash = pd.util.hash_pandas_object(
    text_keys,
    index=False,
).to_numpy(dtype=np.uint64)

timestamps = pd.to_datetime(
    train_source["created_date"],
    utc=True,
    errors="coerce",
)

valid_timestamps = timestamps.dropna()

if valid_timestamps.empty:
    validation_mask = (text_group_hash % 100) < 15
    split_cutoff = None
else:
    split_cutoff = valid_timestamps.quantile(VALIDATION_TIME_QUANTILE)
    latest_group_timestamp = timestamps.groupby(text_group_hash, sort=False).transform(
        "max"
    )
    validation_mask = latest_group_timestamp.ge(split_cutoff).to_numpy()
    validation_mask &= latest_group_timestamp.notna().to_numpy()

    if validation_mask.mean() < 0.08:
        split_cutoff = valid_timestamps.quantile(0.80)
        latest_group_timestamp = timestamps.groupby(
            text_group_hash, sort=False
        ).transform("max")
        validation_mask = latest_group_timestamp.ge(split_cutoff).to_numpy()
        validation_mask &= latest_group_timestamp.notna().to_numpy()

validation_mask = np.asarray(validation_mask, dtype=bool)

valid_source = train_source.loc[validation_mask].copy()
train_source = train_source.loc[~validation_mask].copy()

train_source.reset_index(drop=True, inplace=True)
valid_source.reset_index(drop=True, inplace=True)

del raw_text_for_split
del text_keys
del text_group_hash
del timestamps
del valid_timestamps
gc.collect()


# ============================================================
# Feature table construction
# ============================================================
def build_processed_frame(source_frame, include_labels):
    cleaned_text = source_frame["comment_text"].map(normalize_comment_text)
    counterfactual_text = cleaned_text.map(create_counterfactual_text)

    processed = pd.DataFrame(
        {
            "id": source_frame["id"].to_numpy(dtype=np.int64, copy=False),
            "model_text": cleaned_text.to_numpy(),
            "counterfactual_text": counterfactual_text.to_numpy(),
            "counterfactual_changed": (
                counterfactual_text.to_numpy() != cleaned_text.to_numpy()
            ).astype(np.int8),
        }
    )

    style_features = make_style_features(cleaned_text).reset_index(drop=True)
    processed = pd.concat([processed, style_features], axis=1)

    if include_labels:
        processed["target"] = source_frame["target"].astype(np.float32).to_numpy()
        processed["target_binary"] = (
            source_frame["target"].fillna(0.0).to_numpy() >= 0.5
        ).astype(np.int8)

        processed["identity_annotated"] = (
            source_frame["identity_annotator_count"].fillna(0).to_numpy() > 0
        ).astype(np.int8)

        for column in available_auxiliary_columns:
            processed[column] = source_frame[column].astype(np.float32).to_numpy()

        for column in available_identity_columns:
            processed[column] = source_frame[column].astype(np.float32).to_numpy()

        official_membership = np.zeros(len(source_frame), dtype=bool)

        for column in available_official_identity_columns:
            subgroup_membership = source_frame[column].fillna(0.0).to_numpy() >= 0.5
            processed[f"subgroup_{column}"] = subgroup_membership.astype(np.int8)
            official_membership |= subgroup_membership

        processed["any_official_identity"] = official_membership.astype(np.int8)

    return processed


train_df = build_processed_frame(train_source, include_labels=True)

style_feature_means = train_df[STYLE_RAW_COLUMNS].mean(axis=0)
style_feature_stds = (
    train_df[STYLE_RAW_COLUMNS].std(axis=0).replace(0.0, 1.0).fillna(1.0)
)

for column in STYLE_RAW_COLUMNS:
    train_df[f"{column}_z"] = (
        (train_df[column] - style_feature_means[column]) / style_feature_stds[column]
    ).astype(np.float32)

del train_source
gc.collect()

valid_df = build_processed_frame(valid_source, include_labels=True)

for column in STYLE_RAW_COLUMNS:
    valid_df[f"{column}_z"] = (
        (valid_df[column] - style_feature_means[column]) / style_feature_stds[column]
    ).astype(np.float32)

del valid_source
gc.collect()

test_df = build_processed_frame(test_source, include_labels=False)

for column in STYLE_RAW_COLUMNS:
    test_df[f"{column}_z"] = (
        (test_df[column] - style_feature_means[column]) / style_feature_stds[column]
    ).astype(np.float32)

del test_source
gc.collect()

split_metadata = {
    "split_strategy": (
        "Forward temporal holdout using latest normalized-text groups; identical "
        "normalized comments are assigned to one partition."
    ),
    "validation_time_quantile": VALIDATION_TIME_QUANTILE,
    "temporal_cutoff_utc": None if split_cutoff is None else str(split_cutoff),
    "n_train": int(len(train_df)),
    "n_valid": int(len(valid_df)),
    "n_test": int(len(test_df)),
    "official_identity_columns": available_official_identity_columns,
    "metric": (
        "0.25 * overall_auc + 0.25 * power_mean(subgroup_auc, -5) + "
        "0.25 * power_mean(bpsn_auc, -5) + 0.25 * power_mean(bnsp_auc, -5)"
    ),
}

with open(WORKING_DIR / "data_processing_metadata.json", "w", encoding="utf-8") as f:
    json.dump(split_metadata, f, indent=2)


# ============================================================
# Official competition metric
# ============================================================
def safe_roc_auc(binary_targets, predictions):
    binary_targets = np.asarray(binary_targets, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(binary_targets) == 0 or np.unique(binary_targets).size < 2:
        return np.nan

    return float(roc_auc_score(binary_targets, predictions))


def power_mean(values, power=-5):
    values = np.asarray(values, dtype=np.float64)
    values = values[np.isfinite(values)]

    if len(values) == 0:
        return np.nan

    return float(np.mean(np.power(values, power)) ** (1.0 / power))


def official_bias_aware_auc(targets, predictions, identity_matrix):
    targets = (np.asarray(targets, dtype=np.float64) >= 0.5).astype(np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)
    identity_matrix = np.asarray(identity_matrix, dtype=np.float64)

    if identity_matrix.ndim != 2:
        raise ValueError("identity_matrix must be two-dimensional.")

    if len(targets) != len(predictions) or len(targets) != identity_matrix.shape[0]:
        raise ValueError("Targets, predictions, and identity rows must align.")

    overall_auc = safe_roc_auc(targets, predictions)

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_index in range(identity_matrix.shape[1]):
        subgroup = (
            np.nan_to_num(
                identity_matrix[:, identity_index],
                nan=0.0,
            )
            >= 0.5
        )

        subgroup_aucs.append(
            safe_roc_auc(
                targets[subgroup],
                predictions[subgroup],
            )
        )

        bpsn_mask = ((~subgroup) & (targets == 1)) | (subgroup & (targets == 0))
        bpsn_aucs.append(
            safe_roc_auc(
                targets[bpsn_mask],
                predictions[bpsn_mask],
            )
        )

        bnsp_mask = ((~subgroup) & (targets == 0)) | (subgroup & (targets == 1))
        bnsp_aucs.append(
            safe_roc_auc(
                targets[bnsp_mask],
                predictions[bnsp_mask],
            )
        )

    subgroup_mean = power_mean(subgroup_aucs, power=-5)
    bpsn_mean = power_mean(bpsn_aucs, power=-5)
    bnsp_mean = power_mean(bnsp_aucs, power=-5)

    score = 0.25 * (overall_auc + subgroup_mean + bpsn_mean + bnsp_mean)

    return {
        "score": float(score),
        "overall_auc": float(overall_auc),
        "subgroup_auc": float(subgroup_mean),
        "bpsn_auc": float(bpsn_mean),
        "bnsp_auc": float(bnsp_mean),
    }


# ============================================================
# Model definition
# ============================================================
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = coefficient
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, grad_outputs):
        return -ctx.coefficient * grad_outputs, None


def gradient_reverse(inputs, coefficient):
    return GradientReversalFunction.apply(inputs, coefficient)


class BiasResistantDebertaClassifier(nn.Module):
    def __init__(
        self,
        pretrained_sequence_classifier,
        style_feature_dim,
        num_auxiliary_targets,
        num_identity_targets,
        adversarial_strength,
    ):
        super().__init__()

        self.backbone = pretrained_sequence_classifier.deberta
        hidden_size = self.backbone.config.hidden_size
        self.adversarial_strength = adversarial_strength

        self.text_norm = nn.LayerNorm(hidden_size)

        self.style_encoder = nn.Sequential(
            nn.LayerNorm(style_feature_dim),
            nn.Linear(style_feature_dim, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.10),
            nn.Linear(hidden_size // 2, hidden_size),
        )

        self.fusion_norm = nn.LayerNorm(hidden_size)

        self.toxicity_head = nn.Sequential(
            nn.Dropout(0.20),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.LayerNorm(hidden_size // 2),
            nn.Dropout(0.15),
            nn.Linear(hidden_size // 2, 1),
        )

        self.auxiliary_head = nn.Sequential(
            nn.Dropout(0.15),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Linear(hidden_size // 2, num_auxiliary_targets),
        )

        self.identity_adversary = nn.Sequential(
            nn.Dropout(0.15),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.10),
            nn.Linear(hidden_size // 2, num_identity_targets),
        )

    def forward(
        self,
        input_ids,
        attention_mask,
        style_features=None,
        token_type_ids=None,
    ):
        backbone_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            return_dict=True,
        )

        representation = self.text_norm(backbone_outputs.last_hidden_state[:, 0])

        if style_features is not None:
            style_features = torch.nan_to_num(
                style_features.float(),
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )

            representation = self.fusion_norm(
                representation + 0.15 * self.style_encoder(style_features)
            )

        toxicity_logits = self.toxicity_head(representation).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(representation)

        identity_logits = self.identity_adversary(
            gradient_reverse(
                representation,
                self.adversarial_strength,
            )
        )

        return {
            "toxicity_logits": toxicity_logits,
            "toxicity_probability": torch.sigmoid(toxicity_logits),
            "auxiliary_logits": auxiliary_logits,
            "identity_logits": identity_logits,
            "representation": representation,
        }


class BiasAwareToxicityLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight,
        identity_weight,
        counterfactual_weight,
    ):
        super().__init__()
        self.auxiliary_weight = auxiliary_weight
        self.identity_weight = identity_weight
        self.counterfactual_weight = counterfactual_weight

    @staticmethod
    def masked_bce(logits, targets):
        valid_mask = torch.isfinite(targets)

        if not torch.any(valid_mask):
            return logits.new_zeros(())

        losses = F.binary_cross_entropy_with_logits(
            logits[valid_mask],
            targets[valid_mask].float().clamp(0.0, 1.0),
            reduction="none",
        )

        return losses.mean()

    def forward(
        self,
        model_outputs,
        toxicity_targets,
        identity_targets=None,
        auxiliary_targets=None,
        counterfactual_outputs=None,
        counterfactual_changed=None,
    ):
        toxicity_targets = toxicity_targets.float().clamp(0.0, 1.0)

        toxicity_loss_per_example = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logits"],
            toxicity_targets,
            reduction="none",
        )

        if identity_targets is not None:
            identity_targets = identity_targets.float()
            identity_observed = torch.isfinite(identity_targets)

            identity_membership = (
                torch.nan_to_num(identity_targets, nan=0.0) >= 0.5
            ).any(dim=1)

            benign_identity = identity_membership.float() * (1.0 - toxicity_targets)
            toxic_identity = identity_membership.float() * toxicity_targets

            example_weights = 1.0 + 3.0 * benign_identity + 1.25 * toxic_identity
            example_weights = example_weights / example_weights.mean().clamp_min(1e-6)
        else:
            identity_observed = None
            example_weights = torch.ones_like(toxicity_loss_per_example)

        toxicity_loss = (toxicity_loss_per_example * example_weights).mean()

        auxiliary_loss = model_outputs["toxicity_logits"].new_zeros(())

        if auxiliary_targets is not None:
            auxiliary_loss = self.masked_bce(
                model_outputs["auxiliary_logits"],
                auxiliary_targets,
            )

        identity_loss = model_outputs["toxicity_logits"].new_zeros(())

        if identity_targets is not None and identity_observed is not None:
            identity_loss = self.masked_bce(
                model_outputs["identity_logits"],
                identity_targets,
            )

        counterfactual_loss = model_outputs["toxicity_logits"].new_zeros(())

        if (
            counterfactual_outputs is not None
            and counterfactual_changed is not None
            and torch.any(counterfactual_changed.bool())
        ):
            changed_mask = counterfactual_changed.bool()

            counterfactual_loss = F.smooth_l1_loss(
                model_outputs["toxicity_probability"][changed_mask],
                counterfactual_outputs["toxicity_probability"][changed_mask],
            )

        total_loss = (
            toxicity_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.identity_weight * identity_loss
            + self.counterfactual_weight * counterfactual_loss
        )

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "identity_adversarial_loss": identity_loss.detach(),
            "counterfactual_loss": counterfactual_loss.detach(),
        }


def build_bias_aware_optimizer(neural_model):
    no_decay_terms = (
        "bias",
        "LayerNorm.weight",
        "layer_norm.weight",
    )

    backbone_decay = []
    backbone_no_decay = []
    head_decay = []
    head_no_decay = []

    for parameter_name, parameter in neural_model.named_parameters():
        if not parameter.requires_grad:
            continue

        uses_weight_decay = not any(term in parameter_name for term in no_decay_terms)
        belongs_to_backbone = parameter_name.startswith("backbone.")

        if belongs_to_backbone and uses_weight_decay:
            backbone_decay.append(parameter)
        elif belongs_to_backbone:
            backbone_no_decay.append(parameter)
        elif uses_weight_decay:
            head_decay.append(parameter)
        else:
            head_no_decay.append(parameter)

    return AdamW(
        [
            {
                "params": backbone_decay,
                "lr": BACKBONE_LEARNING_RATE,
                "weight_decay": WEIGHT_DECAY,
            },
            {
                "params": backbone_no_decay,
                "lr": BACKBONE_LEARNING_RATE,
                "weight_decay": 0.0,
            },
            {
                "params": head_decay,
                "lr": HEAD_LEARNING_RATE,
                "weight_decay": WEIGHT_DECAY,
            },
            {
                "params": head_no_decay,
                "lr": HEAD_LEARNING_RATE,
                "weight_decay": 0.0,
            },
        ],
        betas=(0.9, 0.999),
        eps=1e-8,
    )


style_feature_columns = [f"{column}_z" for column in STYLE_RAW_COLUMNS]

model = BiasResistantDebertaClassifier(
    pretrained_sequence_classifier=model,
    style_feature_dim=len(style_feature_columns),
    num_auxiliary_targets=len(AUXILIARY_TARGET_COLUMNS),
    num_identity_targets=len(IDENTITY_COLUMNS),
    adversarial_strength=ADVERSARIAL_STRENGTH,
)

criterion = BiasAwareToxicityLoss(
    auxiliary_weight=AUXILIARY_LOSS_WEIGHT,
    identity_weight=IDENTITY_ADVERSARIAL_LOSS_WEIGHT,
    counterfactual_weight=COUNTERFACTUAL_CONSISTENCY_WEIGHT,
)

optimizer = build_bias_aware_optimizer(model)


# ============================================================
# Dataset and collator
# ============================================================
class ToxicityTextDataset(Dataset):
    def __init__(self, frame, style_columns, has_labels):
        self.texts = frame["model_text"].fillna("[EMPTY]").astype(str).tolist()
        self.counterfactual_texts = (
            frame["counterfactual_text"].fillna("[EMPTY]").astype(str).tolist()
        )
        self.counterfactual_changed = frame["counterfactual_changed"].to_numpy(
            dtype=np.int8,
            copy=True,
        )
        self.style_features = np.ascontiguousarray(
            frame[style_columns]
            .fillna(0.0)
            .to_numpy(
                dtype=np.float32,
                copy=True,
            )
        )
        self.has_labels = has_labels

        if has_labels:
            self.targets = frame["target"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.auxiliary_targets = np.ascontiguousarray(
                frame[AUXILIARY_TARGET_COLUMNS].to_numpy(
                    dtype=np.float32,
                    copy=True,
                )
            )
            self.identity_targets = np.ascontiguousarray(
                frame[IDENTITY_COLUMNS].to_numpy(
                    dtype=np.float32,
                    copy=True,
                )
            )
        else:
            self.targets = None
            self.auxiliary_targets = None
            self.identity_targets = None

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {
            "text": self.texts[index],
            "counterfactual_text": self.counterfactual_texts[index],
            "counterfactual_changed": self.counterfactual_changed[index],
            "style_features": self.style_features[index],
        }

        if self.has_labels:
            item["target"] = self.targets[index]
            item["auxiliary_targets"] = self.auxiliary_targets[index]
            item["identity_targets"] = self.identity_targets[index]

        return item


class ToxicityBatchCollator:
    def __init__(self, tokenizer_instance, max_length, include_labels):
        self.tokenizer = tokenizer_instance
        self.max_length = max_length
        self.include_labels = include_labels

    def tokenize(self, texts):
        encoded = self.tokenizer(
            texts,
            truncation=True,
            max_length=self.max_length,
            padding=True,
            pad_to_multiple_of=8,
            return_tensors="pt",
        )

        return {
            key: value
            for key, value in encoded.items()
            if key in {"input_ids", "attention_mask", "token_type_ids"}
        }

    def __call__(self, batch):
        output = {
            "encoded_text": self.tokenize([row["text"] for row in batch]),
            "counterfactual_texts": [row["counterfactual_text"] for row in batch],
            "counterfactual_changed": torch.tensor(
                [row["counterfactual_changed"] for row in batch],
                dtype=torch.bool,
            ),
            "style_features": torch.from_numpy(
                np.stack([row["style_features"] for row in batch]).astype(
                    np.float32, copy=False
                )
            ),
        }

        if self.include_labels:
            output["targets"] = torch.tensor(
                [row["target"] for row in batch],
                dtype=torch.float32,
            )

            output["auxiliary_targets"] = torch.from_numpy(
                np.stack([row["auxiliary_targets"] for row in batch]).astype(
                    np.float32, copy=False
                )
            )

            output["identity_targets"] = torch.from_numpy(
                np.stack([row["identity_targets"] for row in batch]).astype(
                    np.float32, copy=False
                )
            )

        return output


# ============================================================
# Data loaders
# ============================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
amp_enabled = torch.cuda.is_available()
pin_memory = device.type == "cuda"
num_workers = min(8, max(2, (os.cpu_count() or 2) // 2))

train_dataset = ToxicityTextDataset(
    train_df,
    style_columns=style_feature_columns,
    has_labels=True,
)

valid_dataset = ToxicityTextDataset(
    valid_df,
    style_columns=style_feature_columns,
    has_labels=True,
)

test_dataset = ToxicityTextDataset(
    test_df,
    style_columns=style_feature_columns,
    has_labels=False,
)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    drop_last=False,
    collate_fn=ToxicityBatchCollator(
        tokenizer,
        max_length=MODEL_MAX_LENGTH,
        include_labels=True,
    ),
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    drop_last=False,
    collate_fn=ToxicityBatchCollator(
        tokenizer,
        max_length=MODEL_MAX_LENGTH,
        include_labels=True,
    ),
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    drop_last=False,
    collate_fn=ToxicityBatchCollator(
        tokenizer,
        max_length=MODEL_MAX_LENGTH,
        include_labels=False,
    ),
)


# ============================================================
# Training utilities
# ============================================================
def move_encoded_to_device(encoded_batch, target_device):
    return {
        key: tensor.to(target_device, non_blocking=True)
        for key, tensor in encoded_batch.items()
    }


def tokenize_counterfactual_batch(texts):
    encoded = tokenizer(
        texts,
        truncation=True,
        max_length=MODEL_MAX_LENGTH,
        padding=True,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )

    encoded = {
        key: value
        for key, value in encoded.items()
        if key in {"input_ids", "attention_mask", "token_type_ids"}
    }

    return move_encoded_to_device(encoded, device)


@torch.no_grad()
def predict_probabilities(data_loader):
    model.eval()
    prediction_chunks = []

    for batch in data_loader:
        encoded_text = move_encoded_to_device(
            batch["encoded_text"],
            device,
        )

        style_features = batch["style_features"].to(
            device,
            non_blocking=True,
        )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                **encoded_text,
                style_features=style_features,
            )

        prediction_chunks.append(outputs["toxicity_probability"].float().cpu().numpy())

    if not prediction_chunks:
        return np.empty(0, dtype=np.float32)

    predictions = np.concatenate(prediction_chunks).astype(
        np.float32,
        copy=False,
    )

    return np.clip(predictions, 1e-6, 1.0 - 1e-6)


# ============================================================
# Training and official-metric checkpoint selection
# ============================================================
model.to(device)
scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)
optimizer.zero_grad(set_to_none=True)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_update_steps = max(1, updates_per_epoch * MAX_EPOCHS)
warmup_steps = max(1, int(total_update_steps * WARMUP_RATIO))


def learning_rate_multiplier(current_step):
    if current_step < warmup_steps:
        return float(current_step + 1) / float(warmup_steps)

    remaining_steps = max(1, total_update_steps - warmup_steps)
    progress = float(current_step - warmup_steps) / float(remaining_steps)
    return max(0.0, 1.0 - progress)


scheduler = LambdaLR(
    optimizer,
    lr_lambda=learning_rate_multiplier,
)

valid_targets_for_metric = valid_df["target_binary"].to_numpy(
    dtype=np.int8,
    copy=True,
)

valid_identity_matrix_for_metric = valid_df[OFFICIAL_IDENTITY_COLUMNS].to_numpy(
    dtype=np.float32,
    copy=True,
)

best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()

    epoch_loss_sum = 0.0
    epoch_example_count = 0
    pending_accumulation_steps = 0

    for batch_index, batch in enumerate(train_loader):
        encoded_text = move_encoded_to_device(
            batch["encoded_text"],
            device,
        )

        style_features = batch["style_features"].to(
            device,
            non_blocking=True,
        )

        toxicity_targets = batch["targets"].to(
            device,
            non_blocking=True,
        )

        auxiliary_targets = batch["auxiliary_targets"].to(
            device,
            non_blocking=True,
        )

        identity_targets = batch["identity_targets"].to(
            device,
            non_blocking=True,
        )

        counterfactual_changed = batch["counterfactual_changed"].to(
            device,
            non_blocking=True,
        )

        should_apply_counterfactual = (
            batch_index % COUNTERFACTUAL_BATCH_FREQUENCY == 0
            and bool(counterfactual_changed.any().item())
        )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            model_outputs = model(
                **encoded_text,
                style_features=style_features,
            )

            counterfactual_outputs = None

            if should_apply_counterfactual:
                counterfactual_encoded = tokenize_counterfactual_batch(
                    batch["counterfactual_texts"]
                )

                counterfactual_outputs = model(
                    **counterfactual_encoded,
                    style_features=style_features,
                )

            loss_components = criterion(
                model_outputs=model_outputs,
                toxicity_targets=toxicity_targets,
                identity_targets=identity_targets,
                auxiliary_targets=auxiliary_targets,
                counterfactual_outputs=counterfactual_outputs,
                counterfactual_changed=(
                    counterfactual_changed if should_apply_counterfactual else None
                ),
            )

            unscaled_loss = loss_components["loss"]
            scaled_loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(unscaled_loss):
            optimizer.zero_grad(set_to_none=True)
            pending_accumulation_steps = 0
            continue

        scaler.scale(scaled_loss).backward()
        pending_accumulation_steps += 1

        batch_size = toxicity_targets.shape[0]
        epoch_loss_sum += float(unscaled_loss.detach().float().item()) * batch_size
        epoch_example_count += batch_size

        is_last_batch = batch_index + 1 == len(train_loader)

        if pending_accumulation_steps >= GRADIENT_ACCUMULATION_STEPS or is_last_batch:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                max_norm=1.0,
            )

            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            optimizer.zero_grad(set_to_none=True)

            pending_accumulation_steps = 0

    validation_predictions = predict_probabilities(valid_loader)

    validation_metrics = official_bias_aware_auc(
        targets=valid_targets_for_metric,
        predictions=validation_predictions,
        identity_matrix=valid_identity_matrix_for_metric,
    )

    validation_score = float(validation_metrics["score"])
    mean_train_loss = epoch_loss_sum / max(1, epoch_example_count)

    is_improved = np.isfinite(validation_score) and validation_score > best_score

    if is_improved:
        best_score = validation_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "validation_metrics": validation_metrics,
            },
            BEST_CHECKPOINT_PATH,
        )

        np.save(
            BEST_VALID_PREDICTIONS_PATH,
            validation_predictions,
        )

        with open(BEST_METRICS_PATH, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "best_epoch": int(best_epoch),
                    "split": "precomputed forward temporal grouped holdout",
                    "official_metric": (
                        "0.25 * overall_auc + 0.25 * power_mean(subgroup_auc, -5) "
                        "+ 0.25 * power_mean(bpsn_auc, -5) "
                        "+ 0.25 * power_mean(bnsp_auc, -5)"
                    ),
                    "metrics": {
                        key: float(value) for key, value in validation_metrics.items()
                    },
                },
                f,
                indent=2,
            )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} "
        f"loss={mean_train_loss:.6f} "
        f"official_score={validation_score:.6f} "
        f"overall={validation_metrics['overall_auc']:.6f} "
        f"subgroup={validation_metrics['subgroup_auc']:.6f} "
        f"bpsn={validation_metrics['bpsn_auc']:.6f} "
        f"bnsp={validation_metrics['bnsp_auc']:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

    gc.collect()

    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# ============================================================
# Reload best model, score validation, predict test, submit
# ============================================================
if not BEST_CHECKPOINT_PATH.exists():
    torch.save(
        {
            "epoch": MAX_EPOCHS,
            "model_state_dict": model.state_dict(),
        },
        BEST_CHECKPOINT_PATH,
    )

best_checkpoint = torch.load(
    BEST_CHECKPOINT_PATH,
    map_location=device,
)

model.load_state_dict(
    best_checkpoint["model_state_dict"],
    strict=True,
)

del best_checkpoint
gc.collect()

best_validation_predictions = predict_probabilities(valid_loader)

final_metrics = official_bias_aware_auc(
    targets=valid_targets_for_metric,
    predictions=best_validation_predictions,
    identity_matrix=valid_identity_matrix_for_metric,
)

score = float(final_metrics["score"])

test_predictions = predict_probabilities(test_loader)

if len(test_predictions) != len(test_df):
    raise RuntimeError(
        f"Test prediction count mismatch: {len(test_predictions)} != {len(test_df)}"
    )

if not np.isfinite(test_predictions).all():
    raise RuntimeError("Non-finite test predictions detected.")

submission = pd.DataFrame(
    {
        "id": test_df["id"].to_numpy(dtype=np.int64, copy=False),
        "prediction": test_predictions.astype(np.float64, copy=False),
    }
)

submission.to_csv(
    SUBMISSION_DIR / "submission_a3a1bae6b466406fb356045a362db453.csv",
    index=False,
)

print(f"Final Validation Score: {score}")
