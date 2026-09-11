import os
import re
import html
import json
import shutil
import random
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

os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2026
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")
WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

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

TOXICITY_AUXILIARY_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

TRAIN_COLUMNS = list(
    dict.fromkeys(
        ["id", "target", "comment_text"] + TOXICITY_AUXILIARY_COLUMNS + IDENTITY_COLUMNS
    )
)

URL_PATTERN = re.compile(
    r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]{}]+|(?<!\w)[\w.+-]+@[\w-]+(?:\.[\w-]+)+"
)
EMAIL_PATTERN = re.compile(r"(?i)(?<!\w)[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
WHITESPACE_PATTERN = re.compile(r"\s+")
REPEATED_PUNCT_PATTERN = re.compile(r"([!?.,;:])\1{2,}")
WORD_PATTERN = re.compile(r"\b[\w']+\b")
ALL_CAPS_TOKEN_PATTERN = re.compile(r"\b[A-Z]{3,}\b")
FIRST_PERSON_PATTERN = re.compile(
    r"\b(?:i|i'm|i’ve|i am|my|mine|we|we're|our|ours)\b", re.I
)
NEGATION_PATTERN = re.compile(
    r"\b(?:not|never|no|none|nothing|neither|nor|isn't|aren't|wasn't|weren't|"
    r"don't|doesn't|didn't|can't|cannot|couldn't|shouldn't|wouldn't|won't)\b",
    re.I,
)
QUOTE_PATTERN = re.compile(r"""["'“”‘’]""")


def normalize_comment(value):
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = text.replace("\u200b", "").replace("\ufeff", "").replace("\u00ad", "")
    text = EMAIL_PATTERN.sub(" <EMAIL> ", text)
    text = URL_PATTERN.sub(" <URL> ", text)
    text = REPEATED_PUNCT_PATTERN.sub(r"\1\1", text)
    return WHITESPACE_PATTERN.sub(" ", text).strip()


def make_head_tail_text(text, max_chars=6000, head_chars=3800):
    if len(text) <= max_chars:
        return text
    tail_chars = max_chars - head_chars
    return text[:head_chars].rstrip() + " [SEP] " + text[-tail_chars:].lstrip()


def add_text_features(frame, duplicate_lookup):
    processed = frame.copy()

    processed["clean_text"] = processed["comment_text"].map(normalize_comment)
    processed["model_text"] = processed["clean_text"].map(make_head_tail_text)

    text = processed["clean_text"]
    lower_text = text.str.lower()

    char_count = text.str.len().astype(np.float32)
    alpha_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = text.str.count(r"[A-Z]").astype(np.float32)
    word_count = text.str.count(r"\S+").astype(np.float32)
    unique_word_count = lower_text.map(
        lambda value: len(set(WORD_PATTERN.findall(value)))
    ).astype(np.float32)

    processed["feature_log_char_count"] = np.log1p(char_count).astype(np.float32)
    processed["feature_log_word_count"] = np.log1p(word_count).astype(np.float32)
    processed["feature_log_unique_word_count"] = np.log1p(unique_word_count).astype(
        np.float32
    )
    processed["feature_unique_word_ratio"] = (
        unique_word_count / np.maximum(word_count, 1.0)
    ).astype(np.float32)
    processed["feature_uppercase_ratio"] = (
        uppercase_count / np.maximum(alpha_count, 1.0)
    ).astype(np.float32)
    processed["feature_exclamation_count"] = np.minimum(
        text.str.count("!").astype(np.float32), 20.0
    )
    processed["feature_question_count"] = np.minimum(
        text.str.count(r"\?").astype(np.float32), 20.0
    )
    processed["feature_sentence_count"] = np.minimum(
        text.str.count(r"[.!?]+").astype(np.float32), 100.0
    )
    processed["feature_newline_count"] = np.minimum(
        processed["comment_text"]
        .fillna("")
        .astype(str)
        .str.count(r"\n")
        .astype(np.float32),
        20.0,
    )
    processed["feature_digit_ratio"] = (
        text.str.count(r"\d").astype(np.float32) / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    processed["feature_quote_count"] = np.minimum(
        text.map(lambda value: len(QUOTE_PATTERN.findall(value))).astype(np.float32),
        20.0,
    )
    processed["feature_url_present"] = text.str.contains("<URL>", regex=False).astype(
        np.float32
    )
    processed["feature_email_present"] = text.str.contains(
        "<EMAIL>", regex=False
    ).astype(np.float32)
    processed["feature_all_caps_token_count"] = np.minimum(
        text.map(lambda value: len(ALL_CAPS_TOKEN_PATTERN.findall(value))).astype(
            np.float32
        ),
        20.0,
    )
    processed["feature_first_person_present"] = text.str.contains(
        FIRST_PERSON_PATTERN, na=False
    ).astype(np.float32)
    processed["feature_negation_present"] = text.str.contains(
        NEGATION_PATTERN, na=False
    ).astype(np.float32)

    text_hash = pd.util.hash_pandas_object(text, index=False).astype("uint64")
    processed["text_hash"] = text_hash.to_numpy()
    processed["feature_train_duplicate_count"] = (
        text_hash.map(duplicate_lookup).fillna(0).astype(np.float32).to_numpy()
    )
    processed["feature_log_train_duplicate_count"] = np.log1p(
        processed["feature_train_duplicate_count"]
    ).astype(np.float32)

    return processed


session = CandidateSession.from_env()

raw_train = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=lambda column: column in TRAIN_COLUMNS,
    low_memory=False,
)
raw_test = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train, raw_test)

