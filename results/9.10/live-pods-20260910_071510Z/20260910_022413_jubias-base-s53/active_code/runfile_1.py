import os
os.sched_setaffinity(0, {16, 17})
import json
import math
import os
import pickle
import random
import re
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import AutoModelForSequenceClassification, AutoTokenizer

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# =============================================================================
# Configuration
# =============================================================================

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"
SAMPLE_SUBMISSION_PATH = INPUT_DIR / "sample_submission.csv"

CHECKPOINT_PATH = WORKING_DIR / "best_bias_aware_deberta.pt"
METRICS_PATH = WORKING_DIR / "best_validation_metrics.json"
SUBMISSION_PATH = SUBMISSION_DIR / "submission_b5a111a91ab443bf8a79e72895d4a341.csv"

SEED = 2029
MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 8 if torch.cuda.is_available() else 2
EVAL_BATCH_SIZE = 16 if torch.cuda.is_available() else 2
GRADIENT_ACCUMULATION_STEPS = 4
NUM_EPOCHS = 2
EARLY_STOPPING_PATIENCE = 1
WARMUP_FRACTION = 0.05
# Limit worker creation to the environment's supported process count.
NUM_WORKERS = 2

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

TOXICITY_AUX_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

BASE_TRAIN_COLUMNS = (
    [
        "id",
        "comment_text",
        "target",
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + TOXICITY_AUX_COLUMNS
    + IDENTITY_COLUMNS
)

# =============================================================================
# Reproducibility
# =============================================================================

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pin_memory = device.type == "cuda"

# =============================================================================
# Data processing and feature engineering
# =============================================================================

url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
email_pattern = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
html_pattern = re.compile(r"<[^>\n]{1,200}>")
mention_pattern = re.compile(r"(?<![\w@])@\w{2,}")
repeat_punctuation_pattern = re.compile(r"[!?]{2,}")


def normalize_comment_text(text_series: pd.Series) -> pd.Series:
    text = text_series.fillna("").astype(str).str.normalize("NFKC")
    text = text.str.replace("\u200b", "", regex=False)
    text = text.str.replace("\ufeff", "", regex=False)
    text = text.str.replace("\u00a0", " ", regex=False)
    text = text.str.replace(url_pattern, " [URL] ", regex=True)
    text = text.str.replace(email_pattern, " [EMAIL] ", regex=True)
    text = text.str.replace(html_pattern, " ", regex=True)
    text = text.str.replace(mention_pattern, " [USER] ", regex=True)
    text = text.str.replace(r"\s+", " ", regex=True).str.strip()
    return text.mask(text.eq(""), "[EMPTY]")


def build_text_features(
    raw_text: pd.Series,
    normalized_text: pd.Series,
) -> pd.DataFrame:
    raw = raw_text.fillna("").astype(str).str.normalize("NFKC")
    clean = normalized_text.astype(str)

    char_count = clean.str.len().to_numpy(dtype=np.float32)
    word_count = clean.str.count(r"\S+").to_numpy(dtype=np.float32)
    alphabetic_count = clean.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    uppercase_count = clean.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = clean.str.count(r"\d").to_numpy(dtype=np.float32)

    exclamation_count = raw.str.count("!").to_numpy(dtype=np.float32)
    question_count = raw.str.count(r"\?").to_numpy(dtype=np.float32)
    newline_count = raw.str.count(r"[\r\n]").to_numpy(dtype=np.float32)
    url_count = raw.str.count(url_pattern).to_numpy(dtype=np.float32)
    repeated_punctuation_count = raw.str.count(repeat_punctuation_pattern).to_numpy(
        dtype=np.float32
    )
    quote_count = raw.str.count(r"""["']""").to_numpy(dtype=np.float32)
    sentence_end_count = clean.str.count(r"[.!?]").to_numpy(dtype=np.float32)

    safe_char_count = np.maximum(char_count, 1.0)
    safe_word_count = np.maximum(word_count, 1.0)
    safe_alpha_count = np.maximum(alphabetic_count, 1.0)

    return pd.DataFrame(
        {
            "textstat_log_char_count": np.log1p(char_count),
            "textstat_log_word_count": np.log1p(word_count),
            "textstat_mean_chars_per_word": char_count / safe_word_count,
            "textstat_uppercase_ratio": uppercase_count / safe_alpha_count,
            "textstat_digit_ratio": digit_count / safe_char_count,
            "textstat_alpha_ratio": alphabetic_count / safe_char_count,
            "textstat_log_exclamation_count": np.log1p(exclamation_count),
            "textstat_log_question_count": np.log1p(question_count),
            "textstat_log_sentence_end_count": np.log1p(sentence_end_count),
            "textstat_log_newline_count": np.log1p(newline_count),
            "textstat_log_url_count": np.log1p(url_count),
            "textstat_log_repeated_punctuation_count": np.log1p(
                repeated_punctuation_count
            ),
            "textstat_log_quote_count": np.log1p(quote_count),
            "textstat_is_very_short": (word_count <= 3).astype(np.float32),
            "textstat_is_long": (word_count >= 150).astype(np.float32),
        }
    ).astype(np.float32)


def prepare_split(frame: pd.DataFrame, include_labels: bool) -> pd.DataFrame:
    output = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(),
            "text_for_model": normalize_comment_text(frame["comment_text"]).to_numpy(),
        }
    )

    text_features = build_text_features(frame["comment_text"], output["text_for_model"])
    output = pd.concat([output, text_features], axis=1)

    if include_labels:
        output["target"] = frame["target"].astype(np.float32).clip(0.0, 1.0).to_numpy()
        output["target_binary"] = (
            frame["target"].to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.int8)

        output["toxicity_annotator_count"] = (
            frame["toxicity_annotator_count"].fillna(0).astype(np.int32).to_numpy()
        )
        output["identity_annotator_count"] = (
            frame["identity_annotator_count"].fillna(0).astype(np.int32).to_numpy()
        )

        for column in TOXICITY_AUX_COLUMNS:
            output[column] = (
                frame[column].fillna(0.0).astype(np.float32).clip(0.0, 1.0).to_numpy()
            )

        identity_available = (
            frame[IDENTITY_COLUMNS].notna().any(axis=1).to_numpy(dtype=np.int8)
        )
        output["identity_labels_available"] = identity_available

        identity_values = (
            frame[IDENTITY_COLUMNS].fillna(0.0).clip(0.0, 1.0).astype(np.float32)
        )

        for column in IDENTITY_COLUMNS:
            output[column] = identity_values[column].to_numpy()

        output["identity_any"] = identity_values.max(axis=1).to_numpy(dtype=np.float32)

    return output


