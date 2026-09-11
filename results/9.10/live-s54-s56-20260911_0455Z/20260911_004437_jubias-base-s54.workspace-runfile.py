import os
os.sched_setaffinity(0, {70, 6, 8, 9, 7, 71, 72, 73})
import os
import re
import json
import html
import random
import unicodedata
import warnings

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession

warnings.filterwarnings("ignore")

RANDOM_SEED = 2029
INPUT_DIR = "./input"
WORK_DIR = "./working"
os.makedirs(WORK_DIR, exist_ok=True)

session = CandidateSession.from_env()

raw_train_df = pd.read_csv(os.path.join(INPUT_DIR, "train.csv"), low_memory=False)
raw_test_df = pd.read_csv(os.path.join(INPUT_DIR, "test.csv"), low_memory=False)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df

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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

IDENTITY_COLUMNS = [c for c in IDENTITY_COLUMNS if c in train_df.columns]
OFFICIAL_IDENTITY_COLUMNS = [
    c for c in OFFICIAL_IDENTITY_COLUMNS if c in train_df.columns
]
AUXILIARY_TARGET_COLUMNS = [
    c for c in AUXILIARY_TARGET_COLUMNS if c in train_df.columns
]

URL_PATTERN = re.compile(
    r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]{}]+|"
    r"\b[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}\b"
)
EMAIL_PATTERN = re.compile(r"(?i)\b[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}\b")
USER_PATTERN = re.compile(r"(?<!\w)@[a-zA-Z0-9_]{2,}")
WHITESPACE_PATTERN = re.compile(r"\s+")


def normalize_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", " ").replace("\ufeff", " ").replace("\u00a0", " ")
    text = EMAIL_PATTERN.sub(" [email] ", text)
    text = URL_PATTERN.sub(" [url] ", text)
    text = USER_PATTERN.sub(" [user] ", text)
    return WHITESPACE_PATTERN.sub(" ", text).strip()


def create_transformer_text(clean_text):
    text_length = clean_text.str.len()
    truncated = (
        clean_text.str.slice(0, 6000)
        + " [truncated_middle] "
        + clean_text.str.slice(-2000)
    )
    return pd.Series(
        np.where(
            text_length.gt(8000),
            truncated.to_numpy(dtype=object),
            clean_text.to_numpy(dtype=object),
        ),
        index=clean_text.index,
        dtype=object,
    )


def compute_style_features(clean_text):
    char_count = clean_text.str.len().clip(lower=0, upper=20000).astype(np.float32)
    word_count = (
        clean_text.str.count(r"\S+").clip(lower=0, upper=5000).astype(np.float32)
    )
    alphabetic_count = clean_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").astype(np.float32)
    digit_count = clean_text.str.count(r"\d").astype(np.float32)

    features = pd.DataFrame(index=clean_text.index)
    features["log_char_count"] = np.log1p(char_count)
    features["log_word_count"] = np.log1p(word_count)
    features["uppercase_fraction"] = (
        uppercase_count / alphabetic_count.clip(lower=1.0)
    ).clip(0.0, 1.0)
    features["digit_fraction"] = (digit_count / char_count.clip(lower=1.0)).clip(
        0.0, 1.0
    )
    features["exclamation_density"] = (
        clean_text.str.count("!").astype(np.float32) / char_count.clip(lower=1.0)
    ).clip(0.0, 1.0)
    features["question_density"] = (
        clean_text.str.count(r"\?").astype(np.float32) / char_count.clip(lower=1.0)
    ).clip(0.0, 1.0)
    features["newline_count"] = (
        clean_text.str.count(r"\n").clip(0, 100).astype(np.float32)
    )
    features["repeated_punctuation_count"] = (
        clean_text.str.count(r"([!?.])\1{2,}").clip(0, 100).astype(np.float32)
    )
    features["all_caps_word_count"] = (
        clean_text.str.count(r"\b[A-Z]{2,}\b").clip(0, 500).astype(np.float32)
    )
    features["url_token_count"] = (
        clean_text.str.count(r"\[url\]").clip(0, 100).astype(np.float32)
    )
    features["user_token_count"] = (
        clean_text.str.count(r"\[user\]").clip(0, 100).astype(np.float32)
    )
    features["non_ascii_fraction"] = (
        clean_text.str.count(r"[^\x00-\x7F]").astype(np.float32)
        / char_count.clip(lower=1.0)
    ).clip(0.0, 1.0)
    return features.astype(np.float32)


