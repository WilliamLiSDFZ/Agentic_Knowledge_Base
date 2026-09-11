import html
import json
import os
import random
import re
import shutil
import unicodedata
from contextlib import nullcontext
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from engine.candidate_runtime import CandidateSession
from sklearn.preprocessing import RobustScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
)


SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)
CHECKPOINT_STATE_NAME = "bias_aware_modernbert_state.pt"

IDENTITY_COLUMNS = [
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

ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200d\u2060\ufeff]")
URL_RE = re.compile(
    r"(?i)\b(?:https?://|www\.)[^\s<>\]]+|\b[a-z0-9.-]+\.(?:com|org|net|edu|gov|co|io|uk|ca|au)(?:/[^\s<>\]]*)?"
)
USER_RE = re.compile(r"(?<![\w@])@[A-Za-z0-9_]{2,}")
WHITESPACE_RE = re.compile(r"\s+")
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
TOXIC_LEXICON_RE = re.compile(
    r"(?i)\b(?:fuck(?:ing|er|ed|s)?|shit(?:ty)?|idiot(?:ic)?|moron(?:ic)?|stupid|dumb|"
    r"hate|racist|bigot(?:ed)?|nazi|terrorist|kill|die|disgusting|liar|asshole|bitch)\b"
)
IDENTITY_TERM_RE = re.compile(
    r"(?i)\b(?:man|men|male|woman|women|female|gay|lesbian|homosexual|christian|jew|jewish|"
    r"muslim|islam|black|white|african|mental(?:ly)?|psychiatric|disabled|disability)\b"
)


def clean_comment(value):
    if pd.isna(value):
        return ""

    text = html.unescape(str(value))
    text = unicodedata.normalize("NFKC", text)
    text = ZERO_WIDTH_RE.sub("", text)
    text = URL_RE.sub(" [URL] ", text)
    text = USER_RE.sub(" [USER] ", text)
    return WHITESPACE_RE.sub(" ", text).strip()


def build_text_features(texts):
    text = texts.fillna("").astype(str)
    lower = text.str.lower()

    word_lists = lower.str.findall(WORD_RE)
    word_count = word_lists.str.len().astype(np.float32)
    unique_word_count = word_lists.map(lambda words: len(set(words))).astype(np.float32)

    letter_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    upper_count = text.str.count(r"[A-Z]").astype(np.float32)
    char_count = text.str.len().astype(np.float32)

    features = pd.DataFrame(
        {
            "char_count": char_count,
            "word_count": word_count,
            "unique_word_count": unique_word_count,
            "unique_word_ratio": (
                unique_word_count / np.maximum(word_count, 1.0)
            ).astype(np.float32),
            "letter_count": letter_count,
            "uppercase_ratio": (upper_count / np.maximum(letter_count, 1.0)).astype(
                np.float32
            ),
            "digit_count": text.str.count(r"\d").astype(np.float32),
            "punctuation_count": text.str.count(r"""[!?.,;:'"()\-\[\]{}]""").astype(
                np.float32
            ),
            "exclamation_count": text.str.count("!").astype(np.float32),
            "question_count": text.str.count(r"\?").astype(np.float32),
            "newline_count": text.str.count(r"\n").astype(np.float32),
            "sentence_end_count": text.str.count(r"[.!?]").astype(np.float32),
            "has_url": text.str.contains(r"\[URL\]", regex=True).astype(np.float32),
            "has_user_mention": text.str.contains(r"\[USER\]", regex=True).astype(
                np.float32
            ),
            "has_quote": text.str.contains(r"""["']""", regex=True).astype(np.float32),
            "toxic_lexicon_count": lower.str.count(TOXIC_LEXICON_RE).astype(np.float32),
            "identity_term_count": lower.str.count(IDENTITY_TERM_RE).astype(np.float32),
            "repeated_exclamation": text.str.contains(r"!{2,}", regex=True).astype(
                np.float32
            ),
            "repeated_question": text.str.contains(r"\?{2,}", regex=True).astype(
                np.float32
            ),
            "elongated_token": lower.str.contains(
                r"\b\w*(\w)\1{2,}\w*\b", regex=True
            ).astype(np.float32),
        },
        index=text.index,
    )
    return features.replace([np.inf, -np.inf], 0.0).fillna(0.0).astype(np.float32)


