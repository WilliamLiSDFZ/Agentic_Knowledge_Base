import gc
import json
import re
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime setup and split-safe data preparation
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

input_dir = Path("./input")
working_dir = Path("./working")
working_dir.mkdir(parents=True, exist_ok=True)

raw_train_df = pd.read_csv(input_dir / "train.csv")
raw_test_df = pd.read_csv(input_dir / "test.csv")

# The runtime-owned split occurs before fitting any transform or augmentation.
train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

del raw_train_df, raw_test_df
gc.collect()

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

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
CONTROL_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
HTML_TAG_PATTERN = re.compile(r"<[^>]{1,200}>")
MULTISPACE_PATTERN = re.compile(r"\s+")

IDENTITY_SURFACE_PATTERN = re.compile(
    r"(?i)\b(?:"
    r"male|female|man|woman|men|women|boy|girl|transgender|trans|gay|lesbian|"
    r"homosexual|bisexual|heterosexual|straight|christian|jewish|jew|muslim|islam|"
    r"hindu|buddhist|atheist|black|white|asian|latino|latina|disab(?:led|ility)|"
    r"autis(?:m|tic)|mental(?:ly)?\s+ill"
    r")\b"
)

COUNTERFACTUAL_TERMS = {
    "black": "white",
    "white": "black",
    "christian": "muslim",
    "christians": "muslims",
    "muslim": "christian",
    "muslims": "christians",
    "jewish": "muslim",
    "gay": "straight",
    "lesbian": "straight",
    "homosexual": "heterosexual",
    "heterosexual": "homosexual",
    "male": "female",
    "female": "male",
    "man": "woman",
    "woman": "man",
    "men": "women",
    "women": "men",
}

COUNTERFACTUAL_PATTERN = re.compile(
    r"\b(" + "|".join(sorted(COUNTERFACTUAL_TERMS, key=len, reverse=True)) + r")\b",
    flags=re.IGNORECASE,
)


def normalize_comment_text(text_series: pd.Series) -> pd.Series:
    """Canonicalize noisy comments while preserving lexical toxicity evidence."""
    text = text_series.fillna("").astype(str).str.normalize("NFKC")
    text = text.str.replace("\r\n", "\n", regex=False).str.replace(
        "\r", "\n", regex=False
    )
    text = text.str.replace(CONTROL_PATTERN, " ", regex=True)
    text = text.str.replace(HTML_TAG_PATTERN, " ", regex=True)
    text = text.str.replace(URL_PATTERN, " <URL> ", regex=True)
    text = text.str.replace(EMAIL_PATTERN, " <EMAIL> ", regex=True)
    text = text.str.replace("&amp;", "&", regex=False)
    text = text.str.replace("&lt;", "<", regex=False)
    text = text.str.replace("&gt;", ">", regex=False)
    text = text.str.replace("&quot;", '"', regex=False)
    text = text.str.replace("&#39;", "'", regex=False)
    text = text.str.replace(MULTISPACE_PATTERN, " ", regex=True).str.strip()
    return text


def build_structural_features(clean_text: pd.Series) -> pd.DataFrame:
    """Build inference-safe text structure features."""
    char_count = clean_text.str.len().astype(np.float32)
    word_count = clean_text.str.count(r"\S+").astype(np.float32)
    alpha_count = clean_text.str.count(r"[A-Za-z]").astype(np.float32)
    upper_count = clean_text.str.count(r"[A-Z]").astype(np.float32)

    features = pd.DataFrame(index=clean_text.index)
    features["feat_log_char_count"] = np.log1p(char_count)
    features["feat_log_word_count"] = np.log1p(word_count)
    features["feat_log_line_count"] = np.log1p(
        clean_text.str.count("\n").astype(np.float32) + 1.0
    )
    features["feat_log_exclamation_count"] = np.log1p(
        clean_text.str.count("!").astype(np.float32)
    )
    features["feat_log_question_count"] = np.log1p(
        clean_text.str.count(r"\?").astype(np.float32)
    )
    features["feat_log_quote_count"] = np.log1p(
        clean_text.str.count(r"""["']""").astype(np.float32)
    )
    features["feat_log_digit_count"] = np.log1p(
        clean_text.str.count(r"\d").astype(np.float32)
    )
    features["feat_log_url_marker_count"] = np.log1p(
        clean_text.str.count(r"<URL>").astype(np.float32)
    )
    features["feat_log_repeat_punctuation"] = np.log1p(
        clean_text.str.count(r"[!?]{2,}|\.{3,}").astype(np.float32)
    )
    features["feat_uppercase_ratio"] = upper_count / np.maximum(alpha_count, 1.0)
    features["feat_mean_token_length"] = char_count / np.maximum(word_count, 1.0)
    features["audit_identity_surface_count"] = clean_text.str.count(
        IDENTITY_SURFACE_PATTERN
    ).astype(np.float32)
    return features.astype(np.float32)


