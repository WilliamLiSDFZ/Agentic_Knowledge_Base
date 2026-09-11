import os

# ModernBERT's reference path can invoke TorchDynamo/Inductor, which requires a
# system C compiler unavailable in this execution environment.
os.environ.setdefault("TORCHDYNAMO_DISABLE", "1")
os.environ.setdefault("TORCH_COMPILE_DISABLE", "1")

import re
import html
import json
import shutil
import unicodedata
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import RobustScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from transformers import (
    AutoConfig,
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

session = CandidateSession.from_env()

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

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

TOXICITY_AUXILIARY_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

STRUCTURAL_FEATURE_NAMES = [
    "log_char_count",
    "log_word_count",
    "uppercase_ratio",
    "digit_ratio",
    "non_ascii_ratio",
    "exclamation_per_100_chars",
    "question_per_100_chars",
    "newline_per_100_chars",
    "quote_ratio",
    "url_count",
    "repeated_punctuation_count",
    "all_caps_word_count",
]

LEXICAL_FEATURE_NAMES = [
    f"lexical_identity_{identity_column}"
    for identity_column in OFFICIAL_IDENTITY_COLUMNS
]

FEATURE_COLUMNS = [
    f"fe_{name}" for name in STRUCTURAL_FEATURE_NAMES + LEXICAL_FEATURE_NAMES
]

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
USER_PATTERN = re.compile(r"(?<!\w)@[\w_]{2,}")
HTML_TAG_PATTERN = re.compile(r"</?[a-zA-Z][^>]*>")
WHITESPACE_PATTERN = re.compile(r"\s+")
WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
REPEATED_PUNCT_PATTERN = re.compile(r"[!?.,]{3,}")
CAPITAL_WORD_PATTERN = re.compile(r"\b[A-Z]{3,}\b")

IDENTITY_PATTERNS = {
    "male": re.compile(
        r"\b(?:male|males|man|men|boy|boys|father|fathers|son|sons|husband|husbands)\b"
    ),
    "female": re.compile(
        r"\b(?:female|females|woman|women|girl|girls|mother|mothers|daughter|daughters|wife|wives)\b"
    ),
    "homosexual_gay_or_lesbian": re.compile(
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbt|lgbtq|queer)\b"
    ),
    "christian": re.compile(
        r"\b(?:christian|christians|christianity|catholic|catholics|protestant|protestants)\b"
    ),
    "jewish": re.compile(r"\b(?:jew|jews|jewish|judaism|rabbi|rabbis)\b"),
    "muslim": re.compile(r"\b(?:muslim|muslims|islam|islamic|mosque|mosques)\b"),
    "black": re.compile(
        r"\b(?:black|blacks|african[\s-]?american|african[\s-]?americans)\b"
    ),
    "white": re.compile(r"\b(?:white|whites|caucasian|caucasians)\b"),
    "psychiatric_or_mental_illness": re.compile(
        r"\b(?:mental[\s-]?illness|mental[\s-]?health|mentally[\s-]?ill|psychiatric|depression|depressed|schizophreni\w*|bipolar|autis\w*)\b"
    ),
}


def normalize_comment_text(value):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text).replace("\x00", " ")
    text = HTML_TAG_PATTERN.sub(" ", text)
    text = URL_PATTERN.sub(" [URL] ", text)
    text = USER_PATTERN.sub(" [USER] ", text)
    return WHITESPACE_PATTERN.sub(" ", text).strip()


def clean_text_column(frame):
    frame["comment_text"] = (
        frame["comment_text"].fillna("").astype(str).map(normalize_comment_text)
    )