train_df = train_df.loc[train_df["target"].notna()].reset_index(drop=True)
valid_df = valid_df.loc[valid_df["target"].notna()].reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

for column in TOXICITY_AUXILIARY_COLUMNS + IDENTITY_COLUMNS:
    if column in train_df.columns:
        train_df[column] = train_df[column].fillna(0.0).astype(np.float32)
    if column in valid_df.columns:
        valid_df[column] = valid_df[column].fillna(0.0).astype(np.float32)

train_df["target"] = train_df["target"].astype(np.float32)
valid_df["target"] = valid_df["target"].astype(np.float32)
train_df["target_binary"] = (train_df["target"] >= 0.5).astype(np.int8)
valid_df["target_binary"] = (valid_df["target"] >= 0.5).astype(np.int8)

for frame in (train_df, valid_df):
    available_identity_columns = [
        column for column in IDENTITY_COLUMNS if column in frame.columns
    ]
    available_eval_identity_columns = [
        column for column in EVALUATED_IDENTITY_COLUMNS if column in frame.columns
    ]

    frame["identity_any"] = (
        frame[available_identity_columns].max(axis=1) >= 0.5
    ).astype(np.int8)
    frame["evaluated_identity_any"] = (
        frame[available_eval_identity_columns].max(axis=1) >= 0.5
    ).astype(np.int8)
    frame["bias_slice"] = (
        frame["target_binary"].astype(str)
        + "_"
        + frame["evaluated_identity_any"].astype(str)
    )

train_clean_for_hash = train_df["comment_text"].map(normalize_comment)
train_hashes = pd.util.hash_pandas_object(train_clean_for_hash, index=False).astype(
    "uint64"
)
train_duplicate_lookup = train_hashes.value_counts().to_dict()

train_df = add_text_features(train_df, train_duplicate_lookup)
valid_df = add_text_features(valid_df, train_duplicate_lookup)
test_df = add_text_features(test_df, train_duplicate_lookup)

RAW_FEATURE_COLUMNS = [
    "feature_log_char_count",
    "feature_log_word_count",
    "feature_log_unique_word_count",
    "feature_unique_word_ratio",
    "feature_uppercase_ratio",
    "feature_exclamation_count",
    "feature_question_count",
    "feature_sentence_count",
    "feature_newline_count",
    "feature_digit_ratio",
    "feature_quote_count",
    "feature_url_present",
    "feature_email_present",
    "feature_all_caps_token_count",
    "feature_first_person_present",
    "feature_negation_present",
    "feature_log_train_duplicate_count",
]