def save_processed_frame(frame: pd.DataFrame, basename: str) -> str:
    parquet_path = WORKING_DIR / f"{basename}.parquet"
    pickle_path = WORKING_DIR / f"{basename}.pkl"

    try:
        frame.to_parquet(parquet_path, index=False, compression="zstd")
        if pickle_path.exists():
            pickle_path.unlink()
        return str(parquet_path)
    except Exception:
        if parquet_path.exists():
            parquet_path.unlink()
        frame.to_pickle(pickle_path)
        return str(pickle_path)


sample_submission = pd.read_csv(SAMPLE_SUBMISSION_PATH)
if list(sample_submission.columns) != ["id", "prediction"]:
    raise ValueError("sample_submission.csv must contain exactly id and prediction.")

raw_train = pd.read_csv(TRAIN_PATH, usecols=BASE_TRAIN_COLUMNS)
raw_test = pd.read_csv(TEST_PATH, usecols=["id", "comment_text"])

if not raw_test["id"].equals(sample_submission["id"]):
    raise ValueError("test.csv row order does not match sample_submission.csv.")
if not raw_train["id"].is_unique:
    raise ValueError("Training IDs must be unique.")
if not raw_test["id"].is_unique:
    raise ValueError("Test IDs must be unique.")

raw_duplicate_group = raw_train["comment_text"].fillna("").astype(str)
group_hash = pd.util.hash_pandas_object(
    raw_duplicate_group,
    index=False,
).to_numpy(dtype=np.uint64)