def add_engineered_columns(frame, numeric_features):
    output = frame.copy()
    output["model_text"] = output["comment_text"].map(clean_comment)
    output["text_is_empty"] = (output["model_text"].str.len() == 0).astype(np.int8)

    for column in numeric_features.columns:
        output[f"text_feature_{column}"] = numeric_features[column].to_numpy(
            dtype=np.float32
        )

    return output


def make_bias_aware_training_weights(frame):
    binary_target = frame["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
    identity_values = frame[IDENTITY_COLUMNS].apply(pd.to_numeric, errors="coerce")
    subgroup = (identity_values >= 0.5).any(axis=1).to_numpy()

    weights = np.full(len(frame), 0.25, dtype=np.float32)
    weights += (subgroup & ~binary_target).astype(np.float32)
    weights += (~subgroup & binary_target).astype(np.float32)
    weights += (subgroup & binary_target).astype(np.float32)
    weights /= max(float(weights.mean()), 1e-8)

    return (
        binary_target.astype(np.int8),
        subgroup.astype(np.int8),
        weights.astype(np.float32),
    )


session = CandidateSession.from_env()

train_header = pd.read_csv(INPUT_DIR / "train.csv", nrows=0).columns.tolist()
test_header = pd.read_csv(INPUT_DIR / "test.csv", nrows=0).columns.tolist()

required_train_columns = ["id", "target", "comment_text"]
optional_train_columns = (
    IDENTITY_COLUMNS
    + AUXILIARY_TARGET_COLUMNS
    + ["toxicity_annotator_count", "identity_annotator_count"]
)

train_usecols = [
    column
    for column in required_train_columns + optional_train_columns
    if column in train_header
]
test_usecols = [column for column in ["id", "comment_text"] if column in test_header]

missing_required = set(required_train_columns) - set(train_usecols)
if missing_required:
    raise ValueError(f"Missing required training columns: {sorted(missing_required)}")

missing_identities = set(IDENTITY_COLUMNS) - set(train_usecols)
if missing_identities:
    raise ValueError(f"Missing official identity columns: {sorted(missing_identities)}")

train_df = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=train_usecols,
    low_memory=False,
)
test_df = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=test_usecols,
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_df, test_df)

for frame in (train_df, valid_df, test_df):
    frame["id"] = frame["id"].astype(str)
    frame["comment_text"] = frame["comment_text"].fillna("").astype(str)

for frame in (train_df, valid_df):
    for column in ["target"] + IDENTITY_COLUMNS + AUXILIARY_TARGET_COLUMNS:
        if column in frame.columns:
            frame[column] = pd.to_numeric(frame[column], errors="coerce").astype(
                np.float32
            )

train_text_features_raw = build_text_features(train_df["comment_text"])
valid_text_features_raw = build_text_features(valid_df["comment_text"])
test_text_features_raw = build_text_features(test_df["comment_text"])

count_like_features = [
    column
    for column in train_text_features_raw.columns
    if column
    not in {
        "unique_word_ratio",
        "uppercase_ratio",
        "has_url",
        "has_user_mention",
        "has_quote",
        "repeated_exclamation",
        "repeated_question",
        "elongated_token",
    }
]

for feature_name in count_like_features:
    train_text_features_raw[feature_name] = np.log1p(
        train_text_features_raw[feature_name]
    )
    valid_text_features_raw[feature_name] = np.log1p(
        valid_text_features_raw[feature_name]
    )
    test_text_features_raw[feature_name] = np.log1p(
        test_text_features_raw[feature_name]
    )

text_feature_scaler = RobustScaler(quantile_range=(5.0, 95.0))
text_feature_scaler.fit(train_text_features_raw)

train_text_features = pd.DataFrame(
    text_feature_scaler.transform(train_text_features_raw),
    columns=train_text_features_raw.columns,
    index=train_df.index,
).astype(np.float32)

valid_text_features = pd.DataFrame(
    text_feature_scaler.transform(valid_text_features_raw),
    columns=valid_text_features_raw.columns,
    index=valid_df.index,
).astype(np.float32)

test_text_features = pd.DataFrame(
    text_feature_scaler.transform(test_text_features_raw),
    columns=test_text_features_raw.columns,
    index=test_df.index,
).astype(np.float32)

train_df = add_engineered_columns(train_df, train_text_features)
valid_df = add_engineered_columns(valid_df, valid_text_features)
test_df = add_engineered_columns(test_df, test_text_features)

