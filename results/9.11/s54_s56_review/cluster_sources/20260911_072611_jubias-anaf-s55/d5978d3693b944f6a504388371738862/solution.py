import html
import json
import os
import pickle
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
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


# The runtime-owned split is created before any cleaning, scaling, or weight estimation.
session = CandidateSession.from_env()

input_dir = Path("./input")
working_dir = Path("./working")
working_dir.mkdir(parents=True, exist_ok=True)

identity_columns = [
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

train_header = pd.read_csv(input_dir / "train.csv", nrows=0)
required_train_columns = ["id", "target", "comment_text"] + identity_columns
missing_columns = sorted(set(required_train_columns) - set(train_header.columns))
if missing_columns:
    raise ValueError(f"train.csv is missing required columns: {missing_columns}")

train_dtypes = {
    "id": "int64",
    "target": "float32",
    **{column: "float32" for column in identity_columns},
}

train_raw = pd.read_csv(
    input_dir / "train.csv",
    usecols=required_train_columns,
    dtype=train_dtypes,
    low_memory=False,
)

test_raw = pd.read_csv(
    input_dir / "test.csv",
    usecols=["id", "comment_text"],
    dtype={"id": "int64"},
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_raw, test_raw)

# Positional indices used by runtime prediction callbacks must map directly to these rows.
train_df = train_df.reset_index(drop=True)
valid_df = valid_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)
del train_raw, test_raw


