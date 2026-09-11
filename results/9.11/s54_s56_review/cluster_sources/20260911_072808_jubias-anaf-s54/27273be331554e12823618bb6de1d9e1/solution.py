import html
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.nn.utils import clip_grad_norm_
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


INPUT_DIR = "./input"
WORKING_DIR = "./working/processed"
os.makedirs(WORKING_DIR, exist_ok=True)

session = CandidateSession.from_env()
CONTRACT_SEED = int(getattr(session, "seed", 0))
pairwise_generator = torch.Generator().manual_seed(CONTRACT_SEED)
training_loader_generator = torch.Generator().manual_seed(CONTRACT_SEED)

EVALUATION_IDENTITIES = [
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

NUM_BIAS_CELLS = 18
MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 32
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 3
NUM_WORKERS = 2
HEAD_WARMUP_UPDATES = 200
MAX_PAIRS_PER_COMPONENT = 32
PAIRWISE_LAMBDA = 0.05

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
USER_PATTERN = re.compile(r"(?<!\w)@[A-Za-z0-9_]{1,32}")
WHITESPACE_PATTERN = re.compile(r"\s+")


def clean_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = unicodedata.normalize("NFKC", html.unescape(text))
    text = URL_PATTERN.sub(" <url> ", text)
    text = EMAIL_PATTERN.sub(" <email> ", text)
    text = IP_PATTERN.sub(" <ip> ", text)
    text = USER_PATTERN.sub(" <user> ", text)
    return WHITESPACE_PATTERN.sub(" ", text).strip()


def build_text_features(clean_text):
    text = clean_text.astype("string").fillna("")
    alpha_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = text.str.count(r"[A-Z]").astype(np.float32)

    features = pd.DataFrame(
        {
            "log_char_count": np.log1p(text.str.len().astype(np.float32)),
            "log_word_count": np.log1p(text.str.count(r"\S+").astype(np.float32)),
            "log_unique_word_count": np.log1p(
                text.map(
                    lambda value: len(set(value.lower().split())) if value else 0
                ).astype(np.float32)
            ),
            "uppercase_fraction": (
                uppercase_count / np.maximum(alpha_count, 1.0)
            ).astype(np.float32),
            "exclamation_count": np.log1p(text.str.count("!").astype(np.float32)),
            "question_count": np.log1p(text.str.count(r"\?").astype(np.float32)),
            "quote_count": np.log1p(text.str.count(r"""["']""").astype(np.float32)),
            "newline_count": np.log1p(text.str.count("\n").astype(np.float32)),
            "url_count": np.log1p(text.str.count("<url>").astype(np.float32)),
            "repeated_punctuation_count": np.log1p(
                text.str.count(r"([!?.,])\1{2,}").astype(np.float32)
            ),
        }
    )
    return features.replace([np.inf, -np.inf], 0.0).fillna(0.0).astype(np.float32)


def safe_identity_values(frame):
    identity_values = pd.DataFrame(index=frame.index)

    for column in EVALUATION_IDENTITIES:
        if column in frame.columns:
            identity_values[column] = (
                pd.to_numeric(frame[column], errors="coerce")
                .fillna(0.0)
                .clip(0.0, 1.0)
                .astype(np.float32)
            )
        else:
            identity_values[column] = np.float32(0.0)

    return identity_values


def make_processed_frame(frame, include_labels):
    cleaned_text = frame["comment_text"].map(clean_comment)

    processed = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(),
            "comment_text": cleaned_text.to_numpy(),
            "feature_row": np.arange(len(frame), dtype=np.int64),
        }
    )

    if include_labels:
        target = (
            pd.to_numeric(frame["target"], errors="coerce")
            .fillna(0.0)
            .clip(0.0, 1.0)
            .astype(np.float32)
        )
        identities = safe_identity_values(frame)

        processed["target"] = target.to_numpy()
        processed["target_binary"] = (target.to_numpy() >= 0.5).astype(np.int8)

        for column in EVALUATION_IDENTITIES:
            processed[column] = identities[column].to_numpy()

        processed["identity_any"] = (
            (identities.to_numpy(dtype=np.float32) >= 0.5).any(axis=1)
        ).astype(np.int8)

    return processed, build_text_features(cleaned_text)


