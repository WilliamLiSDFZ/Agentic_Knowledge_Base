import os
os.sched_setaffinity(0, {12, 13})
import os
import re
import json
import math
import random
import html
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
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
    get_cosine_schedule_with_warmup,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

RANDOM_SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

MAX_EPOCHS = 2
EARLY_STOPPING_PATIENCE = 1
MAX_SEQUENCE_LENGTH = 256
MAX_GRAD_NORM = 1.0

NUM_AUXILIARY_TARGETS = 6
NUM_OUTPUTS = 1 + NUM_AUXILIARY_TARGETS
STYLE_FEATURE_DIM = 12

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

STYLE_FEATURE_COLUMNS = [
    "log_char_count",
    "log_word_count",
    "uppercase_ratio",
    "digit_ratio",
    "punctuation_ratio",
    "log_exclamation_count",
    "log_question_count",
    "log_newline_count",
    "url_count",
    "email_count",
    "second_person_count",
    "negation_count",
]

IDENTITY_PATTERNS = {
    "male": r"\b(?:male|males|man|men|boy|boys|father|fathers|son|sons|husband|husbands|gentleman|gentlemen)\b",
    "female": r"\b(?:female|females|woman|women|girl|girls|mother|mothers|daughter|daughters|wife|wives|lady|ladies)\b",
    "homosexual_gay_or_lesbian": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbt|lgbtq|"
        r"queer|bisexual|transgender|transsexual)\b"
    ),
    "christian": r"\b(?:christian|christians|christianity|catholic|catholics|protestant|protestants)\b",
    "jewish": r"\b(?:jew|jews|jewish|judaism|rabbi|rabbis)\b",
    "muslim": r"\b(?:muslim|muslims|islam|islamic|islamist|mosque|mosques)\b",
    "black": r"\b(?:black|blacks|african[\s-]?american|african[\s-]?americans)\b",
    "white": r"\b(?:white|whites|caucasian|caucasians)\b",
    "psychiatric_or_mental_illness": (
        r"\b(?:mental(?:ly)?\s+ill|mental\s+illness|mental\s+health|psychiatric|"
        r"schizophren(?:ia|ic)|bipolar|depress(?:ion|ed)|autis(?:m|tic)|crazy|insane)\b"
    ),
}

