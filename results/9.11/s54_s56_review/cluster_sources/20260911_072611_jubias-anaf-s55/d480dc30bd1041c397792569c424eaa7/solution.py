import html
import json
import re
import shutil
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime-owned split. This must occur before fitting any transformations.
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

input_dir = Path("./input")
working_dir = Path("./working")
feature_dir = working_dir / "processed_features"
feature_dir.mkdir(parents=True, exist_ok=True)

raw_train_df = pd.read_csv(input_dir / "train.csv", low_memory=False)
raw_test_df = pd.read_csv(input_dir / "test.csv", low_memory=False)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

if "comment_text" not in train_df.columns or "comment_text" not in test_df.columns:
    raise ValueError("Both train.csv and test.csv must contain 'comment_text'.")
if "target" not in train_df.columns:
    raise ValueError("train.csv must contain the continuous 'target' column.")


# ---------------------------------------------------------------------
# Data processing and feature engineering.
# ---------------------------------------------------------------------
toxicity_auxiliary_columns = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

identity_label_columns = [
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

IDENTITY_COLUMNS = (
    "male",
    "female",
    "homosexual_gay_or_lesbian",
    "christian",
    "jewish",
    "muslim",
    "black",
    "white",
    "psychiatric_or_mental_illness",
)

available_supervised_columns = [
    column
    for column in ["target", *toxicity_auxiliary_columns, *identity_label_columns]
    if column in train_df.columns
]


def select_usable_columns(
    frame: pd.DataFrame,
    is_training_partition: bool,
) -> pd.DataFrame:
    columns = ["id", "comment_text"]
    if is_training_partition:
        columns.extend(available_supervised_columns)
    return frame.loc[:, columns].copy()


train_df = select_usable_columns(train_df, is_training_partition=True)
valid_df = select_usable_columns(valid_df, is_training_partition=True)
test_df = select_usable_columns(test_df, is_training_partition=False)

url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
whitespace_pattern = re.compile(r"\s+")
control_pattern = re.compile(r"[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f-\u009f]")


def normalize_comment(value: object) -> str:
    if pd.isna(value):
        return ""

    text = html.unescape(str(value))
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", " ").replace("\ufeff", " ")
    text = control_pattern.sub(" ", text)
    text = url_pattern.sub(" <url> ", text)
    return whitespace_pattern.sub(" ", text).strip()


identity_lexicons = {
    "male": r"\b(?:male|males|man|men|boy|boys|gentleman|gentlemen)\b",
    "female": r"\b(?:female|females|woman|women|girl|girls|lady|ladies)\b",
    "gay_lesbian": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|queer|"
        r"lgbt|lgbtq|lgbtqia)\b"
    ),
    "christian": r"\b(?:christian|christians|christianity)\b",
    "jewish": r"\b(?:jew|jews|jewish|judaism)\b",
    "muslim": r"\b(?:muslim|muslims|islam|islamic)\b",
    "black": r"\b(?:black|blacks|african[\s-]?american|afro[\s-]?american)\b",
    "white": r"\b(?:white|whites|caucasian|caucasians)\b",
    "mental_illness": (
        r"\b(?:mental[\s-]?illness|psychiatric|schizophren(?:ia|ic)|"
        r"bipolar|autis(?:m|tic)|depress(?:ion|ed)?)\b"
    ),
}

compiled_identity_patterns = {
    name: re.compile(pattern, flags=re.IGNORECASE)
    for name, pattern in identity_lexicons.items()
}

combined_identity_pattern = re.compile(
    "(?:" + "|".join(f"(?:{pattern})" for pattern in identity_lexicons.values()) + ")",
    flags=re.IGNORECASE,
)