raw_train_df = pd.read_csv(os.path.join(INPUT_DIR, "train.csv"), low_memory=False)
raw_test_df = pd.read_csv(os.path.join(INPUT_DIR, "test.csv"), low_memory=False)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

train_processed, train_feature_frame = make_processed_frame(
    train_df, include_labels=True
)
valid_processed, valid_feature_frame = make_processed_frame(
    valid_df, include_labels=True
)
test_processed, test_feature_frame = make_processed_frame(test_df, include_labels=False)

feature_names = train_feature_frame.columns.tolist()
numeric_scaler = StandardScaler()

train_features = numeric_scaler.fit_transform(train_feature_frame).astype(np.float32)
valid_features = numeric_scaler.transform(valid_feature_frame).astype(np.float32)
test_features = numeric_scaler.transform(test_feature_frame).astype(np.float32)

train_identity_mask = (
    train_processed[EVALUATION_IDENTITIES].to_numpy(dtype=np.float32) >= 0.5
)
valid_identity_mask = (
    valid_processed[EVALUATION_IDENTITIES].to_numpy(dtype=np.float32) >= 0.5
)

train_positive = train_processed["target_binary"].to_numpy(dtype=bool)
valid_positive = valid_processed["target_binary"].to_numpy(dtype=bool)

train_identity_target_cells = np.concatenate(
    [
        train_identity_mask & train_positive[:, None],
        train_identity_mask & (~train_positive[:, None]),
    ],
    axis=1,
).astype(np.uint8)

valid_identity_target_cells = np.concatenate(
    [
        valid_identity_mask & valid_positive[:, None],
        valid_identity_mask & (~valid_positive[:, None]),
    ],
    axis=1,
).astype(np.uint8)

train_processed.to_pickle(os.path.join(WORKING_DIR, "train_processed.pkl"))
valid_processed.to_pickle(os.path.join(WORKING_DIR, "valid_processed.pkl"))
test_processed.to_pickle(os.path.join(WORKING_DIR, "test_processed.pkl"))

np.save(os.path.join(WORKING_DIR, "train_features.npy"), train_features)
np.save(os.path.join(WORKING_DIR, "valid_features.npy"), valid_features)
np.save(os.path.join(WORKING_DIR, "test_features.npy"), test_features)

np.savez_compressed(
    os.path.join(WORKING_DIR, "bias_groups.npz"),
    train_identity_mask=train_identity_mask.astype(np.uint8),
    valid_identity_mask=valid_identity_mask.astype(np.uint8),
    train_identity_target_cells=train_identity_target_cells,
    valid_identity_target_cells=valid_identity_target_cells,
    train_cell_counts=train_identity_target_cells.sum(axis=0),
)

joblib.dump(
    {
        "numeric_scaler": numeric_scaler,
        "feature_names": feature_names,
        "identity_columns": EVALUATION_IDENTITIES,
        "text_cleaning": {
            "unicode_normalization": "NFKC",
            "url_token": "<url>",
            "email_token": "<email>",
            "ip_token": "<ip>",
            "user_token": "<user>",
        },
    },
    os.path.join(WORKING_DIR, "preprocessing_state.joblib"),
)

with open(
    os.path.join(WORKING_DIR, "feature_manifest.json"),
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        {
            "feature_names": feature_names,
            "identity_columns": EVALUATION_IDENTITIES,
            "train_rows": int(len(train_processed)),
            "validation_rows": int(len(valid_processed)),
            "test_rows": int(len(test_processed)),
            "train_identity_target_cell_counts": train_identity_target_cells.sum(
                axis=0
            ).tolist(),
        },
        file,
        indent=2,
    )


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
pin_memory = device.type == "cuda"
amp_enabled = device.type == "cuda"

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