URL_PATTERN = re.compile(r"(?:(?:https?|ftp)://|www\.)\S+", flags=re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", flags=re.IGNORECASE)
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
WHITESPACE_PATTERN = re.compile(r"\s+")

IDENTITY_REPLACEMENT_PATTERN = re.compile(
    "|".join(f"(?:{pattern})" for pattern in IDENTITY_PATTERNS.values()),
    flags=re.IGNORECASE,
)

MODEL_INPUT_COLUMNS = {
    "original_text": "comment_text",
    "masked_text": "identity_masked_text",
    "style_features": STYLE_FEATURE_COLUMNS,
    "lexical_identity_indicator": "lexical_identity_any",
}

MODEL_TARGET_COLUMNS = {
    "target": "target",
    "auxiliary": AUXILIARY_TARGET_COLUMNS,
}

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True


def locate_file(filename: str) -> Path:
    direct_path = INPUT_DIR / filename
    if direct_path.exists():
        return direct_path

    matches = list(INPUT_DIR.rglob(filename))
    if len(matches) != 1:
        raise FileNotFoundError(
            f"Could not uniquely locate {filename} under {INPUT_DIR}"
        )
    return matches[0]


def normalize_comment(value) -> str:
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text).replace("\x00", " ")
    text = URL_PATTERN.sub(" <URL> ", text)
    text = EMAIL_PATTERN.sub(" <EMAIL> ", text)
    text = IP_PATTERN.sub(" <IP> ", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text


def normalize_series(text_series: pd.Series) -> pd.Series:
    return text_series.map(normalize_comment).astype("string").reset_index(drop=True)


def compute_style_matrix(clean_text: pd.Series) -> np.ndarray:
    text = clean_text.fillna("").astype("string")

    char_count = text.str.len().to_numpy(dtype=np.float32)
    word_count = text.str.count(r"\S+").to_numpy(dtype=np.float32)
    alphabetic_count = text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    uppercase_count = text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = text.str.count(r"\d").to_numpy(dtype=np.float32)
    punctuation_count = text.str.count(r"[^\w\s]").to_numpy(dtype=np.float32)
    exclamation_count = text.str.count("!").to_numpy(dtype=np.float32)
    question_count = text.str.count(r"\?").to_numpy(dtype=np.float32)
    newline_count = text.str.count(r"[\r\n]").to_numpy(dtype=np.float32)
    url_count = text.str.count(r"<URL>").to_numpy(dtype=np.float32)
    email_count = text.str.count(r"<EMAIL>").to_numpy(dtype=np.float32)
    second_person_count = text.str.count(
        r"\b(?:you|your|yours|yourself|yourselves|u)\b",
        flags=re.IGNORECASE,
    ).to_numpy(dtype=np.float32)
    negation_count = text.str.count(
        r"\b(?:no|not|never|none|nothing|neither|cannot|can't|won't|isn't|aren't|don't|doesn't|didn't)\b",
        flags=re.IGNORECASE,
    ).to_numpy(dtype=np.float32)

    safe_char_count = np.maximum(char_count, 1.0)
    safe_alpha_count = np.maximum(alphabetic_count, 1.0)

    return np.column_stack(
        [
            np.log1p(char_count),
            np.log1p(word_count),
            uppercase_count / safe_alpha_count,
            digit_count / safe_char_count,
            punctuation_count / safe_char_count,
            np.log1p(exclamation_count),
            np.log1p(question_count),
            np.log1p(newline_count),
            url_count,
            email_count,
            second_person_count,
            negation_count,
        ]
    ).astype(np.float32)


def add_text_and_test_time_features(
    frame: pd.DataFrame,
    scaler: StandardScaler,
    include_labels: bool,
) -> pd.DataFrame:
    clean_text = normalize_series(frame["comment_text"])
    style_matrix = compute_style_matrix(clean_text)
    scaled_style_matrix = scaler.transform(style_matrix).astype(np.float32)

    output = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(),
            "comment_text": clean_text.to_numpy(),
        }
    )

    for column_index, column_name in enumerate(STYLE_FEATURE_COLUMNS):
        output[column_name] = scaled_style_matrix[:, column_index]

    lower_text = clean_text.str.lower()
    identity_tag_prefix = pd.Series(
        "",
        index=clean_text.index,
        dtype="string",
    )

    for identity_name, pattern in IDENTITY_PATTERNS.items():
        flag_column = f"lexical_identity_{identity_name}"
        has_identity = lower_text.str.contains(
            pattern,
            regex=True,
            na=False,
        ).astype(np.float32)

        output[flag_column] = has_identity.to_numpy(dtype=np.float32)

        addition = pd.Series(
            np.where(
                has_identity.to_numpy(dtype=bool),
                f" identitymention_{identity_name} ",
                "",
            ),
            index=clean_text.index,
            dtype="string",
        )
        identity_tag_prefix = identity_tag_prefix + addition

    lexical_identity_columns = [
        f"lexical_identity_{name}" for name in IDENTITY_PATTERNS
    ]

    output["lexical_identity_any"] = (
        output[lexical_identity_columns].max(axis=1).astype(np.float32)
    )

    output["identity_tagged_text"] = (
        (identity_tag_prefix.str.strip() + " " + clean_text).str.strip().to_numpy()
    )

    output["identity_masked_text"] = (
        clean_text.str.replace(
            IDENTITY_REPLACEMENT_PATTERN,
            " <IDENTITY> ",
            regex=True,
        )
        .str.replace(WHITESPACE_PATTERN, " ", regex=True)
        .str.strip()
        .to_numpy()
    )

    if include_labels:
        output["target"] = frame["target"].to_numpy(dtype=np.float32)
        output["target_binary"] = (
            frame["target"].to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.int8)

        for column_name in AUXILIARY_TARGET_COLUMNS:
            output[column_name] = frame[column_name].to_numpy(dtype=np.float32)

        output["identity_annotation_available"] = (
            frame[IDENTITY_COLUMNS].notna().any(axis=1).to_numpy(dtype=np.int8)
        )

        for column_name in IDENTITY_COLUMNS:
            output[column_name] = frame[column_name].to_numpy(dtype=np.float32)

    return output


def save_dataframe(frame: pd.DataFrame, stem: str) -> str:
    parquet_path = WORKING_DIR / f"{stem}.parquet"
    try:
        frame.to_parquet(parquet_path, index=False, compression="zstd")
        return str(parquet_path)
    except (ImportError, ModuleNotFoundError, ValueError):
        pickle_path = WORKING_DIR / f"{stem}.pkl"
        frame.to_pickle(pickle_path, protocol=4)
        return str(pickle_path)


