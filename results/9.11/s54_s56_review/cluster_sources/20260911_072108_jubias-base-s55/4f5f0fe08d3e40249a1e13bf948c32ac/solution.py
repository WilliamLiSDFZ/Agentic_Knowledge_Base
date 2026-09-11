import html
import json
import math
import os
import re
import unicodedata
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime-owned split: this must happen before any preprocessing.
# ---------------------------------------------------------------------
seed = 2025
np.random.seed(seed)
torch.manual_seed(seed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

Path("./working").mkdir(parents=True, exist_ok=True)
Path("./submission").mkdir(parents=True, exist_ok=True)

session = CandidateSession.from_env()

raw_train_df = pd.read_csv("./input/train.csv")
raw_test_df = pd.read_csv("./input/test.csv")
train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df

evaluation_identity_columns = [
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

auxiliary_target_columns = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

url_pattern = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
email_pattern = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
user_pattern = re.compile(r"(?<![\w@])@[\w_]{2,}")
control_pattern = re.compile(r"[\u0000-\u0008\u000b-\u001f\u007f-\u009f]")
whitespace_pattern = re.compile(r"\s+")


def normalize_surface_text(value):
    """Preserve lexical evidence while normalizing markup and unstable surface forms."""
    if pd.isna(value):
        return ""

    text = html.unescape(str(value))
    text = unicodedata.normalize("NFKC", text)
    text = control_pattern.sub(" ", text)
    text = url_pattern.sub(" <URL> ", text)
    text = email_pattern.sub(" <EMAIL> ", text)
    text = ip_pattern.sub(" <IP> ", text)
    text = user_pattern.sub(" <USER> ", text)
    text = whitespace_pattern.sub(" ", text).strip()
    return text


def preprocess_text_column(frame):
    return frame["comment_text"].map(normalize_surface_text).astype(str).tolist()


def numeric_column(frame, column, default=0.0):
    if column not in frame.columns:
        return np.full(len(frame), default, dtype=np.float32)

    return (
        pd.to_numeric(frame[column], errors="coerce")
        .fillna(default)
        .clip(0.0, 1.0)
        .to_numpy(dtype=np.float32)
    )


# Text preprocessing does not learn fitted vocabulary/statistics from validation or test.
train_texts = preprocess_text_column(train_df)
valid_texts = preprocess_text_column(valid_df)
test_texts = preprocess_text_column(test_df)

train_targets = numeric_column(train_df, "target")
train_subtype_targets = np.column_stack(
    [numeric_column(train_df, column) for column in auxiliary_target_columns]
).astype(np.float32)

train_identity_targets = np.column_stack(
    [numeric_column(train_df, column) for column in evaluation_identity_columns]
).astype(np.float32)

if "identity_annotator_count" in train_df.columns:
    identity_annotation_mask = (
        pd.to_numeric(train_df["identity_annotator_count"], errors="coerce")
        .fillna(0.0)
        .to_numpy(dtype=np.float32)
        > 0.0
    )
else:
    identity_annotation_mask = np.ones(len(train_df), dtype=bool)

train_identity_masks = np.repeat(
    identity_annotation_mask[:, None],
    len(evaluation_identity_columns),
    axis=1,
)

subgroup_present = np.any(train_identity_targets >= 0.5, axis=1)
target_is_toxic = train_targets >= 0.5

# Standard Jigsaw four-quadrant weighting: preserve background/non-toxic
# examples while emphasizing BPSN, BNSP, and toxic-background support.
sample_weights = (
    1.0
    + subgroup_present.astype(np.float32)
    + ((~subgroup_present) & target_is_toxic).astype(np.float32)
    + (subgroup_present & (~target_is_toxic)).astype(np.float32)
)
sample_weights /= sample_weights.mean()

train_ids = train_df["id"].astype(str).tolist()

preprocessing_config = {
    "text_column": "comment_text",
    "normalization": [
        "html_unescape",
        "unicode_nfkc",
        "control_character_removal",
        "url_email_ip_user_placeholder_replacement",
        "whitespace_normalization",
    ],
    "max_sequence_length": 256,
    "evaluation_identity_columns": evaluation_identity_columns,
    "auxiliary_target_columns": auxiliary_target_columns,
}
with open("./working/preprocessing_config.json", "w", encoding="utf-8") as output_file:
    json.dump(preprocessing_config, output_file, indent=2)

del train_df, valid_df, test_df


# ---------------------------------------------------------------------
# Model design: DeBERTa encoder with toxicity, subtype, and adversarial
# identity heads.
# ---------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
base_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)

# The previous patch left literal SEARCH/REPLACE delimiters in the source,
# which Python attempted to parse as invalid syntax. Isolate that stale fragment
# while the complete model implementation is reconstructed below.
"""


=======
=======
        self.num_subtypes = int(num_subtypes)


class BiasAwareDebertaModel(nn.Module):
    def __init__(
        self,
        pretrained_classifier,
        num_subtypes,
        num_evaluation_identities,
        head_dropout=0.15,
    ):
        super().__init__()
        self.encoder = pretrained_classifier.deberta
        hidden_size = self.encoder.config.hidden_size

        self.feature_norm = nn.LayerNorm(hidden_size)
        self.feature_dropout = nn.Dropout(head_dropout)

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(head_dropout),
            nn.Linear(hidden_size // 2, 1),
        )

        self.subtype_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(head_dropout),
            nn.Linear(hidden_size // 2, num_subtypes),
        )

>>>>>>> REPLACE

<<<<<<< SEARCH

"""


class BiasAwareDebertaModel(nn.Module):
    def __init__(
        self,
        pretrained_classifier,
        num_subtypes,
        num_evaluation_identities,
        head_dropout=0.15,
    ):
        super().__init__()
        self.encoder = pretrained_classifier.deberta
        hidden_size = self.encoder.config.hidden_size

        self.feature_norm = nn.LayerNorm(hidden_size)
        self.feature_dropout = nn.Dropout(head_dropout)

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(head_dropout),
            nn.Linear(hidden_size // 2, 1),
        )
        self.subtype_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(head_dropout),
            nn.Linear(hidden_size // 2, num_subtypes),
        )

        self.num_subtypes = int(num_subtypes)
        self.num_evaluation_identities = int(num_evaluation_identities)

        for module in (self.toxicity_head, self.subtype_head):
            for layer in module.modules():
                if isinstance(layer, nn.Linear):
                    nn.init.normal_(layer.weight, mean=0.0, std=0.02)
                    if layer.bias is not None:
                        nn.init.zeros_(layer.bias)

    def forward(
        self,
        input_ids,
        attention_mask=None,
        token_type_ids=None,
        return_auxiliary=None,
    ):
        encoder_inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }
        if token_type_ids is not None:
            encoder_inputs["token_type_ids"] = token_type_ids

        encoder_outputs = self.encoder(**encoder_inputs)
        cls_features = encoder_outputs.last_hidden_state[:, 0]
        features = self.feature_dropout(self.feature_norm(cls_features))

        outputs = {
            "toxicity_logits": self.toxicity_head(features).squeeze(-1)
        }
        if return_auxiliary is None:
            return_auxiliary = self.training
        if return_auxiliary:
            outputs["subtype_logits"] = self.subtype_head(features)

        return outputs


