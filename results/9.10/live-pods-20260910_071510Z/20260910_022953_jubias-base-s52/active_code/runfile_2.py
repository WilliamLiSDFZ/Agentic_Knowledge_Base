import os
os.sched_setaffinity(0, {68, 71})
import json
import math
import os
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
import random
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from joblib import dump
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

os.environ["TOKENIZERS_PARALLELISM"] = "false"

RANDOM_STATE = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
PROCESSED_DIR = WORKING_DIR / "processed"
CHECKPOINT_DIR = WORKING_DIR / "checkpoints"
SUBMISSION_DIR = Path("./submission")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

# DeBERTa attention memory grows rapidly with sequence length.  These defaults
# retain a 32-example effective optimization batch while fitting shared GPUs.
MAX_SEQUENCE_LENGTH = int(os.environ.get("MAX_SEQUENCE_LENGTH", "128"))
TRAIN_BATCH_SIZE = int(os.environ.get("TRAIN_BATCH_SIZE", "8"))
INFERENCE_BATCH_SIZE = int(os.environ.get("INFERENCE_BATCH_SIZE", "16"))
GRADIENT_ACCUMULATION_STEPS = int(os.environ.get("GRADIENT_ACCUMULATION_STEPS", "4"))
NUM_EPOCHS = int(os.environ.get("NUM_EPOCHS", "1"))
NUM_WORKERS = 2
EARLY_STOPPING_PATIENCE = int(os.environ.get("EARLY_STOPPING_PATIENCE", "1"))

MODEL_NAME = os.environ.get("MODEL_NAME", "microsoft/deberta-v3-base")
BEST_CHECKPOINT_PATH = CHECKPOINT_DIR / "best_deberta_v3_base_bias_aware_ranker.pt"

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

TOXICITY_SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

TRAIN_COLUMNS = (
    [
        "id",
        "comment_text",
        "target",
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + IDENTITY_COLUMNS
    + TOXICITY_SUBTYPE_COLUMNS
)

NUM_TOXICITY_SUBTYPES = len(TOXICITY_SUBTYPE_COLUMNS)
DEFAULT_NUMERIC_FEATURE_DIM = 13

random.seed(RANDOM_STATE)
np.random.seed(RANDOM_STATE)
torch.manual_seed(RANDOM_STATE)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_STATE)

train_path = INPUT_DIR / "train.csv"
test_path = INPUT_DIR / "test.csv"
sample_submission_path = INPUT_DIR / "sample_submission.csv"

train_raw = pd.read_csv(
    train_path,
    usecols=lambda column: column in TRAIN_COLUMNS,
    low_memory=False,
)
test_raw = pd.read_csv(
    test_path,
    usecols=["id", "comment_text"],
    low_memory=False,
)
sample_submission = pd.read_csv(
    sample_submission_path,
    usecols=["id", "prediction"],
)

if not test_raw["id"].is_unique:
    raise ValueError("Test ids must be unique to guarantee submission-order alignment.")

if not sample_submission["id"].is_unique:
    raise ValueError("Sample-submission ids must be unique.")

test_raw = (
    test_raw.set_index("id").loc[sample_submission["id"].to_numpy()].reset_index()
)

if len(test_raw) != len(sample_submission):
    raise ValueError("Test/sample-submission row count mismatch after id alignment.")

raw_comment_for_split = train_raw["comment_text"].fillna("").astype(str)
duplicate_group_ids = pd.factorize(raw_comment_for_split, sort=False)[0]

official_identity_values = train_raw[OFFICIAL_IDENTITY_COLUMNS].fillna(0.0)
official_identity_present = official_identity_values.ge(0.5).to_numpy()

primary_identity = np.where(
    official_identity_present.any(axis=1),
    official_identity_present.argmax(axis=1) + 1,
    0,
).astype(np.int16)

