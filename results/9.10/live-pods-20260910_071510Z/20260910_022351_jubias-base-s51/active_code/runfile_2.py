import os
os.sched_setaffinity(0, {73, 69})
import json
import math
import os
import random
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

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# =============================================================================
# Configuration
# =============================================================================

SEED = 2027
RANDOM_HASH_BUCKETS = 10_000
VALIDATION_BUCKETS = 1_500

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
PROCESSED_DIR = WORKING_DIR / "processed_toxicity_data"
SUBMISSION_DIR = Path("./submission")

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"
SAMPLE_SUBMISSION_PATH = INPUT_DIR / "sample_submission.csv"
CHECKPOINT_PATH = WORKING_DIR / "best_toxicity_mechanism_router.pt"
METRICS_PATH = WORKING_DIR / "toxicity_training_metrics.json"
SUBMISSION_PATH = SUBMISSION_DIR / "submission_068150042147431aa3f08726706665db.csv"

MODEL_ID = "microsoft/deberta-v3-large"
MAX_LENGTH = int(os.environ.get("TOXICITY_MAX_LENGTH", "192"))
MAX_EPOCHS = int(os.environ.get("TOXICITY_EPOCHS", "1"))
PATIENCE = int(os.environ.get("TOXICITY_PATIENCE", "1"))

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

SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

if MAX_EPOCHS < 1:
    raise ValueError("TOXICITY_EPOCHS must be at least 1")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

try:
    torch.set_float32_matmul_precision("high")
except Exception:
    pass

# =============================================================================
# Data processing and feature engineering
# =============================================================================

train_header = pd.read_csv(TRAIN_PATH, nrows=0).columns.tolist()
test_header = pd.read_csv(TEST_PATH, nrows=0).columns.tolist()

required_train_columns = {"id", "comment_text", "target"}
required_test_columns = {"id", "comment_text"}

if not required_train_columns.issubset(train_header):
    missing = required_train_columns - set(train_header)
    raise ValueError(f"train.csv is missing required columns: {missing}")

if not required_test_columns.issubset(test_header):
    missing = required_test_columns - set(test_header)
    raise ValueError(f"test.csv is missing required columns: {missing}")

available_identity_columns = [
    column for column in IDENTITY_COLUMNS if column in train_header
]
available_subtype_columns = [
    column for column in SUBTYPE_COLUMNS if column in train_header
]

train_usecols = (
    ["id", "comment_text", "target"]
    + available_identity_columns
    + available_subtype_columns
)

train_dtypes = {
    "id": "int64",
    "target": "float32",
    **{
        column: "float32"
        for column in available_identity_columns + available_subtype_columns
    },
}

raw_train_df = pd.read_csv(
    TRAIN_PATH,
    usecols=train_usecols,
    dtype=train_dtypes,
    low_memory=False,
)

raw_test_df = pd.read_csv(
    TEST_PATH,
    usecols=["id", "comment_text"],
    dtype={"id": "int64"},
    low_memory=False,
)

if SAMPLE_SUBMISSION_PATH.exists():
    sample_submission_ids = pd.read_csv(SAMPLE_SUBMISSION_PATH, usecols=["id"])
    if len(sample_submission_ids) != len(raw_test_df):
        raise ValueError("test.csv row count does not match sample_submission.csv")
    if not np.array_equal(
        sample_submission_ids["id"].to_numpy(),
        raw_test_df["id"].to_numpy(),
    ):
        raise ValueError("test.csv ID order does not match sample_submission.csv")

raw_text_for_split = raw_train_df["comment_text"].fillna("").astype(str)
duplicate_safe_hash = pd.util.hash_pandas_object(
    raw_text_for_split,
    index=False,
).to_numpy(dtype=np.uint64)

validation_mask = (duplicate_safe_hash % np.uint64(RANDOM_HASH_BUCKETS)) < np.uint64(
    VALIDATION_BUCKETS
)

if validation_mask.sum() == 0 or (~validation_mask).sum() == 0:
    raise RuntimeError("Duplicate-isolated split produced an empty partition")

raw_train_partition = raw_train_df.loc[~validation_mask].copy()
raw_validation_partition = raw_train_df.loc[validation_mask].copy()

del raw_train_df
del raw_text_for_split
del duplicate_safe_hash
del validation_mask