train_target_binary, train_subgroup, train_sample_weight = (
    make_bias_aware_training_weights(train_df)
)
train_df["target_binary"] = train_target_binary
train_df["is_official_identity_subgroup"] = train_subgroup
train_df["bias_aware_sample_weight"] = train_sample_weight

valid_df["target_binary"] = (
    valid_df["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
).astype(np.int8)
valid_df["is_official_identity_subgroup"] = (
    valid_df[IDENTITY_COLUMNS].ge(0.5).any(axis=1).to_numpy()
).astype(np.int8)

feature_config = {
    "identity_columns": IDENTITY_COLUMNS,
    "auxiliary_target_columns": [
        column for column in AUXILIARY_TARGET_COLUMNS if column in train_df.columns
    ],
    "numeric_text_feature_columns": [
        f"text_feature_{column}" for column in train_text_features.columns
    ],
    "text_column": "model_text",
    "target_column": "target",
    "binary_target_column": "target_binary",
    "sample_weight_column": "bias_aware_sample_weight",
    "normalization": {
        "unicode": "NFKC",
        "url_token": "[URL]",
        "user_token": "[USER]",
        "whitespace": "collapsed",
    },
    "scaler": "RobustScaler(quantile_range=(5, 95))",
    "seed": SEED,
}

joblib.dump(text_feature_scaler, WORKING_DIR / "text_feature_scaler.joblib")
with open(WORKING_DIR / "feature_config.json", "w", encoding="utf-8") as feature_file:
    json.dump(feature_config, feature_file, indent=2)

train_df.to_pickle(WORKING_DIR / "prepared_train.pkl")
valid_df.to_pickle(WORKING_DIR / "prepared_valid.pkl")
test_df.to_pickle(WORKING_DIR / "prepared_test.pkl")

np.save(
    WORKING_DIR / "train_text_features.npy",
    train_text_features.to_numpy(dtype=np.float32),
)
np.save(
    WORKING_DIR / "valid_text_features.npy",
    valid_text_features.to_numpy(dtype=np.float32),
)
np.save(
    WORKING_DIR / "test_text_features.npy",
    test_text_features.to_numpy(dtype=np.float32),
)

NUMERIC_FEATURE_DIM = len(feature_config["numeric_text_feature_columns"])
AUXILIARY_TARGET_COLUMNS = feature_config["auxiliary_target_columns"]
IDENTITY_COLUMNS = feature_config["identity_columns"]

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)


