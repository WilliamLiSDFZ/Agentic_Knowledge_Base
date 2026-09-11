import os
os.sched_setaffinity(0, {4, 68, 42, 106, 47, 48, 111, 112})
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
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, Subset
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# ---------------------------------------------------------------------
# Runtime and paths
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
PROCESSED_DIR = WORKING_DIR / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

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

NUMERIC_FEATURE_COLUMNS = [
    "feature_log_char_count",
    "feature_log_word_count",
    "feature_uppercase_ratio",
    "feature_exclamation_ratio",
    "feature_question_ratio",
    "feature_has_url",
    "feature_has_user",
    "feature_log_train_duplicate_count",
]

TRAIN_COLUMNS = ["id", "target", "comment_text"] + IDENTITY_COLUMNS
TEST_COLUMNS = ["id", "comment_text"]

# ---------------------------------------------------------------------
# Load and split before fitting transformations
# ---------------------------------------------------------------------
train_df = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=lambda column: column in TRAIN_COLUMNS,
    low_memory=False,
)
test_df = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=lambda column: column in TEST_COLUMNS,
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_df, test_df)

# ---------------------------------------------------------------------
# Text normalization and leakage-safe feature engineering
# ---------------------------------------------------------------------
_url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
_email_pattern = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
_user_pattern = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,}")
_zero_width_pattern = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
_whitespace_pattern = re.compile(r"\s+")


def normalize_comment_text(series: pd.Series) -> pd.Series:
    text = series.fillna("").astype(str)
    text = text.map(lambda value: unicodedata.normalize("NFKC", html.unescape(value)))
    text = text.str.replace(_zero_width_pattern, "", regex=True)
    text = text.str.replace(_email_pattern, " [EMAIL] ", regex=True)
    text = text.str.replace(_url_pattern, " [URL] ", regex=True)
    text = text.str.replace(_user_pattern, " [USER] ", regex=True)
    text = text.str.replace(_whitespace_pattern, " ", regex=True).str.strip()
    return text.mask(text.eq(""), "[EMPTY]")


