import os
os.sched_setaffinity(0, {76, 77})
import gc
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
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
    get_cosine_schedule_with_warmup,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2027
VALID_FRACTION = 0.20

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")
WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TARGET_COLUMN = "target"
TEXT_COLUMN = "comment_text"
ID_COLUMN = "id"
GROUP_COLUMN = "article_id"

MODEL_ID = "answerdotai/ModernBERT-large"
NUM_SUBTYPE_LABELS = 6
NUM_OUTPUT_LABELS = 1 + NUM_SUBTYPE_LABELS
MAX_SEQUENCE_LENGTH = 1024
TOKEN_MAX_LENGTH = min(MAX_SEQUENCE_LENGTH, 512)

NUM_EPOCHS = 2
PATIENCE = 1
NUM_WORKERS = 2
BEST_MODEL_PATH = WORKING_DIR / "best_bias_aware_modernbert.pt"

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

SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
EMAIL_RE = re.compile(r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
WHITESPACE_RE = re.compile(r"\s+")
SEPARATED_CHARS_RE = re.compile(r"(?i)(?<!\w)(?:[a-z]\s+){3,}[a-z](?!\w)")
ELONGATED_RE = re.compile(r"(?i)([a-z])\1{2,}")
LEET_TOKEN_RE = re.compile(r"(?i)\b[a-z@$][a-z0-9@$]{2,}\b")
LEET_TRANSLATION = str.maketrans(
    {
        "@": "a",
        "$": "s",
        "0": "o",
        "1": "i",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t",
    }
)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)


def truncate_text(text, max_chars=7600, tail_chars=1300):
    if len(text) <= max_chars:
        return text
    head_chars = max_chars - tail_chars
    return f"{text[:head_chars]} [TRUNCATED] {text[-tail_chars:]}"


def clean_comment(value):
    if pd.isna(value):
        return ""

    text = str(value)
    if "&" in text:
        text = html.unescape(text)

    text = unicodedata.normalize("NFKC", text)
    text = ZERO_WIDTH_RE.sub("", text)
    text = URL_RE.sub(" [URL] ", text)
    text = EMAIL_RE.sub(" [EMAIL] ", text)
    text = WHITESPACE_RE.sub(" ", text).strip()

    return truncate_text(text)


def deobfuscate_comment(text):
    text = text.lower()

    def join_separated(match):
        return re.sub(r"\s+", "", match.group(0))

    def normalize_leet(match):
        token = match.group(0)
        if any(ch in token for ch in "@$013457") and any(ch.isalpha() for ch in token):
            return token.translate(LEET_TRANSLATION)
        return token

    text = SEPARATED_CHARS_RE.sub(join_separated, text)
    text = LEET_TOKEN_RE.sub(normalize_leet, text)
    text = ELONGATED_RE.sub(r"\1\1", text)
    text = WHITESPACE_RE.sub(" ", text).strip()

    return text