FEATURE_COLUMNS = [f"{column}_scaled" for column in RAW_FEATURE_COLUMNS]
TEXT_COLUMN = "model_text"

feature_scaler = RobustScaler(quantile_range=(5.0, 95.0))
feature_scaler.fit(train_df[RAW_FEATURE_COLUMNS].fillna(0.0))

for frame in (train_df, valid_df, test_df):
    scaled_values = feature_scaler.transform(
        frame[RAW_FEATURE_COLUMNS].fillna(0.0)
    ).astype(np.float32)
    frame.loc[:, FEATURE_COLUMNS] = scaled_values

feature_artifact = {
    "normalization": {
        "unicode_normalization": "NFKC",
        "url_token": "<URL>",
        "email_token": "<EMAIL>",
        "long_text_max_chars": 6000,
        "long_text_head_chars": 3800,
    },
    "raw_feature_columns": RAW_FEATURE_COLUMNS,
    "scaled_feature_columns": FEATURE_COLUMNS,
    "identity_columns": IDENTITY_COLUMNS,
    "evaluated_identity_columns": EVALUATED_IDENTITY_COLUMNS,
    "toxicity_auxiliary_columns": TOXICITY_AUXILIARY_COLUMNS,
    "model_text_column": TEXT_COLUMN,
    "target_column": "target",
    "binary_target_column": "target_binary",
}

joblib.dump(feature_scaler, WORKING_DIR / "text_feature_scaler.joblib")
with open(
    WORKING_DIR / "feature_artifact.json", "w", encoding="utf-8"
) as artifact_file:
    json.dump(feature_artifact, artifact_file, indent=2)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame, text_column, feature_columns, identity_columns):
        self.texts = frame[text_column].fillna("").astype(str).to_numpy()
        self.features = (
            frame[feature_columns].fillna(0.0).to_numpy(dtype=np.float32, copy=True)
        )
        self.targets = frame["target"].fillna(0.0).to_numpy(dtype=np.float32, copy=True)
        self.identities = (
            frame[identity_columns].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.float32)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.features[index],
            self.targets[index],
            self.identities[index],
        )


model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"


def collate_training_batch(rows):
    texts, numeric_features, targets, identities = zip(*rows)

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=256,
        return_tensors="pt",
    )
    encoded["numeric_features"] = torch.from_numpy(
        np.stack(numeric_features).astype(np.float32, copy=False)
    )
    encoded["targets"] = torch.tensor(targets, dtype=torch.float32)
    encoded["identities"] = torch.from_numpy(
        np.stack(identities).astype(np.float32, copy=False)
    )
    return encoded


class StructuralFusionToxicityModel(nn.Module):
    def __init__(self, pretrained_classifier, numeric_feature_count):
        super().__init__()
        self.backbone = pretrained_classifier
        hidden_size = self.backbone.config.hidden_size

        self.text_norm = nn.LayerNorm(hidden_size)
        self.feature_encoder = nn.Sequential(
            nn.LayerNorm(numeric_feature_count),
            nn.Linear(numeric_feature_count, 128),
            nn.GELU(),
            nn.Dropout(0.12),
            nn.Linear(128, hidden_size),
        )
        self.feature_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )
        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_size),
            nn.Dropout(0.20),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.12),
            nn.Linear(hidden_size // 2, 2),
        )

    def forward(self, input_ids, attention_mask, numeric_features):
        encoded = self.backbone.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        text_embedding = self.text_norm(encoded.last_hidden_state[:, 0])
        feature_embedding = self.feature_encoder(numeric_features)

        fusion_gate = self.feature_gate(
            torch.cat([text_embedding, feature_embedding], dim=-1)
        )
        fused_embedding = text_embedding + fusion_gate * feature_embedding
        return self.classifier(fused_embedding)