def official_competition_metric(
    validation_frame: pd.DataFrame,
    predictions: np.ndarray,
) -> dict:
    labels = validation_frame["target"].to_numpy(dtype=np.float32)
    binary_labels = (labels >= 0.5).astype(np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(binary_labels) != len(predictions):
        raise ValueError("Prediction count does not match validation label count")

    if np.unique(binary_labels).size != 2:
        raise ValueError("Validation partition must contain both toxicity classes")

    overall_auc = float(roc_auc_score(binary_labels, predictions))
    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_column in EVALUATION_IDENTITY_COLUMNS:
        subgroup_membership = (
            np.nan_to_num(
                validation_frame[identity_column].to_numpy(dtype=np.float32),
                nan=0.0,
            )
            >= 0.5
        )

        subgroup_mask = subgroup_membership
        bpsn_mask = (subgroup_membership & (binary_labels == 0)) | (
            (~subgroup_membership) & (binary_labels == 1)
        )
        bnsp_mask = (subgroup_membership & (binary_labels == 1)) | (
            (~subgroup_membership) & (binary_labels == 0)
        )

        for metric_name, subset_mask, destination in (
            ("subgroup", subgroup_mask, subgroup_aucs),
            ("bpsn", bpsn_mask, bpsn_aucs),
            ("bnsp", bnsp_mask, bnsp_aucs),
        ):
            subset_labels = binary_labels[subset_mask]

            if subset_labels.size == 0 or np.unique(subset_labels).size != 2:
                raise ValueError(
                    f"Official {metric_name} AUC cannot be computed for "
                    f"identity '{identity_column}' on this validation split"
                )

            destination.append(
                float(roc_auc_score(subset_labels, predictions[subset_mask]))
            )

    def generalized_mean(values, power=-5.0):
        values = np.clip(np.asarray(values, dtype=np.float64), 1e-15, 1.0)
        return float(np.mean(np.power(values, power)) ** (1.0 / power))

    subgroup_generalized_mean = generalized_mean(subgroup_aucs)
    bpsn_generalized_mean = generalized_mean(bpsn_aucs)
    bnsp_generalized_mean = generalized_mean(bnsp_aucs)

    final_score = 0.25 * (
        overall_auc
        + subgroup_generalized_mean
        + bpsn_generalized_mean
        + bnsp_generalized_mean
    )

    return {
        "final_score": float(final_score),
        "overall_auc": overall_auc,
        "subgroup_generalized_mean": subgroup_generalized_mean,
        "bpsn_generalized_mean": bpsn_generalized_mean,
        "bnsp_generalized_mean": bnsp_generalized_mean,
        "subgroup_auc_by_identity": dict(
            zip(EVALUATION_IDENTITY_COLUMNS, subgroup_aucs)
        ),
        "bpsn_auc_by_identity": dict(zip(EVALUATION_IDENTITY_COLUMNS, bpsn_aucs)),
        "bnsp_auc_by_identity": dict(zip(EVALUATION_IDENTITY_COLUMNS, bnsp_aucs)),
    }


class FairModernBertToxicityModel(nn.Module):
    def __init__(
        self,
        pretrained_sequence_classifier: ModernBertForSequenceClassification,
        style_feature_dim: int,
        num_outputs: int,
        masked_view_weight: float = 0.60,
        dropout_probability: float = 0.15,
    ):
        super().__init__()

        self.encoder = pretrained_sequence_classifier.model
        hidden_size = pretrained_sequence_classifier.config.hidden_size
        self.masked_view_weight = float(masked_view_weight)

        self.style_projection = nn.Sequential(
            nn.LayerNorm(style_feature_dim),
            nn.Linear(style_feature_dim, hidden_size // 4),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_size + hidden_size // 4),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size + hidden_size // 4, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size // 2, num_outputs),
        )

    def _encode_and_classify(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        style_features: torch.Tensor,
    ) -> torch.Tensor:
        encoder_output = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        cls_embedding = encoder_output.last_hidden_state[:, 0]
        style_embedding = self.style_projection(style_features.float())

        return self.classifier(torch.cat([cls_embedding, style_embedding], dim=-1))

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        masked_input_ids: torch.Tensor,
        masked_attention_mask: torch.Tensor,
        style_features: torch.Tensor,
        lexical_identity_any: torch.Tensor,
    ) -> dict:
        raw_logits = self._encode_and_classify(
            input_ids=input_ids,
            attention_mask=attention_mask,
            style_features=style_features,
        )

        # The OOM occurs because the full masked batch is encoded while the
        # original-view activations are still retained for backpropagation.
        # Only identity-containing rows use the masked view in either logits or loss.
        identity_rows = lexical_identity_any.float().view(-1).gt(0.5)
        if identity_rows.any():
            masked_logits = raw_logits.clone()
            masked_logits[identity_rows] = self._encode_and_classify(
                input_ids=masked_input_ids[identity_rows],
                attention_mask=masked_attention_mask[identity_rows],
                style_features=style_features[identity_rows],
            )
        else:
            masked_logits = raw_logits

        identity_gate = lexical_identity_any.float().view(-1, 1).clamp(0.0, 1.0)
        masked_weight = identity_gate * self.masked_view_weight
        logits = raw_logits * (1.0 - masked_weight) + masked_logits * masked_weight

        return {
            "logits": logits,
            "raw_logits": raw_logits,
            "masked_logits": masked_logits,
        }


class BiasAwareMultiTaskLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight: float = 0.25,
        clean_identity_weight: float = 4.0,
        toxic_identity_weight: float = 1.5,
        counterfactual_weight: float = 0.40,
    ):
        super().__init__()
        self.auxiliary_weight = float(auxiliary_weight)
        self.clean_identity_weight = float(clean_identity_weight)
        self.toxic_identity_weight = float(toxic_identity_weight)
        self.counterfactual_weight = float(counterfactual_weight)

    def forward(
        self,
        model_output: dict,
        target: torch.Tensor,
        auxiliary_targets: torch.Tensor,
        identity_labels: torch.Tensor,
        lexical_identity_any: torch.Tensor,
    ) -> torch.Tensor:
        logits = model_output["logits"]
        target_logits = logits[:, 0]
        target = target.float().view(-1).clamp(0.0, 1.0)

        mentioned_identity = (
            torch.nan_to_num(
                identity_labels.float(),
                nan=0.0,
            )
            .ge(0.5)
            .any(dim=1)
        )

        clean_identity = mentioned_identity & target.lt(0.5)
        toxic_identity = mentioned_identity & target.ge(0.5)

        sample_weight = torch.ones_like(target)
        sample_weight = (
            sample_weight + clean_identity.float() * self.clean_identity_weight
        )
        sample_weight = (
            sample_weight + toxic_identity.float() * self.toxic_identity_weight
        )

        target_loss_per_example = F.binary_cross_entropy_with_logits(
            target_logits,
            target,
            reduction="none",
        )

        target_loss = (
            target_loss_per_example * sample_weight
        ).sum() / sample_weight.sum().clamp_min(1.0)

        auxiliary_targets = auxiliary_targets.float()
        valid_auxiliary = torch.isfinite(auxiliary_targets)
        safe_auxiliary_targets = torch.nan_to_num(
            auxiliary_targets,
            nan=0.0,
        ).clamp(0.0, 1.0)

        auxiliary_loss_per_value = F.binary_cross_entropy_with_logits(
            logits[:, 1:],
            safe_auxiliary_targets,
            reduction="none",
        )

        auxiliary_loss = (
            auxiliary_loss_per_value * valid_auxiliary.float()
        ).sum() / valid_auxiliary.float().sum().clamp_min(1.0)

        lexical_identity_mask = lexical_identity_any.float().view(-1).gt(0.5)
        clean_counterfactual_mask = lexical_identity_mask & target.lt(0.5)

        raw_probability = torch.sigmoid(model_output["raw_logits"][:, 0])
        masked_probability = torch.sigmoid(model_output["masked_logits"][:, 0])
        counterfactual_distance = (raw_probability - masked_probability).pow(2)

        if clean_counterfactual_mask.any():
            counterfactual_loss = counterfactual_distance[
                clean_counterfactual_mask
            ].mean()
        else:
            counterfactual_loss = target_logits.new_zeros(())

        return (
            target_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.counterfactual_weight * counterfactual_loss
        )


class ToxicityFeatureDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, has_labels: bool):
        self.has_labels = bool(has_labels)

        self.original_text = (
            frame[MODEL_INPUT_COLUMNS["original_text"]]
            .fillna("")
            .astype(str)
            .to_numpy()
        )

        self.masked_text = (
            frame[MODEL_INPUT_COLUMNS["masked_text"]].fillna("").astype(str).to_numpy()
        )

        self.style_features = frame[MODEL_INPUT_COLUMNS["style_features"]].to_numpy(
            dtype=np.float32, copy=True
        )

        self.lexical_identity = frame[
            MODEL_INPUT_COLUMNS["lexical_identity_indicator"]
        ].to_numpy(dtype=np.float32, copy=True)

        if self.has_labels:
            self.target = frame[MODEL_TARGET_COLUMNS["target"]].to_numpy(
                dtype=np.float32,
                copy=True,
            )

            self.auxiliary_targets = frame[MODEL_TARGET_COLUMNS["auxiliary"]].to_numpy(
                dtype=np.float32, copy=True
            )

            self.identity_labels = frame[IDENTITY_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.original_text)

    def __getitem__(self, index: int):
        if self.has_labels:
            return (
                self.original_text[index],
                self.masked_text[index],
                self.style_features[index],
                self.target[index],
                self.auxiliary_targets[index],
                self.identity_labels[index],
                self.lexical_identity[index],
            )

        return (
            self.original_text[index],
            self.masked_text[index],
            self.style_features[index],
            self.lexical_identity[index],
        )