def apply_counterfactual_swap(text: str) -> str | None:
    """Produce one lexical identity counterfactual when a safe substitution exists."""
    if not isinstance(text, str) or not COUNTERFACTUAL_PATTERN.search(text):
        return None

    def replace_match(match: re.Match) -> str:
        original = match.group(0)
        replacement = COUNTERFACTUAL_TERMS[original.lower()]
        if original.isupper():
            return replacement.upper()
        if original.istitle():
            return replacement.title()
        return replacement

    swapped = COUNTERFACTUAL_PATTERN.sub(replace_match, text)
    return swapped if swapped != text else None


for frame in (train_df, valid_df, test_df):
    frame["comment_text"] = normalize_comment_text(frame["comment_text"])
    structural_features = build_structural_features(frame["comment_text"])
    for column in structural_features.columns:
        frame[column] = structural_features[column]
    del structural_features

MODEL_NUMERIC_FEATURE_COLUMNS = [
    "feat_log_char_count",
    "feat_log_word_count",
    "feat_log_line_count",
    "feat_log_exclamation_count",
    "feat_log_question_count",
    "feat_log_quote_count",
    "feat_log_digit_count",
    "feat_log_url_marker_count",
    "feat_log_repeat_punctuation",
    "feat_uppercase_ratio",
    "feat_mean_token_length",
]

train_feature_means = train_df[MODEL_NUMERIC_FEATURE_COLUMNS].mean()
train_feature_stds = (
    train_df[MODEL_NUMERIC_FEATURE_COLUMNS].std().replace(0.0, 1.0).fillna(1.0)
)

for frame in (train_df, valid_df, test_df):
    frame[MODEL_NUMERIC_FEATURE_COLUMNS] = (
        frame[MODEL_NUMERIC_FEATURE_COLUMNS]
        .fillna(train_feature_means)
        .sub(train_feature_means, axis="columns")
        .div(train_feature_stds, axis="columns")
        .clip(-8.0, 8.0)
        .astype(np.float32)
    )

available_identity_columns = [c for c in IDENTITY_COLUMNS if c in train_df.columns]
available_eval_identity_columns = [
    c for c in EVALUATED_IDENTITY_COLUMNS if c in train_df.columns
]

if available_identity_columns:
    identity_values = train_df[available_identity_columns]
    identity_labeled = identity_values.notna().any(axis=1)
    identity_mentioned = identity_values.fillna(0.0).ge(0.5).any(axis=1)

    train_df["training_identity_annotated"] = identity_labeled.astype(np.int8)
    train_df["training_identity_mentioned"] = identity_mentioned.astype(np.int8)

    benign_identity = identity_labeled & identity_mentioned & train_df["target"].lt(0.5)
    toxic_identity = identity_labeled & identity_mentioned & train_df["target"].ge(0.5)

    train_df["fairness_sample_weight"] = (
        1.0
        + 1.50 * benign_identity.astype(np.float32)
        + 0.25 * toxic_identity.astype(np.float32)
    ).astype(np.float32)
else:
    train_df["training_identity_annotated"] = np.int8(0)
    train_df["training_identity_mentioned"] = np.int8(0)
    train_df["fairness_sample_weight"] = np.float32(1.0)

augmentation_columns = [
    "source_id",
    "augmentation_id",
    "comment_text",
    "target",
    "fairness_sample_weight",
]
counterfactual_df = pd.DataFrame(columns=augmentation_columns)