def normalize_comment_text(text_series: pd.Series) -> pd.Series:
    text = text_series.fillna("").astype("string")
    text = text.str.normalize("NFKC")
    text = text.str.replace(r"[\r\n]+", " ", regex=True)
    text = text.str.replace(r"<[^>\n]{1,300}>", " ", regex=True)
    text = text.str.replace(
        r"(?i)\b(?:https?://|www\.)[^\s<]+",
        " [URL] ",
        regex=True,
    )
    text = text.str.replace(
        r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b",
        " [EMAIL] ",
        regex=True,
    )
    text = text.str.replace(
        r"(?<!\w)(?:\d{1,3}\.){3}\d{1,3}(?!\w)",
        " [IP] ",
        regex=True,
    )
    text = text.str.replace("&amp;", "&", regex=False)
    text = text.str.replace("&quot;", '"', regex=False)
    text = text.str.replace(r"&#(?:39|x27);", "'", regex=True)
    text = text.str.replace(r"\s+", " ", regex=True).str.strip()
    return text


def create_text_shape_features(clean_text: pd.Series) -> pd.DataFrame:
    char_count = clean_text.str.len().fillna(0).astype(np.float32)
    word_count = clean_text.str.count(r"\S+").fillna(0).astype(np.float32)
    alphabetic_count = clean_text.str.count(r"[A-Za-z]").fillna(0).astype(np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").fillna(0).astype(np.float32)
    digit_count = clean_text.str.count(r"\d").fillna(0).astype(np.float32)
    punctuation_count = clean_text.str.count(r"[^\w\s]").fillna(0).astype(np.float32)

    features = pd.DataFrame(index=clean_text.index)
    features["log_char_count"] = np.log1p(char_count)
    features["log_word_count"] = np.log1p(word_count)
    features["log_sentence_count"] = np.log1p(clean_text.str.count(r"[.!?]+").fillna(0))
    features["log_exclamation_count"] = np.log1p(clean_text.str.count(r"!").fillna(0))
    features["log_question_count"] = np.log1p(clean_text.str.count(r"\?").fillna(0))
    features["log_url_count"] = np.log1p(clean_text.str.count(r"\[URL\]").fillna(0))
    features["log_email_count"] = np.log1p(clean_text.str.count(r"\[EMAIL\]").fillna(0))
    features["log_ip_count"] = np.log1p(clean_text.str.count(r"\[IP\]").fillna(0))
    features["log_repeated_punctuation"] = np.log1p(
        clean_text.str.count(r"([!?.,])\1{1,}").fillna(0)
    )
    features["log_non_ascii_count"] = np.log1p(
        clean_text.str.count(r"[^\x00-\x7F]").fillna(0)
    )
    features["uppercase_alpha_ratio"] = uppercase_count / alphabetic_count.clip(
        lower=1.0
    )
    features["digit_char_ratio"] = digit_count / char_count.clip(lower=1.0)
    features["punctuation_char_ratio"] = punctuation_count / char_count.clip(lower=1.0)
    features["long_token_count"] = np.log1p(
        clean_text.str.count(r"\b\w{15,}\b").fillna(0)
    )

    return features.astype(np.float32)


def build_partition(
    source_df: pd.DataFrame,
    include_labels: bool,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    cleaned_text = normalize_comment_text(source_df["comment_text"])
    raw_features = create_text_shape_features(cleaned_text).reset_index(drop=True)

    output = pd.DataFrame(
        {
            "id": source_df["id"].to_numpy(dtype=np.int64, copy=False),
            "model_text": cleaned_text.astype(str).to_numpy(),
        }
    )

    if include_labels:
        soft_target = source_df["target"].clip(0.0, 1.0).astype(np.float32)
        output["target"] = soft_target.to_numpy()
        output["target_binary"] = (soft_target >= 0.5).astype(np.int8).to_numpy()

        for subtype in available_subtype_columns:
            output[subtype] = (
                source_df[subtype]
                .fillna(0.0)
                .clip(0.0, 1.0)
                .astype(np.float32)
                .to_numpy()
            )

        identity_value_matrix = []
        identity_known_matrix = []

        for identity in available_identity_columns:
            identity_values = (
                source_df[identity].fillna(0.0).clip(0.0, 1.0).astype(np.float32)
            )
            identity_known = source_df[identity].notna().astype(np.int8)

            output[identity] = identity_values.to_numpy()
            output[f"{identity}_mask"] = identity_known.to_numpy()

            identity_value_matrix.append(identity_values.to_numpy(dtype=np.float32))
            identity_known_matrix.append(identity_known.to_numpy(dtype=np.int8))

        if identity_value_matrix:
            output["any_identity"] = np.max(
                np.column_stack(identity_value_matrix),
                axis=1,
            ).astype(np.float32)

            output["identity_annotation_mask"] = np.max(
                np.column_stack(identity_known_matrix),
                axis=1,
            ).astype(np.int8)
        else:
            output["any_identity"] = np.zeros(len(output), dtype=np.float32)
            output["identity_annotation_mask"] = np.zeros(
                len(output),
                dtype=np.int8,
            )

    return output, raw_features


train_df, train_raw_features = build_partition(
    raw_train_partition,
    include_labels=True,
)
validation_df, validation_raw_features = build_partition(
    raw_validation_partition,
    include_labels=True,
)
test_df, test_raw_features = build_partition(
    raw_test_df,
    include_labels=False,
)

del raw_train_partition
del raw_validation_partition
del raw_test_df

feature_columns = train_raw_features.columns.tolist()
feature_means = train_raw_features[feature_columns].mean(axis=0).astype(np.float32)
feature_stds = train_raw_features[feature_columns].std(axis=0).astype(np.float32)
feature_stds = feature_stds.mask(feature_stds < 1e-6, 1.0).astype(np.float32)


def apply_train_fitted_scaling(
    destination_df: pd.DataFrame,
    raw_feature_df: pd.DataFrame,
) -> pd.DataFrame:
    standardized = (raw_feature_df[feature_columns] - feature_means) / feature_stds
    standardized = standardized.clip(lower=-8.0, upper=8.0).astype(np.float32)
    standardized.columns = feature_columns

    return pd.concat(
        [
            destination_df.reset_index(drop=True),
            standardized.reset_index(drop=True),
        ],
        axis=1,
    )


train_df = apply_train_fitted_scaling(train_df, train_raw_features)
validation_df = apply_train_fitted_scaling(
    validation_df,
    validation_raw_features,
)
test_df = apply_train_fitted_scaling(test_df, test_raw_features)

del train_raw_features
del validation_raw_features
del test_raw_features

if not set(feature_columns).issubset(test_df.columns):
    raise RuntimeError("Test features do not match train feature schema")

if (
    train_df["target_binary"].nunique() != 2
    or validation_df["target_binary"].nunique() != 2
):
    raise RuntimeError("Both partitions must contain both toxicity classes")

for identity in OFFICIAL_IDENTITY_COLUMNS:
    if identity not in validation_df.columns:
        raise ValueError(
            f"Official identity column unavailable for validation: {identity}"
        )

metadata = {
    "split_method": (
        "duplicate-isolated deterministic hash split on exact raw comment text; "
        f"{VALIDATION_BUCKETS}/{RANDOM_HASH_BUCKETS} hash buckets form validation"
    ),
    "text_column": "model_text",
    "id_column": "id",
    "soft_target_column": "target",
    "binary_target_column": "target_binary",
    "feature_columns": feature_columns,
    "feature_means": {
        column: float(feature_means[column]) for column in feature_columns
    },
    "feature_stds": {column: float(feature_stds[column]) for column in feature_columns},
    "identity_columns": available_identity_columns,
    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    "identity_mask_suffix": "_mask",
    "subtype_columns": available_subtype_columns,
    "train_rows": int(len(train_df)),
    "validation_rows": int(len(validation_df)),
    "test_rows": int(len(test_df)),
    "test_id_order_matches_sample_submission": True,
}

with open(
    PROCESSED_DIR / "feature_metadata.json",
    "w",
    encoding="utf-8",
) as metadata_file:
    json.dump(metadata, metadata_file, indent=2)

# =============================================================================
# Model design
# =============================================================================

"""
DeBERTa-v3-large Usage Example
Base model: microsoft/deberta-v3-large (~435M parameters)
Domain: Natural Language Processing (text classification, NLI, QA, etc.)
Input: Tokenized text sequences
Output: Classification logits or hidden embeddings
"""

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
pretrained_sequence_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class ToxicityMechanismRouter(nn.Module):
    def __init__(
        self,
        pretrained_classifier: nn.Module,
        num_subtypes: int,
        num_experts: int = 6,
        expert_dim: int = 320,
        dropout_probability: float = 0.15,
    ) -> None:
        super().__init__()

        self.backbone = pretrained_classifier.deberta
        self.hidden_size = int(pretrained_classifier.config.hidden_size)
        self.num_subtypes = int(num_subtypes)
        self.num_experts = int(num_experts)

        self.input_norm = nn.LayerNorm(self.hidden_size)

        self.router = nn.Sequential(
            nn.Linear(self.hidden_size, self.hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(self.hidden_size // 2, self.num_experts),
        )

        self.experts = nn.ModuleList(
            [
                nn.Sequential(
                    nn.LayerNorm(self.hidden_size),
                    nn.Linear(self.hidden_size, expert_dim),
                    nn.GELU(),
                    nn.Dropout(dropout_probability),
                    nn.Linear(expert_dim, expert_dim),
                    nn.GELU(),
                )
                for _ in range(self.num_experts)
            ]
        )

        fused_size = self.hidden_size + expert_dim

        self.shared_projection = nn.Sequential(
            nn.LayerNorm(fused_size),
            nn.Linear(fused_size, expert_dim),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.toxicity_head = nn.Linear(expert_dim, 1)
        self.subtype_head = (
            nn.Linear(expert_dim, self.num_subtypes) if self.num_subtypes > 0 else None
        )

    def gradient_checkpointing_enable(self) -> None:
        if hasattr(self.backbone, "gradient_checkpointing_enable"):
            # Non-reentrant checkpointing retains activation-memory savings.
            # It avoids DeBERTa's reentrant checkpoint graph replay during backward.
            self.backbone.gradient_checkpointing_enable(
                gradient_checkpointing_kwargs={"use_reentrant": False}
            )

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        **kwargs,
    ) -> dict[str, torch.Tensor]:
        backbone_kwargs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }

        if "inputs_embeds" in kwargs:
            backbone_kwargs["inputs_embeds"] = kwargs["inputs_embeds"]

        backbone_output = self.backbone(**backbone_kwargs)
        token_embeddings = backbone_output.last_hidden_state

        mask = attention_mask.unsqueeze(-1).to(token_embeddings.dtype)
        pooled_embedding = (token_embeddings * mask).sum(dim=1) / mask.sum(
            dim=1
        ).clamp_min(1.0)

        pooled_embedding = self.input_norm(pooled_embedding)

        router_logits = self.router(pooled_embedding)
        router_probabilities = F.softmax(router_logits, dim=-1)

        expert_embeddings = torch.stack(
            [expert(pooled_embedding) for expert in self.experts],
            dim=1,
        )

        routed_embedding = torch.sum(
            expert_embeddings * router_probabilities.unsqueeze(-1),
            dim=1,
        )

        shared_embedding = self.shared_projection(
            torch.cat([pooled_embedding, routed_embedding], dim=-1)
        )

        output = {
            "toxicity_logits": self.toxicity_head(shared_embedding).squeeze(-1),
            "router_probabilities": router_probabilities,
            "shared_embedding": shared_embedding,
        }

        if self.subtype_head is not None:
            output["subtype_logits"] = self.subtype_head(shared_embedding)

        return output


class OfficialBiasGroupDROLoss(nn.Module):
    def __init__(
        self,
        num_official_identities: int,
        primary_weight: float = 1.0,
        bias_subset_weight: float = 0.85,
        subtype_weight: float = 0.20,
        dro_temperature: float = 0.12,
        router_entropy_weight: float = 0.005,
    ) -> None:
        super().__init__()

        self.num_official_identities = int(num_official_identities)
        self.primary_weight = float(primary_weight)
        self.bias_subset_weight = float(bias_subset_weight)
        self.subtype_weight = float(subtype_weight)
        self.dro_temperature = float(dro_temperature)
        self.router_entropy_weight = float(router_entropy_weight)
        self.last_components: dict[str, float] = {}

    @staticmethod
    def _binary_cross_entropy(
        logits: torch.Tensor,
        soft_targets: torch.Tensor,
    ) -> torch.Tensor:
        return F.binary_cross_entropy_with_logits(
            logits,
            soft_targets.to(dtype=logits.dtype).clamp(0.0, 1.0),
            reduction="none",
        )

    @staticmethod
    def _subset_has_both_classes(
        binary_targets: torch.Tensor,
        subset_mask: torch.Tensor,
    ) -> bool:
        subset_targets = binary_targets[subset_mask]
        return bool(
            subset_targets.numel() >= 2
            and torch.any(subset_targets == 0).item()
            and torch.any(subset_targets == 1).item()
        )

    def forward(
        self,
        model_output: dict[str, torch.Tensor],
        target: torch.Tensor,
        identity_values: torch.Tensor | None = None,
        identity_masks: torch.Tensor | None = None,
        subtype_targets: torch.Tensor | None = None,
    ) -> torch.Tensor:
        logits = model_output["toxicity_logits"]
        soft_target = target.reshape(-1).to(
            device=logits.device,
            dtype=logits.dtype,
        )
        binary_target = (soft_target >= 0.5).to(torch.long)

        per_example_loss = self._binary_cross_entropy(logits, soft_target)
        primary_loss = per_example_loss.mean()

        subset_losses: list[torch.Tensor] = []

        if identity_values is not None:
            identity_values = identity_values.to(
                device=logits.device,
                dtype=logits.dtype,
            )

            if identity_masks is None:
                identity_masks = torch.ones_like(
                    identity_values,
                    dtype=torch.bool,
                )
            else:
                identity_masks = identity_masks.to(
                    device=logits.device,
                    dtype=torch.bool,
                )

            identity_count = min(
                self.num_official_identities,
                identity_values.shape[1],
                identity_masks.shape[1],
            )

            for identity_index in range(identity_count):
                known_mask = identity_masks[:, identity_index]
                subgroup_mask = known_mask & (identity_values[:, identity_index] >= 0.5)
                background_mask = known_mask & (~subgroup_mask)

                bpsn_mask = (subgroup_mask & (binary_target == 0)) | (
                    background_mask & (binary_target == 1)
                )

                bnsp_mask = (subgroup_mask & (binary_target == 1)) | (
                    background_mask & (binary_target == 0)
                )

                for evaluation_subset_mask in (
                    subgroup_mask,
                    bpsn_mask,
                    bnsp_mask,
                ):
                    if self._subset_has_both_classes(
                        binary_target,
                        evaluation_subset_mask,
                    ):
                        subset_losses.append(
                            per_example_loss[evaluation_subset_mask].mean()
                        )

        if subset_losses:
            stacked_subset_losses = torch.stack(subset_losses)
            temperature = max(self.dro_temperature, 1e-4)

            bias_loss = temperature * torch.logsumexp(
                stacked_subset_losses / temperature,
                dim=0,
            ) - temperature * torch.log(
                torch.tensor(
                    float(len(subset_losses)),
                    device=logits.device,
                    dtype=logits.dtype,
                )
            )
        else:
            bias_loss = torch.zeros(
                (),
                device=logits.device,
                dtype=logits.dtype,
            )

        subtype_loss = torch.zeros(
            (),
            device=logits.device,
            dtype=logits.dtype,
        )

        if (
            subtype_targets is not None
            and "subtype_logits" in model_output
            and model_output["subtype_logits"].shape[1] > 0
        ):
            subtype_logits = model_output["subtype_logits"]

            aligned_targets = subtype_targets[:, : subtype_logits.shape[1]].to(
                device=logits.device,
                dtype=logits.dtype,
            )

            subtype_loss = F.binary_cross_entropy_with_logits(
                subtype_logits,
                aligned_targets.clamp(0.0, 1.0),
                reduction="mean",
            )

        router_probabilities = model_output["router_probabilities"].clamp_min(1e-8)
        router_entropy = (
            -(router_probabilities * router_probabilities.log()).sum(dim=-1).mean()
        )

        router_regularizer = -router_entropy

        total_loss = (
            self.primary_weight * primary_loss
            + self.bias_subset_weight * bias_loss
            + self.subtype_weight * subtype_loss
            + self.router_entropy_weight * router_regularizer
        )

        self.last_components = {
            "primary_bce": float(primary_loss.detach().cpu()),
            "bias_group_dro": float(bias_loss.detach().cpu()),
            "subtype_bce": float(subtype_loss.detach().cpu()),
            "router_entropy": float(router_entropy.detach().cpu()),
            "total_loss": float(total_loss.detach().cpu()),
        }

        return total_loss


model = ToxicityMechanismRouter(
    pretrained_classifier=pretrained_sequence_model,
    num_subtypes=len(available_subtype_columns),
    num_experts=6,
    expert_dim=320,
    dropout_probability=0.15,
)

model.gradient_checkpointing_enable()

criterion = OfficialBiasGroupDROLoss(
    num_official_identities=len(OFFICIAL_IDENTITY_COLUMNS),
    primary_weight=1.0,
    bias_subset_weight=0.85,
    subtype_weight=0.20,
    dro_temperature=0.12,
    router_entropy_weight=0.005,
)

no_decay_terms = (
    "bias",
    "LayerNorm.weight",
    "layer_norm.weight",
    "norm.weight",
)

backbone_decay_parameters = []
backbone_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_backbone_parameter = parameter_name.startswith("backbone.")
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_backbone_parameter and has_no_decay:
        backbone_no_decay_parameters.append(parameter)
    elif is_backbone_parameter:
        backbone_decay_parameters.append(parameter)
    elif has_no_decay:
        head_no_decay_parameters.append(parameter)
    else:
        head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_decay_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": backbone_no_decay_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_parameters,
            "lr": 2.0e-4,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_parameters,
            "lr": 2.0e-4,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

# =============================================================================
# Training and official metric evaluation
# =============================================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"

if device.type == "cuda":
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    if gpu_memory_gb >= 70:
        train_batch_size = 32
    elif gpu_memory_gb >= 38:
        train_batch_size = 24
    elif gpu_memory_gb >= 22:
        train_batch_size = 16
    else:
        train_batch_size = 8
else:
    train_batch_size = 4

eval_batch_size = max(4, min(train_batch_size * 2, 48))
gradient_accumulation_steps = max(
    1,
    math.ceil(32 / train_batch_size),
)
# The execution environment recommends at most two loader workers; exceeding it
# can cause worker contention or freezes without improving tokenizer throughput.
num_workers = min(2, max(1, os.cpu_count() or 1))
pin_memory = device.type == "cuda"

required_identity_columns = list(OFFICIAL_IDENTITY_COLUMNS)

missing_identity_columns = [
    column for column in required_identity_columns if column not in train_df.columns
]

if missing_identity_columns:
    raise ValueError(
        f"Missing required official identity columns: {missing_identity_columns}"
    )

missing_identity_masks = [
    f"{column}_mask"
    for column in required_identity_columns
    if f"{column}_mask" not in train_df.columns
]

if missing_identity_masks:
    raise ValueError(
        f"Missing required identity annotation masks: {missing_identity_masks}"
    )

for subtype_column in available_subtype_columns:
    if subtype_column not in train_df.columns:
        raise ValueError(f"Expected subtype column is unavailable: {subtype_column}")


class ToxicityTrainingDataset(Dataset):
    def __init__(
        self,
        dataframe: pd.DataFrame,
        include_auxiliary_labels: bool,
    ) -> None:
        self.texts = dataframe["model_text"].fillna("").astype(str).tolist()
        self.include_auxiliary_labels = include_auxiliary_labels

        if include_auxiliary_labels:
            self.targets = dataframe["target"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

            self.identity_values = dataframe.loc[
                :,
                required_identity_columns,
            ].to_numpy(
                dtype=np.float32,
                copy=True,
            )

            self.identity_masks = dataframe.loc[
                :,
                [f"{column}_mask" for column in required_identity_columns],
            ].to_numpy(
                dtype=np.int8,
                copy=True,
            )

            self.subtype_targets = dataframe.loc[
                :,
                available_subtype_columns,
            ].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int) -> dict:
        encoded = tokenizer(
            self.texts[index],
            truncation=True,
            max_length=MAX_LENGTH,
            add_special_tokens=True,
            return_attention_mask=True,
            return_token_type_ids=False,
        )

        item = {"tokens": encoded}

        if self.include_auxiliary_labels:
            item["target"] = self.targets[index]
            item["identity_values"] = self.identity_values[index]
            item["identity_masks"] = self.identity_masks[index]
            item["subtype_targets"] = self.subtype_targets[index]

        return item


def toxicity_collate(batch: list[dict]) -> dict[str, torch.Tensor]:
    token_batch = tokenizer.pad(
        [item["tokens"] for item in batch],
        padding=True,
        max_length=MAX_LENGTH,
        pad_to_multiple_of=8 if use_amp else None,
        return_tensors="pt",
    )

    if "target" in batch[0]:
        token_batch["target"] = torch.tensor(
            np.asarray(
                [item["target"] for item in batch],
                dtype=np.float32,
            ),
            dtype=torch.float32,
        )

        token_batch["identity_values"] = torch.tensor(
            np.stack([item["identity_values"] for item in batch]).astype(
                np.float32, copy=False
            ),
            dtype=torch.float32,
        )

        token_batch["identity_masks"] = torch.tensor(
            np.stack([item["identity_masks"] for item in batch]).astype(
                np.bool_, copy=False
            ),
            dtype=torch.bool,
        )

        token_batch["subtype_targets"] = torch.tensor(
            np.stack([item["subtype_targets"] for item in batch]).astype(
                np.float32, copy=False
            ),
            dtype=torch.float32,
        )

    return token_batch


train_dataset = ToxicityTrainingDataset(
    train_df,
    include_auxiliary_labels=True,
)

validation_dataset = ToxicityTrainingDataset(
    validation_df,
    include_auxiliary_labels=False,
)

test_dataset = ToxicityTrainingDataset(
    test_df,
    include_auxiliary_labels=False,
)

loader_kwargs = {
    "num_workers": num_workers,
    "pin_memory": pin_memory,
    "persistent_workers": num_workers > 0,
    "collate_fn": toxicity_collate,
}

train_generator = torch.Generator()
train_generator.manual_seed(SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=train_batch_size,
    shuffle=True,
    drop_last=False,
    generator=train_generator,
    **loader_kwargs,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=eval_batch_size,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=eval_batch_size,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)

model.to(device)

if hasattr(model, "backbone") and hasattr(model.backbone, "config"):
    model.backbone.config.use_cache = False

amp_scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

updates_per_epoch = math.ceil(len(train_loader) / gradient_accumulation_steps)

total_optimizer_updates = max(
    1,
    updates_per_epoch * MAX_EPOCHS,
)

warmup_updates = min(
    max(100, int(0.04 * total_optimizer_updates)),
    max(0, total_optimizer_updates - 1),
)


def cosine_warmup_lambda(step: int) -> float:
    if warmup_updates > 0 and step < warmup_updates:
        return float(step + 1) / float(warmup_updates)

    progress = (step - warmup_updates) / max(
        1,
        total_optimizer_updates - warmup_updates,
    )

    return max(
        0.05,
        0.5 * (1.0 + math.cos(math.pi * min(1.0, progress))),
    )


scheduler = LambdaLR(
    optimizer,
    lr_lambda=cosine_warmup_lambda,
)


@torch.inference_mode()
def predict_from_loader(data_loader: DataLoader) -> np.ndarray:
    model.eval()
    prediction_parts = []

    for batch in data_loader:
        input_ids = batch["input_ids"].to(
            device,
            non_blocking=pin_memory,
        )
        attention_mask = batch["attention_mask"].to(
            device,
            non_blocking=pin_memory,
        )

        with torch.cuda.amp.autocast(enabled=use_amp):
            output = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )
            probabilities = torch.sigmoid(output["toxicity_logits"])

        prediction_parts.append(probabilities.float().cpu().numpy())

    if not prediction_parts:
        raise RuntimeError("Inference loader produced no batches")

    predictions = np.concatenate(prediction_parts).astype(
        np.float64,
        copy=False,
    )

    if not np.isfinite(predictions).all():
        raise RuntimeError("Model inference produced non-finite predictions")

    return predictions


def _auc_for_subset(
    binary_targets: np.ndarray,
    predictions: np.ndarray,
    subset_mask: np.ndarray,
    subset_name: str,
) -> float:
    subset_targets = binary_targets[subset_mask]
    subset_predictions = predictions[subset_mask]

    if subset_targets.size < 2 or np.unique(subset_targets).size != 2:
        raise ValueError(
            f"Validation subset '{subset_name}' does not contain both classes "
            f"(rows={subset_targets.size}, "
            f"classes={np.unique(subset_targets).tolist()})"
        )

    return float(
        roc_auc_score(
            subset_targets,
            subset_predictions,
        )
    )


def official_unintended_bias_score(
    dataframe: pd.DataFrame,
    predictions: np.ndarray,
) -> tuple[float, dict[str, object]]:
    if len(dataframe) != len(predictions):
        raise ValueError("Validation prediction count does not match validation rows")

    binary_targets = dataframe["target_binary"].to_numpy(
        dtype=np.int8,
        copy=False,
    )

    if np.unique(binary_targets).size != 2:
        raise ValueError("Validation target must contain both toxicity classes")

    overall_auc = float(
        roc_auc_score(
            binary_targets,
            predictions,
        )
    )

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in required_identity_columns:
        identity_known = dataframe[f"{identity_column}_mask"].to_numpy(
            dtype=np.int8,
            copy=False,
        ).astype(bool, copy=False)

        identity_positive = (
            dataframe[identity_column].to_numpy(
                dtype=np.float32,
                copy=False,
            )
            >= 0.5
        )

        subgroup = identity_positive
        background = ~subgroup

        subgroup_auc = _auc_for_subset(
            binary_targets,
            predictions,
            subgroup,
            f"{identity_column}/subgroup",
        )

        bpsn_subset = (subgroup & (binary_targets == 0)) | (
            background & (binary_targets == 1)
        )

        bnsp_subset = (subgroup & (binary_targets == 1)) | (
            background & (binary_targets == 0)
        )

        bpsn_auc = _auc_for_subset(
            binary_targets,
            predictions,
            bpsn_subset,
            f"{identity_column}/BPSN",
        )

        bnsp_auc = _auc_for_subset(
            binary_targets,
            predictions,
            bnsp_subset,
            f"{identity_column}/BNSP",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity[identity_column] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
            "annotated_rows": int(identity_known.sum()),
        }

    def power_mean(
        values: list[float],
        power: float = -5.0,
    ) -> float:
        value_array = np.asarray(values, dtype=np.float64)

        if len(value_array) != len(required_identity_columns):
            raise ValueError(
                "Each official identity must contribute to every bias metric"
            )

        return float(np.mean(np.power(value_array, power)) ** (1.0 / power))

    subgroup_power_mean = power_mean(subgroup_aucs)
    bpsn_power_mean = power_mean(bpsn_aucs)
    bnsp_power_mean = power_mean(bnsp_aucs)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    metric_details = {
        "overall_auc": overall_auc,
        "subgroup_power_mean_auc": subgroup_power_mean,
        "bpsn_power_mean_auc": bpsn_power_mean,
        "bnsp_power_mean_auc": bnsp_power_mean,
        "official_final_score": final_score,
        "per_identity": per_identity,
    }

    return final_score, metric_details


best_score = -float("inf")
best_epoch = -1
epochs_without_improvement = 0
training_history = []

optimizer.zero_grad(set_to_none=True)

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()

    running_loss = 0.0
    seen_examples = 0

    for batch_index, batch in enumerate(train_loader):
        input_ids = batch["input_ids"].to(
            device,
            non_blocking=pin_memory,
        )
        attention_mask = batch["attention_mask"].to(
            device,
            non_blocking=pin_memory,
        )
        target = batch["target"].to(
            device,
            non_blocking=pin_memory,
        )
        identity_values = batch["identity_values"].to(
            device,
            non_blocking=pin_memory,
        )
        identity_masks = batch["identity_masks"].to(
            device,
            non_blocking=pin_memory,
        )
        subtype_targets = batch["subtype_targets"].to(
            device,
            non_blocking=pin_memory,
        )

        with torch.cuda.amp.autocast(enabled=use_amp):
            model_output = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )

            unscaled_loss = criterion(
                model_output=model_output,
                target=target,
                identity_values=identity_values,
                identity_masks=identity_masks,
                subtype_targets=subtype_targets,
            )

            scaled_loss = unscaled_loss / gradient_accumulation_steps

        amp_scaler.scale(scaled_loss).backward()

        is_update_step = (batch_index + 1) % gradient_accumulation_steps == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if is_update_step:
            amp_scaler.unscale_(optimizer)

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                max_norm=1.0,
            )

            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_size = target.shape[0]
        running_loss += float(unscaled_loss.detach().float().cpu()) * batch_size
        seen_examples += batch_size

    validation_predictions = predict_from_loader(validation_loader)

    validation_score, validation_details = official_unintended_bias_score(
        validation_df,
        validation_predictions,
    )

    epoch_train_loss = running_loss / max(1, seen_examples)

    history_entry = {
        "epoch": epoch,
        "train_loss": float(epoch_train_loss),
        **validation_details,
    }

    training_history.append(history_entry)

    improved = validation_score > best_score + 1e-7

    if improved:
        best_score = validation_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_validation_score": float(validation_score),
                "model_state_dict": {
                    key: value.detach().cpu()
                    for key, value in model.state_dict().items()
                },
                "optimizer_state_dict": optimizer.state_dict(),
                "max_length": MAX_LENGTH,
                "official_identity_columns": required_identity_columns,
            },
            CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} | "
        f"train_loss={epoch_train_loss:.6f} | "
        f"official_val={validation_score:.6f} | "
        f"best={best_score:.6f}"
    )

    if epochs_without_improvement >= PATIENCE:
        break