class BiasAwareModernBert(nn.Module):
    def __init__(
        self,
        pretrained_sequence_classifier,
        numeric_feature_dim,
        auxiliary_dim,
        dropout_probability=0.15,
    ):
        super().__init__()

        self.encoder = pretrained_sequence_classifier.model
        hidden_size = self.encoder.config.hidden_size
        numeric_hidden_size = 128

        self.text_dropout = nn.Dropout(dropout_probability)
        self.numeric_encoder = nn.Sequential(
            nn.LayerNorm(numeric_feature_dim),
            nn.Linear(numeric_feature_dim, numeric_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(numeric_hidden_size, numeric_hidden_size),
            nn.GELU(),
        )
        self.numeric_gate_logit = nn.Parameter(torch.tensor(-2.0))

        fused_size = hidden_size + numeric_hidden_size
        self.fusion_norm = nn.LayerNorm(fused_size)
        self.toxicity_head = nn.Sequential(
            nn.Linear(fused_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size // 2, 1),
        )
        self.auxiliary_head = nn.Sequential(
            nn.Linear(fused_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size // 2, auxiliary_dim),
        )

    def forward(self, input_ids, attention_mask, numeric_features=None):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        cls_embedding = self.text_dropout(encoder_outputs.last_hidden_state[:, 0, :])

        if numeric_features is None:
            numeric_features = torch.zeros(
                (input_ids.shape[0], self.numeric_encoder[1].in_features),
                dtype=cls_embedding.dtype,
                device=cls_embedding.device,
            )
        else:
            numeric_features = numeric_features.to(
                device=cls_embedding.device,
                dtype=cls_embedding.dtype,
            )

        numeric_embedding = self.numeric_encoder(numeric_features)
        gated_numeric_embedding = (
            torch.sigmoid(self.numeric_gate_logit) * numeric_embedding
        )

        fused_embedding = self.fusion_norm(
            torch.cat([cls_embedding, gated_numeric_embedding], dim=-1)
        )
        toxicity_logits = self.toxicity_head(fused_embedding).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(fused_embedding)

        return {
            "toxicity_logits": toxicity_logits,
            "auxiliary_logits": auxiliary_logits,
        }

    @torch.inference_mode()
    def predict_proba(self, input_ids, attention_mask, numeric_features=None):
        was_training = self.training
        self.eval()
        outputs = self.forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            numeric_features=numeric_features,
        )
        probabilities = torch.sigmoid(outputs["toxicity_logits"])
        if was_training:
            self.train()
        return probabilities


class BiasAwareAucLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight=0.15,
        pairwise_weight=0.35,
        tail_temperature=0.35,
        max_pairs_per_class=64,
        generalized_mean_power=-5.0,
    ):
        super().__init__()
        self.auxiliary_weight = auxiliary_weight
        self.pairwise_weight = pairwise_weight
        self.tail_temperature = tail_temperature
        self.max_pairs_per_class = max_pairs_per_class
        self.generalized_mean_power = generalized_mean_power

    def _bpsn_pairwise_quality(
        self,
        logits,
        subgroup_negative_mask,
        background_toxic_mask,
    ):
        subgroup_negative_scores = logits[subgroup_negative_mask].float()
        background_toxic_scores = logits[background_toxic_mask].float()

        if (
            subgroup_negative_scores.numel() == 0
            or background_toxic_scores.numel() == 0
        ):
            return None

        if background_toxic_scores.numel() > self.max_pairs_per_class:
            selected = torch.randperm(
                background_toxic_scores.numel(),
                device=background_toxic_scores.device,
            )[: self.max_pairs_per_class]
            background_toxic_scores = background_toxic_scores[selected]

        score_differences = (
            background_toxic_scores[:, None] - subgroup_negative_scores[None, :]
        )
        return torch.sigmoid(score_differences).mean()

    def forward(
        self,
        toxicity_logits,
        target_binary,
        sample_weight=None,
        auxiliary_logits=None,
        auxiliary_targets=None,
        identity_memberships=None,
    ):
        target_binary = target_binary.float().reshape(-1)
        toxicity_logits = toxicity_logits.reshape(-1)

        main_loss_per_row = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            target_binary,
            reduction="none",
        )

        if sample_weight is None:
            main_loss = main_loss_per_row.mean()
        else:
            sample_weight = sample_weight.float().reshape(-1)
            main_loss = (
                main_loss_per_row * sample_weight
            ).sum() / sample_weight.sum().clamp_min(1e-6)

        auxiliary_loss = toxicity_logits.new_zeros(())
        if auxiliary_logits is not None and auxiliary_targets is not None:
            auxiliary_targets = auxiliary_targets.float()
            valid_auxiliary_labels = torch.isfinite(auxiliary_targets)
            safe_auxiliary_targets = torch.nan_to_num(
                auxiliary_targets,
                nan=0.0,
                posinf=1.0,
                neginf=0.0,
            )
            auxiliary_loss_per_element = F.binary_cross_entropy_with_logits(
                auxiliary_logits,
                safe_auxiliary_targets,
                reduction="none",
            )
            auxiliary_loss = (
                auxiliary_loss_per_element * valid_auxiliary_labels.float()
            ).sum() / valid_auxiliary_labels.float().sum().clamp_min(1.0)

        bpsn_qualities = []
        if identity_memberships is not None:
            identity_memberships = torch.nan_to_num(
                identity_memberships.float(),
                nan=0.0,
            )
            positive_target = target_binary >= 0.5
            negative_target = ~positive_target

            group_count = min(
                identity_memberships.shape[1],
                len(IDENTITY_COLUMNS),
            )

            for group_index in range(group_count):
                subgroup = identity_memberships[:, group_index] >= 0.5
                bpsn_quality = self._bpsn_pairwise_quality(
                    toxicity_logits,
                    subgroup & negative_target,
                    (~subgroup) & positive_target,
                )
                if bpsn_quality is not None:
                    bpsn_qualities.append(bpsn_quality)

        pairwise_loss = toxicity_logits.new_zeros(())
        if bpsn_qualities:
            qualities = torch.stack(bpsn_qualities).float().clamp(1e-6, 1.0)
            power = self.generalized_mean_power
            log_generalized_mean = (
                torch.logsumexp(power * torch.log(qualities), dim=0)
                - np.log(float(len(bpsn_qualities)))
            ) / power
            pairwise_loss = 1.0 - torch.exp(log_generalized_mean)

        return (
            main_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.pairwise_weight * pairwise_loss
        )