special_tokens = ["<url>", "<email>", "<ip>", "<user>"]
tokenizer.add_special_tokens({"additional_special_tokens": special_tokens})
model.resize_token_embeddings(len(tokenizer))

if hasattr(model, "gradient_checkpointing_enable"):
    model.gradient_checkpointing_enable()


class ToxicityRanker(nn.Module):
    def __init__(self, sequence_classifier):
        super().__init__()
        self.encoder = sequence_classifier

    def forward(self, input_ids, attention_mask=None):
        outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )
        class_logits = outputs.logits

        if class_logits.ndim == 1:
            return class_logits

        if class_logits.shape[-1] == 1:
            return class_logits.squeeze(-1)

        return class_logits[:, 1] - class_logits[:, 0]

    @torch.inference_mode()
    def predict_proba(self, input_ids, attention_mask=None):
        was_training = self.training
        self.eval()
        probabilities = torch.sigmoid(self(input_ids, attention_mask))
        if was_training:
            self.train()
        return probabilities


class DynamicBiasAwareBCELoss(nn.Module):
    def __init__(
        self,
        num_cells=NUM_BIAS_CELLS,
        ema_momentum=0.97,
        emphasis_power=1.5,
        min_weight=0.35,
        max_weight=3.0,
        epsilon=1e-6,
    ):
        super().__init__()
        self.num_cells = int(num_cells)
        self.ema_momentum = float(ema_momentum)
        self.emphasis_power = float(emphasis_power)
        self.min_weight = float(min_weight)
        self.max_weight = float(max_weight)
        self.epsilon = float(epsilon)

        self.register_buffer("cell_loss_ema", torch.ones(self.num_cells))
        self.register_buffer("cell_seen", torch.zeros(self.num_cells))
        self.register_buffer("cell_weights", torch.ones(self.num_cells))

    @torch.no_grad()
    def _refresh_weights(self):
        observed = self.cell_seen > 0

        if not torch.any(observed):
            self.cell_weights.fill_(1.0)
            return

        risks = self.cell_loss_ema.clone()
        reference_risk = risks[observed].mean().clamp_min(self.epsilon)
        relative_risk = (risks / reference_risk).clamp_min(self.epsilon)

        proposed_weights = relative_risk.pow(self.emphasis_power)
        proposed_weights = proposed_weights.clamp(self.min_weight, self.max_weight)

        proposed_weights = torch.where(
            observed,
            proposed_weights,
            torch.ones_like(proposed_weights),
        )
        self.cell_weights.copy_(proposed_weights)

    @torch.no_grad()
    def _update_cell_statistics(self, point_losses, memberships):
        memberships = memberships.to(dtype=torch.bool)

        for cell_index in range(self.num_cells):
            member_mask = memberships[:, cell_index]

            if member_mask.any():
                current_cell_loss = point_losses[member_mask].detach().mean()

                if self.cell_seen[cell_index] == 0:
                    self.cell_loss_ema[cell_index] = current_cell_loss
                else:
                    self.cell_loss_ema[cell_index].mul_(self.ema_momentum).add_(
                        current_cell_loss * (1.0 - self.ema_momentum)
                    )

                self.cell_seen[cell_index].add_(1.0)

        self._refresh_weights()

    def forward(self, logits, targets, cell_membership):
        if logits.ndim != 1:
            logits = logits.reshape(-1)

        targets = targets.to(dtype=logits.dtype).reshape(-1).clamp(0.0, 1.0)

        if cell_membership.ndim != 2 or cell_membership.shape[1] != self.num_cells:
            raise ValueError(
                f"cell_membership must have shape [batch, {self.num_cells}], "
                f"got {tuple(cell_membership.shape)}"
            )

        if cell_membership.shape[0] != logits.shape[0]:
            raise ValueError("logits and cell_membership batch dimensions must match")

        point_losses = F.binary_cross_entropy_with_logits(
            logits,
            targets,
            reduction="none",
        )

        memberships = cell_membership.to(
            device=logits.device,
            dtype=logits.dtype,
        )
        active_cells = memberships.sum(dim=1)

        identity_weight_sum = memberships @ self.cell_weights.to(
            device=logits.device,
            dtype=logits.dtype,
        )

        sample_weights = torch.where(
            active_cells > 0,
            identity_weight_sum / active_cells.clamp_min(1.0),
            torch.ones_like(active_cells),
        ).clamp(self.min_weight, self.max_weight)

        with torch.no_grad():
            self._update_cell_statistics(point_losses, memberships)

        return (point_losses * sample_weights).sum() / sample_weights.sum().clamp_min(
            self.epsilon
        )


