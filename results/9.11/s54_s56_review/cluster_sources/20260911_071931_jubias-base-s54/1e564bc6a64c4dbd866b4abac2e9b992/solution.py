import gc
import html
import json
import math
import os
import re
import shutil
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers.modeling_outputs import SequenceClassifierOutput

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

# ---------------------------------------------------------------------
# Runtime-owned split: performed before fitting preprocessing transforms.
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

raw_train_df = pd.read_csv(INPUT_DIR / "train.csv", low_memory=False)
raw_test_df = pd.read_csv(INPUT_DIR / "test.csv", low_memory=False)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

del raw_train_df, raw_test_df
gc.collect()

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

AUXILIARY_TOXICITY_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

available_identity_columns = [
    col for col in IDENTITY_COLUMNS if col in train_df.columns
]
available_auxiliary_columns = [
    col for col in AUXILIARY_TOXICITY_COLUMNS if col in train_df.columns
]

train_keep_columns = (
    ["id", "comment_text", "target"]
    + available_identity_columns
    + available_auxiliary_columns
)
valid_keep_columns = [col for col in train_keep_columns if col in valid_df.columns]

train_df = train_df.loc[:, train_keep_columns].copy()
valid_df = valid_df.loc[:, valid_keep_columns].copy()
test_df = test_df.loc[:, ["id", "comment_text"]].copy()

URL_PATTERN = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")
MULTISPACE_PATTERN = re.compile(r"\s+")
REPEATED_PUNCT_PATTERN = re.compile(r"([!?.,])\1{3,}")
WORD_PATTERN = re.compile(r"\b[\w']+\b", flags=re.UNICODE)
ALL_CAPS_TOKEN_PATTERN = re.compile(r"\b[A-Z]{2,}\b")


def normalize_comment_series(text_series):
    text = text_series.fillna("").astype(str).map(html.unescape)
    text = text.str.normalize("NFKC")
    text = text.str.replace(HTML_TAG_PATTERN, " ", regex=True)
    text = text.str.replace(URL_PATTERN, " <URL> ", regex=True)
    text = text.str.replace(REPEATED_PUNCT_PATTERN, r"\1\1\1", regex=True)
    return text.str.replace(MULTISPACE_PATTERN, " ", regex=True).str.strip()


def add_text_features(frame):
    original_text = frame["comment_text"].fillna("").astype(str)
    cleaned_text = normalize_comment_series(original_text)

    char_count = cleaned_text.str.len().astype(np.float32)
    word_count = cleaned_text.str.count(WORD_PATTERN).astype(np.float32)
    uppercase_count = original_text.str.count(ALL_CAPS_TOKEN_PATTERN).astype(np.float32)

    frame["model_text"] = cleaned_text
    frame["char_count_log"] = np.log1p(char_count).astype(np.float32)
    frame["word_count_log"] = np.log1p(word_count).astype(np.float32)
    frame["mean_word_length"] = (char_count / np.maximum(word_count, 1.0)).astype(
        np.float32
    )
    frame["exclamation_count_log"] = np.log1p(
        cleaned_text.str.count("!").astype(np.float32)
    ).astype(np.float32)
    frame["question_count_log"] = np.log1p(
        cleaned_text.str.count(r"\?").astype(np.float32)
    ).astype(np.float32)
    frame["newline_count_log"] = np.log1p(
        original_text.str.count(r"\n").astype(np.float32)
    ).astype(np.float32)
    frame["url_count_log"] = np.log1p(
        original_text.str.count(URL_PATTERN).astype(np.float32)
    ).astype(np.float32)
    frame["uppercase_token_ratio"] = (
        (uppercase_count / np.maximum(word_count, 1.0))
        .clip(0.0, 1.0)
        .astype(np.float32)
    )
    frame["digit_ratio"] = (
        (cleaned_text.str.count(r"\d").astype(np.float32) / np.maximum(char_count, 1.0))
        .clip(0.0, 1.0)
        .astype(np.float32)
    )
    frame["repeated_punct_ratio"] = (
        (
            original_text.str.count(r"([!?.,])\1{1,}").astype(np.float32)
            / np.maximum(char_count, 1.0)
        )
        .clip(0.0, 1.0)
        .astype(np.float32)
    )

    frame.drop(columns=["comment_text"], inplace=True)
    return frame