def normalize_comment_text(text_series: pd.Series) -> pd.Series:
    """Preserve toxicity-relevant wording/casing while normalizing noisy web text."""
    text = text_series.fillna("").astype(str).map(html.unescape)
    text = text.str.normalize("NFKC")
    text = text.str.replace(
        r"(?i)\b(?:https?://|www\.)[^\s<>]+",
        " urltoken ",
        regex=True,
    )
    text = text.str.replace(
        r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        " emailtoken ",
        regex=True,
    )
    text = text.str.replace(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", regex=True)
    text = text.str.replace(r"[\r\n\t]+", " ", regex=True)
    text = text.str.replace(r"\s+", " ", regex=True).str.strip()
    return text


raw_text_feature_columns = [
    "log_character_count",
    "log_word_count",
    "uppercase_ratio",
    "exclamation_count",
    "question_count",
    "all_caps_token_count",
    "url_marker_count",
]


def add_text_features(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()
    frame["model_text"] = normalize_comment_text(frame["comment_text"])

    cleaned = frame["model_text"]
    character_count = cleaned.str.len().astype(np.float32)
    word_count = cleaned.str.count(r"\S+").astype(np.float32)
    letter_count = cleaned.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = cleaned.str.count(r"[A-Z]").astype(np.float32)

    frame["log_character_count"] = np.log1p(character_count).astype(np.float32)
    frame["log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["uppercase_ratio"] = (uppercase_count / np.maximum(letter_count, 1.0)).astype(
        np.float32
    )
    frame["exclamation_count"] = np.log1p(
        cleaned.str.count("!").astype(np.float32)
    ).astype(np.float32)
    frame["question_count"] = np.log1p(
        cleaned.str.count(r"\?").astype(np.float32)
    ).astype(np.float32)
    frame["all_caps_token_count"] = np.log1p(
        cleaned.str.count(r"\b[A-Z]{2,}\b").astype(np.float32)
    ).astype(np.float32)
    frame["url_marker_count"] = cleaned.str.count(r"\burltoken\b").astype(np.float32)
    return frame


train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

# Fit stateful numeric transformations only on the training partition.
text_feature_scaler = StandardScaler()
train_scaled_features = text_feature_scaler.fit_transform(
    train_df[raw_text_feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)
valid_scaled_features = text_feature_scaler.transform(
    valid_df[raw_text_feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)
test_scaled_features = text_feature_scaler.transform(
    test_df[raw_text_feature_columns].to_numpy(dtype=np.float32)
).astype(np.float32)

scaled_text_feature_columns = [f"{column}_z" for column in raw_text_feature_columns]
for column_index, column_name in enumerate(scaled_text_feature_columns):
    train_df[column_name] = train_scaled_features[:, column_index]
    valid_df[column_name] = valid_scaled_features[:, column_index]
    test_df[column_name] = test_scaled_features[:, column_index]

# Labels and identity indicators are retained only for training weights and validation fairness.
for frame in (train_df, valid_df):
    frame["target"] = pd.to_numeric(frame["target"], errors="coerce").fillna(0.0)
    frame["target"] = frame["target"].clip(0.0, 1.0).astype(np.float32)
    frame["target_binary"] = (frame["target"] >= 0.5).astype(np.int8)

    for identity_column in identity_columns:
        values = pd.to_numeric(frame[identity_column], errors="coerce").fillna(0.0)
        frame[identity_column] = values.clip(0.0, 1.0).astype(np.float32)
        frame[f"{identity_column}_binary"] = (frame[identity_column] >= 0.5).astype(
            np.int8
        )

# Train-only inverse-prevalence weighting of identity-membership × toxicity strata.
train_targets = train_df["target_binary"].to_numpy(dtype=np.int8)
sample_weight = np.ones(len(train_df), dtype=np.float32)
stratum_weights = {}
reference_count = max(len(train_df) / 4.0, 1.0)

for identity_column in identity_columns:
    subgroup_mask = train_df[f"{identity_column}_binary"].to_numpy(dtype=bool)

    for binary_target in (0, 1):
        stratum_mask = subgroup_mask & (train_targets == binary_target)
        stratum_count = int(stratum_mask.sum())

        if stratum_count == 0:
            stratum_weights[f"{identity_column}|{binary_target}"] = 1.0
            continue

        inverse_prevalence_weight = float(
            np.sqrt(reference_count / float(stratum_count))
        )
        clipped_weight = float(np.clip(inverse_prevalence_weight, 1.0, 6.0))
        stratum_weights[f"{identity_column}|{binary_target}"] = clipped_weight
        sample_weight[stratum_mask] = np.maximum(
            sample_weight[stratum_mask],
            clipped_weight,
        )

train_df["fairness_sample_weight"] = sample_weight.astype(np.float32)

model_input_columns = ["model_text"] + scaled_text_feature_columns
preprocessing_artifacts = {
    "identity_columns": identity_columns,
    "model_input_columns": model_input_columns,
    "raw_text_feature_columns": raw_text_feature_columns,
    "scaled_text_feature_columns": scaled_text_feature_columns,
    "text_feature_scaler": text_feature_scaler,
    "stratum_weights": stratum_weights,
    "text_normalization": {
        "unicode_normalization": "NFKC",
        "url_token": "urltoken",
        "email_token": "emailtoken",
        "preserve_case": True,
    },
}

with open(working_dir / "preprocessing_artifacts.pkl", "wb") as artifact_file:
    pickle.dump(
        preprocessing_artifacts,
        artifact_file,
        protocol=pickle.HIGHEST_PROTOCOL,
    )

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

if torch.cuda.is_available():
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True


# ModernBERT large single-logit toxicity classifier.
model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model_config = AutoConfig.from_pretrained(
    model_id,
    num_labels=1,
)
model_config.problem_type = "regression"
model_config.classifier_dropout = 0.10

model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    config=model_config,
    ignore_mismatched_sizes=True,
)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

max_sequence_length = 256
amp_enabled = device.type == "cuda"
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


def fairness_weighted_soft_bce_loss(
    logits: torch.Tensor,
    targets: torch.Tensor,
    sample_weights: torch.Tensor = None,
) -> torch.Tensor:
    logits = logits.reshape(-1)
    targets = targets.reshape(-1).to(dtype=logits.dtype).clamp_(0.0, 1.0)

    per_example_loss = F.binary_cross_entropy_with_logits(
        logits,
        targets,
        reduction="none",
    )

    if sample_weights is None:
        return per_example_loss.mean()

    sample_weights = sample_weights.reshape(-1).to(
        device=logits.device,
        dtype=logits.dtype,
    )
    sample_weights = sample_weights.clamp_min(0.0)

    return (per_example_loss * sample_weights).sum() / sample_weights.sum().clamp_min(
        torch.finfo(logits.dtype).eps
    )


criterion = fairness_weighted_soft_bce_loss


def logits_to_probabilities(logits: torch.Tensor) -> torch.Tensor:
    return torch.sigmoid(logits.reshape(-1))


no_decay_terms = ("bias", "norm.weight", "layernorm.weight")
head_prefixes = ("head.", "classifier.", "score.")

optimizer_groups = {
    "encoder_decay": [],
    "encoder_no_decay": [],
    "head_decay": [],
    "head_no_decay": [],
}

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    normalized_name = parameter_name.lower()
    is_head = parameter_name.startswith(head_prefixes)
    has_no_decay = any(term in normalized_name for term in no_decay_terms)

    if is_head and has_no_decay:
        optimizer_groups["head_no_decay"].append(parameter)
    elif is_head:
        optimizer_groups["head_decay"].append(parameter)
    elif has_no_decay:
        optimizer_groups["encoder_no_decay"].append(parameter)
    else:
        optimizer_groups["encoder_decay"].append(parameter)

if not optimizer_groups["head_decay"] and not optimizer_groups["head_no_decay"]:
    raise RuntimeError("ModernBERT classification head parameters were not identified.")

optimizer_parameter_groups = []
group_settings = (
    ("encoder_decay", 1.5e-5, 0.01),
    ("encoder_no_decay", 1.5e-5, 0.0),
    ("head_decay", 6.0e-5, 0.01),
    ("head_no_decay", 6.0e-5, 0.0),
)

for group_name, learning_rate, weight_decay in group_settings:
    parameters = optimizer_groups[group_name]
    if parameters:
        optimizer_parameter_groups.append(
            {
                "params": parameters,
                "lr": learning_rate,
                "weight_decay": weight_decay,
            }
        )

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

train_texts = train_df["model_text"].fillna("").astype(str).to_numpy()
valid_texts = valid_df["model_text"].fillna("").astype(str).to_numpy()
test_texts = test_df["model_text"].fillna("").astype(str).to_numpy()

train_targets_array = train_df["target"].to_numpy(dtype=np.float32)
train_weights_array = train_df["fairness_sample_weight"].to_numpy(dtype=np.float32)

num_workers = max(2, min(4, os.cpu_count() or 2))
train_batch_size = 8 if device.type == "cuda" else 2
inference_batch_size = 32 if device.type == "cuda" else 8
gradient_accumulation_steps = 4 if device.type == "cuda" else 1
max_epochs = 2


class WeightedTextDataset(Dataset):
    def __init__(self, texts, targets, weights):
        self.texts = texts
        self.targets = targets
        self.weights = weights

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.targets[index],
            self.weights[index],
        )


class IndexedTextDataset(Dataset):
    def __init__(self, texts, positional_indices):
        self.texts = texts
        self.positional_indices = positional_indices

    def __len__(self):
        return len(self.positional_indices)

    def __getitem__(self, index):
        return self.texts[int(self.positional_indices[index])]


class TrainTextCollator:
    def __call__(self, batch):
        texts, targets, weights = zip(*batch)
        encoded = tokenizer(
            list(texts),
            truncation=True,
            max_length=max_sequence_length,
            padding=True,
            pad_to_multiple_of=8 if device.type == "cuda" else None,
            return_tensors="pt",
            return_token_type_ids=False,
        )
        return (
            dict(encoded),
            torch.as_tensor(targets, dtype=torch.float32),
            torch.as_tensor(weights, dtype=torch.float32),
        )


class InferenceTextCollator:
    def __call__(self, texts):
        encoded = tokenizer(
            list(texts),
            truncation=True,
            max_length=max_sequence_length,
            padding=True,
            pad_to_multiple_of=8 if device.type == "cuda" else None,
            return_tensors="pt",
            return_token_type_ids=False,
        )
        return dict(encoded)


train_dataset = WeightedTextDataset(
    train_texts,
    train_targets_array,
    train_weights_array,
)
train_collator = TrainTextCollator()
inference_collator = InferenceTextCollator()


def _move_model_inputs_to_device(model_inputs):
    return {
        key: value.to(device, non_blocking=True)
        for key, value in model_inputs.items()
        if key in ("input_ids", "attention_mask", "position_ids")
    }


def _predict_from_texts(texts, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(texts):
        raise IndexError(
            "Runtime supplied an out-of-range positional prediction index."
        )

    dataset = IndexedTextDataset(texts, positional_indices)
    loader = DataLoader(
        dataset,
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=(device.type == "cuda"),
        persistent_workers=False,
        collate_fn=inference_collator,
    )

    was_training = model.training
    model.eval()
    prediction_batches = []

    try:
        with torch.inference_mode():
            for model_inputs in loader:
                model_inputs = _move_model_inputs_to_device(model_inputs)
                with torch.cuda.amp.autocast(enabled=amp_enabled):
                    logits = model(**model_inputs).logits
                    probabilities = logits_to_probabilities(logits)

                prediction_batches.append(probabilities.detach().float().cpu().numpy())
    finally:
        model.train(was_training)

    predictions = np.concatenate(prediction_batches).astype(np.float64, copy=False)

    if predictions.shape[0] != positional_indices.shape[0]:
        raise RuntimeError(
            "Prediction count does not match requested positional indices."
        )
    if not np.isfinite(predictions).all():
        raise FloatingPointError("Non-finite model probabilities encountered.")

    return np.clip(predictions, 0.0, 1.0)


def predict_validation(positional_indices):
    return _predict_from_texts(valid_texts, positional_indices)


def predict_test(positional_indices):
    return _predict_from_texts(test_texts, positional_indices)


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": int(max_sequence_length),
            "prediction_transform": "sigmoid",
        },
        checkpoint_dir / "model_state.pt",
    )
    model.config.save_pretrained(checkpoint_dir / "model_config")
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    preprocessing_source = working_dir / "preprocessing_artifacts.pkl"
    if preprocessing_source.exists():
        shutil.copy2(
            preprocessing_source,
            checkpoint_dir / "preprocessing_artifacts.pkl",
        )

    with open(checkpoint_dir / "inference_state.json", "w", encoding="utf-8") as file:
        json.dump(
            {
                "max_sequence_length": int(max_sequence_length),
                "prediction_transform": "sigmoid",
                "text_column": "model_text",
                "uses_numeric_features": False,
            },
            file,
            indent=2,
            sort_keys=True,
        )


def load_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_payload = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=device,
    )

    if int(checkpoint_payload["max_sequence_length"]) != int(max_sequence_length):
        raise RuntimeError("Checkpoint tokenizer sequence length is incompatible.")

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
stop_training = False
completed_optimizer_updates = 0