def build_feature_matrix(text_values):
    feature_width = len(STRUCTURAL_FEATURE_NAMES) + len(LEXICAL_FEATURE_NAMES)
    matrix = np.zeros((len(text_values), feature_width), dtype=np.float32)

    for row_index, text in enumerate(text_values):
        char_count = len(text)
        safe_length = max(char_count, 1)

        alpha_count = sum(character.isalpha() for character in text)
        uppercase_count = sum(character.isupper() for character in text)
        digit_count = sum(character.isdigit() for character in text)
        non_ascii_count = sum(ord(character) > 127 for character in text)

        matrix[row_index, 0] = np.log1p(char_count)
        matrix[row_index, 1] = np.log1p(len(WORD_PATTERN.findall(text)))
        matrix[row_index, 2] = uppercase_count / max(alpha_count, 1)
        matrix[row_index, 3] = digit_count / safe_length
        matrix[row_index, 4] = non_ascii_count / safe_length
        matrix[row_index, 5] = 100.0 * text.count("!") / safe_length
        matrix[row_index, 6] = 100.0 * text.count("?") / safe_length
        matrix[row_index, 7] = 100.0 * text.count("\n") / safe_length
        matrix[row_index, 8] = (text.count('"') + text.count("'")) / safe_length
        matrix[row_index, 9] = len(URL_PATTERN.findall(text))
        matrix[row_index, 10] = len(REPEATED_PUNCT_PATTERN.findall(text))
        matrix[row_index, 11] = len(CAPITAL_WORD_PATTERN.findall(text))

        lower_text = text.lower()
        for identity_offset, identity_column in enumerate(OFFICIAL_IDENTITY_COLUMNS):
            matrix[row_index, len(STRUCTURAL_FEATURE_NAMES) + identity_offset] = float(
                IDENTITY_PATTERNS[identity_column].search(lower_text) is not None
            )

    return matrix


def attach_feature_columns(frame, feature_matrix):
    for column_index, feature_column in enumerate(FEATURE_COLUMNS):
        frame[feature_column] = feature_matrix[:, column_index].astype(
            np.float32,
            copy=False,
        )


train_header = pd.read_csv(INPUT_DIR / "train.csv", nrows=0)
available_train_columns = set(train_header.columns)

train_usecols = [
    column
    for column in (
        ["id", "target", "comment_text"]
        + TOXICITY_AUXILIARY_COLUMNS
        + OFFICIAL_IDENTITY_COLUMNS
    )
    if column in available_train_columns
]

train_source = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=train_usecols,
    low_memory=False,
)

test_source = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_source, test_source)

del train_source
del test_source

for frame in (train_df, valid_df):
    frame["target"] = (
        pd.to_numeric(frame["target"], errors="coerce")
        .fillna(0.0)
        .clip(0.0, 1.0)
        .astype(np.float32)
    )

    for identity_column in OFFICIAL_IDENTITY_COLUMNS:
        if identity_column in frame.columns:
            frame[identity_column] = (
                pd.to_numeric(frame[identity_column], errors="coerce")
                .fillna(0.0)
                .clip(0.0, 1.0)
                .astype(np.float32)
            )

    for auxiliary_column in TOXICITY_AUXILIARY_COLUMNS:
        if auxiliary_column in frame.columns:
            frame[auxiliary_column] = (
                pd.to_numeric(frame[auxiliary_column], errors="coerce")
                .fillna(0.0)
                .clip(0.0, 1.0)
                .astype(np.float32)
            )

for frame in (train_df, valid_df, test_df):
    clean_text_column(frame)

train_feature_matrix = build_feature_matrix(train_df["comment_text"].tolist())

feature_scaler = RobustScaler(quantile_range=(5.0, 95.0))
structural_width = len(STRUCTURAL_FEATURE_NAMES)

train_feature_matrix[:, :structural_width] = feature_scaler.fit_transform(
    train_feature_matrix[:, :structural_width]
).astype(np.float32)

attach_feature_columns(train_df, train_feature_matrix)
del train_feature_matrix

valid_feature_matrix = build_feature_matrix(valid_df["comment_text"].tolist())
valid_feature_matrix[:, :structural_width] = feature_scaler.transform(
    valid_feature_matrix[:, :structural_width]
).astype(np.float32)
attach_feature_columns(valid_df, valid_feature_matrix)
del valid_feature_matrix