def build_text_features(clean_text, robust_text):
    clean_text = clean_text.astype(str)
    robust_text = robust_text.astype(str)

    char_count = clean_text.str.len().to_numpy(dtype=np.float32)
    token_count = clean_text.str.count(r"\S+").to_numpy(dtype=np.float32)
    letter_count = clean_text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = clean_text.str.count(r"\d").to_numpy(dtype=np.float32)
    exclamation_count = clean_text.str.count(r"!").to_numpy(dtype=np.float32)
    question_count = clean_text.str.count(r"\?").to_numpy(dtype=np.float32)
    punctuation_count = clean_text.str.count(r"[^\w\s]").to_numpy(dtype=np.float32)
    quoted_count = clean_text.str.count(r'["“”\']').to_numpy(dtype=np.float32)
    caps_token_count = clean_text.str.count(r"\b[A-Z]{2,}\b").to_numpy(dtype=np.float32)
    url_count = clean_text.str.count(r"\[URL\]").to_numpy(dtype=np.float32)
    email_count = clean_text.str.count(r"\[EMAIL\]").to_numpy(dtype=np.float32)

    safe_chars = np.maximum(char_count, 1.0)
    safe_letters = np.maximum(letter_count, 1.0)

    changed_by_robust_view = (
        robust_text.to_numpy(dtype=str) != clean_text.str.lower().to_numpy(dtype=str)
    ).astype(np.float32)

    return pd.DataFrame(
        {
            "log_char_count": np.log1p(np.minimum(char_count, 8000.0)),
            "log_token_count": np.log1p(np.minimum(token_count, 2000.0)),
            "mean_token_length": char_count / np.maximum(token_count, 1.0),
            "uppercase_letter_ratio": uppercase_count / safe_letters,
            "digit_ratio": digit_count / safe_chars,
            "punctuation_ratio": punctuation_count / safe_chars,
            "exclamation_ratio": exclamation_count / safe_chars,
            "question_ratio": question_count / safe_chars,
            "quote_ratio": quoted_count / safe_chars,
            "log_caps_token_count": np.log1p(np.minimum(caps_token_count, 100.0)),
            "log_url_count": np.log1p(url_count),
            "log_email_count": np.log1p(email_count),
            "obfuscation_normalized": changed_by_robust_view,
            "was_truncated": clean_text.str.contains(
                r"\[TRUNCATED\]", regex=True
            ).to_numpy(dtype=np.float32),
        },
        index=clean_text.index,
        dtype=np.float32,
    )


def make_processed_frame(raw_frame, include_labels):
    clean_text = raw_frame[TEXT_COLUMN].map(clean_comment)
    robust_text = clean_text.map(deobfuscate_comment)
    text_features = build_text_features(clean_text, robust_text)

    processed = pd.DataFrame(
        {
            ID_COLUMN: raw_frame[ID_COLUMN].to_numpy(copy=False),
            "clean_text": clean_text.to_numpy(dtype=object),
            "robust_text": robust_text.to_numpy(dtype=object),
        },
        index=raw_frame.index,
    )

    if include_labels:
        processed[TARGET_COLUMN] = raw_frame[TARGET_COLUMN].astype(np.float32)
        processed["target_binary"] = (
            raw_frame[TARGET_COLUMN].to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.float32)

        for column in SUBTYPE_COLUMNS:
            if column in raw_frame.columns:
                processed[column] = raw_frame[column].fillna(0.0).astype(np.float32)

        for column in IDENTITY_COLUMNS:
            if column in raw_frame.columns:
                processed[column] = raw_frame[column].astype(np.float32)

        toxicity_counts = (
            raw_frame["toxicity_annotator_count"].fillna(0).to_numpy(dtype=np.float32)
        )
        identity_counts = (
            raw_frame["identity_annotator_count"].fillna(0).to_numpy(dtype=np.float32)
        )

        processed["toxicity_annotator_count"] = toxicity_counts
        processed["identity_annotator_count"] = identity_counts
        processed["identity_labels_available"] = (identity_counts > 0).astype(
            np.float32
        )
        processed["label_consensus"] = (
            2.0 * np.abs(raw_frame[TARGET_COLUMN].to_numpy(dtype=np.float32) - 0.5)
        ).astype(np.float32)
        processed["label_precision_weight"] = np.log1p(toxicity_counts).astype(
            np.float32
        )

    return processed, text_features


def save_dataframe(frame, stem):
    parquet_path = WORKING_DIR / f"{stem}.parquet"
    try:
        frame.to_parquet(parquet_path, index=False, compression="zstd")
        return str(parquet_path)
    except Exception:
        pickle_path = WORKING_DIR / f"{stem}.pkl"
        frame.to_pickle(pickle_path)
        return str(pickle_path)


def crop_for_transformer(text, max_chars=2350, head_chars=1450):
    text = str(text)
    if len(text) <= max_chars:
        return text

    tail_chars = max_chars - head_chars
    return text[:head_chars] + " [LONG_COMMENT_MIDDLE_OMITTED] " + text[-tail_chars:]