model = BiasAwareModernBert(
    pretrained_sequence_classifier=model,
    numeric_feature_dim=NUMERIC_FEATURE_DIM,
    auxiliary_dim=len(AUXILIARY_TARGET_COLUMNS),
    dropout_probability=0.15,
)

criterion = BiasAwareAucLoss(
    auxiliary_weight=0.15,
    pairwise_weight=0.35,
    tail_temperature=0.35,
    max_pairs_per_class=64,
    generalized_mean_power=-5.0,
)

no_decay_terms = ("bias", "layernorm.weight", "layer_norm.weight", "norm.weight")
backbone_decay_parameters = []
backbone_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = parameter_name.lower().endswith(no_decay_terms)
    is_backbone = parameter_name.startswith("encoder.")

    if is_backbone and is_no_decay:
        backbone_no_decay_parameters.append(parameter)
    elif is_backbone:
        backbone_decay_parameters.append(parameter)
    elif is_no_decay:
        head_no_decay_parameters.append(parameter)
    else:
        head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_decay_parameters,
            "lr": 1.2e-5,
            "weight_decay": 0.01,
        },
        {
            "params": backbone_no_decay_parameters,
            "lr": 1.2e-5,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_parameters,
            "lr": 8.0e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_parameters,
            "lr": 8.0e-5,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"
pin_memory = device.type == "cuda"

TEXT_COLUMN = feature_config["text_column"]
NUMERIC_COLUMNS = feature_config["numeric_text_feature_columns"]
AUXILIARY_COLUMNS = feature_config["auxiliary_target_columns"]
IDENTITY_COLUMNS = feature_config["identity_columns"]
TARGET_COLUMN = feature_config["binary_target_column"]
WEIGHT_COLUMN = feature_config["sample_weight_column"]

model.to(device)

if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable()


class ToxicityDataset(Dataset):
    def __init__(
        self,
        texts,
        numeric_features,
        targets=None,
        sample_weights=None,
        auxiliary_targets=None,
        identity_memberships=None,
    ):
        self.texts = texts
        self.numeric_features = numeric_features
        self.targets = targets
        self.sample_weights = sample_weights
        self.auxiliary_targets = auxiliary_targets
        self.identity_memberships = identity_memberships

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        record = {
            "text": str(self.texts[index]),
            "numeric_features": self.numeric_features[index],
        }

        if self.targets is not None:
            record["target"] = self.targets[index]
            record["sample_weight"] = self.sample_weights[index]
            record["auxiliary_targets"] = self.auxiliary_targets[index]
            record["identity_memberships"] = self.identity_memberships[index]

        return record


def toxicity_collate(records):
    batch = {
        "texts": [record["text"] for record in records],
        "numeric_features": torch.from_numpy(
            np.stack([record["numeric_features"] for record in records]).astype(
                np.float32,
                copy=False,
            )
        ),
    }

    if "target" in records[0]:
        batch["target"] = torch.as_tensor(
            [record["target"] for record in records],
            dtype=torch.float32,
        )
        batch["sample_weight"] = torch.as_tensor(
            [record["sample_weight"] for record in records],
            dtype=torch.float32,
        )
        batch["auxiliary_targets"] = torch.from_numpy(
            np.stack([record["auxiliary_targets"] for record in records]).astype(
                np.float32,
                copy=False,
            )
        )
        batch["identity_memberships"] = torch.from_numpy(
            np.stack([record["identity_memberships"] for record in records]).astype(
                np.float32,
                copy=False,
            )
        )

    return batch


train_texts = train_df[TEXT_COLUMN].fillna("").astype(str).to_numpy(dtype=object)
train_numeric_features = train_df[NUMERIC_COLUMNS].to_numpy(dtype=np.float32)
train_targets = train_df[TARGET_COLUMN].to_numpy(dtype=np.float32)
train_sample_weights = train_df[WEIGHT_COLUMN].to_numpy(dtype=np.float32)
train_auxiliary_targets = train_df[AUXILIARY_COLUMNS].to_numpy(dtype=np.float32)
train_identity_memberships = train_df[IDENTITY_COLUMNS].to_numpy(dtype=np.float32)

train_dataset = ToxicityDataset(
    texts=train_texts,
    numeric_features=train_numeric_features,
    targets=train_targets,
    sample_weights=train_sample_weights,
    auxiliary_targets=train_auxiliary_targets,
    identity_memberships=train_identity_memberships,
)

class IdentityCyclingBPSNBatchSampler(Sampler):
    def __init__(self, frame, sample_weights, batch_size=8, seed=SEED):
        self.batch_size = batch_size
        self.seed = seed
        self.epoch = 0
        self.num_rows = len(frame)

        targets = frame["target_binary"].to_numpy(dtype=np.int8) >= 0.5
        memberships = np.nan_to_num(
            frame[IDENTITY_COLUMNS].to_numpy(dtype=np.float32),
            nan=0.0,
        )

        self.identity_pools = []
        for group_index, identity_name in enumerate(IDENTITY_COLUMNS):
            subgroup = memberships[:, group_index] >= 0.5
            anchors = np.flatnonzero(subgroup & ~targets).astype(np.int64)
            comparators = np.flatnonzero(~subgroup & targets).astype(np.int64)
            if anchors.size > 0 and comparators.size > 0:
                self.identity_pools.append(
                    (identity_name, anchors, comparators)
                )

        if not self.identity_pools:
            raise ValueError("No valid official BPSN identity pools were constructed")

        fill_weights = np.asarray(sample_weights, dtype=np.float64)
        fill_weights = np.where(
            np.isfinite(fill_weights) & (fill_weights > 0.0),
            fill_weights,
            0.0,
        )
        if fill_weights.sum() == 0.0:
            fill_weights.fill(1.0)
        self.fill_probabilities = fill_weights / fill_weights.sum()

    def __len__(self):
        return (self.num_rows + self.batch_size - 1) // self.batch_size

    def __iter__(self):
        rng = np.random.default_rng(self.seed + self.epoch)
        self.epoch += 1

        identity_order = np.arange(len(self.identity_pools))
        rng.shuffle(identity_order)

        anchor_orders = []
        anchor_cursors = []
        for _, anchors, _ in self.identity_pools:
            order = anchors.copy()
            rng.shuffle(order)
            anchor_orders.append(order)
            anchor_cursors.append(0)

        def draw_anchors(pool_index, count):
            selected = []
            while len(selected) < count:
                order = anchor_orders[pool_index]
                cursor = anchor_cursors[pool_index]
                available = len(order) - cursor
                take = min(count - len(selected), available)
                selected.extend(order[cursor : cursor + take].tolist())
                cursor += take
                if cursor == len(order):
                    rng.shuffle(order)
                    cursor = 0
                anchor_cursors[pool_index] = cursor
            return selected

        for batch_number in range(len(self)):
            pool_index = identity_order[batch_number % len(identity_order)]
            _, _, comparators = self.identity_pools[pool_index]

            batch = draw_anchors(pool_index, count=1)
            comparator_indices = rng.choice(
                comparators,
                size=1,
                replace=comparators.size < 1,
            )
            batch.extend(comparator_indices.tolist())

            fill_count = self.batch_size - len(batch)
            if fill_count > 0:
                fill_indices = rng.choice(
                    self.num_rows,
                    size=fill_count,
                    replace=True,
                    p=self.fill_probabilities,
                )
                batch.extend(fill_indices.tolist())

            rng.shuffle(batch)
            yield batch


num_workers = max(2, min(4, os.cpu_count() or 2))

train_batch_sampler = IdentityCyclingBPSNBatchSampler(
    train_df,
    sample_weights=train_sample_weights,
    batch_size=8,
    seed=SEED,
)

train_loader = DataLoader(
    train_dataset,
    batch_sampler=train_batch_sampler,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    collate_fn=toxicity_collate,
)

scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)
gradient_accumulation_steps = 2
max_length = 256
optimizer_steps = 0


