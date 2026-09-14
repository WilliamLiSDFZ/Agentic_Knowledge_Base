import gc
import json
import math
import os
import random
import time
from contextlib import nullcontext
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
from torch.nn.utils import clip_grad_norm_
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

SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

TOXICITY_SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

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

ANNOTATION_COUNT_COLUMNS = [
    "toxicity_annotator_count",
    "identity_annotator_count",
]

TRAIN_COLUMNS = (
    ["id", "target", "comment_text"]
    + TOXICITY_SUBTYPE_COLUMNS
    + ALL_IDENTITY_COLUMNS
    + ANNOTATION_COUNT_COLUMNS
)
TEST_COLUMNS = ["id", "comment_text"]

FLOAT_COLUMNS = (
    ["target"]
    + TOXICITY_SUBTYPE_COLUMNS
    + ALL_IDENTITY_COLUMNS
    + ANNOTATION_COUNT_COLUMNS
)
TRAIN_DTYPES = {column: "float32" for column in FLOAT_COLUMNS}

TEXT_FEATURE_NAMES = [
    "log1p_char_count",
    "log1p_word_count",
    "average_alpha_chars_per_word",
    "uppercase_alpha_ratio",
    "digit_ratio",
    "non_ascii_ratio",
    "punctuation_ratio",
    "log1p_exclamation_count",
    "log1p_question_count",
    "log1p_linebreak_count",
    "log1p_url_count",
    "log1p_email_count",
    "log1p_user_mention_count",
    "log1p_repeated_punctuation_count",
    "all_caps_word_ratio",
    "second_person_word_ratio",
]

URL_PATTERN = r"(?i)\b(?:https?://|www\.)[^\s<]+"
EMAIL_PATTERN = r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b"
USER_PATTERN = r"(?<![\w@])@[A-Za-z0-9_]{1,50}\b"
ZERO_WIDTH_PATTERN = r"[\u200b-\u200f\u202a-\u202e\u2060\ufeff]"
CONTROL_PATTERN = r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]"
WHITESPACE_PATTERN = r"\s+"

TEXT_PROCESSING_CONFIG = {
    "unicode_normalization": "NFKC",
    "preserve_case": True,
    "url_replacement": " HTTPURL ",
    "email_replacement": " EMAILTOKEN ",
    "user_mention_replacement": " USERTOKEN ",
    "collapse_whitespace": True,
}


# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

torch.set_float32_matmul_precision("high")


# ---------------------------------------------------------------------------
# Runtime-owned split: must happen before fitting any transformations
# ---------------------------------------------------------------------------
session = CandidateSession.from_env()

train_df_raw = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=TRAIN_COLUMNS,
    dtype=TRAIN_DTYPES,
    low_memory=False,
)
test_df_raw = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=TEST_COLUMNS,
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_df_raw, test_df_raw)

del train_df_raw, test_df_raw
gc.collect()

train_df = train_df.reset_index(drop=True)
valid_df = valid_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

sample_submission = pd.read_csv(
    INPUT_DIR / "sample_submission.csv",
    usecols=["id"],
)

if len(sample_submission) != len(test_df):
    raise ValueError(
        "Runtime test partition does not match sample_submission row count."
    )

if not np.array_equal(
    sample_submission["id"].astype(str).to_numpy(),
    test_df["id"].astype(str).to_numpy(),
):
    raise ValueError("Runtime test row order does not match sample_submission.")

del sample_submission
gc.collect()


# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------
for frame in (train_df, valid_df):
    frame["target"] = pd.to_numeric(
        frame["target"],
        errors="coerce",
    ).clip(0.0, 1.0)

    if frame["target"].isna().any():
        raise ValueError("Missing target values were found after the official split.")

    for column in TOXICITY_SUBTYPE_COLUMNS + ALL_IDENTITY_COLUMNS:
        frame[column] = pd.to_numeric(
            frame[column],
            errors="coerce",
        ).clip(0.0, 1.0)

    for column in ANNOTATION_COUNT_COLUMNS:
        frame[column] = (
            pd.to_numeric(frame[column], errors="coerce")
            .fillna(0.0)
            .clip(lower=0.0)
            .astype(np.float32)
        )

    frame["target_soft"] = frame["target"].astype(np.float32)
    frame["target_hard"] = (frame["target"] >= 0.5).astype(np.uint8)


# ---------------------------------------------------------------------------
# Split-safe text normalization and identity-neutral numeric features
# ---------------------------------------------------------------------------
def _as_float32(series):
    return series.fillna(0).to_numpy(dtype=np.float32, copy=False)


def normalize_and_extract_text_features(frame, chunk_size=100_000):
    row_count = len(frame)
    normalized_text = np.empty(row_count, dtype=object)
    features = np.empty(
        (row_count, len(TEXT_FEATURE_NAMES)),
        dtype=np.float32,
    )

    for start in range(0, row_count, chunk_size):
        end = min(start + chunk_size, row_count)

        text = (
            frame["comment_text"]
            .iloc[start:end]
            .fillna("")
            .astype(str)
            .str.normalize(TEXT_PROCESSING_CONFIG["unicode_normalization"])
            .str.replace(ZERO_WIDTH_PATTERN, "", regex=True)
            .str.replace(CONTROL_PATTERN, " ", regex=True)
        )

        char_count = _as_float32(text.str.len())
        word_count = _as_float32(text.str.count(r"\S+"))
        alpha_count = _as_float32(text.str.count(r"[A-Za-z]"))
        uppercase_count = _as_float32(text.str.count(r"[A-Z]"))
        digit_count = _as_float32(text.str.count(r"\d"))
        non_ascii_count = _as_float32(text.str.count(r"[^\x00-\x7F]"))
        punctuation_count = _as_float32(text.str.count(r"[^\w\s]"))
        exclamation_count = _as_float32(text.str.count(r"!"))
        question_count = _as_float32(text.str.count(r"\?"))
        linebreak_count = _as_float32(text.str.count(r"[\r\n]"))
        url_count = _as_float32(text.str.count(URL_PATTERN))
        email_count = _as_float32(text.str.count(EMAIL_PATTERN))
        user_mention_count = _as_float32(text.str.count(USER_PATTERN))
        repeated_punctuation_count = _as_float32(text.str.count(r"[!?.,;:]{2,}"))
        all_caps_word_count = _as_float32(text.str.count(r"\b[A-Z]{2,}\b"))
        second_person_count = _as_float32(
            text.str.count(r"(?i)\b(?:you|your|yours|yourself|yourselves|u|ur)\b")
        )

        safe_char_count = np.maximum(char_count, 1.0)
        safe_alpha_count = np.maximum(alpha_count, 1.0)
        safe_word_count = np.maximum(word_count, 1.0)

        chunk_features = np.column_stack(
            [
                np.log1p(char_count),
                np.log1p(word_count),
                alpha_count / safe_word_count,
                uppercase_count / safe_alpha_count,
                digit_count / safe_char_count,
                non_ascii_count / safe_char_count,
                punctuation_count / safe_char_count,
                np.log1p(exclamation_count),
                np.log1p(question_count),
                np.log1p(linebreak_count),
                np.log1p(url_count),
                np.log1p(email_count),
                np.log1p(user_mention_count),
                np.log1p(repeated_punctuation_count),
                all_caps_word_count / safe_word_count,
                second_person_count / safe_word_count,
            ]
        ).astype(np.float32, copy=False)

        cleaned = (
            text.str.replace(
                URL_PATTERN,
                TEXT_PROCESSING_CONFIG["url_replacement"],
                regex=True,
            )
            .str.replace(
                EMAIL_PATTERN,
                TEXT_PROCESSING_CONFIG["email_replacement"],
                regex=True,
            )
            .str.replace(
                USER_PATTERN,
                TEXT_PROCESSING_CONFIG["user_mention_replacement"],
                regex=True,
            )
            .str.replace(WHITESPACE_PATTERN, " ", regex=True)
            .str.strip()
        )

        normalized_text[start:end] = cleaned.to_numpy(dtype=object)
        features[start:end] = chunk_features

    frame["comment_text"] = normalized_text
    np.nan_to_num(
        features,
        copy=False,
        nan=0.0,
        posinf=0.0,
        neginf=0.0,
    )
    return features


train_text_features_raw = normalize_and_extract_text_features(train_df)
valid_text_features_raw = normalize_and_extract_text_features(valid_df)
test_text_features_raw = normalize_and_extract_text_features(test_df)

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

np.clip(train_text_features, -8.0, 8.0, out=train_text_features)
np.clip(valid_text_features, -8.0, 8.0, out=valid_text_features)
np.clip(test_text_features, -8.0, 8.0, out=test_text_features)

word_count_feature_index = TEXT_FEATURE_NAMES.index("log1p_word_count")
training_word_count_q95 = float(
    np.expm1(
        np.quantile(
            train_text_features_raw[:, word_count_feature_index],
            0.95,
        )
    )
)

estimated_token_q95 = int(np.ceil(training_word_count_q95 * 1.35 + 8))
recommended_max_length = int(
    np.clip(
        np.ceil(estimated_token_q95 / 64.0) * 64,
        128,
        384,
    )
)


