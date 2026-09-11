import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import re
import html
import json
import random
import pickle
import shutil
import warnings

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession

warnings.filterwarnings("ignore", category=FutureWarning)

SEED = 2026
INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

session = CandidateSession.from_env()

official_identity_columns = [
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

all_identity_columns = [
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

toxicity_subtype_columns = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

optional_training_columns = [
    "toxicity_annotator_count",
    "identity_annotator_count",
]

train_header = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    nrows=0,
).columns.tolist()

train_usecols = [
    column
    for column in (
        ["id", "target", "comment_text"]
        + all_identity_columns
        + toxicity_subtype_columns
        + optional_training_columns
    )
    if column in train_header
]

raw_train_df = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    usecols=train_usecols,
    low_memory=False,
)

raw_test_df = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

del raw_train_df
del raw_test_df

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()]+")
USER_PATTERN = re.compile(r"(?<!\w)@[a-zA-Z0-9_]{1,64}")
HTML_TAG_PATTERN = re.compile(r"<[^>\n]{1,200}>")
ZERO_WIDTH_PATTERN = re.compile(r"[\u200b-\u200d\u2060\ufeff]")
CONTROL_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
WHITESPACE_PATTERN = re.compile(r"\s+")
REPEATED_PUNCT_PATTERN = re.compile(r"([!?.,])\1{2,}")
LETTER_PATTERN = re.compile(r"[A-Za-z]")
UPPER_PATTERN = re.compile(r"[A-Z]")
DIGIT_PATTERN = re.compile(r"\d")
NON_ASCII_PATTERN = re.compile(r"[^\x00-\x7F]")