if available_identity_columns:
    cda_mask = (
        train_df["training_identity_annotated"].eq(1)
        & train_df["training_identity_mentioned"].eq(1)
        & train_df["target"].le(0.20)
        & train_df["audit_identity_surface_count"].gt(0)
    )
    cda_source = train_df.loc[
        cda_mask,
        ["id", "comment_text", "target", "fairness_sample_weight"],
    ].copy()

    if not cda_source.empty:
        cda_source["_stable_hash"] = pd.util.hash_pandas_object(
            cda_source["id"].astype(str), index=False
        ).to_numpy(dtype=np.uint64)

        cda_source = cda_source.nsmallest(150_000, "_stable_hash")
        cda_source["counterfactual_text"] = cda_source["comment_text"].map(
            apply_counterfactual_swap
        )
        cda_source = cda_source.dropna(subset=["counterfactual_text"])

        if not cda_source.empty:
            counterfactual_df = pd.DataFrame(
                {
                    "source_id": cda_source["id"].astype(str).to_numpy(),
                    "augmentation_id": (
                        "cf_" + cda_source["id"].astype(str)
                    ).to_numpy(),
                    "comment_text": cda_source["counterfactual_text"].to_numpy(),
                    "target": cda_source["target"].astype(np.float32).to_numpy(),
                    "fairness_sample_weight": (
                        cda_source["fairness_sample_weight"]
                        .astype(np.float32)
                        .to_numpy()
                    ),
                }
            )

    del cda_source
    gc.collect()

train_keep_columns = (
    ["id", "target", "comment_text"]
    + MODEL_NUMERIC_FEATURE_COLUMNS
    + [
        "audit_identity_surface_count",
        "training_identity_annotated",
        "training_identity_mentioned",
        "fairness_sample_weight",
    ]
    + available_identity_columns
)
valid_keep_columns = (
    ["id", "target", "comment_text"]
    + MODEL_NUMERIC_FEATURE_COLUMNS
    + ["audit_identity_surface_count"]
    + [c for c in available_eval_identity_columns if c in valid_df.columns]
)
test_keep_columns = (
    ["id", "comment_text"]
    + MODEL_NUMERIC_FEATURE_COLUMNS
    + ["audit_identity_surface_count"]
)

train_keep_columns = list(
    dict.fromkeys([c for c in train_keep_columns if c in train_df.columns])
)
valid_keep_columns = list(
    dict.fromkeys([c for c in valid_keep_columns if c in valid_df.columns])
)
test_keep_columns = list(
    dict.fromkeys([c for c in test_keep_columns if c in test_df.columns])
)

train_df = train_df.loc[:, train_keep_columns].copy()
valid_df = valid_df.loc[:, valid_keep_columns].copy()
test_df = test_df.loc[:, test_keep_columns].copy()

train_df.to_pickle(working_dir / "train_prepared.pkl")
valid_df.to_pickle(working_dir / "valid_prepared.pkl")
test_df.to_pickle(working_dir / "test_prepared.pkl")
counterfactual_df.to_pickle(working_dir / "counterfactual_benign_identity_prepared.pkl")

feature_manifest = {
    "text_column": "comment_text",
    "model_numeric_feature_columns": MODEL_NUMERIC_FEATURE_COLUMNS,
    "audit_only_feature_columns": ["audit_identity_surface_count"],
    "training_only_supervision_columns": [
        "training_identity_annotated",
        "training_identity_mentioned",
        "fairness_sample_weight",
    ],
    "identity_columns_available_in_train": available_identity_columns,
    "evaluation_identity_columns_available": available_eval_identity_columns,
    "numeric_feature_means": {k: float(v) for k, v in train_feature_means.items()},
    "numeric_feature_stds": {k: float(v) for k, v in train_feature_stds.items()},
    "counterfactual_rows": int(len(counterfactual_df)),
    "split_source": "CandidateSession.split",
    "validation_metric_for_downstream_selection": (
        "official_jigsaw_overall_plus_bias_generalized_mean_auc"
    ),
}

with open(working_dir / "feature_manifest.json", "w", encoding="utf-8") as file:
    json.dump(feature_manifest, file, indent=2, sort_keys=True)

# ---------------------------------------------------------------------
# ModernBERT model and metric-aligned objective
# ---------------------------------------------------------------------
model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    num_labels=1,
)
model.config.problem_type = "regression"

for parameter in model.parameters():
    parameter.requires_grad_(False)

for parameter in model.classifier.parameters():
    parameter.requires_grad_(True)