def autocast_context():
    if amp_enabled:
        return torch.cuda.amp.autocast(dtype=torch.float16)
    return nullcontext()


def predict_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if positions.size == 0:
        return np.empty(0, dtype=np.float32)

    all_texts = frame[TEXT_COLUMN].fillna("").astype(str).to_numpy(dtype=object)
    all_numeric = frame[NUMERIC_COLUMNS].to_numpy(dtype=np.float32)

    inference_dataset = ToxicityDataset(
        texts=all_texts[positions],
        numeric_features=all_numeric[positions],
    )
    inference_loader = DataLoader(
        inference_dataset,
        batch_size=16,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=pin_memory,
        persistent_workers=False,
        collate_fn=toxicity_collate,
    )

    was_training = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                encoded = tokenizer(
                    batch["texts"],
                    truncation=True,
                    max_length=max_length,
                    padding=True,
                    pad_to_multiple_of=8 if amp_enabled else None,
                    return_tensors="pt",
                )

                input_ids = encoded["input_ids"].to(device, non_blocking=True)
                attention_mask = encoded["attention_mask"].to(
                    device,
                    non_blocking=True,
                )
                numeric_features = batch["numeric_features"].to(
                    device,
                    non_blocking=True,
                )

                with autocast_context():
                    outputs = model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        numeric_features=numeric_features,
                    )
                    probabilities = torch.sigmoid(outputs["toxicity_logits"])

                predictions.append(
                    probabilities.detach().float().cpu().numpy().astype(np.float32)
                )
    finally:
        model.train(was_training)

    return np.concatenate(predictions, axis=0)