train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

STRUCTURAL_FEATURE_COLUMNS = [
    "char_count_log",
    "word_count_log",
    "mean_word_length",
    "exclamation_count_log",
    "question_count_log",
    "newline_count_log",
    "url_count_log",
    "uppercase_token_ratio",
    "digit_ratio",
    "repeated_punct_ratio",
]

numeric_scaler = StandardScaler()
train_df.loc[:, STRUCTURAL_FEATURE_COLUMNS] = numeric_scaler.fit_transform(
    train_df[STRUCTURAL_FEATURE_COLUMNS].astype(np.float32)
).astype(np.float32)
valid_df.loc[:, STRUCTURAL_FEATURE_COLUMNS] = numeric_scaler.transform(
    valid_df[STRUCTURAL_FEATURE_COLUMNS].astype(np.float32)
).astype(np.float32)
test_df.loc[:, STRUCTURAL_FEATURE_COLUMNS] = numeric_scaler.transform(
    test_df[STRUCTURAL_FEATURE_COLUMNS].astype(np.float32)
).astype(np.float32)

train_df["target_continuous"] = (
    train_df["target"].fillna(0.0).clip(0.0, 1.0).astype(np.float32)
)
valid_df["target_continuous"] = (
    valid_df["target"].fillna(0.0).clip(0.0, 1.0).astype(np.float32)
)
train_df["target_binary"] = (train_df["target_continuous"] >= 0.5).astype(np.float32)
valid_df["target_binary"] = (valid_df["target_continuous"] >= 0.5).astype(np.float32)

if available_identity_columns:
    for col in available_identity_columns:
        train_df[col] = train_df[col].fillna(0.0).clip(0.0, 1.0).astype(np.float32)
        valid_df[col] = valid_df[col].fillna(0.0).clip(0.0, 1.0).astype(np.float32)

    train_identity_strength = train_df[available_identity_columns].max(axis=1)
    valid_identity_strength = valid_df[available_identity_columns].max(axis=1)

    train_df["identity_strength"] = train_identity_strength.astype(np.float32)
    valid_df["identity_strength"] = valid_identity_strength.astype(np.float32)
    train_df["has_identity"] = (train_identity_strength >= 0.5).astype(np.float32)
    valid_df["has_identity"] = (valid_identity_strength >= 0.5).astype(np.float32)
else:
    train_df["identity_strength"] = np.float32(0.0)
    valid_df["identity_strength"] = np.float32(0.0)
    train_df["has_identity"] = np.float32(0.0)
    valid_df["has_identity"] = np.float32(0.0)

for col in available_auxiliary_columns:
    train_df[col] = train_df[col].fillna(-1.0).clip(-1.0, 1.0).astype(np.float32)
    valid_df[col] = valid_df[col].fillna(-1.0).clip(-1.0, 1.0).astype(np.float32)

positive_rate = float(train_df["target_binary"].mean())
positive_class_weight = 0.5 / max(positive_rate, 1e-6)
negative_class_weight = 0.5 / max(1.0 - positive_rate, 1e-6)

base_class_weight = np.where(
    train_df["target_binary"].to_numpy(dtype=np.float32) > 0.5,
    positive_class_weight,
    negative_class_weight,
).astype(np.float32)

identity_strength = train_df["identity_strength"].to_numpy(dtype=np.float32)
non_toxic_identity = (train_df["has_identity"].to_numpy(dtype=np.float32) > 0.5) & (
    train_df["target_binary"].to_numpy(dtype=np.float32) < 0.5
)

bias_emphasis = (
    1.0 + 0.60 * identity_strength + 0.40 * non_toxic_identity.astype(np.float32)
).astype(np.float32)

