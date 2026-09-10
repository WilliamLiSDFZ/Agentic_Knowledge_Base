import os
os.sched_setaffinity(0, {9, 5})
import html
import json
import math
import os
import random
import re
import unicodedata
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.cuda.amp import GradScaler, autocast
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
)

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

RANDOM_SEED = 2025
VALIDATION_FRACTION = 0.10

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"
SAMPLE_SUBMISSION_PATH = INPUT_DIR / "sample_submission.csv"

CHECKPOINT_PATH = WORKING_DIR / "best_modernbert_bias_aware_checkpoint.pt"
HISTORY_PATH = WORKING_DIR / "training_evaluation_history.json"
VALIDATION_PREDICTIONS_PATH = WORKING_DIR / "best_validation_predictions.csv"
SUBMISSION_PATH = SUBMISSION_DIR / "submission_670ce0b509ed44bea969c6a337219082.csv"

ALL_IDENTITY_COLUMNS = [
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

METRIC_IDENTITY_COLUMNS = [
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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

MODEL_TARGET_COLUMNS = [
    "target",
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

TOXICITY_LOGIT_INDEX = 0
AUXILIARY_LOSS_WEIGHT = 0.20
BACKBONE_LEARNING_RATE = 1.5e-5
HEAD_LEARNING_RATE = 2.0e-4
WEIGHT_DECAY = 0.01

NUM_EPOCHS = 2
EARLY_STOPPING_PATIENCE = 1
TRAIN_BATCH_SIZE = 8
EVAL_BATCH_SIZE = 16
GRADIENT_ACCUMULATION_STEPS = 4
MAX_SEQUENCE_LENGTH = 320
MAX_GRAD_NORM = 1.0
WARMUP_PROPORTION = 0.03

IDENTITY_PATTERNS = {
    "male": r"\b(?:male|males|man|men|boy|boys|father|fathers|husband|husbands)\b",
    "female": r"\b(?:female|females|woman|women|girl|girls|mother|mothers|wife|wives)\b",
    "homosexual_gay_or_lesbian": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbt|lgbtq|queer)\b"
    ),
    "christian": r"\b(?:christian|christians|christianity|catholic|catholics|protestant)\b",
    "jewish": r"\b(?:jew|jews|jewish|judaism|synagogue)\b",
    "muslim": r"\b(?:muslim|muslims|islam|islamic|mosque)\b",
    "black": r"\b(?:black|blacks|african[\s-]?american|afro[\s-]?american)\b",
    "white": r"\b(?:white|whites|caucasian|caucasians)\b",
    "psychiatric_or_mental_illness": (
        r"\b(?:mental(?:ly)?[\s-]?(?:ill|illness)|psychiatric|depression|depressed|"
        r"schizophren(?:ia|ic)|bipolar|autis(?:m|tic)|crazy|insane)\b"
    ),
}

URL_PATTERN = re.compile(r"(?:(?:https?://|www\.)\S+)", flags=re.IGNORECASE)
EMAIL_PATTERN = re.compile(
    r"\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b",
    flags=re.IGNORECASE,
)
WHITESPACE_PATTERN = re.compile(r"\s+")
PROFANITY_PATTERN = (
    r"\b(?:fuck(?:ing|er|ed|s)?|shit(?:ty)?|asshole(?:s)?|bitch(?:es)?|"
    r"cunt(?:s)?|dick(?:s)?|bastard(?:s)?|idiot(?:s)?|moron(?:s)?)\b"
)
NEGATION_PATTERN = (
    r"\b(?:no|not|never|none|nothing|neither|cannot|can't|won't|don't|isn't|aren't)\b"
)
SECOND_PERSON_PATTERN = r"\b(?:you|your|yours|yourself|yourselves|u)\b"


def clean_comment_text(value):
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", html.unescape(str(value)))
    text = text.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    text = text.replace("\ufeff", "").replace("\u00a0", " ")
    text = URL_PATTERN.sub(" [URL] ", text)
    text = EMAIL_PATTERN.sub(" [EMAIL] ", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text


def clean_text_series(series):
    return series.fillna("").map(clean_comment_text).astype(str)


def build_text_features(clean_text):
    text = clean_text.fillna("").astype(str)
    char_count = text.str.len().clip(lower=0, upper=10000).astype(np.float32)
    word_count = text.str.count(r"\S+").clip(lower=0, upper=3000).astype(np.float32)
    alpha_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    upper_count = text.str.count(r"[A-Z]").astype(np.float32)

    features = pd.DataFrame(index=text.index)
    features["log_char_count"] = np.log1p(char_count).astype(np.float32)
    features["log_word_count"] = np.log1p(word_count).astype(np.float32)
    features["log_unique_token_proxy"] = np.log1p(
        text.str.count(r"\b[A-Za-z0-9_]+\b")
        .clip(lower=0, upper=3000)
        .astype(np.float32)
    ).astype(np.float32)
    features["uppercase_alpha_ratio"] = (
        upper_count / np.maximum(alpha_count, 1.0)
    ).astype(np.float32)
    features["log_exclamation_count"] = np.log1p(
        text.str.count(r"!").clip(lower=0, upper=100).astype(np.float32)
    ).astype(np.float32)
    features["log_question_count"] = np.log1p(
        text.str.count(r"\?").clip(lower=0, upper=100).astype(np.float32)
    ).astype(np.float32)
    features["log_repeated_punctuation_count"] = np.log1p(
        text.str.count(r"[!?]{2,}").clip(lower=0, upper=100).astype(np.float32)
    ).astype(np.float32)
    features["log_all_caps_word_count"] = np.log1p(
        text.str.count(r"\b[A-Z]{3,}\b").clip(lower=0, upper=500).astype(np.float32)
    ).astype(np.float32)
    features["log_digit_count"] = np.log1p(
        text.str.count(r"\d").clip(lower=0, upper=500).astype(np.float32)
    ).astype(np.float32)
    features["has_url"] = text.str.contains(r"\[URL\]", regex=True, na=False).astype(
        np.float32
    )
    features["has_email"] = text.str.contains(
        r"\[EMAIL\]", regex=True, na=False
    ).astype(np.float32)
    features["log_profanity_count"] = np.log1p(
        text.str.count(PROFANITY_PATTERN, flags=re.IGNORECASE)
        .clip(lower=0, upper=100)
        .astype(np.float32)
    ).astype(np.float32)
    features["log_negation_count"] = np.log1p(
        text.str.count(NEGATION_PATTERN, flags=re.IGNORECASE)
        .clip(lower=0, upper=100)
        .astype(np.float32)
    ).astype(np.float32)
    features["log_second_person_count"] = np.log1p(
        text.str.count(SECOND_PERSON_PATTERN, flags=re.IGNORECASE)
        .clip(lower=0, upper=100)
        .astype(np.float32)
    ).astype(np.float32)

    identity_feature_columns = []
    for identity_name, pattern in IDENTITY_PATTERNS.items():
        feature_name = f"text_mentions_{identity_name}"
        features[feature_name] = text.str.contains(
            pattern,
            regex=True,
            case=False,
            na=False,
        ).astype(np.float32)
        identity_feature_columns.append(feature_name)

    features["text_identity_mention_count"] = (
        features[identity_feature_columns].sum(axis=1).astype(np.float32)
    )
    return features.astype(np.float32)


def build_identity_metadata(frame, identity_columns):
    identity_values = frame[identity_columns].astype(np.float32)
    identity_known = identity_values.notna().any(axis=1)
    identity_any = identity_values.fillna(0.0).ge(0.5).any(axis=1)

    return pd.DataFrame(
        {
            "identity_label_available": identity_known.astype(np.uint8),
            "identity_any": identity_any.astype(np.uint8),
        },
        index=frame.index,
    )


def make_bias_aware_training_weights(frame, identity_columns):
    target_binary = frame["target"].to_numpy(dtype=np.float32) >= 0.5
    identity_values = frame[identity_columns].to_numpy(dtype=np.float32)
    identity_known = np.isfinite(identity_values).any(axis=1)
    subgroup = np.nan_to_num(identity_values, nan=0.0).max(axis=1) >= 0.5

    weights = np.ones(len(frame), dtype=np.float32)
    eligible = identity_known

    weights[eligible & subgroup] += 1.0
    weights[eligible & subgroup & ~target_binary] += 4.0
    weights[eligible & ~subgroup & target_binary] += 4.0

    weights /= np.maximum(weights.mean(), 1e-8)
    return weights.astype(np.float32)


def save_processed_frame(frame, stem):
    parquet_path = WORKING_DIR / f"{stem}.parquet"
    pickle_path = WORKING_DIR / f"{stem}.pkl"

    try:
        frame.to_parquet(parquet_path, index=False, compression="snappy")
        if pickle_path.exists():
            pickle_path.unlink()
        return str(parquet_path)
    except Exception:
        frame.to_pickle(pickle_path, protocol=4)
        if parquet_path.exists():
            parquet_path.unlink()
        return str(pickle_path)


def safe_auc(binary_labels, predictions, metric_name):
    binary_labels = np.asarray(binary_labels, dtype=np.uint8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if binary_labels.shape[0] != predictions.shape[0]:
        raise ValueError(
            f"{metric_name}: labels and predictions have incompatible lengths."
        )
    if np.unique(binary_labels).size != 2:
        raise ValueError(
            f"{metric_name}: ROC-AUC is undefined because the evaluation subset "
            f"does not contain both toxicity classes."
        )
    return float(roc_auc_score(binary_labels, predictions))


def power_mean(values, power=-5):
    values = np.asarray(values, dtype=np.float64)
    if values.size == 0:
        raise ValueError("Cannot compute a generalized mean without subgroup AUCs.")
    if not np.isfinite(values).all():
        raise ValueError("Subgroup metrics contain non-finite values.")

    values = np.clip(values, 1e-15, 1.0)
    return float(np.mean(values**power) ** (1.0 / power))


def official_jigsaw_bias_metric(validation_frame, predictions):
    if len(validation_frame) != len(predictions):
        raise ValueError("Validation prediction count does not match validation rows.")

    required_identity_columns = list(available_metric_identity_columns)
    if not required_identity_columns:
        raise ValueError(
            "No official metric identity columns are available for bias evaluation."
        )

    target_binary = (
        validation_frame["target"].to_numpy(dtype=np.float32) >= 0.5
    ).astype(np.uint8)

    overall_auc = safe_auc(target_binary, predictions, "overall_auc")
    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in required_identity_columns:
        subgroup = (
            validation_frame[identity_column].fillna(0.0).to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & (target_binary == 0)) | (
            (~subgroup) & (target_binary == 1)
        )
        bnsp_mask = (subgroup & (target_binary == 1)) | (
            (~subgroup) & (target_binary == 0)
        )

        subgroup_auc = safe_auc(
            target_binary[subgroup_mask],
            predictions[subgroup_mask],
            f"{identity_column}_subgroup_auc",
        )
        bpsn_auc = safe_auc(
            target_binary[bpsn_mask],
            predictions[bpsn_mask],
            f"{identity_column}_bpsn_auc",
        )
        bnsp_auc = safe_auc(
            target_binary[bnsp_mask],
            predictions[bnsp_mask],
            f"{identity_column}_bnsp_auc",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity[identity_column] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
            "subgroup_examples": int(subgroup_mask.sum()),
            "bpsn_examples": int(bpsn_mask.sum()),
            "bnsp_examples": int(bnsp_mask.sum()),
        }

    subgroup_power_mean = power_mean(subgroup_aucs, power=-5)
    bpsn_power_mean = power_mean(bpsn_aucs, power=-5)
    bnsp_power_mean = power_mean(bnsp_aucs, power=-5)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    return {
        "final_score": final_score,
        "overall_auc": overall_auc,
        "subgroup_auc_power_mean": subgroup_power_mean,
        "bpsn_auc_power_mean": bpsn_power_mean,
        "bnsp_auc_power_mean": bnsp_power_mean,
        "per_identity": per_identity,
    }


class FusedModernBertToxicityModel(nn.Module):
    def __init__(self, pretrained_backbone, engineered_feature_dim, dropout=0.15):
        super().__init__()

        self.backbone = pretrained_backbone
        self.engineered_feature_dim = int(engineered_feature_dim)
        hidden_size = int(self.backbone.config.hidden_size)
        feature_hidden_size = min(256, max(64, hidden_size // 4))

        self.text_normalization = nn.LayerNorm(hidden_size)

        self.feature_encoder = nn.Sequential(
            nn.LayerNorm(self.engineered_feature_dim),
            nn.Linear(self.engineered_feature_dim, feature_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(feature_hidden_size, feature_hidden_size),
            nn.GELU(),
        )

        fusion_hidden_size = hidden_size
        self.fusion_head = nn.Sequential(
            nn.LayerNorm(hidden_size + feature_hidden_size),
            nn.Linear(hidden_size + feature_hidden_size, fusion_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(fusion_hidden_size, fusion_hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(fusion_hidden_size // 2, len(MODEL_TARGET_COLUMNS)),
        )

    def forward(self, input_ids, attention_mask, engineered_features):
        backbone_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
            return_dict=True,
        )

        final_hidden_states = backbone_outputs.hidden_states[-1]
        text_embedding = self.text_normalization(final_hidden_states[:, 0, :])

        if engineered_features is None:
            raise ValueError(
                "engineered_features is required and must contain the standardized "
                "features produced during data processing."
            )

        engineered_features = engineered_features.to(
            device=text_embedding.device,
            dtype=text_embedding.dtype,
        )

        if engineered_features.ndim != 2:
            raise ValueError(
                "engineered_features must have shape [batch_size, num_features]."
            )

        if engineered_features.shape[1] != self.engineered_feature_dim:
            raise ValueError(
                f"Expected {self.engineered_feature_dim} engineered features, "
                f"received {engineered_features.shape[1]}."
            )

        feature_embedding = self.feature_encoder(engineered_features)
        fused_embedding = torch.cat([text_embedding, feature_embedding], dim=-1)
        return self.fusion_head(fused_embedding)

    def predict_toxicity_probability(
        self,
        input_ids,
        attention_mask,
        engineered_features,
    ):
        logits = self.forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            engineered_features=engineered_features,
        )
        return torch.sigmoid(logits[:, TOXICITY_LOGIT_INDEX])


class BiasAwareMultiTaskBCELoss(nn.Module):
    def __init__(self, auxiliary_loss_weight=AUXILIARY_LOSS_WEIGHT):
        super().__init__()
        self.auxiliary_loss_weight = float(auxiliary_loss_weight)

    def forward(self, logits, targets, toxicity_sample_weight=None):
        if logits.ndim != 2 or logits.shape[1] != len(MODEL_TARGET_COLUMNS):
            raise ValueError(
                f"logits must have shape [batch_size, {len(MODEL_TARGET_COLUMNS)}]."
            )
        if targets.shape != logits.shape:
            raise ValueError(
                f"targets shape {tuple(targets.shape)} does not match logits shape "
                f"{tuple(logits.shape)}."
            )

        targets = targets.to(device=logits.device, dtype=logits.dtype)
        toxicity_targets = targets[:, TOXICITY_LOGIT_INDEX]
        valid_toxicity = torch.isfinite(toxicity_targets)

        if not torch.any(valid_toxicity):
            raise ValueError("A training batch contains no finite toxicity targets.")

        toxicity_losses = F.binary_cross_entropy_with_logits(
            logits[:, TOXICITY_LOGIT_INDEX],
            torch.nan_to_num(toxicity_targets, nan=0.0).clamp(0.0, 1.0),
            reduction="none",
        )

        if toxicity_sample_weight is None:
            toxicity_weights = torch.ones_like(toxicity_losses)
        else:
            toxicity_weights = toxicity_sample_weight.to(
                device=logits.device,
                dtype=logits.dtype,
            ).flatten()

            if toxicity_weights.shape != toxicity_losses.shape:
                raise ValueError(
                    "toxicity_sample_weight must have one value per batch example."
                )

            toxicity_weights = toxicity_weights.clamp_min(0.0)

        toxicity_weights = toxicity_weights * valid_toxicity.to(logits.dtype)
        toxicity_loss = (
            toxicity_losses * toxicity_weights
        ).sum() / toxicity_weights.sum().clamp_min(1.0)

        auxiliary_logits = logits[:, 1:]
        auxiliary_targets = targets[:, 1:]
        valid_auxiliary = torch.isfinite(auxiliary_targets)

        if torch.any(valid_auxiliary):
            auxiliary_losses = F.binary_cross_entropy_with_logits(
                auxiliary_logits,
                torch.nan_to_num(auxiliary_targets, nan=0.0).clamp(0.0, 1.0),
                reduction="none",
            )
            auxiliary_loss = (
                auxiliary_losses * valid_auxiliary.to(logits.dtype)
            ).sum() / valid_auxiliary.sum().clamp_min(1.0)
        else:
            auxiliary_loss = logits.new_zeros(())

        return toxicity_loss + self.auxiliary_loss_weight * auxiliary_loss


class ToxicityFrameDataset(Dataset):
    def __init__(
        self, frame, feature_columns, include_labels=False, include_weights=False
    ):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=True)
        self.features = frame.loc[:, feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.include_labels = bool(include_labels)
        self.include_weights = bool(include_weights)

        if self.include_labels:
            missing_target_columns = [
                column for column in MODEL_TARGET_COLUMNS if column not in frame.columns
            ]
            if missing_target_columns:
                raise ValueError(
                    f"Processed frame is missing model target columns: "
                    f"{missing_target_columns}"
                )

            self.targets = frame.loc[:, MODEL_TARGET_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )

        if self.include_weights:
            if "bias_aware_sample_weight" not in frame.columns:
                raise ValueError(
                    "Training frame lacks bias_aware_sample_weight created during "
                    "data processing."
                )
            self.weights = frame["bias_aware_sample_weight"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.include_labels and self.include_weights:
            return (
                self.texts[index],
                self.features[index],
                self.targets[index],
                self.weights[index],
            )
        if self.include_labels:
            return self.texts[index], self.features[index], self.targets[index]
        return self.texts[index], self.features[index]


seed_value = int(RANDOM_SEED)
random.seed(seed_value)
np.random.seed(seed_value)
torch.manual_seed(seed_value)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed_value)
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = False
    try:
        torch.set_float32_matmul_precision("high")
    except AttributeError:
        pass

train_header = pd.read_csv(TRAIN_PATH, nrows=0).columns.tolist()
available_identity_columns = [
    column for column in ALL_IDENTITY_COLUMNS if column in train_header
]
available_metric_identity_columns = [
    column for column in METRIC_IDENTITY_COLUMNS if column in train_header
]
available_auxiliary_columns = [
    column for column in AUXILIARY_TARGET_COLUMNS if column in train_header
]

required_train_columns = ["id", "comment_text", "target"]
train_usecols = list(
    dict.fromkeys(
        required_train_columns
        + available_identity_columns
        + available_auxiliary_columns
    )
)

float_columns = ["target"] + available_identity_columns + available_auxiliary_columns
train_dtypes = {column: np.float32 for column in float_columns}
train_dtypes["id"] = np.int64

train_full = pd.read_csv(
    TRAIN_PATH,
    usecols=train_usecols,
    dtype=train_dtypes,
    low_memory=False,
)

test_full = pd.read_csv(
    TEST_PATH,
    usecols=["id", "comment_text"],
    dtype={"id": np.int64},
    low_memory=False,
)

raw_group_text = train_full["comment_text"].fillna("").astype(str)
group_ids = pd.util.hash_pandas_object(
    raw_group_text,
    index=False,
).to_numpy(dtype=np.uint64)
del raw_group_text

target_binary_full = (train_full["target"].to_numpy(dtype=np.float32) >= 0.5).astype(
    np.uint8
)

split_identity_metadata = build_identity_metadata(
    train_full,
    available_metric_identity_columns,
)

split_labels = (
    target_binary_full.astype(np.int16) * 4
    + split_identity_metadata["identity_label_available"].to_numpy(dtype=np.int16) * 2
    + split_identity_metadata["identity_any"].to_numpy(dtype=np.int16)
)

unique_labels, label_counts = np.unique(split_labels, return_counts=True)
minimum_label_count = int(label_counts.min()) if len(unique_labels) else 0

if minimum_label_count >= 2:
    n_splits = min(10, minimum_label_count)
    group_splitter = StratifiedGroupKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=RANDOM_SEED,
    )
    train_indices, valid_indices = next(
        group_splitter.split(
            X=np.zeros(len(train_full), dtype=np.uint8),
            y=split_labels,
            groups=group_ids,
        )
    )
else:
    group_splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=VALIDATION_FRACTION,
        random_state=RANDOM_SEED,
    )
    train_indices, valid_indices = next(
        group_splitter.split(
            X=np.zeros(len(train_full), dtype=np.uint8),
            groups=group_ids,
        )
    )

train_raw = train_full.iloc[train_indices].reset_index(drop=True)
valid_raw = train_full.iloc[valid_indices].reset_index(drop=True)
test_raw = test_full.reset_index(drop=True)

del train_full
del test_full
del group_ids
del target_binary_full
del split_identity_metadata
del split_labels
del train_indices
del valid_indices

train_text = clean_text_series(train_raw["comment_text"]).reset_index(drop=True)
valid_text = clean_text_series(valid_raw["comment_text"]).reset_index(drop=True)
test_text = clean_text_series(test_raw["comment_text"]).reset_index(drop=True)

train_features = build_text_features(train_text).reset_index(drop=True)
valid_features = build_text_features(valid_text).reset_index(drop=True)
test_features = build_text_features(test_text).reset_index(drop=True)

feature_columns = train_features.columns.tolist()

feature_scaler = StandardScaler(copy=True)
feature_scaler.fit(train_features[feature_columns].to_numpy(dtype=np.float32))

train_features.loc[:, feature_columns] = feature_scaler.transform(
    train_features[feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)

valid_features.loc[:, feature_columns] = feature_scaler.transform(
    valid_features[feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)

test_features.loc[:, feature_columns] = feature_scaler.transform(
    test_features[feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)

joblib.dump(feature_scaler, WORKING_DIR / "text_feature_scaler.joblib")

train_identity_metadata = build_identity_metadata(
    train_raw,
    available_metric_identity_columns,
).reset_index(drop=True)

valid_identity_metadata = build_identity_metadata(
    valid_raw,
    available_metric_identity_columns,
).reset_index(drop=True)

train_label_columns = (
    ["id", "target"] + available_auxiliary_columns + available_identity_columns
)

train_processed = train_raw[train_label_columns].copy().reset_index(drop=True)
train_processed.insert(1, "model_text", train_text)
train_processed["target_binary"] = (
    train_processed["target"].to_numpy(dtype=np.float32) >= 0.5
).astype(np.uint8)

train_processed = pd.concat(
    [train_processed, train_identity_metadata, train_features],
    axis=1,
)

train_processed["bias_aware_sample_weight"] = make_bias_aware_training_weights(
    train_raw,
    available_metric_identity_columns,
)

valid_processed = valid_raw[train_label_columns].copy().reset_index(drop=True)
valid_processed.insert(1, "model_text", valid_text)
valid_processed["target_binary"] = (
    valid_processed["target"].to_numpy(dtype=np.float32) >= 0.5
).astype(np.uint8)

valid_processed = pd.concat(
    [valid_processed, valid_identity_metadata, valid_features],
    axis=1,
)

test_processed = test_raw[["id"]].copy().reset_index(drop=True)
test_processed["model_text"] = test_text
test_processed = pd.concat([test_processed, test_features], axis=1)

train_output_path = save_processed_frame(train_processed, "train_processed")
valid_output_path = save_processed_frame(valid_processed, "valid_processed")
test_output_path = save_processed_frame(test_processed, "test_processed")

manifest = {
    "random_seed": RANDOM_SEED,
    "validation_fraction_requested": VALIDATION_FRACTION,
    "split_strategy": (
        "StratifiedGroupKFold on exact raw-comment hash, stratified by "
        "target_binary, identity annotation availability, and identity_any"
    ),
    "group_key": (
        "pandas hash of unmodified comment_text; duplicate raw comments are "
        "isolated to one fold"
    ),
    "target_column": "target",
    "binary_target_rule": "target >= 0.5",
    "text_column": "model_text",
    "feature_columns": feature_columns,
    "training_only_weight_column": "bias_aware_sample_weight",
    "identity_columns_available": available_identity_columns,
    "metric_identity_columns_available": available_metric_identity_columns,
    "auxiliary_target_columns_available": available_auxiliary_columns,
    "validation_metric_protocol": {
        "overall_auc": True,
        "subgroup_auc": True,
        "bpsn_auc": True,
        "bnsp_auc": True,
        "power_mean_p": -5,
        "final_metric_weights": {
            "overall_auc": 0.25,
            "subgroup_auc_power_mean": 0.25,
            "bpsn_auc_power_mean": 0.25,
            "bnsp_auc_power_mean": 0.25,
        },
    },
    "artifacts": {
        "train_processed": train_output_path,
        "valid_processed": valid_output_path,
        "test_processed": test_output_path,
        "feature_scaler": str(WORKING_DIR / "text_feature_scaler.joblib"),
    },
    "row_counts": {
        "train": int(len(train_processed)),
        "validation": int(len(valid_processed)),
        "test": int(len(test_processed)),
    },
}

with open(
    WORKING_DIR / "data_processing_manifest.json",
    "w",
    encoding="utf-8",
) as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

engineered_feature_dim = len(feature_columns)
if engineered_feature_dim <= 0:
    raise ValueError("No engineered feature columns were created.")

model = FusedModernBertToxicityModel(
    pretrained_backbone=model,
    engineered_feature_dim=engineered_feature_dim,
    dropout=0.15,
)

criterion = BiasAwareMultiTaskBCELoss(
    auxiliary_loss_weight=AUXILIARY_LOSS_WEIGHT,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")

optimizer_parameter_groups = [
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and name.startswith("backbone.")
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": BACKBONE_LEARNING_RATE,
        "weight_decay": WEIGHT_DECAY,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and name.startswith("backbone.")
            and any(term in name for term in no_decay_terms)
        ],
        "lr": BACKBONE_LEARNING_RATE,
        "weight_decay": 0.0,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and not name.startswith("backbone.")
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": HEAD_LEARNING_RATE,
        "weight_decay": WEIGHT_DECAY,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and not name.startswith("backbone.")
            and any(term in name for term in no_decay_terms)
        ],
        "lr": HEAD_LEARNING_RATE,
        "weight_decay": 0.0,
    },
]

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()

model.to(device)

tokenizer_max_length = getattr(tokenizer, "model_max_length", MAX_SEQUENCE_LENGTH)
if tokenizer_max_length is None or tokenizer_max_length > 100000:
    tokenizer_max_length = MAX_SEQUENCE_LENGTH

MAX_SEQUENCE_LENGTH = min(MAX_SEQUENCE_LENGTH, int(tokenizer_max_length))


def toxicity_collate(batch):
    texts = [row[0] for row in batch]

    encoded = tokenizer(
        texts,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        padding=True,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    collated = {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "engineered_features": torch.from_numpy(
            np.stack([row[1] for row in batch]).astype(np.float32, copy=False)
        ),
    }

    if len(batch[0]) >= 3:
        collated["targets"] = torch.from_numpy(
            np.stack([row[2] for row in batch]).astype(np.float32, copy=False)
        )

    if len(batch[0]) == 4:
        collated["sample_weights"] = torch.from_numpy(
            np.asarray([row[3] for row in batch], dtype=np.float32)
        )

    return collated


num_workers = max(2, min(8, os.cpu_count() or 2))

loader_kwargs = {
    "num_workers": num_workers,
    "pin_memory": True,
    "collate_fn": toxicity_collate,
}

train_dataset = ToxicityFrameDataset(
    train_processed,
    feature_columns=feature_columns,
    include_labels=True,
    include_weights=True,
)

valid_dataset = ToxicityFrameDataset(
    valid_processed,
    feature_columns=feature_columns,
    include_labels=True,
    include_weights=False,
)

test_dataset = ToxicityFrameDataset(
    test_processed,
    feature_columns=feature_columns,
    include_labels=False,
    include_weights=False,
)

train_generator = torch.Generator()
train_generator.manual_seed(seed_value)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=False,
    generator=train_generator,
    **loader_kwargs,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)

optimizer_updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)

total_optimizer_updates = max(
    1,
    optimizer_updates_per_epoch * NUM_EPOCHS,
)

warmup_updates = max(
    1,
    int(total_optimizer_updates * WARMUP_PROPORTION),
)


def cosine_warmup_multiplier(step_number):
    if step_number < warmup_updates:
        return float(step_number + 1) / float(warmup_updates)

    progress = float(step_number - warmup_updates) / float(
        max(1, total_optimizer_updates - warmup_updates)
    )

    return max(0.0, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(
    optimizer,
    lr_lambda=cosine_warmup_multiplier,
)

scaler = GradScaler(enabled=amp_enabled)


def move_batch_to_device(batch):
    return {
        key: (
            value.to(device, non_blocking=True)
            if isinstance(value, torch.Tensor)
            else value
        )
        for key, value in batch.items()
    }


def run_model_inference(data_loader, calculate_loss=False):
    model.eval()
    prediction_chunks = []
    loss_sum = torch.zeros((), device=device)
    example_count = 0

    with torch.no_grad():
        for batch in data_loader:
            batch = move_batch_to_device(batch)

            with autocast(enabled=amp_enabled):
                logits = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    engineered_features=batch["engineered_features"],
                )

                probabilities = torch.sigmoid(logits[:, TOXICITY_LOGIT_INDEX])

                if calculate_loss:
                    batch_loss = criterion(
                        logits=logits,
                        targets=batch["targets"],
                        toxicity_sample_weight=None,
                    )

            batch_size = probabilities.shape[0]
            prediction_chunks.append(probabilities.detach().float().cpu().numpy())
            example_count += batch_size

            if calculate_loss:
                loss_sum += batch_loss.detach() * batch_size

    predictions = np.concatenate(prediction_chunks, axis=0).astype(np.float64)

    if not np.isfinite(predictions).all():
        raise FloatingPointError("Model inference produced non-finite probabilities.")

    mean_loss = (
        float((loss_sum / max(example_count, 1)).detach().cpu())
        if calculate_loss
        else None
    )

    return predictions, mean_loss


best_score = -float("inf")
best_epoch = 0
epochs_without_improvement = 0
training_history = []

for epoch in range(1, NUM_EPOCHS + 1):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    epoch_loss_sum = torch.zeros((), device=device)
    epoch_example_count = 0

    for batch_index, batch in enumerate(train_loader):
        batch = move_batch_to_device(batch)

        with autocast(enabled=amp_enabled):
            logits = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                engineered_features=batch["engineered_features"],
            )

            batch_loss = criterion(
                logits=logits,
                targets=batch["targets"],
                toxicity_sample_weight=batch["sample_weights"],
            )

            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(batch_loss):
            raise FloatingPointError(
                f"Encountered non-finite training loss in epoch {epoch}."
            )

        scaler.scale(scaled_loss).backward()

        is_accumulation_boundary = (
            batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0 or (batch_index + 1) == len(train_loader)

        if is_accumulation_boundary:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                MAX_GRAD_NORM,
            )
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_size = batch["input_ids"].shape[0]
        epoch_loss_sum += batch_loss.detach() * batch_size
        epoch_example_count += batch_size

    train_loss = float((epoch_loss_sum / max(epoch_example_count, 1)).detach().cpu())

    valid_predictions, validation_loss = run_model_inference(
        valid_loader,
        calculate_loss=True,
    )

    validation_metrics = official_jigsaw_bias_metric(
        valid_processed,
        valid_predictions,
    )

    epoch_score = validation_metrics["final_score"]

    epoch_record = {
        "epoch": epoch,
        "train_loss": train_loss,
        "validation_loss": validation_loss,
        "official_validation_metrics": validation_metrics,
        "learning_rates": [
            float(parameter_group["lr"]) for parameter_group in optimizer.param_groups
        ],
    }

    training_history.append(epoch_record)

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_validation_score": best_score,
                "model_state_dict": model.state_dict(),
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "feature_columns": list(feature_columns),
                "model_target_columns": list(MODEL_TARGET_COLUMNS),
            },
            CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch}/{NUM_EPOCHS} | "
        f"train_loss={train_loss:.6f} | "
        f"valid_loss={validation_loss:.6f} | "
        f"official_score={epoch_score:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if not CHECKPOINT_PATH.exists():
    raise FileNotFoundError("Best checkpoint was not created during training.")

best_checkpoint = torch.load(
    CHECKPOINT_PATH,
    map_location=device,
)

model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(device)

best_validation_predictions, best_validation_loss = run_model_inference(
    valid_loader,
    calculate_loss=True,
)

best_validation_metrics = official_jigsaw_bias_metric(
    valid_processed,
    best_validation_predictions,
)

score = float(best_validation_metrics["final_score"])

validation_audit = pd.DataFrame(
    {
        "id": valid_processed["id"].to_numpy(),
        "target": valid_processed["target"].to_numpy(dtype=np.float32),
        "target_binary": (
            valid_processed["target"].to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.uint8),
        "prediction": best_validation_predictions,
    }
)

validation_audit.to_csv(
    VALIDATION_PREDICTIONS_PATH,
    index=False,
)

training_summary = {
    "selection_metric": (
        "Official Jigsaw unintended-bias metric: mean of overall ROC-AUC and "
        "generalized power means (p=-5) of subgroup, BPSN, and BNSP ROC-AUCs."
    ),
    "identity_threshold": "identity >= 0.5",
    "toxicity_threshold_for_metric_labels": "target >= 0.5",
    "best_epoch": int(best_epoch),
    "best_checkpoint_score_during_training": float(best_score),
    "reloaded_checkpoint_validation_loss": float(best_validation_loss),
    "reloaded_checkpoint_validation_metrics": best_validation_metrics,
    "epoch_history": training_history,
    "checkpoint_path": str(CHECKPOINT_PATH),
    "validation_prediction_audit_path": str(VALIDATION_PREDICTIONS_PATH),
    "submission_path": str(SUBMISSION_PATH),
}

with open(HISTORY_PATH, "w", encoding="utf-8") as history_file:
    json.dump(training_summary, history_file, indent=2)

test_predictions, _ = run_model_inference(
    test_loader,
    calculate_loss=False,
)

if len(test_predictions) != len(test_processed):
    raise RuntimeError(
        "Test inference did not produce exactly one model prediction per test row."
    )

if not np.isfinite(test_predictions).all():
    raise FloatingPointError("Test inference produced non-finite predictions.")

submission = pd.DataFrame(
    {
        "id": test_processed["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if submission["id"].duplicated().any():
    raise ValueError("Submission IDs are unexpectedly duplicated.")

if list(submission.columns) != ["id", "prediction"]:
    raise ValueError("Submission columns do not match the required format.")

if SAMPLE_SUBMISSION_PATH.exists():
    sample_submission_columns = pd.read_csv(
        SAMPLE_SUBMISSION_PATH,
        nrows=0,
    ).columns.tolist()

    if sample_submission_columns != ["id", "prediction"]:
        raise ValueError(
            "sample_submission.csv does not use the expected id,prediction format."
        )

    if len(submission) != len(pd.read_csv(SAMPLE_SUBMISSION_PATH, usecols=["id"])):
        raise ValueError(
            "Submission row count does not match sample_submission.csv row count."
        )

submission.to_csv(SUBMISSION_PATH, index=False)

print(f"Final Validation Score: {score}")