def build_label_bundle(frame):
    identity_values = frame[ALL_IDENTITY_COLUMNS].to_numpy(
        dtype=np.float32,
        copy=True,
    )
    evaluation_identity_values = frame[EVALUATION_IDENTITY_COLUMNS].to_numpy(
        dtype=np.float32,
        copy=True,
    )
    subtype_values = frame[TOXICITY_SUBTYPE_COLUMNS].to_numpy(
        dtype=np.float32,
        copy=True,
    )

    identity_observed = ~np.isnan(identity_values)
    evaluation_identity_observed = ~np.isnan(evaluation_identity_values)
    subtype_observed = ~np.isnan(subtype_values)

    identity_masks = np.nan_to_num(identity_values, nan=0.0) >= 0.5
    evaluation_identity_masks = (
        np.nan_to_num(evaluation_identity_values, nan=0.0) >= 0.5
    )

    hard_target = frame["target_hard"].to_numpy(
        dtype=np.uint8,
        copy=True,
    )
    any_evaluation_identity = evaluation_identity_masks.any(axis=1)

    return {
        "target_soft": frame["target_soft"].to_numpy(
            dtype=np.float32,
            copy=True,
        ),
        "target_hard": hard_target,
        "toxicity_subtypes_soft": subtype_values,
        "toxicity_subtypes_observed": subtype_observed,
        "identity_soft": identity_values,
        "identity_observed": identity_observed,
        "identity_mask": identity_masks,
        "evaluation_identity_soft": evaluation_identity_values,
        "evaluation_identity_observed": evaluation_identity_observed,
        "evaluation_identity_mask": evaluation_identity_masks,
        "any_evaluation_identity": any_evaluation_identity,
        "metric_cell": (
            hard_target.astype(np.uint8) + 2 * any_evaluation_identity.astype(np.uint8)
        ),
        "toxicity_annotator_count": frame["toxicity_annotator_count"].to_numpy(
            dtype=np.float32,
            copy=True,
        ),
        "identity_annotator_count": frame["identity_annotator_count"].to_numpy(
            dtype=np.float32,
            copy=True,
        ),
    }


train_labels = build_label_bundle(train_df)
valid_labels = build_label_bundle(valid_df)

processing_metadata = {
    "seed": SEED,
    "text_column": "comment_text",
    "target_column": "target_soft",
    "hard_target_threshold": 0.5,
    "identity_threshold": 0.5,
    "text_feature_names": TEXT_FEATURE_NAMES,
    "toxicity_subtype_columns": TOXICITY_SUBTYPE_COLUMNS,
    "all_identity_columns": ALL_IDENTITY_COLUMNS,
    "evaluation_identity_columns": EVALUATION_IDENTITY_COLUMNS,
    "text_processing": TEXT_PROCESSING_CONFIG,
    "recommended_max_length": recommended_max_length,
    "train_rows": len(train_df),
    "validation_rows": len(valid_df),
    "test_rows": len(test_df),
    "train_word_count_q95": training_word_count_q95,
}

joblib.dump(
    text_feature_scaler,
    WORKING_DIR / "text_feature_scaler.joblib",
)
np.save(
    WORKING_DIR / "train_text_features.npy",
    train_text_features,
    allow_pickle=False,
)
np.save(
    WORKING_DIR / "valid_text_features.npy",
    valid_text_features,
    allow_pickle=False,
)
np.save(
    WORKING_DIR / "test_text_features.npy",
    test_text_features,
    allow_pickle=False,
)