class ToxicityDataset(Dataset):
    def __init__(
        self,
        text_values,
        include_labels=False,
        target_values=None,
        subtype_values=None,
        identity_values=None,
        identity_known=None,
        sample_weights=None,
    ):
        self.text_values = np.asarray(
            [crop_for_transformer(text) for text in text_values],
            dtype=object,
        )
        self.include_labels = include_labels

        if include_labels:
            self.target_values = np.asarray(target_values, dtype=np.float32)
            self.subtype_values = np.asarray(subtype_values, dtype=np.float32)
            self.identity_values = np.asarray(identity_values, dtype=np.float32)
            self.identity_known = np.asarray(identity_known, dtype=np.float32)
            self.sample_weights = np.asarray(sample_weights, dtype=np.float32)

    def __len__(self):
        return len(self.text_values)

    def __getitem__(self, index):
        if not self.include_labels:
            return self.text_values[index]

        return (
            self.text_values[index],
            self.target_values[index],
            self.subtype_values[index],
            self.identity_values[index],
            self.identity_known[index],
            self.sample_weights[index],
        )


def train_collate(batch):
    texts, targets, subtype_targets, identity_targets, identity_known, weights = zip(
        *batch
    )

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=TOKEN_MAX_LENGTH,
        return_tensors="pt",
    )
    encoded["target_fraction"] = torch.tensor(np.asarray(targets, dtype=np.float32))
    encoded["subtype_targets"] = torch.tensor(
        np.asarray(subtype_targets, dtype=np.float32)
    )
    encoded["identity_targets"] = torch.tensor(
        np.asarray(identity_targets, dtype=np.float32)
    )
    encoded["identity_known"] = torch.tensor(
        np.asarray(identity_known, dtype=np.float32)
    )
    encoded["sample_weight"] = torch.tensor(np.asarray(weights, dtype=np.float32))

    return encoded


def inference_collate(batch):
    return tokenizer(
        list(batch),
        padding=True,
        truncation=True,
        max_length=TOKEN_MAX_LENGTH,
        return_tensors="pt",
    )


class BiasAwareModernBert(nn.Module):
    """
    Channel 0 is toxicity. Channels 1:7 are severe_toxicity, obscene, threat,
    insult, identity_attack, and sexual_explicit auxiliary logits.
    """

    def __init__(self, model_id=MODEL_ID, num_labels=NUM_OUTPUT_LABELS):
        super().__init__()
        self.backbone = ModernBertForSequenceClassification.from_pretrained(
            model_id,
            num_labels=num_labels,
            ignore_mismatched_sizes=True,
        )
        self.backbone.config.problem_type = "multi_label_classification"

    def forward(self, input_ids, attention_mask=None):
        outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        return outputs.logits


