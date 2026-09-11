import os
os.sched_setaffinity(0, {42, 43, 44, 45, 106, 107, 108, 109})
import html
import json
import numbers
import os
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
import pickle
import re
import unicodedata
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertModel,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForTokenClassification,
)

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime setup and data processing
# ---------------------------------------------------------------------

session = CandidateSession.from_env()

INPUT_DIR = Path("./input")
TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"

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

TRAIN_COLUMNS = [
    "id",
    "target",
    "comment_text",
    "toxicity_annotator_count",
    "identity_annotator_count",
    *IDENTITY_COLUMNS,
]
TEST_COLUMNS = ["id", "comment_text"]

URL_PATTERN = r"(?i)\b(?:https?://|www\.)[^\s<>()]+"
EMAIL_PATTERN = r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
HTML_ENTITY_PATTERN = r"&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z]+);"

IDENTITY_PATTERN = (
    r"(?i)\b(?:"
    r"african[\s-]+american|asian(?:s)?|atheist(?:s)?|autis(?:m|tic)|"
    r"bisexual(?:s)?|black(?:s)?|buddhist(?:s)?|caucasian(?:s)?|"
    r"christian(?:s|ity)?|disabled|disabilit(?:y|ies)|female(?:s)?|"
    r"gay(?:s)?|heterosexual(?:s)?|hindu(?:s)?|hispanic(?:s)?|"
    r"homosexual(?:s)?|islam(?:ic)?|jew(?:s|ish)?|latino(?:s)?|"
    r"lesbian(?:s)?|lgbtq?\+?|male(?:s)?|man|men|woman|women|"
    r"mental[\s-]+illness|muslim(?:s)?|queer(?:s)?|psychiatric|"
    r"trans(?:gender)?|trans[\s-]+(?:man|woman)|white(?:s)?"
    r")\b"
)

TEXT_FEATURE_COLUMNS = [
    "textf_log_chars",
    "textf_log_words",
    "textf_log_mean_word_length",
    "textf_uppercase_ratio",
    "textf_digit_ratio",
    "textf_exclamation_density",
    "textf_question_density",
    "textf_repeated_punctuation_density",
    "textf_caps_word_density",
    "textf_url_density",
    "textf_email_density",
    "textf_non_ascii_ratio",
    "textf_quote_density",
]


def read_competition_data():
    train_header = pd.read_csv(TRAIN_PATH, nrows=0).columns.tolist()
    test_header = pd.read_csv(TEST_PATH, nrows=0).columns.tolist()

    missing_train = sorted(set(TRAIN_COLUMNS) - set(train_header))
    missing_test = sorted(set(TEST_COLUMNS) - set(test_header))
    if missing_train:
        raise ValueError(f"train.csv is missing required columns: {missing_train}")
    if missing_test:
        raise ValueError(f"test.csv is missing required columns: {missing_test}")

    train_dtypes = {
        "target": np.float32,
        "toxicity_annotator_count": np.float32,
        "identity_annotator_count": np.float32,
        **{column: np.float32 for column in IDENTITY_COLUMNS},
    }

    train_frame = pd.read_csv(
        TRAIN_PATH,
        usecols=TRAIN_COLUMNS,
        dtype=train_dtypes,
        low_memory=False,
    )
    test_frame = pd.read_csv(
        TEST_PATH,
        usecols=TEST_COLUMNS,
        low_memory=False,
    )

    if train_frame["id"].duplicated().any():
        raise ValueError("The runtime split requires unique training IDs.")
    if test_frame["id"].duplicated().any():
        raise ValueError("The submission requires unique test IDs.")
    if train_frame["target"].isna().any():
        raise ValueError("Training targets must be present for every training row.")

    return train_frame, test_frame


