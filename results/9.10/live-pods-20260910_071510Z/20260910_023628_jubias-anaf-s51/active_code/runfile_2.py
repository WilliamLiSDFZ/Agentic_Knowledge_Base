import os
os.sched_setaffinity(0, {69, 70})
import gc
import html
import json
import math
import os

# Avoid CUDA allocator fragmentation when another process occupies GPU memory.
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import re
import unicodedata
import warnings
from pathlib import Path
from typing import Dict, Optional

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedShuffleSplit
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

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
PROCESSED_DIR = WORKING_DIR / "processed_toxicity"
CHECKPOINT_DIR = WORKING_DIR / "checkpoints"
SUBMISSION_DIR = Path("./submission")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

MAX_LENGTH = 512
TRAIN_BATCH_SIZE = 8
EVAL_BATCH_SIZE = 16
GRADIENT_ACCUMULATION_STEPS = 4
NUM_EPOCHS = 1
NUM_WORKERS = max(2, min(4, (os.cpu_count() or 2) // 2))
MAX_GRAD_NORM = 1.0
WARMUP_RATIO = 0.05

torch.manual_seed(SEED)
np.random.seed(SEED)

if torch.cuda.is_available():
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

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

TRAIN_COLUMNS = (
    [
        "id",
        "comment_text",
        "target",
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + IDENTITY_COLUMNS
    + AUXILIARY_TARGET_COLUMNS
)

STYLE_FEATURE_COLUMNS = [
    "log_char_count",
    "log_word_count",
    "log_exclamation_count",
    "log_question_count",
    "log_sentence_end_count",
    "uppercase_ratio",
    "digit_ratio",
    "punctuation_ratio",
    "url_count",
    "email_count",
    "toxic_lexicon_count",
    "identity_lexicon_count",
    "repeated_punctuation",
]

TOXIC_LEXICON_PATTERN = re.compile(
    r"\b(?:idiot|moron|stupid|dumb|hate|hateful|racist|bigot|bigoted|"
    r"disgusting|pathetic|trash|scum|loser|liar|kill|murder|rape|"
    r"fascist|nazi|terrorist|bastard|asshole|bitch)\b",
    flags=re.IGNORECASE,
)

IDENTITY_LEXICON_PATTERN = re.compile(
    r"\b(?:man|men|woman|women|male|female|boy|boys|girl|girls|"
    r"gay|lesbian|homosexual|bisexual|transgender|trans|straight|heterosexual|"
    r"christian|jewish|muslim|islamic|hindu|buddhist|atheist|"
    r"black|white|asian|latino|latina|racial|disability|disabled|autistic)\b",
    flags=re.IGNORECASE,
)

COUNTERFACTUAL_MAP = {
    "male": "female",
    "female": "male",
    "man": "woman",
    "woman": "man",
    "men": "women",
    "women": "men",
    "boy": "girl",
    "girl": "boy",
    "boys": "girls",
    "girls": "boys",
    "christian": "muslim",
    "muslim": "christian",
    "jewish": "muslim",
    "black": "white",
    "white": "black",
    "asian": "latino",
    "latino": "asian",
    "latina": "asian",
    "gay": "straight",
    "lesbian": "heterosexual",
    "homosexual": "heterosexual",
    "heterosexual": "homosexual",
    "transgender": "cisgender",
}

COUNTERFACTUAL_PATTERN = re.compile(
    r"\b("
    + "|".join(sorted(map(re.escape, COUNTERFACTUAL_MAP), key=len, reverse=True))
    + r")\b",
    flags=re.IGNORECASE,
)


def find_input_file(filename: str) -> Path:
    direct_path = INPUT_DIR / filename
    if direct_path.exists():
        return direct_path

    matches = list(INPUT_DIR.rglob(filename))
    if not matches:
        raise FileNotFoundError(
            f"Could not locate {filename} under {INPUT_DIR.resolve()}"
        )
    return matches[0]


def normalize_text(text_series: pd.Series) -> pd.Series:
    text = text_series.astype("string").fillna("")
    text = text.map(
        lambda value: unicodedata.normalize("NFKC", html.unescape(str(value)))
    )
    text = text.str.replace(
        r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b",
        " [EMAIL] ",
        regex=True,
    )
    text = text.str.replace(
        r"(?i)\b(?:https?://|www\.)\S+",
        " [URL] ",
        regex=True,
    )
    text = text.str.replace(r"<[^>]+>", " ", regex=True)
    text = text.str.replace("\u200b", " ", regex=False)
    text = text.str.replace("\r\n", "\n", regex=False)
    text = text.str.replace("\r", "\n", regex=False)
    text = text.str.replace(r"\s+", " ", regex=True)
    return text.str.strip().astype(str)


def duplicate_group_key(text_series: pd.Series) -> pd.Series:
    text = text_series.astype("string").fillna("")
    text = text.map(lambda value: unicodedata.normalize("NFKC", str(value)))
    return text.str.lower().str.replace(r"\s+", " ", regex=True).str.strip()


def build_style_features(model_text: pd.Series) -> pd.DataFrame:
    char_count = model_text.str.len().astype(np.float32)
    word_count = model_text.str.count(r"\b\w+\b").astype(np.float32)
    uppercase_count = model_text.str.count(r"[A-Z]").astype(np.float32)
    alphabetic_count = model_text.str.count(r"[A-Za-z]").astype(np.float32)
    digit_count = model_text.str.count(r"\d").astype(np.float32)
    punctuation_count = model_text.str.count(r"[^\w\s]").astype(np.float32)

    features = pd.DataFrame(index=model_text.index)
    features["log_char_count"] = np.log1p(char_count)
    features["log_word_count"] = np.log1p(word_count)
    features["log_exclamation_count"] = np.log1p(
        model_text.str.count("!").astype(np.float32)
    )
    features["log_question_count"] = np.log1p(
        model_text.str.count(r"\?").astype(np.float32)
    )
    features["log_sentence_end_count"] = np.log1p(
        model_text.str.count(r"[.!?]").astype(np.float32)
    )
    features["uppercase_ratio"] = uppercase_count / np.maximum(alphabetic_count, 1.0)
    features["digit_ratio"] = digit_count / np.maximum(char_count, 1.0)
    features["punctuation_ratio"] = punctuation_count / np.maximum(char_count, 1.0)
    features["url_count"] = model_text.str.count(r"\[URL\]").astype(np.float32)
    features["email_count"] = model_text.str.count(r"\[EMAIL\]").astype(np.float32)
    features["toxic_lexicon_count"] = model_text.str.count(
        TOXIC_LEXICON_PATTERN
    ).astype(np.float32)
    features["identity_lexicon_count"] = model_text.str.count(
        IDENTITY_LEXICON_PATTERN
    ).astype(np.float32)
    features["repeated_punctuation"] = model_text.str.contains(
        r"([!?.,])\1{2,}",
        regex=True,
    ).astype(np.float32)

    return (
        features[STYLE_FEATURE_COLUMNS]
        .replace([np.inf, -np.inf], 0.0)
        .fillna(0.0)
        .astype(np.float32)
    )


def swap_identity_terms(text: str) -> str:
    def replace_match(match: re.Match) -> str:
        return COUNTERFACTUAL_MAP[match.group(0).lower()]

    return COUNTERFACTUAL_PATTERN.sub(replace_match, text)


def make_group_isolated_split(frame: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    group_text = duplicate_group_key(frame["comment_text"])
    group_codes, _ = pd.factorize(group_text, sort=False)
    group_codes = group_codes.astype(np.int32, copy=False)
    n_groups = int(group_codes.max()) + 1

    group_toxic = np.zeros(n_groups, dtype=np.uint8)
    row_toxic = (frame["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.uint8)
    np.maximum.at(group_toxic, group_codes, row_toxic)

    metric_identity = (
        frame[METRIC_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
    )
    group_identity = np.zeros(
        (n_groups, len(METRIC_IDENTITY_COLUMNS)),
        dtype=np.uint8,
    )

    for identity_index in range(len(METRIC_IDENTITY_COLUMNS)):
        np.maximum.at(
            group_identity[:, identity_index],
            group_codes,
            metric_identity[:, identity_index],
        )

    identity_prevalence = group_identity.mean(axis=0)
    identity_priority = np.where(
        group_identity == 1,
        identity_prevalence[None, :],
        2.0,
    )

    has_identity = group_identity.any(axis=1)
    primary_identity = np.zeros(n_groups, dtype=np.int16)
    primary_identity[has_identity] = (
        np.argmin(identity_priority[has_identity], axis=1).astype(np.int16) + 1
    )

    group_strata = (primary_identity * 2 + group_toxic).astype(np.int32)
    group_index = np.arange(n_groups)

    try:
        splitter = StratifiedShuffleSplit(
            n_splits=1,
            test_size=0.10,
            random_state=SEED,
        )
        train_group_indices, valid_group_indices = next(
            splitter.split(group_index, group_strata)
        )
    except ValueError:
        rng = np.random.RandomState(SEED)
        shuffled_groups = rng.permutation(group_index)
        valid_size = max(1, int(round(0.10 * n_groups)))
        valid_group_indices = shuffled_groups[:valid_size]
        train_group_indices = shuffled_groups[valid_size:]

    is_validation_group = np.zeros(n_groups, dtype=bool)
    is_validation_group[valid_group_indices] = True
    validation_mask = is_validation_group[group_codes]
    train_mask = ~validation_mask

    if not train_mask.any() or not validation_mask.any():
        raise RuntimeError(
            "Group-isolated split unexpectedly produced an empty partition."
        )

    return np.flatnonzero(train_mask), np.flatnonzero(validation_mask)


def assemble_processed_frame(
    raw_frame: pd.DataFrame,
    model_text: pd.Series,
    raw_style_features: pd.DataFrame,
    fitted_scaler: StandardScaler,
    include_labels: bool,
) -> pd.DataFrame:
    scaled_features = fitted_scaler.transform(
        raw_style_features.to_numpy(dtype=np.float32, copy=False)
    ).astype(np.float32)

    scaled_feature_frame = pd.DataFrame(
        scaled_features,
        index=raw_frame.index,
        columns=[f"{column}_z" for column in STYLE_FEATURE_COLUMNS],
    )

    output_parts = [
        raw_frame[["id"]].reset_index(drop=True),
        pd.DataFrame(
            {"model_text": model_text.to_numpy()},
            index=raw_frame.index,
        ).reset_index(drop=True),
        scaled_feature_frame.reset_index(drop=True),
    ]

    if include_labels:
        labels = raw_frame[
            ["target", "toxicity_annotator_count"]
            + AUXILIARY_TARGET_COLUMNS
            + IDENTITY_COLUMNS
        ].copy()
        labels[IDENTITY_COLUMNS] = labels[IDENTITY_COLUMNS].fillna(0.0)
        labels = labels.astype(np.float32)
        labels["target_binary"] = (labels["target"] >= 0.5).astype(np.int8)
        labels["identity_labeled"] = (
            raw_frame["identity_annotator_count"].to_numpy(dtype=np.int32) > 0
        ).astype(np.int8)
        labels["subgroup_any"] = (
            labels[IDENTITY_COLUMNS].to_numpy(dtype=np.float32).max(axis=1) >= 0.5
        ).astype(np.int8)
        output_parts.append(labels.reset_index(drop=True))

    return pd.concat(output_parts, axis=1)


def save_frame(frame: pd.DataFrame, stem: str) -> str:
    parquet_path = PROCESSED_DIR / f"{stem}.parquet"
    try:
        frame.to_parquet(
            parquet_path,
            index=False,
            engine="pyarrow",
            compression="zstd",
        )
        return str(parquet_path)
    except Exception:
        pickle_path = PROCESSED_DIR / f"{stem}.pkl"
        frame.to_pickle(pickle_path)
        return str(pickle_path)


train_path = find_input_file("train.csv")
test_path = find_input_file("test.csv")

train_raw = pd.read_csv(train_path, usecols=TRAIN_COLUMNS, low_memory=False)
test_raw = pd.read_csv(test_path, usecols=["id", "comment_text"], low_memory=False)

if train_raw["id"].duplicated().any() or test_raw["id"].duplicated().any():
    raise ValueError("Duplicate IDs were found; IDs must uniquely identify rows.")

if train_raw["target"].isna().any():
    raise ValueError("Training target contains missing values.")

train_indices, valid_indices = make_group_isolated_split(train_raw)

train_partition = train_raw.iloc[train_indices].copy()
valid_partition = train_raw.iloc[valid_indices].copy()

del train_indices, valid_indices, train_raw
gc.collect()

train_text = normalize_text(train_partition["comment_text"])
train_style = build_style_features(train_text)

style_scaler = StandardScaler()
style_scaler.fit(train_style.to_numpy(dtype=np.float32, copy=False))

train_processed = assemble_processed_frame(
    raw_frame=train_partition,
    model_text=train_text,
    raw_style_features=train_style,
    fitted_scaler=style_scaler,
    include_labels=True,
)

valid_text = normalize_text(valid_partition["comment_text"])
valid_style = build_style_features(valid_text)

valid_processed = assemble_processed_frame(
    raw_frame=valid_partition,
    model_text=valid_text,
    raw_style_features=valid_style,
    fitted_scaler=style_scaler,
    include_labels=True,
)

test_text = normalize_text(test_raw["comment_text"])
test_style = build_style_features(test_text)

test_processed = assemble_processed_frame(
    raw_frame=test_raw,
    model_text=test_text,
    raw_style_features=test_style,
    fitted_scaler=style_scaler,
    include_labels=False,
)

counterfactual_candidate = (
    (train_processed["target_binary"].to_numpy() == 0)
    & (train_processed["subgroup_any"].to_numpy() == 1)
    & train_processed["model_text"]
    .str.contains(COUNTERFACTUAL_PATTERN, regex=True)
    .to_numpy()
)

counterfactual_augmentation = train_processed.loc[
    counterfactual_candidate,
    ["id", "model_text", "target", "target_binary"]
    + [f"{column}_z" for column in STYLE_FEATURE_COLUMNS],
].copy()

if len(counterfactual_augmentation) > 0:
    counterfactual_augmentation = counterfactual_augmentation.rename(
        columns={"id": "source_id"}
    )
    original_counterfactual_text = counterfactual_augmentation["model_text"].to_numpy(
        copy=True
    )

    counterfactual_augmentation["model_text"] = counterfactual_augmentation[
        "model_text"
    ].map(swap_identity_terms)

    changed_mask = (
        counterfactual_augmentation["model_text"].to_numpy()
        != original_counterfactual_text
    )

    counterfactual_augmentation = counterfactual_augmentation.loc[
        changed_mask
    ].reset_index(drop=True)

    if len(counterfactual_augmentation) > 0:
        augmented_style = build_style_features(
            counterfactual_augmentation["model_text"]
        )
        augmented_scaled = style_scaler.transform(
            augmented_style.to_numpy(dtype=np.float32, copy=False)
        ).astype(np.float32)

        counterfactual_augmentation[
            [f"{column}_z" for column in STYLE_FEATURE_COLUMNS]
        ] = augmented_scaled

counterfactual_augmentation["is_counterfactual"] = np.int8(1)
train_processed["is_counterfactual"] = np.int8(0)
valid_processed["is_counterfactual"] = np.int8(0)
test_processed["is_counterfactual"] = np.int8(0)

scaler_path = PROCESSED_DIR / "style_feature_scaler.joblib"
joblib.dump(
    {
        "scaler": style_scaler,
        "input_columns": STYLE_FEATURE_COLUMNS,
        "output_columns": [f"{column}_z" for column in STYLE_FEATURE_COLUMNS],
    },
    scaler_path,
)

train_output_path = save_frame(train_processed, "train_processed")
valid_output_path = save_frame(valid_processed, "validation_processed")
test_output_path = save_frame(test_processed, "test_processed")
augmentation_output_path = save_frame(
    counterfactual_augmentation,
    "train_counterfactual_augmentation",
)

manifest = {
    "seed": SEED,
    "split_strategy": "duplicate-group-isolated identity-aware stratified holdout",
    "validation_fraction": 0.10,
    "text_column": "model_text",
    "target_column": "target",
    "binary_target_column": "target_binary",
    "identity_columns": IDENTITY_COLUMNS,
    "official_metric_identity_columns": METRIC_IDENTITY_COLUMNS,
    "auxiliary_target_columns": AUXILIARY_TARGET_COLUMNS,
    "style_feature_columns": [f"{column}_z" for column in STYLE_FEATURE_COLUMNS],
    "scaler_path": str(scaler_path),
    "train_path": train_output_path,
    "validation_path": valid_output_path,
    "test_path": test_output_path,
    "counterfactual_augmentation_path": augmentation_output_path,
    "train_rows": int(len(train_processed)),
    "validation_rows": int(len(valid_processed)),
    "test_rows": int(len(test_processed)),
    "counterfactual_rows": int(len(counterfactual_augmentation)),
}

with open(PROCESSED_DIR / "manifest.json", "w", encoding="utf-8") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

# The base encoder preserves the pretrained ModernBERT text-classification approach
# while leaving sufficient memory for optimizer state, gradients, and inference.
model_id = "answerdotai/ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)
base_model = model

NUM_STYLE_FEATURES = len(STYLE_FEATURE_COLUMNS)
NUM_IDENTITY_COLUMNS = len(IDENTITY_COLUMNS)


class FairToxicityModernBERT(nn.Module):
    def __init__(
        self,
        pretrained_classifier: ModernBertForSequenceClassification,
        num_style_features: int,
        dropout: float = 0.20,
    ) -> None:
        super().__init__()
        self.encoder = pretrained_classifier.model
        hidden_size = pretrained_classifier.config.hidden_size

        self.style_encoder = nn.Sequential(
            nn.LayerNorm(num_style_features),
            nn.Linear(num_style_features, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, hidden_size),
            nn.GELU(),
        )

        self.text_norm = nn.LayerNorm(hidden_size)
        self.style_norm = nn.LayerNorm(hidden_size)

        self.fusion_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )

        self.fusion_projection = nn.Sequential(
            nn.Linear(hidden_size * 3, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.LayerNorm(hidden_size),
        )

        self.toxicity_head = nn.Linear(hidden_size, 1)
        self.concentration_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 4),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 4, 1),
        )

        nn.init.normal_(self.toxicity_head.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.toxicity_head.bias)
        nn.init.normal_(self.concentration_head[-1].weight, mean=0.0, std=0.02)
        nn.init.constant_(
            self.concentration_head[-1].bias,
            math.log(math.exp(12.0) - 1.0),
        )

    @staticmethod
    def _masked_mean_pool(
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        mask = attention_mask.unsqueeze(-1).to(dtype=hidden_states.dtype)
        summed = (hidden_states * mask).sum(dim=1)
        count = mask.sum(dim=1).clamp_min(1.0)
        return summed / count

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        style_features: Optional[torch.Tensor] = None,
    ) -> Dict[str, torch.Tensor]:
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        text_embedding = self._masked_mean_pool(
            encoder_outputs.last_hidden_state,
            attention_mask,
        )
        text_embedding = self.text_norm(text_embedding)

        if style_features is None:
            style_features = torch.zeros(
                (input_ids.shape[0], NUM_STYLE_FEATURES),
                dtype=text_embedding.dtype,
                device=text_embedding.device,
            )

        style_embedding = self.style_norm(
            self.style_encoder(style_features.to(dtype=text_embedding.dtype))
        )

        gate = self.fusion_gate(torch.cat([text_embedding, style_embedding], dim=-1))
        gated_style = gate * style_embedding

        fused_embedding = self.fusion_projection(
            torch.cat(
                [
                    text_embedding,
                    gated_style,
                    text_embedding * gated_style,
                ],
                dim=-1,
            )
        )

        toxicity_logit = self.toxicity_head(fused_embedding).squeeze(-1)
        concentration = (
            F.softplus(self.concentration_head(fused_embedding).squeeze(-1)) + 2.0
        ).clamp(max=200.0)

        return {
            "toxicity_logit": toxicity_logit,
            "toxicity_probability": torch.sigmoid(toxicity_logit),
            "concentration": concentration,
            "embedding": fused_embedding,
        }


class BiasAwareBetaBinomialLoss(nn.Module):
    def __init__(
        self,
        num_identity_columns: int,
        identity_importance: Optional[torch.Tensor] = None,
        bce_weight: float = 0.55,
        beta_binomial_weight: float = 0.45,
        benign_identity_boost: float = 2.40,
        toxic_identity_boost: float = 0.90,
        toxic_background_boost: float = 0.35,
    ) -> None:
        super().__init__()

        if identity_importance is None:
            identity_importance = torch.ones(
                num_identity_columns,
                dtype=torch.float32,
            )

        identity_importance = torch.as_tensor(
            identity_importance,
            dtype=torch.float32,
        )

        if identity_importance.ndim != 1:
            raise ValueError("identity_importance must be one-dimensional.")

        if identity_importance.numel() != num_identity_columns:
            raise ValueError(
                "identity_importance length must equal num_identity_columns."
            )

        if torch.any(identity_importance <= 0):
            raise ValueError("identity_importance values must all be positive.")

        self.register_buffer(
            "identity_importance",
            identity_importance / identity_importance.mean().clamp_min(1e-6),
        )

        self.bce_weight = float(bce_weight)
        self.beta_binomial_weight = float(beta_binomial_weight)
        self.benign_identity_boost = float(benign_identity_boost)
        self.toxic_identity_boost = float(toxic_identity_boost)
        self.toxic_background_boost = float(toxic_background_boost)

    @staticmethod
    def _beta_binomial_nll(
        probability: torch.Tensor,
        concentration: torch.Tensor,
        target: torch.Tensor,
        annotator_count: torch.Tensor,
    ) -> torch.Tensor:
        n = annotator_count.to(dtype=probability.dtype).clamp_min(1.0)
        k = torch.round(target * n).clamp(min=0.0)
        k = torch.minimum(k, n)

        alpha = (probability * concentration).clamp_min(1e-4)
        beta = ((1.0 - probability) * concentration).clamp_min(1e-4)

        log_combination = (
            torch.lgamma(n + 1.0) - torch.lgamma(k + 1.0) - torch.lgamma(n - k + 1.0)
        )

        log_beta_ratio = (
            torch.lgamma(k + alpha)
            + torch.lgamma(n - k + beta)
            - torch.lgamma(n + alpha + beta)
            + torch.lgamma(alpha + beta)
            - torch.lgamma(alpha)
            - torch.lgamma(beta)
        )

        return -(log_combination + log_beta_ratio)

    def forward(
        self,
        model_output: Dict[str, torch.Tensor],
        target: torch.Tensor,
        toxicity_annotator_count: torch.Tensor,
        identity_targets: Optional[torch.Tensor] = None,
        identity_labeled: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        logits = model_output["toxicity_logit"]
        probability = model_output["toxicity_probability"]
        concentration = model_output["concentration"]

        target = target.to(dtype=logits.dtype).clamp(0.0, 1.0)

        base_bce = F.binary_cross_entropy_with_logits(
            logits,
            target,
            reduction="none",
        )

        beta_binomial_nll = self._beta_binomial_nll(
            probability=probability,
            concentration=concentration,
            target=target,
            annotator_count=toxicity_annotator_count,
        )

        per_example_loss = (
            self.bce_weight * base_bce + self.beta_binomial_weight * beta_binomial_nll
        )

        if identity_targets is None:
            identity_strength = torch.zeros_like(target)
            identity_is_known = torch.zeros_like(target)
        else:
            identity_targets = identity_targets.to(dtype=logits.dtype).clamp(0.0, 1.0)
            weighted_identity_targets = (
                identity_targets * self.identity_importance.unsqueeze(0)
            )
            identity_strength = weighted_identity_targets.amax(dim=1).clamp(0.0, 1.0)

            if identity_labeled is None:
                identity_is_known = torch.ones_like(target)
            else:
                identity_is_known = identity_labeled.to(dtype=logits.dtype).clamp(
                    0.0,
                    1.0,
                )

        is_toxic = (target >= 0.5).to(dtype=logits.dtype)
        benign_identity = (1.0 - is_toxic) * identity_strength
        toxic_identity = is_toxic * identity_strength
        toxic_known_background = (
            is_toxic * (1.0 - identity_strength) * identity_is_known
        )

        fairness_weight = (
            1.0
            + self.benign_identity_boost * benign_identity
            + self.toxic_identity_boost * toxic_identity
            + self.toxic_background_boost * toxic_known_background
        )

        annotation_weight = torch.sqrt(
            toxicity_annotator_count.to(dtype=logits.dtype).clamp(min=3.0, max=20.0)
            / 5.0
        ).clamp(min=0.75, max=2.0)

        sample_weight = fairness_weight * annotation_weight

        return (per_example_loss * sample_weight).sum() / sample_weight.sum().clamp_min(
            1e-6
        )


model = FairToxicityModernBERT(
    pretrained_classifier=base_model,
    num_style_features=NUM_STYLE_FEATURES,
    dropout=0.20,
)

if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable()

criterion = BiasAwareBetaBinomialLoss(
    num_identity_columns=NUM_IDENTITY_COLUMNS,
    bce_weight=0.55,
    beta_binomial_weight=0.45,
    benign_identity_boost=2.40,
    toxic_identity_boost=0.90,
    toxic_background_boost=0.35,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
encoder_decay_params = []
encoder_no_decay_params = []
head_decay_params = []
head_no_decay_params = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = any(term in parameter_name for term in no_decay_terms)
    is_encoder_parameter = parameter_name.startswith("encoder.")

    if is_encoder_parameter and is_no_decay:
        encoder_no_decay_params.append(parameter)
    elif is_encoder_parameter:
        encoder_decay_params.append(parameter)
    elif is_no_decay:
        head_no_decay_params.append(parameter)
    else:
        head_decay_params.append(parameter)

optimizer = AdamW(
    [
        {
            "params": encoder_decay_params,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": encoder_no_decay_params,
            "lr": 1.5e-5,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_params,
            "lr": 2.0e-4,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_params,
            "lr": 2.0e-4,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
    # Avoid AdamW foreach temporary tensors that caused the optimizer-step OOM.
    foreach=False,
)


def official_power_mean(values: np.ndarray, power: float = -5.0) -> float:
    values = np.asarray(values, dtype=np.float64)

    if values.size == 0 or not np.isfinite(values).all():
        raise ValueError("Bias metric aggregation received invalid AUC values.")

    if np.any(values <= 0.0):
        raise ValueError(
            "AUC values must be strictly positive for negative power mean."
        )

    return float(np.power(np.mean(np.power(values, power)), 1.0 / power))


def checked_auc(
    y_true: np.ndarray,
    prediction: np.ndarray,
    metric_name: str,
) -> float:
    y_true = np.asarray(y_true, dtype=np.int8)
    prediction = np.asarray(prediction, dtype=np.float64)

    if len(y_true) != len(prediction):
        raise ValueError(
            f"{metric_name}: labels and predictions have different lengths."
        )

    if len(y_true) == 0 or np.unique(y_true).size != 2:
        raise ValueError(
            f"{metric_name}: subset must contain both toxic and non-toxic examples."
        )

    if not np.isfinite(prediction).all():
        raise ValueError(f"{metric_name}: non-finite model predictions found.")

    return float(roc_auc_score(y_true, prediction))


def official_unintended_bias_metric(
    validation_frame: pd.DataFrame,
    prediction: np.ndarray,
) -> tuple[float, dict]:
    target = (validation_frame["target"].to_numpy(dtype=np.float32) >= 0.5).astype(
        np.int8
    )

    prediction = np.asarray(prediction, dtype=np.float64)
    overall_auc = checked_auc(target, prediction, "overall_auc")

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in METRIC_IDENTITY_COLUMNS:
        subgroup = (
            validation_frame[identity_column].fillna(0.0).to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & (target == 0)) | ((~subgroup) & (target == 1))
        bnsp_mask = (subgroup & (target == 1)) | ((~subgroup) & (target == 0))

        subgroup_auc = checked_auc(
            target[subgroup_mask],
            prediction[subgroup_mask],
            f"{identity_column}_subgroup_auc",
        )

        bpsn_auc = checked_auc(
            target[bpsn_mask],
            prediction[bpsn_mask],
            f"{identity_column}_bpsn_auc",
        )

        bnsp_auc = checked_auc(
            target[bnsp_mask],
            prediction[bnsp_mask],
            f"{identity_column}_bnsp_auc",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity[identity_column] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
        }

    subgroup_power_mean = official_power_mean(np.asarray(subgroup_aucs))
    bpsn_power_mean = official_power_mean(np.asarray(bpsn_aucs))
    bnsp_power_mean = official_power_mean(np.asarray(bnsp_aucs))

    final_score = 0.25 * (
        overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean
    )

    details = {
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
        "per_identity": per_identity,
    }

    return float(final_score), details


style_feature_columns = [f"{column}_z" for column in STYLE_FEATURE_COLUMNS]

required_train_columns = (
    [
        "model_text",
        "target",
        "toxicity_annotator_count",
        "identity_labeled",
    ]
    + style_feature_columns
    + IDENTITY_COLUMNS
)

missing_train_columns = [
    column for column in required_train_columns if column not in train_processed.columns
]

if missing_train_columns:
    raise KeyError(
        f"Required processed training columns are missing: {missing_train_columns}"
    )

missing_valid_columns = [
    column for column in required_train_columns if column not in valid_processed.columns
]

if missing_valid_columns:
    raise KeyError(
        f"Required processed validation columns are missing: {missing_valid_columns}"
    )

missing_test_columns = [
    column
    for column in ["id", "model_text"] + style_feature_columns
    if column not in test_processed.columns
]

if missing_test_columns:
    raise KeyError(
        f"Required processed test columns are missing: {missing_test_columns}"
    )


class ToxicityFrameDataset(Dataset):
    def __init__(
        self,
        frame: pd.DataFrame,
        include_targets: bool,
    ) -> None:
        self.texts = (
            frame["model_text"]
            .fillna("")
            .astype(str)
            .to_numpy(dtype=object, copy=False)
        )

        self.style_features = frame[style_feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )

        self.include_targets = include_targets

        if include_targets:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.identity_targets = (
                frame[IDENTITY_COLUMNS]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )
            self.identity_labeled = frame["identity_labeled"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.annotator_counts = frame["toxicity_annotator_count"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int):
        if self.include_targets:
            return (
                self.texts[index],
                self.style_features[index],
                self.targets[index],
                self.annotator_counts[index],
                self.identity_targets[index],
                self.identity_labeled[index],
            )

        return self.texts[index], self.style_features[index]


class ToxicityCollator:
    def __init__(
        self,
        tokenizer_object,
        max_length: int,
        include_targets: bool,
    ) -> None:
        self.tokenizer_object = tokenizer_object
        self.max_length = max_length
        self.include_targets = include_targets

    def __call__(self, batch):
        texts = [sample[0] for sample in batch]

        encoded = self.tokenizer_object(
            texts,
            truncation=True,
            max_length=self.max_length,
            padding=True,
            return_tensors="pt",
        )

        output = {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "style_features": torch.as_tensor(
                np.stack([sample[1] for sample in batch]),
                dtype=torch.float32,
            ),
        }

        if self.include_targets:
            output["target"] = torch.as_tensor(
                [sample[2] for sample in batch],
                dtype=torch.float32,
            )

            output["toxicity_annotator_count"] = torch.as_tensor(
                [sample[3] for sample in batch],
                dtype=torch.float32,
            )

            output["identity_targets"] = torch.as_tensor(
                np.stack([sample[4] for sample in batch]),
                dtype=torch.float32,
            )

            output["identity_labeled"] = torch.as_tensor(
                [sample[5] for sample in batch],
                dtype=torch.float32,
            )

        return output


train_fit_frame = train_processed.loc[:, required_train_columns].copy()
valid_fit_frame = valid_processed.loc[:, required_train_columns].copy()

if len(counterfactual_augmentation) > 0:
    augmentation_frame = counterfactual_augmentation.copy()

    for column in style_feature_columns:
        if column not in augmentation_frame.columns:
            augmentation_frame[column] = np.float32(0.0)

    for column in IDENTITY_COLUMNS:
        augmentation_frame[column] = np.float32(0.0)

    augmentation_frame["identity_labeled"] = np.float32(0.0)
    augmentation_frame["toxicity_annotator_count"] = np.float32(5.0)

    augmentation_frame = augmentation_frame[required_train_columns]

    train_fit_frame = pd.concat(
        [train_fit_frame, augmentation_frame],
        axis=0,
        ignore_index=True,
    )

train_dataset = ToxicityFrameDataset(train_fit_frame, include_targets=True)
valid_dataset = ToxicityFrameDataset(valid_fit_frame, include_targets=True)
test_dataset = ToxicityFrameDataset(test_processed, include_targets=False)

train_generator = torch.Generator()
train_generator.manual_seed(SEED)

loader_kwargs = {
    "num_workers": NUM_WORKERS,
    "pin_memory": amp_enabled,
    "persistent_workers": NUM_WORKERS > 0,
}

if NUM_WORKERS > 0:
    loader_kwargs["prefetch_factor"] = 2

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=train_generator,
    collate_fn=ToxicityCollator(tokenizer, MAX_LENGTH, include_targets=True),
    drop_last=False,
    **loader_kwargs,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    collate_fn=ToxicityCollator(tokenizer, MAX_LENGTH, include_targets=True),
    drop_last=False,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    collate_fn=ToxicityCollator(tokenizer, MAX_LENGTH, include_targets=False),
    drop_last=False,
    **loader_kwargs,
)

model = model.to(device)
criterion = criterion.to(device)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_updates = max(1, updates_per_epoch * NUM_EPOCHS)
warmup_updates = int(total_updates * WARMUP_RATIO)


def cosine_warmup_schedule(step: int) -> float:
    if warmup_updates > 0 and step < warmup_updates:
        return float(step + 1) / float(max(1, warmup_updates))

    progress = float(step - warmup_updates) / float(
        max(1, total_updates - warmup_updates)
    )
    progress = min(1.0, max(0.0, progress))

    return max(0.05, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=cosine_warmup_schedule)
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


@torch.no_grad()
def predict_from_loader(data_loader: DataLoader) -> np.ndarray:
    model.eval()
    prediction_parts = []

    for batch in data_loader:
        input_ids = batch["input_ids"].to(device, non_blocking=True)
        attention_mask = batch["attention_mask"].to(device, non_blocking=True)
        style_features = batch["style_features"].to(device, non_blocking=True)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            model_output = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                style_features=style_features,
            )
            probabilities = model_output["toxicity_probability"]

        prediction_parts.append(probabilities.detach().float().cpu().numpy())

    predictions = np.concatenate(prediction_parts, axis=0).astype(np.float64)

    if not np.isfinite(predictions).all():
        raise RuntimeError("Model inference produced non-finite predictions.")

    return predictions


checkpoint_path = CHECKPOINT_DIR / "best_fair_modernbert.pt"
best_score = -np.inf
best_epoch = -1

for epoch in range(NUM_EPOCHS):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    total_loss = 0.0
    total_examples = 0

    for batch_index, batch in enumerate(train_loader):
        input_ids = batch["input_ids"].to(device, non_blocking=True)
        attention_mask = batch["attention_mask"].to(device, non_blocking=True)
        style_features = batch["style_features"].to(device, non_blocking=True)
        target = batch["target"].to(device, non_blocking=True)

        annotator_count = batch["toxicity_annotator_count"].to(
            device,
            non_blocking=True,
        )

        identity_targets = batch["identity_targets"].to(
            device,
            non_blocking=True,
        )

        identity_labeled = batch["identity_labeled"].to(
            device,
            non_blocking=True,
        )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            model_output = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                style_features=style_features,
            )

            batch_loss = criterion(
                model_output=model_output,
                target=target,
                toxicity_annotator_count=annotator_count,
                identity_targets=identity_targets,
                identity_labeled=identity_labeled,
            )

            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()

        should_update = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if should_update:
            grad_scaler.unscale_(optimizer)
            clip_grad_norm_(model.parameters(), MAX_GRAD_NORM)
            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_size = int(target.shape[0])
        total_loss += float(batch_loss.detach().cpu()) * batch_size
        total_examples += batch_size

    validation_predictions = predict_from_loader(valid_loader)

    validation_score, validation_details = official_unintended_bias_metric(
        valid_fit_frame,
        validation_predictions,
    )

    epoch_loss = total_loss / max(1, total_examples)

    if validation_score > best_score:
        best_score = validation_score
        best_epoch = epoch

        torch.save(
            {
                "epoch": epoch,
                "validation_score": validation_score,
                "validation_details": validation_details,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
            },
            checkpoint_path,
        )

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"loss={epoch_loss:.6f} "
        f"overall_auc={validation_details['overall_auc']:.6f} "
        f"bias_score={validation_score:.6f}"
    )

if not checkpoint_path.exists():
    raise RuntimeError("No model checkpoint was saved during training.")

try:
    best_checkpoint = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
except TypeError:
    best_checkpoint = torch.load(checkpoint_path, map_location="cpu")

model.load_state_dict(best_checkpoint["model_state_dict"], strict=True)
model = model.to(device)

best_validation_predictions = predict_from_loader(valid_loader)

score, final_validation_details = official_unintended_bias_metric(
    valid_fit_frame,
    best_validation_predictions,
)

test_predictions = predict_from_loader(test_loader)

if len(test_predictions) != len(test_processed):
    raise RuntimeError(
        f"Test prediction count mismatch: {len(test_predictions)} vs {len(test_processed)}"
    )

submission = pd.DataFrame(
    {
        "id": test_processed["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if submission["id"].duplicated().any():
    raise ValueError("Submission contains duplicate IDs.")

if not np.isfinite(submission["prediction"].to_numpy()).all():
    raise ValueError("Submission contains non-finite predictions.")

submission.to_csv(SUBMISSION_DIR / "submission_bb86bba208314a8d947966d5fd33b043.csv", index=False)

print(f"Final Validation Score: {score}")