if best_epoch < 0 or not CHECKPOINT_PATH.exists():
    raise RuntimeError("No valid official-metric checkpoint was saved")

checkpoint = torch.load(
    CHECKPOINT_PATH,
    map_location=device,
)

model.load_state_dict(
    checkpoint["model_state_dict"],
    strict=True,
)

model.to(device)

final_validation_predictions = predict_from_loader(validation_loader)

score, final_validation_details = official_unintended_bias_score(
    validation_df,
    final_validation_predictions,
)

test_predictions = predict_from_loader(test_loader)

if len(test_predictions) != len(test_df):
    raise RuntimeError(
        f"Test prediction count mismatch: " f"{len(test_predictions)} != {len(test_df)}"
    )

submission = pd.DataFrame(
    {
        "id": test_df["id"].to_numpy(
            dtype=np.int64,
            copy=False,
        ),
        "prediction": np.clip(
            test_predictions,
            0.0,
            1.0,
        ),
    }
)

if submission["id"].duplicated().any():
    raise RuntimeError("Submission IDs are unexpectedly duplicated")

submission.to_csv(
    SUBMISSION_PATH,
    index=False,
)

with open(
    METRICS_PATH,
    "w",
    encoding="utf-8",
) as metrics_file:
    json.dump(
        {
            "split": (
                "duplicate-isolated deterministic hash holdout " "from preprocessing"
            ),
            "metric": (
                "official competition score: 0.25 overall AUC + 0.25 each "
                "of p=-5 generalized subgroup, BPSN, and BNSP AUC means"
            ),
            "best_epoch": int(best_epoch),
            "checkpoint_validation_score": float(best_score),
            "reloaded_checkpoint_validation": final_validation_details,
            "history": training_history,
            "submission_path": str(SUBMISSION_PATH),
            "submission_rows": int(len(submission)),
        },
        metrics_file,
        indent=2,
    )

print(f"Final Validation Score: {score}")