class BiasAwarePairwiseRankingLoss(nn.Module):
    def __init__(
        self,
        max_pairs_per_component=MAX_PAIRS_PER_COMPONENT,
        generator=None,
    ):
        super().__init__()
        self.max_pairs_per_component = int(max_pairs_per_component)
        self.generator = generator if generator is not None else torch.Generator()

    def _sample_indices(self, candidate_indices, sample_count):
        sampled_positions = torch.randint(
            candidate_indices.numel(),
            (sample_count,),
            generator=self.generator,
        )
        return candidate_indices.index_select(
            0,
            sampled_positions.to(candidate_indices.device),
        )

    def forward(self, logits, targets, identity_masks):
        if logits.ndim != 1:
            logits = logits.reshape(-1)

        targets = targets.to(dtype=logits.dtype).reshape(-1).clamp(0.0, 1.0)

        if identity_masks.ndim != 2 or identity_masks.shape[1] != len(
            EVALUATION_IDENTITIES
        ):
            raise ValueError(
                "identity_masks must have shape "
                f"[batch, {len(EVALUATION_IDENTITIES)}], "
                f"got {tuple(identity_masks.shape)}"
            )

        if identity_masks.shape[0] != logits.shape[0]:
            raise ValueError("logits and identity_masks batch dimensions must match")

        identity_masks = identity_masks.to(device=logits.device, dtype=torch.bool)
        target_positive = targets >= 0.5
        component_losses = []

        def add_component(positive_mask, negative_mask):
            positive_indices = torch.nonzero(
                positive_mask,
                as_tuple=False,
            ).flatten()
            negative_indices = torch.nonzero(
                negative_mask,
                as_tuple=False,
            ).flatten()

            if positive_indices.numel() == 0 or negative_indices.numel() == 0:
                return

            sample_count = min(
                self.max_pairs_per_component,
                int(positive_indices.numel()) * int(negative_indices.numel()),
            )
            sampled_positive = self._sample_indices(positive_indices, sample_count)
            sampled_negative = self._sample_indices(negative_indices, sample_count)

            margins = logits[sampled_positive] - logits[sampled_negative]
            component_losses.append(F.softplus(-margins).mean())

        add_component(target_positive, ~target_positive)

        for identity_index in range(identity_masks.shape[1]):
            identity_member = identity_masks[:, identity_index]
            background_member = ~identity_member

            add_component(
                identity_member & target_positive,
                identity_member & ~target_positive,
            )
            add_component(
                background_member & target_positive,
                identity_member & ~target_positive,
            )
            add_component(
                identity_member & target_positive,
                background_member & ~target_positive,
            )

        if not component_losses:
            return logits.sum() * 0.0, 0

        return torch.stack(component_losses).mean(), len(component_losses)


model = ToxicityRanker(model).to(device)
criterion = DynamicBiasAwareBCELoss().to(device)
ranking_criterion = BiasAwarePairwiseRankingLoss(
    generator=pairwise_generator,
).to(device)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
head_terms = ("classifier", "score")

base_decay = []
base_no_decay = []
head_decay = []
head_no_decay = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_head = any(term in parameter_name for term in head_terms)
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_head and has_no_decay:
        head_no_decay.append(parameter)
    elif is_head:
        head_decay.append(parameter)
    elif has_no_decay:
        base_no_decay.append(parameter)
    else:
        base_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": base_decay, "lr": 1.5e-5, "weight_decay": 0.01},
        {"params": base_no_decay, "lr": 1.5e-5, "weight_decay": 0.0},
        {"params": head_decay, "lr": 5.0e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 5.0e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)