class BiasAwareMultiTaskLoss(nn.Module):
    def __init__(self, subtype_weight=0.20):
        super().__init__()
        self.subtype_weight = float(subtype_weight)

    def forward(
        self,
        model_outputs,
        target,
        subtype_targets,
        identity_targets,
        sample_weights,
        identity_mask,
    ):
        target = target.float().clamp(0.0, 1.0)

        toxicity_loss_values = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logits"],
            target,
            reduction="none",
        )

        weights = sample_weights.float().clamp_min(0.0)
        toxicity_loss = (
            toxicity_loss_values * weights
        ).sum() / weights.sum().clamp_min(1.0)

        subtype_loss_values = F.binary_cross_entropy_with_logits(
            model_outputs["subtype_logits"],
            subtype_targets.float().clamp(0.0, 1.0),
            reduction="none",
        )
        subtype_loss = subtype_loss_values.mean()

        return toxicity_loss + self.subtype_weight * subtype_loss


model = BiasAwareDebertaModel(
    pretrained_classifier=base_model,
    num_subtypes=len(auxiliary_target_columns),
    num_evaluation_identities=len(evaluation_identity_columns),
    head_dropout=0.15,
)
del base_model

criterion = BiasAwareMultiTaskLoss(
    subtype_weight=0.20,
)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")