for epoch_index in range(max_epochs):
    generator = torch.Generator()
    generator.manual_seed(2029 + epoch_index)

    train_loader = DataLoader(
        train_dataset,
        batch_size=train_batch_size,
        shuffle=True,
        generator=generator,
        num_workers=num_workers,
        pin_memory=(device.type == "cuda"),
        persistent_workers=False,
        collate_fn=train_collator,
        drop_last=False,
    )

    model.train()
    accumulated_microbatches = 0
    epoch_loss_sum = 0.0
    epoch_loss_batches = 0
    epoch_updates = 0

    for model_inputs, targets, sample_weights in train_loader:
        model_inputs = _move_model_inputs_to_device(model_inputs)
        targets = targets.to(device, non_blocking=True)
        sample_weights = sample_weights.to(device, non_blocking=True)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            logits = model(**model_inputs).logits
            raw_loss = criterion(logits, targets, sample_weights)
            scaled_loss = raw_loss / gradient_accumulation_steps

        if not torch.isfinite(raw_loss):
            raise FloatingPointError("Encountered a non-finite training loss.")

        grad_scaler.scale(scaled_loss).backward()
        accumulated_microbatches += 1
        epoch_loss_sum += float(raw_loss.detach().cpu())
        epoch_loss_batches += 1

        if accumulated_microbatches < gradient_accumulation_steps:
            continue

        grad_scaler.unscale_(optimizer)
        clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        accumulated_microbatches = 0
        completed_optimizer_updates += 1
        epoch_updates += 1

        stop_training = session.step()
        if stop_training:
            break

    if not stop_training and accumulated_microbatches > 0:
        grad_scaler.unscale_(optimizer)
        clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        completed_optimizer_updates += 1
        epoch_updates += 1
        stop_training = session.step()

    mean_epoch_loss = epoch_loss_sum / max(epoch_loss_batches, 1)
    print(
        f"epoch={epoch_index + 1} updates={epoch_updates} "
        f"loss={mean_epoch_loss:.6f}"
    )

    if stop_training:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