def add_text_features(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()
    cleaned = normalize_comment_text(frame["comment_text"])
    frame["comment_text"] = cleaned

    char_count = cleaned.str.len().clip(lower=1).astype(np.float32)
    alpha_count = cleaned.str.count(r"[A-Za-z]").clip(lower=1).astype(np.float32)
    upper_count = cleaned.str.count(r"[A-Z]").astype(np.float32)

    frame["feature_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["feature_log_word_count"] = np.log1p(
        cleaned.str.split().str.len().astype(np.float32)
    ).astype(np.float32)
    frame["feature_uppercase_ratio"] = (upper_count / alpha_count).astype(np.float32)
    frame["feature_exclamation_ratio"] = (
        cleaned.str.count("!").astype(np.float32) / char_count
    ).astype(np.float32)
    frame["feature_question_ratio"] = (
        cleaned.str.count(r"\?").astype(np.float32) / char_count
    ).astype(np.float32)
    frame["feature_has_url"] = cleaned.str.contains(
        r"\[URL\]", regex=True, na=False
    ).astype(np.float32)
    frame["feature_has_user"] = cleaned.str.contains(
        r"\[USER\]", regex=True, na=False
    ).astype(np.float32)
    frame["feature_text_hash"] = pd.util.hash_pandas_object(
        cleaned, index=False
    ).to_numpy(dtype=np.uint64)

    return frame


train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

train_hash_counts = train_df["feature_text_hash"].value_counts(sort=False)
for frame in (train_df, valid_df, test_df):
    frame["feature_log_train_duplicate_count"] = np.log1p(
        frame["feature_text_hash"].map(train_hash_counts).fillna(0).astype(np.float32)
    ).astype(np.float32)

feature_scaler = StandardScaler()
train_df.loc[:, NUMERIC_FEATURE_COLUMNS] = feature_scaler.fit_transform(
    train_df[NUMERIC_FEATURE_COLUMNS].astype(np.float32)
).astype(np.float32)

for frame in (valid_df, test_df):
    frame.loc[:, NUMERIC_FEATURE_COLUMNS] = feature_scaler.transform(
        frame[NUMERIC_FEATURE_COLUMNS].astype(np.float32)
    ).astype(np.float32)

for frame in (train_df, valid_df):
    identity_values = frame[IDENTITY_COLUMNS].fillna(0.0).astype(np.float32)
    frame["identity_any"] = (identity_values.max(axis=1) >= 0.5).astype(np.int8)
    frame["target_binary"] = (frame["target"].astype(np.float32) >= 0.5).astype(np.int8)

train_identity = train_df["identity_any"].to_numpy(dtype=bool)
train_toxic = train_df["target_binary"].to_numpy(dtype=bool)

sample_weight = np.full(len(train_df), 0.25, dtype=np.float32)
sample_weight += 0.25 * train_identity
sample_weight += 0.25 * (train_toxic & ~train_identity)
sample_weight += 0.25 * (~train_toxic & train_identity)
train_df["sample_weight"] = (
    sample_weight / max(float(sample_weight.mean()), 1e-8)
).astype(np.float32)

valid_df["sample_weight"] = np.ones(len(valid_df), dtype=np.float32)
test_df["sample_weight"] = np.ones(len(test_df), dtype=np.float32)

train_df.drop(columns=["feature_text_hash"], inplace=True)
valid_df.drop(columns=["feature_text_hash"], inplace=True)
test_df.drop(columns=["feature_text_hash"], inplace=True)

joblib.dump(feature_scaler, PROCESSED_DIR / "numeric_feature_scaler.joblib")

processing_manifest = {
    "text_column": "comment_text",
    "numeric_feature_columns": NUMERIC_FEATURE_COLUMNS,
    "identity_columns": IDENTITY_COLUMNS,
    "target_column": "target",
    "continuous_target": True,
    "identity_threshold": 0.5,
    "weight_column": "sample_weight",
    "train_rows": int(len(train_df)),
    "validation_rows": int(len(valid_df)),
    "test_rows": int(len(test_df)),
}
with open(PROCESSED_DIR / "processing_manifest.json", "w", encoding="utf-8") as f:
    json.dump(processing_manifest, f, indent=2)

# ---------------------------------------------------------------------
# Model design
# ---------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
pretrained_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = coefficient
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, grad_outputs):
        return -ctx.coefficient * grad_outputs, None


class GradientReversal(nn.Module):
    def __init__(self, coefficient: float = 0.12):
        super().__init__()
        self.coefficient = float(coefficient)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return GradientReversalFunction.apply(inputs, self.coefficient)


class FrozenLoRALinear(nn.Module):
    """Frozen pretrained projection augmented with a zero-initialized LoRA residual."""

    def __init__(
        self,
        base_layer: nn.Linear,
        rank: int = 8,
        alpha: float = 16.0,
    ):
        super().__init__()
        if not isinstance(base_layer, nn.Linear):
            raise TypeError("FrozenLoRALinear requires an nn.Linear base layer")
        if rank < 1:
            raise ValueError("LoRA rank must be positive")

        self.base_layer = base_layer
        for parameter in self.base_layer.parameters():
            parameter.requires_grad = False

        self.rank = int(rank)
        self.scaling = float(alpha) / float(rank)
        self.lora_A = nn.Linear(base_layer.in_features, rank, bias=False)
        self.lora_B = nn.Linear(rank, base_layer.out_features, bias=False)

        nn.init.kaiming_uniform_(self.lora_A.weight, a=np.sqrt(5))
        nn.init.zeros_(self.lora_B.weight)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.base_layer(inputs) + self.lora_B(self.lora_A(inputs)) * self.scaling