class OfficialBiasRankingLoss(nn.Module):
    """
    BCE learns the fractional toxicity and subtype annotations. Pairwise losses
    directly approximate the subgroup, BPSN, and BNSP ROC-AUC constructions.
    """

    def __init__(
        self,
        auxiliary_weight=0.22,
        fairness_weight=0.30,
        worst_group_temperature=4.0,
    ):
        super().__init__()
        self.auxiliary_weight = auxiliary_weight
        self.fairness_weight = fairness_weight
        self.worst_group_temperature = worst_group_temperature

    @staticmethod
    def _pairwise_auc_surrogate(positive_scores, negative_scores):
        if positive_scores.numel() == 0 or negative_scores.numel() == 0:
            return None

        margin = negative_scores.unsqueeze(0) - positive_scores.unsqueeze(1)
        return F.softplus(margin).mean()

    def _identity_ranking_loss(
        self,
        toxicity_logits,
        binary_targets,
        identity_values,
        identity_known,
    ):
        identity_values = torch.nan_to_num(
            identity_values,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )

        positive_target = binary_targets >= 0.5
        annotated_identity = identity_known >= 0.5
        per_identity_losses = []

        for identity_index in range(identity_values.shape[1]):
            subgroup = (identity_values[:, identity_index] >= 0.5) & annotated_identity
            background = (~subgroup) & annotated_identity

            subgroup_positive = toxicity_logits[subgroup & positive_target]
            subgroup_negative = toxicity_logits[subgroup & (~positive_target)]
            background_positive = toxicity_logits[background & positive_target]
            background_negative = toxicity_logits[background & (~positive_target)]

            metric_losses = []

            subgroup_auc_loss = self._pairwise_auc_surrogate(
                subgroup_positive,
                subgroup_negative,
            )
            if subgroup_auc_loss is not None:
                metric_losses.append(subgroup_auc_loss)

            bpsn_auc_loss = self._pairwise_auc_surrogate(
                background_positive,
                subgroup_negative,
            )
            if bpsn_auc_loss is not None:
                metric_losses.append(bpsn_auc_loss)

            bnsp_auc_loss = self._pairwise_auc_surrogate(
                subgroup_positive,
                background_negative,
            )
            if bnsp_auc_loss is not None:
                metric_losses.append(bnsp_auc_loss)

            if metric_losses:
                per_identity_losses.append(torch.stack(metric_losses).mean())

        if not per_identity_losses:
            return toxicity_logits.new_zeros(())

        per_identity_losses = torch.stack(per_identity_losses)
        focus_weights = torch.softmax(
            self.worst_group_temperature * per_identity_losses.detach(),
            dim=0,
        )

        return torch.sum(focus_weights * per_identity_losses)

    def forward(
        self,
        logits,
        target_fraction,
        subtype_targets,
        identity_values,
        identity_known,
        sample_weight=None,
    ):
        toxicity_logits = logits[:, 0]
        subtype_logits = logits[:, 1:]

        target_fraction = target_fraction.float().reshape(-1).clamp(0.0, 1.0)
        subtype_targets = subtype_targets.float().clamp(0.0, 1.0)

        toxicity_bce = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            target_fraction,
            reduction="none",
        )

        if sample_weight is not None:
            sample_weight = sample_weight.float().reshape(-1).clamp_min(0.05)
            toxicity_bce = (toxicity_bce * sample_weight).sum() / sample_weight.sum()
        else:
            toxicity_bce = toxicity_bce.mean()

        subtype_bce = F.binary_cross_entropy_with_logits(
            subtype_logits,
            subtype_targets,
            reduction="mean",
        )

        ranking_loss = self._identity_ranking_loss(
            toxicity_logits=toxicity_logits,
            binary_targets=target_fraction,
            identity_values=identity_values,
            identity_known=identity_known,
        )

        return (
            toxicity_bce
            + self.auxiliary_weight * subtype_bce
            + self.fairness_weight * ranking_loss
        )


def _layer_index(parameter_name, num_hidden_layers):
    matched = re.search(r"(?:layers|encoder\.layer)\.(\d+)\.", parameter_name)
    if matched is not None:
        return int(matched.group(1))

    if "embeddings" in parameter_name:
        return 0

    return num_hidden_layers


def build_optimizer(
    model,
    backbone_learning_rate=1.4e-5,
    classifier_learning_rate=2.4e-5,
    layerwise_decay=0.92,
    weight_decay=0.01,
):
    num_hidden_layers = int(model.backbone.config.num_hidden_layers)
    parameter_groups = {}

    for parameter_name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue

        is_head = any(
            head_name in parameter_name
            for head_name in ("classifier", "head", "pooler")
        )

        if is_head:
            learning_rate = classifier_learning_rate
        else:
            layer_number = min(
                _layer_index(parameter_name, num_hidden_layers),
                num_hidden_layers,
            )
            learning_rate = backbone_learning_rate * (
                layerwise_decay ** (num_hidden_layers - layer_number)
            )

        no_decay = (
            parameter_name.endswith(".bias")
            or "LayerNorm.weight" in parameter_name
            or "layer_norm.weight" in parameter_name
            or ".norm.weight" in parameter_name
        )

        group_key = (learning_rate, 0.0 if no_decay else weight_decay)

        if group_key not in parameter_groups:
            parameter_groups[group_key] = {
                "params": [],
                "lr": learning_rate,
                "weight_decay": group_key[1],
            }

        parameter_groups[group_key]["params"].append(parameter)

    return AdamW(
        list(parameter_groups.values()),
        betas=(0.9, 0.98),
        eps=1e-6,
    )


