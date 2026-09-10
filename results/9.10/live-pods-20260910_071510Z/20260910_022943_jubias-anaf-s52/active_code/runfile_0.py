import os
os.sched_setaffinity(0, {9, 7})
import gc
import html
import json
import math
import os
import random
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2025
TRAINING_SEED = 2025
N_SPLITS = 10
VALID_FOLD = 0
IDENTITY_THRESHOLD = 0.5
SAMPLER_WEIGHT_MIN = 0.25
SAMPLER_WEIGHT_MAX = 5.0

# ModernBERT-large exceeded the GPU memory available alongside other processes.
# Shorter sequences, smaller micro-batches, and equivalent effective batch size prevent OOM.
MAX_LENGTH = 128
TRAIN_BATCH_SIZE = 2
EVAL_BATCH_SIZE = 4
GRADIENT_ACCUMULATION_STEPS = 12
NUM_EPOCHS = 1
NUM_WORKERS = 2
WARMUP_FRACTION = 0.02
MAX_GRAD_NORM = 1.0
POWER_MEAN_P = -5.0

BACKBONE_LEARNING_RATE = 1.2e-5
CLASSIFIER_LEARNING_RATE = 6.0e-5
WEIGHT_DECAY = 0.01

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"

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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

REQUIRED_TRAIN_COLUMNS = (
    ["id", "comment_text", "target"] + AUXILIARY_TARGET_COLUMNS + IDENTITY_COLUMNS
)
REQUIRED_TEST_COLUMNS = ["id", "comment_text"]

URL_PATTERN = re.compile(
    r"\b(?:https?://|www\.)[^\s<>()\[\]{}]+|"
    r"\b[a-z0-9.-]+\.(?:com|org|net|edu|gov|io|co|uk|ca|au)"
    r"(?:/[^\s<>()\[\]{}]*)?",
    flags=re.IGNORECASE,
)
EMAIL_PATTERN = re.compile(
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    flags=re.IGNORECASE,
)
USER_PATTERN = re.compile(r"(?<!\w)@\w+")
HTML_TAG_PATTERN = re.compile(r"<[^>\n]+>")
WHITESPACE_PATTERN = re.compile(r"\s+")