def normalize_text(text_series):
    text = text_series.fillna("").astype(str)

    entity_rows = text.str.contains(HTML_ENTITY_PATTERN, regex=True, na=False)
    if entity_rows.any():
        text.loc[entity_rows] = text.loc[entity_rows].map(html.unescape)

    unicode_rows = text.str.contains(r"[^\x00-\x7F]", regex=True, na=False)
    if unicode_rows.any():
        text.loc[unicode_rows] = text.loc[unicode_rows].map(
            lambda value: unicodedata.normalize("NFKC", value)
        )

    text = text.str.replace("\u200b", "", regex=False)
    text = text.str.replace("\ufeff", "", regex=False)
    text = text.str.replace("\r\n", "\n", regex=False)
    text = text.str.replace("\r", "\n", regex=False)
    text = text.str.replace(URL_PATTERN, " urltoken ", regex=True)
    text = text.str.replace(EMAIL_PATTERN, " emailtoken ", regex=True)
    text = text.str.replace(r"[\n\t]+", " ", regex=True)
    text = text.str.replace(r"\s{2,}", " ", regex=True).str.strip()
    return text


def build_text_feature_matrix(raw_text, clean_text):
    safe_length = np.maximum(clean_text.str.len().to_numpy(dtype=np.float32), 1.0)
    word_count = clean_text.str.count(r"\S+").to_numpy(dtype=np.float32)
    alpha_count = clean_text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = clean_text.str.count(r"\d").to_numpy(dtype=np.float32)

    exclamation_count = clean_text.str.count("!").to_numpy(dtype=np.float32)
    question_count = clean_text.str.count(r"\?").to_numpy(dtype=np.float32)
    repeated_punctuation = clean_text.str.count(r"[!?]{2,}").to_numpy(dtype=np.float32)
    caps_words = clean_text.str.count(r"\b[A-Z]{2,}\b").to_numpy(dtype=np.float32)
    quote_count = clean_text.str.count(r"""["']""").to_numpy(dtype=np.float32)

    url_count = raw_text.str.count(URL_PATTERN).to_numpy(dtype=np.float32)
    email_count = raw_text.str.count(EMAIL_PATTERN).to_numpy(dtype=np.float32)
    non_ascii_count = raw_text.str.count(r"[^\x00-\x7F]").to_numpy(dtype=np.float32)

    mean_word_length = np.divide(
        alpha_count,
        np.maximum(word_count, 1.0),
        out=np.zeros_like(alpha_count),
        where=word_count > 0,
    )

    return np.column_stack(
        [
            np.log1p(safe_length),
            np.log1p(word_count),
            np.log1p(mean_word_length),
            uppercase_count / np.maximum(alpha_count, 1.0),
            digit_count / safe_length,
            exclamation_count / safe_length,
            question_count / safe_length,
            repeated_punctuation / np.maximum(word_count, 1.0),
            caps_words / np.maximum(word_count, 1.0),
            url_count / np.maximum(word_count, 1.0),
            email_count / np.maximum(word_count, 1.0),
            non_ascii_count / safe_length,
            quote_count / safe_length,
        ]
    ).astype(np.float32, copy=False)


def prepare_text_partition(frame):
    prepared = frame.copy()
    raw_text = prepared["comment_text"].fillna("").astype(str)
    clean_text = normalize_text(raw_text)

    prepared["comment_text"] = clean_text
    prepared["counterfactual_text"] = (
        clean_text.str.replace(
            IDENTITY_PATTERN,
            " identityterm ",
            regex=True,
        )
        .str.replace(r"\s{2,}", " ", regex=True)
        .str.strip()
    )

    prepared["counterfactual_identity_terms"] = clean_text.str.count(
        IDENTITY_PATTERN
    ).astype(np.int16)
    prepared["counterfactual_available"] = (
        prepared["counterfactual_identity_terms"] > 0
    ).astype(np.int8)

    raw_features = build_text_feature_matrix(raw_text, clean_text)
    return prepared, raw_features