train_sample_weight = base_class_weight * bias_emphasis
train_sample_weight /= train_sample_weight.mean()
train_df["sample_weight"] = train_sample_weight.astype(np.float32)

train_texts = train_df["model_text"].to_numpy(dtype=object)
valid_texts = valid_df["model_text"].to_numpy(dtype=object)
test_texts = test_df["model_text"].to_numpy(dtype=object)

train_structural_features = train_df[STRUCTURAL_FEATURE_COLUMNS].to_numpy(
    dtype=np.float32
)
valid_structural_features = valid_df[STRUCTURAL_FEATURE_COLUMNS].to_numpy(
    dtype=np.float32
)
test_structural_features = test_df[STRUCTURAL_FEATURE_COLUMNS].to_numpy(
    dtype=np.float32
)

train_targets = train_df["target_continuous"].to_numpy(dtype=np.float32)

train_identity_targets = (
    train_df[available_identity_columns].to_numpy(dtype=np.float32)
    if available_identity_columns
    else np.zeros((len(train_df), 0), dtype=np.float32)
)

feature_state = {
    "structural_feature_columns": STRUCTURAL_FEATURE_COLUMNS,
    "identity_columns": available_identity_columns,
    "evaluated_identity_columns": [
        col for col in EVALUATED_IDENTITY_COLUMNS if col in available_identity_columns
    ],
    "auxiliary_columns": available_auxiliary_columns,
    "numeric_scaler": numeric_scaler,
    "text_normalization": "NFKC + HTML unescape + URL token + whitespace normalization",
}
joblib.dump(feature_state, WORKING_DIR / "feature_state.joblib")

# ---------------------------------------------------------------------
# DeBERTa-v3-large model and identity-cell Group-DRO training objective.
# ---------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
base_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
structural_feature_dim = len(STRUCTURAL_FEATURE_COLUMNS)

evaluated_identity_indices = [
    available_identity_columns.index(col)
    for col in EVALUATED_IDENTITY_COLUMNS
    if col in available_identity_columns
]


class TextShapeDebertaClassifier(nn.Module):
    def __init__(self, pretrained_sequence_classifier, numeric_feature_dim):
        super().__init__()
        self.backbone = pretrained_sequence_classifier
        self.config = pretrained_sequence_classifier.config
        self.numeric_feature_dim = int(numeric_feature_dim)

        hidden_size = self.config.hidden_size
        self.shape_norm = nn.LayerNorm(self.numeric_feature_dim)
        self.shape_adapter = nn.Sequential(
            nn.Linear(self.numeric_feature_dim, hidden_size),
            nn.GELU(),
            nn.Dropout(0.15),
            nn.Linear(hidden_size, self.config.num_labels),
        )
        self.shape_scale = nn.Parameter(torch.tensor(0.05, dtype=torch.float32))

    def forward(
        self,
        input_ids,
        attention_mask=None,
        token_type_ids=None,
        structural_features=None,
        **kwargs,
    ):
        encoder_outputs = self.backbone.deberta(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            return_dict=True,
        )
        sequence_output = encoder_outputs.last_hidden_state
        pooled_output = self.backbone.pooler(sequence_output)
        pooled_output = self.backbone.dropout(pooled_output)
        logits = self.backbone.classifier(pooled_output)

        if structural_features is not None and self.numeric_feature_dim > 0:
            structural_features = structural_features.to(
                device=logits.device,
                dtype=logits.dtype,
            )
            shape_logits = self.shape_adapter(self.shape_norm(structural_features))
            logits = logits + self.shape_scale.tanh() * shape_logits

        return SequenceClassifierOutput(logits=logits)


