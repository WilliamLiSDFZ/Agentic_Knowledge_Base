import os
os.sched_setaffinity(0, {10, 11})
import os
import re
import gc
import html
import json
import math
import random
import unicodedata

# The previous large-model, 16x256 microbatch exhausted the shared GPU during attention.
# Use allocator segments plus a smaller pretrained encoder and lower activation footprint while preserving model-based training and inference.
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.autograd import Function
from torch.cuda.amp import GradScaler, autocast
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModel, AutoTokenizer


os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2027
INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"

MAX_LENGTH = 192
BATCH_SIZE = min(12, int(os.environ.get("BATCH_SIZE", "12")))
MAX_EPOCHS = int(os.environ.get("MAX_EPOCHS", "1"))
GRADIENT_ACCUMULATION_STEPS = max(
    3,
    int(os.environ.get("GRADIENT_ACCUMULATION_STEPS", "3")),
)
NUM_WORKERS = 2
EARLY_STOPPING_PATIENCE = 1

CHECKPOINT_PATH = os.path.join(WORKING_DIR, "best_metric_aligned_deberta.pt")

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda = device.type == "cuda"

identity_columns = [
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

subtype_columns = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

train_path = os.path.join(INPUT_DIR, "train.csv")
test_path = os.path.join(INPUT_DIR, "test.csv")

train_header = pd.read_csv(train_path, nrows=0).columns.tolist()
test_header = pd.read_csv(test_path, nrows=0).columns.tolist()

available_identity_columns = [
    column for column in identity_columns if column in train_header
]
available_eval_identity_columns = [
    column for column in evaluation_identity_columns if column in train_header
]
available_subtype_columns = [
    column for column in subtype_columns if column in train_header
]

required_train_columns = [
    column
    for column in (
        [
            "id",
            "comment_text",
            "target",
            "identity_annotator_count",
            "toxicity_annotator_count",
        ]
        + available_identity_columns
        + available_subtype_columns
    )
    if column in train_header
]

train_dtypes = {}
for column in required_train_columns:
    if column == "id":
        train_dtypes[column] = "int64"
    elif column in available_identity_columns + available_subtype_columns + ["target"]:
        train_dtypes[column] = "float32"
    elif column in ["identity_annotator_count", "toxicity_annotator_count"]:
        train_dtypes[column] = "int32"

train = pd.read_csv(
    train_path,
    usecols=required_train_columns,
    dtype=train_dtypes,
    low_memory=False,
)

test = pd.read_csv(
    test_path,
    usecols=[column for column in ["id", "comment_text"] if column in test_header],
    dtype={"id": "int64"},
    low_memory=False,
)

train["comment_text"] = train["comment_text"].fillna("")
test["comment_text"] = test["comment_text"].fillna("")

target_binary = (train["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)

if available_eval_identity_columns:
    identity_known_for_split = (
        train[available_eval_identity_columns].notna().any(axis=1).to_numpy()
    )
    eval_identity_values = (
        train[available_eval_identity_columns].fillna(0.0).to_numpy(dtype=np.float32)
    )
    identity_present_for_split = eval_identity_values.max(axis=1) >= 0.5
    primary_identity = eval_identity_values.argmax(axis=1).astype(np.int16) + 1
    identity_group = np.where(
        identity_present_for_split,
        primary_identity,
        np.where(
            identity_known_for_split,
            len(available_eval_identity_columns) + 1,
            len(available_eval_identity_columns) + 2,
        ),
    )
else:
    identity_group = np.zeros(len(train), dtype=np.int16)

n_identity_groups = int(identity_group.max()) + 1
split_strata = (
    target_binary.astype(np.int16) * n_identity_groups + identity_group
).astype(np.int16)

duplicate_group_ids = pd.util.hash_pandas_object(
    train["comment_text"].astype(str),
    index=False,
).to_numpy(dtype=np.uint64)

splitter = StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=SEED)
fit_indices, valid_indices = next(
    splitter.split(
        X=np.zeros(len(train), dtype=np.uint8),
        y=split_strata,
        groups=duplicate_group_ids,
    )
)

fit_raw = train.iloc[fit_indices].copy()
valid_raw = train.iloc[valid_indices].copy()

del target_binary
del identity_group
del split_strata
del duplicate_group_ids
del fit_indices
del valid_indices
del train
gc.collect()

url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>\]\[()]+")
email_pattern = re.compile(r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
whitespace_pattern = re.compile(r"\s+")

identity_swap_pairs = {
    "women": "men",
    "woman": "man",
    "female": "male",
    "girls": "boys",
    "girl": "boy",
    "men": "women",
    "man": "woman",
    "male": "female",
    "boys": "girls",
    "boy": "girl",
    "christians": "muslims",
    "christian": "muslim",
    "muslims": "christians",
    "muslim": "christian",
    "jews": "christians",
    "jewish": "christian",
    "black": "white",
    "white": "black",
    "gay": "straight",
    "lesbian": "heterosexual",
    "straight": "gay",
    "heterosexual": "lesbian",
}

identity_swap_pattern = re.compile(
    r"\b("
    + "|".join(
        sorted(
            (re.escape(key) for key in identity_swap_pairs),
            key=len,
            reverse=True,
        )
    )
    + r")\b",
    flags=re.IGNORECASE,
)


def preserve_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement.capitalize()
    return replacement


def clean_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", "").replace("\ufeff", "").replace("\u00ad", "")
    text = url_pattern.sub(" URLTOKEN ", text)
    text = email_pattern.sub(" EMAILTOKEN ", text)
    text = whitespace_pattern.sub(" ", text).strip()
    return text


def identity_counterfactual(text):
    changed = False

    def replace_match(match):
        nonlocal changed
        source = match.group(0)
        replacement = identity_swap_pairs[source.lower()]
        changed = True
        return preserve_case(source, replacement)

    swapped = identity_swap_pattern.sub(replace_match, text)
    return swapped if changed else ""


def create_text_features(clean_text):
    char_count = clean_text.str.len().to_numpy(dtype=np.float32)
    word_count = clean_text.str.count(r"\S+").to_numpy(dtype=np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    alphabetic_count = clean_text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    digit_count = clean_text.str.count(r"\d").to_numpy(dtype=np.float32)
    punctuation_count = clean_text.str.count(r"[^\w\s]").to_numpy(dtype=np.float32)
    exclamation_count = clean_text.str.count("!").to_numpy(dtype=np.float32)
    question_count = clean_text.str.count(r"\?").to_numpy(dtype=np.float32)
    quote_count = clean_text.str.count(r"""["']""").to_numpy(dtype=np.float32)
    capital_word_count = clean_text.str.count(r"\b[A-Z]{2,}\b").to_numpy(
        dtype=np.float32
    )
    repeated_punctuation = clean_text.str.count(r"([!?.,])\1{1,}").to_numpy(
        dtype=np.float32
    )
    url_count = clean_text.str.count(r"\bURLTOKEN\b").to_numpy(dtype=np.float32)
    email_count = clean_text.str.count(r"\bEMAILTOKEN\b").to_numpy(dtype=np.float32)

    safe_chars = np.maximum(char_count, 1.0)
    safe_alpha = np.maximum(alphabetic_count, 1.0)
    safe_words = np.maximum(word_count, 1.0)

    return pd.DataFrame(
        {
            "tf_log_char_count": np.log1p(char_count),
            "tf_log_word_count": np.log1p(word_count),
            "tf_uppercase_ratio": uppercase_count / safe_alpha,
            "tf_digit_ratio": digit_count / safe_chars,
            "tf_punctuation_ratio": punctuation_count / safe_chars,
            "tf_log_exclamation_count": np.log1p(exclamation_count),
            "tf_log_question_count": np.log1p(question_count),
            "tf_log_quote_count": np.log1p(quote_count),
            "tf_capital_word_ratio": capital_word_count / safe_words,
            "tf_log_repeated_punctuation": np.log1p(repeated_punctuation),
            "tf_log_url_count": np.log1p(url_count),
            "tf_log_email_count": np.log1p(email_count),
        },
        index=clean_text.index,
        dtype=np.float32,
    )


def process_partition(frame, is_training):
    processed = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(dtype=np.int64),
            "comment_text": frame["comment_text"].map(clean_comment),
        }
    )

    processed["counterfactual_text"] = processed["comment_text"].map(
        identity_counterfactual
    )
    processed["counterfactual_available"] = (
        processed["counterfactual_text"].str.len().to_numpy() > 0
    ).astype(np.int8)

    raw_text_features = create_text_features(processed["comment_text"])
    raw_text_features.index = processed.index

    if is_training:
        processed["target"] = frame["target"].to_numpy(dtype=np.float32)
        processed["target_binary"] = (
            processed["target"].to_numpy(dtype=np.float32) >= 0.5
        ).astype(np.int8)

        if available_identity_columns:
            identity_available = (
                frame[available_identity_columns]
                .notna()
                .any(axis=1)
                .to_numpy(dtype=np.int8)
            )
            identity_matrix = (
                frame[available_identity_columns].fillna(0.0).to_numpy(dtype=np.float32)
            )
            processed["identity_label_available"] = identity_available
            processed["any_identity"] = (identity_matrix.max(axis=1) >= 0.5).astype(
                np.int8
            )

            for column_index, column in enumerate(available_identity_columns):
                processed[f"identity__{column}"] = identity_matrix[:, column_index]
        else:
            processed["identity_label_available"] = np.zeros(
                len(processed),
                dtype=np.int8,
            )
            processed["any_identity"] = np.zeros(len(processed), dtype=np.int8)

        for column in available_subtype_columns:
            processed[f"subtype__{column}"] = (
                frame[column].fillna(0.0).to_numpy(dtype=np.float32)
            )

    return processed, raw_text_features.reset_index(drop=True)


fit_processed, fit_text_features = process_partition(fit_raw, is_training=True)
valid_processed, valid_text_features = process_partition(valid_raw, is_training=True)
test_processed, test_text_features = process_partition(test, is_training=False)

del fit_raw
del valid_raw
del test
gc.collect()

text_feature_columns = fit_text_features.columns.tolist()

text_feature_scaler = StandardScaler()
fit_scaled_features = text_feature_scaler.fit_transform(fit_text_features).astype(
    np.float32
)
valid_scaled_features = text_feature_scaler.transform(valid_text_features).astype(
    np.float32
)
test_scaled_features = text_feature_scaler.transform(test_text_features).astype(
    np.float32
)

for feature_index, feature_name in enumerate(text_feature_columns):
    fit_processed[feature_name] = fit_scaled_features[:, feature_index]
    valid_processed[feature_name] = valid_scaled_features[:, feature_index]
    test_processed[feature_name] = test_scaled_features[:, feature_index]

del fit_text_features
del valid_text_features
del test_text_features
del fit_scaled_features
del valid_scaled_features
del test_scaled_features
gc.collect()

joblib.dump(
    text_feature_scaler,
    os.path.join(WORKING_DIR, "text_feature_scaler.joblib"),
)

processing_metadata = {
    "seed": SEED,
    "split_strategy": "StratifiedGroupKFold with exact-text duplicate grouping",
    "validation_fraction": float(
        len(valid_processed) / (len(fit_processed) + len(valid_processed))
    ),
    "text_feature_columns": text_feature_columns,
    "identity_columns": available_identity_columns,
    "evaluation_identity_columns": available_eval_identity_columns,
    "subtype_columns": available_subtype_columns,
    "train_rows": int(len(fit_processed)),
    "valid_rows": int(len(valid_processed)),
    "test_rows": int(len(test_processed)),
}

joblib.dump(
    processing_metadata,
    os.path.join(WORKING_DIR, "processing_metadata.joblib"),
)


class GradientReverse(Function):
    @staticmethod
    def forward(ctx, inputs, strength):
        ctx.strength = float(strength)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, grad_outputs):
        return -ctx.strength * grad_outputs, None