def add_training_supervision_columns(frame):
    identity_values = frame[IDENTITY_COLUMNS].to_numpy(dtype=np.float32, copy=True)
    identity_values = np.nan_to_num(identity_values, nan=0.0, posinf=0.0, neginf=0.0)

    annotator_count = (
        frame["identity_annotator_count"].fillna(0.0).to_numpy(dtype=np.float32)
    )
    identity_known = annotator_count > 0.0
    if not identity_known.any():
        identity_known = frame[IDENTITY_COLUMNS].notna().any(axis=1).to_numpy()

    identity_any = (identity_values >= 0.5).any(axis=1)
    toxic_target = frame["target"].to_numpy(dtype=np.float32)
    toxic_binary = (toxic_target >= 0.5).astype(np.int8)

    frame["target_binary"] = toxic_binary
    frame["identity_annotation_available"] = identity_known.astype(np.int8)
    frame["identity_any"] = (identity_known & identity_any).astype(np.int8)

    subgroup_negative = identity_known & identity_any & (toxic_binary == 0)
    subgroup_positive = identity_known & identity_any & (toxic_binary == 1)

    fairness_weight = np.ones(len(frame), dtype=np.float32)
    fairness_weight[subgroup_negative] = 3.0
    fairness_weight[subgroup_positive] = 1.75

    toxicity_votes = (
        frame["toxicity_annotator_count"].fillna(1.0).to_numpy(dtype=np.float32)
    )
    vote_reliability = np.clip(toxicity_votes, 1.0, 10.0) / 10.0
    target_certainty = 0.75 + 0.5 * np.abs(toxic_target - 0.5)

    frame["label_confidence"] = target_certainty.astype(np.float32)
    frame["supervision_weight"] = (
        fairness_weight * (0.75 + 0.25 * np.sqrt(vote_reliability)) * target_certainty
    ).astype(np.float32)

    return frame


raw_train_df, raw_test_df = read_competition_data()

# The runtime-controlled split is performed before fitting any transform.
train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

train_df, train_text_features = prepare_text_partition(train_df)
valid_df, valid_text_features = prepare_text_partition(valid_df)
test_df, test_text_features = prepare_text_partition(test_df)

train_df = add_training_supervision_columns(train_df)
valid_df = add_training_supervision_columns(valid_df)

text_feature_scaler = StandardScaler(copy=True)
train_scaled_features = text_feature_scaler.fit_transform(train_text_features).astype(
    np.float32
)
valid_scaled_features = text_feature_scaler.transform(valid_text_features).astype(
    np.float32
)
test_scaled_features = text_feature_scaler.transform(test_text_features).astype(
    np.float32
)

for column_index, column_name in enumerate(TEXT_FEATURE_COLUMNS):
    train_df[column_name] = train_scaled_features[:, column_index]
    valid_df[column_name] = valid_scaled_features[:, column_index]
    test_df[column_name] = test_scaled_features[:, column_index]

model_text_column = "comment_text"
counterfactual_text_column = "counterfactual_text"
numeric_feature_columns = TEXT_FEATURE_COLUMNS.copy()

preprocessing_state = {
    "model_text_column": model_text_column,
    "counterfactual_text_column": counterfactual_text_column,
    "numeric_feature_columns": numeric_feature_columns,
    "identity_columns": IDENTITY_COLUMNS,
    "identity_pattern": IDENTITY_PATTERN,
    "url_pattern": URL_PATTERN,
    "email_pattern": EMAIL_PATTERN,
}


# ---------------------------------------------------------------------
# Model design
# ---------------------------------------------------------------------

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Only the pretrained encoder is used by the custom toxicity and fairness heads.
# Loading ModernBertModel avoids creating an unused randomly initialized classifier.
model = ModernBertModel.from_pretrained(model_id)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
if device.type == "cuda":
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

identity_column_count = len(IDENTITY_COLUMNS)
numeric_feature_dim = len(numeric_feature_columns)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, strength):
        ctx.strength = float(strength)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return -ctx.strength * gradient_output, None


def gradient_reverse(inputs, strength):
    return GradientReversalFunction.apply(inputs, strength)