with open(
    WORKING_DIR / "processing_metadata.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(processing_metadata, file, indent=2)

prepared_data = {
    "session": session,
    "train_df": train_df,
    "valid_df": valid_df,
    "test_df": test_df,
    "train_text_features": train_text_features,
    "valid_text_features": valid_text_features,
    "test_text_features": test_text_features,
    "train_labels": train_labels,
    "valid_labels": valid_labels,
    "text_feature_scaler": text_feature_scaler,
    "metadata": processing_metadata,
}

del (
    train_text_features_raw,
    valid_text_features_raw,
    test_text_features_raw,
)
gc.collect()


# ---------------------------------------------------------------------------
# ModernBERT backbone and fused toxicity head
# ---------------------------------------------------------------------------
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


class ModernBertToxicityModel(nn.Module):
    def __init__(
        self,
        pretrained_sequence_model,
        numeric_feature_count,
        numeric_hidden_size=64,
        dropout_probability=0.15,
    ):
        super().__init__()

        self.encoder = pretrained_sequence_model.base_model
        hidden_size = int(self.encoder.config.hidden_size)

        self.text_normalization = nn.LayerNorm(hidden_size)

        self.numeric_projection = nn.Sequential(
            nn.Linear(numeric_feature_count, numeric_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(numeric_hidden_size, numeric_hidden_size),
            nn.GELU(),
        )

        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden_size + numeric_hidden_size),
            nn.Dropout(dropout_probability),
            nn.Linear(
                hidden_size + numeric_hidden_size,
                hidden_size // 2,
            ),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.toxicity_head = nn.Linear(hidden_size // 2, 1)

        self.numeric_feature_count = int(numeric_feature_count)
        self.architecture_config = {
            "model_id": model_id,
            "numeric_feature_count": self.numeric_feature_count,
            "numeric_hidden_size": int(numeric_hidden_size),
            "dropout_probability": float(dropout_probability),
            "pooling": "masked_mean",
            "output": "single_toxicity_logit",
        }

        self._initialize_task_layers()

    def _initialize_task_layers(self):
        for module in (
            self.numeric_projection,
            self.fusion,
            self.toxicity_head,
        ):
            for layer in module.modules():
                if isinstance(layer, nn.Linear):
                    nn.init.xavier_uniform_(layer.weight)
                    if layer.bias is not None:
                        nn.init.zeros_(layer.bias)

    @staticmethod
    def _masked_mean_pool(last_hidden_state, attention_mask):
        mask = attention_mask.unsqueeze(-1).to(
            dtype=last_hidden_state.dtype,
            device=last_hidden_state.device,
        )
        summed = (last_hidden_state * mask).sum(dim=1)
        denominator = mask.sum(dim=1).clamp_min(1.0)
        return summed / denominator

    def forward(
        self,
        input_ids,
        attention_mask,
        text_features,
    ):
        if text_features is None:
            raise ValueError("text_features must be supplied for every sample.")

        if text_features.ndim != 2:
            raise ValueError("text_features must have shape [batch, feature_count].")

        if text_features.shape[1] != self.numeric_feature_count:
            raise ValueError(
                f"Expected {self.numeric_feature_count} text features, "
                f"received {text_features.shape[1]}."
            )

        encoder_output = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        pooled_text = self._masked_mean_pool(
            encoder_output.last_hidden_state,
            attention_mask,
        )
        pooled_text = self.text_normalization(pooled_text)

        numeric_embedding = self.numeric_projection(
            text_features.to(dtype=pooled_text.dtype)
        )

        fused_embedding = torch.cat(
            [pooled_text, numeric_embedding],
            dim=-1,
        )
        fused_embedding = self.fusion(fused_embedding)

        return self.toxicity_head(fused_embedding).squeeze(-1)


# ---------------------------------------------------------------------------
# Soft BCE plus queue-backed official-AUC pool ranking surrogate
# ---------------------------------------------------------------------------
class QueueBackedOfficialAUCLoss(nn.Module):
    def __init__(
        self,
        identity_count,
        queue_size=8192,
        maximum_pairs_per_direction=512,
        pairwise_weight=0.20,
        temperature=1.0,
    ):
        super().__init__()

        if identity_count <= 0:
            raise ValueError("identity_count must be positive.")
        if queue_size <= 0:
            raise ValueError("queue_size must be positive.")
        if maximum_pairs_per_direction <= 0:
            raise ValueError("maximum_pairs_per_direction must be positive.")
        if temperature <= 0.0:
            raise ValueError("temperature must be positive.")

        self.identity_count = int(identity_count)
        self.queue_size = int(queue_size)
        self.maximum_pairs_per_direction = int(maximum_pairs_per_direction)
        self.pairwise_weight = float(pairwise_weight)
        self.temperature = float(temperature)

        self.register_buffer(
            "_queue_logits",
            torch.zeros(self.queue_size, dtype=torch.float32),
        )
        self.register_buffer(
            "_queue_targets",
            torch.zeros(self.queue_size, dtype=torch.bool),
        )
        self.register_buffer(
            "_queue_identities",
            torch.zeros(
                self.queue_size,
                self.identity_count,
                dtype=torch.bool,
            ),
        )
        self.register_buffer(
            "_queue_pointer",
            torch.zeros((), dtype=torch.long),
        )
        self.register_buffer(
            "_queue_filled",
            torch.zeros((), dtype=torch.long),
        )

        self.group_dro_family_names = (
            "subgroup",
            "bpsn",
            "bnsp",
        )
        self.group_dro_ema_decay = 0.95
        self.group_dro_temperature = 0.5
        self.group_dro_max_cell_weight = 0.35
        self.group_dro_config = {
            "family_names": list(self.group_dro_family_names),
            "ema_decay": self.group_dro_ema_decay,
            "temperature": self.group_dro_temperature,
            "maximum_cell_weight": self.group_dro_max_cell_weight,
            "initial_ema_loss": float(math.log(2.0)),
            "update_frequency": "successful_optimizer_step",
            "availability_policy": "masked_without_ema_or_gradient_weight",
            "projection": "iterative_cap_and_redistribute",
        }

        initial_ema_loss = float(math.log(2.0))
        initial_cell_weight = 1.0 / float(self.identity_count)

        for family_name in self.group_dro_family_names:
            self.register_buffer(
                f"_{family_name}_ema_losses",
                torch.full(
                    (self.identity_count,),
                    initial_ema_loss,
                    dtype=torch.float32,
                ),
            )
            self.register_buffer(
                f"_{family_name}_weights",
                torch.full(
                    (self.identity_count,),
                    initial_cell_weight,
                    dtype=torch.float32,
                ),
            )
            self.register_buffer(
                f"_{family_name}_accumulated_loss_sums",
                torch.zeros(self.identity_count, dtype=torch.float32),
            )
            self.register_buffer(
                f"_{family_name}_availability_counts",
                torch.zeros(self.identity_count, dtype=torch.long),
            )
            self.register_buffer(
                f"_{family_name}_last_availability",
                torch.zeros(self.identity_count, dtype=torch.bool),
            )

        self.last_components = {}

    def reset_queue(self):
        self._queue_logits.zero_()
        self._queue_targets.zero_()
        self._queue_identities.zero_()
        self._queue_pointer.zero_()
        self._queue_filled.zero_()

    def _available_queue(self):
        count = int(self._queue_filled.item())
        return (
            self._queue_logits[:count],
            self._queue_targets[:count],
            self._queue_identities[:count],
        )

    @torch.no_grad()
    def _enqueue(
        self,
        logits,
        hard_targets,
        identity_masks,
    ):
        logits = logits.detach().float().reshape(-1)
        hard_targets = hard_targets.detach().bool().reshape(-1)
        identity_masks = identity_masks.detach().bool()

        row_count = logits.shape[0]
        if row_count == 0:
            return

        if row_count >= self.queue_size:
            self._queue_logits.copy_(logits[-self.queue_size :])
            self._queue_targets.copy_(hard_targets[-self.queue_size :])
            self._queue_identities.copy_(identity_masks[-self.queue_size :])
            self._queue_pointer.zero_()
            self._queue_filled.fill_(self.queue_size)
            return

        pointer = int(self._queue_pointer.item())
        first_count = min(row_count, self.queue_size - pointer)
        second_count = row_count - first_count

        self._queue_logits[pointer : pointer + first_count].copy_(logits[:first_count])
        self._queue_targets[pointer : pointer + first_count].copy_(
            hard_targets[:first_count]
        )
        self._queue_identities[pointer : pointer + first_count].copy_(
            identity_masks[:first_count]
        )

        if second_count > 0:
            self._queue_logits[:second_count].copy_(logits[first_count:])
            self._queue_targets[:second_count].copy_(hard_targets[first_count:])
            self._queue_identities[:second_count].copy_(identity_masks[first_count:])

        self._queue_pointer.fill_((pointer + row_count) % self.queue_size)
        self._queue_filled.fill_(
            min(
                self.queue_size,
                int(self._queue_filled.item()) + row_count,
            )
        )

    def _sampled_directional_loss(
        self,
        positive_logits,
        negative_logits,
    ):
        positive_count = positive_logits.numel()
        negative_count = negative_logits.numel()

        if positive_count == 0 or negative_count == 0:
            return None

        total_pair_count = positive_count * negative_count
        pair_count = min(
            total_pair_count,
            self.maximum_pairs_per_direction,
        )

        if total_pair_count <= self.maximum_pairs_per_direction:
            margins = (positive_logits[:, None] - negative_logits[None, :]).reshape(-1)
        else:
            positive_indices = torch.randint(
                low=0,
                high=positive_count,
                size=(pair_count,),
                device=positive_logits.device,
            )
            negative_indices = torch.randint(
                low=0,
                high=negative_count,
                size=(pair_count,),
                device=negative_logits.device,
            )
            margins = (
                positive_logits[positive_indices] - negative_logits[negative_indices]
            )

        return F.softplus(-margins / self.temperature).mean()

    def _pool_loss(
        self,
        current_logits,
        queue_logits,
        current_positive_mask,
        current_negative_mask,
        queue_positive_mask,
        queue_negative_mask,
    ):
        directional_losses = []

        current_positive_logits = current_logits[current_positive_mask]
        current_negative_logits = current_logits[current_negative_mask]
        queue_positive_logits = queue_logits[queue_positive_mask]
        queue_negative_logits = queue_logits[queue_negative_mask]

        all_negative_logits = torch.cat(
            [
                current_negative_logits,
                queue_negative_logits,
            ],
            dim=0,
        )

        current_positive_loss = self._sampled_directional_loss(
            current_positive_logits,
            all_negative_logits,
        )
        if current_positive_loss is not None:
            directional_losses.append(current_positive_loss)

        queue_positive_loss = self._sampled_directional_loss(
            queue_positive_logits,
            current_negative_logits,
        )
        if queue_positive_loss is not None:
            directional_losses.append(queue_positive_loss)

        if not directional_losses:
            return None

        return torch.stack(directional_losses).mean()

    def _family_buffers(self, family_name):
        if family_name not in self.group_dro_family_names:
            raise KeyError(f"Unknown group-DRO family: {family_name}")

        return (
            getattr(self, f"_{family_name}_ema_losses"),
            getattr(self, f"_{family_name}_weights"),
            getattr(self, f"_{family_name}_accumulated_loss_sums"),
            getattr(self, f"_{family_name}_availability_counts"),
            getattr(self, f"_{family_name}_last_availability"),
        )

    @torch.no_grad()
    def _project_capped_weights(self, unprojected_weights):
        unprojected_weights = unprojected_weights.float().reshape(-1)

        if unprojected_weights.numel() != self.identity_count:
            raise ValueError("Group-DRO weight vector has an incompatible shape.")

        finite_weights = torch.nan_to_num(
            unprojected_weights,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        ).clamp_min(0.0)

        if float(finite_weights.sum().item()) <= 0.0:
            finite_weights.fill_(1.0)

        effective_cap = max(
            self.group_dro_max_cell_weight,
            1.0 / float(self.identity_count),
        )
        projected_weights = torch.zeros_like(finite_weights)
        remaining_mask = torch.ones_like(finite_weights, dtype=torch.bool)
        remaining_mass = 1.0

        for _ in range(self.identity_count):
            remaining_count = int(remaining_mask.sum().item())
            if remaining_count == 0:
                break

            remaining_source = finite_weights[remaining_mask]
            source_sum = remaining_source.sum()

            if float(source_sum.item()) <= 0.0:
                candidate_weights = torch.full_like(
                    remaining_source,
                    remaining_mass / float(remaining_count),
                )
            else:
                candidate_weights = (
                    remaining_source / source_sum * remaining_mass
                )

            capped_mask = candidate_weights > effective_cap

            if not bool(capped_mask.any().item()):
                projected_weights[remaining_mask] = candidate_weights
                remaining_mass = 0.0
                break

            remaining_indices = torch.nonzero(
                remaining_mask,
                as_tuple=False,
            ).reshape(-1)
            capped_indices = remaining_indices[capped_mask]
            projected_weights[capped_indices] = effective_cap
            remaining_mask[capped_indices] = False
            remaining_mass = max(
                0.0,
                remaining_mass
                - effective_cap * float(capped_indices.numel()),
            )

        if bool(remaining_mask.any().item()) and remaining_mass > 0.0:
            remaining_count = int(remaining_mask.sum().item())
            projected_weights[remaining_mask] = (
                remaining_mass / float(remaining_count)
            )

        return projected_weights / projected_weights.sum().clamp_min(1e-12)

    def _group_dro_family_loss(
        self,
        losses,
        family_name,
        accumulate_statistics,
    ):
        availability = torch.tensor(
            [loss is not None for loss in losses],
            dtype=torch.bool,
            device=self._queue_logits.device,
        )
        normalized_weights = torch.zeros(
            self.identity_count,
            dtype=torch.float32,
            device=self._queue_logits.device,
        )

        if not bool(availability.any().item()):
            return None, availability, normalized_weights

        (
            _,
            persistent_weights,
            accumulated_loss_sums,
            availability_counts,
            _,
        ) = self._family_buffers(family_name)

        masked_weights = persistent_weights.float() * availability.float()
        masked_weight_sum = masked_weights.sum()

        if float(masked_weight_sum.detach().item()) <= 0.0:
            normalized_weights[availability] = (
                1.0 / float(availability.sum().item())
            )
        else:
            normalized_weights = masked_weights / masked_weight_sum

        available_losses = torch.stack(
            [loss for loss in losses if loss is not None]
        )
        family_loss = (
            available_losses
            * normalized_weights[availability].to(
                dtype=available_losses.dtype
            )
        ).sum()

        if accumulate_statistics:
            with torch.no_grad():
                detached_losses = available_losses.detach().float()
                accumulated_loss_sums[availability].add_(detached_losses)
                availability_counts[availability].add_(1)

        return family_loss, availability, normalized_weights

    @torch.no_grad()
    def commit_group_dro_statistics(self):
        for family_name in self.group_dro_family_names:
            (
                ema_losses,
                persistent_weights,
                accumulated_loss_sums,
                availability_counts,
                last_availability,
            ) = self._family_buffers(family_name)

            availability = availability_counts > 0
            last_availability.copy_(availability)

            if bool(availability.any().item()):
                observed_losses = (
                    accumulated_loss_sums[availability]
                    / availability_counts[availability].float()
                )
                ema_losses[availability].mul_(
                    self.group_dro_ema_decay
                ).add_(
                    observed_losses,
                    alpha=(1.0 - self.group_dro_ema_decay),
                )

                stabilized_logits = (
                    ema_losses / self.group_dro_temperature
                )
                stabilized_logits = stabilized_logits - stabilized_logits.max()
                exponentiated_weights = torch.exp(stabilized_logits)
                persistent_weights.copy_(
                    self._project_capped_weights(exponentiated_weights)
                )

            accumulated_loss_sums.zero_()
            availability_counts.zero_()

    @torch.no_grad()
    def discard_group_dro_statistics(self):
        for family_name in self.group_dro_family_names:
            (
                _,
                _,
                accumulated_loss_sums,
                availability_counts,
                _,
            ) = self._family_buffers(family_name)
            accumulated_loss_sums.zero_()
            availability_counts.zero_()

    @torch.no_grad()
    def group_dro_snapshot(self, identity_names=None):
        if identity_names is None:
            identity_names = [
                str(identity_index)
                for identity_index in range(self.identity_count)
            ]

        if len(identity_names) != self.identity_count:
            raise ValueError("Identity-name order has an incompatible length.")

        snapshot = {
            "identity_order": list(identity_names),
            "config": dict(self.group_dro_config),
            "families": {},
        }

        for family_name in self.group_dro_family_names:
            (
                ema_losses,
                persistent_weights,
                _,
                _,
                last_availability,
            ) = self._family_buffers(family_name)

            family_weights = persistent_weights.detach().float().cpu()
            snapshot["families"][family_name] = {
                "availability": (
                    last_availability.detach().cpu().tolist()
                ),
                "ema_losses": ema_losses.detach().float().cpu().tolist(),
                "weights": family_weights.tolist(),
                "maximum_concentration": float(family_weights.max().item()),
            }

        snapshot["maximum_family_concentration"] = max(
            family_snapshot["maximum_concentration"]
            for family_snapshot in snapshot["families"].values()
        )
        return snapshot

    def forward(
        self,
        logits,
        soft_targets,
        hard_targets,
        evaluation_identity_masks,
        update_queue=True,
    ):
        logits = logits.float().reshape(-1)
        soft_targets = soft_targets.float().reshape(-1).clamp(0.0, 1.0)
        hard_targets = hard_targets.bool().reshape(-1)
        evaluation_identity_masks = evaluation_identity_masks.bool()

        if logits.shape != soft_targets.shape:
            raise ValueError("logits and soft_targets must have equal shape.")

        if logits.shape != hard_targets.shape:
            raise ValueError("logits and hard_targets must have equal shape.")

        if evaluation_identity_masks.shape != (
            logits.shape[0],
            self.identity_count,
        ):
            raise ValueError("evaluation_identity_masks has an incompatible shape.")

        if self._queue_logits.device != logits.device:
            self.to(logits.device)

        pointwise_loss = F.binary_cross_entropy_with_logits(
            logits,
            soft_targets,
        )

        (
            queue_logits,
            queue_targets,
            queue_identities,
        ) = self._available_queue()

        current_positive = hard_targets
        current_negative = ~hard_targets
        queue_positive = queue_targets
        queue_negative = ~queue_targets

        overall_loss = self._pool_loss(
            current_logits=logits,
            queue_logits=queue_logits,
            current_positive_mask=current_positive,
            current_negative_mask=current_negative,
            queue_positive_mask=queue_positive,
            queue_negative_mask=queue_negative,
        )

        subgroup_losses = []
        bpsn_losses = []
        bnsp_losses = []

        for identity_index in range(self.identity_count):
            current_subgroup = evaluation_identity_masks[
                :,
                identity_index,
            ]
            queue_subgroup = queue_identities[
                :,
                identity_index,
            ]

            current_background = ~current_subgroup
            queue_background = ~queue_subgroup

            subgroup_losses.append(
                self._pool_loss(
                    current_logits=logits,
                    queue_logits=queue_logits,
                    current_positive_mask=(current_positive & current_subgroup),
                    current_negative_mask=(current_negative & current_subgroup),
                    queue_positive_mask=(queue_positive & queue_subgroup),
                    queue_negative_mask=(queue_negative & queue_subgroup),
                )
            )

            bpsn_losses.append(
                self._pool_loss(
                    current_logits=logits,
                    queue_logits=queue_logits,
                    current_positive_mask=(current_positive & current_background),
                    current_negative_mask=(current_negative & current_subgroup),
                    queue_positive_mask=(queue_positive & queue_background),
                    queue_negative_mask=(queue_negative & queue_subgroup),
                )
            )

            bnsp_losses.append(
                self._pool_loss(
                    current_logits=logits,
                    queue_logits=queue_logits,
                    current_positive_mask=(current_positive & current_subgroup),
                    current_negative_mask=(current_negative & current_background),
                    queue_positive_mask=(queue_positive & queue_subgroup),
                    queue_negative_mask=(queue_negative & queue_background),
                )
            )

        (
            subgroup_loss,
            subgroup_availability,
            subgroup_weights,
        ) = self._group_dro_family_loss(
            subgroup_losses,
            family_name="subgroup",
            accumulate_statistics=update_queue,
        )
        (
            bpsn_loss,
            bpsn_availability,
            bpsn_weights,
        ) = self._group_dro_family_loss(
            bpsn_losses,
            family_name="bpsn",
            accumulate_statistics=update_queue,
        )
        (
            bnsp_loss,
            bnsp_availability,
            bnsp_weights,
        ) = self._group_dro_family_loss(
            bnsp_losses,
            family_name="bnsp",
            accumulate_statistics=update_queue,
        )

        official_family_surrogates = [
            loss
            for loss in (
                overall_loss,
                subgroup_loss,
                bpsn_loss,
                bnsp_loss,
            )
            if loss is not None
        ]

        if official_family_surrogates:
            ranking_loss = (
                torch.stack(official_family_surrogates).sum()
                / float(len(official_family_surrogates))
            )
        else:
            ranking_loss = logits.sum() * 0.0

        total_loss = pointwise_loss + self.pairwise_weight * ranking_loss

        self.last_components = {
            "total": total_loss.detach(),
            "soft_bce": pointwise_loss.detach(),
            "official_auc_surrogate": ranking_loss.detach(),
            "overall_auc_surrogate": (
                None if overall_loss is None else overall_loss.detach()
            ),
            "subgroup_auc_surrogate": (
                None if subgroup_loss is None else subgroup_loss.detach()
            ),
            "bpsn_auc_surrogate": (None if bpsn_loss is None else bpsn_loss.detach()),
            "bnsp_auc_surrogate": (None if bnsp_loss is None else bnsp_loss.detach()),
            "group_dro": {
                "config": dict(self.group_dro_config),
                "subgroup": {
                    "availability": subgroup_availability.detach(),
                    "ema_losses": self._subgroup_ema_losses.detach().clone(),
                    "normalized_weights": subgroup_weights.detach(),
                },
                "bpsn": {
                    "availability": bpsn_availability.detach(),
                    "ema_losses": self._bpsn_ema_losses.detach().clone(),
                    "normalized_weights": bpsn_weights.detach(),
                },
                "bnsp": {
                    "availability": bnsp_availability.detach(),
                    "ema_losses": self._bnsp_ema_losses.detach().clone(),
                    "normalized_weights": bnsp_weights.detach(),
                },
            },
        }

        if update_queue:
            self._enqueue(
                logits=logits,
                hard_targets=hard_targets,
                identity_masks=evaluation_identity_masks,
            )

        return total_loss


model = ModernBertToxicityModel(
    pretrained_sequence_model=model,
    numeric_feature_count=len(TEXT_FEATURE_NAMES),
    numeric_hidden_size=64,
    dropout_probability=0.15,
)

if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable()

if hasattr(model.encoder.config, "use_cache"):
    model.encoder.config.use_cache = False

criterion = QueueBackedOfficialAUCLoss(
    identity_count=len(EVALUATION_IDENTITY_COLUMNS),
    queue_size=8192,
    maximum_pairs_per_direction=512,
    pairwise_weight=0.20,
    temperature=1.0,
)


# ---------------------------------------------------------------------------
# Optimizer and mixed precision
# ---------------------------------------------------------------------------
backbone_learning_rate = 1.2e-5
head_learning_rate = 8.0e-5
weight_decay = 0.01

optimizer_parameter_groups = {
    ("backbone", "decay"): [],
    ("backbone", "no_decay"): [],
    ("head", "decay"): [],
    ("head", "no_decay"): [],
}

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    component = "backbone" if parameter_name.startswith("encoder.") else "head"

    use_weight_decay = not (
        parameter_name.endswith(".bias")
        or parameter.ndim == 1
        or "norm" in parameter_name.lower()
    )

    decay_group = "decay" if use_weight_decay else "no_decay"
    optimizer_parameter_groups[(component, decay_group)].append(parameter)

optimizer = AdamW(
    [
        {
            "params": optimizer_parameter_groups[("backbone", "decay")],
            "lr": backbone_learning_rate,
            "weight_decay": weight_decay,
        },
        {
            "params": optimizer_parameter_groups[("backbone", "no_decay")],
            "lr": backbone_learning_rate,
            "weight_decay": 0.0,
        },
        {
            "params": optimizer_parameter_groups[("head", "decay")],
            "lr": head_learning_rate,
            "weight_decay": weight_decay,
        },
        {
            "params": optimizer_parameter_groups[("head", "no_decay")],
            "lr": head_learning_rate,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

use_mixed_precision = torch.cuda.is_available()
mixed_precision_dtype = (
    torch.bfloat16
    if (use_mixed_precision and torch.cuda.is_bf16_supported())
    else torch.float16
)

grad_scaler = torch.cuda.amp.GradScaler(
    enabled=(use_mixed_precision and mixed_precision_dtype == torch.float16)
)

model_design_config = {
    "model_id": model_id,
    "maximum_sequence_length": int(prepared_data["metadata"]["recommended_max_length"]),
    "numeric_feature_names": list(TEXT_FEATURE_NAMES),
    "evaluation_identity_columns": list(EVALUATION_IDENTITY_COLUMNS),
    "soft_target_training": True,
    "hard_target_threshold_for_auc_loss": 0.5,
    "queue_size": criterion.queue_size,
    "maximum_pairs_per_direction": (criterion.maximum_pairs_per_direction),
    "pairwise_weight": criterion.pairwise_weight,
    "pairwise_temperature": criterion.temperature,
    "group_dro": dict(criterion.group_dro_config),
    "group_dro_family_coefficient": 0.25,
    "backbone_learning_rate": backbone_learning_rate,
    "head_learning_rate": head_learning_rate,
    "weight_decay": weight_decay,
    "mixed_precision_dtype": str(mixed_precision_dtype),
}


# ---------------------------------------------------------------------------
# Runtime training configuration
# ---------------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model.to(device)
criterion.to(device)

maximum_sequence_length = int(model_design_config["maximum_sequence_length"])
train_batch_size = 4 if device.type == "cuda" else 1
inference_batch_size = 16 if device.type == "cuda" else 2
gradient_accumulation_steps = 2 if device.type == "cuda" else 8
maximum_epochs = 3
maximum_gradient_norm = 1.0
warmup_optimizer_steps = 100

optimizer.zero_grad(set_to_none=True)


def learning_rate_multiplier(step):
    if step < warmup_optimizer_steps:
        return max(
            0.01,
            float(step + 1) / float(warmup_optimizer_steps),
        )

    decay_steps = step - warmup_optimizer_steps
    return max(
        0.20,
        math.exp(-decay_steps / 8000.0),
    )


scheduler = LambdaLR(
    optimizer,
    lr_lambda=learning_rate_multiplier,
)


# ---------------------------------------------------------------------------
# Auditable task-faithful official metric implementation
# CandidateSession owns checkpoint selection using its contract implementation.
# ---------------------------------------------------------------------------
def _safe_binary_auc(labels, predictions):
    labels = np.asarray(labels, dtype=np.uint8)
    predictions = np.asarray(
        predictions,
        dtype=np.float64,
    )

    if labels.size == 0 or np.unique(labels).size != 2:
        return np.nan

    return float(roc_auc_score(labels, predictions))


def _negative_power_mean(values, power=-5):
    values = np.asarray(values, dtype=np.float64)

    if values.size == 0 or not np.all(np.isfinite(values)):
        return np.nan

    if np.any(values <= 0.0):
        return 0.0

    return float(
        np.power(
            np.mean(np.power(values, power)),
            1.0 / power,
        )
    )


def calculate_official_jigsaw_metric(
    target_values,
    prediction_values,
    identity_values,
    identity_names=EVALUATION_IDENTITY_COLUMNS,
):
    hard_target = np.asarray(target_values, dtype=np.float64) >= 0.5
    predictions = np.asarray(
        prediction_values,
        dtype=np.float64,
    ).reshape(-1)
    identity_values = np.asarray(
        identity_values,
        dtype=np.float64,
    )

    if predictions.shape[0] != hard_target.shape[0]:
        raise ValueError("Target and prediction lengths do not match.")

    if identity_values.shape != (
        hard_target.shape[0],
        len(identity_names),
    ):
        raise ValueError("Identity matrix has an incompatible shape.")

    overall_auc = _safe_binary_auc(
        hard_target,
        predictions,
    )
    metric_rows = []

    for identity_index, identity_name in enumerate(identity_names):
        subgroup = (
            np.nan_to_num(
                identity_values[:, identity_index],
                nan=0.0,
            )
            >= 0.5
        )
        background = ~subgroup

        subgroup_mask = subgroup
        bpsn_mask = (background & hard_target) | (subgroup & ~hard_target)
        bnsp_mask = (subgroup & hard_target) | (background & ~hard_target)

        metric_rows.append(
            {
                "identity": identity_name,
                "subgroup_auc": _safe_binary_auc(
                    hard_target[subgroup_mask],
                    predictions[subgroup_mask],
                ),
                "bpsn_auc": _safe_binary_auc(
                    hard_target[bpsn_mask],
                    predictions[bpsn_mask],
                ),
                "bnsp_auc": _safe_binary_auc(
                    hard_target[bnsp_mask],
                    predictions[bnsp_mask],
                ),
            }
        )

    subgroup_power_mean = _negative_power_mean(
        [row["subgroup_auc"] for row in metric_rows],
        power=-5,
    )
    bpsn_power_mean = _negative_power_mean(
        [row["bpsn_auc"] for row in metric_rows],
        power=-5,
    )
    bnsp_power_mean = _negative_power_mean(
        [row["bnsp_auc"] for row in metric_rows],
        power=-5,
    )

    components = np.asarray(
        [
            overall_auc,
            subgroup_power_mean,
            bpsn_power_mean,
            bnsp_power_mean,
        ],
        dtype=np.float64,
    )

    if not np.all(np.isfinite(components)):
        raise ValueError("Official metric contains an undefined AUC component.")

    return {
        "score": float(np.mean(components)),
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
        "per_identity": metric_rows,
    }


# ---------------------------------------------------------------------------
# Datasets and collators
# ---------------------------------------------------------------------------
class ToxicityTrainingDataset(Dataset):
    def __init__(
        self,
        texts,
        text_features,
        soft_targets,
        hard_targets,
        evaluation_identity_masks,
    ):
        self.texts = texts
        self.text_features = text_features
        self.soft_targets = soft_targets
        self.hard_targets = hard_targets
        self.evaluation_identity_masks = evaluation_identity_masks

        row_count = len(self.texts)

        if not (
            len(self.text_features)
            == len(self.soft_targets)
            == len(self.hard_targets)
            == len(self.evaluation_identity_masks)
            == row_count
        ):
            raise ValueError("Training arrays do not have matching row counts.")

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.text_features[index],
            self.soft_targets[index],
            self.hard_targets[index],
            self.evaluation_identity_masks[index],
        )


class PositionalInferenceDataset(Dataset):
    def __init__(
        self,
        texts,
        text_features,
        positional_indices,
    ):
        self.texts = texts
        self.text_features = text_features
        self.positional_indices = np.asarray(
            positional_indices,
            dtype=np.int64,
        ).reshape(-1)

        if len(self.texts) != len(self.text_features):
            raise ValueError("Inference text and feature arrays do not match.")

        if self.positional_indices.size:
            if self.positional_indices.min() < 0:
                raise IndexError("Negative positional inference index.")

            if self.positional_indices.max() >= len(self.texts):
                raise IndexError("Positional inference index is out of bounds.")

    def __len__(self):
        return len(self.positional_indices)

    def __getitem__(self, index):
        position = int(self.positional_indices[index])
        return (
            self.texts[position],
            self.text_features[position],
        )


class TrainingCollator:
    def __init__(
        self,
        tokenizer_object,
        max_length,
    ):
        self.tokenizer = tokenizer_object
        self.max_length = int(max_length)

    def __call__(self, rows):
        (
            texts,
            features,
            soft_targets,
            hard_targets,
            identity_masks,
        ) = zip(*rows)

        encoded = self.tokenizer(
            list(texts),
            padding=True,
            truncation=True,
            max_length=self.max_length,
            pad_to_multiple_of=8,
            return_tensors="pt",
            return_token_type_ids=False,
        )

        return {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "text_features": torch.from_numpy(
                np.stack(features).astype(
                    np.float32,
                    copy=False,
                )
            ),
            "soft_targets": torch.as_tensor(
                soft_targets,
                dtype=torch.float32,
            ),
            "hard_targets": torch.as_tensor(
                hard_targets,
                dtype=torch.bool,
            ),
            "evaluation_identity_masks": torch.from_numpy(
                np.stack(identity_masks).astype(
                    np.bool_,
                    copy=False,
                )
            ),
        }


class InferenceCollator:
    def __init__(
        self,
        tokenizer_object,
        max_length,
    ):
        self.tokenizer = tokenizer_object
        self.max_length = int(max_length)

    def __call__(self, rows):
        texts, features = zip(*rows)

        encoded = self.tokenizer(
            list(texts),
            padding=True,
            truncation=True,
            max_length=self.max_length,
            pad_to_multiple_of=8,
            return_tensors="pt",
            return_token_type_ids=False,
        )

        return {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "text_features": torch.from_numpy(
                np.stack(features).astype(
                    np.float32,
                    copy=False,
                )
            ),
        }


def seed_worker(worker_id):
    worker_seed = (SEED + worker_id) % (2**32)
    random.seed(worker_seed)
    np.random.seed(worker_seed)


class RoleCompleteWindowSampler(torch.utils.data.Sampler):
    def __init__(
        self,
        hard_targets,
        evaluation_identity_masks,
        batch_size,
        gradient_accumulation_steps,
        seed=2025,
    ):
        self.hard_targets = np.asarray(
            hard_targets,
            dtype=np.bool_,
        ).reshape(-1)
        self.evaluation_identity_masks = np.asarray(
            evaluation_identity_masks,
            dtype=np.bool_,
        )
        self.batch_size = int(batch_size)
        self.gradient_accumulation_steps = int(
            gradient_accumulation_steps
        )
        self.window_size = (
            self.batch_size * self.gradient_accumulation_steps
        )
        self.seed = int(seed)
        self.epoch = 0

        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive.")

        if self.gradient_accumulation_steps <= 0:
            raise ValueError(
                "gradient_accumulation_steps must be positive."
            )

        if self.window_size < 4:
            raise ValueError(
                "Role-complete windows require at least four samples."
            )

        if self.evaluation_identity_masks.ndim != 2:
            raise ValueError(
                "evaluation_identity_masks must be a two-dimensional array."
            )

        if (
            self.evaluation_identity_masks.shape[0]
            != self.hard_targets.shape[0]
        ):
            raise ValueError(
                "Sampler label arrays do not have matching row counts."
            )

        self.row_count = int(self.hard_targets.shape[0])
        self.identity_count = int(
            self.evaluation_identity_masks.shape[1]
        )

        if self.identity_count <= 0:
            raise ValueError(
                "RoleCompleteWindowSampler requires at least one identity."
            )

        self._subgroup_pools = {}

        for identity_index in range(self.identity_count):
            subgroup = self.evaluation_identity_masks[
                :,
                identity_index,
            ]

            self._subgroup_pools[(identity_index, True)] = np.flatnonzero(
                subgroup & self.hard_targets
            ).astype(np.int64, copy=False)
            self._subgroup_pools[(identity_index, False)] = np.flatnonzero(
                subgroup & ~self.hard_targets
            ).astype(np.int64, copy=False)

        self._cached_epoch = None
        self._cached_order = None

    def __len__(self):
        return self.row_count

    def set_epoch(self, epoch_index):
        epoch_index = int(epoch_index)

        if epoch_index < 0:
            raise ValueError("epoch_index must be non-negative.")

        if epoch_index != self.epoch:
            self.epoch = epoch_index
            self._cached_epoch = None
            self._cached_order = None

    def _role_positions(self):
        if (
            self.batch_size >= 2
            and self.gradient_accumulation_steps >= 2
        ):
            return (
                (0, "subgroup_positive"),
                (1, "background_positive"),
                (self.batch_size, "subgroup_negative"),
                (self.batch_size + 1, "background_negative"),
            )

        return (
            (0, "subgroup_positive"),
            (1, "background_positive"),
            (2, "subgroup_negative"),
            (3, "background_negative"),
        )

    def _build_epoch_order(self):
        if (
            self._cached_epoch == self.epoch
            and self._cached_order is not None
        ):
            return self._cached_order

        build_start = time.perf_counter()
        rng = np.random.default_rng(self.seed + self.epoch)
        epoch_permutation = rng.permutation(
            self.row_count
        ).astype(np.int64, copy=False)

        permutation_rank = np.empty(
            self.row_count,
            dtype=np.int64,
        )
        permutation_rank[epoch_permutation] = np.arange(
            self.row_count,
            dtype=np.int64,
        )

        ordered_subgroup_pools = {}

        for role_key, role_pool in self._subgroup_pools.items():
            if role_pool.size == 0:
                ordered_subgroup_pools[role_key] = role_pool
                continue

            ordered_subgroup_pools[role_key] = role_pool[
                np.argsort(
                    permutation_rank[role_pool],
                    kind="stable",
                )
            ]

        subgroup_cursors = {
            role_key: 0
            for role_key in ordered_subgroup_pools
        }
        background_cursors = {
            (identity_index, target_value): 0
            for identity_index in range(self.identity_count)
            for target_value in (False, True)
        }
        used = np.zeros(
            self.row_count,
            dtype=np.bool_,
        )
        epoch_order = np.full(
            self.row_count,
            -1,
            dtype=np.int64,
        )

        def take_subgroup(identity_index, target_value):
            role_key = (identity_index, target_value)
            role_pool = ordered_subgroup_pools[role_key]
            cursor = subgroup_cursors[role_key]

            while cursor < role_pool.size:
                row_index = int(role_pool[cursor])
                cursor += 1

                if not used[row_index]:
                    subgroup_cursors[role_key] = cursor
                    return row_index

            subgroup_cursors[role_key] = cursor
            return None

        def take_background(identity_index, target_value):
            role_key = (identity_index, target_value)
            cursor = background_cursors[role_key]

            while cursor < self.row_count:
                row_index = int(epoch_permutation[cursor])
                cursor += 1

                if used[row_index]:
                    continue

                if bool(self.hard_targets[row_index]) != target_value:
                    continue

                if self.evaluation_identity_masks[
                    row_index,
                    identity_index,
                ]:
                    continue

                background_cursors[role_key] = cursor
                return row_index

            background_cursors[role_key] = cursor
            return None

        role_positions = self._role_positions()
        window_count = int(
            math.ceil(self.row_count / float(self.window_size))
        )

        for window_index in range(window_count):
            window_start = window_index * self.window_size
            window_end = min(
                window_start + self.window_size,
                self.row_count,
            )
            window_length = window_end - window_start
            identity_index = (
                window_index + self.epoch
            ) % self.identity_count

            for relative_position, role_name in role_positions:
                if relative_position >= window_length:
                    continue

                if role_name == "subgroup_positive":
                    row_index = take_subgroup(
                        identity_index,
                        True,
                    )
                elif role_name == "subgroup_negative":
                    row_index = take_subgroup(
                        identity_index,
                        False,
                    )
                elif role_name == "background_positive":
                    row_index = take_background(
                        identity_index,
                        True,
                    )
                elif role_name == "background_negative":
                    row_index = take_background(
                        identity_index,
                        False,
                    )
                else:
                    raise RuntimeError(
                        f"Unknown sampler role: {role_name}"
                    )

                if row_index is None:
                    continue

                absolute_position = (
                    window_start + relative_position
                )

                if epoch_order[absolute_position] >= 0:
                    raise RuntimeError(
                        "Role scheduler attempted to overwrite a slot."
                    )

                epoch_order[absolute_position] = row_index
                used[row_index] = True

        fill_cursor = 0

        for order_position in range(self.row_count):
            if epoch_order[order_position] >= 0:
                continue

            while (
                fill_cursor < self.row_count
                and used[int(epoch_permutation[fill_cursor])]
            ):
                fill_cursor += 1

            if fill_cursor >= self.row_count:
                raise RuntimeError(
                    "Seeded epoch permutation was exhausted while filling."
                )

            row_index = int(epoch_permutation[fill_cursor])
            fill_cursor += 1
            epoch_order[order_position] = row_index
            used[row_index] = True

        if np.any(epoch_order < 0):
            raise RuntimeError(
                "Role-complete sampler left unfilled epoch positions."
            )

        self._cached_epoch = self.epoch
        self._cached_order = epoch_order
        self.last_build_seconds = float(
            time.perf_counter() - build_start
        )
        return self._cached_order

    def __iter__(self):
        return iter(self._build_epoch_order())


def _window_family_availability(
    order,
    hard_targets,
    identity_masks,
    window_size,
    maximum_windows,
):
    order = np.asarray(order, dtype=np.int64)
    hard_targets = np.asarray(
        hard_targets,
        dtype=np.bool_,
    )
    identity_masks = np.asarray(
        identity_masks,
        dtype=np.bool_,
    )
    available_window_count = int(
        math.ceil(order.size / float(window_size))
    )
    audited_window_count = min(
        int(maximum_windows),
        available_window_count,
    )
    family_counts = {
        "subgroup": np.zeros(
            identity_masks.shape[1],
            dtype=np.int64,
        ),
        "bpsn": np.zeros(
            identity_masks.shape[1],
            dtype=np.int64,
        ),
        "bnsp": np.zeros(
            identity_masks.shape[1],
            dtype=np.int64,
        ),
    }

    for window_index in range(audited_window_count):
        window_start = window_index * window_size
        window_end = min(
            window_start + window_size,
            order.size,
        )
        window_indices = order[window_start:window_end]
        window_targets = hard_targets[
            window_indices
        ][:, None]
        window_identities = identity_masks[window_indices]

        subgroup_positive = np.any(
            window_targets & window_identities,
            axis=0,
        )
        subgroup_negative = np.any(
            ~window_targets & window_identities,
            axis=0,
        )
        background_positive = np.any(
            window_targets & ~window_identities,
            axis=0,
        )
        background_negative = np.any(
            ~window_targets & ~window_identities,
            axis=0,
        )

        family_counts["subgroup"] += (
            subgroup_positive & subgroup_negative
        )
        family_counts["bpsn"] += (
            background_positive & subgroup_negative
        )
        family_counts["bnsp"] += (
            subgroup_positive & background_negative
        )

    return audited_window_count, family_counts


def audit_role_complete_sampler(
    sampler,
    loader,
    hard_targets,
    identity_masks,
    maximum_windows=1_000,
    throughput_micro_batches=32,
):
    sampler.set_epoch(0)
    packed_order = sampler._build_epoch_order()
    expected_membership = np.arange(
        len(sampler),
        dtype=np.int64,
    )

    if not np.array_equal(
        np.sort(packed_order),
        expected_membership,
    ):
        raise RuntimeError(
            "Role-complete sampler violated exact one-pass epoch membership."
        )

    packed_target_marginal = np.bincount(
        np.asarray(hard_targets, dtype=np.uint8)[packed_order],
        minlength=2,
    )
    original_target_marginal = np.bincount(
        np.asarray(hard_targets, dtype=np.uint8),
        minlength=2,
    )

    if not np.array_equal(
        packed_target_marginal,
        original_target_marginal,
    ):
        raise RuntimeError(
            "Role-complete sampler changed the global target marginal."
        )

    packed_identity_marginal = np.asarray(
        identity_masks,
        dtype=np.bool_,
    )[packed_order].sum(
        axis=0,
        dtype=np.int64,
    )
    original_identity_marginal = np.asarray(
        identity_masks,
        dtype=np.bool_,
    ).sum(
        axis=0,
        dtype=np.int64,
    )

    if not np.array_equal(
        packed_identity_marginal,
        original_identity_marginal,
    ):
        raise RuntimeError(
            "Role-complete sampler changed global identity marginals."
        )

    random_order = np.random.default_rng(
        sampler.seed
    ).permutation(
        len(sampler)
    ).astype(np.int64, copy=False)

    (
        audited_window_count,
        packed_family_counts,
    ) = _window_family_availability(
        order=packed_order,
        hard_targets=hard_targets,
        identity_masks=identity_masks,
        window_size=sampler.window_size,
        maximum_windows=maximum_windows,
    )
    (
        random_window_count,
        random_family_counts,
    ) = _window_family_availability(
        order=random_order,
        hard_targets=hard_targets,
        identity_masks=identity_masks,
        window_size=sampler.window_size,
        maximum_windows=maximum_windows,
    )

    if audited_window_count != random_window_count:
        raise RuntimeError(
            "Packed and random audits examined different window counts."
        )

    for family_name in ("subgroup", "bpsn", "bnsp"):
        if (
            packed_family_counts[family_name].sum()
            <= random_family_counts[family_name].sum()
        ):
            raise RuntimeError(
                f"Role-complete packing did not improve {family_name} "
                "availability."
            )

    packed_total = int(
        sum(
            counts.sum()
            for counts in packed_family_counts.values()
        )
    )
    random_total = int(
        sum(
            counts.sum()
            for counts in random_family_counts.values()
        )
    )

    if packed_total < random_total + audited_window_count:
        raise RuntimeError(
            "Role-complete packing did not materially improve "
            "valid-cell availability."
        )

    throughput_start = time.perf_counter()
    loader_iterator = iter(loader)
    measured_micro_batches = min(
        int(throughput_micro_batches),
        len(loader),
    )

    for _ in range(measured_micro_batches):
        next(loader_iterator)

    throughput_seconds = float(
        time.perf_counter() - throughput_start
    )
    del loader_iterator

    micro_batches_per_second = (
        measured_micro_batches / max(throughput_seconds, 1e-12)
    )

    if (
        not np.isfinite(micro_batches_per_second)
        or micro_batches_per_second <= 0.01
    ):
        raise RuntimeError(
            "Role-complete loader throughput is unsafe."
        )

    audit = {
        "seed": int(sampler.seed),
        "audited_windows": int(audited_window_count),
        "window_size": int(sampler.window_size),
        "exact_one_pass_membership": True,
        "duplicate_indices": 0,
        "target_marginal": original_target_marginal.tolist(),
        "identity_marginal": original_identity_marginal.tolist(),
        "packed_family_availability": {
            family_name: counts.tolist()
            for family_name, counts in packed_family_counts.items()
        },
        "random_family_availability": {
            family_name: counts.tolist()
            for family_name, counts in random_family_counts.items()
        },
        "packed_total_availability": packed_total,
        "random_total_availability": random_total,
        "availability_gain": packed_total - random_total,
        "sampler_build_seconds": float(
            sampler.last_build_seconds
        ),
        "loader_micro_batches_per_second": float(
            micro_batches_per_second
        ),
    }
    print(
        "Role-complete sampler audit: "
        + json.dumps(
            audit,
            sort_keys=True,
        )
    )
    return audit


train_text_array = train_df["comment_text"].to_numpy(
    dtype=object,
    copy=False,
)
valid_text_array = valid_df["comment_text"].to_numpy(
    dtype=object,
    copy=False,
)
test_text_array = test_df["comment_text"].to_numpy(
    dtype=object,
    copy=False,
)

training_dataset = ToxicityTrainingDataset(
    texts=train_text_array,
    text_features=train_text_features,
    soft_targets=train_labels["target_soft"],
    hard_targets=train_labels["target_hard"],
    evaluation_identity_masks=train_labels["evaluation_identity_mask"],
)

loader_generator = torch.Generator()
loader_generator.manual_seed(SEED)

role_complete_window_sampler = RoleCompleteWindowSampler(
    hard_targets=train_labels["target_hard"],
    evaluation_identity_masks=train_labels["evaluation_identity_mask"],
    batch_size=train_batch_size,
    gradient_accumulation_steps=gradient_accumulation_steps,
    seed=SEED,
)

training_loader = DataLoader(
    training_dataset,
    batch_size=train_batch_size,
    shuffle=False,
    sampler=role_complete_window_sampler,
    num_workers=2,
    pin_memory=(device.type == "cuda"),
    persistent_workers=True,
    prefetch_factor=2,
    drop_last=False,
    collate_fn=TrainingCollator(
        tokenizer,
        maximum_sequence_length,
    ),
    worker_init_fn=seed_worker,
    generator=loader_generator,
)

role_sampler_audit = audit_role_complete_sampler(
    sampler=role_complete_window_sampler,
    loader=training_loader,
    hard_targets=train_labels["target_hard"],
    identity_masks=train_labels["evaluation_identity_mask"],
    maximum_windows=1_000,
    throughput_micro_batches=32,
)
model_design_config["role_complete_window_sampler"] = {
    "class_name": role_complete_window_sampler.__class__.__name__,
    "seed": SEED,
    "batch_size": train_batch_size,
    "gradient_accumulation_steps": gradient_accumulation_steps,
    "window_size": role_complete_window_sampler.window_size,
    "identity_rotation": list(EVALUATION_IDENTITY_COLUMNS),
    "role_order": [
        "subgroup_positive",
        "background_positive",
        "subgroup_negative",
        "background_negative",
    ],
    "audit": role_sampler_audit,
}


# ---------------------------------------------------------------------------
# Identical validation/test inference path
# ---------------------------------------------------------------------------
def _autocast_context():
    if device.type != "cuda":
        return nullcontext()

    return torch.autocast(
        device_type="cuda",
        dtype=mixed_precision_dtype,
        enabled=use_mixed_precision,
    )


def _predict_positional_subset(
    texts,
    text_features,
    positional_indices,
):
    positional_indices = np.asarray(
        positional_indices,
        dtype=np.int64,
    ).reshape(-1)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float32)

    inference_dataset = PositionalInferenceDataset(
        texts=texts,
        text_features=text_features,
        positional_indices=positional_indices,
    )

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=2,
        pin_memory=(device.type == "cuda"),
        persistent_workers=True,
        prefetch_factor=2,
        drop_last=False,
        collate_fn=InferenceCollator(
            tokenizer,
            maximum_sequence_length,
        ),
        worker_init_fn=seed_worker,
    )

    was_training = model.training
    model.eval()
    prediction_chunks = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                input_ids = batch["input_ids"].to(
                    device,
                    non_blocking=True,
                )
                attention_mask = batch["attention_mask"].to(
                    device,
                    non_blocking=True,
                )
                numeric_features = batch["text_features"].to(
                    device,
                    non_blocking=True,
                )

                with _autocast_context():
                    logits = model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        text_features=numeric_features,
                    )

                probabilities = torch.sigmoid(logits.float())
                prediction_chunks.append(
                    probabilities.cpu()
                    .numpy()
                    .astype(
                        np.float32,
                        copy=False,
                    )
                )
    finally:
        model.train(was_training)

    predictions = np.concatenate(prediction_chunks)

    if predictions.shape != (len(positional_indices),):
        raise RuntimeError("Inference produced an unexpected prediction shape.")

    if not np.all(np.isfinite(predictions)):
        raise FloatingPointError("Inference produced non-finite predictions.")

    return np.clip(
        predictions,
        0.0,
        1.0,
    )


def predict_validation(positional_indices):
    global latest_validation_diagnostics

    positional_indices = np.asarray(
        positional_indices,
        dtype=np.int64,
    ).reshape(-1)
    predictions = _predict_positional_subset(
        texts=valid_text_array,
        text_features=valid_text_features,
        positional_indices=positional_indices,
    )

    is_full_validation = (
        positional_indices.size == len(valid_text_array)
        and np.array_equal(
            np.sort(positional_indices),
            np.arange(len(valid_text_array), dtype=np.int64),
        )
    )

    if is_full_validation:
        ordered_predictions = np.empty(
            len(valid_text_array),
            dtype=np.float32,
        )
        ordered_predictions[positional_indices] = predictions

        official_metrics = calculate_official_jigsaw_metric(
            target_values=valid_labels["target_soft"],
            prediction_values=ordered_predictions,
            identity_values=valid_labels["evaluation_identity_soft"],
        )
        identity_family_aucs = []

        for identity_row in official_metrics["per_identity"]:
            for family_name in (
                "subgroup",
                "bpsn",
                "bnsp",
            ):
                identity_family_aucs.append(
                    {
                        "identity": identity_row["identity"],
                        "family": family_name,
                        "auc": float(
                            identity_row[f"{family_name}_auc"]
                        ),
                    }
                )

        weakest_six = sorted(
            identity_family_aucs,
            key=lambda row: (
                row["auc"],
                EVALUATION_IDENTITY_COLUMNS.index(row["identity"]),
                row["family"],
            ),
        )[:6]

        latest_validation_diagnostics = {
            "optimizer_updates": int(optimizer_updates),
            "group_dro": criterion.group_dro_snapshot(
                EVALUATION_IDENTITY_COLUMNS
            ),
            "official_composite": float(official_metrics["score"]),
            "overall_auc": float(official_metrics["overall_auc"]),
            "subgroup_power_mean": float(
                official_metrics["subgroup_power_mean"]
            ),
            "bpsn_power_mean": float(official_metrics["bpsn_power_mean"]),
            "bnsp_power_mean": float(official_metrics["bnsp_power_mean"]),
            "weakest_six_identity_family_aucs": weakest_six,
        }
        validation_diagnostics_history.append(
            latest_validation_diagnostics
        )
        print(
            "Validation diagnostics: "
            + json.dumps(
                latest_validation_diagnostics,
                sort_keys=True,
            )
        )

    return predictions


def predict_test(positional_indices):
    return _predict_positional_subset(
        texts=test_text_array,
        text_features=test_text_features,
        positional_indices=positional_indices,
    )


# ---------------------------------------------------------------------------
# Reproducible checkpoint callbacks
# ---------------------------------------------------------------------------
optimizer_updates = 0
latest_validation_diagnostics = {}
validation_diagnostics_history = []
controller_smoke_test_passed = False
controller_smoke_test_summary = {}
controller_cumulative_availability = {
    family_name: np.zeros(
        len(EVALUATION_IDENTITY_COLUMNS),
        dtype=np.int64,
    )
    for family_name in criterion.group_dro_family_names
}


def log_controller_activity(successful_update):
    global controller_smoke_test_passed
    global controller_smoke_test_summary

    initial_ema_loss = float(math.log(2.0))
    family_telemetry = {}
    any_ema_moved = False
    any_weight_nonuniform = False

    for family_name in criterion.group_dro_family_names:
        (
            ema_losses,
            persistent_weights,
            _,
            _,
            last_availability,
        ) = criterion._family_buffers(family_name)

        current_availability = (
            last_availability.detach()
            .cpu()
            .numpy()
            .astype(np.int64, copy=False)
        )
        controller_cumulative_availability[
            family_name
        ] += current_availability

        ema_values = (
            ema_losses.detach()
            .float()
            .cpu()
            .numpy()
            .astype(np.float64, copy=False)
        )
        weight_values = (
            persistent_weights.detach()
            .float()
            .cpu()
            .numpy()
            .astype(np.float64, copy=False)
        )
        ema_changes = ema_values - initial_ema_loss
        weight_entropy = float(
            -np.sum(
                weight_values
                * np.log(np.clip(weight_values, 1e-12, None))
            )
        )

        family_ema_moved = bool(
            np.any(np.abs(ema_changes) > 1e-6)
        )
        family_weight_nonuniform = bool(
            np.ptp(weight_values) > 1e-6
        )
        any_ema_moved = any_ema_moved or family_ema_moved
        any_weight_nonuniform = (
            any_weight_nonuniform
            or family_weight_nonuniform
        )

        family_telemetry[family_name] = {
            "current_availability": current_availability.tolist(),
            "cumulative_availability_counts": (
                controller_cumulative_availability[
                    family_name
                ].tolist()
            ),
            "ema_changes_from_log2": ema_changes.tolist(),
            "weights": weight_values.tolist(),
            "weight_entropy": weight_entropy,
            "ema_moved": family_ema_moved,
            "weights_nonuniform": family_weight_nonuniform,
        }

    controller_smoke_test_summary = {
        "successful_update": int(successful_update),
        "queue_occupancy": int(
            criterion._queue_filled.detach().cpu().item()
        ),
        "queue_capacity": int(criterion.queue_size),
        "families": family_telemetry,
        "any_ema_moved": any_ema_moved,
        "any_weight_nonuniform": any_weight_nonuniform,
    }

    if successful_update in (1, 25, 50, 100, 150, 200):
        print(
            "Controller activity: "
            + json.dumps(
                controller_smoke_test_summary,
                sort_keys=True,
            )
        )

    if successful_update == 200:
        controller_smoke_test_passed = (
            any_ema_moved and any_weight_nonuniform
        )

        if not controller_smoke_test_passed:
            raise RuntimeError(
                "Role-complete controller smoke test failed: "
                "EMAs or family weights remained inactive."
            )


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    checkpoint_payload = {
        "model_state_dict": model.state_dict(),
        "criterion_state_dict": criterion.state_dict(),
        "architecture_config": dict(model.architecture_config),
        "model_design_config": dict(model_design_config),
        "group_dro_config": dict(criterion.group_dro_config),
        "latest_validation_diagnostics": dict(latest_validation_diagnostics),
        "processing_metadata": dict(prepared_data["metadata"]),
        "maximum_sequence_length": (maximum_sequence_length),
        "numeric_feature_names": list(TEXT_FEATURE_NAMES),
        "evaluation_identity_columns": list(EVALUATION_IDENTITY_COLUMNS),
        "optimizer_updates": int(optimizer_updates),
        "prediction_postprocessing": ("sigmoid_clip_0_1"),
    }

    temporary_model_path = checkpoint_directory / "model_state.pt.tmp"
    final_model_path = checkpoint_directory / "model_state.pt"

    torch.save(
        checkpoint_payload,
        temporary_model_path,
    )
    os.replace(
        temporary_model_path,
        final_model_path,
    )

    tokenizer_directory = checkpoint_directory / "tokenizer"
    tokenizer.save_pretrained(tokenizer_directory)

    joblib.dump(
        text_feature_scaler,
        checkpoint_directory / "text_feature_scaler.joblib",
    )

    checkpoint_manifest = {
        "model_class": model.__class__.__name__,
        "model_id": model_id,
        "maximum_sequence_length": (maximum_sequence_length),
        "numeric_feature_count": len(TEXT_FEATURE_NAMES),
        "numeric_feature_names": list(TEXT_FEATURE_NAMES),
        "identity_threshold": 0.5,
        "target_metric_threshold": 0.5,
        "official_metric_power": -5,
        "official_metric_component_weights": [
            0.25,
            0.25,
            0.25,
            0.25,
        ],
        "optimizer_updates": int(optimizer_updates),
        "group_dro_config": dict(criterion.group_dro_config),
        "latest_validation_diagnostics": dict(latest_validation_diagnostics),
    }

    with open(
        checkpoint_directory / "checkpoint_manifest.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            checkpoint_manifest,
            file,
            indent=2,
            default=str,
        )


def load_checkpoint(directory):
    global tokenizer
    global text_feature_scaler
    global latest_validation_diagnostics

    checkpoint_directory = Path(directory)
    checkpoint_path = checkpoint_directory / "model_state.pt"

    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Missing checkpoint: {checkpoint_path}")

    tokenizer_directory = checkpoint_directory / "tokenizer"
    scaler_path = checkpoint_directory / "text_feature_scaler.joblib"

    if not tokenizer_directory.exists():
        raise FileNotFoundError(
            f"Missing checkpoint tokenizer: " f"{tokenizer_directory}"
        )

    if not scaler_path.exists():
        raise FileNotFoundError(f"Missing checkpoint scaler: {scaler_path}")

    was_training = model.training

    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )

    saved_maximum_length = int(
        checkpoint_payload.get(
            "maximum_sequence_length",
            maximum_sequence_length,
        )
    )

    if saved_maximum_length != maximum_sequence_length:
        raise ValueError("Checkpoint sequence length does not match inference state.")

    saved_feature_names = checkpoint_payload.get(
        "numeric_feature_names",
        list(TEXT_FEATURE_NAMES),
    )

    if list(saved_feature_names) != list(TEXT_FEATURE_NAMES):
        raise ValueError("Checkpoint numeric feature order does not match.")

    saved_identity_columns = checkpoint_payload.get(
        "evaluation_identity_columns",
        list(EVALUATION_IDENTITY_COLUMNS),
    )

    if list(saved_identity_columns) != list(EVALUATION_IDENTITY_COLUMNS):
        raise ValueError("Checkpoint identity-column order does not match.")

    model.load_state_dict(
        checkpoint_payload["model_state_dict"],
        strict=True,
    )

    if "criterion_state_dict" in checkpoint_payload:
        criterion.load_state_dict(
            checkpoint_payload["criterion_state_dict"],
            strict=True,
        )

    latest_validation_diagnostics = dict(
        checkpoint_payload.get(
            "latest_validation_diagnostics",
            {},
        )
    )

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_directory)
    text_feature_scaler = joblib.load(scaler_path)

    if int(text_feature_scaler.n_features_in_) != len(TEXT_FEATURE_NAMES):
        raise ValueError("Checkpoint scaler feature count does not match.")

    model.to(device)
    model.train(was_training)

    del checkpoint_payload
    gc.collect()

    if device.type == "cuda":
        torch.cuda.empty_cache()


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())


