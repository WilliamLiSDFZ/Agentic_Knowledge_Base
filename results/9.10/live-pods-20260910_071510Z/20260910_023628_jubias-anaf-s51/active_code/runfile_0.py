import os
os.sched_setaffinity(0, {5, 6})
import html
import json
import math
import os
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
import re
import unicodedata
from collections import deque
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
    get_cosine_schedule_with_warmup,
)

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

SEED = 2025
VALID_FOLD = 0
N_SPLITS = 10
MAX_MODEL_CHARS = 6000
MAX_SEQUENCE_LENGTH = 384

NUM_STYLE_FEATURES = 13
NUM_EVALUATED_IDENTITIES = 9

ENCODER_LEARNING_RATE = 1.5e-5
HEAD_LEARNING_RATE = 1.0e-4
WEIGHT_DECAY = 0.01

BCE_WEIGHT = 1.0
PAIRWISE_WEIGHT = 0.15
PAIR_MEMORY_SIZE = 256
MAX_PAIRS_PER_SIDE = 64

TRAIN_BATCH_SIZE = 8
EVAL_BATCH_SIZE = 24
GRADIENT_ACCUMULATION_STEPS = 2
NUM_EPOCHS = 1
WARMUP_FRACTION = 0.06
MAX_GRAD_NORM = 1.0
NUM_WORKERS = 2
POWER_MEAN_P = -5.0

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
PROCESSED_DIR = WORKING_DIR / "processed"
SUBMISSION_DIR = Path("./submission")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"
BEST_MODEL_PATH = WORKING_DIR / "best_modernbert_toxicity_ranker.pt"

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