def add_text_features(frame: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    frame = frame.copy()

    cleaned_text = frame["comment_text"].map(normalize_comment)
    frame["model_text"] = cleaned_text
    frame["identity_masked_text"] = (
        cleaned_text.str.replace(
            combined_identity_pattern,
            " <identity> ",
            regex=True,
        )
        .str.replace(whitespace_pattern, " ", regex=True)
        .str.strip()
    )

    char_count = cleaned_text.str.len().astype(np.float32)
    word_count = cleaned_text.str.count(r"\b[\w']+\b").astype(np.float32)
    letter_count = cleaned_text.str.count(r"[A-Za-z]").astype(np.float32)

    engineered_features = {
        "feat_log_char_count": np.log1p(char_count),
        "feat_log_word_count": np.log1p(word_count),
        "feat_log_url_count": np.log1p(
            cleaned_text.str.count(r"<url>").astype(np.float32)
        ),
        "feat_log_exclamation_count": np.log1p(
            cleaned_text.str.count(r"!").astype(np.float32)
        ),
        "feat_log_question_count": np.log1p(
            cleaned_text.str.count(r"\?").astype(np.float32)
        ),
        "feat_log_quote_count": np.log1p(
            cleaned_text.str.count(r"""["']""").astype(np.float32)
        ),
        "feat_log_newline_count": np.log1p(
            cleaned_text.str.count(r"\n").astype(np.float32)
        ),
        "feat_log_digit_count": np.log1p(
            cleaned_text.str.count(r"\d").astype(np.float32)
        ),
        "feat_log_repeated_punctuation": np.log1p(
            cleaned_text.str.count(r"(?:!{2,}|\?{2,}|\.{3,})").astype(np.float32)
        ),
        "feat_uppercase_ratio": (
            cleaned_text.str.count(r"[A-Z]").astype(np.float32)
            / np.maximum(letter_count, 1.0)
        ),
        "feat_digit_ratio": (
            cleaned_text.str.count(r"\d").astype(np.float32)
            / np.maximum(char_count, 1.0)
        ),
        "feat_punctuation_ratio": (
            cleaned_text.str.count(r"[^\w\s]").astype(np.float32)
            / np.maximum(char_count, 1.0)
        ),
    }

    for feature_name, values in engineered_features.items():
        frame[feature_name] = np.asarray(values, dtype=np.float32)

    lexical_feature_columns = []
    for identity_name, pattern in compiled_identity_patterns.items():
        feature_name = f"feat_identity_mention_{identity_name}"
        frame[feature_name] = cleaned_text.str.contains(pattern, na=False).astype(
            np.float32
        )
        lexical_feature_columns.append(feature_name)

    frame["feat_identity_mention_count"] = (
        frame[lexical_feature_columns].sum(axis=1).astype(np.float32)
    )

    feature_columns = (
        list(engineered_features)
        + lexical_feature_columns
        + ["feat_identity_mention_count"]
    )

    frame.drop(columns=["comment_text"], inplace=True)
    return frame, feature_columns


train_df, numeric_feature_columns = add_text_features(train_df)
valid_df, valid_feature_columns = add_text_features(valid_df)
test_df, test_feature_columns = add_text_features(test_df)

if (
    numeric_feature_columns != valid_feature_columns
    or numeric_feature_columns != test_feature_columns
):
    raise RuntimeError("Feature schemas differ across data partitions.")

scaler_state = {}

for column in numeric_feature_columns:
    train_values = train_df[column].to_numpy(dtype=np.float32, copy=False)
    finite_values = train_values[np.isfinite(train_values)]

    if finite_values.size == 0:
        lower, upper, mean, std = 0.0, 0.0, 0.0, 1.0
    else:
        lower = float(np.quantile(finite_values, 0.001))
        upper = float(np.quantile(finite_values, 0.999))
        clipped_train_values = np.clip(finite_values, lower, upper)
        mean = float(clipped_train_values.mean())
        std = float(clipped_train_values.std())
        if not np.isfinite(std) or std < 1e-6:
            std = 1.0

    scaler_state[column] = {
        "lower": lower,
        "upper": upper,
        "mean": mean,
        "std": std,
    }


def apply_train_fitted_scaler(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()

    for column, params in scaler_state.items():
        values = frame[column].to_numpy(dtype=np.float32, copy=False)
        values = np.nan_to_num(
            values,
            nan=params["mean"],
            posinf=params["upper"],
            neginf=params["lower"],
        )
        values = np.clip(values, params["lower"], params["upper"])
        frame[column] = ((values - params["mean"]) / params["std"]).astype(np.float32)

    return frame


train_df = apply_train_fitted_scaler(train_df)
valid_df = apply_train_fitted_scaler(valid_df)
test_df = apply_train_fitted_scaler(test_df)

for column in available_supervised_columns:
    train_df[column] = pd.to_numeric(train_df[column], errors="coerce").astype(
        np.float32
    )
    valid_df[column] = pd.to_numeric(valid_df[column], errors="coerce").astype(
        np.float32
    )

if not test_df["id"].astype(str).equals(raw_test_df["id"].astype(str)):
    raise RuntimeError("Test row order changed during preprocessing.")

artifact_paths = {
    "train": feature_dir / "train_features.parquet",
    "validation": feature_dir / "validation_features.parquet",
    "test": feature_dir / "test_features.parquet",
}

try:
    train_df.to_parquet(artifact_paths["train"], index=False, compression="zstd")
    valid_df.to_parquet(artifact_paths["validation"], index=False, compression="zstd")
    test_df.to_parquet(artifact_paths["test"], index=False, compression="zstd")
    storage_format = "parquet"
except Exception:
    artifact_paths = {
        "train": feature_dir / "train_features.pkl",
        "validation": feature_dir / "validation_features.pkl",
        "test": feature_dir / "test_features.pkl",
    }
    train_df.to_pickle(artifact_paths["train"])
    valid_df.to_pickle(artifact_paths["validation"])
    test_df.to_pickle(artifact_paths["test"])
    storage_format = "pickle"

feature_manifest = {
    "storage_format": storage_format,
    "text_column": "model_text",
    "counterfactual_text_column": "identity_masked_text",
    "numeric_feature_columns": numeric_feature_columns,
    "supervised_columns": available_supervised_columns,
    "scaler_state_fitted_on": "train_partition_only",
    "scaler_state": scaler_state,
    "artifacts": {name: str(path) for name, path in artifact_paths.items()},
    "train_rows": int(len(train_df)),
    "validation_rows": int(len(valid_df)),
    "test_rows": int(len(test_df)),
}

with open(feature_dir / "feature_manifest.json", "w", encoding="utf-8") as file:
    json.dump(feature_manifest, file, indent=2)


# ---------------------------------------------------------------------
# Model design: DeBERTa toxicity prediction with conditional identity MMD.
# ---------------------------------------------------------------------
MODEL_ID = "microsoft/deberta-v3-large"
MAX_SEQUENCE_LENGTH = 256

class FairDebertaToxicityModel(nn.Module):
=======
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class FairDebertaToxicityModel(nn.Module):


=======

=======
=======


class FairDebertaToxicityModel(nn.Module):
=======
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class FairDebertaToxicityModel(nn.Module):


=======

=======


class FairDebertaToxicityModel(nn.Module):
    def __init__(
        self,
        pretrained_sequence_model: nn.Module,
        num_identity_labels: int,
        dropout_probability: float = 0.15,
    ) -> None:
        super().__init__()

        self.encoder = pretrained_sequence_model.deberta
        self.hidden_size = int(pretrained_sequence_model.config.hidden_size)
        self.dropout_probability = float(dropout_probability)

        self.representation_norm = nn.LayerNorm(self.hidden_size)
        self.representation_dropout = nn.Dropout(self.dropout_probability)

        self.toxicity_head = nn.Sequential(
            nn.Linear(self.hidden_size, self.hidden_size // 2),
            nn.GELU(),
            nn.Dropout(self.dropout_probability),
            nn.Linear(self.hidden_size // 2, 1),
        )

        self.identity_adversary = nn.Sequential(
            nn.Linear(self.hidden_size, self.hidden_size // 2),
            nn.GELU(),
            nn.Dropout(self.dropout_probability),
            nn.Linear(self.hidden_size // 2, num_identity_labels),
        )

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        adversarial_coefficient: float = 0.0,
    ) -> dict[str, torch.Tensor]:
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        cls_representation = encoder_outputs.last_hidden_state[:, 0]
        representation = self.representation_dropout(
            self.representation_norm(cls_representation)
        )

        toxicity_logits = self.toxicity_head(representation).squeeze(-1)

        return {
            "toxicity_logits": toxicity_logits,
        }

    @torch.inference_mode()
    def predict_proba(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        was_training = self.training
        self.eval()

        outputs = self.forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            adversarial_coefficient=0.0,
        )
        probabilities = torch.sigmoid(outputs["toxicity_logits"])

        self.train(was_training)
        return probabilities


class FairToxicityLoss(nn.Module):
    def __init__(
        self,
        mmd_loss_weight: float = 0.03,
        benign_target_threshold: float = 0.5,
        num_random_features: int = 32,
        min_group_observations: int = 1,
    ) -> None:
        super().__init__()
        self.mmd_loss_weight = float(mmd_loss_weight)
        self.benign_target_threshold = float(benign_target_threshold)
        self.min_group_observations = int(min_group_observations)

        rff_generator = torch.Generator(device="cpu")
        rff_generator.manual_seed(2027)
        rff_frequencies = torch.randn(
            int(num_random_features),
            generator=rff_generator,
            dtype=torch.float32,
        )
        rff_phases = (
            2.0
            * np.pi
            * torch.rand(
                int(num_random_features),
                generator=rff_generator,
                dtype=torch.float32,
            )
        )
        self.register_buffer("rff_frequencies", rff_frequencies)
        self.register_buffer("rff_phases", rff_phases)

    def forward(
        self,
        model_outputs: dict[str, torch.Tensor],
        toxicity_targets: torch.Tensor,
        identity_targets: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        toxicity_targets = toxicity_targets.float().clamp_(0.0, 1.0)
        toxicity_logits = model_outputs["toxicity_logits"]

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
        )

        logits_float = toxicity_logits.float()
        rff_features = torch.cos(
            logits_float.unsqueeze(1)
            * self.rff_frequencies.to(dtype=torch.float32).unsqueeze(0)
            + self.rff_phases.to(dtype=torch.float32).unsqueeze(0)
        )
        rff_features = rff_features * np.sqrt(2.0 / self.rff_frequencies.numel())

        identity_targets = identity_targets.float()
        valid_identity_labels = torch.isfinite(identity_targets)
        benign_rows = toxicity_targets < self.benign_target_threshold
        toxic_rows = toxicity_targets >= self.benign_target_threshold
        mmd_terms = []

        for toxicity_stratum in (benign_rows, toxic_rows):
            for identity_index in range(identity_targets.shape[1]):
                identity_values = identity_targets[:, identity_index]
                valid_labels = valid_identity_labels[:, identity_index]
                present_rows = (
                    toxicity_stratum
                    & valid_labels
                    & (identity_values >= 0.5)
                )
                absent_rows = (
                    toxicity_stratum
                    & valid_labels
                    & (identity_values < 0.5)
                )

                if (
                    int(present_rows.sum().item()) >= self.min_group_observations
                    and int(absent_rows.sum().item()) >= self.min_group_observations
                ):
                    mean_difference = (
                        rff_features[present_rows].mean(dim=0)
                        - rff_features[absent_rows].mean(dim=0)
                    )
                    mmd_terms.append(mean_difference.square().sum())

        if mmd_terms:
            conditional_mmd_loss = torch.stack(mmd_terms).mean()
        else:
            conditional_mmd_loss = logits_float.sum() * 0.0

        total_loss = toxicity_loss + self.mmd_loss_weight * conditional_mmd_loss
        active_mmd_cells = toxicity_logits.new_tensor(float(len(mmd_terms)))

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "mmd_loss": conditional_mmd_loss.detach(),
            "active_mmd_cells": active_mmd_cells.detach(),
        }


fair_model = FairDebertaToxicityModel(
    pretrained_sequence_model=model,
    num_identity_labels=len(IDENTITY_COLUMNS),
    dropout_probability=0.15,
)

criterion = FairToxicityLoss(
    mmd_loss_weight=0.03,
    benign_target_threshold=0.5,
)

optimizer = AdamW(
    [
        {
            "params": fair_model.encoder.parameters(),
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": (
                list(fair_model.representation_norm.parameters())
                + list(fair_model.toxicity_head.parameters())
            ),
            "lr": 1.0e-4,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)


# ---------------------------------------------------------------------
# Training, runtime checkpointing, official-metric validation and export.
# ---------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
fair_model.to(device)

torch.manual_seed(2027)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(2027)

TRAIN_BATCH_SIZE = 4
INFERENCE_BATCH_SIZE = 16
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 100
NUM_WORKERS = 2
PIN_MEMORY = device.type == "cuda"


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame: pd.DataFrame) -> None:
        self.texts = frame["model_text"].fillna("").astype(str).tolist()
        self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)

        identity_arrays = []
        for column in IDENTITY_COLUMNS:
            if column in frame.columns:
                identity_arrays.append(
                    frame[column].to_numpy(dtype=np.float32, copy=True)
                )
            else:
                identity_arrays.append(np.full(len(frame), np.nan, dtype=np.float32))

        self.identity_targets = np.column_stack(identity_arrays).astype(
            np.float32,
            copy=False,
        )

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int):
        return (
            self.texts[index],
            self.targets[index],
            self.identity_targets[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts) -> None:
        self.texts = list(texts)

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int) -> str:
        return self.texts[index]


def training_collate(batch):
    texts, targets, identity_targets = zip(*batch)

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "targets": torch.tensor(np.asarray(targets), dtype=torch.float32),
        "identity_targets": torch.tensor(
            np.asarray(identity_targets),
            dtype=torch.float32,
        ),
    }


def inference_collate(batch):
    encoded = tokenizer(
        list(batch),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
    }


@torch.inference_mode()
def predict_processed_rows(
    frame: pd.DataFrame,
    positional_indices: np.ndarray,
) -> np.ndarray:
    positional_indices = np.asarray(positional_indices, dtype=np.int64)

    if positional_indices.ndim != 1:
        raise ValueError("Prediction indices must be a one-dimensional array.")
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    selected_texts = (
        frame.iloc[positional_indices]["model_text"].fillna("").astype(str).tolist()
    )

    inference_dataset = ToxicityInferenceDataset(selected_texts)
    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=inference_collate,
    )

    was_training = fair_model.training
    fair_model.eval()
    prediction_chunks = []

    for batch in inference_loader:
        input_ids = batch["input_ids"].to(device, non_blocking=PIN_MEMORY)
        attention_mask = batch["attention_mask"].to(device, non_blocking=PIN_MEMORY)

        with torch.cuda.amp.autocast(enabled=device.type == "cuda"):
            model_outputs = fair_model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                adversarial_coefficient=0.0,
            )
            probabilities = torch.sigmoid(model_outputs["toxicity_logits"])

        prediction_chunks.append(probabilities.float().cpu().numpy())

    fair_model.train(was_training)

    predictions = np.concatenate(prediction_chunks).astype(np.float64, copy=False)
    return np.clip(predictions, 1e-7, 1.0 - 1e-7)