def official_bias_score(validation_frame, predictions, identity_columns):
    y_true = (validation_frame[TARGET_COLUMN].to_numpy(dtype=np.float32) >= 0.5).astype(
        np.int8
    )
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(np.unique(y_true)) != 2:
        raise ValueError("Validation target has fewer than two classes.")

    if not np.isfinite(predictions).all():
        raise ValueError("Non-finite validation predictions encountered.")

    overall_auc = float(roc_auc_score(y_true, predictions))
    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_column in identity_columns:
        subgroup = (
            validation_frame[identity_column].fillna(0.0).to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_auc_mask = subgroup
        bpsn_auc_mask = (subgroup & (y_true == 0)) | ((~subgroup) & (y_true == 1))
        bnsp_auc_mask = (subgroup & (y_true == 1)) | ((~subgroup) & (y_true == 0))

        def exact_auc(mask, metric_name):
            subset_y = y_true[mask]
            if len(subset_y) == 0 or len(np.unique(subset_y)) != 2:
                raise ValueError(
                    f"Undefined {metric_name} for identity '{identity_column}' "
                    "in held-out validation data."
                )
            return float(roc_auc_score(subset_y, predictions[mask]))

        subgroup_aucs.append(exact_auc(subgroup_auc_mask, "subgroup AUC"))
        bpsn_aucs.append(exact_auc(bpsn_auc_mask, "BPSN AUC"))
        bnsp_aucs.append(exact_auc(bnsp_auc_mask, "BNSP AUC"))

    def power_mean_minus_five(values):
        values = np.asarray(values, dtype=np.float64)
        return float(np.mean(np.power(values, -5.0)) ** (-1.0 / 5.0))

    subgroup_power_mean = power_mean_minus_five(subgroup_aucs)
    bpsn_power_mean = power_mean_minus_five(bpsn_aucs)
    bnsp_power_mean = power_mean_minus_five(bnsp_aucs)

    final_score = 0.25 * (
        overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean
    )

    diagnostics = {
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
    }

    return float(final_score), diagnostics


train_header = pd.read_csv(INPUT_DIR / "train.csv", nrows=0).columns.tolist()
available_identity_columns = [c for c in IDENTITY_COLUMNS if c in train_header]
available_subtype_columns = [c for c in SUBTYPE_COLUMNS if c in train_header]

required_train_columns = (
    [
        ID_COLUMN,
        TEXT_COLUMN,
        TARGET_COLUMN,
        GROUP_COLUMN,
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + available_identity_columns
    + available_subtype_columns
)

train_dtypes = {
    column: np.float32
    for column in [TARGET_COLUMN]
    + available_identity_columns
    + available_subtype_columns
}

raw_all_train = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=required_train_columns,
    dtype=train_dtypes,
    low_memory=False,
)

raw_test = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=[ID_COLUMN, TEXT_COLUMN],
    dtype={ID_COLUMN: np.int64},
    low_memory=False,
)

target_binary = (raw_all_train[TARGET_COLUMN].to_numpy(dtype=np.float32) >= 0.5).astype(
    np.int16
)