toxicity_binary = train_raw["target"].ge(0.5).astype(np.int8).to_numpy()
split_strata = (
    toxicity_binary * (len(OFFICIAL_IDENTITY_COLUMNS) + 1) + primary_identity
).astype(np.int16)

try:
    min_stratum_size = int(pd.Series(split_strata).value_counts().min())
    n_splits = max(2, min(10, min_stratum_size))

    split_iterator = StratifiedGroupKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=RANDOM_STATE,
    ).split(
        X=train_raw["id"].to_numpy(),
        y=split_strata,
        groups=duplicate_group_ids,
    )

    _, validation_indices = next(split_iterator)
    training_mask = np.ones(len(train_raw), dtype=bool)
    training_mask[validation_indices] = False

except ValueError:
    fallback_splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=0.10,
        random_state=RANDOM_STATE,
    )
    training_indices, validation_indices = next(
        fallback_splitter.split(
            X=train_raw["id"].to_numpy(),
            y=split_strata,
            groups=duplicate_group_ids,
        )
    )
    training_mask = np.zeros(len(train_raw), dtype=bool)
    training_mask[training_indices] = True

train_df = train_raw.loc[training_mask].copy().reset_index(drop=True)
valid_df = train_raw.loc[~training_mask].copy().reset_index(drop=True)
test_df = test_raw.copy().reset_index(drop=True)

del train_raw
del test_raw
del raw_comment_for_split
del duplicate_group_ids
del official_identity_values
del official_identity_present
del primary_identity
del toxicity_binary
del split_strata

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
HTML_PATTERN = re.compile(r"<[^>\n]{1,100}>")
REPEATED_PUNCTUATION_PATTERN = re.compile(r"([!?.,])\1{3,}")
ZERO_WIDTH_PATTERN = re.compile(r"[\u200b-\u200d\ufeff]")