def engineer_text_features(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()

    raw_text = frame["comment_text"].fillna("").astype(str)
    raw_length = raw_text.str.len().clip(lower=0)

    letter_count = raw_text.str.count(LETTER_PATTERN)
    uppercase_count = raw_text.str.count(UPPER_PATTERN)
    url_count = raw_text.str.count(URL_PATTERN)
    mention_count = raw_text.str.count(USER_PATTERN)
    newline_count = raw_text.str.count(r"[\r\n]+")
    repeated_punctuation_count = raw_text.str.count(REPEATED_PUNCT_PATTERN)
    digit_count = raw_text.str.count(DIGIT_PATTERN)
    non_ascii_count = raw_text.str.count(NON_ASCII_PATTERN)
    question_count = raw_text.str.count(r"\?")
    exclamation_count = raw_text.str.count(r"!")

    canonical_text = raw_text.str.normalize("NFKC")

    entity_mask = canonical_text.str.contains(
        r"&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z]+);",
        regex=True,
        na=False,
    )
    if entity_mask.any():
        canonical_text.loc[entity_mask] = canonical_text.loc[entity_mask].map(
            html.unescape
        )

    canonical_text = canonical_text.str.replace(
        ZERO_WIDTH_PATTERN,
        "",
        regex=True,
    )
    canonical_text = canonical_text.str.replace(
        CONTROL_PATTERN,
        " ",
        regex=True,
    )
    canonical_text = canonical_text.str.replace(
        HTML_TAG_PATTERN,
        " ",
        regex=True,
    )
    canonical_text = canonical_text.str.replace(
        URL_PATTERN,
        " urltoken ",
        regex=True,
    )
    canonical_text = canonical_text.str.replace(
        USER_PATTERN,
        " usertoken ",
        regex=True,
    )
    canonical_text = canonical_text.str.replace(
        WHITESPACE_PATTERN,
        " ",
        regex=True,
    ).str.strip()

    surface_text = canonical_text.copy()
    canonical_text = canonical_text.str.lower()

    word_count = canonical_text.str.count(r"\S+").clip(lower=0)
    uppercase_ratio = (uppercase_count / letter_count.clip(lower=1)).astype(np.float32)
    digit_ratio = (digit_count / raw_length.clip(lower=1)).astype(np.float32)
    non_ascii_ratio = (non_ascii_count / raw_length.clip(lower=1)).astype(np.float32)

    style_tokens = np.full(len(frame), "", dtype=object)

    all_caps_mask = (letter_count >= 8) & (uppercase_ratio >= 0.55)
    emphasis_mask = (exclamation_count >= 2) | (repeated_punctuation_count >= 1)
    question_mask = question_count >= 2
    long_mask = word_count >= 180
    link_mask = url_count >= 1
    reply_mask = mention_count >= 1

    style_tokens[all_caps_mask.to_numpy()] += " style_allcaps"
    style_tokens[emphasis_mask.to_numpy()] += " style_emphasis"
    style_tokens[question_mask.to_numpy()] += " style_questions"
    style_tokens[long_mask.to_numpy()] += " style_longcomment"
    style_tokens[link_mask.to_numpy()] += " style_link"
    style_tokens[reply_mask.to_numpy()] += " style_reply"

    frame["surface_text"] = surface_text
    frame["canonical_text"] = canonical_text
    frame["model_text"] = (
        pd.Series(style_tokens, index=frame.index, dtype="object")
        .str.cat(canonical_text, sep=" ")
        .str.strip()
    )

    frame["f_log_char_length"] = np.log1p(raw_length).astype(np.float32)
    frame["f_log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["f_log_newline_count"] = np.log1p(newline_count).astype(np.float32)
    frame["f_log_url_count"] = np.log1p(url_count).astype(np.float32)
    frame["f_log_mention_count"] = np.log1p(mention_count).astype(np.float32)
    frame["f_uppercase_ratio"] = uppercase_ratio
    frame["f_log_repeated_punctuation"] = np.log1p(repeated_punctuation_count).astype(
        np.float32
    )
    frame["f_digit_ratio"] = digit_ratio
    frame["f_non_ascii_ratio"] = non_ascii_ratio

    return frame


train_df = engineer_text_features(train_df)
valid_df = engineer_text_features(valid_df)
test_df = engineer_text_features(test_df)

numeric_feature_columns = [
    "f_log_char_length",
    "f_log_word_count",
    "f_log_newline_count",
    "f_log_url_count",
    "f_log_mention_count",
    "f_uppercase_ratio",
    "f_log_repeated_punctuation",
    "f_digit_ratio",
    "f_non_ascii_ratio",
]

numeric_scaler = StandardScaler()

train_df[numeric_feature_columns] = numeric_scaler.fit_transform(
    train_df[numeric_feature_columns].astype(np.float32)
).astype(np.float32)

valid_df[numeric_feature_columns] = numeric_scaler.transform(
    valid_df[numeric_feature_columns].astype(np.float32)
).astype(np.float32)

test_df[numeric_feature_columns] = numeric_scaler.transform(
    test_df[numeric_feature_columns].astype(np.float32)
).astype(np.float32)

for frame in (train_df, valid_df):
    frame["target"] = (
        pd.to_numeric(frame["target"], errors="coerce")
        .fillna(0.0)
        .clip(0.0, 1.0)
        .astype(np.float32)
    )
    frame["target_binary"] = (frame["target"] >= 0.5).astype(np.int8)
    frame["target_confidence"] = (2.0 * (frame["target"] - 0.5).abs()).astype(
        np.float32
    )

    available_identities = [
        column for column in all_identity_columns if column in frame.columns
    ]

    identity_values = (
        frame[available_identities]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .clip(0.0, 1.0)
        .astype(np.float32)
    )

    frame.loc[:, available_identities] = identity_values
    frame["identity_any"] = (identity_values.max(axis=1) >= 0.5).astype(np.int8)
    frame["identity_count"] = (identity_values >= 0.5).sum(axis=1).astype(np.int8)

    for subtype_column in toxicity_subtype_columns:
        if subtype_column not in frame.columns:
            frame[subtype_column] = 0.0
        frame[subtype_column] = (
            pd.to_numeric(frame[subtype_column], errors="coerce")
            .fillna(0.0)
            .clip(0.0, 1.0)
            .astype(np.float32)
        )

    for identity_column in official_identity_columns:
        if identity_column not in frame.columns:
            frame[identity_column] = 0.0
        frame[identity_column] = (
            pd.to_numeric(frame[identity_column], errors="coerce")
            .fillna(0.0)
            .clip(0.0, 1.0)
            .astype(np.float32)
        )

test_df["identity_any"] = np.nan
test_df["identity_count"] = np.nan

processing_state = {
    "seed": SEED,
    "text_column": "model_text",
    "surface_text_column": "surface_text",
    "canonical_text_column": "canonical_text",
    "numeric_feature_columns": numeric_feature_columns,
    "official_identity_columns": official_identity_columns,
    "all_identity_columns": all_identity_columns,
    "toxicity_subtype_columns": toxicity_subtype_columns,
    "numeric_scaler": numeric_scaler,
    "normalization_version": "nfkc_html_url_user_structural_v1",
}

with open(
    os.path.join(WORKING_DIR, "text_processing_state.pkl"),
    "wb",
) as state_file:
    pickle.dump(
        processing_state,
        state_file,
        protocol=pickle.HIGHEST_PROTOCOL,
    )

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

text_column = processing_state["text_column"]

for frame in (train_df, valid_df, test_df):
    frame[text_column] = frame[text_column].fillna("").astype(str)

for feature_column in numeric_feature_columns:
    for frame in (train_df, valid_df, test_df):
        if feature_column not in frame.columns:
            frame[feature_column] = 0.0


class DualWindowToxicityDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, include_labels: bool):
        self.texts = frame[text_column].astype(str).to_numpy()
        self.numeric = frame[numeric_feature_columns].to_numpy(dtype=np.float32)
        self.include_labels = include_labels

        if include_labels:
            self.target = frame["target"].to_numpy(dtype=np.float32)
            self.identities = (
                frame[official_identity_columns].fillna(0.0).to_numpy(dtype=np.float32)
            )
            self.subtypes = (
                frame[toxicity_subtype_columns].fillna(0.0).to_numpy(dtype=np.float32)
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = (self.texts[index], self.numeric[index])

        if self.include_labels:
            item += (
                self.target[index],
                self.identities[index],
                self.subtypes[index],
            )

        return item


def collate_dual_window(batch):
    texts = [row[0] for row in batch]

    numeric = torch.as_tensor(
        np.stack([row[1] for row in batch]),
        dtype=torch.float32,
    )

    token_lists = tokenizer(
        texts,
        add_special_tokens=False,
        truncation=False,
        padding=False,
    )["input_ids"]

    body_length = 190
    first_windows = []
    last_windows = []

    for token_ids in token_lists:
        if len(token_ids) <= body_length:
            first_window = token_ids
            last_window = token_ids
        else:
            first_window = token_ids[:body_length]
            last_window = token_ids[-body_length:]

        first_windows.append(tokenizer.build_inputs_with_special_tokens(first_window))
        last_windows.append(tokenizer.build_inputs_with_special_tokens(last_window))

    padded = tokenizer.pad(
        {"input_ids": first_windows + last_windows},
        padding=True,
        return_tensors="pt",
    )

    batch_size = len(batch)

    output = {
        "input_ids": padded["input_ids"].view(2, batch_size, -1).transpose(0, 1),
        "attention_mask": padded["attention_mask"].view(2, batch_size, -1).transpose(0, 1),
        "numeric": numeric,
    }

    if len(batch[0]) == 5:
        output["target"] = torch.as_tensor(
            np.asarray([row[2] for row in batch], dtype=np.float32)
        )
        output["identities"] = torch.as_tensor(
            np.stack([row[3] for row in batch]).astype(np.float32)
        )
        output["subtypes"] = torch.as_tensor(
            np.stack([row[4] for row in batch]).astype(np.float32)
        )

    return output


class DualWindowModernBERT(nn.Module):
    def __init__(
        self,
        pretrained_classifier,
        numeric_dim: int,
        subtype_dim: int,
    ):
        super().__init__()

        self.encoder = pretrained_classifier.model
        hidden_size = pretrained_classifier.config.hidden_size
        del pretrained_classifier

        self.window_norm = nn.LayerNorm(hidden_size)
        self.window_gate = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 4),
            nn.GELU(),
            nn.Linear(hidden_size // 4, 1),
        )

        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden_size + numeric_dim),
            nn.Linear(hidden_size + numeric_dim, hidden_size),
            nn.GELU(),
            nn.Dropout(0.18),
        )

        self.toxicity_head = nn.Linear(hidden_size, 1)
        self.subtype_head = nn.Linear(hidden_size, subtype_dim)

    def forward(self, input_ids, attention_mask, numeric):
        batch_size, windows, sequence_length = input_ids.shape

        flat_ids = input_ids.reshape(batch_size * windows, sequence_length)
        flat_mask = attention_mask.reshape(batch_size * windows, sequence_length)

        encoded = self.encoder(
            input_ids=flat_ids,
            attention_mask=flat_mask,
            return_dict=True,
        ).last_hidden_state[:, 0]

        encoded = self.window_norm(encoded).view(batch_size, windows, -1)

        window_valid = attention_mask.sum(dim=-1).gt(2)
        gate_logits = self.window_gate(encoded).squeeze(-1)
        gate_logits = gate_logits.masked_fill(~window_valid, -1e4)
        gate_weights = torch.softmax(gate_logits, dim=1)

        pooled = torch.sum(
            encoded * gate_weights.unsqueeze(-1),
            dim=1,
        )

        fused = self.fusion(torch.cat([pooled, numeric], dim=1))

        return {
            "toxicity_logits": self.toxicity_head(fused).squeeze(-1),
            "subtype_logits": self.subtype_head(fused),
        }


