import os
os.sched_setaffinity(0, {10, 11})
import os
import re
import gc
import html
import json
import math
import random
import warnings
import unicodedata

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from torch.cuda.amp import GradScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    get_cosine_schedule_with_warmup,
)

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
SEED = 2027
INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"

TRAIN_PATH = os.path.join(INPUT_DIR, "train.csv")
TEST_PATH = os.path.join(INPUT_DIR, "test.csv")
SAMPLE_SUBMISSION_PATH = os.path.join(INPUT_DIR, "sample_submission.csv")
BEST_MODEL_PATH = os.path.join(WORKING_DIR, "best_bias_aware_deberta.pt")
METRICS_PATH = os.path.join(WORKING_DIR, "training_metrics.json")

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 4
EVAL_BATCH_SIZE = 8
GRADIENT_ACCUMULATION_STEPS = 8
MAX_EPOCHS = 2
EARLY_STOPPING_PATIENCE = 1
NUM_WORKERS = max(2, min(4, os.cpu_count() or 2))

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cudnn.benchmark = True

try:
    torch.set_float32_matmul_precision("high")
except Exception:
    pass

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda_amp = device.type == "cuda"

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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

numeric_feature_columns = [
    "feat_log_char_count",
    "feat_log_word_count",
    "feat_uppercase_ratio",
    "feat_log_exclamation_count",
    "feat_log_question_count",
    "feat_log_newline_count",
    "feat_log_url_count",
    "feat_repeated_punctuation",
    "feat_all_caps_token_count",
    "feat_quoted_text",
]