class BiasAdversarialDeberta(nn.Module):
    def __init__(
        self,
        pretrained_classifier: nn.Module,
        numeric_feature_dim: int,
        num_identity_labels: int,
        adversarial_coefficient: float = 0.12,
        dropout_probability: float = 0.15,
        adapter_rank: int = 8,
        adapter_alpha: float = 16.0,
        adapter_layer_count: int = 2,
    ):
        super().__init__()
        self.encoder = pretrained_classifier.deberta
        self.hidden_size = int(pretrained_classifier.config.hidden_size)

        # Keep the pretrained backbone fixed and train rank-8 residual adapters
        # only in the final attention blocks.
        for parameter in self.encoder.parameters():
            parameter.requires_grad = False

        if adapter_layer_count < 1:
            raise ValueError("adapter_layer_count must be positive")

        for encoder_layer in list(self.encoder.encoder.layer)[-adapter_layer_count:]:
            for projection_parent, projection_names in (
                (
                    encoder_layer.attention.self,
                    ("query_proj", "key_proj", "value_proj"),
                ),
                (encoder_layer.attention.output, ("dense",)),
            ):
                for projection_name in projection_names:
                    projection = getattr(projection_parent, projection_name)
                    setattr(
                        projection_parent,
                        projection_name,
                        FrozenLoRALinear(
                            projection,
                            rank=adapter_rank,
                            alpha=adapter_alpha,
                        ),
                    )

        self.text_norm = nn.LayerNorm(self.hidden_size)
        self.numeric_projection = nn.Sequential(
            nn.LayerNorm(numeric_feature_dim),
            nn.Linear(numeric_feature_dim, 128),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )
        self.toxicity_head = nn.Sequential(
            nn.Linear(self.hidden_size + 128, 384),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(384, 1),
        )
        self.gradient_reversal = GradientReversal(adversarial_coefficient)
        self.identity_head = nn.Sequential(
            nn.Linear(self.hidden_size, 384),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(384, num_identity_labels),
        )

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        numeric_features: torch.Tensor,
    ) -> dict:
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        contextual_representation = self.text_norm(
            encoder_outputs.last_hidden_state[:, 0]
        )
        numeric_representation = self.numeric_projection(
            numeric_features.to(dtype=contextual_representation.dtype)
        )

        toxicity_logit = self.toxicity_head(
            torch.cat([contextual_representation, numeric_representation], dim=-1)
        ).squeeze(-1)

        identity_logits = self.identity_head(
            self.gradient_reversal(contextual_representation)
        )

        return {
            "toxicity_logit": toxicity_logit,
            "identity_logits": identity_logits,
        }


class FairToxicityLoss(nn.Module):
    def __init__(self, adversarial_loss_weight: float = 0.10):
        super().__init__()
        self.adversarial_loss_weight = float(adversarial_loss_weight)

    def forward(
        self,
        outputs: dict,
        toxicity_targets: torch.Tensor,
        sample_weights: torch.Tensor,
        identity_targets: torch.Tensor | None = None,
        identity_observed_mask: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, dict]:
        toxicity_targets = toxicity_targets.float().clamp(0.0, 1.0)
        sample_weights = sample_weights.float().clamp_min(0.0)

        toxicity_per_example = F.binary_cross_entropy_with_logits(
            outputs["toxicity_logit"],
            toxicity_targets,
            reduction="none",
        )
        toxicity_loss = (
            toxicity_per_example * sample_weights
        ).sum() / sample_weights.sum().clamp_min(1e-8)

        identity_loss = toxicity_loss.new_zeros(())
        if identity_targets is not None and identity_observed_mask is not None:
            observed = identity_observed_mask.bool()
            if observed.any():
                identity_loss = F.binary_cross_entropy_with_logits(
                    outputs["identity_logits"][observed],
                    identity_targets.float()[observed].clamp(0.0, 1.0),
                    reduction="none",
                ).mean()

        total_loss = toxicity_loss + self.adversarial_loss_weight * identity_loss
        return total_loss, {
            "toxicity_loss": toxicity_loss.detach(),
            "identity_adversary_loss": identity_loss.detach(),
        }


