import os
import re
import json
import html
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
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime-owned split: performed before fitting any data-dependent state.
# ---------------------------------------------------------------------
os.environ["TOKENIZERS_PARALLELISM"] = "false"

session = CandidateSession.from_env()

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
FEATURE_DIR = WORKING_DIR / "text_features"
FEATURE_DIR.mkdir(parents=True, exist_ok=True)

train_path = INPUT_DIR / "train.csv"
test_path = INPUT_DIR / "test.csv"

all_train_columns = pd.read_csv(train_path, nrows=0).columns.tolist()

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
official_identity_columns = [
    column for column in official_identity_columns if column in all_train_columns
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
all_identity_columns = [
    column for column in all_identity_columns if column in all_train_columns
]

auxiliary_target_columns = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]
auxiliary_target_columns = [
    column for column in auxiliary_target_columns if column in all_train_columns
]

train_usecols = list(
    dict.fromkeys(
        ["id", "target", "comment_text"]
        + auxiliary_target_columns
        + all_identity_columns
    )
)

train_dtype = {"id": "int64", "target": "float32"}
train_dtype.update(
    {column: "float32" for column in auxiliary_target_columns + all_identity_columns}
)

raw_train_df = pd.read_csv(
    train_path,
    usecols=train_usecols,
    dtype=train_dtype,
    low_memory=False,
)
raw_test_df = pd.read_csv(
    test_path,
    usecols=["id", "comment_text"],
    dtype={"id": "int64"},
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df


# ---------------------------------------------------------------------
# Stateless text normalization and inference-safe feature engineering.
# ---------------------------------------------------------------------
CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
URL_RE = re.compile(
    r"\b(?:https?://|www\.)[^\s<>()\[\]{}]+"
    r"|\b(?:[a-z0-9-]+\.)+(?:com|org|net|edu|gov|io|co|uk|ca|au)"
    r"(?:/[^\s<>()\[\]{}]*)?",
    flags=re.IGNORECASE,
)
EMAIL_RE = re.compile(
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    flags=re.IGNORECASE,
)
MULTISPACE_RE = re.compile(r"[ \t\f\v]+")
NEWLINE_RE = re.compile(r"\s*\n+\s*")

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
    "black": "white",
    "white": "black",
    "asian": "latino",
    "latino": "asian",
    "latina": "asian",
    "christian": "muslim",
    "christians": "muslims",
    "muslim": "jewish",
    "muslims": "jews",
    "jewish": "christian",
    "jews": "christians",
    "gay": "straight",
    "lesbian": "straight",
    "homosexual": "heterosexual",
    "heterosexual": "homosexual",
    "straight": "gay",
    "transgender": "cisgender",
    "cisgender": "transgender",
}
COUNTERFACTUAL_RE = re.compile(
    r"\b(?:"
    + "|".join(
        sorted(
            map(re.escape, COUNTERFACTUAL_MAP),
            key=len,
            reverse=True,
        )
    )
    + r")\b",
    flags=re.IGNORECASE,
)


def normalize_single_text(value):
    text = "" if pd.isna(value) else str(value)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = CONTROL_CHAR_RE.sub(" ", text)
    text = EMAIL_RE.sub(" <EMAIL> ", text)
    text = URL_RE.sub(" <URL> ", text)
    text = NEWLINE_RE.sub(" <NL> ", text)
    text = MULTISPACE_RE.sub(" ", text).strip()
    return text


def preserve_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement.capitalize()
    return replacement


def swap_identity_terms(text):
    def replace_match(match):
        source = match.group(0)
        replacement = COUNTERFACTUAL_MAP[source.lower()]
        return preserve_case(source, replacement)

    return COUNTERFACTUAL_RE.sub(replace_match, text)