ALL_IDENTITY_COLUMNS = [
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

AUXILIARY_LABEL_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

torch.manual_seed(SEED)
np.random.seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

train_usecols = [
    "id",
    "comment_text",
    "target",
    "toxicity_annotator_count",
    "identity_annotator_count",
    *ALL_IDENTITY_COLUMNS,
    *AUXILIARY_LABEL_COLUMNS,
]

train_raw = pd.read_csv(TRAIN_PATH, usecols=train_usecols)
test_raw = pd.read_csv(TEST_PATH, usecols=["id", "comment_text"])

missing_train_columns = set(train_usecols) - set(train_raw.columns)
if missing_train_columns:
    raise ValueError(f"Missing required train columns: {sorted(missing_train_columns)}")

if train_raw["id"].duplicated().any() or test_raw["id"].duplicated().any():
    raise ValueError("Identifiers must be unique within each dataset.")

identity_values = (
    train_raw[EVALUATED_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
)
identity_flags = (identity_values >= 0.5).astype(np.int8)
identity_mask = identity_flags.astype(np.int64) @ (
    1 << np.arange(len(EVALUATED_IDENTITY_COLUMNS))
)

target_binary = (train_raw["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)
identity_any = identity_flags.any(axis=1).astype(np.int8)

split_groups = (
    train_raw["comment_text"]
    .fillna("")
    .astype(str)
    .str.normalize("NFKC")
    .str.strip()
    .str.lower()
)

split_strata = (
    pd.Series(target_binary, index=train_raw.index).astype(str)
    + "_identity_any_"
    + pd.Series(identity_any, index=train_raw.index).astype(str)
)

splitter = StratifiedGroupKFold(
    n_splits=N_SPLITS,
    shuffle=True,
    random_state=SEED,
)

train_indices = None
valid_indices = None

for fold_index, (fold_train_indices, fold_valid_indices) in enumerate(
    splitter.split(
        X=np.zeros(len(train_raw), dtype=np.uint8),
        y=split_strata,
        groups=split_groups,
    )
):
    if fold_index == VALID_FOLD:
        train_indices = np.sort(fold_train_indices)
        valid_indices = np.sort(fold_valid_indices)
        break

if train_indices is None or valid_indices is None:
    raise RuntimeError("Unable to create the requested validation split.")

if (
    np.intersect1d(
        split_groups.iloc[train_indices],
        split_groups.iloc[valid_indices],
    ).size
    != 0
):
    raise RuntimeError(
        "Duplicate comment groups leaked across training and validation."
    )

URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
EMAIL_RE = re.compile(r"(?i)\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
HTML_TAG_RE = re.compile(r"<[^>\n]{1,300}>")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
WHITESPACE_RE = re.compile(r"\s+")


def normalize_comment(text):
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = CONTROL_RE.sub(" ", text)
    text = URL_RE.sub(" URL ", text)
    text = EMAIL_RE.sub(" EMAIL ", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = WHITESPACE_RE.sub(" ", text).strip()

    if not text:
        return "[EMPTY_COMMENT]"

    if len(text) > MAX_MODEL_CHARS:
        head_chars = MAX_MODEL_CHARS - 1000
        text = text[:head_chars] + " [TRUNCATED] " + text[-1000:]

    return text


def build_text_features(raw_text):
    source_text = raw_text.fillna("").astype(str)
    model_text = source_text.map(normalize_comment)

    letter_count = model_text.str.count(r"[A-Za-z]").astype(np.float32)
    upper_count = model_text.str.count(r"[A-Z]").astype(np.float32)
    text_length = np.maximum(
        model_text.str.len().to_numpy(dtype=np.float32),
        1.0,
    )

    feature_frame = pd.DataFrame(
        {
            "text_log_char_count": np.log1p(
                model_text.str.len().to_numpy(dtype=np.float32)
            ),
            "text_log_word_count": np.log1p(
                model_text.str.count(r"\b[\w']+\b").to_numpy(dtype=np.float32)
            ),
            "text_log_sentence_count": np.log1p(
                model_text.str.count(r"[.!?]+").to_numpy(dtype=np.float32)
            ),
            "text_uppercase_ratio": (
                upper_count / np.maximum(letter_count, 1.0)
            ).to_numpy(dtype=np.float32),
            "text_digit_ratio": (
                model_text.str.count(r"\d").to_numpy(dtype=np.float32) / text_length
            ),
            "text_exclamation_count": np.log1p(
                model_text.str.count(r"!").to_numpy(dtype=np.float32)
            ),
            "text_question_count": np.log1p(
                model_text.str.count(r"\?").to_numpy(dtype=np.float32)
            ),
            "text_repeated_punctuation_count": np.log1p(
                model_text.str.count(r"[!?]{2,}").to_numpy(dtype=np.float32)
            ),
            "text_all_caps_token_count": np.log1p(
                model_text.str.count(r"\b[A-Z]{2,}\b").to_numpy(dtype=np.float32)
            ),
            "text_url_count": np.log1p(
                model_text.str.count(r"\bURL\b").to_numpy(dtype=np.float32)
            ),
            "text_email_count": np.log1p(
                model_text.str.count(r"\bEMAIL\b").to_numpy(dtype=np.float32)
            ),
            "text_negation_count": np.log1p(
                model_text.str.count(
                    r"(?i)\b(?:no|not|never|neither|nor|cannot|can't|won't|isn't|aren't|don't|doesn't|didn't)\b"
                ).to_numpy(dtype=np.float32)
            ),
            "text_is_empty": (model_text == "[EMPTY_COMMENT]").astype(np.float32),
        },
        index=raw_text.index,
    )

    return model_text, feature_frame.astype(np.float32)


all_model_text, all_text_features = build_text_features(train_raw["comment_text"])
test_model_text, test_text_features = build_text_features(test_raw["comment_text"])

feature_columns = all_text_features.columns.tolist()
if len(feature_columns) != NUM_STYLE_FEATURES:
    raise ValueError(
        f"Expected {NUM_STYLE_FEATURES} style features, found {len(feature_columns)}."
    )

scaler = StandardScaler()

scaled_train_features = scaler.fit_transform(
    all_text_features.iloc[train_indices]
).astype(np.float32)

scaled_valid_features = scaler.transform(all_text_features.iloc[valid_indices]).astype(
    np.float32
)

scaled_test_features = scaler.transform(test_text_features).astype(np.float32)
scaled_feature_columns = [f"{column}_z" for column in feature_columns]

label_frame = pd.DataFrame(
    {
        "id": train_raw["id"].to_numpy(),
        "label_target_soft": train_raw["target"].to_numpy(dtype=np.float32),
        "label_target_binary": target_binary,
        "label_toxicity_annotator_count": train_raw[
            "toxicity_annotator_count"
        ].to_numpy(dtype=np.int32),
        "label_identity_annotator_count": train_raw[
            "identity_annotator_count"
        ].to_numpy(dtype=np.int32),
        "label_identity_annotation_available": (
            train_raw["identity_annotator_count"].to_numpy(dtype=np.int32) > 0
        ).astype(np.int8),
        "label_identity_mask": identity_mask.astype(np.int16),
        "label_identity_any": identity_any,
        "label_bias_stratum_code": (
            target_binary.astype(np.int16) * (1 << len(EVALUATED_IDENTITY_COLUMNS))
            + identity_mask.astype(np.int16)
        ),
        "label_reliability": (
            np.abs(train_raw["target"].to_numpy(dtype=np.float32) - 0.5)
            * 2.0
            * np.log1p(train_raw["toxicity_annotator_count"].to_numpy(dtype=np.float32))
        ).astype(np.float32),
    },
    index=train_raw.index,
)

for identity_column in ALL_IDENTITY_COLUMNS:
    label_frame[f"label_identity_{identity_column}"] = train_raw[
        identity_column
    ].to_numpy(dtype=np.float32)

for auxiliary_column in AUXILIARY_LABEL_COLUMNS:
    label_frame[f"label_{auxiliary_column}"] = train_raw[auxiliary_column].to_numpy(
        dtype=np.float32
    )


def make_labeled_partition(indices, scaled_features):
    partition = label_frame.iloc[indices].reset_index(drop=True)
    partition.insert(1, "model_text", all_model_text.iloc[indices].to_numpy())

    scaled_frame = pd.DataFrame(
        scaled_features,
        columns=scaled_feature_columns,
    )

    return pd.concat([partition, scaled_frame], axis=1)


train_data = make_labeled_partition(train_indices, scaled_train_features)
valid_data = make_labeled_partition(valid_indices, scaled_valid_features)

test_data = pd.DataFrame(
    {
        "id": test_raw["id"].to_numpy(),
        "model_text": test_model_text.to_numpy(),
    }
)

test_data = pd.concat(
    [
        test_data,
        pd.DataFrame(scaled_test_features, columns=scaled_feature_columns),
    ],
    axis=1,
)

if train_data["model_text"].isna().any() or valid_data["model_text"].isna().any():
    raise ValueError("Text normalization produced missing model inputs.")

if len(test_data) != len(test_raw) or not np.array_equal(
    test_data["id"].to_numpy(),
    test_raw["id"].to_numpy(),
):
    raise RuntimeError("Test row order or identifiers changed during preprocessing.")


def save_table(frame, stem):
    parquet_path = PROCESSED_DIR / f"{stem}.parquet"
    try:
        frame.to_parquet(parquet_path, index=False, compression="snappy")
        return str(parquet_path)
    except Exception:
        pickle_path = PROCESSED_DIR / f"{stem}.pkl"
        frame.to_pickle(pickle_path)
        return str(pickle_path)


train_output_path = save_table(train_data, "train_features")
valid_output_path = save_table(valid_data, "valid_features")
test_output_path = save_table(test_data, "test_features")

np.savez_compressed(
    PROCESSED_DIR / "text_feature_scaler.npz",
    feature_columns=np.asarray(feature_columns),
    scaled_feature_columns=np.asarray(scaled_feature_columns),
    mean=scaler.mean_.astype(np.float32),
    scale=scaler.scale_.astype(np.float32),
)

manifest = {
    "seed": SEED,
    "validation_fold": VALID_FOLD,
    "n_splits": N_SPLITS,
    "split_method": (
        "StratifiedGroupKFold on target_binary + identity_any, "
        "grouped by canonical comment text"
    ),
    "train_path": train_output_path,
    "valid_path": valid_output_path,
    "test_path": test_output_path,
    "n_train": int(len(train_data)),
    "n_valid": int(len(valid_data)),
    "n_test": int(len(test_data)),
    "model_text_column": "model_text",
    "inference_feature_columns": ["model_text", *scaled_feature_columns],
    "target_column": "label_target_binary",
    "soft_target_column": "label_target_soft",
    "evaluated_identity_columns": [
        f"label_identity_{column}" for column in EVALUATED_IDENTITY_COLUMNS
    ],
    "training_only_label_columns": [
        column for column in train_data.columns if column.startswith("label_")
    ],
}

with open(PROCESSED_DIR / "manifest.json", "w", encoding="utf-8") as manifest_file:
    json.dump(manifest, manifest_file, indent=2)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
base_model = ModernBertForSequenceClassification.from_pretrained(model_id)


class ToxicityRanker(nn.Module):
    """
    Text-only inference model. Identity membership is deliberately absent from
    forward inputs and is used exclusively by the training objective.
    """

    def __init__(
        self,
        pretrained_sequence_classifier,
        num_style_features,
        style_hidden_size=96,
        dropout_probability=0.15,
    ):
        super().__init__()

        self.encoder = pretrained_sequence_classifier.model
        hidden_size = pretrained_sequence_classifier.config.hidden_size

        self.text_dropout = nn.Dropout(dropout_probability)

        self.style_encoder = nn.Sequential(
            nn.LayerNorm(num_style_features),
            nn.Linear(num_style_features, style_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden_size + style_hidden_size),
            nn.Linear(hidden_size + style_hidden_size, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.classifier = nn.Linear(hidden_size, 1)
        nn.init.normal_(self.classifier.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.classifier.bias)

    def forward(self, input_ids, attention_mask, style_features=None):
        encoder_output = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        text_representation = self.text_dropout(encoder_output.last_hidden_state[:, 0])

        if style_features is None:
            style_features = torch.zeros(
                (input_ids.shape[0], NUM_STYLE_FEATURES),
                dtype=text_representation.dtype,
                device=text_representation.device,
            )
        else:
            style_features = style_features.to(dtype=text_representation.dtype)

        style_representation = self.style_encoder(style_features)

        fused_representation = self.fusion(
            torch.cat(
                [text_representation, style_representation],
                dim=-1,
            )
        )

        return self.classifier(fused_representation).squeeze(-1)


class StratifiedAUCMemoryObjective(nn.Module):
    """
    BCE is aligned to the binary competition target. The ranking term uses
    training-only identity flags to form the three official conditional ranking
    relations: subgroup, BPSN, and BNSP.
    """

    def __init__(
        self,
        num_identities,
        bce_weight=1.0,
        pairwise_weight=0.15,
        memory_size=256,
        max_pairs_per_side=64,
    ):
        super().__init__()

        self.num_identities = num_identities
        self.bce_weight = bce_weight
        self.pairwise_weight = pairwise_weight
        self.memory_size = memory_size
        self.max_pairs_per_side = max_pairs_per_side
        self.reset_memory()

    def reset_memory(self):
        self.subgroup_positive_memory = [
            deque(maxlen=self.memory_size) for _ in range(self.num_identities)
        ]
        self.subgroup_negative_memory = [
            deque(maxlen=self.memory_size) for _ in range(self.num_identities)
        ]
        self.background_positive_memory = [
            deque(maxlen=self.memory_size) for _ in range(self.num_identities)
        ]
        self.background_negative_memory = [
            deque(maxlen=self.memory_size) for _ in range(self.num_identities)
        ]

    def _sample_current(self, values):
        if values.numel() <= self.max_pairs_per_side:
            return values

        sampled_indices = torch.randperm(
            values.numel(),
            device=values.device,
        )[: self.max_pairs_per_side]

        return values[sampled_indices]

    def _memory_tensor(self, memory_queue, device, dtype):
        if not memory_queue:
            return None

        memory_values = torch.tensor(
            list(memory_queue),
            device=device,
            dtype=dtype,
        )

        if memory_values.numel() > self.max_pairs_per_side:
            sample_indices = torch.randint(
                low=0,
                high=memory_values.numel(),
                size=(self.max_pairs_per_side,),
                device=device,
            )
            memory_values = memory_values[sample_indices]

        return memory_values

    def _pairwise_logistic_loss(self, positive_scores, negative_scores):
        if positive_scores.numel() == 0 or negative_scores.numel() == 0:
            return None

        pair_count = min(
            positive_scores.numel(),
            negative_scores.numel(),
            self.max_pairs_per_side,
        )

        positive_scores = positive_scores[
            torch.randperm(
                positive_scores.numel(),
                device=positive_scores.device,
            )[:pair_count]
        ]

        negative_scores = negative_scores[
            torch.randperm(
                negative_scores.numel(),
                device=negative_scores.device,
            )[:pair_count]
        ]

        return F.softplus(negative_scores - positive_scores).mean()

    def _stratum_ranking_loss(
        self,
        current_positive,
        current_negative,
        positive_memory,
        negative_memory,
    ):
        loss_terms = []

        in_batch_loss = self._pairwise_logistic_loss(
            current_positive,
            current_negative,
        )

        if in_batch_loss is not None:
            loss_terms.append(in_batch_loss)

        detached_negative_memory = self._memory_tensor(
            negative_memory,
            current_positive.device,
            current_positive.dtype,
        )

        if detached_negative_memory is not None and current_positive.numel() > 0:
            current_positive = self._sample_current(current_positive)

            paired_negatives = detached_negative_memory[
                torch.randint(
                    low=0,
                    high=detached_negative_memory.numel(),
                    size=(current_positive.numel(),),
                    device=current_positive.device,
                )
            ]

            loss_terms.append(F.softplus(paired_negatives - current_positive).mean())

        detached_positive_memory = self._memory_tensor(
            positive_memory,
            current_negative.device,
            current_negative.dtype,
        )

        if detached_positive_memory is not None and current_negative.numel() > 0:
            current_negative = self._sample_current(current_negative)

            paired_positives = detached_positive_memory[
                torch.randint(
                    low=0,
                    high=detached_positive_memory.numel(),
                    size=(current_negative.numel(),),
                    device=current_negative.device,
                )
            ]

            loss_terms.append(F.softplus(current_negative - paired_positives).mean())

        if not loss_terms:
            return None

        return torch.stack(loss_terms).mean()

    def ranking_loss(
        self,
        logits,
        binary_targets,
        identity_flags,
        identity_available,
    ):
        if identity_flags.ndim != 2:
            raise ValueError(
                "identity_flags must have shape [batch_size, num_identities]."
            )

        if identity_flags.shape[1] != self.num_identities:
            raise ValueError(
                f"Expected {self.num_identities} evaluated identities, "
                f"received {identity_flags.shape[1]}."
            )

        targets = binary_targets.bool()
        known_identity_labels = identity_available.bool()
        subgroup_flags = identity_flags.bool()
        all_losses = []

        for identity_index in range(self.num_identities):
            in_subgroup = subgroup_flags[:, identity_index] & known_identity_labels
            in_background = (~subgroup_flags[:, identity_index]) & known_identity_labels

            subgroup_positive = logits[in_subgroup & targets]
            subgroup_negative = logits[in_subgroup & (~targets)]
            background_positive = logits[in_background & targets]
            background_negative = logits[in_background & (~targets)]

            subgroup_auc_loss = self._stratum_ranking_loss(
                subgroup_positive,
                subgroup_negative,
                self.subgroup_positive_memory[identity_index],
                self.subgroup_negative_memory[identity_index],
            )

            if subgroup_auc_loss is not None:
                all_losses.append(subgroup_auc_loss)

            bpsn_auc_loss = self._stratum_ranking_loss(
                background_positive,
                subgroup_negative,
                self.background_positive_memory[identity_index],
                self.subgroup_negative_memory[identity_index],
            )

            if bpsn_auc_loss is not None:
                all_losses.append(bpsn_auc_loss)

            bnsp_auc_loss = self._stratum_ranking_loss(
                subgroup_positive,
                background_negative,
                self.subgroup_positive_memory[identity_index],
                self.background_negative_memory[identity_index],
            )

            if bnsp_auc_loss is not None:
                all_losses.append(bnsp_auc_loss)

        if not all_losses:
            return logits.sum() * 0.0

        return torch.stack(all_losses).mean()

    def forward(
        self,
        logits,
        binary_targets,
        identity_flags,
        identity_available,
    ):
        logits = logits.reshape(-1)
        binary_targets = binary_targets.reshape(-1).float()

        if logits.shape[0] != binary_targets.shape[0]:
            raise ValueError("logits and binary_targets must have equal batch size.")

        bce_loss = F.binary_cross_entropy_with_logits(
            logits,
            binary_targets,
        )

        pairwise_loss = self.ranking_loss(
            logits=logits,
            binary_targets=binary_targets,
            identity_flags=identity_flags,
            identity_available=identity_available,
        )

        return self.bce_weight * bce_loss + self.pairwise_weight * pairwise_loss

    @torch.no_grad()
    def update_memory(
        self,
        logits,
        binary_targets,
        identity_flags,
        identity_available,
    ):
        logits = logits.detach().reshape(-1).float().cpu()
        targets = binary_targets.detach().reshape(-1).bool().cpu()
        identity_flags = identity_flags.detach().bool().cpu()
        identity_available = identity_available.detach().reshape(-1).bool().cpu()

        for identity_index in range(self.num_identities):
            subgroup = identity_flags[:, identity_index] & identity_available
            background = (~identity_flags[:, identity_index]) & identity_available

            for value in logits[subgroup & targets].tolist():
                self.subgroup_positive_memory[identity_index].append(value)

            for value in logits[subgroup & (~targets)].tolist():
                self.subgroup_negative_memory[identity_index].append(value)

            for value in logits[background & targets].tolist():
                self.background_positive_memory[identity_index].append(value)

            for value in logits[background & (~targets)].tolist():
                self.background_negative_memory[identity_index].append(value)


model = ToxicityRanker(
    pretrained_sequence_classifier=base_model,
    num_style_features=NUM_STYLE_FEATURES,
)

# AdamW failed when it lazily allocated moment tensors for the large encoder.
# Keep the pretrained semantic encoder fixed and train the task-specific fusion
# head, eliminating encoder gradients and AdamW state while preserving model inference.
for parameter in model.encoder.parameters():
    parameter.requires_grad_(False)

del base_model

criterion = StratifiedAUCMemoryObjective(
    num_identities=NUM_EVALUATED_IDENTITIES,
    bce_weight=BCE_WEIGHT,
    pairwise_weight=PAIRWISE_WEIGHT,
    memory_size=PAIR_MEMORY_SIZE,
    max_pairs_per_side=MAX_PAIRS_PER_SIDE,
)

no_decay_terms = (
    "bias",
    "LayerNorm.weight",
    "layer_norm.weight",
    "norm.weight",
)

encoder_decay_parameters = []
encoder_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = any(term in parameter_name for term in no_decay_terms)
    is_encoder_parameter = parameter_name.startswith("encoder.")

    if is_encoder_parameter and is_no_decay:
        encoder_no_decay_parameters.append(parameter)
    elif is_encoder_parameter:
        encoder_decay_parameters.append(parameter)
    elif is_no_decay:
        head_no_decay_parameters.append(parameter)
    else:
        head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": encoder_decay_parameters,
            "lr": ENCODER_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
        {
            "params": encoder_no_decay_parameters,
            "lr": ENCODER_LEARNING_RATE,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_parameters,
            "lr": HEAD_LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
        },
        {
            "params": head_no_decay_parameters,
            "lr": HEAD_LEARNING_RATE,
            "weight_decay": 0.0,
        },
    ]
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"

if use_amp:
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

identity_label_columns = [
    f"label_identity_{identity_name}" for identity_name in EVALUATED_IDENTITY_COLUMNS
]


class ToxicityDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.texts = frame["model_text"].fillna("[EMPTY_COMMENT]").astype(str).tolist()

        self.style_features = np.ascontiguousarray(
            frame[scaled_feature_columns].to_numpy(
                dtype=np.float32,
                copy=True,
            )
        )

        self.include_labels = include_labels

        if include_labels:
            self.targets = frame["label_target_binary"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

            self.identity_flags = (
                np.nan_to_num(
                    frame[identity_label_columns].to_numpy(
                        dtype=np.float32,
                        copy=True,
                    ),
                    nan=0.0,
                )
                >= 0.5
            ).astype(np.float32)

            self.identity_available = frame[
                "label_identity_annotation_available"
            ].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        sample = {
            "text": self.texts[index],
            "style_features": self.style_features[index],
        }

        if self.include_labels:
            sample["target"] = self.targets[index]
            sample["identity_flags"] = self.identity_flags[index]
            sample["identity_available"] = self.identity_available[index]

        return sample


def collate_batch(samples):
    encoded = tokenizer(
        [sample["text"] for sample in samples],
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        padding=True,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )

    batch = {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "style_features": torch.from_numpy(
            np.stack(
                [sample["style_features"] for sample in samples],
                axis=0,
            ).astype(np.float32, copy=False)
        ),
    }

    if "target" in samples[0]:
        batch["target"] = torch.tensor(
            [sample["target"] for sample in samples],
            dtype=torch.float32,
        )

        batch["identity_flags"] = torch.from_numpy(
            np.stack(
                [sample["identity_flags"] for sample in samples],
                axis=0,
            ).astype(np.float32, copy=False)
        )

        batch["identity_available"] = torch.tensor(
            [sample["identity_available"] for sample in samples],
            dtype=torch.float32,
        )

    return batch


train_dataset = ToxicityDataset(train_data, include_labels=True)
valid_dataset = ToxicityDataset(valid_data, include_labels=True)
test_dataset = ToxicityDataset(test_data, include_labels=False)

loader_options = {
    "num_workers": NUM_WORKERS,
    "pin_memory": use_amp,
    "collate_fn": collate_batch,
}

if NUM_WORKERS > 0:
    loader_options["persistent_workers"] = True
    loader_options["prefetch_factor"] = 2

train_generator = torch.Generator()
train_generator.manual_seed(SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=train_generator,
    drop_last=False,
    **loader_options,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_options,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_options,
)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_updates = updates_per_epoch * NUM_EPOCHS
warmup_updates = max(1, int(total_updates * WARMUP_FRACTION))

scheduler = get_cosine_schedule_with_warmup(
    optimizer=optimizer,
    num_warmup_steps=warmup_updates,
    num_training_steps=total_updates,
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=use_amp)


def move_to_device(batch):
    return {
        key: value.to(device, non_blocking=use_amp)
        for key, value in batch.items()
        if key != "text"
    }


def safe_roc_auc(labels, predictions, metric_name):
    labels = np.asarray(labels, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if np.unique(labels).size != 2:
        raise ValueError(
            f"{metric_name} is undefined because its validation subset "
            "does not contain both toxicity classes."
        )

    return float(roc_auc_score(labels, predictions))


def official_bias_score(binary_targets, predictions, identity_values_array):
    binary_targets = np.asarray(binary_targets, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)
    identity_values_array = np.asarray(
        identity_values_array,
        dtype=np.float32,
    )

    if len(binary_targets) != len(predictions):
        raise ValueError("Validation labels and predictions have different lengths.")

    expected_shape = (
        len(binary_targets),
        len(EVALUATED_IDENTITY_COLUMNS),
    )

    if identity_values_array.shape != expected_shape:
        raise ValueError("Identity-label shape does not match evaluated identities.")

    if not np.isfinite(predictions).all():
        raise ValueError("Model inference produced non-finite predictions.")

    overall_auc = safe_roc_auc(
        binary_targets,
        predictions,
        "overall AUC",
    )

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    identity_flags_array = np.nan_to_num(identity_values_array, nan=0.0) >= 0.5

    for identity_index, identity_name in enumerate(EVALUATED_IDENTITY_COLUMNS):
        subgroup = identity_flags_array[:, identity_index]
        background = ~subgroup
        toxic = binary_targets.astype(bool)
        non_toxic = ~toxic

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & non_toxic) | (background & toxic)
        bnsp_mask = (subgroup & toxic) | (background & non_toxic)

        subgroup_aucs.append(
            safe_roc_auc(
                binary_targets[subgroup_mask],
                predictions[subgroup_mask],
                f"{identity_name} subgroup AUC",
            )
        )

        bpsn_aucs.append(
            safe_roc_auc(
                binary_targets[bpsn_mask],
                predictions[bpsn_mask],
                f"{identity_name} BPSN AUC",
            )
        )

        bnsp_aucs.append(
            safe_roc_auc(
                binary_targets[bnsp_mask],
                predictions[bnsp_mask],
                f"{identity_name} BNSP AUC",
            )
        )

    def generalized_mean(values):
        values = np.asarray(values, dtype=np.float64)
        return float(np.mean(values**POWER_MEAN_P) ** (1.0 / POWER_MEAN_P))

    subgroup_generalized_mean = generalized_mean(subgroup_aucs)
    bpsn_generalized_mean = generalized_mean(bpsn_aucs)
    bnsp_generalized_mean = generalized_mean(bnsp_aucs)

    final_score = 0.25 * (
        overall_auc
        + subgroup_generalized_mean
        + bpsn_generalized_mean
        + bnsp_generalized_mean
    )

    return {
        "final_score": float(final_score),
        "overall_auc": float(overall_auc),
        "subgroup_generalized_mean": float(subgroup_generalized_mean),
        "bpsn_generalized_mean": float(bpsn_generalized_mean),
        "bnsp_generalized_mean": float(bnsp_generalized_mean),
    }


@torch.inference_mode()
def predict_from_loader(data_loader):
    model.eval()
    all_predictions = []

    for batch in data_loader:
        batch = move_to_device(batch)

        autocast_context = (
            torch.cuda.amp.autocast(enabled=True) if use_amp else nullcontext()
        )

        with autocast_context:
            logits = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                style_features=batch["style_features"],
            )
            probabilities = torch.sigmoid(logits)

        all_predictions.append(probabilities.float().cpu().numpy())

    predictions = np.concatenate(all_predictions).astype(
        np.float64,
        copy=False,
    )

    if not np.isfinite(predictions).all():
        raise ValueError("Model inference produced non-finite predictions.")

    return predictions


model = model.to(device)

best_score = -np.inf
best_epoch = -1

for epoch in range(NUM_EPOCHS):
    model.train()
    # model.train() recursively changes submodules; retain deterministic frozen features.
    model.encoder.eval()
    criterion.reset_memory()
    optimizer.zero_grad(set_to_none=True)

    cumulative_loss = 0.0
    observed_batches = 0
    pending_memory_updates = []

    for batch_index, batch in enumerate(train_loader):
        batch = move_to_device(batch)

        autocast_context = (
            torch.cuda.amp.autocast(enabled=True) if use_amp else nullcontext()
        )

        with autocast_context:
            logits = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                style_features=batch["style_features"],
            )

            batch_loss = criterion(
                logits=logits,
                binary_targets=batch["target"],
                identity_flags=batch["identity_flags"],
                identity_available=batch["identity_available"],
            )

            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(batch_loss):
            raise FloatingPointError(
                f"Non-finite loss encountered during epoch {epoch + 1}."
            )

        amp_scaler.scale(scaled_loss).backward()

        cumulative_loss += float(batch_loss.detach().cpu())
        observed_batches += 1

        pending_memory_updates.append(
            (
                logits.detach(),
                batch["target"].detach(),
                batch["identity_flags"].detach(),
                batch["identity_available"].detach(),
            )
        )

        should_update = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if should_update:
            amp_scaler.unscale_(optimizer)

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                MAX_GRAD_NORM,
            )

            amp_scaler.step(optimizer)
            amp_scaler.update()
            scheduler.step()
            optimizer.zero_grad(set_to_none=True)

            for (
                memory_logits,
                memory_target,
                memory_identities,
                memory_available,
            ) in pending_memory_updates:
                criterion.update_memory(
                    logits=memory_logits,
                    binary_targets=memory_target,
                    identity_flags=memory_identities,
                    identity_available=memory_available,
                )

            pending_memory_updates.clear()

    validation_predictions = predict_from_loader(valid_loader)

    validation_metrics = official_bias_score(
        binary_targets=valid_data["label_target_binary"].to_numpy(dtype=np.int8),
        predictions=validation_predictions,
        identity_values_array=valid_data[identity_label_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        ),
    )

    epoch_score = validation_metrics["final_score"]

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch

        torch.save(
            {
                "epoch": epoch,
                "validation_metrics": validation_metrics,
                "model_state_dict": model.state_dict(),
            },
            BEST_MODEL_PATH,
        )

    mean_train_loss = cumulative_loss / max(observed_batches, 1)
    mean_bias_score = np.mean(
        [
            validation_metrics["subgroup_generalized_mean"],
            validation_metrics["bpsn_generalized_mean"],
            validation_metrics["bnsp_generalized_mean"],
        ]
    )

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"loss={mean_train_loss:.6f} "
        f"official_score={epoch_score:.6f} "
        f"overall_auc={validation_metrics['overall_auc']:.6f} "
        f"bias_mean={mean_bias_score:.6f}"
    )

if best_epoch < 0 or not BEST_MODEL_PATH.exists():
    raise RuntimeError("No valid model checkpoint was saved.")

best_checkpoint = torch.load(BEST_MODEL_PATH, map_location=device)
model.load_state_dict(best_checkpoint["model_state_dict"], strict=True)
model = model.to(device)
model.eval()

final_validation_predictions = predict_from_loader(valid_loader)

final_validation_metrics = official_bias_score(
    binary_targets=valid_data["label_target_binary"].to_numpy(dtype=np.int8),
    predictions=final_validation_predictions,
    identity_values_array=valid_data[identity_label_columns].to_numpy(
        dtype=np.float32,
        copy=True,
    ),
)

test_predictions = predict_from_loader(test_loader)

if len(test_predictions) != len(test_data):
    raise RuntimeError("Test inference did not produce one prediction per test row.")

submission = pd.DataFrame(
    {
        "id": test_data["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if submission["id"].duplicated().any():
    raise RuntimeError("Submission contains duplicate identifiers.")

sample_submission_path = INPUT_DIR / "sample_submission.csv"
if sample_submission_path.exists():
    sample_submission = pd.read_csv(sample_submission_path, usecols=["id"])
    if not np.array_equal(
        submission["id"].to_numpy(),
        sample_submission["id"].to_numpy(),
    ):
        raise RuntimeError(
            "Submission identifier order does not match sample_submission.csv."
        )

submission.to_csv(SUBMISSION_DIR / "submission_77ff443c80bf484fa4af16c7424949ed.csv", index=False)

score = float(final_validation_metrics["final_score"])
print(f"Final Validation Score: {score}")