class IdentityGroupDROLoss(nn.Module):
    def __init__(self, identity_count, robust_weight=0.38, ema_momentum=0.96):
        super().__init__()
        self.identity_count = identity_count
        self.robust_weight = robust_weight
        self.ema_momentum = ema_momentum
        self.register_buffer("group_ema", torch.zeros(identity_count * 2))
        self.register_buffer("group_seen", torch.zeros(identity_count * 2))

    def forward(self, logits, targets, identities):
        binary_targets = (targets >= 0.5).float()

        binary_loss = F.binary_cross_entropy_with_logits(
            logits[:, 0],
            binary_targets,
            reduction="none",
        )
        soft_loss = F.binary_cross_entropy_with_logits(
            logits[:, 1],
            targets.clamp(0.0, 1.0),
            reduction="none",
        )

        example_loss = 0.78 * binary_loss + 0.22 * soft_loss
        base_loss = example_loss.mean()

        active_group_losses = []
        active_group_ids = []
        class_targets = binary_targets >= 0.5

        for identity_index in range(self.identity_count):
            identity_present = identities[:, identity_index] >= 0.5

            for class_index in range(2):
                group_mask = identity_present & (class_targets == bool(class_index))
                group_id = identity_index * 2 + class_index

                if group_mask.any():
                    group_loss = example_loss[group_mask].mean()
                    active_group_losses.append(group_loss)
                    active_group_ids.append(group_id)

                    with torch.no_grad():
                        if self.group_seen[group_id] == 0:
                            self.group_ema[group_id] = group_loss.detach()
                        else:
                            self.group_ema[group_id] = (
                                self.ema_momentum * self.group_ema[group_id]
                                + (1.0 - self.ema_momentum) * group_loss.detach()
                            )
                        self.group_seen[group_id] += 1.0

        if not active_group_losses:
            return base_loss

        active_group_losses = torch.stack(active_group_losses)
        active_group_ids = torch.tensor(
            active_group_ids,
            dtype=torch.long,
            device=logits.device,
        )

        historical_losses = self.group_ema[active_group_ids].detach()
        robust_weights = torch.softmax(4.0 * historical_losses, dim=0)
        robust_loss = torch.sum(robust_weights * active_group_losses)

        return (1.0 - self.robust_weight) * base_loss + self.robust_weight * robust_loss


model = StructuralFusionToxicityModel(
    pretrained_classifier=model,
    numeric_feature_count=len(FEATURE_COLUMNS),
).to(device)

criterion = IdentityGroupDROLoss(
    identity_count=len(EVALUATED_IDENTITY_COLUMNS),
    robust_weight=0.38,
).to(device)

backbone_parameters = list(model.backbone.parameters())
backbone_parameter_ids = {id(parameter) for parameter in backbone_parameters}
head_parameters = [
    parameter
    for parameter in model.parameters()
    if id(parameter) not in backbone_parameter_ids
]

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_parameters,
            "lr": 1.0e-4,
            "weight_decay": 0.02,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

scheduler = torch.optim.lr_scheduler.LambdaLR(
    optimizer,
    lr_lambda=lambda step: min(1.0, float(step + 1) / 100.0),
)

train_dataset = ToxicityTrainingDataset(
    train_df,
    TEXT_COLUMN,
    FEATURE_COLUMNS,
    EVALUATED_IDENTITY_COLUMNS,
)

train_loader = DataLoader(
    train_dataset,
    batch_size=12,
    shuffle=True,
    num_workers=2,
    pin_memory=use_amp,
    persistent_workers=True,
    drop_last=False,
    collate_fn=collate_training_batch,
)

scaler = torch.cuda.amp.GradScaler(enabled=use_amp)