def predict_validation(positional_indices: np.ndarray) -> np.ndarray:
    return predict_processed_rows(valid_df, positional_indices)


def predict_test(positional_indices: np.ndarray) -> np.ndarray:
    return predict_processed_rows(test_df, positional_indices)


def save_checkpoint(directory) -> None:
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": fair_model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
        },
        checkpoint_dir / "fair_deberta_checkpoint.pt",
    )

    fair_model.encoder.config.to_json_file(str(checkpoint_dir / "encoder_config.json"))
    tokenizer.save_pretrained(str(checkpoint_dir / "tokenizer"))

    checkpoint_metadata = {
        "architecture": "FairDebertaToxicityModel",
        "model_id": MODEL_ID,
        "max_sequence_length": int(MAX_SEQUENCE_LENGTH),
        "text_column": "model_text",
        "identity_columns": list(IDENTITY_COLUMNS),
        "identity_adversary_enabled": False,
        "model_training_mode": bool(fair_model.training),
    }

    with open(
        checkpoint_dir / "inference_config.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(checkpoint_metadata, file, indent=2)

    manifest_path = feature_dir / "feature_manifest.json"
    if manifest_path.exists():
        shutil.copy2(manifest_path, checkpoint_dir / "feature_manifest.json")


def load_checkpoint(directory) -> None:
    checkpoint_dir = Path(directory)
    checkpoint_path = checkpoint_dir / "fair_deberta_checkpoint.pt"

    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

    checkpoint = torch.load(checkpoint_path, map_location=device)
    fair_model.load_state_dict(checkpoint["model_state_dict"], strict=True)

    if "optimizer_state_dict" in checkpoint:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

        for optimizer_state in optimizer.state.values():
            for key, value in optimizer_state.items():
                if torch.is_tensor(value):
                    optimizer_state[key] = value.to(device)

    metadata_path = checkpoint_dir / "inference_config.json"
    training_mode = True

    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as file:
            metadata = json.load(file)

        if int(metadata["max_sequence_length"]) != int(MAX_SEQUENCE_LENGTH):
            raise RuntimeError("Checkpoint sequence length differs from active model.")

        training_mode = bool(metadata.get("model_training_mode", True))

    fair_model.train(training_mode)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

train_dataset = ToxicityTrainingDataset(train_df)
train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=NUM_WORKERS > 0,
    collate_fn=training_collate,
    generator=torch.Generator().manual_seed(2027),
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=device.type == "cuda")
optimizer.zero_grad(set_to_none=True)