def _binary_auc(labels, scores):
    labels = np.asarray(labels, dtype=bool)
    scores = np.asarray(scores, dtype=np.float64)

    positive_count = int(labels.sum())
    negative_count = int((~labels).sum())
    if positive_count == 0 or negative_count == 0:
        return None

    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(scores.size, dtype=np.float64)
    start = 0

    while start < scores.size:
        end = start + 1
        while end < scores.size and scores[order[end]] == scores[order[start]]:
            end += 1
        ranks[order[start:end]] = 0.5 * (start + end + 1)
        start = end

    positive_rank_sum = ranks[labels].sum()
    return float(
        (positive_rank_sum - positive_count * (positive_count + 1) / 2.0)
        / (positive_count * negative_count)
    )


def print_validation_bpsn_diagnostics(positional_indices, predictions):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    targets = valid_df[TARGET_COLUMN].to_numpy(dtype=np.float32)[positions] >= 0.5
    memberships = np.nan_to_num(
        valid_df[IDENTITY_COLUMNS].to_numpy(dtype=np.float32)[positions],
        nan=0.0,
    )

    bpsn_aucs = []
    diagnostic_parts = []

    for group_index, identity_name in enumerate(IDENTITY_COLUMNS):
        subgroup = memberships[:, group_index] >= 0.5
        bpsn_mask = (subgroup & ~targets) | (~subgroup & targets)
        auc = _binary_auc(targets[bpsn_mask], predictions[bpsn_mask])

        if auc is None:
            diagnostic_parts.append(f"{identity_name}=NA")
        else:
            bpsn_aucs.append(auc)
            diagnostic_parts.append(f"{identity_name}={auc:.5f}")

    if bpsn_aucs:
        bpsn_generalized_mean = float(
            np.exp(np.mean(-5.0 * np.log(np.clip(bpsn_aucs, 1e-12, 1.0))) / -5.0)
        )
        generalized_mean_text = f"{bpsn_generalized_mean:.5f}"
    else:
        generalized_mean_text = "NA"

    print(
        "Validation BPSN diagnostics: "
        f"p=-5_generalized_mean={generalized_mean_text}; "
        + ", ".join(diagnostic_parts)
    )


def print_validation_official_diagnostics(positional_indices, predictions):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    targets = valid_df[TARGET_COLUMN].to_numpy(dtype=np.float32)[positions] >= 0.5
    memberships = np.nan_to_num(
        valid_df[IDENTITY_COLUMNS].to_numpy(dtype=np.float32)[positions],
        nan=0.0,
    )

    overall_auc = _binary_auc(targets, predictions)
    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for group_index in range(len(IDENTITY_COLUMNS)):
        subgroup = memberships[:, group_index] >= 0.5

        subgroup_auc = _binary_auc(targets[subgroup], predictions[subgroup])
        if subgroup_auc is not None:
            subgroup_aucs.append(subgroup_auc)

        bpsn_mask = (subgroup & ~targets) | (~subgroup & targets)
        bpsn_auc = _binary_auc(targets[bpsn_mask], predictions[bpsn_mask])
        if bpsn_auc is not None:
            bpsn_aucs.append(bpsn_auc)

        bnsp_mask = (subgroup & targets) | (~subgroup & ~targets)
        bnsp_auc = _binary_auc(targets[bnsp_mask], predictions[bnsp_mask])
        if bnsp_auc is not None:
            bnsp_aucs.append(bnsp_auc)

    def generalized_mean(aucs):
        if not aucs:
            return None
        return float(
            np.exp(
                np.mean(
                    -5.0 * np.log(np.clip(aucs, 1e-12, 1.0))
                ) / -5.0
            )
        )

    subgroup_generalized_mean = generalized_mean(subgroup_aucs)
    bpsn_generalized_mean = generalized_mean(bpsn_aucs)
    bnsp_generalized_mean = generalized_mean(bnsp_aucs)

    def format_auc(value):
        return "NA" if value is None else f"{value:.5f}"

    print(
        "Validation official diagnostics: "
        f"overall={format_auc(overall_auc)}; "
        f"subgroup_p=-5_generalized_mean="
        f"{format_auc(subgroup_generalized_mean)}; "
        f"bpsn_p=-5_generalized_mean={format_auc(bpsn_generalized_mean)}; "
        f"bnsp_p=-5_generalized_mean={format_auc(bnsp_generalized_mean)}"
    )