def engineer_text_features(frame):
    raw_text = frame["comment_text"].fillna("").astype(str)

    has_url = raw_text.str.contains(URL_RE, na=False).astype("float32")
    has_email = raw_text.str.contains(EMAIL_RE, na=False).astype("float32")

    canonical_text = raw_text.map(normalize_single_text)
    frame["text_model"] = canonical_text
    frame.drop(columns=["comment_text"], inplace=True)

    char_count = canonical_text.str.len().clip(lower=0).astype("float32")
    word_count = canonical_text.str.count(r"\S+").astype("float32")
    alpha_count = canonical_text.str.count(r"[A-Za-z]").astype("float32")
    uppercase_count = canonical_text.str.count(r"[A-Z]").astype("float32")
    digit_count = canonical_text.str.count(r"\d").astype("float32")

    identity_lexical_flag = canonical_text.str.contains(
        COUNTERFACTUAL_RE,
        na=False,
    ).astype("int8")

    frame["counterfactual_text"] = pd.Series(
        pd.NA,
        index=frame.index,
        dtype="string",
    )
    counterfactual_mask = identity_lexical_flag.astype(bool)
    if counterfactual_mask.any():
        frame.loc[counterfactual_mask, "counterfactual_text"] = (
            canonical_text.loc[counterfactual_mask]
            .map(swap_identity_terms)
            .astype("string")
        )

    frame["identity_lexical_flag"] = identity_lexical_flag
    frame["log_char_count"] = np.log1p(char_count).astype("float32")
    frame["log_word_count"] = np.log1p(word_count).astype("float32")
    frame["uppercase_ratio"] = (
        (uppercase_count / alpha_count.clip(lower=1.0)).clip(0.0, 1.0).astype("float32")
    )
    frame["digit_ratio"] = (
        (digit_count / char_count.clip(lower=1.0)).clip(0.0, 1.0).astype("float32")
    )
    frame["exclamation_count"] = np.log1p(
        canonical_text.str.count("!").astype("float32")
    ).astype("float32")
    frame["question_count"] = np.log1p(
        canonical_text.str.count(r"\?").astype("float32")
    ).astype("float32")
    frame["quote_count"] = np.log1p(
        canonical_text.str.count(r"""["']""").astype("float32")
    ).astype("float32")
    frame["newline_count"] = np.log1p(
        canonical_text.str.count(r"<NL>").astype("float32")
    ).astype("float32")
    frame["has_url"] = has_url
    frame["has_email"] = has_email


engineer_text_features(train_df)
engineer_text_features(valid_df)
engineer_text_features(test_df)

train_df["target_binary"] = (train_df["target"].fillna(0.0) >= 0.5).astype("int8")
valid_df["target_binary"] = (valid_df["target"].fillna(0.0) >= 0.5).astype("int8")

text_feature_columns = [
    "log_char_count",
    "log_word_count",
    "uppercase_ratio",
    "digit_ratio",
    "exclamation_count",
    "question_count",
    "quote_count",
    "newline_count",
    "has_url",
    "has_email",
    "identity_lexical_flag",
]

text_feature_scaler = RobustScaler(
    quantile_range=(5.0, 95.0),
    with_centering=True,
    with_scaling=True,
)

train_features = train_df[text_feature_columns].fillna(0.0).to_numpy(dtype=np.float32)
text_feature_scaler.fit(train_features)

for frame in (train_df, valid_df, test_df):
    scaled_features = text_feature_scaler.transform(
        frame[text_feature_columns].fillna(0.0).to_numpy(dtype=np.float32)
    ).astype(np.float32)

    for feature_idx, feature_name in enumerate(text_feature_columns):
        frame[f"{feature_name}_scaled"] = scaled_features[:, feature_idx]

scaled_text_feature_columns = [f"{column}_scaled" for column in text_feature_columns]

joblib.dump(text_feature_scaler, FEATURE_DIR / "text_feature_scaler.joblib")

with open(FEATURE_DIR / "feature_config.json", "w", encoding="utf-8") as handle:
    json.dump(
        {
            "text_column": "text_model",
            "counterfactual_text_column": "counterfactual_text",
            "raw_text_feature_columns": text_feature_columns,
            "scaled_text_feature_columns": scaled_text_feature_columns,
            "official_identity_columns": official_identity_columns,
            "all_identity_columns": all_identity_columns,
            "auxiliary_target_columns": auxiliary_target_columns,
            "target_column": "target",
            "binary_target_column": "target_binary",
            "counterfactual_map": COUNTERFACTUAL_MAP,
        },
        handle,
        ensure_ascii=False,
        indent=2,
    )


# ---------------------------------------------------------------------
# DeBERTa-v3-large model and metric-aligned ranking objective.
# ---------------------------------------------------------------------
"""
DeBERTa-v3-large Usage Example
Base model: microsoft/deberta-v3-large (~435M parameters)
Domain: Natural language toxicity classification
Input: tokenized comments
Output: two-class toxicity logits
"""

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)
model.config.id2label = {0: "non_toxic", 1: "toxic"}
model.config.label2id = {"non_toxic": 0, "toxic": 1}