model = BiasAdversarialDeberta(
    pretrained_classifier=pretrained_classifier,
    numeric_feature_dim=len(NUMERIC_FEATURE_COLUMNS),
    num_identity_labels=len(IDENTITY_COLUMNS),
    adversarial_coefficient=0.12,
    dropout_probability=0.15,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")
adapter_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    if ".lora_" in parameter_name:
        adapter_parameters.append(parameter)
    elif parameter.ndim == 1 or any(term in parameter_name for term in no_decay_terms):
        head_no_decay_parameters.append(parameter)
    else:
        head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {"params": adapter_parameters, "lr": 2.0e-4, "weight_decay": 0.01},
        {"params": head_decay_parameters, "lr": 1.5e-4, "weight_decay": 0.01},
        {"params": head_no_decay_parameters, "lr": 1.5e-4, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

criterion = FairToxicityLoss(adversarial_loss_weight=0.10)

# ---------------------------------------------------------------------
# Training and runtime evaluation callbacks
# ---------------------------------------------------------------------
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
AMP_ENABLED = DEVICE.type == "cuda"
MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 32
INFERENCE_BATCH_SIZE = 64
GRADIENT_ACCUMULATION_STEPS = 1
NUM_WORKERS = 2
PIN_MEMORY = DEVICE.type == "cuda"

torch.manual_seed(2029)
if DEVICE.type == "cuda":
    torch.cuda.manual_seed_all(2029)

model.to(DEVICE)

identity_targets_train = (
    train_df[IDENTITY_COLUMNS]
    .fillna(0.0)
    .to_numpy(
        dtype=np.float32,
        copy=True,
    )
)
identity_observed_train = (~train_df[IDENTITY_COLUMNS].isna().all(axis=1)).to_numpy(
    dtype=np.bool_,
    copy=True,
)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame: pd.DataFrame):
        self.texts = frame["comment_text"].fillna("[EMPTY]").astype(str).to_numpy()
        self.numeric_features = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
        self.sample_weights = frame["sample_weight"].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.identity_targets = identity_targets_train
        self.identity_observed = identity_observed_train

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.numeric_features[index],
            self.targets[index],
            self.sample_weights[index],
            self.identity_targets[index],
            self.identity_observed[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, frame: pd.DataFrame):
        self.texts = frame["comment_text"].fillna("[EMPTY]").astype(str).to_numpy()
        self.numeric_features = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index], self.numeric_features[index]


def training_collate(batch):
    texts, numeric_features, targets, sample_weights, identity_targets, observed = zip(
        *batch
    )
    tokenized = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )
    tokenized["numeric_features"] = torch.from_numpy(
        np.asarray(numeric_features, dtype=np.float32)
    )
    tokenized["targets"] = torch.from_numpy(np.asarray(targets, dtype=np.float32))
    tokenized["sample_weights"] = torch.from_numpy(
        np.asarray(sample_weights, dtype=np.float32)
    )
    tokenized["identity_targets"] = torch.from_numpy(
        np.asarray(identity_targets, dtype=np.float32)
    )
    tokenized["identity_observed_mask"] = torch.from_numpy(
        np.asarray(observed, dtype=np.bool_)
    )
    return tokenized


def inference_collate(batch):
    texts, numeric_features = zip(*batch)
    tokenized = tokenizer(
        list(texts),
        truncation=True,
        max_length=MAX_LENGTH,
        padding=True,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )
    tokenized["numeric_features"] = torch.from_numpy(
        np.asarray(numeric_features, dtype=np.float32)
    )
    return tokenized


train_dataset = ToxicityTrainingDataset(train_df)
validation_dataset = ToxicityInferenceDataset(valid_df)
test_dataset = ToxicityInferenceDataset(test_df)

train_loader_generator = torch.Generator()
train_loader_generator.manual_seed(2029)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=train_loader_generator,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    collate_fn=training_collate,
    drop_last=False,
)

warmup_updates = 50
planned_decay_updates = 10000


def learning_rate_multiplier(update_number):
    if update_number < warmup_updates:
        return max(0.05, float(update_number + 1) / float(warmup_updates))

    progress = min(
        1.0,
        float(update_number - warmup_updates)
        / float(max(1, planned_decay_updates - warmup_updates)),
    )
    return max(0.10, 1.0 - 0.90 * progress)


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
scaler = torch.cuda.amp.GradScaler(enabled=AMP_ENABLED)

checkpoint_root = WORKING_DIR / "checkpoints"
checkpoint_root.mkdir(parents=True, exist_ok=True)
optimizer_updates = 0