class FairnessAdversarialModernBert(nn.Module):
    def __init__(self, encoder, hidden_size, numeric_dim, identity_dim):
        super().__init__()
        self.encoder = encoder
        self.numeric_dim = int(numeric_dim)
        self.identity_dim = int(identity_dim)

        self.text_norm = nn.LayerNorm(hidden_size)
        self.text_dropout = nn.Dropout(0.15)

        self.numeric_projector = nn.Sequential(
            nn.Linear(self.numeric_dim, 48),
            nn.GELU(),
            nn.LayerNorm(48),
            nn.Dropout(0.10),
        )

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size + 48, hidden_size),
            nn.GELU(),
            nn.LayerNorm(hidden_size),
            nn.Dropout(0.20),
            nn.Linear(hidden_size, 1),
        )

        self.identity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.LayerNorm(hidden_size // 2),
            nn.Dropout(0.15),
            nn.Linear(hidden_size // 2, self.identity_dim),
        )

    def forward(
        self,
        input_ids,
        attention_mask,
        numeric_features=None,
        adversarial_strength=1.0,
    ):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        pooled_text = self.text_norm(encoder_outputs.last_hidden_state[:, 0])
        pooled_text = self.text_dropout(pooled_text)

        if numeric_features is None:
            numeric_features = pooled_text.new_zeros(
                (pooled_text.shape[0], self.numeric_dim)
            )

        numeric_features = numeric_features.to(
            device=pooled_text.device,
            dtype=pooled_text.dtype,
        )
        numeric_embedding = self.numeric_projector(numeric_features)

        toxicity_logit = self.toxicity_head(
            torch.cat([pooled_text, numeric_embedding], dim=-1)
        ).squeeze(-1)

        identity_logit = self.identity_head(
            gradient_reverse(pooled_text, adversarial_strength)
        )

        return {
            "toxicity_logit": toxicity_logit,
            "identity_logit": identity_logit,
        }


class BiasAwareAdversarialLoss(nn.Module):
    def __init__(self, identity_pos_weight, identity_loss_weight=0.12):
        super().__init__()
        self.register_buffer(
            "identity_pos_weight",
            torch.as_tensor(identity_pos_weight, dtype=torch.float32),
        )
        self.identity_loss_weight = float(identity_loss_weight)

    def forward(
        self,
        model_outputs,
        toxicity_target,
        supervision_weight=None,
        identity_target=None,
        identity_known=None,
    ):
        toxicity_logit = model_outputs["toxicity_logit"]
        toxicity_target = toxicity_target.to(
            device=toxicity_logit.device,
            dtype=toxicity_logit.dtype,
        ).reshape(-1)

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logit,
            toxicity_target,
            reduction="none",
        )

        if supervision_weight is not None:
            supervision_weight = supervision_weight.to(
                device=toxicity_logit.device,
                dtype=toxicity_logit.dtype,
            ).reshape(-1)
            toxicity_loss = toxicity_loss * supervision_weight

        toxicity_loss = toxicity_loss.mean()

        identity_logit = model_outputs["identity_logit"]
        if identity_target is None or identity_known is None:
            identity_loss = identity_logit.sum() * 0.0
        else:
            identity_target = torch.nan_to_num(
                identity_target.to(
                    device=identity_logit.device,
                    dtype=identity_logit.dtype,
                ),
                nan=0.0,
                posinf=1.0,
                neginf=0.0,
            ).clamp_(0.0, 1.0)

            identity_known = (
                identity_known.to(device=identity_logit.device).bool().reshape(-1)
            )

            if bool(identity_known.any()):
                per_label_loss = F.binary_cross_entropy_with_logits(
                    identity_logit,
                    identity_target,
                    pos_weight=self.identity_pos_weight.to(identity_logit.dtype),
                    reduction="none",
                )
                known_mask = identity_known.unsqueeze(1).to(per_label_loss.dtype)
                identity_loss = (per_label_loss * known_mask).sum() / (
                    known_mask.sum() * per_label_loss.shape[1]
                ).clamp_min(1.0)
            else:
                identity_loss = identity_logit.sum() * 0.0

        return toxicity_loss + self.identity_loss_weight * identity_loss


pretrained_encoder = model
hidden_size = int(pretrained_encoder.config.hidden_size)

model = FairnessAdversarialModernBert(
    encoder=pretrained_encoder,
    hidden_size=hidden_size,
    numeric_dim=numeric_feature_dim,
    identity_dim=identity_column_count,
).to(device)

train_identity_values = train_df[IDENTITY_COLUMNS].to_numpy(
    dtype=np.float32,
    copy=True,
)
train_identity_values = np.nan_to_num(
    train_identity_values,
    nan=0.0,
    posinf=1.0,
    neginf=0.0,
)
train_identity_known = train_df["identity_annotation_available"].to_numpy(
    dtype=bool,
    copy=False,
)