test_feature_matrix = build_feature_matrix(test_df["comment_text"].tolist())
test_feature_matrix[:, :structural_width] = feature_scaler.transform(
    test_feature_matrix[:, :structural_width]
).astype(np.float32)
attach_feature_columns(test_df, test_feature_matrix)
del test_feature_matrix

for frame in (train_df, valid_df):
    present_identity_columns = [
        identity_column
        for identity_column in OFFICIAL_IDENTITY_COLUMNS
        if identity_column in frame.columns
    ]

    frame["target_binary"] = (frame["target"].to_numpy(dtype=np.float32) >= 0.5).astype(
        np.int8
    )

    frame["label_identity_any"] = (
        frame[present_identity_columns].to_numpy(dtype=np.float32).max(axis=1) >= 0.5
    ).astype(np.int8)

    frame["label_identity_count"] = (
        (frame[present_identity_columns].to_numpy(dtype=np.float32) >= 0.5)
        .sum(axis=1)
        .astype(np.int8)
    )

train_identity_any = train_df["label_identity_any"].to_numpy(dtype=bool)
train_toxic_binary = train_df["target_binary"].to_numpy(dtype=bool)

sample_weight = np.ones(len(train_df), dtype=np.float32)
sample_weight += train_identity_any.astype(np.float32)
sample_weight += ((~train_identity_any) & train_toxic_binary).astype(np.float32)
sample_weight += 4.0 * (train_identity_any & (~train_toxic_binary)).astype(np.float32)

target_consensus = np.abs(train_df["target"].to_numpy(dtype=np.float32) - 0.5) * 2.0

weighted_consensus = sample_weight * (0.75 + 0.25 * target_consensus)
train_df["train_sample_weight"] = (
    weighted_consensus / weighted_consensus.mean()
).astype(np.float32)

lexical_identity_feature_columns = [
    f"fe_lexical_identity_{identity_column}"
    for identity_column in OFFICIAL_IDENTITY_COLUMNS
]

for frame in (train_df, valid_df, test_df):
    frame["lexical_identity_any"] = (
        frame[lexical_identity_feature_columns].to_numpy(dtype=np.float32).max(axis=1)
        > 0.0
    ).astype(np.int8)

joblib.dump(
    {
        "feature_scaler": feature_scaler,
        "structural_feature_names": STRUCTURAL_FEATURE_NAMES,
        "lexical_feature_names": LEXICAL_FEATURE_NAMES,
        "feature_columns": FEATURE_COLUMNS,
        "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    },
    WORKING_DIR / "toxicity_feature_transform.joblib",
)

with open(
    WORKING_DIR / "toxicity_feature_schema.json",
    "w",
    encoding="utf-8",
) as schema_file:
    json.dump(
        {
            "text_column": "comment_text",
            "target_column": "target",
            "feature_columns": FEATURE_COLUMNS,
            "sample_weight_column": "train_sample_weight",
            "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
            "validation_split_source": "CandidateSession.split",
        },
        schema_file,
        indent=2,
    )

model_id = "answerdotai/ModernBERT-large"

# Disable both global Dynamo compilation and ModernBERT's optional compiled
# reference implementation before constructing the pretrained model.
if hasattr(torch, "_dynamo"):
    torch._dynamo.config.disable = True

model_config = AutoConfig.from_pretrained(model_id)
if hasattr(model_config, "reference_compile"):
    model_config.reference_compile = False

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    config=model_config,
)

STRUCTURAL_FEATURE_DIM = len(STRUCTURAL_FEATURE_NAMES)