# ---------------------------------------------------------------------------
# Mixed-precision training with cooperative runtime stopping
# ---------------------------------------------------------------------------
stop_training = False

for epoch_index in range(maximum_epochs):
    role_complete_window_sampler.set_epoch(epoch_index)
    model.train()
    criterion.train()

    epoch_loss_sum = 0.0
    epoch_micro_batches = 0
    accumulated_micro_batches = 0

    for batch in training_loader:
        input_ids = batch["input_ids"].to(
            device,
            non_blocking=True,
        )
        attention_mask = batch["attention_mask"].to(
            device,
            non_blocking=True,
        )
        numeric_features = batch["text_features"].to(
            device,
            non_blocking=True,
        )
        soft_targets = batch["soft_targets"].to(
            device,
            non_blocking=True,
        )
        hard_targets = batch["hard_targets"].to(
            device,
            non_blocking=True,
        )
        identity_masks = batch["evaluation_identity_masks"].to(
            device,
            non_blocking=True,
        )

        with _autocast_context():
            logits = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                text_features=numeric_features,
            )

            loss = criterion(
                logits=logits,
                soft_targets=soft_targets,
                hard_targets=hard_targets,
                evaluation_identity_masks=identity_masks,
                update_queue=True,
            )

        if not torch.isfinite(loss):
            raise FloatingPointError("Non-finite training loss encountered.")

        unscaled_loss_value = float(loss.detach().cpu())
        scaled_loss = loss / gradient_accumulation_steps

        grad_scaler.scale(scaled_loss).backward()

        epoch_loss_sum += unscaled_loss_value
        epoch_micro_batches += 1
        accumulated_micro_batches += 1

        if accumulated_micro_batches < gradient_accumulation_steps:
            continue

        grad_scaler.unscale_(optimizer)

        clip_grad_norm_(
            model.parameters(),
            max_norm=maximum_gradient_norm,
        )

        scale_before_step = (
            float(grad_scaler.get_scale()) if grad_scaler.is_enabled() else 1.0
        )

        grad_scaler.step(optimizer)
        grad_scaler.update()

        scale_after_step = (
            float(grad_scaler.get_scale()) if grad_scaler.is_enabled() else 1.0
        )

        optimizer.zero_grad(set_to_none=True)
        accumulated_micro_batches = 0

        optimizer_step_was_executed = (
            not grad_scaler.is_enabled() or scale_after_step >= scale_before_step
        )

        if not optimizer_step_was_executed:
            criterion.discard_group_dro_statistics()
            continue

        criterion.commit_group_dro_statistics()
        scheduler.step()
        optimizer_updates += 1
        log_controller_activity(optimizer_updates)

        if session.step():
            stop_training = True
            break

    if not stop_training and accumulated_micro_batches > 0:
        grad_scaler.unscale_(optimizer)

        gradient_rescale = float(gradient_accumulation_steps) / float(
            accumulated_micro_batches
        )

        for parameter in model.parameters():
            if parameter.grad is not None:
                parameter.grad.mul_(gradient_rescale)

        clip_grad_norm_(
            model.parameters(),
            max_norm=maximum_gradient_norm,
        )

        scale_before_step = (
            float(grad_scaler.get_scale()) if grad_scaler.is_enabled() else 1.0
        )

        grad_scaler.step(optimizer)
        grad_scaler.update()

        scale_after_step = (
            float(grad_scaler.get_scale()) if grad_scaler.is_enabled() else 1.0
        )

        optimizer.zero_grad(set_to_none=True)

        optimizer_step_was_executed = (
            not grad_scaler.is_enabled() or scale_after_step >= scale_before_step
        )

        if optimizer_step_was_executed:
            criterion.commit_group_dro_statistics()
            scheduler.step()
            optimizer_updates += 1
            log_controller_activity(optimizer_updates)

            if session.step():
                stop_training = True
        else:
            criterion.discard_group_dro_statistics()

    mean_epoch_loss = epoch_loss_sum / max(epoch_micro_batches, 1)

    best_score_text = (
        "pending"
        if session.best_validation_score is None
        else (f"{float(session.best_validation_score):.6f}")
    )

    print(
        f"Epoch {epoch_index + 1} | "
        f"optimizer_steps={optimizer_updates} | "
        f"loss={mean_epoch_loss:.6f} | "
        f"best_official_score={best_score_text}"
    )

    if stop_training:
        break