known_count = max(int(train_identity_known.sum()), 1)
soft_positive_count = (
    train_identity_values * train_identity_known[:, None].astype(np.float32)
).sum(axis=0)
soft_negative_count = np.maximum(known_count - soft_positive_count, 1.0)
identity_pos_weight = np.clip(
    soft_negative_count / np.maximum(soft_positive_count, 1.0),
    1.0,
    20.0,
).astype(np.float32)

criterion = BiasAwareAdversarialLoss(
    identity_pos_weight=identity_pos_weight,
    identity_loss_weight=0.12,
).to(device)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
encoder_decay_params = []
encoder_no_decay_params = []
head_decay_params = []
head_no_decay_params = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_encoder_parameter = parameter_name.startswith("encoder.")
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_encoder_parameter and has_no_decay:
        encoder_no_decay_params.append(parameter)
    elif is_encoder_parameter:
        encoder_decay_params.append(parameter)
    elif has_no_decay:
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
            "lr": 1.5e-4,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_params,
            "lr": 1.5e-4,
            "weight_decay": 0.0,
        },
    ],
)

amp_enabled = device.type == "cuda"
try:
    grad_scaler = torch.amp.GradScaler("cuda", enabled=amp_enabled)
except AttributeError:
    grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


# ---------------------------------------------------------------------
# Training, inference callbacks, checkpointing, and runtime evaluation
# ---------------------------------------------------------------------

MAX_SEQUENCE_LENGTH = 256
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 24
GRADIENT_ACCUMULATION_STEPS = 2
MAX_EPOCHS = 2
COUNTERFACTUAL_CONSISTENCY_WEIGHT = 0.12
NUM_WORKERS = max(2, min(4, os.cpu_count() or 2))


class ToxicityDataset(Dataset):
    def __init__(self, frame, positional_indices=None, include_training_fields=False):
        if positional_indices is None:
            positional_indices = np.arange(len(frame), dtype=np.int64)

        self.positions = np.asarray(positional_indices, dtype=np.int64)
        self.texts = frame[model_text_column].to_numpy(dtype=object, copy=False)
        self.counterfactual_texts = frame[counterfactual_text_column].to_numpy(
            dtype=object,
            copy=False,
        )
        self.numeric_features = frame[numeric_feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.include_training_fields = bool(include_training_fields)

        if self.include_training_fields:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.supervision_weights = frame["supervision_weight"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_targets = np.nan_to_num(
                frame[IDENTITY_COLUMNS].to_numpy(dtype=np.float32, copy=True),
                nan=0.0,
                posinf=1.0,
                neginf=0.0,
            )
            self.identity_known = frame["identity_annotation_available"].to_numpy(
                dtype=np.bool_,
                copy=True,
            )
            self.counterfactual_eligible = (
                (frame["target_binary"].to_numpy(dtype=np.int8, copy=False) == 0)
                & (frame["identity_any"].to_numpy(dtype=np.int8, copy=False) == 1)
                & (
                    frame["counterfactual_available"].to_numpy(
                        dtype=np.int8,
                        copy=False,
                    )
                    == 1
                )
            )

    def __len__(self):
        return len(self.positions)

    def __getitem__(self, item_index):
        position = int(self.positions[item_index])
        sample = {
            "text": str(self.texts[position]),
            "counterfactual_text": str(self.counterfactual_texts[position]),
            "numeric_features": self.numeric_features[position],
        }

        if self.include_training_fields:
            sample.update(
                {
                    "target": self.targets[position],
                    "supervision_weight": self.supervision_weights[position],
                    "identity_target": self.identity_targets[position],
                    "identity_known": self.identity_known[position],
                    "counterfactual_eligible": self.counterfactual_eligible[position],
                }
            )

        return sample


def tokenize_text_batch(texts):
    encoded = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        padding=True,
        return_tensors="pt",
    )
    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
    }