class BiasAwarePairwiseAUCLoss(nn.Module):
    def __init__(
        self,
        identity_names,
        classification_weight=0.60,
        ranking_weight=0.40,
        margin_temperature=0.25,
        identity_threshold=0.50,
        max_pairs_per_slice=96,
        hard_group_temperature=0.20,
    ):
        super().__init__()
        self.identity_names = tuple(identity_names)
        self.classification_weight = float(classification_weight)
        self.ranking_weight = float(ranking_weight)
        self.margin_temperature = float(margin_temperature)
        self.identity_threshold = float(identity_threshold)
        self.max_pairs_per_slice = int(max_pairs_per_slice)
        self.hard_group_temperature = float(hard_group_temperature)

    def pairwise_auc_surrogate(self, positive_scores, negative_scores):
        positive_count = positive_scores.numel()
        negative_count = negative_scores.numel()

        if positive_count == 0 or negative_count == 0:
            return None

        pair_count = min(
            self.max_pairs_per_slice,
            positive_count * negative_count,
        )
        pair_indices = torch.arange(
            pair_count,
            device=positive_scores.device,
        )

        positive_indices = pair_indices.remainder(positive_count)
        negative_indices = (pair_indices * 17 + 3).remainder(negative_count)

        score_margin = (
            positive_scores[positive_indices] - negative_scores[negative_indices]
        )
        return F.softplus(-score_margin / self.margin_temperature).mean()

    def forward(self, logits, binary_targets, identity_targets):
        if logits.ndim != 2 or logits.size(-1) != 2:
            raise ValueError("Expected logits with shape [batch_size, 2].")

        if identity_targets.ndim != 2:
            raise ValueError(
                "Expected identity_targets with shape [batch_size, n_identities]."
            )

        if identity_targets.size(1) != len(self.identity_names):
            raise ValueError(
                "Identity target columns must match configured official identities."
            )

        binary_targets = binary_targets.float().reshape(-1)
        if binary_targets.numel() != logits.size(0):
            raise ValueError("binary_targets and logits must have equal batch size.")

        class_margin = logits[:, 1] - logits[:, 0]
        classification_loss = F.binary_cross_entropy_with_logits(
            class_margin,
            binary_targets,
        )

        toxic_mask = binary_targets >= 0.5
        non_toxic_mask = ~toxic_mask
        slice_losses = []

        for identity_index in range(identity_targets.size(1)):
            subgroup_mask = (
                identity_targets[:, identity_index].float() >= self.identity_threshold
            )
            background_mask = ~subgroup_mask

            subgroup_loss = self.pairwise_auc_surrogate(
                class_margin[subgroup_mask & toxic_mask],
                class_margin[subgroup_mask & non_toxic_mask],
            )
            if subgroup_loss is not None:
                slice_losses.append(subgroup_loss)

            bpsn_loss = self.pairwise_auc_surrogate(
                class_margin[background_mask & toxic_mask],
                class_margin[subgroup_mask & non_toxic_mask],
            )
            if bpsn_loss is not None:
                slice_losses.append(bpsn_loss)

            bnsp_loss = self.pairwise_auc_surrogate(
                class_margin[subgroup_mask & toxic_mask],
                class_margin[background_mask & non_toxic_mask],
            )
            if bnsp_loss is not None:
                slice_losses.append(bnsp_loss)

        if not slice_losses:
            return classification_loss

        slice_losses = torch.stack(slice_losses)
        hard_weights = torch.softmax(
            (slice_losses.detach() - slice_losses.detach().mean())
            / self.hard_group_temperature,
            dim=0,
        )
        ranking_loss = torch.sum(hard_weights * slice_losses)

        return (
            self.classification_weight * classification_loss
            + self.ranking_weight * ranking_loss
        )


criterion = BiasAwarePairwiseAUCLoss(
    identity_names=official_identity_columns,
    classification_weight=0.60,
    ranking_weight=0.40,
    margin_temperature=0.25,
    max_pairs_per_slice=96,
    hard_group_temperature=0.20,
)

head_parameter_names = ("classifier.", "pooler.")
backbone_parameters = []
head_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue
    if parameter_name.startswith(head_parameter_names):
        head_parameters.append(parameter)
    else:
        backbone_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_parameters,
            "lr": 5.0e-5,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)


def toxicity_probability_from_logits(logits):
    return torch.softmax(logits, dim=-1)[:, 1]


# ---------------------------------------------------------------------
# Training, official-runtime validation, checkpointing, and submission.
# ---------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 24
NUM_WORKERS = 2
MAX_EPOCHS = 4