COUNTERFACTUAL_REPLACEMENTS = {
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
    "christians": "muslims",
    "muslim": "christian",
    "muslims": "christians",
    "jewish": "buddhist",
    "jews": "buddhists",
    "buddhist": "jewish",
    "buddhists": "jews",
    "hindu": "atheist",
    "hindus": "atheists",
    "atheist": "hindu",
    "atheists": "hindus",
    "black": "white",
    "white": "black",
    "asian": "latino",
    "latino": "asian",
    "gay": "straight",
    "straight": "gay",
    "lesbian": "heterosexual",
    "heterosexual": "lesbian",
    "transgender": "cisgender",
    "cisgender": "transgender",
}

COUNTERFACTUAL_PATTERN = re.compile(
    r"(?i)(?<![\w-])("
    + "|".join(
        sorted(
            map(re.escape, COUNTERFACTUAL_REPLACEMENTS.keys()),
            key=len,
            reverse=True,
        )
    )
    + r")(?![\w-])"
)


def preserve_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement.capitalize()
    return replacement


def swap_identity_terms(text):
    def replace_match(match):
        source = match.group(0)
        return preserve_case(
            source,
            COUNTERFACTUAL_REPLACEMENTS[source.lower()],
        )

    return COUNTERFACTUAL_PATTERN.sub(replace_match, text)


def build_identity_metadata(frame):
    if not IDENTITY_COLUMNS:
        return (
            np.zeros(len(frame), dtype=bool),
            np.zeros(len(frame), dtype=bool),
            np.zeros(len(frame), dtype=np.float32),
        )

    identity_frame = frame.reindex(columns=IDENTITY_COLUMNS)
    identity_known = identity_frame.notna().any(axis=1).to_numpy(dtype=bool)
    identity_strength = (
        identity_frame.fillna(0.0).max(axis=1).to_numpy(dtype=np.float32)
    )
    identity_present = identity_strength >= 0.5
    return identity_known, identity_present, identity_strength


train_clean_text = train_df["comment_text"].map(normalize_comment)
valid_clean_text = valid_df["comment_text"].map(normalize_comment)
test_clean_text = test_df["comment_text"].map(normalize_comment)

train_transformer_text = create_transformer_text(train_clean_text)
valid_transformer_text = create_transformer_text(valid_clean_text)
test_transformer_text = create_transformer_text(test_clean_text)

train_style_raw = compute_style_features(train_clean_text)
valid_style_raw = compute_style_features(valid_clean_text)
test_style_raw = compute_style_features(test_clean_text)

style_feature_columns = train_style_raw.columns.tolist()
style_scaler = StandardScaler()

train_style_scaled = pd.DataFrame(
    style_scaler.fit_transform(train_style_raw),
    columns=style_feature_columns,
    index=train_df.index,
    dtype=np.float32,
)
valid_style_scaled = pd.DataFrame(
    style_scaler.transform(valid_style_raw),
    columns=style_feature_columns,
    index=valid_df.index,
    dtype=np.float32,
)
test_style_scaled = pd.DataFrame(
    style_scaler.transform(test_style_raw),
    columns=style_feature_columns,
    index=test_df.index,
    dtype=np.float32,
)

_, train_identity_present, _ = build_identity_metadata(train_df)

stable_hash = pd.util.hash_pandas_object(
    train_df["id"].astype(str),
    index=False,
).to_numpy(dtype=np.uint64)

counterfactual_candidate = train_identity_present & ((stable_hash % np.uint64(3)) == 0)
counterfactual_text = pd.Series(pd.NA, index=train_df.index, dtype=object)

for row_index in train_df.index[counterfactual_candidate]:
    original_text = train_transformer_text.at[row_index]
    swapped_text = swap_identity_terms(original_text)
    if swapped_text != original_text:
        counterfactual_text.at[row_index] = swapped_text