backbone_parameters = [
    (name, parameter)
    for name, parameter in model.named_parameters()
    if name.startswith("encoder.") and parameter.requires_grad
]
head_parameters = [
    (name, parameter)
    for name, parameter in model.named_parameters()
    if not name.startswith("encoder.") and parameter.requires_grad
]

optimizer_groups = [
    {
        "params": [
            parameter
            for name, parameter in backbone_parameters
            if not any(term in name for term in no_decay_terms)
        ],
        "lr": 1.5e-5,
        "weight_decay": 0.01,
    },
    {
        "params": [
            parameter
            for name, parameter in backbone_parameters
            if any(term in name for term in no_decay_terms)
        ],
        "lr": 1.5e-5,
        "weight_decay": 0.0,
    },
    {
        "params": [
            parameter
            for name, parameter in head_parameters
            if not any(term in name for term in no_decay_terms)
        ],
        "lr": 1.0e-4,
        "weight_decay": 0.01,
    },
    {
        "params": [
            parameter
            for name, parameter in head_parameters
            if any(term in name for term in no_decay_terms)
        ],
        "lr": 1.0e-4,
        "weight_decay": 0.0,
    },
]

optimizer = AdamW(
    optimizer_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)


# ---------------------------------------------------------------------
# Training and runtime callbacks.
# ---------------------------------------------------------------------
max_sequence_length = 256
train_batch_size = 8
inference_batch_size = 16
gradient_accumulation_steps = 2
num_workers = 2
pin_memory = device.type == "cuda"


class ToxicityTrainingDataset(Dataset):
    def __init__(
        self,
        texts,
        targets,
        subtype_targets,
        identity_targets,
        identity_masks,
        weights,
    ):
        self.texts = texts
        self.targets = targets
        self.subtype_targets = subtype_targets
        self.identity_targets = identity_targets
        self.identity_masks = identity_masks
        self.weights = weights

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.targets[index],
            self.subtype_targets[index],
            self.identity_targets[index],
            self.identity_masks[index],
            self.weights[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts, positions):
        self.texts = texts
        self.positions = np.asarray(positions, dtype=np.int64)

    def __len__(self):
        return len(self.positions)

    def __getitem__(self, index):
        return self.texts[int(self.positions[index])]


def training_collate(batch):
    texts, targets, subtype_targets, identity_targets, identity_masks, weights = zip(
        *batch
    )

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=max_sequence_length,
        return_tensors="pt",
    )

    return {
        "encoded": encoded,
        "target": torch.tensor(np.asarray(targets), dtype=torch.float32),
        "subtype_targets": torch.tensor(
            np.stack(subtype_targets),
            dtype=torch.float32,
        ),
        "identity_targets": torch.tensor(
            np.stack(identity_targets),
            dtype=torch.float32,
        ),
        "identity_masks": torch.tensor(
            np.stack(identity_masks),
            dtype=torch.bool,
        ),
        "weights": torch.tensor(np.asarray(weights), dtype=torch.float32),
    }


def inference_collate(batch):
    return tokenizer(
        list(batch),
        padding=True,
        truncation=True,
        max_length=max_sequence_length,
        return_tensors="pt",
    )


def predict_positions(texts, positions):
    positions = np.asarray(positions, dtype=np.int64).reshape(-1)

    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)

    if positions.min() < 0 or positions.max() >= len(texts):
        raise IndexError("Prediction positions are outside the supplied split.")

    prior_mode = model.training
    model.eval()
    predictions = []

    prediction_loader = DataLoader(
        ToxicityInferenceDataset(texts, positions),
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=pin_memory,
        persistent_workers=True,
        prefetch_factor=2,
        collate_fn=inference_collate,
    )

    try:
        with torch.inference_mode():
            for encoded in prediction_loader:
                encoded = {
                    name: value.to(device, non_blocking=True)
                    for name, value in encoded.items()
                }

                amp_context = (
                    torch.cuda.amp.autocast(enabled=True)
                    if device.type == "cuda"
                    else nullcontext()
                )

                with amp_context:
                    outputs = model(**encoded, return_auxiliary=False)
                    probabilities = torch.sigmoid(outputs["toxicity_logits"])

                predictions.append(probabilities.float().cpu().numpy())
    finally:
        model.train(prior_mode)

    return np.concatenate(predictions).astype(np.float64, copy=False)