del training_loader, training_dataset
gc.collect()

if device.type == "cuda":
    torch.cuda.empty_cache()

result = session.finish()
score = float(result["best_validation_score"])
baseline_validation_score = 0.9328472510315861
baseline_overall_auc = 0.9644048891050647
best_overall_auc = float(
    latest_validation_diagnostics.get(
        "overall_auc",
        np.nan,
    )
)
composite_improved = score > baseline_validation_score
overall_auc_drop_exceeded = (
    np.isfinite(best_overall_auc)
    and (
        baseline_overall_auc - best_overall_auc
        > 0.003
    )
)
rejection_reasons = []

if not composite_improved:
    rejection_reasons.append(
        "no_official_composite_improvement"
    )

if not controller_smoke_test_passed:
    rejection_reasons.append(
        "controller_inactive_within_200_updates"
    )

if overall_auc_drop_exceeded and not composite_improved:
    rejection_reasons.append(
        "overall_auc_drop_without_compensating_composite_gain"
    )

refinement_accepted = not rejection_reasons
print(f"Final Validation Score: {score}")
print(f"Final Validation Overall AUC: {best_overall_auc}")
print(
    "Role-complete sampler refinement decision: "
    + (
        "accepted"
        if refinement_accepted
        else "rejected_" + "_and_".join(rejection_reasons)
    )
)