class IdentityCellGroupDROLoss(nn.Module):
    def __init__(
        self,
        identity_indices,
        dro_strength=0.45,
        ema_momentum=0.97,
        temperature=3.0,
        minimum_group_examples=2,
    ):
        super().__init__()
        self.identity_indices = tuple(int(x) for x in identity_indices)
        self.dro_strength = float(dro_strength)
        self.ema_momentum = float(ema_momentum)
        self.temperature = float(temperature)
        self.minimum_group_examples = int(minimum_group_examples)

        number_of_groups = max(1, 4 * len(self.identity_indices))
        self.register_buffer(
            "group_loss_ema",
            torch.zeros(number_of_groups, dtype=torch.float32),
        )
        self.register_buffer(
            "group_seen",
            torch.zeros(number_of_groups, dtype=torch.bool),
        )

    @staticmethod
    def per_example_loss(logits, binary_targets):
        positive_logit = logits[:, 1] - logits[:, 0]
        return F.binary_cross_entropy_with_logits(
            positive_logit,
            binary_targets,
            reduction="none",
        )

    def forward(
        self, logits, toxicity_targets, identity_targets=None, sample_weight=None
    ):
        binary_targets = (toxicity_targets.reshape(-1) >= 0.5).to(logits.dtype)
        per_example_loss = self.per_example_loss(logits, binary_targets)

        if sample_weight is None:
            sample_weight = torch.ones_like(per_example_loss)
        else:
            sample_weight = (
                sample_weight.reshape(-1)
                .to(
                    device=logits.device,
                    dtype=logits.dtype,
                )
                .clamp_min(1e-4)
            )

        global_loss = (per_example_loss * sample_weight).sum() / sample_weight.sum()

        if (
            identity_targets is None
            or identity_targets.ndim != 2
            or len(self.identity_indices) == 0
        ):
            return global_loss

        identity_targets = identity_targets.to(
            device=logits.device,
            dtype=logits.dtype,
        )

        active_losses = []
        active_indices = []

        for local_index, identity_index in enumerate(self.identity_indices):
            if identity_index >= identity_targets.shape[1]:
                continue

            is_subgroup = identity_targets[:, identity_index] >= 0.5
            is_positive = binary_targets >= 0.5
            cell_masks = (
                is_subgroup & ~is_positive,
                is_subgroup & is_positive,
                ~is_subgroup & ~is_positive,
                ~is_subgroup & is_positive,
            )

            for offset, cell_mask in enumerate(cell_masks):
                group_index = 4 * local_index + offset
                if int(cell_mask.sum().item()) < self.minimum_group_examples:
                    continue

                cell_weights = sample_weight[cell_mask]
                cell_loss = (
                    per_example_loss[cell_mask] * cell_weights
                ).sum() / cell_weights.sum()

                active_losses.append(cell_loss)
                active_indices.append(group_index)

                with torch.no_grad():
                    detached = cell_loss.detach().float()
                    if self.group_seen[group_index]:
                        self.group_loss_ema[group_index].mul_(self.ema_momentum).add_(
                            detached * (1.0 - self.ema_momentum)
                        )
                    else:
                        self.group_loss_ema[group_index].copy_(detached)
                        self.group_seen[group_index] = True

        if not active_losses:
            return global_loss

        active_losses = torch.stack(active_losses)
        active_indices = torch.tensor(
            active_indices,
            device=logits.device,
            dtype=torch.long,
        )

        with torch.no_grad():
            robust_weights = torch.softmax(
                self.group_loss_ema[active_indices] * self.temperature,
                dim=0,
            )

        robust_loss = (robust_weights.to(active_losses.dtype) * active_losses).sum()
        return (1.0 - self.dro_strength) * global_loss + self.dro_strength * robust_loss


model = TextShapeDebertaClassifier(
    pretrained_sequence_classifier=base_model,
    numeric_feature_dim=structural_feature_dim,
).to(device)

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()
    model.backbone.config.use_cache = False

criterion = IdentityCellGroupDROLoss(
    identity_indices=evaluated_identity_indices,
    dro_strength=0.45,
    ema_momentum=0.97,
    temperature=3.0,
    minimum_group_examples=2,
).to(device)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")
optimizer_parameter_groups = []