def predict_partition(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)

    if positional_indices.ndim != 1:
        raise ValueError("Prediction indices must be one-dimensional.")
    if len(positional_indices) and (
        positional_indices.min() < 0 or positional_indices.max() >= len(frame)
    ):
        raise IndexError("Prediction indices are outside the requested partition.")

    previous_training_state = model.training
    model.eval()

    predictions = np.empty(len(positional_indices), dtype=np.float32)
    partition_texts = frame[TEXT_COLUMN].fillna("").astype(str).to_numpy()
    partition_features = (
        frame[FEATURE_COLUMNS]
        .fillna(0.0)
        .to_numpy(
            dtype=np.float32,
            copy=False,
        )
    )

    inference_batch_size = 24

    try:
        with torch.inference_mode():
            for start_idx in range(0, len(positional_indices), inference_batch_size):
                batch_positions = positional_indices[
                    start_idx : start_idx + inference_batch_size
                ]

                encoded = tokenizer(
                    partition_texts[batch_positions].tolist(),
                    padding=True,
                    truncation=True,
                    max_length=256,
                    return_tensors="pt",
                )
                encoded = {
                    key: value.to(device, non_blocking=True)
                    for key, value in encoded.items()
                }

                batch_features = torch.from_numpy(
                    np.ascontiguousarray(partition_features[batch_positions])
                ).to(device, non_blocking=True)

                with torch.cuda.amp.autocast(enabled=use_amp):
                    logits = model(
                        input_ids=encoded["input_ids"],
                        attention_mask=encoded["attention_mask"],
                        numeric_features=batch_features,
                    )
                    binary_probability = torch.sigmoid(logits[:, 0])
                    soft_probability = torch.sigmoid(logits[:, 1])
                    probability = 0.78 * binary_probability + 0.22 * soft_probability

                predictions[start_idx : start_idx + len(batch_positions)] = (
                    probability.float().cpu().numpy()
                )
    finally:
        model.train(previous_training_state)

    return np.clip(predictions, 1e-6, 1.0 - 1e-6)


def predict_validation(positional_indices):
    return predict_partition(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_partition(test_df, positional_indices)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    tokenizer.save_pretrained(str(directory / "tokenizer"))
    model.backbone.config.save_pretrained(str(directory / "backbone_config"))

    inference_state = {
        "model_id": model_id,
        "text_column": TEXT_COLUMN,
        "feature_columns": list(FEATURE_COLUMNS),
        "identity_columns": list(EVALUATED_IDENTITY_COLUMNS),
        "max_length": 256,
        "prediction_blend": {
            "binary_head": 0.78,
            "soft_target_head": 0.22,
        },
    }
    with open(directory / "inference_state.json", "w", encoding="utf-8") as output_file:
        json.dump(inference_state, output_file, indent=2)

    for artifact_name in ("feature_artifact.json", "text_feature_scaler.joblib"):
        source_path = WORKING_DIR / artifact_name
        if source_path.exists():
            shutil.copy2(source_path, directory / artifact_name)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "criterion_state_dict": criterion.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "scaler_state_dict": scaler.state_dict(),
        },
        directory / "training_state.pt",
    )


def load_checkpoint(directory):
    global tokenizer

    directory = Path(directory)
    tokenizer = AutoTokenizer.from_pretrained(
        str(directory / "tokenizer"),
        local_files_only=True,
    )

    checkpoint = torch.load(
        directory / "training_state.pt",
        map_location=device,
        weights_only=False,
    )

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    criterion.load_state_dict(checkpoint["criterion_state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    scheduler.load_state_dict(checkpoint["scheduler_state_dict"])
    scaler.load_state_dict(checkpoint["scaler_state_dict"])


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer_updates = 0
epoch = 0
stop_training = False

while not stop_training:
    epoch += 1
    model.train()

    epoch_loss = 0.0
    completed_batches = 0

    for batch in train_loader:
        input_ids = batch["input_ids"].to(device, non_blocking=True)
        attention_mask = batch["attention_mask"].to(device, non_blocking=True)
        numeric_features = batch["numeric_features"].to(device, non_blocking=True)
        targets = batch["targets"].to(device, non_blocking=True)
        identities = batch["identities"].to(device, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                numeric_features=numeric_features,
            )
            loss = criterion(logits, targets, identities)

        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        scheduler.step()

        optimizer_updates += 1
        completed_batches += 1
        epoch_loss += float(loss.detach().cpu())

        stop_training = session.step()
        if stop_training:
            break

    if completed_batches == 0:
        break

    print(
        f"epoch={epoch} mean_loss={epoch_loss / completed_batches:.6f} "
        f"optimizer_updates={optimizer_updates}"
    )

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