def set_encoder_backbone_frozen(frozen):
    for parameter_name, parameter in model.named_parameters():
        is_head = any(term in parameter_name for term in head_terms)
        parameter.requires_grad = is_head or not frozen

    state = "frozen" if frozen else "unfrozen"
    print(f"Encoder backbone {state} for head warm-up.")


grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, texts, targets, cell_memberships, identity_masks):
        self.texts = np.asarray(texts, dtype=object)
        self.targets = np.asarray(targets, dtype=np.float32)
        self.cell_memberships = np.asarray(cell_memberships, dtype=np.uint8)
        self.identity_masks = np.asarray(identity_masks, dtype=np.uint8)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            str(self.texts[index]),
            self.targets[index],
            self.cell_memberships[index],
            self.identity_masks[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts):
        self.texts = np.asarray(texts, dtype=object)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return str(self.texts[index])


def training_collate(batch):
    texts, targets, memberships, identity_masks = zip(*batch)

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    return (
        encoded,
        torch.as_tensor(np.asarray(targets), dtype=torch.float32),
        torch.as_tensor(np.asarray(memberships), dtype=torch.uint8),
        torch.as_tensor(np.asarray(identity_masks), dtype=torch.uint8),
    )


def inference_collate(batch):
    return tokenizer(
        list(batch),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )


train_texts = train_processed["comment_text"].fillna("").astype(str).to_numpy()
train_targets = train_processed["target"].to_numpy(dtype=np.float32)
train_cells = np.asarray(train_identity_target_cells, dtype=np.uint8)
train_identity_masks = np.asarray(train_identity_mask, dtype=np.uint8)

if (
    len(train_texts) != len(train_targets)
    or len(train_texts) != len(train_cells)
    or len(train_texts) != len(train_identity_masks)
):
    raise RuntimeError(
        "Training text, target, identity-cell, and identity-mask arrays are "
        "misaligned."
    )

training_dataset = ToxicityTrainingDataset(
    texts=train_texts,
    targets=train_targets,
    cell_memberships=train_cells,
    identity_masks=train_identity_masks,
)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=False,
    num_workers=NUM_WORKERS,
    pin_memory=pin_memory,
    persistent_workers=NUM_WORKERS > 0,
    collate_fn=training_collate,
    generator=training_loader_generator,
)


def _predict_texts(texts):
    texts = np.asarray(texts, dtype=object)

    if len(texts) == 0:
        return np.empty(0, dtype=np.float64)

    previous_mode = model.training
    model.eval()

    inference_loader = DataLoader(
        ToxicityInferenceDataset(texts.astype(str)),
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=pin_memory,
        persistent_workers=False,
        collate_fn=inference_collate,
    )

    predictions = []

    with torch.inference_mode():
        for encoded in inference_loader:
            encoded = {
                name: tensor.to(device, non_blocking=pin_memory)
                for name, tensor in encoded.items()
            }

            with torch.cuda.amp.autocast(enabled=amp_enabled):
                logits = model(
                    input_ids=encoded["input_ids"],
                    attention_mask=encoded.get("attention_mask"),
                )
                probabilities = torch.sigmoid(logits)

            predictions.append(
                probabilities.detach().float().cpu().numpy().astype(np.float64)
            )

    if previous_mode:
        model.train()

    return np.concatenate(predictions, axis=0)