class OfficialSliceAwareLoss(nn.Module):
    def __init__(self, subtype_weight=0.14):
        super().__init__()
        self.subtype_weight = subtype_weight

    def forward(self, outputs, target, identities, subtypes):
        target = target.clamp(0.0, 1.0)
        toxicity_logits = outputs["toxicity_logits"]

        identity_present = identities.ge(0.5).any(dim=1)
        toxic = target.ge(0.5)

        benign_identity = identity_present & (~toxic)
        toxic_identity = identity_present & toxic
        toxic_background = (~identity_present) & toxic

        sample_weight = torch.ones_like(target)
        sample_weight = sample_weight + 1.10 * benign_identity.float()
        sample_weight = sample_weight + 0.45 * toxic_identity.float()
        sample_weight = sample_weight + 0.25 * toxic_background.float()

        confidence = 0.70 + 0.30 * (2.0 * (target - 0.5).abs())
        sample_weight = sample_weight * confidence

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            target,
            reduction="none",
        )
        toxicity_loss = (
            toxicity_loss * sample_weight
        ).sum() / sample_weight.sum().clamp_min(1.0)

        subtype_loss = F.binary_cross_entropy_with_logits(
            outputs["subtype_logits"],
            subtypes.clamp(0.0, 1.0),
            reduction="none",
        ).mean(dim=1)

        subtype_loss = (
            subtype_loss * sample_weight
        ).sum() / sample_weight.sum().clamp_min(1.0)

        return toxicity_loss + self.subtype_weight * subtype_loss