def training_collate(samples):
    batch = tokenize_text_batch([sample["text"] for sample in samples])
    batch["counterfactual_texts"] = [
        sample["counterfactual_text"] for sample in samples
    ]
    batch["numeric_features"] = torch.as_tensor(
        np.stack([sample["numeric_features"] for sample in samples]),
        dtype=torch.float32,
    )
    batch["target"] = torch.as_tensor(
        [sample["target"] for sample in samples],
        dtype=torch.float32,
    )
    batch["supervision_weight"] = torch.as_tensor(
        [sample["supervision_weight"] for sample in samples],
        dtype=torch.float32,
    )
    batch["identity_target"] = torch.as_tensor(
        np.stack([sample["identity_target"] for sample in samples]),
        dtype=torch.float32,
    )
    batch["identity_known"] = torch.as_tensor(
        [sample["identity_known"] for sample in samples],
        dtype=torch.bool,
    )
    batch["counterfactual_eligible"] = torch.as_tensor(
        [sample["counterfactual_eligible"] for sample in samples],
        dtype=torch.bool,
    )
    return batch


def inference_collate(samples):
    batch = tokenize_text_batch([sample["text"] for sample in samples])
    batch["numeric_features"] = torch.as_tensor(
        np.stack([sample["numeric_features"] for sample in samples]),
        dtype=torch.float32,
    )
    return batch


def make_loader(dataset, batch_size, collate_fn, shuffle=False):
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=NUM_WORKERS,
        pin_memory=(device.type == "cuda"),
        persistent_workers=True,
        prefetch_factor=2,
        collate_fn=collate_fn,
        drop_last=False,
    )


def autocast_context():
    if amp_enabled:
        return torch.autocast(device_type="cuda", dtype=torch.float16)
    return nullcontext()


def predict_partition(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    was_training = model.training
    model.eval()

    prediction_dataset = ToxicityDataset(
        frame=frame,
        positional_indices=positional_indices,
        include_training_fields=False,
    )
    prediction_loader = make_loader(
        prediction_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        collate_fn=inference_collate,
        shuffle=False,
    )

    predictions = []
    with torch.inference_mode():
        for batch in prediction_loader:
            input_ids = batch["input_ids"].to(device, non_blocking=True)
            attention_mask = batch["attention_mask"].to(device, non_blocking=True)
            numeric_features = batch["numeric_features"].to(device, non_blocking=True)

            with autocast_context():
                model_outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    numeric_features=numeric_features,
                    adversarial_strength=0.0,
                )
                probabilities = torch.sigmoid(model_outputs["toxicity_logit"])

            predictions.append(probabilities.float().cpu().numpy())

    if was_training:
        model.train()

    return np.clip(
        np.concatenate(predictions, axis=0).astype(np.float64, copy=False),
        1e-7,
        1.0 - 1e-7,
    )


def predict_validation(positional_indices):
    return predict_partition(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_partition(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
            "numeric_feature_columns": list(numeric_feature_columns),
            "identity_columns": list(IDENTITY_COLUMNS),
        },
        checkpoint_dir / "fairness_modernbert_state.pt",
    )

    with open(checkpoint_dir / "preprocessing_state.pkl", "wb") as handle:
        pickle.dump(
            {
                "preprocessing_state": preprocessing_state,
                "text_feature_scaler": text_feature_scaler,
            },
            handle,
            protocol=pickle.HIGHEST_PROTOCOL,
        )

    with open(
        checkpoint_dir / "inference_config.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(
            {
                "model_text_column": model_text_column,
                "counterfactual_text_column": counterfactual_text_column,
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "numeric_feature_columns": list(numeric_feature_columns),
                "identity_columns": list(IDENTITY_COLUMNS),
            },
            handle,
            indent=2,
        )

    tokenizer.save_pretrained(str(checkpoint_dir / "tokenizer"))


def load_checkpoint(directory):
    global tokenizer
    global preprocessing_state, text_feature_scaler
    global model_text_column, counterfactual_text_column, numeric_feature_columns

    checkpoint_dir = Path(directory)
    checkpoint = torch.load(
        checkpoint_dir / "fairness_modernbert_state.pt",
        map_location=device,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)

    with open(checkpoint_dir / "preprocessing_state.pkl", "rb") as handle:
        saved_preprocessing = pickle.load(handle)
    preprocessing_state = saved_preprocessing["preprocessing_state"]
    text_feature_scaler = saved_preprocessing["text_feature_scaler"]
    model_text_column = preprocessing_state["model_text_column"]
    counterfactual_text_column = preprocessing_state["counterfactual_text_column"]
    numeric_feature_columns = preprocessing_state["numeric_feature_columns"]

    tokenizer_dir = checkpoint_dir / "tokenizer"
    if tokenizer_dir.exists():
        tokenizer = tokenizer.__class__.from_pretrained(str(tokenizer_dir))


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