def toxicity_collate(samples):
    original_texts = [sample[0] for sample in samples]
    masked_texts = [sample[1] for sample in samples]

    original_tokens = tokenizer(
        original_texts,
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    masked_tokens = tokenizer(
        masked_texts,
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    batch = {
        "input_ids": original_tokens["input_ids"],
        "attention_mask": original_tokens["attention_mask"],
        "masked_input_ids": masked_tokens["input_ids"],
        "masked_attention_mask": masked_tokens["attention_mask"],
        "style_features": torch.as_tensor(
            np.stack([sample[2] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        ),
    }

    if len(samples[0]) == 7:
        batch["target"] = torch.as_tensor(
            np.asarray([sample[3] for sample in samples], dtype=np.float32)
        )

        batch["auxiliary_targets"] = torch.as_tensor(
            np.stack([sample[4] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        )

        batch["identity_labels"] = torch.as_tensor(
            np.stack([sample[5] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        )

        batch["lexical_identity_any"] = torch.as_tensor(
            np.asarray([sample[6] for sample in samples], dtype=np.float32)
        )
    else:
        batch["lexical_identity_any"] = torch.as_tensor(
            np.asarray([sample[3] for sample in samples], dtype=np.float32)
        )

    return batch


train_path = locate_file("train.csv")
test_path = locate_file("test.csv")
sample_submission_path = locate_file("sample_submission.csv")

sample_submission = pd.read_csv(sample_submission_path)
if list(sample_submission.columns) != ["id", "prediction"]:
    raise ValueError("sample_submission.csv must contain exactly: id, prediction")

train_columns = (
    ["id", "comment_text", "target"] + AUXILIARY_TARGET_COLUMNS + IDENTITY_COLUMNS
)

train = pd.read_csv(
    train_path,
    usecols=train_columns,
    low_memory=False,
)

test = pd.read_csv(
    test_path,
    usecols=["id", "comment_text"],
    low_memory=False,
)

if train["id"].duplicated().any() or test["id"].duplicated().any():
    raise ValueError("IDs must be unique within each dataset")

if train["target"].isna().any():
    raise ValueError("Training target contains missing values")

if not np.array_equal(
    test["id"].to_numpy(),
    sample_submission["id"].to_numpy(),
):
    raise ValueError("test.csv row order does not match sample_submission.csv")

target_binary = (train["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)

identity_presence = (
    train[IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
)

identity_prevalence = identity_presence.mean(axis=0)
rarity_weight = 1.0 / np.maximum(identity_prevalence, 1e-6)

primary_identity_index = (identity_presence * rarity_weight).argmax(axis=1) + 1

primary_identity_index[~identity_presence.any(axis=1)] = 0

split_strata = (
    pd.Series(target_binary.astype(str), index=train.index)
    + "_"
    + pd.Series(primary_identity_index.astype(str), index=train.index)
)

stratum_counts = split_strata.value_counts()
rare_strata = stratum_counts[stratum_counts < 10].index

split_strata = split_strata.where(
    ~split_strata.isin(rare_strata),
    "rare_" + pd.Series(target_binary.astype(str), index=train.index),
)

raw_comment_for_groups = train["comment_text"].fillna("").astype(str)
comment_groups = pd.util.hash_pandas_object(
    raw_comment_for_groups,
    index=False,
).to_numpy(dtype=np.uint64)

splitter = StratifiedGroupKFold(
    n_splits=10,
    shuffle=True,
    random_state=RANDOM_SEED,
)

train_indices, validation_indices = next(
    splitter.split(
        X=np.zeros(len(train), dtype=np.int8),
        y=split_strata.to_numpy(),
        groups=comment_groups,
    )
)

train_partition = train.iloc[train_indices].copy()
validation_partition = train.iloc[validation_indices].copy()

train_group_set = set(comment_groups[train_indices].tolist())
validation_group_set = set(comment_groups[validation_indices].tolist())

if train_group_set.intersection(validation_group_set):
    raise RuntimeError("Exact duplicate comments crossed the train/validation boundary")

del raw_comment_for_groups
del comment_groups
del train

train_clean_text = normalize_series(train_partition["comment_text"])
train_style_matrix = compute_style_matrix(train_clean_text)

style_scaler = StandardScaler()
style_scaler.fit(train_style_matrix)

train_features = add_text_and_test_time_features(
    frame=train_partition,
    scaler=style_scaler,
    include_labels=True,
)
train_features["split"] = "train"

validation_features = add_text_and_test_time_features(
    frame=validation_partition,
    scaler=style_scaler,
    include_labels=True,
)
validation_features["split"] = "validation"

test_features = add_text_and_test_time_features(
    frame=test,
    scaler=style_scaler,
    include_labels=False,
)
test_features["split"] = "test"

train_output_path = save_dataframe(train_features, "train_features")
validation_output_path = save_dataframe(validation_features, "validation_features")
test_output_path = save_dataframe(test_features, "test_features")

np.savez_compressed(
    WORKING_DIR / "style_scaler.npz",
    mean=style_scaler.mean_.astype(np.float32),
    scale=style_scaler.scale_.astype(np.float32),
    feature_names=np.asarray(STYLE_FEATURE_COLUMNS),
)

manifest = {
    "train_features_path": train_output_path,
    "validation_features_path": validation_output_path,
    "test_features_path": test_output_path,
    "text_columns": [
        "comment_text",
        "identity_tagged_text",
        "identity_masked_text",
    ],
    "style_feature_columns": STYLE_FEATURE_COLUMNS,
    "identity_lexical_feature_columns": [
        f"lexical_identity_{name}" for name in IDENTITY_PATTERNS
    ]
    + ["lexical_identity_any"],
    "identity_label_columns": IDENTITY_COLUMNS,
    "evaluation_identity_columns": EVALUATION_IDENTITY_COLUMNS,
    "auxiliary_target_columns": AUXILIARY_TARGET_COLUMNS,
    "target_column": "target",
    "binary_target_column": "target_binary",
    "split_strategy": (
        "10-fold StratifiedGroupKFold with exact raw-comment hashing as "
        "groups; the first fold is validation, and strata combine binary "
        "toxicity with the rarest mentioned identity."
    ),
    "validation_metric_for_downstream_training": (
        "Official competition score: 0.25 * overall ROC-AUC + 0.25 each for "
        "the p=-5 generalized means of subgroup, BPSN, and BNSP ROC-AUCs."
    ),
    "n_train": int(len(train_features)),
    "n_validation": int(len(validation_features)),
    "n_test": int(len(test_features)),
}

with open(
    WORKING_DIR / "feature_manifest.json",
    "w",
    encoding="utf-8",
) as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

# ModernBERT-base preserves the pretrained Transformer approach while leaving
# enough memory for optimizer state and the bias-aware dual-view training loss.
model_id = "answerdotai/ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

model = FairModernBertToxicityModel(
    pretrained_sequence_classifier=model,
    style_feature_dim=STYLE_FEATURE_DIM,
    num_outputs=NUM_OUTPUTS,
    masked_view_weight=0.60,
    dropout_probability=0.15,
)

criterion = BiasAwareMultiTaskLoss(
    auxiliary_weight=0.25,
    clean_identity_weight=4.0,
    toxic_identity_weight=1.5,
    counterfactual_weight=0.40,
)

no_decay_terms = (
    "bias",
    "LayerNorm.weight",
    "layer_norm.weight",
    "norm.weight",
)

optimizer_parameter_groups = [
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and name.startswith("encoder.")
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": 2.0e-5,
        "weight_decay": 0.01,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and name.startswith("encoder.")
            and any(term in name for term in no_decay_terms)
        ],
        "lr": 2.0e-5,
        "weight_decay": 0.0,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and not name.startswith("encoder.")
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": 1.0e-4,
        "weight_decay": 0.01,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if parameter.requires_grad
            and not name.startswith("encoder.")
            and any(term in name for term in no_decay_terms)
        ],
        "lr": 1.0e-4,
        "weight_decay": 0.0,
    },
]

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
AMP_ENABLED = torch.cuda.is_available()
use_amp = bool(AMP_ENABLED and device.type == "cuda")

if device.type == "cuda":
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    if gpu_memory_gb >= 70:
        train_batch_size = 24
        gradient_accumulation_steps = 2
    elif gpu_memory_gb >= 38:
        train_batch_size = 12
        gradient_accumulation_steps = 4
    elif gpu_memory_gb >= 22:
        train_batch_size = 8
        gradient_accumulation_steps = 4
    else:
        train_batch_size = 4
        gradient_accumulation_steps = 8
else:
    train_batch_size = 2
    gradient_accumulation_steps = 8

inference_batch_size = max(1, train_batch_size)
# The execution environment recommends at most two loader workers; using more
# can slow training or freeze workers without improving GPU utilization.
num_workers = 2
pin_memory = device.type == "cuda"


def move_model_inputs_to_device(batch: dict) -> dict:
    return {
        "input_ids": batch["input_ids"].to(device, non_blocking=True),
        "attention_mask": batch["attention_mask"].to(
            device,
            non_blocking=True,
        ),
        "masked_input_ids": batch["masked_input_ids"].to(
            device,
            non_blocking=True,
        ),
        "masked_attention_mask": batch["masked_attention_mask"].to(
            device,
            non_blocking=True,
        ),
        "style_features": batch["style_features"].to(
            device,
            non_blocking=True,
        ),
        "lexical_identity_any": batch["lexical_identity_any"].to(
            device,
            non_blocking=True,
        ),
    }


@torch.no_grad()
def predict_with_model(data_loader: DataLoader) -> np.ndarray:
    model.eval()
    prediction_chunks = []

    for batch in data_loader:
        model_inputs = move_model_inputs_to_device(batch)

        with torch.cuda.amp.autocast(enabled=use_amp):
            output = model(**model_inputs)
            probabilities = torch.sigmoid(output["logits"][:, 0])

        prediction_chunks.append(
            probabilities.float()
            .cpu()
            .numpy()
            .astype(
                np.float32,
                copy=False,
            )
        )

    if not prediction_chunks:
        raise RuntimeError("Inference loader produced no prediction batches")

    return np.clip(
        np.concatenate(prediction_chunks, axis=0),
        1e-6,
        1.0 - 1e-6,
    )


train_dataset = ToxicityFeatureDataset(train_features, has_labels=True)
validation_dataset = ToxicityFeatureDataset(
    validation_features,
    has_labels=True,
)

data_loader_kwargs = {
    "num_workers": num_workers,
    "pin_memory": pin_memory,
    "persistent_workers": num_workers > 0,
    "prefetch_factor": 2,
    "collate_fn": toxicity_collate,
}

train_generator = torch.Generator()
train_generator.manual_seed(RANDOM_SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=train_batch_size,
    shuffle=True,
    generator=train_generator,
    drop_last=False,
    **data_loader_kwargs,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=inference_batch_size,
    shuffle=False,
    drop_last=False,
    **data_loader_kwargs,
)

optimizer_steps_per_epoch = math.ceil(len(train_loader) / gradient_accumulation_steps)
total_optimizer_steps = max(1, optimizer_steps_per_epoch * MAX_EPOCHS)
warmup_steps = int(0.06 * total_optimizer_steps)

scheduler = get_cosine_schedule_with_warmup(
    optimizer=optimizer,
    num_warmup_steps=warmup_steps,
    num_training_steps=total_optimizer_steps,
)

model.to(device)
criterion.to(device)

scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

checkpoint_path = WORKING_DIR / "best_fair_modernbert_toxicity.pt"
history_path = WORKING_DIR / "training_history.json"

best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0
training_history = []

optimizer.zero_grad(set_to_none=True)

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    epoch_loss_total = torch.zeros((), device=device)
    epoch_batch_count = 0

    for batch_index, batch in enumerate(train_loader, start=1):
        model_inputs = move_model_inputs_to_device(batch)

        target = batch["target"].to(device, non_blocking=True)
        auxiliary_targets = batch["auxiliary_targets"].to(
            device,
            non_blocking=True,
        )
        identity_labels = batch["identity_labels"].to(
            device,
            non_blocking=True,
        )

        with torch.cuda.amp.autocast(enabled=use_amp):
            model_output = model(**model_inputs)

            loss = criterion(
                model_output=model_output,
                target=target,
                auxiliary_targets=auxiliary_targets,
                identity_labels=identity_labels,
                lexical_identity_any=model_inputs["lexical_identity_any"],
            )

        if torch.isfinite(loss):
            scaler.scale(loss / gradient_accumulation_steps).backward()

            epoch_loss_total += loss.detach()
            epoch_batch_count += 1

            should_step = (
                batch_index % gradient_accumulation_steps == 0
                or batch_index == len(train_loader)
            )

            if should_step:
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(
                    model.parameters(),
                    MAX_GRAD_NORM,
                )
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad(set_to_none=True)
                scheduler.step()
        else:
            optimizer.zero_grad(set_to_none=True)

    validation_predictions = predict_with_model(validation_loader)

    validation_metrics = official_competition_metric(
        validation_features,
        validation_predictions,
    )

    validation_score = validation_metrics["final_score"]

    mean_training_loss = float(
        (epoch_loss_total / max(epoch_batch_count, 1)).detach().cpu().item()
    )

    epoch_record = {
        "epoch": epoch,
        "train_loss": mean_training_loss,
        **validation_metrics,
    }

    training_history.append(epoch_record)

    if validation_score > best_score:
        best_score = float(validation_score)
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "validation_metrics": validation_metrics,
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
            },
            checkpoint_path,
        )

        np.save(
            WORKING_DIR / "best_validation_predictions.npy",
            validation_predictions.astype(np.float32, copy=False),
        )
    else:
        epochs_without_improvement += 1

    with open(history_path, "w", encoding="utf-8") as history_file:
        json.dump(
            {
                "selection_metric": (
                    "official score = 0.25 * (overall_auc + "
                    "p=-5 subgroup mean + p=-5 BPSN mean + p=-5 BNSP mean)"
                ),
                "best_epoch": best_epoch,
                "best_score": best_score,
                "history": training_history,
            },
            history_file,
            indent=2,
        )

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} "
        f"loss={mean_training_loss:.6f} "
        f"official_score={validation_score:.6f} "
        f"overall_auc={validation_metrics['overall_auc']:.6f} "
        f"bpsn={validation_metrics['bpsn_generalized_mean']:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if not checkpoint_path.exists():
    raise RuntimeError("No valid model checkpoint was produced during training")

best_checkpoint = torch.load(checkpoint_path, map_location=device)

model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(device)
model.eval()

final_validation_predictions = predict_with_model(validation_loader)

final_validation_metrics = official_competition_metric(
    validation_features,
    final_validation_predictions,
)

score = float(final_validation_metrics["final_score"])

test_dataset = ToxicityFeatureDataset(test_features, has_labels=False)

test_loader = DataLoader(
    test_dataset,
    batch_size=inference_batch_size,
    shuffle=False,
    drop_last=False,
    **data_loader_kwargs,
)

test_predictions = predict_with_model(test_loader)

if len(test_predictions) != len(test_features):
    raise RuntimeError("Test prediction count does not match test feature count")

submission = pd.DataFrame(
    {
        "id": test_features["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64, copy=False),
    }
)

if submission["id"].duplicated().any():
    raise RuntimeError("Submission contains duplicate IDs")

if not np.array_equal(
    submission["id"].to_numpy(),
    sample_submission["id"].to_numpy(),
):
    raise RuntimeError("Submission row order does not match sample_submission.csv")

submission.to_csv(SUBMISSION_DIR / "submission_e147e143e9924e18ae326501cb721f4d.csv", index=False)

with open(
    WORKING_DIR / "final_validation_metrics.json",
    "w",
    encoding="utf-8",
) as metric_file:
    json.dump(
        {
            "selected_epoch": int(best_checkpoint["epoch"]),
            "official_validation_metrics": final_validation_metrics,
        },
        metric_file,
        indent=2,
    )

print(f"Final Validation Score: {score}")