model = DualWindowModernBERT(
    pretrained_classifier=model,
    numeric_dim=len(numeric_feature_columns),
    subtype_dim=len(toxicity_subtype_columns),
).to(device)

criterion = OfficialSliceAwareLoss(subtype_weight=0.14)

backbone_parameters = []
head_parameters = []

for name, parameter in model.named_parameters():
    if name.startswith("encoder."):
        backbone_parameters.append(parameter)
    else:
        head_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": 1.35e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_parameters,
            "lr": 7.5e-5,
            "weight_decay": 0.02,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

warmup_updates = 100
planned_updates = 2600


def lr_scale(step):
    if step < warmup_updates:
        return max(0.05, float(step + 1) / float(warmup_updates))

    progress = min(
        1.0,
        float(step - warmup_updates) / float(max(1, planned_updates - warmup_updates)),
    )

    return max(0.12, 0.5 * (1.0 + np.cos(np.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=lr_scale)
scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)

train_dataset = DualWindowToxicityDataset(
    train_df,
    include_labels=True,
)

train_target = train_df["target"].to_numpy(dtype=np.float32)
train_identity = (
    train_df[official_identity_columns]
    .fillna(0.0)
    .to_numpy(dtype=np.float32)
    .max(axis=1)
    >= 0.5
)
train_toxic = train_target >= 0.5

sampling_weights = np.full(
    len(train_df),
    0.28,
    dtype=np.float64,
)
sampling_weights[(~train_identity) & train_toxic] = 1.10
sampling_weights[train_identity & (~train_toxic)] = 1.75
sampling_weights[train_identity & train_toxic] = 1.50
sampling_weights = sampling_weights / sampling_weights.sum()

sampler = WeightedRandomSampler(
    weights=torch.as_tensor(sampling_weights, dtype=torch.double),
    num_samples=len(train_dataset),
    replacement=True,
)

batch_size = 12 if amp_enabled else 2

train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    sampler=sampler,
    num_workers=2,
    pin_memory=amp_enabled,
    persistent_workers=True,
    collate_fn=collate_dual_window,
    drop_last=True,
)