train_dataset = ToxicityDataset(
    frame=train_df,
    include_training_fields=True,
)
train_loader = make_loader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    collate_fn=training_collate,
    shuffle=True,
)

model.train()
optimizer.zero_grad(set_to_none=True)
stopped_by_runtime = False

for epoch_index in range(MAX_EPOCHS):
    epoch_loss_sum = 0.0
    completed_updates = 0
    accumulated_batches = 0

    for batch_index, batch in enumerate(train_loader):
        input_ids = batch["input_ids"].to(device, non_blocking=True)
        attention_mask = batch["attention_mask"].to(device, non_blocking=True)
        numeric_features = batch["numeric_features"].to(device, non_blocking=True)
        targets = batch["target"].to(device, non_blocking=True)
        supervision_weights = batch["supervision_weight"].to(device, non_blocking=True)
        identity_targets = batch["identity_target"].to(device, non_blocking=True)
        identity_known = batch["identity_known"].to(device, non_blocking=True)
        counterfactual_eligible = batch["counterfactual_eligible"].to(
            device,
            non_blocking=True,
        )

        adversarial_strength = min(
            1.0,
            0.10 + 0.90 * (completed_updates / max(1000, len(train_loader) // 2)),
        )

        with autocast_context():
            model_outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                numeric_features=numeric_features,
                adversarial_strength=adversarial_strength,
            )

            supervised_loss = criterion(
                model_outputs=model_outputs,
                toxicity_target=targets,
                supervision_weight=supervision_weights,
                identity_target=identity_targets,
                identity_known=identity_known,
            )

            if bool(counterfactual_eligible.any()):
                selected_indices = torch.nonzero(
                    counterfactual_eligible,
                    as_tuple=False,
                ).squeeze(1)

                counterfactual_encoded = tokenize_text_batch(
                    [
                        batch["counterfactual_texts"][int(index)]
                        for index in selected_indices.detach().cpu().tolist()
                    ]
                )
                counterfactual_input_ids = counterfactual_encoded["input_ids"].to(
                    device,
                    non_blocking=True,
                )
                counterfactual_attention_mask = counterfactual_encoded[
                    "attention_mask"
                ].to(device, non_blocking=True)

                counterfactual_outputs = model(
                    input_ids=counterfactual_input_ids,
                    attention_mask=counterfactual_attention_mask,
                    numeric_features=numeric_features.index_select(
                        0,
                        selected_indices,
                    ),
                    adversarial_strength=0.0,
                )

                original_probabilities = torch.sigmoid(
                    model_outputs["toxicity_logit"].index_select(
                        0,
                        selected_indices,
                    )
                )
                counterfactual_probabilities = torch.sigmoid(
                    counterfactual_outputs["toxicity_logit"]
                )
                consistency_loss = F.mse_loss(
                    original_probabilities,
                    counterfactual_probabilities,
                )
            else:
                consistency_loss = model_outputs["toxicity_logit"].sum() * 0.0

            total_loss = (
                supervised_loss + COUNTERFACTUAL_CONSISTENCY_WEIGHT * consistency_loss
            )
            scaled_loss = total_loss / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()
        accumulated_batches += 1

        is_update_boundary = (
            accumulated_batches >= GRADIENT_ACCUMULATION_STEPS
            or batch_index + 1 == len(train_loader)
        )

        if is_update_boundary:
            grad_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)

            completed_updates += 1
            epoch_loss_sum += float(total_loss.detach().float().cpu())
            accumulated_batches = 0

            stop = session.step()
            if stop:
                stopped_by_runtime = True
                break

    mean_epoch_loss = epoch_loss_sum / max(completed_updates, 1)
    print(
        f"Epoch {epoch_index + 1}: updates={completed_updates}, "
        f"train_loss={mean_epoch_loss:.6f}"
    )

    if stopped_by_runtime:
        break

# CandidateSession owns official continuous-AUC evaluation, score logging, checkpoint
# selection, and submission export. finish() may return None after successfully logging it.
session.finish()