torch.manual_seed(2029)
np.random.seed(2029)

model.to(device)
# Non-reentrant checkpointing avoids DeBERTa's reentrant backward graph reuse error.
# It preserves activation-memory savings while allowing one normal backward pass per update.
if hasattr(model, "gradient_checkpointing_enable"):
    model.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )
if hasattr(model.config, "use_cache"):
    model.config.use_cache = False


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["text_model"].to_numpy(dtype=object, copy=False)
        self.binary_targets = (
            frame["target_binary"].fillna(0).astype(np.float32).to_numpy(copy=True)
        )
        self.identity_targets = (
            frame[official_identity_columns]
            .fillna(0.0)
            .astype(np.float32)
            .to_numpy(copy=True)
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        if not isinstance(text, str):
            text = "" if pd.isna(text) else str(text)

        return (
            text,
            torch.tensor(self.binary_targets[index], dtype=torch.float32),
            torch.from_numpy(self.identity_targets[index]),
        )


def collate_training_batch(batch):
    texts, binary_targets, identity_targets = zip(*batch)
    encoded = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )
    return (
        encoded,
        torch.stack(binary_targets),
        torch.stack(identity_targets),
    )


def predict_frame_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    was_training = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for start in range(0, len(positions), INFERENCE_BATCH_SIZE):
                batch_positions = positions[start : start + INFERENCE_BATCH_SIZE]
                texts = (
                    frame.iloc[batch_positions]["text_model"]
                    .fillna("")
                    .astype(str)
                    .tolist()
                )
                encoded = tokenizer(
                    texts,
                    truncation=True,
                    max_length=MAX_LENGTH,
                    padding=True,
                    return_tensors="pt",
                )
                encoded = {
                    key: value.to(device, non_blocking=True)
                    for key, value in encoded.items()
                }

                with torch.cuda.amp.autocast(enabled=use_amp):
                    logits = model(**encoded).logits
                    probabilities = toxicity_probability_from_logits(logits)

                predictions.append(
                    probabilities.detach().float().cpu().numpy().astype(np.float64)
                )
    finally:
        model.train(was_training)

    return np.concatenate(predictions, axis=0)


def predict_validation(positional_indices):
    return predict_frame_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_length": MAX_LENGTH,
            "prediction_semantics": "softmax_class_1_toxicity_probability",
            "official_identity_columns": list(official_identity_columns),
        },
        checkpoint_dir / "model_state.pt",
    )

    model.config.save_pretrained(checkpoint_dir / "model_config")
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    with open(checkpoint_dir / "inference_state.json", "w", encoding="utf-8") as handle:
        json.dump(
            {
                "text_column": "text_model",
                "max_length": MAX_LENGTH,
                "prediction_semantics": "softmax_class_1_toxicity_probability",
                "identity_threshold": 0.5,
            },
            handle,
            indent=2,
        )

    for artifact_name in ("feature_config.json", "text_feature_scaler.joblib"):
        source_path = FEATURE_DIR / artifact_name
        if source_path.exists():
            shutil.copy2(source_path, checkpoint_dir / artifact_name)


def load_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=device,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

training_dataset = ToxicityTrainingDataset(train_df)
training_generator = torch.Generator()
training_generator.manual_seed(2029)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=False,
    num_workers=NUM_WORKERS,
    pin_memory=use_amp,
    persistent_workers=True,
    collate_fn=collate_training_batch,
    generator=training_generator,
)

scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
stop_training = False
optimizer_updates = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    running_loss = 0.0
    completed_updates = 0

    for encoded_batch, binary_targets, identity_targets in training_loader:
        encoded_batch = {
            key: value.to(device, non_blocking=True)
            for key, value in encoded_batch.items()
        }
        binary_targets = binary_targets.to(device, non_blocking=True)
        identity_targets = identity_targets.to(device, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(**encoded_batch).logits
            loss = criterion(
                logits=logits,
                binary_targets=binary_targets,
                identity_targets=identity_targets,
            )

        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()

        optimizer_updates += 1
        completed_updates += 1
        running_loss += float(loss.detach().cpu())

        stop_training = session.step()
        if stop_training:
            break

    mean_loss = running_loss / max(completed_updates, 1)
    print(
        f"epoch={epoch} updates={completed_updates} "
        f"optimizer_steps={optimizer_updates} train_loss={mean_loss:.6f}"
    )

    if stop_training:
        break

result = session.finish()