class ContextualToxicityRanker(nn.Module):
    def __init__(self, text_model, structural_feature_dim=STRUCTURAL_FEATURE_DIM):
        super().__init__()
        self.text_model = text_model
        self.structural_feature_dim = structural_feature_dim

        self.style_head = nn.Sequential(
            nn.LayerNorm(structural_feature_dim),
            nn.Linear(structural_feature_dim, 48),
            nn.GELU(),
            nn.Dropout(0.15),
            nn.Linear(48, 1),
        )

        nn.init.zeros_(self.style_head[-1].weight)
        nn.init.zeros_(self.style_head[-1].bias)

        if hasattr(self.text_model, "gradient_checkpointing_enable"):
            self.text_model.gradient_checkpointing_enable()

        if hasattr(self.text_model.config, "use_cache"):
            self.text_model.config.use_cache = False

    def forward(self, input_ids, attention_mask=None, style_features=None, **kwargs):
        kwargs.pop("token_type_ids", None)

        outputs = self.text_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            **kwargs,
        )

        raw_logits = outputs.logits

        if raw_logits.ndim == 1:
            text_logit = raw_logits
        elif raw_logits.shape[-1] == 1:
            text_logit = raw_logits[:, 0]
        else:
            text_logit = raw_logits[:, 1] - raw_logits[:, 0]

        if style_features is None:
            return text_logit

        style_features = style_features[:, : self.structural_feature_dim].float()
        return text_logit + self.style_head(style_features).squeeze(-1)


class BiasAUCSurrogateLoss(nn.Module):
    def __init__(
        self,
        rank_weight=0.30,
        rank_temperature=0.35,
        tail_temperature=8.0,
    ):
        super().__init__()
        self.rank_weight = rank_weight
        self.rank_temperature = rank_temperature
        self.tail_temperature = tail_temperature

    def _pairwise_rank_loss(self, positive_logits, negative_logits):
        if positive_logits.numel() == 0 or negative_logits.numel() == 0:
            return None

        margins = (
            negative_logits[:, None] - positive_logits[None, :]
        ) / self.rank_temperature

        return F.softplus(margins).mean()

    def forward(self, logits, targets, identities=None, sample_weights=None):
        targets = targets.float().view(-1)
        logits = logits.view(-1)

        pointwise_loss = F.binary_cross_entropy_with_logits(
            logits,
            targets,
            reduction="none",
        )

        if sample_weights is None:
            classification_loss = pointwise_loss.mean()
        else:
            sample_weights = sample_weights.float().view(-1).clamp_min(0.0)
            classification_loss = (
                pointwise_loss * sample_weights
            ).sum() / sample_weights.sum().clamp_min(1e-6)

        if identities is None:
            return classification_loss

        identities = identities.float()

        if identities.ndim != 2 or identities.shape[0] != logits.shape[0]:
            raise ValueError(
                "identities must have shape [batch_size, number_of_identity_groups]."
            )

        toxic = targets >= 0.5
        rank_losses = []

        for identity_index in range(identities.shape[1]):
            subgroup = identities[:, identity_index] >= 0.5
            background = ~subgroup

            subgroup_auc_loss = self._pairwise_rank_loss(
                logits[subgroup & toxic],
                logits[subgroup & (~toxic)],
            )
            if subgroup_auc_loss is not None:
                rank_losses.append(subgroup_auc_loss)

            bpsn_auc_loss = self._pairwise_rank_loss(
                logits[background & toxic],
                logits[subgroup & (~toxic)],
            )
            if bpsn_auc_loss is not None:
                rank_losses.append(bpsn_auc_loss)

            bnsp_auc_loss = self._pairwise_rank_loss(
                logits[subgroup & toxic],
                logits[background & (~toxic)],
            )
            if bnsp_auc_loss is not None:
                rank_losses.append(bnsp_auc_loss)

        if not rank_losses:
            return classification_loss

        rank_losses = torch.stack(rank_losses)

        tail_risk_rank_loss = (
            torch.logsumexp(rank_losses * self.tail_temperature, dim=0)
            / self.tail_temperature
        )

        return classification_loss + self.rank_weight * tail_risk_rank_loss


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ContextualToxicityRanker(model).to(device)
criterion = BiasAUCSurrogateLoss()