train_bias_weight = np.ones(len(train_df), dtype=np.float32)
soft_target = train_df["target"].fillna(0.0).to_numpy(dtype=np.float32)
train_bias_weight += 1.25 * (train_identity_present & (soft_target < 0.5)).astype(
    np.float32
)
train_bias_weight += 0.35 * (train_identity_present & (soft_target >= 0.5)).astype(
    np.float32
)


def assemble_prepared_frame(
    source_frame,
    transformer_text,
    scaled_style_features,
    include_labels=False,
    include_counterfactual=False,
    include_training_weight=False,
):
    prepared = pd.DataFrame(
        {
            "id": source_frame["id"].to_numpy(),
            "model_text": transformer_text.to_numpy(dtype=object),
        },
        index=source_frame.index,
    )

    for feature_name in style_feature_columns:
        prepared[feature_name] = scaled_style_features[feature_name].to_numpy(
            dtype=np.float32
        )

    if include_labels:
        label_columns = ["target"] + AUXILIARY_TARGET_COLUMNS + IDENTITY_COLUMNS
        for column in [c for c in label_columns if c in source_frame.columns]:
            prepared[column] = source_frame[column].to_numpy()

        if IDENTITY_COLUMNS:
            prepared["identity_labels_available"] = (
                source_frame[IDENTITY_COLUMNS]
                .notna()
                .any(axis=1)
                .to_numpy(dtype=np.int8)
            )
            prepared["identity_mention_strength"] = (
                source_frame[IDENTITY_COLUMNS]
                .fillna(0.0)
                .max(axis=1)
                .to_numpy(dtype=np.float32)
            )

    if include_counterfactual:
        prepared["counterfactual_text"] = counterfactual_text.to_numpy(dtype=object)

    if include_training_weight:
        prepared["bias_training_weight"] = train_bias_weight

    return prepared.reset_index(drop=True)


prepared_train_df = assemble_prepared_frame(
    train_df,
    train_transformer_text,
    train_style_scaled,
    include_labels=True,
    include_counterfactual=True,
    include_training_weight=True,
)
prepared_valid_df = assemble_prepared_frame(
    valid_df,
    valid_transformer_text,
    valid_style_scaled,
    include_labels=True,
)
prepared_test_df = assemble_prepared_frame(
    test_df,
    test_transformer_text,
    test_style_scaled,
)

prepared_train_df.to_pickle(os.path.join(WORK_DIR, "prepared_train.pkl"))
prepared_valid_df.to_pickle(os.path.join(WORK_DIR, "prepared_valid.pkl"))
prepared_test_df.to_pickle(os.path.join(WORK_DIR, "prepared_test.pkl"))

feature_state = {
    "random_seed": RANDOM_SEED,
    "text_normalization": "NFKC + HTML unescape + URL/email/user placeholders + whitespace normalization",
    "transformer_truncation": {
        "max_characters": 8000,
        "head_characters": 6000,
        "tail_characters": 2000,
    },
    "style_feature_columns": style_feature_columns,
    "style_scaler": style_scaler,
    "identity_columns": IDENTITY_COLUMNS,
    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    "auxiliary_target_columns": AUXILIARY_TARGET_COLUMNS,
    "counterfactual_replacements": COUNTERFACTUAL_REPLACEMENTS,
}
joblib.dump(feature_state, os.path.join(WORK_DIR, "feature_state.joblib"))

with open(
    os.path.join(WORK_DIR, "prepared_data_manifest.json"), "w", encoding="utf-8"
) as f:
    json.dump(
        {
            "train_rows": int(len(prepared_train_df)),
            "validation_rows": int(len(prepared_valid_df)),
            "test_rows": int(len(prepared_test_df)),
            "style_feature_columns": style_feature_columns,
            "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
            "counterfactual_pairs": int(
                prepared_train_df["counterfactual_text"].notna().sum()
            ),
            "split_first": True,
            "scaler_fit_partition": "train_only",
        },
        f,
        indent=2,
    )

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-base")
base_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-base",
    num_labels=2,
)

STYLE_FEATURE_DIM = len(style_feature_columns)
NUM_AUXILIARY_TARGETS = len(AUXILIARY_TARGET_COLUMNS)
NUM_IDENTITY_TARGETS = len(IDENTITY_COLUMNS)