def move_batch_to_device(batch):
    return {
        name: value.to(device, non_blocking=amp_enabled)
        for name, value in batch.items()
    }


@torch.inference_mode()
def predict_frame(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    subset = frame.iloc[positional_indices]
    dataset = DualWindowToxicityDataset(subset, include_labels=False)

    loader = DataLoader(
        dataset,
        batch_size=20 if amp_enabled else 2,
        shuffle=False,
        num_workers=2,
        pin_memory=amp_enabled,
        persistent_workers=True,
        collate_fn=collate_dual_window,
    )

    was_training = model.training
    model.eval()

    prediction_batches = []

    for batch in loader:
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric=batch["numeric"],
            )
            probabilities = torch.sigmoid(outputs["toxicity_logits"])

        prediction_batches.append(probabilities.float().cpu().numpy())

    if was_training:
        model.train()

    return np.concatenate(prediction_batches).astype(np.float64)


def predict_validation(positional_indices):
    return predict_frame(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame(test_df, positional_indices)


checkpoint_state_name = "model_state.pt"


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    state_path = os.path.join(directory, checkpoint_state_name)
    temporary_state_path = state_path + ".tmp"

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "architecture": type(model).__name__,
        },
        temporary_state_path,
    )

    os.replace(temporary_state_path, state_path)

    tokenizer.save_pretrained(os.path.join(directory, "tokenizer"))

    encoder_config = getattr(
        getattr(model, "encoder", model),
        "config",
        None,
    )

    model_metadata = {
        "architecture": type(model).__name__,
        "text_column": processing_state.get("text_column"),
        "numeric_feature_columns": processing_state.get(
            "numeric_feature_columns",
            [],
        ),
        "official_identity_columns": processing_state.get(
            "official_identity_columns",
            [],
        ),
        "toxicity_subtype_columns": processing_state.get(
            "toxicity_subtype_columns",
            [],
        ),
        "encoder_config": (
            encoder_config.to_dict() if encoder_config is not None else None
        ),
    }

    with open(
        os.path.join(directory, "inference_metadata.json"),
        "w",
    ) as metadata_file:
        json.dump(model_metadata, metadata_file)

    processing_source = os.path.join(
        WORKING_DIR,
        "text_processing_state.pkl",
    )
    processing_destination = os.path.join(
        directory,
        "text_processing_state.pkl",
    )

    if os.path.exists(processing_source):
        shutil.copy2(processing_source, processing_destination)
    else:
        with open(processing_destination, "wb") as processing_file:
            pickle.dump(
                processing_state,
                processing_file,
                protocol=pickle.HIGHEST_PROTOCOL,
            )


def load_checkpoint(directory):
    checkpoint = torch.load(
        os.path.join(directory, checkpoint_state_name),
        map_location=device,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)

accumulation_steps = 2
optimizer_updates = 0
stop_training = False
max_epochs = 100

for epoch in range(max_epochs):
    model.train()

    epoch_loss_sum = 0.0
    epoch_batches = 0

    for batch_index, batch in enumerate(train_loader):
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric=batch["numeric"],
            )

            loss = criterion(
                outputs=outputs,
                target=batch["target"],
                identities=batch["identities"],
                subtypes=batch["subtypes"],
            )

            scaled_loss = loss / accumulation_steps

        scaler.scale(scaled_loss).backward()

        epoch_loss_sum += float(loss.detach().cpu())
        epoch_batches += 1

        if (batch_index + 1) % accumulation_steps != 0:
            continue

        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0,
        )

        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

        optimizer_updates += 1
        stop_training = session.step()

        if stop_training:
            break

    mean_loss = epoch_loss_sum / max(epoch_batches, 1)

    print(
        f"Epoch {epoch + 1}: loss={mean_loss:.6f}, "
        f"optimizer_updates={optimizer_updates}"
    )

    if stop_training:
        break

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")