identity_matrix_for_split = (
    raw_all_train[EVALUATED_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
    >= 0.5
)

identity_count = identity_matrix_for_split.sum(axis=1).astype(np.int16)
primary_identity = np.where(
    identity_count > 0,
    identity_matrix_for_split.argmax(axis=1).astype(np.int16) + 1,
    0,
)
identity_count_band = np.minimum(identity_count, 3).astype(np.int16)

split_strata = (target_binary + 2 * primary_identity + 24 * identity_count_band).astype(
    np.int32
)

article_groups = raw_all_train[GROUP_COLUMN].to_numpy()

reference_rates = np.concatenate(
    [
        np.array([target_binary.mean()], dtype=np.float64),
        identity_matrix_for_split.mean(axis=0, dtype=np.float64),
    ]
)

try:
    splitter = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEED)
    best_balance = np.inf
    train_indices = None
    validation_indices = None

    for candidate_train_idx, candidate_valid_idx in splitter.split(
        raw_all_train,
        split_strata,
        groups=article_groups,
    ):
        candidate_rates = np.concatenate(
            [
                np.array(
                    [target_binary[candidate_valid_idx].mean()],
                    dtype=np.float64,
                ),
                identity_matrix_for_split[candidate_valid_idx].mean(
                    axis=0,
                    dtype=np.float64,
                ),
            ]
        )

        balance_error = np.mean(np.abs(candidate_rates - reference_rates))

        if balance_error < best_balance:
            best_balance = balance_error
            train_indices = candidate_train_idx
            validation_indices = candidate_valid_idx

except Exception:
    fallback_splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=VALID_FRACTION,
        random_state=SEED,
    )

    train_indices, validation_indices = next(
        fallback_splitter.split(
            raw_all_train,
            target_binary,
            groups=article_groups,
        )
    )

raw_train = raw_all_train.iloc[train_indices].copy()
raw_validation = raw_all_train.iloc[validation_indices].copy()

del raw_all_train, train_indices, validation_indices
gc.collect()

train_df, train_text_features = make_processed_frame(raw_train, include_labels=True)
validation_df, validation_text_features = make_processed_frame(
    raw_validation,
    include_labels=True,
)
test_df, test_text_features = make_processed_frame(raw_test, include_labels=False)

feature_scaler = StandardScaler()
feature_scaler.fit(train_text_features.to_numpy(dtype=np.float32))

scaled_feature_columns = [
    f"textmeta_{column}" for column in train_text_features.columns
]

for processed_frame, feature_frame in (
    (train_df, train_text_features),
    (validation_df, validation_text_features),
    (test_df, test_text_features),
):
    scaled_values = feature_scaler.transform(feature_frame.to_numpy(dtype=np.float32))
    scaled_values = np.nan_to_num(
        scaled_values,
        nan=0.0,
        posinf=0.0,
        neginf=0.0,
    ).astype(np.float32)

    processed_frame[scaled_feature_columns] = scaled_values

joblib.dump(feature_scaler, WORKING_DIR / "text_feature_scaler.joblib")

train_path = save_dataframe(train_df, "train_processed")
validation_path = save_dataframe(validation_df, "validation_processed")
test_path = save_dataframe(test_df, "test_processed")

manifest = {
    "split_method": (
        "StratifiedGroupKFold(article_id), selected for closest "
        "identity/toxicity prevalence"
    ),
    "random_seed": SEED,
    "group_column": GROUP_COLUMN,
    "text_columns": ["clean_text", "robust_text"],
    "numeric_feature_columns": scaled_feature_columns,
    "target_column": TARGET_COLUMN,
    "binary_target_column": "target_binary",
    "identity_columns": available_identity_columns,
    "evaluated_identity_columns": EVALUATED_IDENTITY_COLUMNS,
    "subtype_columns": available_subtype_columns,
    "train_path": train_path,
    "validation_path": validation_path,
    "test_path": test_path,
    "scaler_path": str(WORKING_DIR / "text_feature_scaler.joblib"),
    "n_train": int(len(train_df)),
    "n_validation": int(len(validation_df)),
    "n_test": int(len(test_df)),
}