class GradientReversal(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = float(coefficient)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradients):
        return -ctx.coefficient * gradients, None


class FairDebertaRanker(nn.Module):
    def __init__(
        self,
        pretrained_classifier,
        style_feature_dim,
        num_auxiliary_targets,
        num_identity_targets,
        dropout=0.15,
        adversarial_strength=0.20,
    ):
        super().__init__()
        self.backbone = pretrained_classifier.deberta
        hidden_size = pretrained_classifier.config.hidden_size
        self.adversarial_strength = float(adversarial_strength)

        self.style_projection = nn.Sequential(
            nn.LayerNorm(style_feature_dim),
            nn.Linear(style_feature_dim, 64),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden_size + 64),
            nn.Linear(hidden_size + 64, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.toxicity_head = nn.Linear(hidden_size, 1)
        self.auxiliary_head = nn.Linear(hidden_size, num_auxiliary_targets)
        self.identity_adversary = nn.Sequential(
            nn.LayerNorm(hidden_size),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, num_identity_targets),
        )

        nn.init.normal_(self.toxicity_head.weight, std=0.02)
        nn.init.zeros_(self.toxicity_head.bias)
        nn.init.normal_(self.auxiliary_head.weight, std=0.02)
        nn.init.zeros_(self.auxiliary_head.bias)

    def forward(self, input_ids, attention_mask, style_features=None):
        backbone_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        cls_embedding = backbone_outputs.last_hidden_state[:, 0]

        if style_features is None:
            style_features = torch.zeros(
                cls_embedding.size(0),
                STYLE_FEATURE_DIM,
                device=cls_embedding.device,
                dtype=cls_embedding.dtype,
            )
        else:
            style_features = style_features.to(
                device=cls_embedding.device,
                dtype=cls_embedding.dtype,
            )

        representation = self.fusion(
            torch.cat([cls_embedding, self.style_projection(style_features)], dim=-1)
        )
        reversed_representation = GradientReversal.apply(
            representation,
            self.adversarial_strength,
        )

        return {
            "toxicity_logit": self.toxicity_head(representation).squeeze(-1),
            "auxiliary_logits": self.auxiliary_head(representation),
            "identity_adversarial_logits": self.identity_adversary(
                reversed_representation
            ),
        }


class BiasAwareRankingLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight=0.25,
        adversarial_weight=0.06,
        ranking_weight=0.35,
        temperature=0.75,
        max_pairs_per_group=64,
    ):
        super().__init__()
        self.auxiliary_weight = float(auxiliary_weight)
        self.adversarial_weight = float(adversarial_weight)
        self.ranking_weight = float(ranking_weight)
        self.temperature = float(temperature)
        self.max_pairs_per_group = int(max_pairs_per_group)

    def _sample_scores(self, scores):
        if scores.numel() <= self.max_pairs_per_group:
            return scores
        indices = torch.randperm(scores.numel(), device=scores.device)[
            : self.max_pairs_per_group
        ]
        return scores[indices]

    def _pairwise_auc_surrogate(self, positive_scores, negative_scores):
        if positive_scores.numel() == 0 or negative_scores.numel() == 0:
            return None
        positive_scores = self._sample_scores(positive_scores)
        negative_scores = self._sample_scores(negative_scores)
        margins = (
            positive_scores[:, None] - negative_scores[None, :]
        ) / self.temperature
        return F.softplus(-margins).mean()

    def _official_bias_ranking_loss(
        self,
        toxicity_logits,
        toxicity_targets,
        official_identity_targets,
    ):
        if official_identity_targets is None:
            return toxicity_logits.sum() * 0.0

        terms = []
        binary_target = toxicity_targets >= 0.5

        for identity_index in range(official_identity_targets.size(1)):
            values = official_identity_targets[:, identity_index]
            known = torch.isfinite(values)
            subgroup = known & (values >= 0.5)
            background = known & (values < 0.5)

            subgroup_term = self._pairwise_auc_surrogate(
                toxicity_logits[subgroup & binary_target],
                toxicity_logits[subgroup & ~binary_target],
            )
            if subgroup_term is not None:
                terms.append(subgroup_term)

            bpsn_term = self._pairwise_auc_surrogate(
                toxicity_logits[background & binary_target],
                toxicity_logits[subgroup & ~binary_target],
            )
            if bpsn_term is not None:
                terms.append(bpsn_term)

            bnsp_term = self._pairwise_auc_surrogate(
                toxicity_logits[subgroup & binary_target],
                toxicity_logits[background & ~binary_target],
            )
            if bnsp_term is not None:
                terms.append(bnsp_term)

        return torch.stack(terms).mean() if terms else toxicity_logits.sum() * 0.0

    def forward(
        self,
        outputs,
        toxicity_targets,
        sample_weights=None,
        auxiliary_targets=None,
        identity_targets=None,
        official_identity_targets=None,
    ):
        toxicity_targets = toxicity_targets.float().clamp(0.0, 1.0)
        primary_per_example = F.binary_cross_entropy_with_logits(
            outputs["toxicity_logit"],
            toxicity_targets,
            reduction="none",
        )

        if sample_weights is None:
            primary_loss = primary_per_example.mean()
        else:
            weights = sample_weights.float().clamp_min(0.0)
            primary_loss = (
                primary_per_example * weights
            ).sum() / weights.sum().clamp_min(1.0)

        auxiliary_loss = outputs["toxicity_logit"].sum() * 0.0
        if auxiliary_targets is not None:
            valid_auxiliary = torch.isfinite(auxiliary_targets.float())
            if bool(valid_auxiliary.any().item()):
                safe_auxiliary = torch.nan_to_num(
                    auxiliary_targets.float(), nan=0.0
                ).clamp(0.0, 1.0)
                raw_auxiliary = F.binary_cross_entropy_with_logits(
                    outputs["auxiliary_logits"],
                    safe_auxiliary,
                    reduction="none",
                )
                auxiliary_loss = raw_auxiliary[valid_auxiliary].mean()

        adversarial_loss = outputs["toxicity_logit"].sum() * 0.0
        if identity_targets is not None:
            valid_identity = torch.isfinite(identity_targets.float())
            valid_identity = valid_identity & (toxicity_targets < 0.5).unsqueeze(1)
            if bool(valid_identity.any().item()):
                safe_identity = torch.nan_to_num(
                    identity_targets.float(), nan=0.0
                ).clamp(0.0, 1.0)
                raw_identity = F.binary_cross_entropy_with_logits(
                    outputs["identity_adversarial_logits"],
                    safe_identity,
                    reduction="none",
                )
                adversarial_loss = raw_identity[valid_identity].mean()

        ranking_loss = self._official_bias_ranking_loss(
            outputs["toxicity_logit"],
            toxicity_targets,
            official_identity_targets,
        )

        total = (
            primary_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.adversarial_weight * adversarial_loss
            + self.ranking_weight * ranking_loss
        )
        return total, {
            "primary_loss": primary_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "adversarial_loss": adversarial_loss.detach(),
            "ranking_loss": ranking_loss.detach(),
        }


model = FairDebertaRanker(
    base_model,
    style_feature_dim=STYLE_FEATURE_DIM,
    num_auxiliary_targets=NUM_AUXILIARY_TARGETS,
    num_identity_targets=NUM_IDENTITY_TARGETS,
)
del base_model

num_backbone_layers = int(model.backbone.config.num_hidden_layers)
optimizer_groups = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    no_weight_decay = (
        parameter_name.endswith("bias")
        or "LayerNorm.weight" in parameter_name
        or "layer_norm.weight" in parameter_name
    )

    if parameter_name.startswith("backbone.encoder.layer."):
        layer_number = int(
            parameter_name.split("backbone.encoder.layer.")[1].split(".")[0]
        )
        learning_rate = 1.2e-5 * (0.92 ** (num_backbone_layers - 1 - layer_number))
    elif parameter_name.startswith("backbone."):
        learning_rate = 1.2e-5 * (0.92**num_backbone_layers)
    else:
        learning_rate = 8.0e-5

    optimizer_groups.append(
        {
            "params": [parameter],
            "lr": learning_rate,
            "weight_decay": 0.0 if no_weight_decay else 0.01,
        }
    )