for learning_rate, selector in (
    (1.5e-5, lambda name: name.startswith("backbone.deberta.")),
    (5.0e-5, lambda name: not name.startswith("backbone.deberta.")),
):
    decay_parameters = [
        parameter
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
        and selector(name)
        and not any(term in name for term in no_decay_terms)
    ]
    no_decay_parameters = [
        parameter
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
        and selector(name)
        and any(term in name for term in no_decay_terms)
    ]

    if decay_parameters:
        optimizer_parameter_groups.append(
            {"params": decay_parameters, "lr": learning_rate, "weight_decay": 0.01}
        )
    if no_decay_parameters:
        optimizer_parameter_groups.append(
            {"params": no_decay_parameters, "lr": learning_rate, "weight_decay": 0.0}
        )

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-6,
)

AMP_ENABLED = device.type == "cuda"
grad_scaler = torch.cuda.amp.GradScaler(enabled=AMP_ENABLED)

# ---------------------------------------------------------------------
# Data, inference callbacks, checkpoint persistence, and training.
# ---------------------------------------------------------------------
MAX_SEQUENCE_LENGTH = 256
TRAIN_BATCH_SIZE = 8 if AMP_ENABLED else 2
INFERENCE_BATCH_SIZE = 24 if AMP_ENABLED else 4
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 4
NUM_WORKERS = 2


class ToxicityTrainingDataset(Dataset):
    def __init__(self, texts, features, targets, identities, weights):
        self.texts = texts
        self.features = features
        self.targets = targets
        self.identities = identities
        self.weights = weights

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            str(self.texts[index]),
            self.features[index],
            np.float32(self.targets[index]),
            self.identities[index],
            np.float32(self.weights[index]),
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts, features):
        self.texts = texts
        self.features = features

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return str(self.texts[index]), self.features[index]


def training_collate_fn(samples):
    texts = [sample[0] for sample in samples]
    features = torch.from_numpy(
        np.ascontiguousarray(
            np.stack([sample[1] for sample in samples]).astype(np.float32)
        )
    )
    targets = torch.tensor([sample[2] for sample in samples], dtype=torch.float32)
    identities = torch.from_numpy(
        np.ascontiguousarray(
            np.stack([sample[3] for sample in samples]).astype(np.float32)
        )
    )
    weights = torch.tensor([sample[4] for sample in samples], dtype=torch.float32)
    return texts, features, targets, identities, weights


def inference_collate_fn(samples):
    texts = [sample[0] for sample in samples]
    features = torch.from_numpy(
        np.ascontiguousarray(
            np.stack([sample[1] for sample in samples]).astype(np.float32)
        )
    )
    return texts, features


def encode_text_batch(text_batch):
    encoded = tokenizer(
        list(text_batch),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
    )
    return {
        name: value.to(device=device, non_blocking=True)
        for name, value in encoded.items()
    }


@torch.inference_mode()
def predict_probability_array(text_array, feature_array, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(text_array):
        raise IndexError("Candidate runtime supplied out-of-range positional indices.")

    subset_texts = text_array[positional_indices]
    subset_features = feature_array[positional_indices]

    inference_loader = DataLoader(
        ToxicityInferenceDataset(subset_texts, subset_features),
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=AMP_ENABLED,
        persistent_workers=False,
        collate_fn=inference_collate_fn,
    )

    was_training = model.training
    model.eval()
    predictions = []

    try:
        for text_batch, feature_batch in inference_loader:
            encoded_batch = encode_text_batch(text_batch)
            feature_batch = feature_batch.to(
                device=device,
                dtype=torch.float32,
                non_blocking=True,
            )

            with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
                logits = model(
                    **encoded_batch,
                    structural_features=feature_batch,
                ).logits
                probabilities = torch.softmax(logits.float(), dim=1)[:, 1]

            predictions.append(probabilities.cpu().numpy())
    finally:
        model.train(was_training)

    return np.concatenate(predictions).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_probability_array(
        valid_texts,
        valid_structural_features,
        positional_indices,
    )


def predict_test(positional_indices):
    return predict_probability_array(
        test_texts,
        test_structural_features,
        positional_indices,
    )


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "criterion_state_dict": criterion.state_dict(),
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
            "structural_feature_dim": structural_feature_dim,
            "probability_transform": "softmax(logits)[:, 1]",
        },
        checkpoint_dir / "model_state.pt",
    )

    model.config.save_pretrained(checkpoint_dir / "model_config")
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    with open(checkpoint_dir / "inference_state.json", "w", encoding="utf-8") as file:
        json.dump(
            {
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "structural_feature_columns": STRUCTURAL_FEATURE_COLUMNS,
                "model_output_probability": "softmax(class_logits)[:, 1]",
                "normalization_source": "working/feature_state.joblib",
            },
            file,
            indent=2,
            sort_keys=True,
        )

    feature_state_path = WORKING_DIR / "feature_state.joblib"
    if feature_state_path.exists():
        shutil.copy2(feature_state_path, checkpoint_dir / "feature_state.joblib")