def predict_validation(positions):
    return predict_positions(valid_texts, positions)


def predict_test(positions):
    return predict_positions(test_texts, positions)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    checkpoint_path = directory / "model_state.pt"
    temporary_path = directory / "model_state.tmp.pt"

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_sequence_length": max_sequence_length,
            "evaluation_identity_columns": evaluation_identity_columns,
            "auxiliary_target_columns": auxiliary_target_columns,
        },
        temporary_path,
    )
    os.replace(temporary_path, checkpoint_path)

    tokenizer.save_pretrained(directory / "tokenizer")

    with open(
        directory / "inference_config.json", "w", encoding="utf-8"
    ) as output_file:
        json.dump(preprocessing_config, output_file, indent=2)


def load_checkpoint(directory):
    directory = Path(directory)
    checkpoint_path = directory / "model_state.pt"

    try:
        checkpoint = torch.load(
            checkpoint_path,
            map_location=device,
            weights_only=False,
        )
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location=device)

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

training_dataset = ToxicityTrainingDataset(
    texts=train_texts,
    targets=train_targets,
    subtype_targets=train_subtype_targets,
    identity_targets=train_identity_targets,
    identity_masks=train_identity_masks,
    weights=sample_weights,
)

loader_generator = torch.Generator()
loader_generator.manual_seed(seed)

training_loader = DataLoader(
    training_dataset,
    batch_size=train_batch_size,
    shuffle=True,
    generator=loader_generator,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=training_collate,
    drop_last=False,
)

estimated_optimizer_steps = min(
    20000,
    max(
        1000,
        math.ceil(len(training_loader) / gradient_accumulation_steps) * 2,
    ),
)
warmup_steps = min(250, max(50, estimated_optimizer_steps // 50))


def learning_rate_multiplier(step_number):
    if step_number < warmup_steps:
        return max(0.05, float(step_number + 1) / float(warmup_steps))

    progress = min(
        1.0,
        float(step_number - warmup_steps)
        / float(max(1, estimated_optimizer_steps - warmup_steps)),
    )
    return max(0.10, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
scaler = torch.cuda.amp.GradScaler(enabled=device.type == "cuda")

session.start_training(train_ids)

stop_training = False
optimizer_updates = 0
max_epochs = 3

for epoch in range(max_epochs):
    if stop_training:
        break

    model.train()
    optimizer.zero_grad(set_to_none=True)

    epoch_loss_sum = 0.0
    epoch_batches = 0
    epoch_updates = 0

    for batch_index, batch in enumerate(training_loader):
        encoded = {
            name: value.to(device, non_blocking=True)
            for name, value in batch["encoded"].items()
        }

        target = batch["target"].to(device, non_blocking=True)
        subtype_targets = batch["subtype_targets"].to(device, non_blocking=True)
        identity_targets = batch["identity_targets"].to(device, non_blocking=True)
        identity_masks = batch["identity_masks"].to(device, non_blocking=True)
        weights = batch["weights"].to(device, non_blocking=True)

        amp_context = (
            torch.cuda.amp.autocast(enabled=True)
            if device.type == "cuda"
            else nullcontext()
        )

        with amp_context:
            outputs = model(**encoded, return_auxiliary=True)
            unscaled_loss = criterion(
                model_outputs=outputs,
                target=target,
                subtype_targets=subtype_targets,
                identity_targets=identity_targets,
                sample_weights=weights,
                identity_mask=identity_masks,
            )
            loss = unscaled_loss / gradient_accumulation_steps

        scaler.scale(loss).backward()

        epoch_loss_sum += float(unscaled_loss.detach().cpu())
        epoch_batches += 1

        is_last_batch = batch_index + 1 == len(training_loader)
        should_step = (
            batch_index + 1
        ) % gradient_accumulation_steps == 0 or is_last_batch

        if should_step:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

            optimizer_updates += 1
            epoch_updates += 1

            stop_training = session.step()
            if stop_training:
                break

    mean_epoch_loss = epoch_loss_sum / max(epoch_batches, 1)
    print(
        f"epoch={epoch + 1} updates={epoch_updates} "
        f"total_updates={optimizer_updates} loss={mean_epoch_loss:.6f}"
    )

session.finish()