def clean_comment(value):
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = URL_PATTERN.sub(" urltoken ", text)
    text = EMAIL_PATTERN.sub(" emailtoken ", text)
    text = USER_PATTERN.sub(" usertoken ", text)
    text = HTML_TAG_PATTERN.sub(" ", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text


def add_text_features(frame):
    cleaned_text = frame["comment_text"].map(clean_comment).astype(str)
    frame["comment_text"] = cleaned_text

    char_count = cleaned_text.str.len().astype(np.float32)
    word_count = cleaned_text.str.count(r"\S+").astype(np.float32)
    alpha_count = cleaned_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = cleaned_text.str.count(r"[A-Z]").astype(np.float32)

    frame["text_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["text_log_word_count"] = np.log1p(word_count).astype(np.float32)
    frame["text_log_exclamation_count"] = np.log1p(
        cleaned_text.str.count("!").astype(np.float32)
    ).astype(np.float32)
    frame["text_log_question_count"] = np.log1p(
        cleaned_text.str.count(r"\?").astype(np.float32)
    ).astype(np.float32)
    frame["text_log_newline_count"] = np.log1p(
        cleaned_text.str.count("\n").astype(np.float32)
    ).astype(np.float32)
    frame["text_uppercase_fraction"] = (
        uppercase_count / np.maximum(alpha_count, 1.0)
    ).astype(np.float32)
    frame["text_has_url"] = cleaned_text.str.contains("urltoken", regex=False).astype(
        np.int8
    )
    frame["text_has_email"] = cleaned_text.str.contains(
        "emailtoken", regex=False
    ).astype(np.int8)
    frame["text_has_user_mention"] = cleaned_text.str.contains(
        "usertoken", regex=False
    ).astype(np.int8)

    return frame


def add_identity_features(frame, has_target):
    identity_values = frame[IDENTITY_COLUMNS]
    identity_known = identity_values.notna().any(axis=1)
    identity_mentioned = identity_values.ge(IDENTITY_THRESHOLD).any(axis=1)

    frame["identity_labels_available"] = identity_known.astype(np.int8)
    frame["identity_union"] = identity_mentioned.astype(np.int8)

    if has_target:
        frame["target_binary"] = (frame["target"] >= IDENTITY_THRESHOLD).astype(np.int8)

    return frame


def save_feature_table(frame, stem):
    parquet_path = WORKING_DIR / f"{stem}.parquet"
    try:
        frame.to_parquet(parquet_path, index=False, compression="zstd")
        return str(parquet_path)
    except Exception:
        pickle_path = WORKING_DIR / f"{stem}.pkl"
        frame.to_pickle(pickle_path)
        return str(pickle_path)


def read_feature_table(path_value):
    path = Path(path_value)
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    if path.suffix in {".pkl", ".pickle"}:
        return pd.read_pickle(path)
    raise ValueError(f"Unsupported feature-table format: {path}")


def checked_auc(binary_labels, predictions, subset_mask, metric_name):
    subset_labels = binary_labels[subset_mask]
    subset_predictions = predictions[subset_mask]

    if subset_labels.size == 0 or np.unique(subset_labels).size != 2:
        raise RuntimeError(
            f"{metric_name} is undefined on this validation fold because it does not "
            "contain both toxic and non-toxic examples."
        )

    return float(roc_auc_score(subset_labels, subset_predictions))


def generalized_mean(metric_values, power=POWER_MEAN_P):
    values = np.asarray(metric_values, dtype=np.float64)
    if values.size == 0 or not np.isfinite(values).all() or (values <= 0).any():
        raise RuntimeError("Bias AUC values must be finite and positive.")
    return float(np.mean(values**power) ** (1.0 / power))


def official_competition_metric(target_values, prediction_values, identity_values):
    if len(target_values) != len(prediction_values):
        raise ValueError("Targets and predictions must have identical lengths.")

    target_binary = np.asarray(target_values >= 0.5, dtype=bool)
    predictions = np.asarray(prediction_values, dtype=np.float64)

    overall_auc = checked_auc(
        target_binary,
        predictions,
        np.ones(len(target_binary), dtype=bool),
        "overall_auc",
    )

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in OFFICIAL_IDENTITY_COLUMNS:
        subgroup = (
            identity_values[identity_column].fillna(0.0).to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_auc = checked_auc(
            target_binary,
            predictions,
            subgroup,
            f"{identity_column}_subgroup_auc",
        )

        bpsn_mask = (subgroup & ~target_binary) | (~subgroup & target_binary)
        bpsn_auc = checked_auc(
            target_binary,
            predictions,
            bpsn_mask,
            f"{identity_column}_bpsn_auc",
        )

        bnsp_mask = (subgroup & target_binary) | (~subgroup & ~target_binary)
        bnsp_auc = checked_auc(
            target_binary,
            predictions,
            bnsp_mask,
            f"{identity_column}_bnsp_auc",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)
        per_identity[identity_column] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
        }

    subgroup_power_mean = generalized_mean(subgroup_aucs)
    bpsn_power_mean = generalized_mean(bpsn_aucs)
    bnsp_power_mean = generalized_mean(bnsp_aucs)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    details = {
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
        "official_final_score": final_score,
        "per_identity": per_identity,
    }
    return final_score, details


class ToxicityTextDataset(Dataset):
    def __init__(self, texts, targets=None):
        self.texts = texts
        self.targets = targets

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.targets is None:
            return self.texts[index]
        return self.texts[index], self.targets[index]


class ToxicityBatchCollator:
    def __init__(self, tokenizer_instance, max_length, with_targets):
        self.tokenizer_instance = tokenizer_instance
        self.max_length = max_length
        self.with_targets = with_targets

    def __call__(self, batch):
        if self.with_targets:
            texts, targets = zip(*batch)
        else:
            texts = batch

        encoded = self.tokenizer_instance(
            list(texts),
            truncation=True,
            max_length=self.max_length,
            padding=True,
            return_tensors="pt",
        )
        encoded.pop("token_type_ids", None)

        if self.with_targets:
            encoded["targets"] = torch.tensor(targets, dtype=torch.float32)

        return encoded


random.seed(TRAINING_SEED)
np.random.seed(TRAINING_SEED)
torch.manual_seed(TRAINING_SEED)
torch.cuda.manual_seed_all(TRAINING_SEED)

if not torch.cuda.is_available():
    raise RuntimeError("CUDA is required for ModernBERT fine-tuning in this script.")

device = torch.device("cuda")
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

try:
    torch.set_float32_matmul_precision("high")
except AttributeError:
    pass

train_raw = pd.read_csv(TRAIN_PATH, usecols=REQUIRED_TRAIN_COLUMNS, low_memory=False)
test_raw = pd.read_csv(TEST_PATH, usecols=REQUIRED_TEST_COLUMNS, low_memory=False)

missing_train_columns = sorted(set(REQUIRED_TRAIN_COLUMNS) - set(train_raw.columns))
missing_test_columns = sorted(set(REQUIRED_TEST_COLUMNS) - set(test_raw.columns))

if missing_train_columns:
    raise ValueError(f"Missing required train columns: {missing_train_columns}")
if missing_test_columns:
    raise ValueError(f"Missing required test columns: {missing_test_columns}")

target_binary_for_split = (train_raw["target"].to_numpy() >= IDENTITY_THRESHOLD).astype(
    np.int8
)
identity_known_for_split = train_raw[IDENTITY_COLUMNS].notna().any(axis=1).to_numpy()
identity_present_for_split = (
    train_raw[IDENTITY_COLUMNS].ge(IDENTITY_THRESHOLD).any(axis=1).to_numpy()
)

identity_state_for_split = np.where(
    identity_known_for_split,
    identity_present_for_split.astype(np.int8),
    2,
).astype(np.int8)

stratification_labels = (target_binary_for_split * 3 + identity_state_for_split).astype(
    np.int8
)

text_groups, _ = pd.factorize(
    train_raw["comment_text"].fillna("").astype(str),
    sort=False,
)

try:
    splitter = StratifiedGroupKFold(
        n_splits=N_SPLITS,
        shuffle=True,
        random_state=SEED,
    )
except TypeError:
    splitter = StratifiedGroupKFold(n_splits=N_SPLITS)

split_iterator = splitter.split(
    X=np.zeros(len(train_raw), dtype=np.uint8),
    y=stratification_labels,
    groups=text_groups,
)

train_indices = None
valid_indices = None

for fold_index, (candidate_train_indices, candidate_valid_indices) in enumerate(
    split_iterator
):
    if fold_index == VALID_FOLD:
        train_indices = candidate_train_indices
        valid_indices = candidate_valid_indices
        break

if train_indices is None or valid_indices is None:
    raise RuntimeError("Unable to construct the requested validation fold.")

train_processed = train_raw.iloc[train_indices].copy()
valid_processed = train_raw.iloc[valid_indices].copy()
test_processed = test_raw.copy()

del train_raw, test_raw, text_groups, stratification_labels
del target_binary_for_split
del identity_known_for_split, identity_present_for_split, identity_state_for_split
gc.collect()

train_processed = add_text_features(train_processed)
valid_processed = add_text_features(valid_processed)
test_processed = add_text_features(test_processed)

train_processed = add_identity_features(train_processed, has_target=True)
valid_processed = add_identity_features(valid_processed, has_target=True)

train_sampler_cell = train_processed["identity_union"].to_numpy(
    dtype=np.int8
) * 2 + train_processed["target_binary"].to_numpy(dtype=np.int8)

cell_counts = np.bincount(train_sampler_cell, minlength=4).astype(np.float64)
nonzero_counts = cell_counts[cell_counts > 0]

if len(nonzero_counts) == 0:
    raise RuntimeError("No valid training rows were available for sampler weights.")

reference_count = float(np.mean(nonzero_counts))
cell_weights = np.ones(4, dtype=np.float64)

for cell_id, count in enumerate(cell_counts):
    if count > 0:
        cell_weights[cell_id] = reference_count / count

cell_weights = np.clip(cell_weights, SAMPLER_WEIGHT_MIN, SAMPLER_WEIGHT_MAX)
sample_weights = cell_weights[train_sampler_cell]
sample_weights = sample_weights / sample_weights.mean()

train_processed["sampler_cell"] = train_sampler_cell.astype(np.int8)
train_processed["sampler_weight"] = sample_weights.astype(np.float32)
valid_processed["sampler_weight"] = np.ones(len(valid_processed), dtype=np.float32)

if train_processed["id"].isin(valid_processed["id"]).any():
    raise RuntimeError("Train/validation ID overlap detected.")
if len(test_processed) == 0 or not test_processed["id"].is_unique:
    raise RuntimeError("Test IDs must be non-empty and unique.")

train_feature_path = save_feature_table(train_processed, "train_features")
valid_feature_path = save_feature_table(valid_processed, "valid_features")
test_feature_path = save_feature_table(test_processed, "test_features")

feature_columns = [
    "comment_text",
    "text_log_char_count",
    "text_log_word_count",
    "text_log_exclamation_count",
    "text_log_question_count",
    "text_log_newline_count",
    "text_uppercase_fraction",
    "text_has_url",
    "text_has_email",
    "text_has_user_mention",
]

manifest = {
    "seed": SEED,
    "validation_method": (
        "StratifiedGroupKFold on target_binary x identity-label-state, "
        "grouped by exact raw comment text"
    ),
    "identity_threshold": IDENTITY_THRESHOLD,
    "identity_columns": IDENTITY_COLUMNS,
    "auxiliary_target_columns": AUXILIARY_TARGET_COLUMNS,
    "model_feature_columns": feature_columns,
    "target_column": "target",
    "binary_target_column": "target_binary",
    "sampler_weight_column": "sampler_weight",
    "train_feature_path": train_feature_path,
    "valid_feature_path": valid_feature_path,
    "test_feature_path": test_feature_path,
    "n_train_rows": int(len(train_processed)),
    "n_valid_rows": int(len(valid_processed)),
    "n_test_rows": int(len(test_processed)),
    "test_id_order_path": str(WORKING_DIR / "test_ids.npy"),
}

np.save(WORKING_DIR / "test_ids.npy", test_processed["id"].to_numpy())

with open(WORKING_DIR / "feature_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

del train_processed, valid_processed, test_processed
gc.collect()

train_frame = read_feature_table(manifest["train_feature_path"])
valid_frame = read_feature_table(manifest["valid_feature_path"])
test_frame = read_feature_table(manifest["test_feature_path"])

required_train_columns = {"comment_text", "target", "sampler_weight"}
required_valid_columns = {"comment_text", "target"} | set(OFFICIAL_IDENTITY_COLUMNS)
required_test_columns = {"id", "comment_text"}

missing_train = required_train_columns - set(train_frame.columns)
missing_valid = required_valid_columns - set(valid_frame.columns)
missing_test = required_test_columns - set(test_frame.columns)

if missing_train:
    raise ValueError(f"Training features are missing columns: {sorted(missing_train)}")
if missing_valid:
    raise ValueError(
        f"Validation features are missing columns: {sorted(missing_valid)}"
    )
if missing_test:
    raise ValueError(f"Test features are missing columns: {sorted(missing_test)}")

if len(train_frame) == 0 or len(valid_frame) == 0 or len(test_frame) == 0:
    raise RuntimeError("Training, validation, and test tables must all be non-empty.")

if not test_frame["id"].is_unique:
    raise RuntimeError("Test IDs must be unique.")

expected_test_ids_path = Path(manifest["test_id_order_path"])
if expected_test_ids_path.exists():
    expected_test_ids = np.load(expected_test_ids_path, allow_pickle=False)
    if not np.array_equal(test_frame["id"].to_numpy(), expected_test_ids):
        raise RuntimeError(
            "Test feature-table order does not match preserved test ID order."
        )

train_texts = train_frame["comment_text"].fillna("").astype(str).tolist()
valid_texts = valid_frame["comment_text"].fillna("").astype(str).tolist()
test_texts = test_frame["comment_text"].fillna("").astype(str).tolist()

train_targets = train_frame["target"].to_numpy(dtype=np.float32)
valid_targets = valid_frame["target"].to_numpy(dtype=np.float32)
train_sampler_weights = train_frame["sampler_weight"].to_numpy(dtype=np.float64)

if not np.isfinite(train_targets).all() or not np.isfinite(valid_targets).all():
    raise ValueError("Toxicity targets must be finite.")
if not np.isfinite(train_sampler_weights).all() or (train_sampler_weights <= 0).any():
    raise ValueError("Sampler weights must be finite and strictly positive.")

# The base checkpoint retains ModernBERT text modeling while fitting reliably in shared GPU memory.
model_id = "answerdotai/ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    num_labels=1,
    ignore_mismatched_sizes=True,
)
model.config.problem_type = "regression"

criterion = torch.nn.BCEWithLogitsLoss(reduction="none")

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
backbone_decay_params = []
backbone_no_decay_params = []
classifier_decay_params = []
classifier_no_decay_params = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_classifier = "classifier" in parameter_name
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_classifier and has_no_decay:
        classifier_no_decay_params.append(parameter)
    elif is_classifier:
        classifier_decay_params.append(parameter)
    elif has_no_decay:
        backbone_no_decay_params.append(parameter)
    else:
        backbone_decay_params.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_decay_params,
            "lr": BACKBONE_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
        {
            "params": backbone_no_decay_params,
            "lr": BACKBONE_LEARNING_RATE,
            "weight_decay": 0.0,
        },
        {
            "params": classifier_decay_params,
            "lr": CLASSIFIER_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
        {
            "params": classifier_no_decay_params,
            "lr": CLASSIFIER_LEARNING_RATE,
            "weight_decay": 0.0,
        },
    ]
)


def logits_to_prediction(logits):
    return torch.sigmoid(logits.reshape(-1))


train_dataset = ToxicityTextDataset(train_texts, train_targets)
valid_dataset = ToxicityTextDataset(valid_texts, valid_targets)
test_dataset = ToxicityTextDataset(test_texts)

sampler_generator = torch.Generator()
sampler_generator.manual_seed(TRAINING_SEED)

train_sampler = WeightedRandomSampler(
    weights=torch.as_tensor(train_sampler_weights, dtype=torch.double),
    num_samples=len(train_sampler_weights),
    replacement=True,
    generator=sampler_generator,
)

train_collator = ToxicityBatchCollator(tokenizer, MAX_LENGTH, with_targets=True)
inference_collator = ToxicityBatchCollator(tokenizer, MAX_LENGTH, with_targets=False)

loader_kwargs = {
    "num_workers": NUM_WORKERS,
    "pin_memory": True,
    "persistent_workers": NUM_WORKERS > 0,
    "prefetch_factor": 2 if NUM_WORKERS > 0 else None,
}

if loader_kwargs["prefetch_factor"] is None:
    loader_kwargs.pop("prefetch_factor")

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    sampler=train_sampler,
    drop_last=False,
    collate_fn=train_collator,
    **loader_kwargs,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    collate_fn=train_collator,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    collate_fn=inference_collator,
    **loader_kwargs,
)