def canonicalize_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = unicodedata.normalize("NFKC", text)
    text = ZERO_WIDTH_PATTERN.sub("", text)
    text = URL_PATTERN.sub(" URL ", text)
    text = EMAIL_PATTERN.sub(" EMAIL ", text)
    text = HTML_PATTERN.sub(" ", text)
    text = REPEATED_PUNCTUATION_PATTERN.sub(r"\1\1\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if text else "[EMPTY]"


def add_text_features(frame):
    source_text = frame["comment_text"].fillna("").astype(str)
    cleaned_text = source_text.map(canonicalize_comment)

    char_count = source_text.str.len().clip(lower=0)
    letter_count = source_text.str.count(r"[A-Za-z]")
    uppercase_count = source_text.str.count(r"[A-Z]")
    word_count = cleaned_text.str.count(r"\S+")

    frame["model_text"] = cleaned_text
    frame["numeric_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["numeric_log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["numeric_uppercase_ratio"] = (
        uppercase_count / letter_count.clip(lower=1)
    ).astype(np.float32)
    frame["numeric_log_exclamation_count"] = np.log1p(
        source_text.str.count("!")
    ).astype(np.float32)
    frame["numeric_log_question_count"] = np.log1p(source_text.str.count(r"\?")).astype(
        np.float32
    )
    frame["numeric_log_punctuation_count"] = np.log1p(
        source_text.str.count(r"[!?,.;:]")
    ).astype(np.float32)
    frame["numeric_log_digit_count"] = np.log1p(source_text.str.count(r"\d")).astype(
        np.float32
    )
    frame["numeric_log_newline_count"] = np.log1p(
        source_text.str.count(r"[\r\n]")
    ).astype(np.float32)
    frame["numeric_url_present"] = source_text.str.contains(
        URL_PATTERN,
        na=False,
    ).astype(np.float32)
    frame["numeric_email_present"] = source_text.str.contains(
        EMAIL_PATTERN,
        na=False,
    ).astype(np.float32)
    frame["numeric_quote_present"] = source_text.str.contains(
        r"""["']""",
        regex=True,
        na=False,
    ).astype(np.float32)
    frame["numeric_all_caps_word_count"] = np.log1p(
        source_text.str.count(r"\b[A-Z]{3,}\b")
    ).astype(np.float32)
    frame["numeric_elongated_token_count"] = np.log1p(
        source_text.str.count(r"(?i)\b\w*(.)\1{2,}\w*\b")
    ).astype(np.float32)

    return frame


def add_training_labels(frame):
    identity_values = frame[IDENTITY_COLUMNS].fillna(0.0)
    official_values = frame[OFFICIAL_IDENTITY_COLUMNS].fillna(0.0)

    identity_present = identity_values.ge(0.5).to_numpy()
    official_present = official_values.ge(0.5).to_numpy()

    frame["target_binary"] = frame["target"].ge(0.5).astype(np.int8)
    frame["identity_any"] = identity_present.any(axis=1).astype(np.int8)
    frame["identity_label_available"] = (
        frame[IDENTITY_COLUMNS].notna().any(axis=1).astype(np.int8)
    )
    frame["official_identity_any"] = official_present.any(axis=1).astype(np.int8)
    frame["official_identity_primary"] = np.where(
        official_present.any(axis=1),
        official_present.argmax(axis=1) + 1,
        0,
    ).astype(np.int8)
    frame["subgroup_max_fraction"] = identity_values.max(axis=1).astype(np.float32)
    frame["label_confidence_weight"] = np.sqrt(
        frame["toxicity_annotator_count"].clip(lower=1)
    ).astype(np.float32)

    return frame


train_df = add_training_labels(add_text_features(train_df))
valid_df = add_training_labels(add_text_features(valid_df))
test_df = add_text_features(test_df)

numeric_feature_columns = [
    column for column in train_df.columns if column.startswith("numeric_")
]

numeric_scaler = StandardScaler()
train_df[numeric_feature_columns] = numeric_scaler.fit_transform(
    train_df[numeric_feature_columns]
).astype(np.float32)
valid_df[numeric_feature_columns] = numeric_scaler.transform(
    valid_df[numeric_feature_columns]
).astype(np.float32)
test_df[numeric_feature_columns] = numeric_scaler.transform(
    test_df[numeric_feature_columns]
).astype(np.float32)

dump(numeric_scaler, PROCESSED_DIR / "numeric_feature_scaler.joblib")

feature_schema = {
    "text_column": "model_text",
    "target_column": "target",
    "binary_target_column": "target_binary",
    "numeric_feature_columns": numeric_feature_columns,
    "identity_columns": IDENTITY_COLUMNS,
    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    "toxicity_subtype_columns": TOXICITY_SUBTYPE_COLUMNS,
    "split_strategy": "StratifiedGroupKFold on exact raw-comment duplicate groups",
    "random_state": RANDOM_STATE,
    "submission_id_order_path": str(sample_submission_path),
}

with open(PROCESSED_DIR / "feature_schema.json", "w", encoding="utf-8") as schema_file:
    json.dump(feature_schema, schema_file, indent=2)

# The base checkpoint preserves DeBERTa-v3's pretrained language representation
# while avoiding the large model's attention-activation OOM on shared GPUs.
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
pretrained_model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2,
)


class DebertaBiasAwareRanker(nn.Module):
    def __init__(self, pretrained_sequence_model, numeric_feature_dim):
        super().__init__()

        self.encoder = pretrained_sequence_model.deberta
        hidden_size = self.encoder.config.hidden_size
        dropout_probability = float(
            getattr(pretrained_sequence_model.config, "classifier_dropout", 0.15)
            or 0.15
        )

        self.text_projection = nn.Sequential(
            nn.LayerNorm(hidden_size * 2),
            nn.Linear(hidden_size * 2, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.numeric_projection = nn.Sequential(
            nn.LayerNorm(numeric_feature_dim),
            nn.Linear(numeric_feature_dim, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.fusion_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )
        self.fusion_norm = nn.LayerNorm(hidden_size)
        self.fusion_dropout = nn.Dropout(dropout_probability)

        self.toxicity_head = nn.Linear(hidden_size, 1)
        self.subtype_head = nn.Linear(hidden_size, NUM_TOXICITY_SUBTYPES)

        for module in (
            self.text_projection,
            self.numeric_projection,
            self.fusion_gate,
            self.toxicity_head,
            self.subtype_head,
        ):
            for layer in module.modules():
                if isinstance(layer, nn.Linear):
                    nn.init.xavier_uniform_(layer.weight)
                    if layer.bias is not None:
                        nn.init.zeros_(layer.bias)

    @staticmethod
    def masked_mean_pool(hidden_states, attention_mask):
        if attention_mask is None:
            return hidden_states.mean(dim=1)

        mask = attention_mask.unsqueeze(-1).to(dtype=hidden_states.dtype)
        denominator = mask.sum(dim=1).clamp_min(1.0)
        return (hidden_states * mask).sum(dim=1) / denominator

    def forward(
        self,
        input_ids,
        attention_mask=None,
        token_type_ids=None,
        numeric_features=None,
    ):
        encoder_inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }

        if token_type_ids is not None:
            encoder_inputs["token_type_ids"] = token_type_ids

        encoder_outputs = self.encoder(**encoder_inputs)
        hidden_states = encoder_outputs.last_hidden_state

        cls_embedding = hidden_states[:, 0]
        mean_embedding = self.masked_mean_pool(hidden_states, attention_mask)

        text_embedding = self.text_projection(
            torch.cat([cls_embedding, mean_embedding], dim=-1)
        )

        if numeric_features is None:
            numeric_embedding = torch.zeros_like(text_embedding)
        else:
            numeric_embedding = self.numeric_projection(
                numeric_features.to(dtype=text_embedding.dtype)
            )

        fusion_gate = self.fusion_gate(
            torch.cat([text_embedding, numeric_embedding], dim=-1)
        )
        fused_embedding = self.fusion_norm(
            text_embedding + fusion_gate * numeric_embedding
        )
        fused_embedding = self.fusion_dropout(fused_embedding)

        return {
            "toxicity_logit": self.toxicity_head(fused_embedding).squeeze(-1),
            "subtype_logits": self.subtype_head(fused_embedding),
            "embedding": fused_embedding,
        }


class OfficialBiasAwareRankingLoss(nn.Module):
    def __init__(
        self,
        toxicity_weight=1.0,
        subtype_weight=0.20,
        bias_ranking_weight=0.75,
        ranking_temperature=0.35,
        hard_group_power=4.0,
    ):
        super().__init__()
        self.toxicity_weight = toxicity_weight
        self.subtype_weight = subtype_weight
        self.bias_ranking_weight = bias_ranking_weight
        self.ranking_temperature = ranking_temperature
        self.hard_group_power = hard_group_power

    def _pairwise_rank_loss(self, positive_logits, negative_logits):
        if positive_logits.numel() == 0 or negative_logits.numel() == 0:
            return None

        score_differences = (
            positive_logits[:, None] - negative_logits[None, :]
        ) / self.ranking_temperature

        return F.softplus(-score_differences).mean()

    def _bias_rank_loss(
        self,
        toxicity_logits,
        binary_targets,
        identity_labels,
        identity_label_available,
    ):
        if identity_labels is None or identity_label_available is None:
            return toxicity_logits.sum() * 0.0

        binary_targets = binary_targets.bool()
        identity_label_available = identity_label_available.bool()
        per_metric_losses = []

        for identity_index in range(identity_labels.shape[1]):
            annotated = identity_label_available & torch.isfinite(
                identity_labels[:, identity_index]
            )
            subgroup = annotated & (identity_labels[:, identity_index] >= 0.5)
            background = annotated & ~subgroup

            subgroup_positive = toxicity_logits[subgroup & binary_targets]
            subgroup_negative = toxicity_logits[subgroup & ~binary_targets]
            background_positive = toxicity_logits[background & binary_targets]
            background_negative = toxicity_logits[background & ~binary_targets]

            subgroup_auc_loss = self._pairwise_rank_loss(
                subgroup_positive,
                subgroup_negative,
            )
            bpsn_auc_loss = self._pairwise_rank_loss(
                background_positive,
                subgroup_negative,
            )
            bnsp_auc_loss = self._pairwise_rank_loss(
                subgroup_positive,
                background_negative,
            )

            for metric_loss in (
                subgroup_auc_loss,
                bpsn_auc_loss,
                bnsp_auc_loss,
            ):
                if metric_loss is not None:
                    per_metric_losses.append(metric_loss)

        if not per_metric_losses:
            return toxicity_logits.sum() * 0.0

        stacked_losses = torch.stack(per_metric_losses)
        return (stacked_losses.pow(self.hard_group_power).mean()).pow(
            1.0 / self.hard_group_power
        )

    def forward(
        self,
        model_outputs,
        toxicity_targets,
        toxicity_annotator_counts=None,
        subtype_targets=None,
        identity_labels=None,
        identity_label_available=None,
    ):
        toxicity_logits = model_outputs["toxicity_logit"]
        toxicity_targets = toxicity_targets.to(
            device=toxicity_logits.device,
            dtype=toxicity_logits.dtype,
        ).clamp(0.0, 1.0)

        toxicity_loss_per_example = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
            reduction="none",
        )

        if toxicity_annotator_counts is not None:
            confidence_weights = torch.sqrt(
                toxicity_annotator_counts.to(
                    device=toxicity_logits.device,
                    dtype=toxicity_logits.dtype,
                ).clamp(min=1.0, max=25.0)
            )
            confidence_weights = (
                confidence_weights / confidence_weights.mean().clamp_min(1e-6)
            )
            toxicity_loss = (toxicity_loss_per_example * confidence_weights).mean()
        else:
            toxicity_loss = toxicity_loss_per_example.mean()

        subtype_loss = toxicity_logits.sum() * 0.0
        if subtype_targets is not None:
            subtype_targets = subtype_targets.to(
                device=toxicity_logits.device,
                dtype=toxicity_logits.dtype,
            )
            valid_subtypes = torch.isfinite(subtype_targets)

            if valid_subtypes.any():
                subtype_loss_values = F.binary_cross_entropy_with_logits(
                    model_outputs["subtype_logits"],
                    torch.nan_to_num(subtype_targets, nan=0.0).clamp(0.0, 1.0),
                    reduction="none",
                )
                subtype_loss = subtype_loss_values[valid_subtypes].mean()

        binary_targets = toxicity_targets >= 0.5
        bias_ranking_loss = self._bias_rank_loss(
            toxicity_logits=toxicity_logits,
            binary_targets=binary_targets,
            identity_labels=identity_labels,
            identity_label_available=identity_label_available,
        )

        total_loss = (
            self.toxicity_weight * toxicity_loss
            + self.subtype_weight * subtype_loss
            + self.bias_ranking_weight * bias_ranking_loss
        )

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "subtype_loss": subtype_loss.detach(),
            "bias_ranking_loss": bias_ranking_loss.detach(),
        }


model = DebertaBiasAwareRanker(
    pretrained_sequence_model=pretrained_model,
    numeric_feature_dim=len(numeric_feature_columns),
)

criterion = OfficialBiasAwareRankingLoss(
    toxicity_weight=1.0,
    subtype_weight=0.20,
    bias_ranking_weight=0.75,
    ranking_temperature=0.35,
    hard_group_power=4.0,
)

backbone_learning_rate = 8e-6
head_learning_rate = 1.5e-4
weight_decay = 0.01
no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")

optimizer_parameter_groups = [
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if name.startswith("encoder.")
            and parameter.requires_grad
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": backbone_learning_rate,
        "weight_decay": weight_decay,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if name.startswith("encoder.")
            and parameter.requires_grad
            and any(term in name for term in no_decay_terms)
        ],
        "lr": backbone_learning_rate,
        "weight_decay": 0.0,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if not name.startswith("encoder.")
            and parameter.requires_grad
            and not any(term in name for term in no_decay_terms)
        ],
        "lr": head_learning_rate,
        "weight_decay": weight_decay,
    },
    {
        "params": [
            parameter
            for name, parameter in model.named_parameters()
            if not name.startswith("encoder.")
            and parameter.requires_grad
            and any(term in name for term in no_decay_terms)
        ],
        "lr": head_learning_rate,
        "weight_decay": 0.0,
    },
]

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda_amp = device.type == "cuda"