def predict_validation(positional_indices):
    predictions = predict_positions(valid_df, positional_indices)
    print_validation_bpsn_diagnostics(positional_indices, predictions)
    print_validation_official_diagnostics(positional_indices, predictions)
    return predictions


def predict_test(positional_indices):
    return predict_positions(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    checkpoint_payload = {
        "model_state_dict": model.state_dict(),
        "optimizer_steps": int(optimizer_steps),
        "max_length": int(max_length),
        "numeric_feature_columns": NUMERIC_COLUMNS,
        "auxiliary_target_columns": AUXILIARY_COLUMNS,
        "identity_columns": IDENTITY_COLUMNS,
    }
    torch.save(checkpoint_payload, checkpoint_directory / CHECKPOINT_STATE_NAME)

    with open(
        checkpoint_directory / "inference_config.json",
        "w",
        encoding="utf-8",
    ) as config_file:
        json.dump(
            {
                "model_class": model.__class__.__name__,
                "tokenizer_name": tokenizer.name_or_path,
                "max_length": max_length,
                "numeric_feature_columns": NUMERIC_COLUMNS,
                "text_column": TEXT_COLUMN,
            },
            config_file,
            indent=2,
        )

    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")

    for artifact_name in ("feature_config.json", "text_feature_scaler.joblib"):
        source_path = WORKING_DIR / artifact_name
        if source_path.exists():
            shutil.copy2(source_path, checkpoint_directory / artifact_name)


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_payload = torch.load(
        checkpoint_directory / CHECKPOINT_STATE_NAME,
        map_location="cpu",
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

stop_training = False
optimizer.zero_grad(set_to_none=True)

for epoch in range(100000):
    if stop_training:
        break

    model.train()
    epoch_loss_sum = 0.0
    epoch_batches = 0
    pending_accumulation = 0

    for batch in train_loader:
        encoded = tokenizer(
            batch["texts"],
            truncation=True,
            max_length=max_length,
            padding=True,
            pad_to_multiple_of=8 if amp_enabled else None,
            return_tensors="pt",
        )

        input_ids = encoded["input_ids"].to(device, non_blocking=True)
        attention_mask = encoded["attention_mask"].to(device, non_blocking=True)
        numeric_features = batch["numeric_features"].to(device, non_blocking=True)
        targets = batch["target"].to(device, non_blocking=True)
        sample_weights = batch["sample_weight"].to(device, non_blocking=True)
        auxiliary_targets = batch["auxiliary_targets"].to(device, non_blocking=True)
        identity_memberships = batch["identity_memberships"].to(
            device,
            non_blocking=True,
        )

        with autocast_context():
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                numeric_features=numeric_features,
            )
            batch_loss = criterion(
                toxicity_logits=outputs["toxicity_logits"],
                target_binary=targets,
                sample_weight=sample_weights,
                auxiliary_logits=outputs["auxiliary_logits"],
                auxiliary_targets=auxiliary_targets,
                identity_memberships=identity_memberships,
            )
            scaled_loss = batch_loss / gradient_accumulation_steps

        scaler.scale(scaled_loss).backward()
        epoch_loss_sum += float(batch_loss.detach().cpu())
        epoch_batches += 1
        pending_accumulation += 1

        if pending_accumulation == gradient_accumulation_steps:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)

            optimizer_steps += 1
            pending_accumulation = 0

            if session.step():
                stop_training = True
                break

    if not stop_training and pending_accumulation > 0:
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)

        optimizer_steps += 1
        if session.step():
            stop_training = True

    if epoch_batches > 0:
        print(
            f"Epoch {epoch + 1}: mean_train_loss={epoch_loss_sum / epoch_batches:.6f}, "
            f"optimizer_steps={optimizer_steps}"
        )

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