session.start_training(train_df["id"].astype(str).tolist())

stop_training = False
optimizer_updates = 0

for _epoch in range(MAX_EPOCHS):
    if stop_training:
        break

    fair_model.train()
    accumulated_batches = 0
    running_bce_loss = 0.0
    running_mmd_loss = 0.0
    running_active_mmd_cells = 0.0
    logged_batches = 0

    for batch_index, batch in enumerate(train_loader):
        input_ids = batch["input_ids"].to(device, non_blocking=PIN_MEMORY)
        attention_mask = batch["attention_mask"].to(device, non_blocking=PIN_MEMORY)
        toxicity_targets = batch["targets"].to(device, non_blocking=PIN_MEMORY)
        identity_targets = batch["identity_targets"].to(device, non_blocking=PIN_MEMORY)

        adversarial_coefficient = 0.0

        with torch.cuda.amp.autocast(enabled=device.type == "cuda"):
            model_outputs = fair_model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                adversarial_coefficient=adversarial_coefficient,
            )

            loss_components = criterion(
                model_outputs=model_outputs,
                toxicity_targets=toxicity_targets,
                identity_targets=identity_targets,
            )

            scaled_loss = loss_components["loss"] / GRADIENT_ACCUMULATION_STEPS

        running_bce_loss += float(loss_components["toxicity_loss"].item())
        running_mmd_loss += float(loss_components["mmd_loss"].item())
        running_active_mmd_cells += float(
            loss_components["active_mmd_cells"].item()
        )
        logged_batches += 1

        amp_scaler.scale(scaled_loss).backward()
        accumulated_batches += 1

        is_accumulation_boundary = (
            accumulated_batches >= GRADIENT_ACCUMULATION_STEPS
            or batch_index + 1 == len(train_loader)
        )

        if not is_accumulation_boundary:
            continue

        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(fair_model.parameters(), max_norm=1.0)

        previous_scale = amp_scaler.get_scale()
        amp_scaler.step(optimizer)
        amp_scaler.update()
        step_executed = amp_scaler.get_scale() >= previous_scale

        optimizer.zero_grad(set_to_none=True)
        accumulated_batches = 0

        if step_executed:
            optimizer_updates += 1
            stop_training = session.step()

            if stop_training:
                break

    if logged_batches:
        print(
            "Epoch diagnostics: "
            f"BCE={running_bce_loss / logged_batches:.6f}, "
            f"MMD={running_mmd_loss / logged_batches:.6f}, "
            f"active_identity_label_cells="
            f"{running_active_mmd_cells / logged_batches:.2f}"
        )

del train_loader

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")