# ---------------------------------------------------------------------
# Data loading and preprocessing
# ---------------------------------------------------------------------
TRAIN_COLUMNS = (
    [
        "id",
        "comment_text",
        "target",
        "article_id",
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + AUXILIARY_TARGET_COLUMNS
    + IDENTITY_COLUMNS
)

FLOAT_COLUMNS = ["target"] + AUXILIARY_TARGET_COLUMNS + IDENTITY_COLUMNS
DTYPES = {column: np.float32 for column in FLOAT_COLUMNS}
DTYPES["toxicity_annotator_count"] = np.int32
DTYPES["identity_annotator_count"] = np.int32
DTYPES["article_id"] = np.int32
DTYPES["id"] = np.int64

train_raw = pd.read_csv(TRAIN_PATH, usecols=TRAIN_COLUMNS, dtype=DTYPES)
test_raw = pd.read_csv(
    TEST_PATH,
    usecols=["id", "comment_text"],
    dtype={"id": np.int64},
)
sample_submission = pd.read_csv(
    SAMPLE_SUBMISSION_PATH,
    usecols=["id", "prediction"],
)

if train_raw["id"].duplicated().any():
    raise ValueError("Training IDs must be unique.")
if test_raw["id"].duplicated().any():
    raise ValueError("Test IDs must be unique.")
if set(sample_submission["id"]) != set(test_raw["id"]):
    raise ValueError("sample_submission.csv IDs and test.csv IDs do not match.")

test_raw = (
    test_raw.set_index("id").loc[sample_submission["id"].to_numpy()].reset_index()
)

HTML_BREAK_RE = re.compile(r"(?is)<\s*br\s*/?\s*>")
HTML_TAG_RE = re.compile(r"(?is)<[^>\n]{1,300}>")
URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>{}\[\]|\\^`]+")
EMAIL_RE = re.compile(r"(?i)\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
LONG_NUMBER_RE = re.compile(r"\b\d[\d,._-]{2,}\b")
HORIZONTAL_WHITESPACE_RE = re.compile(r"[ \t\r\f\v]+")
EXCESS_NEWLINES_RE = re.compile(r"\n{3,}")


def normalize_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = unicodedata.normalize("NFKC", html.unescape(text))
    text = text.replace("\x00", " ")
    text = HTML_BREAK_RE.sub("\n", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = URL_RE.sub(" [URL] ", text)
    text = EMAIL_RE.sub(" [EMAIL] ", text)
    text = LONG_NUMBER_RE.sub(" [NUMBER] ", text)
    text = HORIZONTAL_WHITESPACE_RE.sub(" ", text)
    text = EXCESS_NEWLINES_RE.sub("\n\n", text)
    return text.strip()


def add_text_features(frame):
    frame = frame.copy()
    normalized_text = frame.pop("comment_text").fillna("").map(normalize_comment)
    frame["model_text"] = normalized_text

    char_count = normalized_text.str.len().astype(np.float32)
    word_count = normalized_text.str.count(r"\S+").astype(np.float32)
    alpha_count = normalized_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = normalized_text.str.count(r"[A-Z]").astype(np.float32)

    frame["feat_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["feat_log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["feat_uppercase_ratio"] = (
        uppercase_count / np.maximum(alpha_count, 1.0)
    ).astype(np.float32)
    frame["feat_log_exclamation_count"] = np.log1p(
        normalized_text.str.count(r"!").astype(np.float32)
    ).astype(np.float32)
    frame["feat_log_question_count"] = np.log1p(
        normalized_text.str.count(r"\?").astype(np.float32)
    ).astype(np.float32)
    frame["feat_log_newline_count"] = np.log1p(
        normalized_text.str.count(r"\n").astype(np.float32)
    ).astype(np.float32)
    frame["feat_log_url_count"] = np.log1p(
        normalized_text.str.count(r"\[URL\]").astype(np.float32)
    ).astype(np.float32)
    frame["feat_repeated_punctuation"] = normalized_text.str.contains(
        r"([!?.,])\1{2}",
        regex=True,
    ).astype(np.float32)
    frame["feat_all_caps_token_count"] = np.log1p(
        normalized_text.str.count(r"\b[A-Z]{3,}\b").astype(np.float32)
    ).astype(np.float32)
    frame["feat_quoted_text"] = normalized_text.str.contains(
        r"""["“”']""",
        regex=True,
    ).astype(np.float32)

    return frame


train_raw = add_text_features(train_raw)
test_raw = add_text_features(test_raw)

train_raw["target_binary"] = (train_raw["target"] >= 0.5).astype(np.int8)

for identity_column in IDENTITY_COLUMNS:
    original_identity = train_raw[identity_column]
    train_raw[f"{identity_column}_is_labeled"] = original_identity.notna().astype(
        np.int8
    )
    train_raw[f"{identity_column}_binary"] = (
        original_identity.fillna(0.0) >= 0.5
    ).astype(np.int8)

for auxiliary_column in AUXILIARY_TARGET_COLUMNS:
    train_raw[auxiliary_column] = (
        train_raw[auxiliary_column].fillna(0.0).astype(np.float32)
    )

identity_binary_columns = [f"{column}_binary" for column in EVALUATED_IDENTITY_COLUMNS]
toxicity_binary = train_raw["target_binary"].to_numpy(dtype=np.float32)
identity_binary_matrix = train_raw[identity_binary_columns].to_numpy(dtype=np.float32)

reference_prevalence = np.concatenate(
    [
        np.array([toxicity_binary.mean()], dtype=np.float64),
        identity_binary_matrix.mean(axis=0).astype(np.float64),
        (
            (identity_binary_matrix * toxicity_binary[:, None]).sum(axis=0)
            / np.maximum(identity_binary_matrix.sum(axis=0), 1.0)
        ).astype(np.float64),
    ]
)

article_groups = train_raw["article_id"].to_numpy()
splitter = GroupShuffleSplit(n_splits=12, test_size=0.10, random_state=SEED)

best_split_score = np.inf
best_train_indices = None
best_validation_indices = None

for candidate_train_indices, candidate_validation_indices in splitter.split(
    train_raw,
    y=toxicity_binary,
    groups=article_groups,
):
    candidate_y = toxicity_binary[candidate_validation_indices]
    candidate_identity = identity_binary_matrix[candidate_validation_indices]

    candidate_prevalence = np.concatenate(
        [
            np.array([candidate_y.mean()], dtype=np.float64),
            candidate_identity.mean(axis=0).astype(np.float64),
            (
                (candidate_identity * candidate_y[:, None]).sum(axis=0)
                / np.maximum(candidate_identity.sum(axis=0), 1.0)
            ).astype(np.float64),
        ]
    )

    expected_standard_error = np.sqrt(
        np.maximum(reference_prevalence * (1.0 - reference_prevalence), 1e-5)
        / max(len(candidate_validation_indices), 1)
    )

    prevalence_distance = np.mean(
        np.abs(candidate_prevalence - reference_prevalence)
        / np.maximum(expected_standard_error, 0.0025)
    )

    group_size_distance = (
        abs(len(candidate_validation_indices) / len(train_raw) - 0.10) * 25.0
    )

    subgroup_positive_counts = (candidate_identity * candidate_y[:, None]).sum(axis=0)
    subgroup_negative_counts = (candidate_identity * (1.0 - candidate_y[:, None])).sum(
        axis=0
    )

    insufficient_subgroup_penalty = (
        (subgroup_positive_counts < 25).sum() + (subgroup_negative_counts < 25).sum()
    ) * 1000.0

    candidate_score = (
        prevalence_distance + group_size_distance + insufficient_subgroup_penalty
    )

    if candidate_score < best_split_score:
        best_split_score = candidate_score
        best_train_indices = candidate_train_indices
        best_validation_indices = candidate_validation_indices

if best_train_indices is None or best_validation_indices is None:
    raise RuntimeError("Unable to construct an article-disjoint validation split.")

train_data = train_raw.iloc[best_train_indices].reset_index(drop=True)
validation_data = train_raw.iloc[best_validation_indices].reset_index(drop=True)
test_data = test_raw.reset_index(drop=True)

feature_scaler = StandardScaler()
train_data.loc[:, numeric_feature_columns] = feature_scaler.fit_transform(
    train_data[numeric_feature_columns]
).astype(np.float32)
validation_data.loc[:, numeric_feature_columns] = feature_scaler.transform(
    validation_data[numeric_feature_columns]
).astype(np.float32)
test_data.loc[:, numeric_feature_columns] = feature_scaler.transform(
    test_data[numeric_feature_columns]
).astype(np.float32)

joblib.dump(
    feature_scaler,
    os.path.join(WORKING_DIR, "text_feature_scaler.joblib"),
)

np.savez_compressed(
    os.path.join(WORKING_DIR, "article_disjoint_split_indices.npz"),
    train_indices=best_train_indices,
    validation_indices=best_validation_indices,
)

preprocessing_metadata = {
    "split_strategy": (
        "article-disjoint GroupShuffleSplit selected for toxicity "
        "and identity prevalence balance"
    ),
    "validation_fraction": float(
        len(validation_data) / (len(train_data) + len(validation_data))
    ),
    "text_column": "model_text",
    "target_column": "target",
    "binary_target_column": "target_binary",
    "model_feature_columns": ["model_text"] + numeric_feature_columns,
    "numeric_feature_columns": numeric_feature_columns,
    "auxiliary_target_columns": AUXILIARY_TARGET_COLUMNS,
    "identity_columns": IDENTITY_COLUMNS,
    "evaluated_identity_columns": EVALUATED_IDENTITY_COLUMNS,
    "submission_id_column": "id",
    "submission_prediction_column": "prediction",
    "test_order_matches_sample_submission": bool(
        np.array_equal(
            test_data["id"].to_numpy(),
            sample_submission["id"].to_numpy(),
        )
    ),
}

with open(
    os.path.join(WORKING_DIR, "preprocessing_metadata.json"),
    "w",
    encoding="utf-8",
) as metadata_file:
    json.dump(preprocessing_metadata, metadata_file, indent=2)

# ---------------------------------------------------------------------
# Model design
# ---------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
base_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = float(coefficient)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return -ctx.coefficient * gradient_output, None


def gradient_reverse(inputs, coefficient):
    return GradientReversalFunction.apply(inputs, coefficient)


class BiasAwareDeberta(nn.Module):
    def __init__(
        self,
        encoder,
        numeric_feature_count,
        auxiliary_target_count=6,
        evaluated_identity_count=9,
        fusion_width=256,
        dropout_probability=0.20,
    ):
        super().__init__()
        self.encoder = encoder
        self.hidden_size = encoder.config.hidden_size

        self.numeric_projection = nn.Sequential(
            nn.LayerNorm(numeric_feature_count),
            nn.Linear(numeric_feature_count, 64),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.fusion = nn.Sequential(
            nn.LayerNorm(self.hidden_size * 2 + 64),
            nn.Linear(self.hidden_size * 2 + 64, fusion_width),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(fusion_width, fusion_width),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.toxicity_head = nn.Linear(
            fusion_width,
            1 + auxiliary_target_count,
        )

        self.identity_adversary = nn.Sequential(
            nn.LayerNorm(fusion_width),
            nn.Linear(fusion_width, fusion_width // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(fusion_width // 2, evaluated_identity_count),
        )

        self._initialize_new_layers()

    def _initialize_new_layers(self):
        for module in (
            self.numeric_projection,
            self.fusion,
            self.toxicity_head,
            self.identity_adversary,
        ):
            for layer in module.modules():
                if isinstance(layer, nn.Linear):
                    nn.init.normal_(layer.weight, mean=0.0, std=0.02)
                    if layer.bias is not None:
                        nn.init.zeros_(layer.bias)

    @staticmethod
    def _masked_mean(hidden_states, attention_mask):
        mask = attention_mask.unsqueeze(-1).to(hidden_states.dtype)
        return (hidden_states * mask).sum(dim=1) / mask.sum(dim=1).clamp_min(1.0)

    def forward(
        self,
        input_ids,
        attention_mask,
        numeric_features,
        adversarial_coefficient=0.0,
    ):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        hidden_states = encoder_outputs.last_hidden_state
        cls_embedding = hidden_states[:, 0]
        mean_embedding = self._masked_mean(hidden_states, attention_mask)
        numeric_embedding = self.numeric_projection(numeric_features)

        fused_embedding = self.fusion(
            torch.cat(
                [cls_embedding, mean_embedding, numeric_embedding],
                dim=-1,
            )
        )

        toxicity_logits = self.toxicity_head(fused_embedding)
        identity_logits = self.identity_adversary(
            gradient_reverse(fused_embedding, adversarial_coefficient)
        )

        return {
            "toxicity_logits": toxicity_logits,
            "target_logit": toxicity_logits[:, 0],
            "auxiliary_logits": toxicity_logits[:, 1:],
            "identity_logits": identity_logits,
        }


class OfficialBiasSurrogateLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight=0.30,
        adversarial_weight=0.08,
        ranking_weight=0.40,
        subgroup_example_weight=1.75,
        pair_temperature=0.35,
    ):
        super().__init__()
        self.auxiliary_weight = float(auxiliary_weight)
        self.adversarial_weight = float(adversarial_weight)
        self.ranking_weight = float(ranking_weight)
        self.subgroup_example_weight = float(subgroup_example_weight)
        self.pair_temperature = float(pair_temperature)

    def _ranking_loss(self, positive_logits, negative_logits):
        if positive_logits.numel() == 0 or negative_logits.numel() == 0:
            return None

        margins = (
            positive_logits[:, None] - negative_logits[None, :]
        ) / self.pair_temperature

        return F.softplus(-margins).mean()

    def _official_regime_ranking_loss(
        self,
        target_logits,
        binary_targets,
        identity_targets,
        identity_observed,
    ):
        ranking_terms = []

        for identity_index in range(identity_targets.size(1)):
            observed = identity_observed[:, identity_index] > 0.5
            in_subgroup = (identity_targets[:, identity_index] >= 0.5) & observed
            in_background = (~in_subgroup) & observed

            subgroup_positive = target_logits[in_subgroup & (binary_targets >= 0.5)]
            subgroup_negative = target_logits[in_subgroup & (binary_targets < 0.5)]
            background_positive = target_logits[in_background & (binary_targets >= 0.5)]
            background_negative = target_logits[in_background & (binary_targets < 0.5)]

            subgroup_auc_surrogate = self._ranking_loss(
                subgroup_positive,
                subgroup_negative,
            )
            bpsn_auc_surrogate = self._ranking_loss(
                background_positive,
                subgroup_negative,
            )
            bnsp_auc_surrogate = self._ranking_loss(
                subgroup_positive,
                background_negative,
            )

            for term in (
                subgroup_auc_surrogate,
                bpsn_auc_surrogate,
                bnsp_auc_surrogate,
            ):
                if term is not None:
                    ranking_terms.append(term)

        if not ranking_terms:
            return target_logits.new_zeros(())

        return torch.stack(ranking_terms).mean()

    def forward(
        self,
        model_outputs,
        target_values,
        auxiliary_targets,
        identity_targets,
        identity_observed,
    ):
        target_values = target_values.float().clamp(0.0, 1.0)
        auxiliary_targets = auxiliary_targets.float().clamp(0.0, 1.0)
        identity_targets = identity_targets.float().clamp(0.0, 1.0)
        identity_observed = identity_observed.float()

        target_logits = model_outputs["target_logit"]

        subgroup_present = (
            ((identity_targets >= 0.5) * identity_observed).sum(dim=1) > 0
        ).float()

        target_weights = 1.0 + (self.subgroup_example_weight - 1.0) * subgroup_present

        primary_bce = F.binary_cross_entropy_with_logits(
            target_logits,
            target_values,
            reduction="none",
        )

        primary_loss = (
            primary_bce * target_weights
        ).sum() / target_weights.sum().clamp_min(1.0)

        auxiliary_loss = F.binary_cross_entropy_with_logits(
            model_outputs["auxiliary_logits"],
            auxiliary_targets,
        )

        identity_bce = F.binary_cross_entropy_with_logits(
            model_outputs["identity_logits"],
            identity_targets,
            reduction="none",
        )

        identity_loss = (
            identity_bce * identity_observed
        ).sum() / identity_observed.sum().clamp_min(1.0)

        binary_targets = (target_values >= 0.5).float()

        ranking_loss = self._official_regime_ranking_loss(
            target_logits=target_logits,
            binary_targets=binary_targets,
            identity_targets=identity_targets,
            identity_observed=identity_observed,
        )

        total_loss = (
            primary_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.adversarial_weight * identity_loss
            + self.ranking_weight * ranking_loss
        )

        return {
            "loss": total_loss,
            "primary_loss": primary_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "identity_loss": identity_loss.detach(),
            "ranking_loss": ranking_loss.detach(),
        }


def build_layerwise_parameter_groups(
    network,
    backbone_learning_rate=1.5e-5,
    head_learning_rate=1.2e-4,
    layerwise_decay=0.92,
    weight_decay=0.01,
):
    no_decay_tokens = ("bias", "LayerNorm.weight", "layer_norm.weight")
    encoder_layer_count = network.encoder.config.num_hidden_layers
    parameter_groups = []

    for parameter_name, parameter in network.named_parameters():
        if not parameter.requires_grad:
            continue

        uses_weight_decay = not any(
            token in parameter_name for token in no_decay_tokens
        )

        parameter_weight_decay = weight_decay if uses_weight_decay else 0.0

        if parameter_name.startswith("encoder."):
            layer_index = 0

            if ".encoder.layer." in parameter_name:
                suffix = parameter_name.split(".encoder.layer.", 1)[1]
                layer_index = int(suffix.split(".", 1)[0]) + 1

            learning_rate = backbone_learning_rate * (
                layerwise_decay ** (encoder_layer_count - layer_index)
            )
        else:
            learning_rate = head_learning_rate

        parameter_groups.append(
            {
                "params": [parameter],
                "lr": learning_rate,
                "weight_decay": parameter_weight_decay,
            }
        )

    return parameter_groups


model = BiasAwareDeberta(
    encoder=base_classifier.deberta,
    numeric_feature_count=len(numeric_feature_columns),
    auxiliary_target_count=len(AUXILIARY_TARGET_COLUMNS),
    evaluated_identity_count=len(EVALUATED_IDENTITY_COLUMNS),
)

criterion = OfficialBiasSurrogateLoss(
    auxiliary_weight=0.30,
    adversarial_weight=0.08,
    ranking_weight=0.40,
    subgroup_example_weight=1.75,
    pair_temperature=0.35,
)

optimizer = AdamW(
    build_layerwise_parameter_groups(model),
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_scaler = GradScaler(enabled=use_cuda_amp)

# Non-reentrant checkpointing avoids reusing freed activations during backward.
# This preserves memory savings while remaining compatible with the custom loss graph.
if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )

if hasattr(model.encoder.config, "use_cache"):
    model.encoder.config.use_cache = False

model.to(device)


# ---------------------------------------------------------------------
# Datasets and loaders
# ---------------------------------------------------------------------
class CommentDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.texts = frame["model_text"].fillna("").astype(str).tolist()
        self.numeric_features = np.ascontiguousarray(
            frame[numeric_feature_columns].to_numpy(
                dtype=np.float32,
                copy=True,
            )
        )
        self.include_labels = include_labels

        if include_labels:
            self.target_values = np.ascontiguousarray(
                frame["target"]
                .fillna(0.0)
                .to_numpy(
                    dtype=np.float32,
                    copy=True,
                )
            )

            self.auxiliary_targets = np.ascontiguousarray(
                frame[AUXILIARY_TARGET_COLUMNS]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )

            self.identity_targets = np.ascontiguousarray(
                frame[EVALUATED_IDENTITY_COLUMNS]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )

            observed_columns = [
                f"{column}_is_labeled" for column in EVALUATED_IDENTITY_COLUMNS
            ]

            self.identity_observed = np.ascontiguousarray(
                frame[observed_columns]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.include_labels:
            return (
                self.texts[index],
                self.numeric_features[index],
                self.target_values[index],
                self.auxiliary_targets[index],
                self.identity_targets[index],
                self.identity_observed[index],
            )

        return self.texts[index], self.numeric_features[index]


class TokenizingCollator:
    def __init__(self, tokenizer_object, max_length):
        self.tokenizer_object = tokenizer_object
        self.max_length = max_length

    def __call__(self, batch):
        texts = [row[0] for row in batch]

        tokenized = self.tokenizer_object(
            texts,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

        result = {
            "input_ids": tokenized["input_ids"],
            "attention_mask": tokenized["attention_mask"],
            "numeric_features": torch.from_numpy(
                np.ascontiguousarray(np.stack([row[1] for row in batch]))
            ),
        }

        if len(batch[0]) == 6:
            result["target_values"] = torch.from_numpy(
                np.asarray([row[2] for row in batch], dtype=np.float32)
            )

            result["auxiliary_targets"] = torch.from_numpy(
                np.ascontiguousarray(np.stack([row[3] for row in batch]))
            )

            result["identity_targets"] = torch.from_numpy(
                np.ascontiguousarray(np.stack([row[4] for row in batch]))
            )

            result["identity_observed"] = torch.from_numpy(
                np.ascontiguousarray(np.stack([row[5] for row in batch]))
            )

        return result


train_dataset = CommentDataset(train_data, include_labels=True)
validation_dataset = CommentDataset(validation_data, include_labels=True)
test_dataset = CommentDataset(test_data, include_labels=False)

collator = TokenizingCollator(tokenizer, MAX_LENGTH)

loader_common = {
    "num_workers": NUM_WORKERS,
    "pin_memory": use_cuda_amp,
    "persistent_workers": NUM_WORKERS > 0,
}

train_generator = torch.Generator()
train_generator.manual_seed(SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=train_generator,
    collate_fn=collator,
    drop_last=False,
    **loader_common,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    collate_fn=collator,
    drop_last=False,
    **loader_common,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    collate_fn=collator,
    drop_last=False,
    **loader_common,
)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_update_steps = max(1, updates_per_epoch * MAX_EPOCHS)
warmup_steps = int(total_update_steps * 0.06)

scheduler = get_cosine_schedule_with_warmup(
    optimizer=optimizer,
    num_warmup_steps=warmup_steps,
    num_training_steps=total_update_steps,
)


# ---------------------------------------------------------------------
# Official competition metric
# ---------------------------------------------------------------------
def official_bias_metric(target_binary, predictions, identity_frame):
    target_binary = np.asarray(target_binary, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if target_binary.shape[0] != predictions.shape[0]:
        raise ValueError("Target and prediction lengths differ.")

    if not np.isfinite(predictions).all():
        raise ValueError("Predictions contain non-finite values.")

    if np.unique(target_binary).size != 2:
        raise ValueError("Overall validation target must contain both classes.")

    overall_auc = float(roc_auc_score(target_binary, predictions))

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_column in EVALUATED_IDENTITY_COLUMNS:
        subgroup = (
            identity_frame[f"{identity_column}_binary"].to_numpy(
                dtype=np.int8, copy=False
            )
            >= 1
        )

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & (target_binary == 0)) | (
            ~subgroup & (target_binary == 1)
        )
        bnsp_mask = (subgroup & (target_binary == 1)) | (
            ~subgroup & (target_binary == 0)
        )

        for metric_name, mask in (
            ("subgroup", subgroup_mask),
            ("bpsn", bpsn_mask),
            ("bnsp", bnsp_mask),
        ):
            subset_labels = target_binary[mask]

            if subset_labels.size == 0 or np.unique(subset_labels).size != 2:
                raise ValueError(
                    f"Official {metric_name} AUC is undefined for identity "
                    f"'{identity_column}' on this validation split."
                )

        subgroup_aucs.append(
            float(
                roc_auc_score(
                    target_binary[subgroup_mask],
                    predictions[subgroup_mask],
                )
            )
        )

        bpsn_aucs.append(
            float(
                roc_auc_score(
                    target_binary[bpsn_mask],
                    predictions[bpsn_mask],
                )
            )
        )

        bnsp_aucs.append(
            float(
                roc_auc_score(
                    target_binary[bnsp_mask],
                    predictions[bnsp_mask],
                )
            )
        )

    def generalized_mean(values, power=-5.0):
        values = np.clip(
            np.asarray(values, dtype=np.float64),
            1e-12,
            1.0,
        )
        return float(np.mean(values**power) ** (1.0 / power))

    subgroup_generalized_mean = generalized_mean(subgroup_aucs)
    bpsn_generalized_mean = generalized_mean(bpsn_aucs)
    bnsp_generalized_mean = generalized_mean(bnsp_aucs)

    final_score = float(
        0.25
        * (
            overall_auc
            + subgroup_generalized_mean
            + bpsn_generalized_mean
            + bnsp_generalized_mean
        )
    )

    return {
        "final_score": final_score,
        "overall_auc": overall_auc,
        "subgroup_auc_generalized_mean": subgroup_generalized_mean,
        "bpsn_auc_generalized_mean": bpsn_generalized_mean,
        "bnsp_auc_generalized_mean": bnsp_generalized_mean,
        "subgroup_aucs": dict(zip(EVALUATED_IDENTITY_COLUMNS, subgroup_aucs)),
        "bpsn_aucs": dict(zip(EVALUATED_IDENTITY_COLUMNS, bpsn_aucs)),
        "bnsp_aucs": dict(zip(EVALUATED_IDENTITY_COLUMNS, bnsp_aucs)),
    }


def move_batch_to_device(batch):
    return {
        name: value.to(device, non_blocking=use_cuda_amp)
        for name, value in batch.items()
    }


def predict_probabilities(data_loader):
    model.eval()
    all_predictions = []

    with torch.inference_mode():
        for batch in data_loader:
            batch = move_batch_to_device(batch)

            with torch.cuda.amp.autocast(enabled=use_cuda_amp):
                outputs = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    numeric_features=batch["numeric_features"],
                    adversarial_coefficient=0.0,
                )

                probabilities = torch.sigmoid(outputs["target_logit"])

            all_predictions.append(probabilities.float().cpu().numpy())

    if not all_predictions:
        raise RuntimeError("Inference produced no predictions.")

    return np.concatenate(all_predictions, axis=0)


# ---------------------------------------------------------------------
# Training, official validation, and inference
# ---------------------------------------------------------------------
best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0
training_history = []

optimizer.zero_grad(set_to_none=True)

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    running_loss = 0.0
    processed_examples = 0

    for batch_index, batch in enumerate(train_loader):
        batch = move_batch_to_device(batch)

        adversarial_progress = (
            (epoch - 1) * len(train_loader) + batch_index + 1
        ) / max(1, MAX_EPOCHS * len(train_loader))

        adversarial_coefficient = min(
            0.20,
            0.20 * (2.0 / (1.0 + math.exp(-10.0 * adversarial_progress)) - 1.0),
        )

        with torch.cuda.amp.autocast(enabled=use_cuda_amp):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
                adversarial_coefficient=adversarial_coefficient,
            )

            loss_components = criterion(
                model_outputs=outputs,
                target_values=batch["target_values"],
                auxiliary_targets=batch["auxiliary_targets"],
                identity_targets=batch["identity_targets"],
                identity_observed=batch["identity_observed"],
            )

            unscaled_loss = loss_components["loss"]
            loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        amp_scaler.scale(loss).backward()

        should_step = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if should_step:
            amp_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                max_norm=1.0,
            )
            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_size = batch["input_ids"].shape[0]
        running_loss += float(unscaled_loss.detach().float().item()) * batch_size
        processed_examples += batch_size

    validation_predictions = predict_probabilities(validation_loader)

    validation_metrics = official_bias_metric(
        validation_data["target_binary"].to_numpy(
            dtype=np.int8,
            copy=False,
        ),
        validation_predictions,
        validation_data,
    )

    epoch_loss = running_loss / max(processed_examples, 1)
    epoch_score = validation_metrics["final_score"]

    epoch_record = {
        "epoch": epoch,
        "training_loss": float(epoch_loss),
        **validation_metrics,
    }

    training_history.append(epoch_record)

    if epoch_score > best_score + 1e-7:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_validation_score": float(best_score),
                "model_state_dict": {
                    key: value.detach().cpu()
                    for key, value in model.state_dict().items()
                },
            },
            BEST_MODEL_PATH,
        )
    else:
        epochs_without_improvement += 1

    bias_auc_mean = np.mean(
        [
            validation_metrics["subgroup_auc_generalized_mean"],
            validation_metrics["bpsn_auc_generalized_mean"],
            validation_metrics["bnsp_auc_generalized_mean"],
        ]
    )

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} "
        f"loss={epoch_loss:.6f} "
        f"official_score={epoch_score:.6f} "
        f"overall_auc={validation_metrics['overall_auc']:.6f} "
        f"bias_auc={bias_auc_mean:.6f}"
    )

    del validation_predictions
    gc.collect()

    if use_cuda_amp:
        torch.cuda.empty_cache()

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if best_epoch < 0 or not os.path.exists(BEST_MODEL_PATH):
    raise RuntimeError("No valid model checkpoint was saved.")

try:
    best_checkpoint = torch.load(
        BEST_MODEL_PATH,
        map_location=device,
        weights_only=True,
    )
except TypeError:
    best_checkpoint = torch.load(
        BEST_MODEL_PATH,
        map_location=device,
    )

model.load_state_dict(best_checkpoint["model_state_dict"], strict=True)
model.to(device)

best_validation_predictions = predict_probabilities(validation_loader)

final_validation_metrics = official_bias_metric(
    validation_data["target_binary"].to_numpy(
        dtype=np.int8,
        copy=False,
    ),
    best_validation_predictions,
    validation_data,
)

score = float(final_validation_metrics["final_score"])

test_predictions = predict_probabilities(test_loader)
test_predictions = np.clip(
    test_predictions.astype(np.float64),
    0.0,
    1.0,
)

if len(test_predictions) != len(test_data):
    raise RuntimeError("Test inference did not produce one prediction per test row.")

if not np.isfinite(test_predictions).all():
    raise RuntimeError("Test predictions contain non-finite values.")

if not np.array_equal(
    test_data["id"].to_numpy(),
    sample_submission["id"].to_numpy(),
):
    raise ValueError("Test rows are not aligned with sample_submission row order.")

submission = pd.DataFrame(
    {
        "id": test_data["id"].to_numpy(
            dtype=np.int64,
            copy=False,
        ),
        "prediction": test_predictions,
    }
)

submission_path = os.path.join(SUBMISSION_DIR, "submission_7d08349335134d04abedae44dc030bbd.csv")
submission.to_csv(
    submission_path,
    index=False,
    float_format="%.10f",
)

if list(submission.columns) != ["id", "prediction"]:
    raise ValueError("Submission columns do not match the required format.")

if len(submission) != len(sample_submission):
    raise ValueError("Submission row count does not match sample_submission.")

with open(METRICS_PATH, "w", encoding="utf-8") as metrics_file:
    json.dump(
        {
            "best_epoch": int(best_epoch),
            "best_checkpoint_score": float(best_score),
            "final_reloaded_validation_metrics": final_validation_metrics,
            "history": training_history,
            "submission_path": submission_path,
        },
        metrics_file,
        indent=2,
    )

print(f"Final Validation Score: {score}")