class MetricAlignedRobustRankingLoss(nn.Module):
    """
    Combines soft-label BCE with ranking losses for overall, subgroup,
    BPSN, and BNSP discrimination.
    """

    def __init__(
        self,
        bce_weight: float = 0.30,
        robust_temperature: float = 0.10,
        rank_temperature: float = 1.0,
        max_pairs_per_component: int = 192,
    ) -> None:
        super().__init__()
        self.bce_weight = float(bce_weight)
        self.robust_temperature = float(robust_temperature)
        self.rank_temperature = float(rank_temperature)
        self.max_pairs_per_component = int(max_pairs_per_component)

    def _pairwise_ranking_loss(
        self,
        logits: torch.Tensor,
        positive_mask: torch.Tensor,
        negative_mask: torch.Tensor,
        sample_weight: torch.Tensor,
    ) -> torch.Tensor | None:
        positive_indices = torch.where(positive_mask)[0]
        negative_indices = torch.where(negative_mask)[0]

        if positive_indices.numel() == 0 or negative_indices.numel() == 0:
            return None

        n_pairs = min(
            int(positive_indices.numel()),
            int(negative_indices.numel()),
            self.max_pairs_per_component,
        )
        if n_pairs <= 0:
            return None

        positive_order = torch.randperm(
            positive_indices.numel(),
            device=logits.device,
        )[:n_pairs]
        negative_order = torch.randperm(
            negative_indices.numel(),
            device=logits.device,
        )[:n_pairs]

        pos_idx = positive_indices[positive_order]
        neg_idx = negative_indices[negative_order]

        margins = (logits[pos_idx] - logits[neg_idx]) / self.rank_temperature
        pair_losses = F.softplus(-margins)

        pair_weights = torch.sqrt(
            sample_weight[pos_idx].clamp_min(1e-4)
            * sample_weight[neg_idx].clamp_min(1e-4)
        )
        return (pair_losses * pair_weights).sum() / pair_weights.sum().clamp_min(1e-6)

    def forward(
        self,
        logits: torch.Tensor,
        soft_targets: torch.Tensor,
        identity_values: torch.Tensor | None = None,
        sample_weight: torch.Tensor | None = None,
    ) -> torch.Tensor:
        logits = logits.reshape(-1).float()
        soft_targets = soft_targets.reshape(-1).float().clamp(0.0, 1.0)

        if sample_weight is None:
            sample_weight = torch.ones_like(soft_targets)
        else:
            sample_weight = sample_weight.reshape(-1).float().clamp_min(1e-4)

        pointwise_loss = F.binary_cross_entropy_with_logits(
            logits,
            soft_targets,
            reduction="none",
        )
        bce_loss = (
            pointwise_loss * sample_weight
        ).sum() / sample_weight.sum().clamp_min(1e-6)

        binary_targets = soft_targets.ge(0.5)
        overall_rank_loss = self._pairwise_ranking_loss(
            logits=logits,
            positive_mask=binary_targets,
            negative_mask=~binary_targets,
            sample_weight=sample_weight,
        )
        if overall_rank_loss is None:
            overall_rank_loss = torch.zeros(
                (),
                device=logits.device,
                dtype=logits.dtype,
            )

        bias_component_losses = []

        if identity_values is not None and identity_values.numel() > 0:
            identity_values = identity_values.to(logits.device).float()
            if identity_values.ndim == 1:
                identity_values = identity_values.unsqueeze(1)

            for identity_index in range(identity_values.shape[1]):
                identity_column = identity_values[:, identity_index]
                identity_observed = torch.isfinite(identity_column)
                subgroup = identity_observed & identity_column.ge(0.5)
                background = identity_observed & ~subgroup

                subgroup_auc_loss = self._pairwise_ranking_loss(
                    logits=logits,
                    positive_mask=subgroup & binary_targets,
                    negative_mask=subgroup & ~binary_targets,
                    sample_weight=sample_weight,
                )
                if subgroup_auc_loss is not None:
                    bias_component_losses.append(subgroup_auc_loss)

                bpsn_auc_loss = self._pairwise_ranking_loss(
                    logits=logits,
                    positive_mask=background & binary_targets,
                    negative_mask=subgroup & ~binary_targets,
                    sample_weight=sample_weight,
                )
                if bpsn_auc_loss is not None:
                    bias_component_losses.append(bpsn_auc_loss)

                bnsp_auc_loss = self._pairwise_ranking_loss(
                    logits=logits,
                    positive_mask=subgroup & binary_targets,
                    negative_mask=background & ~binary_targets,
                    sample_weight=sample_weight,
                )
                if bnsp_auc_loss is not None:
                    bias_component_losses.append(bnsp_auc_loss)

        if bias_component_losses:
            component_tensor = torch.stack(bias_component_losses)
            robust_bias_loss = self.robust_temperature * torch.logsumexp(
                component_tensor / self.robust_temperature,
                dim=0,
            )
            rank_loss = 0.25 * overall_rank_loss + 0.75 * robust_bias_loss
        else:
            rank_loss = overall_rank_loss

        return self.bce_weight * bce_loss + (1.0 - self.bce_weight) * rank_loss