# Activation checkpointing recomputes transformer activations during backpropagation,
# substantially reducing training memory without changing model predictions or metric logic.
model.gradient_checkpointing_enable()
model.config.use_cache = False
model.to(device)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_updates = max(1, updates_per_epoch * NUM_EPOCHS)
warmup_updates = max(1, int(total_updates * WARMUP_FRACTION))


def lr_lambda(current_step):
    if current_step < warmup_updates:
        return float(current_step + 1) / float(max(1, warmup_updates))

    progress = float(current_step - warmup_updates) / float(
        max(1, total_updates - warmup_updates)
    )
    return max(0.05, 0.5 * (1.0 + math.cos(math.pi * min(progress, 1.0))))


scheduler = LambdaLR(optimizer, lr_lambda=lr_lambda)
scaler = torch.cuda.amp.GradScaler(enabled=True)


def model_probabilities(data_loader):
    model.eval()
    all_predictions = []

    with torch.inference_mode():
        for batch in data_loader:
            batch.pop("targets", None)
            batch = {
                key: value.to(device, non_blocking=True) for key, value in batch.items()
            }

            with torch.cuda.amp.autocast(enabled=True):
                logits = model(**batch).logits

            probabilities = logits_to_prediction(logits).float().cpu().numpy()
            all_predictions.append(probabilities)

    if not all_predictions:
        raise RuntimeError("Inference produced no prediction batches.")

    predictions = np.concatenate(all_predictions).astype(np.float64, copy=False)

    if not np.isfinite(predictions).all():
        raise RuntimeError("Model inference produced non-finite predictions.")

    return predictions