try:
    if hasattr(model.encoder, "gradient_checkpointing_enable"):
        # DeBERTa shares relative-position tensors across checkpointed layers.
        # Non-reentrant checkpointing retains the required autograd connections.
        model.encoder.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )
except (AttributeError, TypeError):
    # If checkpointing is unavailable, train normally rather than falling back
    # to the unsafe default re-entrant implementation.
    pass

model.to(device)


class ToxicityDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.texts = frame["model_text"].fillna("").astype(str).tolist()
        self.numeric_features = frame[numeric_feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.include_labels = include_labels

        if include_labels:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.annotator_counts = frame["toxicity_annotator_count"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.subtype_targets = frame[TOXICITY_SUBTYPE_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_labels = frame[OFFICIAL_IDENTITY_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_label_available = frame["identity_label_available"].to_numpy(
                dtype=np.float32, copy=True
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {
            "text": self.texts[index],
            "numeric_features": self.numeric_features[index],
        }

        if self.include_labels:
            item.update(
                {
                    "target": self.targets[index],
                    "annotator_count": self.annotator_counts[index],
                    "subtype_targets": self.subtype_targets[index],
                    "identity_labels": self.identity_labels[index],
                    "identity_label_available": self.identity_label_available[index],
                }
            )

        return item


def toxicity_collate(batch):
    encoded = tokenizer(
        [row["text"] for row in batch],
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        padding=True,
        return_tensors="pt",
    )

    output = {
        "inputs": {key: value for key, value in encoded.items()},
        "numeric_features": torch.as_tensor(
            np.stack([row["numeric_features"] for row in batch]),
            dtype=torch.float32,
        ),
    }

    if "target" in batch[0]:
        output.update(
            {
                "target": torch.as_tensor(
                    [row["target"] for row in batch],
                    dtype=torch.float32,
                ),
                "annotator_count": torch.as_tensor(
                    [row["annotator_count"] for row in batch],
                    dtype=torch.float32,
                ),
                "subtype_targets": torch.as_tensor(
                    np.stack([row["subtype_targets"] for row in batch]),
                    dtype=torch.float32,
                ),
                "identity_labels": torch.as_tensor(
                    np.stack([row["identity_labels"] for row in batch]),
                    dtype=torch.float32,
                ),
                "identity_label_available": torch.as_tensor(
                    [row["identity_label_available"] for row in batch],
                    dtype=torch.float32,
                ),
            }
        )

    return output


def seed_worker(worker_id):
    worker_seed = RANDOM_STATE + worker_id
    random.seed(worker_seed)
    np.random.seed(worker_seed)


train_dataset = ToxicityDataset(train_df, include_labels=True)
valid_dataset = ToxicityDataset(valid_df, include_labels=True)
test_dataset = ToxicityDataset(test_df, include_labels=False)

loader_generator = torch.Generator()
loader_generator.manual_seed(RANDOM_STATE)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=use_cuda_amp,
    persistent_workers=True,
    prefetch_factor=2,
    worker_init_fn=seed_worker,
    generator=loader_generator,
    collate_fn=toxicity_collate,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=INFERENCE_BATCH_SIZE,
    shuffle=False,
    num_workers=NUM_WORKERS,
    pin_memory=use_cuda_amp,
    persistent_workers=True,
    prefetch_factor=2,
    worker_init_fn=seed_worker,
    collate_fn=toxicity_collate,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=INFERENCE_BATCH_SIZE,
    shuffle=False,
    num_workers=NUM_WORKERS,
    pin_memory=use_cuda_amp,
    persistent_workers=True,
    prefetch_factor=2,
    worker_init_fn=seed_worker,
    collate_fn=toxicity_collate,
)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_update_steps = max(1, updates_per_epoch * NUM_EPOCHS)
warmup_steps = max(1, int(0.03 * total_update_steps))


def learning_rate_multiplier(step_number):
    completed_steps = step_number + 1

    if completed_steps <= warmup_steps:
        return float(completed_steps) / float(warmup_steps)

    progress = (completed_steps - warmup_steps) / max(
        1,
        total_update_steps - warmup_steps,
    )
    progress = min(1.0, max(0.0, progress))

    return 0.5 * (1.0 + math.cos(math.pi * progress))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
scaler = torch.cuda.amp.GradScaler(enabled=use_cuda_amp)


@torch.inference_mode()
def predict_probabilities(data_loader):
    model.eval()
    prediction_parts = []

    for batch in data_loader:
        model_inputs = {
            key: value.to(device, non_blocking=use_cuda_amp)
            for key, value in batch["inputs"].items()
        }
        numeric_features = batch["numeric_features"].to(
            device,
            non_blocking=use_cuda_amp,
        )

        with torch.cuda.amp.autocast(enabled=use_cuda_amp):
            outputs = model(
                **model_inputs,
                numeric_features=numeric_features,
            )
            probabilities = torch.sigmoid(outputs["toxicity_logit"])

        prediction_parts.append(probabilities.float().cpu().numpy())

    return np.concatenate(prediction_parts, axis=0)


def safe_roc_auc(binary_target, predictions):
    binary_target = np.asarray(binary_target, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if binary_target.size == 0 or np.unique(binary_target).size < 2:
        return np.nan

    return float(roc_auc_score(binary_target, predictions))


def official_bias_aware_auc(validation_frame, predictions):
    targets = validation_frame["target"].to_numpy(dtype=np.float32) >= 0.5
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(targets) != len(predictions):
        raise ValueError(
            "Validation prediction count does not match validation labels."
        )

    overall_auc = safe_roc_auc(targets, predictions)

    metric_values = {
        "subgroup_auc": [],
        "bpsn_auc": [],
        "bnsp_auc": [],
    }

    for identity_column in OFFICIAL_IDENTITY_COLUMNS:
        subgroup = validation_frame[identity_column].to_numpy(dtype=np.float32) >= 0.5
        background = ~subgroup

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & ~targets) | (background & targets)
        bnsp_mask = (subgroup & targets) | (background & ~targets)

        metric_values["subgroup_auc"].append(
            safe_roc_auc(
                targets[subgroup_mask],
                predictions[subgroup_mask],
            )
        )
        metric_values["bpsn_auc"].append(
            safe_roc_auc(
                targets[bpsn_mask],
                predictions[bpsn_mask],
            )
        )
        metric_values["bnsp_auc"].append(
            safe_roc_auc(
                targets[bnsp_mask],
                predictions[bnsp_mask],
            )
        )

    def generalized_mean(values, power=-5.0):
        values = np.asarray(values, dtype=np.float64)
        values = values[np.isfinite(values)]

        if values.size == 0:
            return np.nan

        values = np.clip(values, 1e-15, 1.0)
        return float(np.mean(values**power) ** (1.0 / power))

    subgroup_mean = generalized_mean(metric_values["subgroup_auc"])
    bpsn_mean = generalized_mean(metric_values["bpsn_auc"])
    bnsp_mean = generalized_mean(metric_values["bnsp_auc"])

    component_scores = np.asarray(
        [overall_auc, subgroup_mean, bpsn_mean, bnsp_mean],
        dtype=np.float64,
    )

    if not np.isfinite(component_scores).all():
        raise ValueError(
            "Official validation metric is undefined because one or more AUC "
            "components have no positive/negative examples."
        )

    final_score = float(component_scores.mean())

    return final_score, {
        "overall_auc": float(overall_auc),
        "subgroup_auc": float(subgroup_mean),
        "bpsn_auc": float(bpsn_mean),
        "bnsp_auc": float(bnsp_mean),
    }


best_score = -np.inf
epochs_without_improvement = 0

for epoch in range(NUM_EPOCHS):
    model.train()
    optimizer.zero_grad(set_to_none=True)
    cumulative_loss = 0.0

    for batch_index, batch in enumerate(train_loader):
        model_inputs = {
            key: value.to(device, non_blocking=use_cuda_amp)
            for key, value in batch["inputs"].items()
        }

        numeric_features = batch["numeric_features"].to(
            device,
            non_blocking=use_cuda_amp,
        )
        targets = batch["target"].to(device, non_blocking=use_cuda_amp)
        annotator_counts = batch["annotator_count"].to(
            device,
            non_blocking=use_cuda_amp,
        )
        subtype_targets = batch["subtype_targets"].to(
            device,
            non_blocking=use_cuda_amp,
        )
        identity_labels = batch["identity_labels"].to(
            device,
            non_blocking=use_cuda_amp,
        )
        identity_label_available = batch["identity_label_available"].to(
            device,
            non_blocking=use_cuda_amp,
        )

        with torch.cuda.amp.autocast(enabled=use_cuda_amp):
            model_outputs = model(
                **model_inputs,
                numeric_features=numeric_features,
            )

            loss_outputs = criterion(
                model_outputs=model_outputs,
                toxicity_targets=targets,
                toxicity_annotator_counts=annotator_counts,
                subtype_targets=subtype_targets,
                identity_labels=identity_labels,
                identity_label_available=identity_label_available,
            )

            unscaled_loss = loss_outputs["loss"]
            loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(loss).backward()
        cumulative_loss += float(unscaled_loss.detach().cpu())

        is_update_step = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if is_update_step:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

    validation_predictions = predict_probabilities(valid_loader)
    epoch_score, epoch_components = official_bias_aware_auc(
        valid_df,
        validation_predictions,
    )
    average_train_loss = cumulative_loss / max(1, len(train_loader))

    if epoch_score > best_score:
        best_score = epoch_score
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_validation_score": best_score,
                "model_state_dict": model.state_dict(),
            },
            BEST_CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"loss={average_train_loss:.5f} "
        f"official_auc={epoch_score:.6f} "
        f"overall={epoch_components['overall_auc']:.6f} "
        f"subgroup={epoch_components['subgroup_auc']:.6f} "
        f"bpsn={epoch_components['bpsn_auc']:.6f} "
        f"bnsp={epoch_components['bnsp_auc']:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

best_checkpoint = torch.load(BEST_CHECKPOINT_PATH, map_location=device)
model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(device)

best_validation_predictions = predict_probabilities(valid_loader)
score, _ = official_bias_aware_auc(valid_df, best_validation_predictions)

test_predictions = predict_probabilities(test_loader)

if len(test_predictions) != len(test_df):
    raise ValueError("Test prediction count does not match the test dataframe.")

expected_ids = sample_submission["id"].to_numpy()
if not np.array_equal(test_df["id"].to_numpy(), expected_ids):
    raise ValueError("test_df is not aligned to sample_submission id ordering.")

submission = pd.DataFrame(
    {
        "id": test_df["id"].to_numpy(),
        "prediction": np.clip(test_predictions, 0.0, 1.0).astype(np.float64),
    }
)

submission.to_csv(SUBMISSION_DIR / "submission_f5465a97998249689ef20df90ebf394d.csv", index=False)

print(f"Final Validation Score: {score}")