with open(WORKING_DIR / "data_manifest.json", "w", encoding="utf-8") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

del (
    raw_train,
    raw_validation,
    raw_test,
    train_text_features,
    validation_text_features,
    test_text_features,
    identity_matrix_for_split,
)
gc.collect()

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = BiasAwareModernBert()
criterion = OfficialBiasRankingLoss()
optimizer = build_optimizer(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"
amp_scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

if use_amp:
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    if gpu_memory_gb >= 70:
        TRAIN_BATCH_SIZE = 12
    elif gpu_memory_gb >= 35:
        TRAIN_BATCH_SIZE = 8
    else:
        TRAIN_BATCH_SIZE = 4
else:
    TRAIN_BATCH_SIZE = 1

EVAL_BATCH_SIZE = max(1, TRAIN_BATCH_SIZE * 2)
GRADIENT_ACCUMULATION_STEPS = max(1, 32 // TRAIN_BATCH_SIZE)

identity_matrix_train = (
    train_df[EVALUATED_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
)

identity_known_train = train_df["identity_labels_available"].to_numpy(dtype=np.float32)

target_fraction_train = train_df[TARGET_COLUMN].to_numpy(dtype=np.float32)
target_binary_train = target_fraction_train >= 0.5

identity_any_train = (identity_matrix_train >= 0.5).any(axis=1) & (
    identity_known_train >= 0.5
)

sample_weights_train = np.ones(len(train_df), dtype=np.float32)
sample_weights_train += (1.00 * identity_any_train * (~target_binary_train)).astype(
    np.float32
)
sample_weights_train += (0.25 * identity_any_train * target_binary_train).astype(
    np.float32
)
sample_weights_train /= sample_weights_train.mean()

train_clean_text = train_df["clean_text"].to_numpy(dtype=object)
train_robust_text = train_df["robust_text"].to_numpy(dtype=object)
train_ids = train_df[ID_COLUMN].to_numpy(dtype=np.int64)

use_robust_view = (train_ids % 5) == 0
train_text_values = np.where(
    use_robust_view,
    train_robust_text,
    train_clean_text,
)

train_dataset = ToxicityDataset(
    text_values=train_text_values,
    include_labels=True,
    target_values=target_fraction_train,
    subtype_values=(
        train_df.reindex(columns=SUBTYPE_COLUMNS, fill_value=0.0)
        .fillna(0.0)
        .to_numpy(dtype=np.float32)
    ),
    identity_values=identity_matrix_train,
    identity_known=identity_known_train,
    sample_weights=sample_weights_train,
)

validation_dataset = ToxicityDataset(
    text_values=validation_df["clean_text"].to_numpy(dtype=object),
    include_labels=False,
)

test_dataset = ToxicityDataset(
    text_values=test_df["clean_text"].to_numpy(dtype=object),
    include_labels=False,
)

loader_kwargs = {
    "num_workers": NUM_WORKERS,
    "pin_memory": use_amp,
}

if NUM_WORKERS > 0:
    loader_kwargs["persistent_workers"] = True
    loader_kwargs["prefetch_factor"] = 2

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=False,
    collate_fn=train_collate,
    **loader_kwargs,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    collate_fn=inference_collate,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    collate_fn=inference_collate,
    **loader_kwargs,
)

model.to(device)

if hasattr(model.backbone, "gradient_checkpointing_enable") and use_amp:
    model.backbone.gradient_checkpointing_enable()

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_updates = max(1, updates_per_epoch * NUM_EPOCHS)
warmup_updates = max(1, int(0.06 * total_updates))

scheduler = get_cosine_schedule_with_warmup(
    optimizer,
    num_warmup_steps=warmup_updates,
    num_training_steps=total_updates,
)


@torch.no_grad()
def predict_with_model(data_loader):
    model.eval()
    all_predictions = []

    for encoded in data_loader:
        encoded = {
            key: value.to(device, non_blocking=True) for key, value in encoded.items()
        }

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(
                input_ids=encoded["input_ids"],
                attention_mask=encoded.get("attention_mask"),
            )
            probabilities = torch.sigmoid(logits[:, 0])

        all_predictions.append(probabilities.float().cpu().numpy())

    return np.concatenate(all_predictions, axis=0)


best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0

for epoch in range(NUM_EPOCHS):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    cumulative_loss = 0.0
    batches_seen = 0

    for batch_index, encoded in enumerate(train_loader):
        input_ids = encoded["input_ids"].to(device, non_blocking=True)

        attention_mask = encoded.get("attention_mask")
        if attention_mask is not None:
            attention_mask = attention_mask.to(device, non_blocking=True)

        target_fraction = encoded["target_fraction"].to(device, non_blocking=True)
        subtype_targets = encoded["subtype_targets"].to(device, non_blocking=True)
        identity_targets = encoded["identity_targets"].to(device, non_blocking=True)
        identity_known = encoded["identity_known"].to(device, non_blocking=True)
        sample_weight = encoded["sample_weight"].to(device, non_blocking=True)

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )
            loss = criterion(
                logits=logits,
                target_fraction=target_fraction,
                subtype_targets=subtype_targets,
                identity_values=identity_targets,
                identity_known=identity_known,
                sample_weight=sample_weight,
            )

        if not torch.isfinite(loss):
            raise FloatingPointError("Non-finite training loss encountered.")

        cumulative_loss += float(loss.detach().cpu())
        batches_seen += 1

        scaled_loss = loss / GRADIENT_ACCUMULATION_STEPS
        amp_scaler.scale(scaled_loss).backward()

        is_update_step = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if is_update_step:
            amp_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

    validation_predictions = predict_with_model(validation_loader)
    epoch_score, epoch_metrics = official_bias_score(
        validation_df,
        validation_predictions,
        EVALUATED_IDENTITY_COLUMNS,
    )

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"loss={cumulative_loss / max(batches_seen, 1):.5f} "
        f"official={epoch_score:.6f} "
        f"overall={epoch_metrics['overall_auc']:.6f} "
        f"subgroup={epoch_metrics['subgroup_power_mean']:.6f} "
        f"bpsn={epoch_metrics['bpsn_power_mean']:.6f} "
        f"bnsp={epoch_metrics['bnsp_power_mean']:.6f}"
    )

    if epoch_score > best_score + 1e-7:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_score": best_score,
                "model_state_dict": model.state_dict(),
            },
            BEST_MODEL_PATH,
        )
    else:
        epochs_without_improvement += 1
        if epochs_without_improvement >= PATIENCE:
            break

    gc.collect()
    if use_amp:
        torch.cuda.empty_cache()

best_checkpoint = torch.load(BEST_MODEL_PATH, map_location=device)
model.load_state_dict(best_checkpoint["model_state_dict"], strict=True)
model.to(device)

final_validation_predictions = predict_with_model(validation_loader)
score, final_metrics = official_bias_score(
    validation_df,
    final_validation_predictions,
    EVALUATED_IDENTITY_COLUMNS,
)

test_predictions = predict_with_model(test_loader)
test_predictions = np.nan_to_num(
    test_predictions,
    nan=0.5,
    posinf=1.0,
    neginf=0.0,
).clip(0.0, 1.0)

submission = pd.DataFrame(
    {
        "id": test_df[ID_COLUMN].to_numpy(copy=False),
        "prediction": test_predictions.astype(np.float64),
    }
)

submission.to_csv(SUBMISSION_DIR / "submission_98b302aede904490860454bf123fc520.csv", index=False)

del (
    train_dataset,
    validation_dataset,
    test_dataset,
    train_loader,
    validation_loader,
    test_loader,
)
gc.collect()

if use_amp:
    torch.cuda.empty_cache()

print(f"Final Validation Score: {score}")