best_checkpoint_path = WORKING_DIR / "best_modernbert_toxicity.pt"
best_metrics_path = WORKING_DIR / "best_validation_metrics.json"

best_score = -np.inf
best_epoch = -1

for epoch in range(1, NUM_EPOCHS + 1):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    running_loss = 0.0
    observed_examples = 0

    for batch_index, batch in enumerate(train_loader, start=1):
        targets = batch.pop("targets").to(device, non_blocking=True)
        batch = {
            key: value.to(device, non_blocking=True) for key, value in batch.items()
        }

        with torch.cuda.amp.autocast(enabled=True):
            logits = model(**batch).logits.reshape(-1)
            per_example_loss = criterion(logits, targets)
            loss = per_example_loss.mean() / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(loss).backward()

        is_update_step = (
            batch_index % GRADIENT_ACCUMULATION_STEPS == 0
            or batch_index == len(train_loader)
        )

        if is_update_step:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), MAX_GRAD_NORM)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_size = targets.shape[0]
        running_loss += float(per_example_loss.detach().mean().item()) * batch_size
        observed_examples += batch_size

    epoch_loss = running_loss / max(1, observed_examples)
    validation_predictions = model_probabilities(valid_loader)

    if len(validation_predictions) != len(valid_frame):
        raise RuntimeError(
            "Validation prediction count does not match validation rows."
        )

    validation_score, validation_details = official_competition_metric(
        valid_targets,
        validation_predictions,
        valid_frame[OFFICIAL_IDENTITY_COLUMNS],
    )

    if validation_score > best_score:
        best_score = validation_score
        best_epoch = epoch

        torch.save(
            {
                "epoch": epoch,
                "score": validation_score,
                "model_state_dict": model.state_dict(),
            },
            best_checkpoint_path,
        )

        with open(best_metrics_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "epoch": epoch,
                    "train_loss": epoch_loss,
                    **validation_details,
                },
                f,
                indent=2,
            )

    print(
        f"Epoch {epoch}/{NUM_EPOCHS} | loss={epoch_loss:.6f} | "
        f"official_score={validation_score:.6f} | "
        f"overall_auc={validation_details['overall_auc']:.6f} | "
        f"bpsn_pm={validation_details['bpsn_power_mean']:.6f}"
    )

