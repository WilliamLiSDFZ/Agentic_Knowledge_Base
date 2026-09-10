import os
os.sched_setaffinity(0, {5, 6})
import html
import json
import math
import os

# Release unused cached CUDA blocks between allocations rather than retaining
# fragmented segments while sharing the GPU with other active processes.
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import random
import re
import unicodedata

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

# =============================================================================
# Configuration
# =============================================================================

RANDOM_SEED = 2025

INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"

VALID_FOLD = 0
N_SPLITS = 10
MIXTURE_BALANCED_FRACTION = 0.30

# The large checkpoint cannot allocate AdamW state on the shared 22 GB GPU.
# The base checkpoint retains pretrained ModernBERT fine-tuning while fitting
# model weights, gradients, activations, and optimizer moments in memory.
MODEL_ID = "answerdotai/ModernBERT-base"
BACKBONE_LEARNING_RATE = 1.0e-5
CLASSIFIER_LEARNING_RATE = 2.0e-5
WEIGHT_DECAY = 0.01

NUM_EPOCHS = 1
# ModernBERT-large's activation memory is the OOM source.  The smaller
# micro-batch and checkpointed activations retain the original effective
# optimization batch size (8 * 4 = 16 * 2 = 32).
TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 8
GRADIENT_ACCUMULATION_STEPS = 4
MAX_LENGTH = 192
NUM_WORKERS = min(2, max(1, (os.cpu_count() or 2) // 2))
WARMUP_FRACTION = 0.06
MAX_GRAD_NORM = 1.0

BEST_CHECKPOINT_PATH = os.path.join(WORKING_DIR, "best_modernbert_toxicity.pt")
METRIC_HISTORY_PATH = os.path.join(WORKING_DIR, "metric_history.json")

EVAL_IDENTITY_COLUMNS = [
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

TEXT_FEATURE_NAMES = [
    "log_char_count",
    "log_word_count",
    "log_exclamation_count",
    "log_question_count",
    "log_repeated_punctuation_count",
    "log_digit_count",
    "log_url_count",
    "uppercase_ratio",
    "digit_ratio",
    "punctuation_ratio",
]

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True

# =============================================================================
# Data processing and feature engineering
# =============================================================================

train_raw = pd.read_csv(os.path.join(INPUT_DIR, "train.csv"))
test_raw = pd.read_csv(os.path.join(INPUT_DIR, "test.csv"))
sample_submission = pd.read_csv(os.path.join(INPUT_DIR, "sample_submission.csv"))

required_train_columns = {"id", "comment_text", "target", *EVAL_IDENTITY_COLUMNS}
missing_train_columns = required_train_columns.difference(train_raw.columns)

if missing_train_columns:
    raise ValueError(f"Missing required train columns: {sorted(missing_train_columns)}")

if list(sample_submission.columns) != ["id", "prediction"]:
    raise ValueError(
        "sample_submission.csv must contain exactly the columns ['id', 'prediction']."
    )

if not sample_submission["id"].equals(test_raw["id"]):
    raise ValueError("test.csv row order does not match sample_submission.csv.")

raw_text_for_groups = train_raw["comment_text"].fillna("").astype(str)
duplicate_group_id, _ = pd.factorize(raw_text_for_groups, sort=False)

binary_target = (train_raw["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)
identity_matrix = (
    train_raw[EVAL_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
)
any_evaluated_identity = identity_matrix.any(axis=1).astype(np.int8)

# Four strata:
# 0 = background non-toxic
# 1 = identity-mentioned non-toxic
# 2 = background toxic
# 3 = identity-mentioned toxic
split_stratum = (2 * binary_target + any_evaluated_identity).astype(np.int8)

splitter = StratifiedGroupKFold(
    n_splits=N_SPLITS,
    shuffle=True,
    random_state=RANDOM_SEED,
)

split_iter = splitter.split(
    X=np.empty((len(train_raw), 1), dtype=np.uint8),
    y=split_stratum,
    groups=duplicate_group_id,
)

for fold_index, (train_indices, valid_indices) in enumerate(split_iter):
    if fold_index == VALID_FOLD:
        break

if (
    np.intersect1d(
        duplicate_group_id[train_indices],
        duplicate_group_id[valid_indices],
    ).size
    != 0
):
    raise RuntimeError(
        "Duplicate comment groups overlap between training and validation."
    )

train_columns = ["id", "comment_text", "target"]
valid_columns = ["id", "comment_text", "target", *EVAL_IDENTITY_COLUMNS]

train_df = train_raw.loc[train_indices, train_columns].copy().reset_index(drop=True)
valid_df = train_raw.loc[valid_indices, valid_columns].copy().reset_index(drop=True)
test_df = test_raw.loc[:, ["id", "comment_text"]].copy().reset_index(drop=True)

train_stratum = split_stratum[train_indices]
valid_stratum = split_stratum[valid_indices]

del train_raw
del raw_text_for_groups
del duplicate_group_id
del identity_matrix
del any_evaluated_identity

html_break_pattern = re.compile(r"<\s*br\s*/?\s*>", flags=re.IGNORECASE)
url_pattern = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
email_pattern = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", flags=re.IGNORECASE)
user_pattern = re.compile(r"(?<!\w)@\w+")
control_pattern = re.compile(r"[\x00-\x08\x0b-\x1f\x7f-\x9f]")
whitespace_pattern = re.compile(r"\s+")


def clean_comment_text(value):
    if pd.isna(value):
        return "[EMPTY]"

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = html_break_pattern.sub(" ", text)
    text = url_pattern.sub(" <URL> ", text)
    text = email_pattern.sub(" <EMAIL> ", text)
    text = user_pattern.sub(" <USER> ", text)
    text = control_pattern.sub(" ", text)
    text = whitespace_pattern.sub(" ", text).strip()

    return text if text else "[EMPTY]"


for frame in (train_df, valid_df, test_df):
    frame["comment_text"] = (
        frame["comment_text"].map(clean_comment_text).astype("string")
    )


def build_text_features(text_series):
    text = text_series.fillna("[EMPTY]").astype(str)

    character_count = text.str.len().to_numpy(dtype=np.float32)
    word_count = text.str.count(r"\b\w+\b").to_numpy(dtype=np.float32)
    exclamation_count = text.str.count("!").to_numpy(dtype=np.float32)
    question_count = text.str.count(r"\?").to_numpy(dtype=np.float32)
    repeated_punctuation_count = text.str.count(r"[!?]{2,}").to_numpy(dtype=np.float32)
    digit_count = text.str.count(r"\d").to_numpy(dtype=np.float32)
    url_count = text.str.count(r"<URL>").to_numpy(dtype=np.float32)
    uppercase_count = text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    letter_count = text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    punctuation_count = text.str.count(r"[!?.,;:\-]").to_numpy(dtype=np.float32)

    safe_character_count = np.maximum(character_count, 1.0)
    safe_letter_count = np.maximum(letter_count, 1.0)

    return np.column_stack(
        [
            np.log1p(character_count),
            np.log1p(word_count),
            np.log1p(exclamation_count),
            np.log1p(question_count),
            np.log1p(repeated_punctuation_count),
            np.log1p(digit_count),
            np.log1p(url_count),
            uppercase_count / safe_letter_count,
            digit_count / safe_character_count,
            punctuation_count / safe_character_count,
        ]
    ).astype(np.float32)


train_text_features_raw = build_text_features(train_df["comment_text"])
valid_text_features_raw = build_text_features(valid_df["comment_text"])
test_text_features_raw = build_text_features(test_df["comment_text"])

text_feature_scaler = StandardScaler()

train_text_features = text_feature_scaler.fit_transform(train_text_features_raw).astype(
    np.float32
)
valid_text_features = text_feature_scaler.transform(valid_text_features_raw).astype(
    np.float32
)
test_text_features = text_feature_scaler.transform(test_text_features_raw).astype(
    np.float32
)

stratum_counts = np.bincount(train_stratum, minlength=4).astype(np.float64)

if np.any(stratum_counts == 0):
    raise ValueError("At least one toxicity-by-identity training stratum is empty.")

natural_probability = np.full(
    len(train_df),
    1.0 / len(train_df),
    dtype=np.float64,
)
balanced_probability = 1.0 / (4.0 * stratum_counts[train_stratum])

mixture_probability = (
    1.0 - MIXTURE_BALANCED_FRACTION
) * natural_probability + MIXTURE_BALANCED_FRACTION * balanced_probability

train_sampling_weight = (mixture_probability / mixture_probability.mean()).astype(
    np.float32
)

train_df["sampling_stratum"] = train_stratum.astype(np.int8)
train_df["sampling_weight"] = train_sampling_weight

train_labels = train_df["target"].to_numpy(dtype=np.float32)
valid_labels = valid_df["target"].to_numpy(dtype=np.float32)

valid_identity_labels = (
    valid_df[EVAL_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
)

train_df.to_pickle(os.path.join(WORKING_DIR, "prepared_train.pkl"))
valid_df.to_pickle(os.path.join(WORKING_DIR, "prepared_validation.pkl"))
test_df.to_pickle(os.path.join(WORKING_DIR, "prepared_test.pkl"))

np.savez_compressed(
    os.path.join(WORKING_DIR, "prepared_text_features.npz"),
    train_features=train_text_features,
    validation_features=valid_text_features,
    test_features=test_text_features,
    train_labels=train_labels,
    validation_labels=valid_labels,
    validation_identity_labels=valid_identity_labels,
    validation_strata=valid_stratum.astype(np.int8),
    train_ids=train_df["id"].to_numpy(),
    validation_ids=valid_df["id"].to_numpy(),
    test_ids=test_df["id"].to_numpy(),
    feature_names=np.asarray(TEXT_FEATURE_NAMES),
)

joblib.dump(
    text_feature_scaler,
    os.path.join(WORKING_DIR, "text_feature_scaler.joblib"),
)

# =============================================================================
# Model design
# =============================================================================

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = ModernBertForSequenceClassification.from_pretrained(
    MODEL_ID,
    num_labels=1,
    problem_type="regression",
)

model.config.pad_token_id = tokenizer.pad_token_id


def weighted_soft_toxicity_bce(
    logits: torch.Tensor,
    targets: torch.Tensor,
    sample_weights: torch.Tensor | None = None,
) -> torch.Tensor:
    """Soft-label BCE for fractional human toxicity annotations."""
    logits = logits.reshape(-1)
    targets = targets.to(dtype=logits.dtype).reshape(-1).clamp_(0.0, 1.0)

    per_example_loss = F.binary_cross_entropy_with_logits(
        logits,
        targets,
        reduction="none",
    )

    if sample_weights is None:
        return per_example_loss.mean()

    sample_weights = sample_weights.to(
        device=logits.device,
        dtype=logits.dtype,
    ).reshape(-1)

    if sample_weights.numel() != per_example_loss.numel():
        raise ValueError("sample_weights must contain one value per example.")

    return (per_example_loss * sample_weights).sum() / sample_weights.sum().clamp_min(
        torch.finfo(logits.dtype).eps
    )


criterion = weighted_soft_toxicity_bce

classifier_parameters = []
backbone_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    if parameter_name.startswith("classifier."):
        classifier_parameters.append(parameter)
    else:
        backbone_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": BACKBONE_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
        {
            "params": classifier_parameters,
            "lr": CLASSIFIER_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
    ],
    betas=(0.9, 0.999),
    eps=1.0e-8,
)

# =============================================================================
# Training and evaluation
# =============================================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

if device.type == "cuda":
    # The failed run retained a substantial reserved-but-unallocated cache.
    torch.cuda.empty_cache()

if hasattr(model.config, "use_cache"):
    model.config.use_cache = False

# Recompute transformer activations during backward instead of retaining every
# layer activation from the forward pass, substantially reducing CUDA demand.
model.gradient_checkpointing_enable()


class ToxicityTextDataset(Dataset):
    def __init__(self, texts, labels=None, sample_weights=None):
        self.texts = texts
        self.labels = labels
        self.sample_weights = sample_weights

        if self.labels is not None and len(self.texts) != len(self.labels):
            raise ValueError("Texts and labels must have equal lengths.")

        if self.sample_weights is not None and len(self.texts) != len(
            self.sample_weights
        ):
            raise ValueError("Texts and sample weights must have equal lengths.")

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.labels is None:
            return str(self.texts[index])

        weight = (
            float(self.sample_weights[index])
            if self.sample_weights is not None
            else 1.0
        )

        return str(self.texts[index]), float(self.labels[index]), weight


class TransformerBatchCollator:
    def __init__(self, tokenizer_instance, max_length, include_labels):
        self.tokenizer_instance = tokenizer_instance
        self.max_length = max_length
        self.include_labels = include_labels

    def __call__(self, batch):
        if self.include_labels:
            texts, labels, weights = zip(*batch)
        else:
            texts = batch

        encoded = self.tokenizer_instance(
            list(texts),
            truncation=True,
            max_length=self.max_length,
            padding=True,
            pad_to_multiple_of=8,
            return_tensors="pt",
        )

        encoded.pop("token_type_ids", None)

        if self.include_labels:
            encoded["targets"] = torch.tensor(labels, dtype=torch.float32)
            encoded["sample_weights"] = torch.tensor(weights, dtype=torch.float32)

        return encoded


class CappedMixtureStratifiedOrderingSampler(Sampler):
    """
    Uses the predefined 70/30 natural/balanced mixture to front-load
    metric-critical strata while retaining every unique training row once
    per epoch and avoiding repeated rare-example oversampling.
    """

    def __init__(self, strata, balanced_fraction, seed):
        self.strata = np.asarray(strata, dtype=np.int64)
        self.balanced_fraction = float(balanced_fraction)
        self.seed = int(seed)
        self.epoch = 0
        self.unique_strata = np.unique(self.strata)

        self.indices_by_stratum = {
            int(stratum): np.flatnonzero(self.strata == stratum)
            for stratum in self.unique_strata
        }

    def __len__(self):
        return len(self.strata)

    def __iter__(self):
        rng = np.random.default_rng(self.seed + self.epoch)
        self.epoch += 1

        total_count = len(self.strata)
        balanced_share = self.balanced_fraction * total_count / len(self.unique_strata)

        prioritized_parts = []
        remaining_parts = []

        for stratum in self.unique_strata:
            indices = self.indices_by_stratum[int(stratum)].copy()
            rng.shuffle(indices)

            natural_share = (1.0 - self.balanced_fraction) * len(indices)
            capped_count = min(
                len(indices),
                int(round(natural_share + balanced_share)),
            )

            prioritized_parts.append(indices[:capped_count])
            remaining_parts.append(indices[capped_count:])

        prioritized = np.concatenate(prioritized_parts)
        remaining = np.concatenate(remaining_parts)

        rng.shuffle(prioritized)
        rng.shuffle(remaining)

        return iter(np.concatenate([prioritized, remaining]).tolist())


train_texts = train_df["comment_text"].to_numpy(dtype=object, copy=False)
valid_texts = valid_df["comment_text"].to_numpy(dtype=object, copy=False)
test_texts = test_df["comment_text"].to_numpy(dtype=object, copy=False)

train_targets = train_labels.astype(np.float32, copy=False)
validation_targets = valid_labels.astype(np.float32, copy=False)

train_sample_weights = train_df["sampling_weight"].to_numpy(
    dtype=np.float32,
    copy=False,
)

train_strata_for_sampler = train_df["sampling_stratum"].to_numpy(
    dtype=np.int8,
    copy=False,
)

train_dataset = ToxicityTextDataset(
    texts=train_texts,
    labels=train_targets,
    sample_weights=train_sample_weights,
)

validation_dataset = ToxicityTextDataset(
    texts=valid_texts,
    labels=validation_targets,
)

test_dataset = ToxicityTextDataset(texts=test_texts)

train_collator = TransformerBatchCollator(
    tokenizer_instance=tokenizer,
    max_length=MAX_LENGTH,
    include_labels=True,
)

inference_collator = TransformerBatchCollator(
    tokenizer_instance=tokenizer,
    max_length=MAX_LENGTH,
    include_labels=False,
)

train_sampler = CappedMixtureStratifiedOrderingSampler(
    strata=train_strata_for_sampler,
    balanced_fraction=MIXTURE_BALANCED_FRACTION,
    seed=RANDOM_SEED,
)

loader_options = {
    "num_workers": NUM_WORKERS,
    "pin_memory": device.type == "cuda",
    "persistent_workers": NUM_WORKERS > 0,
    "prefetch_factor": 2,
}

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    sampler=train_sampler,
    collate_fn=train_collator,
    drop_last=False,
    **loader_options,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=INFERENCE_BATCH_SIZE,
    shuffle=False,
    collate_fn=inference_collator,
    drop_last=False,
    **loader_options,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=INFERENCE_BATCH_SIZE,
    shuffle=False,
    collate_fn=inference_collator,
    drop_last=False,
    **loader_options,
)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_optimizer_steps = max(1, NUM_EPOCHS * updates_per_epoch)
warmup_steps = max(1, int(WARMUP_FRACTION * total_optimizer_steps))


def learning_rate_multiplier(step):
    if step < warmup_steps:
        return float(step + 1) / float(warmup_steps)

    remaining_steps = max(1, total_optimizer_steps - warmup_steps)

    return max(
        0.0,
        float(total_optimizer_steps - step) / float(remaining_steps),
    )


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)

amp_enabled = device.type == "cuda"
scaler = torch.amp.GradScaler("cuda", enabled=amp_enabled)


def predict_probabilities(data_loader):
    model.eval()
    prediction_chunks = []

    with torch.no_grad():
        for encoded_batch in data_loader:
            model_inputs = {
                key: value.to(device, non_blocking=True)
                for key, value in encoded_batch.items()
            }

            with torch.autocast(
                device_type=device.type,
                dtype=torch.float16,
                enabled=amp_enabled,
            ):
                logits = model(**model_inputs).logits.reshape(-1)

            prediction_chunks.append(torch.sigmoid(logits).float().cpu().numpy())

    predictions = np.concatenate(prediction_chunks).astype(np.float64, copy=False)

    if not np.all(np.isfinite(predictions)):
        raise RuntimeError("Model inference produced non-finite probabilities.")

    return predictions


def _strict_binary_auc(labels, predictions, subset_name):
    labels = np.asarray(labels, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if labels.size == 0 or np.unique(labels).size != 2:
        raise ValueError(
            f"Official AUC is undefined for '{subset_name}': "
            f"{labels.size} rows with classes {np.unique(labels).tolist()}."
        )

    return float(roc_auc_score(labels, predictions))


def compute_official_bias_metric(targets, predictions, identity_values):
    """
    Official competition metric:
      0.25 * overall AUC +
      0.25 * generalized mean of subgroup AUCs +
      0.25 * generalized mean of BPSN AUCs +
      0.25 * generalized mean of BNSP AUCs.
    """
    binary_targets = (np.asarray(targets, dtype=np.float32) >= 0.5).astype(np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)
    identity_values = np.asarray(identity_values, dtype=np.float32)

    if len(binary_targets) != len(predictions):
        raise ValueError("Targets and predictions must have equal lengths.")

    expected_identity_shape = (
        len(binary_targets),
        len(EVAL_IDENTITY_COLUMNS),
    )

    if identity_values.shape != expected_identity_shape:
        raise ValueError(
            "Identity matrix shape does not match the evaluation identities."
        )

    overall_auc = _strict_binary_auc(
        binary_targets,
        predictions,
        "overall",
    )

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = []

    for column_index, identity_name in enumerate(EVAL_IDENTITY_COLUMNS):
        subgroup = identity_values[:, column_index] >= 0.5
        background = ~subgroup

        subgroup_auc = _strict_binary_auc(
            binary_targets[subgroup],
            predictions[subgroup],
            f"{identity_name}/subgroup",
        )

        bpsn_mask = (subgroup & (binary_targets == 0)) | (
            background & (binary_targets == 1)
        )

        bpsn_auc = _strict_binary_auc(
            binary_targets[bpsn_mask],
            predictions[bpsn_mask],
            f"{identity_name}/BPSN",
        )

        bnsp_mask = (subgroup & (binary_targets == 1)) | (
            background & (binary_targets == 0)
        )

        bnsp_auc = _strict_binary_auc(
            binary_targets[bnsp_mask],
            predictions[bnsp_mask],
            f"{identity_name}/BNSP",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity.append(
            {
                "identity": identity_name,
                "subgroup_auc": subgroup_auc,
                "bpsn_auc": bpsn_auc,
                "bnsp_auc": bnsp_auc,
            }
        )

    def generalized_mean(values, power=-5.0):
        values = np.asarray(values, dtype=np.float64)
        return float(np.mean(np.power(values, power)) ** (1.0 / power))

    subgroup_mean = generalized_mean(subgroup_aucs)
    bpsn_mean = generalized_mean(bpsn_aucs)
    bnsp_mean = generalized_mean(bnsp_aucs)

    final_score = 0.25 * (overall_auc + subgroup_mean + bpsn_mean + bnsp_mean)

    metric_details = {
        "overall_auc": overall_auc,
        "subgroup_generalized_mean_auc": subgroup_mean,
        "bpsn_generalized_mean_auc": bpsn_mean,
        "bnsp_generalized_mean_auc": bnsp_mean,
        "official_score": float(final_score),
        "per_identity": per_identity,
    }

    return float(final_score), metric_details


best_score = -np.inf
best_epoch = -1
metric_history = []

for epoch in range(NUM_EPOCHS):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    weighted_loss_sum = 0.0
    weight_sum = 0.0
    accumulation_count = 0

    for batch_index, encoded_batch in enumerate(train_loader):
        targets = encoded_batch.pop("targets").to(device, non_blocking=True)
        sample_weights = encoded_batch.pop("sample_weights").to(
            device,
            non_blocking=True,
        )

        model_inputs = {
            key: value.to(device, non_blocking=True)
            for key, value in encoded_batch.items()
        }

        with torch.autocast(
            device_type=device.type,
            dtype=torch.float16,
            enabled=amp_enabled,
        ):
            logits = model(**model_inputs).logits
            batch_loss = criterion(
                logits=logits,
                targets=targets,
                sample_weights=sample_weights,
            )

        scaler.scale(batch_loss / GRADIENT_ACCUMULATION_STEPS).backward()
        accumulation_count += 1

        weighted_loss_sum += float(batch_loss.detach().item()) * float(
            sample_weights.sum().item()
        )
        weight_sum += float(sample_weights.sum().item())

        should_step = (
            accumulation_count == GRADIENT_ACCUMULATION_STEPS
            or batch_index + 1 == len(train_loader)
        )

        if should_step:
            scaler.unscale_(optimizer)

            if accumulation_count != GRADIENT_ACCUMULATION_STEPS:
                correction = GRADIENT_ACCUMULATION_STEPS / accumulation_count

                for parameter_group in optimizer.param_groups:
                    for parameter in parameter_group["params"]:
                        if parameter.grad is not None:
                            parameter.grad.mul_(correction)

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                MAX_GRAD_NORM,
            )

            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

            accumulation_count = 0

    validation_predictions = predict_probabilities(validation_loader)

    epoch_score, epoch_metric_details = compute_official_bias_metric(
        targets=validation_targets,
        predictions=validation_predictions,
        identity_values=valid_identity_labels,
    )

    epoch_record = {
        "epoch": int(epoch + 1),
        "train_weighted_bce": float(weighted_loss_sum / max(weight_sum, 1e-12)),
        **epoch_metric_details,
    }

    metric_history.append(epoch_record)

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch

        torch.save(
            {
                "epoch": int(epoch),
                "official_validation_score": float(epoch_score),
                "model_state_dict": model.state_dict(),
            },
            BEST_CHECKPOINT_PATH,
        )

        np.save(
            os.path.join(WORKING_DIR, "best_validation_predictions.npy"),
            validation_predictions.astype(np.float32),
        )

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"loss={epoch_record['train_weighted_bce']:.6f} "
        f"official_auc={epoch_score:.6f}"
    )

with open(METRIC_HISTORY_PATH, "w", encoding="utf-8") as metric_file:
    json.dump(
        {
            "selection_metric": "official_overall_and_bias_generalized_auc",
            "best_epoch": int(best_epoch + 1),
            "best_score": float(best_score),
            "epochs": metric_history,
        },
        metric_file,
        indent=2,
    )

if best_epoch < 0 or not os.path.exists(BEST_CHECKPOINT_PATH):
    raise RuntimeError("No valid model checkpoint was created.")

checkpoint = torch.load(BEST_CHECKPOINT_PATH, map_location=device)
model.load_state_dict(checkpoint["model_state_dict"], strict=True)
del checkpoint

best_validation_predictions = predict_probabilities(validation_loader)

score, final_metric_details = compute_official_bias_metric(
    targets=validation_targets,
    predictions=best_validation_predictions,
    identity_values=valid_identity_labels,
)

with open(
    os.path.join(WORKING_DIR, "final_validation_metric.json"),
    "w",
    encoding="utf-8",
) as metric_file:
    json.dump(final_metric_details, metric_file, indent=2)

test_predictions = predict_probabilities(test_loader)

if len(test_predictions) != len(test_df):
    raise RuntimeError("Test prediction count does not match the test dataframe.")

submission = pd.DataFrame(
    {
        "id": test_df["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

submission_path = os.path.join(SUBMISSION_DIR, "submission_3d7d33a2797c414eb809ae73e113a24a.csv")
submission.to_csv(submission_path, index=False)

if list(submission.columns) != ["id", "prediction"]:
    raise RuntimeError("Submission columns do not match the required format.")

if len(submission) != len(test_df):
    raise RuntimeError("Submission row count does not match the test set.")

print(f"Final Validation Score: {score}")