validation_mask = (group_hash % np.uint64(5)) == 0
if validation_mask.sum() == 0 or (~validation_mask).sum() == 0:
    raise RuntimeError("Duplicate-group validation split produced an empty partition.")

train_raw = raw_train.loc[~validation_mask].reset_index(drop=True).copy()
valid_raw = raw_train.loc[validation_mask].reset_index(drop=True).copy()
del raw_train

train_processed = prepare_split(train_raw, include_labels=True)
valid_processed = prepare_split(valid_raw, include_labels=True)
test_processed = prepare_split(raw_test, include_labels=False)

del train_raw
del valid_raw
del raw_test

NUMERIC_FEATURE_COLUMNS = [
    column for column in train_processed.columns if column.startswith("textstat_")
]

scaler = StandardScaler(copy=True)

train_processed.loc[:, NUMERIC_FEATURE_COLUMNS] = scaler.fit_transform(
    train_processed[NUMERIC_FEATURE_COLUMNS]
).astype(np.float32)

valid_processed.loc[:, NUMERIC_FEATURE_COLUMNS] = scaler.transform(
    valid_processed[NUMERIC_FEATURE_COLUMNS]
).astype(np.float32)

test_processed.loc[:, NUMERIC_FEATURE_COLUMNS] = scaler.transform(
    test_processed[NUMERIC_FEATURE_COLUMNS]
).astype(np.float32)

with open(WORKING_DIR / "text_feature_scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file, protocol=pickle.HIGHEST_PROTOCOL)

artifact_paths = {
    "train": save_processed_frame(train_processed, "train_processed"),
    "validation": save_processed_frame(valid_processed, "validation_processed"),
    "test": save_processed_frame(test_processed, "test_processed"),
}

manifest = {
    "split_strategy": (
        "deterministic exact-raw-comment duplicate-group hash split; "
        "validation if hash_mod_5_equals_0"
    ),
    "validation_fraction_approximate": 0.20,
    "train_rows": int(len(train_processed)),
    "validation_rows": int(len(valid_processed)),
    "test_rows": int(len(test_processed)),
    "text_column": "text_for_model",
    "target_column": "target",
    "binary_target_column": "target_binary",
    "identity_columns": IDENTITY_COLUMNS,
    "toxicity_auxiliary_columns": TOXICITY_AUX_COLUMNS,
    "identity_availability_column": "identity_labels_available",
    "numeric_feature_columns": NUMERIC_FEATURE_COLUMNS,
    "scaler_path": str(WORKING_DIR / "text_feature_scaler.pkl"),
    "artifacts": artifact_paths,
}

with open(WORKING_DIR / "data_manifest.json", "w", encoding="utf-8") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

# =============================================================================
# Model design
# =============================================================================

"""
DeBERTa-v3-large Usage Example
Base model: microsoft/deberta-v3-large (~435M parameters)
Domain: Natural Language Processing (text classification, NLI, QA, etc.)
Input: tokenized text sequences
Output: Classification logits or hidden embeddings

Reference: https://huggingface.co/microsoft/deberta-v3-large
"""

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
base_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, strength):
        ctx.strength = strength
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return gradient_output.neg() * ctx.strength, None


def gradient_reverse(inputs, strength):
    return GradientReversalFunction.apply(inputs, strength)