criterion = BiasAwareRankingLoss()
optimizer = AdamW(optimizer_groups, betas=(0.9, 0.999), eps=1e-8)

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 12
INFERENCE_BATCH_SIZE = 16
GRADIENT_ACCUMULATION_STEPS = 2
MAX_EPOCHS = 3
WARMUP_UPDATES = 300
PLANNED_UPDATES = 20000
COUNTERFACTUAL_CONSISTENCY_WEIGHT = 0.08
NUM_WORKERS = 2

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"
pin_memory = device.type == "cuda"
amp_scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
model.to(device)

identity_columns_for_training = list(IDENTITY_COLUMNS)
official_identity_positions = [
    identity_columns_for_training.index(column)
    for column in OFFICIAL_IDENTITY_COLUMNS
    if column in identity_columns_for_training
]

train_texts = prepared_train_df["model_text"].fillna("").astype(str).tolist()
valid_texts = prepared_valid_df["model_text"].fillna("").astype(str).tolist()
test_texts = prepared_test_df["model_text"].fillna("").astype(str).tolist()

train_style_matrix = prepared_train_df[style_feature_columns].to_numpy(
    dtype=np.float32, copy=True
)
valid_style_matrix = prepared_valid_df[style_feature_columns].to_numpy(
    dtype=np.float32, copy=True
)
test_style_matrix = prepared_test_df[style_feature_columns].to_numpy(
    dtype=np.float32, copy=True
)

train_targets = (
    prepared_train_df["target"].fillna(0.0).clip(0.0, 1.0).to_numpy(dtype=np.float32)
)
train_sample_weights = (
    prepared_train_df["bias_training_weight"]
    .fillna(1.0)
    .clip(lower=0.0)
    .to_numpy(dtype=np.float32)
)
train_auxiliary_targets = prepared_train_df.reindex(
    columns=AUXILIARY_TARGET_COLUMNS
).to_numpy(dtype=np.float32, copy=True)
train_identity_targets = prepared_train_df.reindex(
    columns=identity_columns_for_training
).to_numpy(dtype=np.float32, copy=True)

train_counterfactual_texts = (
    prepared_train_df["counterfactual_text"].fillna("").astype(str).tolist()
)
train_has_counterfactual = np.asarray(
    [
        bool(counterfactual.strip()) and counterfactual != original
        for counterfactual, original in zip(train_counterfactual_texts, train_texts)
    ],
    dtype=bool,
)


class PositionalIndexDataset(Dataset):
    def __init__(self, indices):
        self.indices = np.asarray(indices, dtype=np.int64)

    def __len__(self):
        return int(self.indices.shape[0])

    def __getitem__(self, index):
        return int(self.indices[index])


def tokenize_texts(text_batch):
    encoded = tokenizer(
        list(text_batch),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        pad_to_multiple_of=8 if use_amp else None,
        return_tensors="pt",
    )
    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
    }


def train_collate_fn(batch_indices):
    batch_indices = np.asarray(batch_indices, dtype=np.int64)
    encoded = tokenize_texts([train_texts[i] for i in batch_indices])

    batch = {
        **encoded,
        "style_features": torch.from_numpy(train_style_matrix[batch_indices]),
        "targets": torch.from_numpy(train_targets[batch_indices]),
        "sample_weights": torch.from_numpy(train_sample_weights[batch_indices]),
        "auxiliary_targets": torch.from_numpy(train_auxiliary_targets[batch_indices]),
        "identity_targets": torch.from_numpy(train_identity_targets[batch_indices]),
    }

    mask = train_has_counterfactual[batch_indices]
    if mask.any():
        positions = np.flatnonzero(mask).astype(np.int64)
        counterfactual_encoded = tokenize_texts(
            [train_counterfactual_texts[batch_indices[i]] for i in positions]
        )
        batch["counterfactual_positions"] = torch.from_numpy(positions)
        batch["counterfactual_input_ids"] = counterfactual_encoded["input_ids"]
        batch["counterfactual_attention_mask"] = counterfactual_encoded[
            "attention_mask"
        ]
        batch["counterfactual_style_features"] = torch.from_numpy(
            train_style_matrix[batch_indices[positions]]
        )
    else:
        batch["counterfactual_positions"] = None
        batch["counterfactual_input_ids"] = None
        batch["counterfactual_attention_mask"] = None
        batch["counterfactual_style_features"] = None

    return batch