backbone_parameters = list(model.text_model.parameters())
style_parameters = list(model.style_head.parameters())

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": style_parameters,
            "lr": 4.0e-4,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_enabled = device.type == "cuda"
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 16 if device.type == "cuda" else 4
INFERENCE_BATCH_SIZE = 32 if device.type == "cuda" else 8
NUM_WORKERS = max(2, min(4, (os.cpu_count() or 2) // 2))
PIN_MEMORY = device.type == "cuda"

identity_columns_for_loss = [
    column for column in OFFICIAL_IDENTITY_COLUMNS if column in train_df.columns
]

style_feature_columns = FEATURE_COLUMNS[: model.structural_feature_dim]

train_texts = train_df["comment_text"].fillna("").astype(str).to_numpy()
valid_texts = valid_df["comment_text"].fillna("").astype(str).to_numpy()
test_texts = test_df["comment_text"].fillna("").astype(str).to_numpy()

train_styles = np.ascontiguousarray(
    train_df[style_feature_columns].to_numpy(dtype=np.float32)
)
valid_styles = np.ascontiguousarray(
    valid_df[style_feature_columns].to_numpy(dtype=np.float32)
)
test_styles = np.ascontiguousarray(
    test_df[style_feature_columns].to_numpy(dtype=np.float32)
)

train_targets = np.ascontiguousarray(
    train_df["target"].to_numpy(dtype=np.float32).clip(0.0, 1.0)
)

train_identities = np.ascontiguousarray(
    train_df[identity_columns_for_loss].to_numpy(dtype=np.float32).clip(0.0, 1.0)
)

train_sample_weights = np.ascontiguousarray(
    train_df["train_sample_weight"].to_numpy(dtype=np.float32)
)

if len(train_texts) == 0:
    raise RuntimeError("The runtime training partition is empty.")

if len(valid_texts) == 0:
    raise RuntimeError("The runtime validation partition is empty.")

if len(test_texts) == 0:
    raise RuntimeError("The runtime test partition is empty.")


class ToxicityTrainingDataset(Dataset):
    def __init__(self, texts, styles, targets, identities, weights):
        self.texts = texts
        self.styles = styles
        self.targets = targets
        self.identities = identities
        self.weights = weights

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.styles[index],
            self.targets[index],
            self.identities[index],
            self.weights[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts, styles, positions):
        self.texts = texts
        self.styles = styles
        self.positions = np.asarray(positions, dtype=np.int64)

    def __len__(self):
        return len(self.positions)

    def __getitem__(self, index):
        position = self.positions[index]
        return self.texts[position], self.styles[position]


def collate_training(batch):
    texts, styles, targets, identities, weights = zip(*batch)

    encoded = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )

    encoded["style_features"] = torch.from_numpy(
        np.ascontiguousarray(np.stack(styles).astype(np.float32, copy=False))
    )

    encoded["targets"] = torch.tensor(targets, dtype=torch.float32)

    encoded["identities"] = torch.from_numpy(
        np.ascontiguousarray(np.stack(identities).astype(np.float32, copy=False))
    )

    encoded["sample_weights"] = torch.tensor(weights, dtype=torch.float32)
    return encoded


def collate_inference(batch):
    texts, styles = zip(*batch)

    encoded = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )

    encoded["style_features"] = torch.from_numpy(
        np.ascontiguousarray(np.stack(styles).astype(np.float32, copy=False))
    )

    return encoded