def _predict_positions(inference_dataset, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)

    indexed_dataset = Subset(inference_dataset, positions.tolist())
    inference_loader = DataLoader(
        indexed_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        collate_fn=inference_collate,
        drop_last=False,
    )

    was_training = model.training
    model.eval()
    prediction_chunks = []

    with torch.no_grad():
        for batch in inference_loader:
            input_ids = batch["input_ids"].to(DEVICE, non_blocking=PIN_MEMORY)
            attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=PIN_MEMORY)
            numeric_features = batch["numeric_features"].to(
                DEVICE,
                non_blocking=PIN_MEMORY,
            )

            with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
                outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    numeric_features=numeric_features,
                )
                probabilities = torch.sigmoid(outputs["toxicity_logit"])

            prediction_chunks.append(
                probabilities.float().cpu().numpy().astype(np.float64, copy=False)
            )

    if was_training:
        model.train()

    return np.concatenate(prediction_chunks, axis=0)


def predict_validation(positional_indices):
    return _predict_positions(validation_dataset, positional_indices)


def predict_test(positional_indices):
    return _predict_positions(test_dataset, positional_indices)


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    cpu_state_dict = {
        name: value.detach().cpu() for name, value in model.state_dict().items()
    }

    torch.save(
        {
            "model_state_dict": cpu_state_dict,
            "optimizer_updates": int(optimizer_updates),
            "max_length": int(MAX_LENGTH),
        },
        checkpoint_directory / "model_state.pt",
    )

    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")

    inference_state = {
        "text_column": "comment_text",
        "numeric_feature_columns": NUMERIC_FEATURE_COLUMNS,
        "identity_columns": IDENTITY_COLUMNS,
        "max_length": MAX_LENGTH,
        "probability_transform": "sigmoid(toxicity_logit)",
        "continuous_target_training": True,
    }
    with open(
        checkpoint_directory / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(inference_state, f, indent=2)

    source_scaler = PROCESSED_DIR / "numeric_feature_scaler.joblib"
    source_manifest = PROCESSED_DIR / "processing_manifest.json"

    if source_scaler.exists():
        shutil.copy2(source_scaler, checkpoint_directory / source_scaler.name)
    if source_manifest.exists():
        shutil.copy2(source_manifest, checkpoint_directory / source_manifest.name)


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint = torch.load(
        checkpoint_directory / "model_state.pt",
        map_location=DEVICE,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(DEVICE)
    model.eval()


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

stop_requested = False
optimizer.zero_grad(set_to_none=True)

epoch = 0
while not stop_requested:
    epoch += 1

    model.train()
    epoch_loss_sum = 0.0
    epoch_batches = 0
    epoch_updates = 0
    pending_accumulation = 0

    for batch_index, batch in enumerate(train_loader):
        input_ids = batch["input_ids"].to(DEVICE, non_blocking=PIN_MEMORY)
        attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=PIN_MEMORY)
        numeric_features = batch["numeric_features"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        )
        targets = batch["targets"].to(DEVICE, non_blocking=PIN_MEMORY)
        sample_weights = batch["sample_weights"].to(DEVICE, non_blocking=PIN_MEMORY)
        batch_identity_targets = batch["identity_targets"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        )
        identity_observed_mask = batch["identity_observed_mask"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        )

        with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                numeric_features=numeric_features,
            )
            unscaled_loss, _ = criterion(
                outputs=outputs,
                toxicity_targets=targets,
                sample_weights=sample_weights,
                identity_targets=batch_identity_targets,
                identity_observed_mask=identity_observed_mask,
            )
            loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(loss).backward()
        pending_accumulation += 1
        epoch_loss_sum += float(unscaled_loss.detach().cpu())
        epoch_batches += 1

        is_last_batch = batch_index + 1 == len(train_loader)
        if pending_accumulation == GRADIENT_ACCUMULATION_STEPS or is_last_batch:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

            optimizer_updates += 1
            epoch_updates += 1
            pending_accumulation = 0

            stop_requested = session.step()
            if stop_requested:
                break

    if epoch_batches > 0:
        mean_epoch_loss = epoch_loss_sum / epoch_batches
        print(
            f"Epoch {epoch}: updates={epoch_updates} " f"loss={mean_epoch_loss:.6f}"
        )

score = session.finish()
print(f"Final Validation Score: {score}")