def make_inference_collate(texts, style_matrix):
    def inference_collate_fn(batch_indices):
        batch_indices = np.asarray(batch_indices, dtype=np.int64)
        encoded = tokenize_texts([texts[i] for i in batch_indices])
        encoded["style_features"] = torch.from_numpy(style_matrix[batch_indices])
        return encoded

    return inference_collate_fn


def move_to_device(tensor):
    return tensor.to(device, non_blocking=pin_memory)


@torch.no_grad()
def infer_probabilities(texts, style_matrix, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    loader = DataLoader(
        PositionalIndexDataset(positional_indices),
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=pin_memory,
        persistent_workers=False,
        collate_fn=make_inference_collate(texts, style_matrix),
    )

    was_training = model.training
    model.eval()
    chunks = []

    for batch in loader:
        with torch.cuda.amp.autocast(enabled=use_amp):
            outputs = model(
                input_ids=move_to_device(batch["input_ids"]),
                attention_mask=move_to_device(batch["attention_mask"]),
                style_features=move_to_device(batch["style_features"]),
            )
            probabilities = torch.sigmoid(outputs["toxicity_logit"])

        chunks.append(probabilities.detach().float().cpu().numpy().astype(np.float64))

    if was_training:
        model.train()

    return np.concatenate(chunks, axis=0)


def predict_validation(positional_indices):
    return infer_probabilities(
        valid_texts,
        valid_style_matrix,
        positional_indices,
    )


def predict_test(positional_indices):
    return infer_probabilities(
        test_texts,
        test_style_matrix,
        positional_indices,
    )


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_length": MAX_LENGTH,
            "style_feature_columns": style_feature_columns,
            "identity_columns": identity_columns_for_training,
            "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
            "counterfactual_consistency_weight": COUNTERFACTUAL_CONSISTENCY_WEIGHT,
        },
        os.path.join(directory, "model_state.pt"),
    )

    with open(
        os.path.join(directory, "model_configuration.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(
            {
                "backbone_config": model.backbone.config.to_dict(),
                "max_length": MAX_LENGTH,
                "style_feature_columns": style_feature_columns,
                "identity_columns": identity_columns_for_training,
                "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
                "inference_postprocessing": "sigmoid(toxicity_logit)",
            },
            f,
            indent=2,
        )

    tokenizer.save_pretrained(os.path.join(directory, "tokenizer"))
    joblib.dump(
        feature_state, os.path.join(directory, "feature_transform_state.joblib")
    )


def load_checkpoint(directory):
    payload = torch.load(
        os.path.join(directory, "model_state.pt"),
        map_location=device,
    )
    model.load_state_dict(payload["model_state_dict"], strict=True)
    model.to(device)


def learning_rate_multiplier(update_number):
    if update_number < WARMUP_UPDATES:
        return max(1.0e-3, float(update_number + 1) / float(WARMUP_UPDATES))

    progress = min(
        1.0,
        float(update_number - WARMUP_UPDATES)
        / float(max(1, PLANNED_UPDATES - WARMUP_UPDATES)),
    )
    return max(0.10, 0.5 * (1.0 + np.cos(np.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)

session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)
session.start_training(train_df["id"].astype(str).tolist())

train_generator = torch.Generator()
train_generator.manual_seed(RANDOM_SEED)

train_loader = DataLoader(
    PositionalIndexDataset(np.arange(len(train_texts), dtype=np.int64)),
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=train_generator,
    num_workers=NUM_WORKERS,
    pin_memory=pin_memory,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=train_collate_fn,
)

optimizer.zero_grad(set_to_none=True)
training_stopped = False

for epoch in range(MAX_EPOCHS):
    model.train()
    epoch_loss = 0.0
    epoch_primary_loss = 0.0
    epoch_ranking_loss = 0.0
    epoch_updates = 0
    pending_microbatches = 0

    for batch_number, batch in enumerate(train_loader):
        targets = move_to_device(batch["targets"])
        identity_targets = move_to_device(batch["identity_targets"])

        official_identity_targets = (
            identity_targets[:, official_identity_positions]
            if official_identity_positions
            else None
        )

        with torch.cuda.amp.autocast(enabled=use_amp):
            outputs = model(
                input_ids=move_to_device(batch["input_ids"]),
                attention_mask=move_to_device(batch["attention_mask"]),
                style_features=move_to_device(batch["style_features"]),
            )

            supervised_loss, loss_components = criterion(
                outputs=outputs,
                toxicity_targets=targets,
                sample_weights=move_to_device(batch["sample_weights"]),
                auxiliary_targets=move_to_device(batch["auxiliary_targets"]),
                identity_targets=identity_targets,
                official_identity_targets=official_identity_targets,
            )

            consistency_loss = supervised_loss.new_zeros(())
            positions = batch["counterfactual_positions"]

            if positions is not None:
                positions = move_to_device(positions)
                benign_mask = targets[positions] < 0.5

                if bool(benign_mask.any().item()):
                    counterfactual_outputs = model(
                        input_ids=move_to_device(batch["counterfactual_input_ids"]),
                        attention_mask=move_to_device(
                            batch["counterfactual_attention_mask"]
                        ),
                        style_features=move_to_device(
                            batch["counterfactual_style_features"]
                        ),
                    )
                    original_probabilities = torch.sigmoid(
                        outputs["toxicity_logit"][positions][benign_mask]
                    )
                    counterfactual_probabilities = torch.sigmoid(
                        counterfactual_outputs["toxicity_logit"][benign_mask]
                    )
                    consistency_loss = F.mse_loss(
                        original_probabilities,
                        counterfactual_probabilities,
                    )

            total_loss = (
                supervised_loss + COUNTERFACTUAL_CONSISTENCY_WEIGHT * consistency_loss
            )

        pending_microbatches += 1
        amp_scaler.scale(total_loss / GRADIENT_ACCUMULATION_STEPS).backward()

        is_boundary = (
            pending_microbatches >= GRADIENT_ACCUMULATION_STEPS
            or batch_number + 1 == len(train_loader)
        )
        if not is_boundary:
            continue

        if pending_microbatches != GRADIENT_ACCUMULATION_STEPS:
            correction = float(GRADIENT_ACCUMULATION_STEPS) / float(
                pending_microbatches
            )
            for parameter in model.parameters():
                if parameter.grad is not None:
                    parameter.grad.mul_(correction)

        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        amp_scaler.step(optimizer)
        amp_scaler.update()
        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

        epoch_updates += 1
        epoch_loss += float(total_loss.detach().float().cpu())
        epoch_primary_loss += float(
            loss_components["primary_loss"].detach().float().cpu()
        )
        epoch_ranking_loss += float(
            loss_components["ranking_loss"].detach().float().cpu()
        )
        pending_microbatches = 0

        if session.step():
            training_stopped = True
            break

    if epoch_updates > 0:
        print(
            f"Epoch {epoch + 1}: updates={epoch_updates} "
            f"loss={epoch_loss / epoch_updates:.5f} "
            f"primary={epoch_primary_loss / epoch_updates:.5f} "
            f"ranking={epoch_ranking_loss / epoch_updates:.5f}"
        )

    if training_stopped:
        break

finish_result = session.finish()

score = np.nan
if isinstance(finish_result, (float, int, np.floating, np.integer)):
    score = float(finish_result)
elif isinstance(finish_result, dict):
    for key in (
        "final_validation_score",
        "best_validation_score",
        "best_score",
        "score",
    ):
        if finish_result.get(key) is not None:
            score = float(finish_result[key])
            break

if not np.isfinite(score):
    for attribute in (
        "final_validation_score",
        "best_validation_score",
        "best_score",
        "score",
    ):
        value = getattr(session, attribute, None)
        if value is not None and not callable(value):
            try:
                score = float(value)
                if np.isfinite(score):
                    break
            except (TypeError, ValueError):
                pass

print(f"Final Validation Score: {score}")