def predict_positions(texts, styles, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    if positions.min() < 0 or positions.max() >= len(texts):
        raise IndexError(
            "Runtime requested prediction positions outside the partition."
        )

    inference_dataset = ToxicityInferenceDataset(texts, styles, positions)

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=collate_inference,
    )

    previous_mode = model.training
    model.eval()
    outputs = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                model_inputs = {
                    key: value.to(device, non_blocking=PIN_MEMORY)
                    for key, value in batch.items()
                }

                with torch.cuda.amp.autocast(enabled=amp_enabled):
                    logits = model(**model_inputs)

                outputs.append(torch.sigmoid(logits.float()).detach().cpu().numpy())
    finally:
        model.train(previous_mode)

    return np.concatenate(outputs).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_positions(valid_texts, valid_styles, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_texts, test_styles, positional_indices)


checkpoint_state = {"optimizer_steps": 0}


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state": model.state_dict(),
            "optimizer_steps": int(checkpoint_state["optimizer_steps"]),
        },
        checkpoint_directory / "model_state.pt",
    )

    model.text_model.config.to_json_file(
        str(checkpoint_directory / "backbone_config.json")
    )

    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")

    with open(
        checkpoint_directory / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(
            {
                "max_length": MAX_LENGTH,
                "style_feature_columns": style_feature_columns,
                "identity_columns_for_loss": identity_columns_for_loss,
                "optimizer_steps": int(checkpoint_state["optimizer_steps"]),
            },
            handle,
            indent=2,
        )

    for artifact_name in (
        "toxicity_feature_transform.joblib",
        "toxicity_feature_schema.json",
    ):
        source = WORKING_DIR / artifact_name
        if source.exists():
            shutil.copy2(source, checkpoint_directory / artifact_name)


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)

    payload = torch.load(
        checkpoint_directory / "model_state.pt",
        map_location=device,
    )

    model.load_state_dict(payload["model_state"], strict=True)
    model.to(device)

    checkpoint_state["optimizer_steps"] = int(
        payload.get("optimizer_steps", checkpoint_state["optimizer_steps"])
    )


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

sampling_weights = np.sqrt(np.clip(train_sample_weights, a_min=0.25, a_max=8.0)).astype(
    np.float64
)

train_sampler = WeightedRandomSampler(
    weights=torch.as_tensor(sampling_weights, dtype=torch.double),
    num_samples=len(train_texts),
    replacement=True,
)

training_dataset = ToxicityTrainingDataset(
    train_texts,
    train_styles,
    train_targets,
    train_identities,
    train_sample_weights,
)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    sampler=train_sampler,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=NUM_WORKERS > 0,
    prefetch_factor=2,
    collate_fn=collate_training,
)

session.start_training(train_df["id"].astype(str).tolist())

stop_training = False
epoch_index = 0
max_epochs = 100

while not stop_training and epoch_index < max_epochs:
    epoch_index += 1
    model.train()

    epoch_loss_sum = 0.0
    epoch_updates = 0

    for batch in training_loader:
        targets = batch.pop("targets").to(device, non_blocking=PIN_MEMORY)
        identities = batch.pop("identities").to(device, non_blocking=PIN_MEMORY)
        sample_weights = batch.pop("sample_weights").to(
            device,
            non_blocking=PIN_MEMORY,
        )

        model_inputs = {
            key: value.to(device, non_blocking=PIN_MEMORY)
            for key, value in batch.items()
        }

        optimizer.zero_grad(set_to_none=True)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            logits = model(**model_inputs)
            loss = criterion(
                logits=logits,
                targets=targets,
                identities=identities,
                sample_weights=sample_weights,
            )

        if not torch.isfinite(loss):
            raise FloatingPointError("Encountered a non-finite training loss.")

        grad_scaler.scale(loss).backward()
        grad_scaler.unscale_(optimizer)

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        grad_scaler.step(optimizer)
        grad_scaler.update()

        checkpoint_state["optimizer_steps"] += 1
        epoch_updates += 1
        epoch_loss_sum += float(loss.detach().cpu())

        stop_training = session.step()
        if stop_training:
            break

    mean_epoch_loss = epoch_loss_sum / max(epoch_updates, 1)

    print(f"epoch={epoch_index} updates={epoch_updates} " f"loss={mean_epoch_loss:.6f}")

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