def gradient_reverse(inputs, strength=1.0):
    return GradientReverse.apply(inputs, strength)


class DebertaMetricAlignedToxicityModel(nn.Module):
    def __init__(self, backbone, num_identity_labels, dropout=0.15):
        super().__init__()
        self.backbone = backbone
        hidden_size = backbone.config.hidden_size

        self.token_attention = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.Tanh(),
            nn.Linear(hidden_size // 2, 1, bias=False),
        )
        self.representation_norm = nn.LayerNorm(hidden_size * 2)
        self.representation_projection = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.toxicity_head = nn.Linear(hidden_size, 1)
        self.identity_adversary = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, num_identity_labels),
        )

    def forward(
        self,
        input_ids,
        attention_mask,
        token_type_ids=None,
        adversarial_strength=1.0,
    ):
        backbone_inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }

        if token_type_ids is not None:
            backbone_inputs["token_type_ids"] = token_type_ids

        encoder_outputs = self.backbone(**backbone_inputs)
        hidden_states = encoder_outputs.last_hidden_state

        token_scores = self.token_attention(hidden_states).squeeze(-1)
        token_scores = token_scores.masked_fill(attention_mask == 0, -1.0e4)
        attention_weights = torch.softmax(token_scores, dim=1)

        attentive_pool = torch.sum(
            hidden_states * attention_weights.unsqueeze(-1),
            dim=1,
        )
        cls_pool = hidden_states[:, 0]

        representation = torch.cat([cls_pool, attentive_pool], dim=-1)
        representation = self.representation_norm(representation)
        representation = self.representation_projection(representation)

        toxicity_logit = self.toxicity_head(representation).squeeze(-1)
        identity_logits = self.identity_adversary(
            gradient_reverse(representation, adversarial_strength)
        )

        return {
            "toxicity_logit": toxicity_logit,
            "identity_logits": identity_logits,
            "representation": representation,
        }