def load_checkpoint(directory):
    checkpoint = torch.load(
        Path(directory) / "model_state.pt",
        map_location=device,
        weights_only=False,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    if "criterion_state_dict" in checkpoint:
        criterion.load_state_dict(checkpoint["criterion_state_dict"], strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

training_dataset = ToxicityTrainingDataset(
    texts=train_texts,
    features=train_structural_features,
    targets=train_targets,
    identities=train_identity_targets,
    weights=train_df["sample_weight"].to_numpy(dtype=np.float32),
)

loader_generator = torch.Generator()
loader_generator.manual_seed(2027)

training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=True,
    num_workers=NUM_WORKERS,
    pin_memory=AMP_ENABLED,
    persistent_workers=True,
    collate_fn=training_collate_fn,
    generator=loader_generator,
)

estimated_updates_per_epoch = max(
    1,
    len(training_dataset) // (TRAIN_BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS),
)
planned_optimizer_updates = max(1, estimated_updates_per_epoch * MAX_EPOCHS)
warmup_updates = min(200, max(20, planned_optimizer_updates // 100))


def learning_rate_scale(update_index):
    if update_index < warmup_updates:
        return max(0.05, float(update_index + 1) / float(warmup_updates))

    progress = min(
        1.0,
        float(update_index - warmup_updates)
        / float(max(1, planned_optimizer_updates - warmup_updates)),
    )
    return 0.25 + 0.75 * 0.5 * (1.0 + math.cos(math.pi * progress))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_scale)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
training_should_stop = False
completed_optimizer_updates = 0

for epoch_index in range(MAX_EPOCHS):
    model.train()
    epoch_loss_sum = 0.0
    epoch_microbatches = 0

    for batch_index, (
        text_batch,
        feature_batch,
        target_batch,
        identity_batch,
        weight_batch,
    ) in enumerate(training_loader):
        encoded_batch = encode_text_batch(text_batch)
        feature_batch = feature_batch.to(
            device=device,
            dtype=torch.float32,
            non_blocking=True,
        )
        target_batch = target_batch.to(
            device=device,
            dtype=torch.float32,
            non_blocking=True,
        )
        identity_batch = identity_batch.to(
            device=device,
            dtype=torch.float32,
            non_blocking=True,
        )
        weight_batch = weight_batch.to(
            device=device,
            dtype=torch.float32,
            non_blocking=True,
        )

        with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
            logits = model(
                **encoded_batch,
                structural_features=feature_batch,
            ).logits
            batch_loss = criterion(
                logits=logits,
                toxicity_targets=target_batch,
                identity_targets=identity_batch,
                sample_weight=weight_batch,
            )
            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()

        epoch_loss_sum += float(batch_loss.detach().cpu())
        epoch_microbatches += 1

        if (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS != 0:
            continue

        grad_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        scheduler.step()
        optimizer.zero_grad(set_to_none=True)

        completed_optimizer_updates += 1
        training_should_stop = session.step()

        if training_should_stop:
            break

    mean_epoch_loss = epoch_loss_sum / max(1, epoch_microbatches)
    print(
        f"epoch={epoch_index + 1} updates={completed_optimizer_updates} "
        f"train_loss={mean_epoch_loss:.6f}"
    )

    if training_should_stop:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