if best_epoch < 0 or not best_checkpoint_path.exists():
    raise RuntimeError("No valid checkpoint was saved.")

best_checkpoint = torch.load(best_checkpoint_path, map_location=device)
model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(device)

final_validation_predictions = model_probabilities(valid_loader)
score, final_validation_details = official_competition_metric(
    valid_targets,
    final_validation_predictions,
    valid_frame[OFFICIAL_IDENTITY_COLUMNS],
)

test_predictions = model_probabilities(test_loader)

if len(test_predictions) != len(test_frame):
    raise RuntimeError("Test prediction count does not match test rows.")

submission = pd.DataFrame(
    {
        "id": test_frame["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if list(submission.columns) != ["id", "prediction"]:
    raise RuntimeError("Submission columns must be exactly ['id', 'prediction'].")

if len(submission) != len(test_frame) or submission["prediction"].isna().any():
    raise RuntimeError(
        "Submission must contain one finite prediction for every test row."
    )

if not np.isfinite(submission["prediction"].to_numpy()).all():
    raise RuntimeError("Submission contains non-finite predictions.")

submission.to_csv(SUBMISSION_DIR / "submission_7d4be756747548edb21f4f6e2f129961.csv", index=False)

with open(WORKING_DIR / "final_validation_metrics.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "selected_epoch": int(best_checkpoint["epoch"]),
            "selected_checkpoint_score": float(best_checkpoint["score"]),
            **final_validation_details,
        },
        f,
        indent=2,
    )

print(f"Final Validation Score: {score}")