criterion = MetricAlignedRobustRankingLoss(
    bce_weight=0.30,
    robust_temperature=0.10,
    rank_temperature=1.0,
    max_pairs_per_component=192,
)

no_decay_terms = (
    "bias",
    "norm.weight",
    "norm.bias",
    "layernorm.weight",
    "layernorm.bias",
)
head_terms = ("classifier", "head", "score")

head_decay = []
head_no_decay = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = any(term in parameter_name.lower() for term in no_decay_terms)
    is_head = any(term in parameter_name.lower() for term in head_terms)

    if not is_head:
        raise RuntimeError(
            f"Only classifier/head parameters may be trainable, got: {parameter_name}"
        )

    if is_no_decay:
        head_no_decay.append(parameter)
    else:
        head_decay.append(parameter)

trainable_parameters = head_decay + head_no_decay

optimizer = AdamW(
    [
        {"params": head_decay, "lr": 3.0e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 3.0e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

# ---------------------------------------------------------------------
# Training, official validation, checkpointing, and runtime submission
# ---------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

amp_enabled = torch.cuda.is_available()
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)

MAX_SEQUENCE_LENGTH = 384
TRAIN_BATCH_SIZE = 32
INFERENCE_BATCH_SIZE = 12
GRADIENT_ACCUMULATION_STEPS = 1
NUM_WORKERS = 2
MAX_EPOCHS = 3

official_identity_columns = [
    column for column in available_eval_identity_columns if column in train_df.columns
]

original_texts = (
    train_df["comment_text"].fillna("").astype(str).to_numpy(dtype=object, copy=True)
)
original_targets = train_df["target"].astype(np.float32).to_numpy(copy=True)
original_weights = (
    train_df["fairness_sample_weight"]
    .fillna(1.0)
    .astype(np.float32)
    .to_numpy(copy=True)
)

if official_identity_columns:
    original_identity_values = train_df[official_identity_columns].to_numpy(
        dtype=np.float32,
        copy=True,
    )
else:
    original_identity_values = np.empty((len(train_df), 0), dtype=np.float32)

if len(counterfactual_df) > 0:
    counterfactual_texts = (
        counterfactual_df["comment_text"]
        .fillna("")
        .astype(str)
        .to_numpy(dtype=object, copy=True)
    )
    counterfactual_targets = (
        counterfactual_df["target"].astype(np.float32).to_numpy(copy=True)
    )
    counterfactual_weights = (
        counterfactual_df["fairness_sample_weight"]
        .fillna(1.0)
        .astype(np.float32)
        .to_numpy(copy=True)
    )
    counterfactual_identity_values = np.full(
        (len(counterfactual_df), len(official_identity_columns)),
        np.nan,
        dtype=np.float32,
    )

    training_texts = np.concatenate([original_texts, counterfactual_texts])
    training_targets = np.concatenate([original_targets, counterfactual_targets])
    training_weights = np.concatenate([original_weights, counterfactual_weights])
    training_identity_values = np.concatenate(
        [original_identity_values, counterfactual_identity_values],
        axis=0,
    )
else:
    training_texts = original_texts
    training_targets = original_targets
    training_weights = original_weights
    training_identity_values = original_identity_values


class PreparedToxicityDataset(Dataset):
    def __init__(self, texts, targets, weights, identity_values):
        self.texts = texts
        self.targets = targets
        self.weights = weights
        self.identity_values = identity_values

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.targets[index],
            self.weights[index],
            self.identity_values[index],
        )


training_dataset = PreparedToxicityDataset(
    texts=training_texts,
    targets=training_targets,
    weights=training_weights,
    identity_values=training_identity_values,
)

loader_kwargs = {
    "batch_size": TRAIN_BATCH_SIZE,
    "shuffle": True,
    "num_workers": NUM_WORKERS,
    "pin_memory": device.type == "cuda",
    "drop_last": False,
}

if NUM_WORKERS > 0:
    loader_kwargs["persistent_workers"] = True
    loader_kwargs["prefetch_factor"] = 2


def tokenize_to_device(text_batch):
    encoded = tokenizer(
        list(text_batch),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )
    encoded.pop("token_type_ids", None)
    return {key: value.to(device, non_blocking=True) for key, value in encoded.items()}


def predict_rows(frame: pd.DataFrame, positional_indices: np.ndarray) -> np.ndarray:
    positional_indices = np.asarray(positional_indices, dtype=np.int64)

    if positional_indices.ndim != 1:
        raise ValueError("Prediction callback indices must be one-dimensional.")

    if len(positional_indices) == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(frame):
        raise IndexError("Prediction callback received an out-of-range index.")

    was_training = model.training
    model.eval()
    prediction_chunks = []

    try:
        with torch.inference_mode():
            for start in range(0, len(positional_indices), INFERENCE_BATCH_SIZE):
                batch_positions = positional_indices[
                    start : start + INFERENCE_BATCH_SIZE
                ]
                text_batch = (
                    frame["comment_text"]
                    .iloc[batch_positions]
                    .fillna("")
                    .astype(str)
                    .tolist()
                )

                encoded = tokenize_to_device(text_batch)

                with torch.cuda.amp.autocast(enabled=amp_enabled):
                    logits = model(**encoded).logits.reshape(-1)

                prediction_chunks.append(torch.sigmoid(logits).float().cpu().numpy())
    finally:
        model.train(was_training)

    return np.concatenate(prediction_chunks).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_rows(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_rows(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
            "prediction_activation": "sigmoid",
            "identity_columns_for_training_loss": official_identity_columns,
        },
        checkpoint_dir / "model_state.pt",
    )

    model.config.save_pretrained(checkpoint_dir / "model_config")
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    inference_state = {
        "text_column": "comment_text",
        "max_sequence_length": MAX_SEQUENCE_LENGTH,
        "prediction_activation": "sigmoid",
        "identity_columns_for_training_loss": official_identity_columns,
    }

    with open(
        checkpoint_dir / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(inference_state, file, indent=2, sort_keys=True)

    prepared_manifest = working_dir / "feature_manifest.json"
    if prepared_manifest.exists():
        shutil.copy2(prepared_manifest, checkpoint_dir / "feature_manifest.json")


def load_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_payload = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=device,
    )
    model.load_state_dict(checkpoint_payload["model_state_dict"], strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_requested = False
total_optimizer_updates = 0

for epoch in range(MAX_EPOCHS):
    model.train()
    epoch_loader = DataLoader(training_dataset, **loader_kwargs)
    epoch_loss_sum = 0.0
    epoch_optimizer_updates = 0

    for batch_index, (
        text_batch,
        target_batch,
        weight_batch,
        identity_batch,
    ) in enumerate(epoch_loader):
        encoded = tokenize_to_device(text_batch)
        soft_targets = target_batch.to(device, non_blocking=True).float()
        sample_weights = weight_batch.to(device, non_blocking=True).float()
        identity_values = identity_batch.to(device, non_blocking=True).float()

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            logits = model(**encoded).logits.reshape(-1)
            loss = criterion(
                logits=logits,
                soft_targets=soft_targets,
                identity_values=identity_values,
                sample_weight=sample_weights,
            )
            scaled_loss = loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(loss):
            raise FloatingPointError("Encountered a non-finite metric-aligned loss.")

        grad_scaler.scale(scaled_loss).backward()
        epoch_loss_sum += float(loss.detach().cpu())

        is_accumulation_boundary = (
            batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0 or (batch_index + 1) == len(epoch_loader)

        if not is_accumulation_boundary:
            continue

        grad_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(trainable_parameters, max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        total_optimizer_updates += 1
        epoch_optimizer_updates += 1

        stop_requested = session.step()
        if stop_requested:
            break

    mean_epoch_loss = epoch_loss_sum / max(epoch_optimizer_updates, 1)
    print(
        f"epoch={epoch + 1} optimizer_updates={epoch_optimizer_updates} "
        f"total_updates={total_optimizer_updates} "
        f"train_loss={mean_epoch_loss:.6f} completed={not stop_requested}"
    )

    if stop_requested:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