class OfficialBiasSurrogateLoss(nn.Module):
    def __init__(
        self,
        evaluation_indices,
        pairwise_weight=0.55,
        adversarial_weight=0.035,
        pairwise_temperature=0.50,
        worst_group_focus=5.0,
    ):
        super().__init__()
        self.evaluation_indices = list(evaluation_indices)
        self.pairwise_weight = float(pairwise_weight)
        self.adversarial_weight = float(adversarial_weight)
        self.pairwise_temperature = float(pairwise_temperature)
        self.worst_group_focus = float(worst_group_focus)

    def pairwise_auc_loss(self, positive_logits, negative_logits):
        if positive_logits.numel() == 0 or negative_logits.numel() == 0:
            return None

        margins = (
            positive_logits.unsqueeze(1) - negative_logits.unsqueeze(0)
        ) / self.pairwise_temperature

        return F.softplus(-margins).mean()

    def official_partition_surrogate(
        self,
        logits,
        binary_targets,
        identity_targets,
        identity_available,
    ):
        valid_losses = []

        for identity_index in self.evaluation_indices:
            subgroup = identity_targets[:, identity_index] >= 0.5
            background = ~subgroup

            subgroup_auc = self.pairwise_auc_loss(
                logits[subgroup & (binary_targets == 1)],
                logits[subgroup & (binary_targets == 0)],
            )
            bpsn_auc = self.pairwise_auc_loss(
                logits[background & (binary_targets == 1)],
                logits[subgroup & (binary_targets == 0)],
            )
            bnsp_auc = self.pairwise_auc_loss(
                logits[subgroup & (binary_targets == 1)],
                logits[background & (binary_targets == 0)],
            )

            for partition_loss in (subgroup_auc, bpsn_auc, bnsp_auc):
                if partition_loss is not None:
                    valid_losses.append(partition_loss)

        if not valid_losses:
            return logits.sum() * 0.0

        partition_losses = torch.stack(valid_losses)
        return (
            torch.logsumexp(
                partition_losses * self.worst_group_focus,
                dim=0,
            )
            / self.worst_group_focus
        )

    def forward(
        self,
        model_outputs,
        toxicity_targets,
        identity_targets=None,
        identity_available=None,
    ):
        toxicity_logits = model_outputs["toxicity_logit"]
        toxicity_targets = toxicity_targets.float().clamp(0.0, 1.0)

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
        )

        if identity_targets is None or identity_available is None:
            return toxicity_loss

        identity_targets = identity_targets.float().clamp(0.0, 1.0)
        identity_available = identity_available.bool()
        hard_toxicity_targets = (toxicity_targets >= 0.5).long()

        bias_ranking_loss = self.official_partition_surrogate(
            logits=toxicity_logits,
            binary_targets=hard_toxicity_targets,
            identity_targets=identity_targets,
            identity_available=identity_available,
        )

        neutral_known_mask = (hard_toxicity_targets == 0) & identity_available

        if neutral_known_mask.any():
            adversarial_loss = F.binary_cross_entropy_with_logits(
                model_outputs["identity_logits"][neutral_known_mask],
                identity_targets[neutral_known_mask],
            )
        else:
            adversarial_loss = toxicity_logits.sum() * 0.0

        return (
            toxicity_loss
            + self.pairwise_weight * bias_ranking_loss
            + self.adversarial_weight * adversarial_loss
        )


tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-base")
base_model = AutoModel.from_pretrained("microsoft/deberta-v3-base")

model = DebertaMetricAlignedToxicityModel(
    backbone=base_model,
    num_identity_labels=len(available_identity_columns),
    dropout=0.15,
)

del base_model
gc.collect()

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    # Non-reentrant checkpointing safely supports the toxicity and adversarial
    # branches consuming the same encoder representation during one backward pass.
    model.backbone.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )

evaluation_identity_indices = [
    available_identity_columns.index(column)
    for column in available_eval_identity_columns
    if column in available_identity_columns
]

criterion = OfficialBiasSurrogateLoss(
    evaluation_indices=evaluation_identity_indices,
    pairwise_weight=0.55,
    adversarial_weight=0.035,
    pairwise_temperature=0.50,
    worst_group_focus=5.0,
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
            "lr": 7.5e-5,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

model = model.to(device)

identity_feature_columns = [f"identity__{name}" for name in available_identity_columns]
evaluation_identity_feature_columns = [
    f"identity__{name}"
    for name in available_eval_identity_columns
    if f"identity__{name}" in valid_processed.columns
]

missing_training_columns = [
    column
    for column in ["comment_text", "target", "identity_label_available"]
    + identity_feature_columns
    if column not in fit_processed.columns
]

if missing_training_columns:
    raise RuntimeError(
        f"Required processed training columns are missing: {missing_training_columns}"
    )

missing_validation_columns = [
    column
    for column in ["comment_text", "target", "identity_label_available"]
    + evaluation_identity_feature_columns
    if column not in valid_processed.columns
]

if missing_validation_columns:
    raise RuntimeError(
        f"Required processed validation columns are missing: {missing_validation_columns}"
    )


class ToxicityTextDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.texts = frame["comment_text"].fillna("").astype(str).to_numpy()
        self.include_labels = include_labels

        if include_labels:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.identity_targets = (
                frame[identity_feature_columns]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )
            self.identity_available = frame["identity_label_available"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
        else:
            self.targets = None
            self.identity_targets = None
            self.identity_available = None

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {"text": self.texts[index]}

        if self.include_labels:
            item["target"] = self.targets[index]
            item["identity_targets"] = self.identity_targets[index]
            item["identity_available"] = self.identity_available[index]

        return item


def make_collate_fn(include_labels):
    def collate_fn(rows):
        texts = [row["text"] for row in rows]

        tokenized = tokenizer(
            texts,
            truncation=True,
            max_length=MAX_LENGTH,
            padding=True,
            return_tensors="pt",
        )

        batch = {name: tensor for name, tensor in tokenized.items()}

        if include_labels:
            batch["target"] = torch.tensor(
                [row["target"] for row in rows],
                dtype=torch.float32,
            )
            batch["identity_targets"] = torch.tensor(
                np.stack([row["identity_targets"] for row in rows]),
                dtype=torch.float32,
            )
            batch["identity_available"] = torch.tensor(
                [row["identity_available"] for row in rows],
                dtype=torch.float32,
            )

        return batch

    return collate_fn


def make_loader(dataset, include_labels, shuffle=False):
    generator = torch.Generator()
    generator.manual_seed(SEED + (1 if shuffle else 2))

    return DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=shuffle,
        num_workers=NUM_WORKERS,
        pin_memory=use_cuda,
        persistent_workers=NUM_WORKERS > 0,
        prefetch_factor=2,
        collate_fn=make_collate_fn(include_labels),
        generator=generator,
        drop_last=False,
    )


fit_dataset = ToxicityTextDataset(fit_processed, include_labels=True)
valid_dataset = ToxicityTextDataset(valid_processed, include_labels=True)
test_dataset = ToxicityTextDataset(test_processed, include_labels=False)

fit_loader = make_loader(fit_dataset, include_labels=True, shuffle=True)
valid_loader = make_loader(valid_dataset, include_labels=True, shuffle=False)
test_loader = make_loader(test_dataset, include_labels=False, shuffle=False)


def move_model_inputs(batch):
    model_inputs = {
        "input_ids": batch["input_ids"].to(device, non_blocking=use_cuda),
        "attention_mask": batch["attention_mask"].to(
            device,
            non_blocking=use_cuda,
        ),
    }

    if "token_type_ids" in batch:
        model_inputs["token_type_ids"] = batch["token_type_ids"].to(
            device,
            non_blocking=use_cuda,
        )

    return model_inputs


def predict_with_model(data_loader):
    model.eval()
    prediction_parts = []

    with torch.no_grad():
        for batch in data_loader:
            model_inputs = move_model_inputs(batch)

            with autocast(enabled=use_cuda):
                outputs = model(
                    **model_inputs,
                    adversarial_strength=0.0,
                )
                probabilities = torch.sigmoid(outputs["toxicity_logit"])

            prediction_parts.append(probabilities.float().cpu().numpy())

    return np.concatenate(prediction_parts, axis=0)


def exact_auc(binary_target, predictions, metric_name):
    binary_target = np.asarray(binary_target, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if np.unique(binary_target).size != 2:
        raise RuntimeError(
            f"Official {metric_name} AUC is undefined on this validation split "
            "because it contains only one class."
        )

    return float(roc_auc_score(binary_target, predictions))


def official_unintended_bias_metrics(frame, predictions):
    binary_target = (frame["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(binary_target) != len(predictions):
        raise ValueError("Validation target and prediction lengths do not match.")

    overall_auc = exact_auc(binary_target, predictions, "overall")

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []
    per_identity = {}

    for identity_column in evaluation_identity_feature_columns:
        subgroup_values = frame[identity_column].fillna(0.0).to_numpy(dtype=np.float32)
        subgroup = subgroup_values >= 0.5
        background = ~subgroup

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & (binary_target == 0)) | (
            background & (binary_target == 1)
        )
        bnsp_mask = (subgroup & (binary_target == 1)) | (
            background & (binary_target == 0)
        )

        identity_name = identity_column.replace("identity__", "")

        subgroup_auc = exact_auc(
            binary_target[subgroup_mask],
            predictions[subgroup_mask],
            f"{identity_name} subgroup",
        )
        bpsn_auc = exact_auc(
            binary_target[bpsn_mask],
            predictions[bpsn_mask],
            f"{identity_name} BPSN",
        )
        bnsp_auc = exact_auc(
            binary_target[bnsp_mask],
            predictions[bnsp_mask],
            f"{identity_name} BNSP",
        )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        per_identity[identity_name] = {
            "subgroup_auc": subgroup_auc,
            "bpsn_auc": bpsn_auc,
            "bnsp_auc": bnsp_auc,
        }

    if not subgroup_aucs:
        raise RuntimeError("No official evaluation identity columns are available.")

    power = -5.0

    def generalized_mean(values):
        values = np.clip(np.asarray(values, dtype=np.float64), 1e-15, 1.0)
        return float(np.mean(np.power(values, power)) ** (1.0 / power))

    subgroup_power_mean = generalized_mean(subgroup_aucs)
    bpsn_power_mean = generalized_mean(bpsn_aucs)
    bnsp_power_mean = generalized_mean(bnsp_aucs)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    return {
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
        "final_score": final_score,
        "per_identity": per_identity,
    }


total_optimizer_steps = max(
    1,
    math.ceil(len(fit_loader) / GRADIENT_ACCUMULATION_STEPS) * MAX_EPOCHS,
)
warmup_steps = max(1, int(total_optimizer_steps * 0.06))


def lr_multiplier(step):
    if step < warmup_steps:
        return float(step + 1) / float(warmup_steps)

    progress = float(step - warmup_steps) / float(
        max(1, total_optimizer_steps - warmup_steps)
    )

    return max(
        0.08,
        0.5 * (1.0 + math.cos(math.pi * min(progress, 1.0))),
    )


scheduler = LambdaLR(optimizer, lr_lambda=lr_multiplier)
scaler = GradScaler(enabled=use_cuda)

best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0
global_optimizer_step = 0

for epoch in range(MAX_EPOCHS):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    total_training_loss = 0.0
    processed_examples = 0
    num_batches = len(fit_loader)

    for batch_index, batch in enumerate(fit_loader):
        model_inputs = move_model_inputs(batch)
        target = batch["target"].to(device, non_blocking=use_cuda)
        identity_targets = batch["identity_targets"].to(
            device,
            non_blocking=use_cuda,
        )
        identity_available = batch["identity_available"].to(
            device,
            non_blocking=use_cuda,
        )

        adversarial_strength = min(
            1.0,
            float(global_optimizer_step + 1) / float(max(1, warmup_steps)),
        )

        with autocast(enabled=use_cuda):
            model_outputs = model(
                **model_inputs,
                adversarial_strength=adversarial_strength,
            )

            batch_loss = criterion(
                model_outputs=model_outputs,
                toxicity_targets=target,
                identity_targets=identity_targets,
                identity_available=identity_available,
            )

            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(scaled_loss).backward()

        batch_size_now = target.shape[0]
        total_training_loss += float(batch_loss.detach().cpu()) * batch_size_now
        processed_examples += batch_size_now

        should_update = (
            batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0 or batch_index + 1 == num_batches

        if should_update:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()
            global_optimizer_step += 1

    validation_predictions = predict_with_model(valid_loader)
    validation_metrics = official_unintended_bias_metrics(
        valid_processed,
        validation_predictions,
    )

    epoch_score = validation_metrics["final_score"]
    mean_training_loss = total_training_loss / max(1, processed_examples)

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "score": best_score,
                "model_state_dict": model.state_dict(),
                "validation_metrics": validation_metrics,
            },
            CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch + 1}/{MAX_EPOCHS} "
        f"loss={mean_training_loss:.6f} "
        f"official_score={epoch_score:.6f}"
    )

    del validation_predictions
    gc.collect()

    if use_cuda:
        torch.cuda.empty_cache()

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if not os.path.exists(CHECKPOINT_PATH):
    raise RuntimeError("No model checkpoint was saved.")

best_checkpoint = torch.load(CHECKPOINT_PATH, map_location=device)
model.load_state_dict(best_checkpoint["model_state_dict"])
model.eval()

final_validation_predictions = predict_with_model(valid_loader)
final_validation_metrics = official_unintended_bias_metrics(
    valid_processed,
    final_validation_predictions,
)
score = float(final_validation_metrics["final_score"])

with open(
    os.path.join(WORKING_DIR, "best_validation_metrics.json"),
    "w",
) as metric_file:
    json.dump(
        {
            "best_epoch": int(best_epoch + 1),
            "official_validation_metric": final_validation_metrics,
        },
        metric_file,
        indent=2,
    )

test_predictions = predict_with_model(test_loader)

if len(test_predictions) != len(test_processed):
    raise RuntimeError("Test prediction count does not match the processed test set.")

submission = pd.DataFrame(
    {
        "id": test_processed["id"].to_numpy(dtype=np.int64),
        "prediction": np.clip(test_predictions, 0.0, 1.0).astype(np.float64),
    }
)

submission.to_csv(
    os.path.join(SUBMISSION_DIR, "submission_f7a48d60a67c49c8b6b91cac0f9cde19.csv"),
    index=False,
)

print(f"Final Validation Score: {score}")