def predict_validation(positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if np.any(positional_indices < 0) or np.any(
        positional_indices >= len(valid_processed)
    ):
        raise IndexError(
            "Validation callback received an out-of-range positional index."
        )

    validation_texts = (
        valid_processed["comment_text"]
        .iloc[positional_indices]
        .fillna("")
        .astype(str)
        .to_numpy()
    )

    return _predict_texts(validation_texts)


def predict_test(positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if np.any(positional_indices < 0) or np.any(
        positional_indices >= len(test_processed)
    ):
        raise IndexError("Test callback received an out-of-range positional index.")

    test_texts = (
        test_processed["comment_text"]
        .iloc[positional_indices]
        .fillna("")
        .astype(str)
        .to_numpy()
    )

    return _predict_texts(test_texts)


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "criterion_state_dict": criterion.state_dict(),
            "max_length": MAX_LENGTH,
            "special_tokens": special_tokens,
        },
        checkpoint_directory / "model_state.pt",
    )

    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")
    model.encoder.config.save_pretrained(checkpoint_directory / "model_config")

    preprocessing_source = Path("./working/processed/preprocessing_state.joblib")
    if preprocessing_source.exists():
        shutil.copy2(
            preprocessing_source,
            checkpoint_directory / "preprocessing_state.joblib",
        )

    with open(
        checkpoint_directory / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            {
                "max_length": MAX_LENGTH,
                "prediction_transform": "sigmoid(toxicity_class_margin)",
                "tokenizer_directory": "tokenizer",
                "model_config_directory": "model_config",
            },
            file,
            indent=2,
        )


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_path = checkpoint_directory / "model_state.pt"

    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Missing checkpoint state: {checkpoint_path}")

    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)

    if "criterion_state_dict" in checkpoint:
        criterion.load_state_dict(checkpoint["criterion_state_dict"], strict=True)

    model.to(device)
    criterion.to(device)
    ranking_criterion.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

set_encoder_backbone_frozen(True)
session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
should_stop = False
optimizer_updates = 0

for epoch_index in range(MAX_EPOCHS):
    model.train()
    epoch_loss_sum = 0.0
    epoch_ranking_loss_sum = 0.0
    epoch_ranking_component_count = 0
    epoch_examples = 0
    accumulated_batches = 0

    for encoded, targets, memberships, identity_masks in training_loader:
        encoded = {
            name: tensor.to(device, non_blocking=pin_memory)
            for name, tensor in encoded.items()
        }
        targets = targets.to(device, non_blocking=pin_memory)
        memberships = memberships.to(device, non_blocking=pin_memory)
        identity_masks = identity_masks.to(device, non_blocking=pin_memory)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            logits = model(
                input_ids=encoded["input_ids"],
                attention_mask=encoded.get("attention_mask"),
            )
            dynamic_bce_loss = criterion(logits, targets, memberships)
            ranking_loss, valid_ranking_components = ranking_criterion(
                logits,
                targets,
                identity_masks,
            )
            batch_loss = dynamic_bce_loss + PAIRWISE_LAMBDA * ranking_loss
            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()

        batch_size = int(targets.shape[0])
        epoch_loss_sum += float(batch_loss.detach().cpu()) * batch_size
        epoch_ranking_loss_sum += float(ranking_loss.detach().cpu()) * batch_size
        epoch_ranking_component_count += valid_ranking_components
        epoch_examples += batch_size
        accumulated_batches += 1

        if accumulated_batches >= GRADIENT_ACCUMULATION_STEPS:
            grad_scaler.unscale_(optimizer)
            clip_grad_norm_(model.parameters(), max_norm=1.0)
            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)

            accumulated_batches = 0
            optimizer_updates += 1

            if optimizer_updates == HEAD_WARMUP_UPDATES:
                set_encoder_backbone_frozen(False)

            should_stop = session.step()

            if should_stop:
                break

    if not should_stop and accumulated_batches > 0:
        grad_scaler.unscale_(optimizer)
        clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        optimizer_updates += 1

        if optimizer_updates == HEAD_WARMUP_UPDATES:
            set_encoder_backbone_frozen(False)

        should_stop = session.step()

    mean_epoch_loss = epoch_loss_sum / max(epoch_examples, 1)
    mean_ranking_loss = epoch_ranking_loss_sum / max(epoch_examples, 1)
    print(
        f"Epoch {epoch_index + 1}: "
        f"loss={mean_epoch_loss:.6f}, "
        f"ranking_loss={mean_ranking_loss:.6f}, "
        f"valid_ranking_components={epoch_ranking_component_count}, "
        f"updates={optimizer_updates}"
    )

    if should_stop:
        break

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