class BiasAwareDeberta(nn.Module):
    def __init__(
        self,
        backbone,
        hidden_size,
        numeric_feature_count,
        identity_count,
        toxicity_aux_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
        super().__init__()
        self.backbone = backbone
        self.adversarial_strength = adversarial_strength

        numeric_hidden_size = 256
        task_hidden_size = 512

        self.numeric_encoder = nn.Sequential(
            nn.LayerNorm(numeric_feature_count),
            nn.Linear(numeric_feature_count, numeric_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(numeric_hidden_size, hidden_size),
        )

        self.fusion_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )
        self.fusion_norm = nn.LayerNorm(hidden_size)

        self.shared_representation = nn.Sequential(
            nn.Linear(hidden_size, task_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.LayerNorm(task_hidden_size),
        )

        self.toxicity_head = nn.Linear(task_hidden_size, 1)
        self.auxiliary_head = nn.Linear(task_hidden_size, toxicity_aux_count)

        self.identity_adversary = nn.Sequential(
            nn.Linear(task_hidden_size + 2, task_hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(task_hidden_size // 2, identity_count),
        )

    def forward(
        self,
        input_ids,
        attention_mask,
        numeric_features,
        toxicity_condition=None,
    ):
        encoder_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        text_representation = encoder_outputs.last_hidden_state[:, 0]
        numeric_representation = self.numeric_encoder(numeric_features)

        fusion_gate = self.fusion_gate(
            torch.cat([text_representation, numeric_representation], dim=-1)
        )

        fused_representation = self.fusion_norm(
            text_representation + fusion_gate * numeric_representation
        )

        representation = self.shared_representation(fused_representation)
        toxicity_logits = self.toxicity_head(representation).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(representation)

        if toxicity_condition is None:
            toxicity_condition = torch.sigmoid(toxicity_logits).detach()

        toxicity_condition = toxicity_condition.reshape(-1, 1).clamp(0.0, 1.0)
        condition_features = torch.cat(
            [toxicity_condition, 1.0 - toxicity_condition],
            dim=-1,
        )

        adversarial_features = torch.cat(
            [
                gradient_reverse(representation, self.adversarial_strength),
                condition_features,
            ],
            dim=-1,
        )

        identity_logits = self.identity_adversary(adversarial_features)

        return {
            "toxicity_logit": toxicity_logits,
            "auxiliary_logits": auxiliary_logits,
            "identity_logits": identity_logits,
        }


class BiasAwareToxicityLoss(nn.Module):
    def __init__(
        self,
        auxiliary_weight=0.20,
        adversarial_weight=0.08,
        subgroup_threshold=0.5,
    ):
        super().__init__()
        self.auxiliary_weight = auxiliary_weight
        self.adversarial_weight = adversarial_weight
        self.subgroup_threshold = subgroup_threshold

    def forward(self, model_outputs, batch_labels):
        toxicity_targets = batch_labels["target"].float().reshape(-1).clamp(0.0, 1.0)
        identity_targets = batch_labels["identity_targets"].float().clamp(0.0, 1.0)
        auxiliary_targets = batch_labels["auxiliary_targets"].float().clamp(0.0, 1.0)

        toxic_binary = toxicity_targets >= self.subgroup_threshold
        subgroup_member = identity_targets.max(dim=1).values >= self.subgroup_threshold

        sample_weights = torch.ones_like(toxicity_targets)
        sample_weights = sample_weights + subgroup_member.float()
        sample_weights = (
            sample_weights + 5.0 * (subgroup_member & ~toxic_binary).float()
        )
        sample_weights = (
            sample_weights + 5.0 * (~subgroup_member & toxic_binary).float()
        )
        sample_weights = sample_weights / sample_weights.mean().clamp_min(1e-6)

        toxicity_loss_per_sample = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logit"],
            toxicity_targets,
            reduction="none",
        )
        toxicity_loss = (toxicity_loss_per_sample * sample_weights).mean()

        auxiliary_loss = F.binary_cross_entropy_with_logits(
            model_outputs["auxiliary_logits"],
            auxiliary_targets,
            reduction="mean",
        )

        identity_loss_per_sample = F.binary_cross_entropy_with_logits(
            model_outputs["identity_logits"],
            identity_targets,
            reduction="none",
        ).mean(dim=1)

        identity_available = (
            batch_labels["identity_labels_available"].bool().reshape(-1)
        )

        if identity_available.any():
            identity_loss = identity_loss_per_sample[identity_available].mean()
        else:
            identity_loss = model_outputs["toxicity_logit"].sum() * 0.0

        total_loss = (
            toxicity_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.adversarial_weight * identity_loss
        )

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "identity_adversarial_loss": identity_loss.detach(),
        }


backbone = base_model.deberta
del base_model

# Non-reentrant checkpointing preserves the backbone's memory savings without
# re-entering autograd through shared multi-head losses during backward passes.
if hasattr(backbone, "gradient_checkpointing_enable"):
    backbone.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )

model = BiasAwareDeberta(
    backbone=backbone,
    hidden_size=backbone.config.hidden_size,
    numeric_feature_count=len(NUMERIC_FEATURE_COLUMNS),
    identity_count=len(IDENTITY_COLUMNS),
    toxicity_aux_count=len(TOXICITY_AUX_COLUMNS),
    dropout_probability=0.15,
    adversarial_strength=0.08,
)

criterion = BiasAwareToxicityLoss(
    auxiliary_weight=0.20,
    adversarial_weight=0.08,
    subgroup_threshold=0.5,
)

optimizer = AdamW(
    [
        {
            "params": model.backbone.parameters(),
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": [
                parameter
                for name, parameter in model.named_parameters()
                if not name.startswith("backbone.")
            ],
            "lr": 2.0e-4,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=torch.cuda.is_available())

# =============================================================================
# Datasets and loaders
# =============================================================================


class ToxicityDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, labeled: bool):
        self.texts = frame["text_for_model"].fillna("[EMPTY]").astype(str).to_numpy()
        self.numeric_features = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.lengths = np.minimum(
            np.maximum(frame["text_for_model"].fillna("").str.len().to_numpy(), 1),
            MAX_LENGTH * 5,
        ).astype(np.int32)

        self.labeled = labeled

        if labeled:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.auxiliary_targets = frame[TOXICITY_AUX_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_targets = frame[IDENTITY_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_available = frame["identity_labels_available"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        encoded = tokenizer(
            self.texts[index],
            add_special_tokens=True,
            truncation=True,
            max_length=MAX_LENGTH,
            padding=False,
            return_attention_mask=True,
        )

        item = {
            "row_index": int(index),
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "numeric_features": self.numeric_features[index],
        }

        if self.labeled:
            item["target"] = self.targets[index]
            item["auxiliary_targets"] = self.auxiliary_targets[index]
            item["identity_targets"] = self.identity_targets[index]
            item["identity_labels_available"] = self.identity_available[index]

        return item


class LengthBucketBatchSampler(Sampler):
    def __init__(self, lengths, batch_size, shuffle, seed):
        self.lengths = np.asarray(lengths)
        self.batch_size = int(batch_size)
        self.shuffle = bool(shuffle)
        self.seed = int(seed)
        self.epoch = 0
        self.sorted_indices = np.argsort(self.lengths, kind="mergesort")

    def set_epoch(self, epoch):
        self.epoch = int(epoch)

    def __iter__(self):
        batches = [
            self.sorted_indices[start : start + self.batch_size].tolist()
            for start in range(0, len(self.sorted_indices), self.batch_size)
        ]

        if self.shuffle:
            rng = np.random.default_rng(self.seed + self.epoch)
            mega_batch_size = 64

            mega_batches = [
                batches[start : start + mega_batch_size]
                for start in range(0, len(batches), mega_batch_size)
            ]

            rng.shuffle(mega_batches)

            for mega_batch in mega_batches:
                rng.shuffle(mega_batch)
                for batch in mega_batch:
                    yield batch
        else:
            for batch in batches:
                yield batch

    def __len__(self):
        return math.ceil(len(self.sorted_indices) / self.batch_size)


def collate_batch(samples):
    token_features = [
        {
            "input_ids": sample["input_ids"],
            "attention_mask": sample["attention_mask"],
        }
        for sample in samples
    ]

    padded_tokens = tokenizer.pad(
        token_features,
        padding=True,
        pad_to_multiple_of=8 if device.type == "cuda" else None,
        return_tensors="pt",
    )

    batch = {
        "row_index": torch.tensor(
            [sample["row_index"] for sample in samples],
            dtype=torch.long,
        ),
        "input_ids": padded_tokens["input_ids"],
        "attention_mask": padded_tokens["attention_mask"],
        "numeric_features": torch.from_numpy(
            np.stack([sample["numeric_features"] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        ),
    }

    if "target" in samples[0]:
        batch["target"] = torch.tensor(
            [sample["target"] for sample in samples],
            dtype=torch.float32,
        )
        batch["auxiliary_targets"] = torch.from_numpy(
            np.stack([sample["auxiliary_targets"] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        )
        batch["identity_targets"] = torch.from_numpy(
            np.stack([sample["identity_targets"] for sample in samples]).astype(
                np.float32,
                copy=False,
            )
        )
        batch["identity_labels_available"] = torch.tensor(
            [sample["identity_labels_available"] for sample in samples],
            dtype=torch.float32,
        )

    return batch


def make_loader(dataset, batch_size, shuffle, seed):
    sampler = LengthBucketBatchSampler(
        lengths=dataset.lengths,
        batch_size=batch_size,
        shuffle=shuffle,
        seed=seed,
    )

    return DataLoader(
        dataset,
        batch_sampler=sampler,
        num_workers=NUM_WORKERS,
        pin_memory=pin_memory,
        persistent_workers=NUM_WORKERS > 0,
        collate_fn=collate_batch,
    )


def move_model_batch_to_device(batch):
    return {
        "input_ids": batch["input_ids"].to(device, non_blocking=True),
        "attention_mask": batch["attention_mask"].to(device, non_blocking=True),
        "numeric_features": batch["numeric_features"].to(device, non_blocking=True),
        "target": batch["target"].to(device, non_blocking=True),
        "auxiliary_targets": batch["auxiliary_targets"].to(
            device,
            non_blocking=True,
        ),
        "identity_targets": batch["identity_targets"].to(
            device,
            non_blocking=True,
        ),
        "identity_labels_available": batch["identity_labels_available"].to(
            device,
            non_blocking=True,
        ),
    }


# =============================================================================
# Official metric and inference
# =============================================================================


def predict_with_model(inference_model, loader, expected_rows):
    inference_model.eval()
    predictions = np.empty(expected_rows, dtype=np.float32)
    seen = np.zeros(expected_rows, dtype=np.bool_)

    with torch.no_grad():
        for batch in loader:
            row_indices = batch["row_index"].numpy()

            model_inputs = {
                "input_ids": batch["input_ids"].to(device, non_blocking=True),
                "attention_mask": batch["attention_mask"].to(
                    device,
                    non_blocking=True,
                ),
                "numeric_features": batch["numeric_features"].to(
                    device,
                    non_blocking=True,
                ),
            }

            with torch.cuda.amp.autocast(enabled=device.type == "cuda"):
                outputs = inference_model(**model_inputs)
                batch_predictions = torch.sigmoid(outputs["toxicity_logit"]).float()

            predictions[row_indices] = batch_predictions.detach().cpu().numpy()
            seen[row_indices] = True

    if not seen.all() or not np.isfinite(predictions).all():
        raise RuntimeError("Inference did not produce one finite prediction per row.")

    return np.clip(predictions, 1e-7, 1.0 - 1e-7)


def checked_auc(y_true, y_score, metric_name):
    y_true = np.asarray(y_true, dtype=np.int8)

    if np.unique(y_true).size != 2:
        raise RuntimeError(
            f"{metric_name} is undefined because its subset has only one class."
        )

    return float(roc_auc_score(y_true, y_score))


def power_mean(values, power=-5):
    values = np.clip(np.asarray(values, dtype=np.float64), 1e-12, 1.0)
    return float(np.mean(values**power) ** (1.0 / power))


def official_bias_aware_score(validation_frame, predictions):
    binary_target = validation_frame["target_binary"].to_numpy(dtype=np.int8)
    identity_annotation_available = validation_frame[
        "identity_labels_available"
    ].to_numpy(dtype=np.bool_)

    overall_auc = checked_auc(binary_target, predictions, "overall_auc")

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in OFFICIAL_IDENTITY_COLUMNS:
        subgroup_member = (
            validation_frame[identity_column].to_numpy(dtype=np.float32) >= 0.5
        )

        subgroup_mask = subgroup_member

        bpsn_mask = (subgroup_member & (binary_target == 0)) | (
            (~subgroup_member) & (binary_target == 1)
        )

        bnsp_mask = (subgroup_member & (binary_target == 1)) | (
            (~subgroup_member) & (binary_target == 0)
        )

        subgroup_auc = checked_auc(
            binary_target[subgroup_mask],
            predictions[subgroup_mask],
            f"{identity_column}_subgroup_auc",
        )

        bpsn_auc = checked_auc(
            binary_target[bpsn_mask],
            predictions[bpsn_mask],
            f"{identity_column}_bpsn_auc",
        )

        bnsp_auc = checked_auc(
            binary_target[bnsp_mask],
            predictions[bnsp_mask],
            f"{identity_column}_bnsp_auc",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity[identity_column] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
            "annotated_validation_rows": int(identity_annotation_available.sum()),
            "subgroup_rows": int(subgroup_mask.sum()),
        }

    subgroup_power_mean = power_mean(subgroup_aucs, power=-5)
    bpsn_power_mean = power_mean(bpsn_aucs, power=-5)
    bnsp_power_mean = power_mean(bnsp_aucs, power=-5)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    return final_score, {
        "overall_auc": overall_auc,
        "subgroup_power_mean_auc": subgroup_power_mean,
        "bpsn_power_mean_auc": bpsn_power_mean,
        "bnsp_power_mean_auc": bnsp_power_mean,
        "official_final_score": final_score,
        "identity_metric_population": "validation rows with identity annotations",
        "per_identity": per_identity,
    }


# =============================================================================
# Training, checkpoint selection, validation, and submission
# =============================================================================

if not set(OFFICIAL_IDENTITY_COLUMNS).issubset(set(IDENTITY_COLUMNS)):
    raise ValueError("Official identity columns are missing.")

train_dataset = ToxicityDataset(train_processed, labeled=True)
validation_dataset = ToxicityDataset(valid_processed, labeled=True)
test_dataset = ToxicityDataset(test_processed, labeled=False)

train_loader = make_loader(
    train_dataset,
    TRAIN_BATCH_SIZE,
    shuffle=True,
    seed=SEED,
)

validation_loader = make_loader(
    validation_dataset,
    EVAL_BATCH_SIZE,
    shuffle=False,
    seed=SEED,
)

test_loader = make_loader(
    test_dataset,
    EVAL_BATCH_SIZE,
    shuffle=False,
    seed=SEED,
)

model = model.to(device)

if device.type == "cuda" and torch.cuda.device_count() > 1:
    model = torch.nn.DataParallel(model)

optimizer.zero_grad(set_to_none=True)

steps_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_optimizer_steps = max(1, steps_per_epoch * NUM_EPOCHS)
warmup_steps = max(1, int(total_optimizer_steps * WARMUP_FRACTION))


def learning_rate_multiplier(step):
    if step < warmup_steps:
        return float(step + 1) / float(warmup_steps)

    progress = float(step - warmup_steps) / float(
        max(1, total_optimizer_steps - warmup_steps)
    )

    return max(
        0.05,
        0.5 * (1.0 + math.cos(math.pi * min(progress, 1.0))),
    )


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)

best_score = -float("inf")
best_epoch = -1
epochs_without_improvement = 0

for epoch in range(1, NUM_EPOCHS + 1):
    train_loader.batch_sampler.set_epoch(epoch)
    model.train()

    epoch_loss_sum = 0.0
    epoch_sample_count = 0

    optimizer.zero_grad(set_to_none=True)

    for batch_number, batch in enumerate(train_loader, start=1):
        model_batch = move_model_batch_to_device(batch)
        batch_size = model_batch["target"].shape[0]

        with torch.cuda.amp.autocast(enabled=device.type == "cuda"):
            model_outputs = model(
                input_ids=model_batch["input_ids"],
                attention_mask=model_batch["attention_mask"],
                numeric_features=model_batch["numeric_features"],
                toxicity_condition=model_batch["target"],
            )

            loss_outputs = criterion(model_outputs, model_batch)
            unscaled_loss = loss_outputs["loss"]
            loss = unscaled_loss / GRADIENT_ACCUMULATION_STEPS

        amp_scaler.scale(loss).backward()

        epoch_loss_sum += float(unscaled_loss.detach().cpu()) * batch_size
        epoch_sample_count += batch_size

        should_step = (
            batch_number % GRADIENT_ACCUMULATION_STEPS == 0
            or batch_number == len(train_loader)
        )

        if should_step:
            amp_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

    validation_predictions = predict_with_model(
        model,
        validation_loader,
        expected_rows=len(validation_dataset),
    )

    epoch_score, epoch_metrics = official_bias_aware_score(
        valid_processed,
        validation_predictions,
    )

    mean_train_loss = epoch_loss_sum / max(1, epoch_sample_count)

    print(
        f"Epoch {epoch}/{NUM_EPOCHS} | train_loss={mean_train_loss:.6f} | "
        f"official_bias_score={epoch_score:.6f} | "
        f"overall_auc={epoch_metrics['overall_auc']:.6f} | "
        f"bpsn_pm={epoch_metrics['bpsn_power_mean_auc']:.6f}"
    )

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        state_dict = (
            model.module.state_dict()
            if isinstance(model, torch.nn.DataParallel)
            else model.state_dict()
        )

        torch.save(
            {
                "epoch": epoch,
                "official_score": epoch_score,
                "model_state_dict": state_dict,
                "metrics": epoch_metrics,
            },
            CHECKPOINT_PATH,
        )

        with open(METRICS_PATH, "w", encoding="utf-8") as metrics_file:
            json.dump(
                {
                    "best_epoch": best_epoch,
                    "split": "duplicate-group-isolated hash holdout",
                    "metric": ("official overall AUC plus three p=-5 bias power means"),
                    **epoch_metrics,
                },
                metrics_file,
                indent=2,
            )
    else:
        epochs_without_improvement += 1

        if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
            break

if not CHECKPOINT_PATH.exists():
    raise RuntimeError("No validation checkpoint was saved.")

best_checkpoint = torch.load(CHECKPOINT_PATH, map_location=device)

inference_model = model.module if isinstance(model, torch.nn.DataParallel) else model

inference_model.load_state_dict(
    best_checkpoint["model_state_dict"],
    strict=True,
)

final_validation_predictions = predict_with_model(
    inference_model,
    validation_loader,
    expected_rows=len(validation_dataset),
)

score, final_metrics = official_bias_aware_score(
    valid_processed,
    final_validation_predictions,
)

test_predictions = predict_with_model(
    inference_model,
    test_loader,
    expected_rows=len(test_dataset),
)

submission = pd.DataFrame(
    {
        "id": test_processed["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if len(submission) != len(test_processed) or submission["id"].duplicated().any():
    raise RuntimeError("Submission integrity check failed.")

if list(submission.columns) != ["id", "prediction"]:
    raise RuntimeError("Submission columns do not match the required format.")

submission.to_csv(SUBMISSION_PATH, index=False)

with open(METRICS_PATH, "w", encoding="utf-8") as metrics_file:
    json.dump(
        {
            "best_epoch": int(best_checkpoint["epoch"]),
            "split": "duplicate-group-isolated hash holdout",
            "metric": "official overall AUC plus three p=-5 bias power means",
            "submission_path": str(SUBMISSION_PATH),
            **final_metrics,
        },
        metrics_file,
        indent=2,
    )

print(f"Final Validation Score: {score}")