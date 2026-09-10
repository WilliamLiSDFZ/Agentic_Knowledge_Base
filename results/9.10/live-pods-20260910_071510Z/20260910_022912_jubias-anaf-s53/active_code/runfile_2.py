import os
os.sched_setaffinity(0, {69, 70})
import gc
import html
import json
import math
import os
import re
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import pandas as pd

# Reduce CUDA allocator fragmentation before Torch initializes CUDA.
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedShuffleSplit
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
    get_cosine_schedule_with_warmup,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

SEED = 2025
MODEL_SEED = 2025
TRAINING_SEED = 2025

VALID_FRACTION = 0.10
MAX_COUNTERFACTUAL_ROWS = 100_000

MAX_EPOCHS = 1
MAX_SEQUENCE_LENGTH = 192
TARGET_EFFECTIVE_BATCH_SIZE = 32
# The runtime reports that more than two workers can cause slowdowns or freezes.
NUM_WORKERS = 2
MAX_GRAD_NORM = 1.0
WARMUP_FRACTION = 0.03

INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = INPUT_DIR / "train.csv"
TEST_PATH = INPUT_DIR / "test.csv"
SAMPLE_SUBMISSION_PATH = INPUT_DIR / "sample_submission.csv"

TARGET_COLUMN = "target"
TEXT_COLUMN = "comment_text"
ID_COLUMN = "id"

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

AUXILIARY_TOXICITY_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

ANNOTATION_COLUMNS = [
    "toxicity_annotator_count",
    "identity_annotator_count",
]

MODEL_OUTPUT_NAMES = ["toxicity"] + AUXILIARY_TOXICITY_COLUMNS
NUM_MODEL_OUTPUTS = len(MODEL_OUTPUT_NAMES)
TOXICITY_LOGIT_INDEX = 0
AUXILIARY_LOGIT_SLICE = slice(1, NUM_MODEL_OUTPUTS)

torch.manual_seed(MODEL_SEED)
np.random.seed(SEED)

requested_columns = (
    [ID_COLUMN, TEXT_COLUMN, TARGET_COLUMN]
    + AUXILIARY_TOXICITY_COLUMNS
    + IDENTITY_COLUMNS
    + ANNOTATION_COLUMNS
)

available_train_columns = pd.read_csv(TRAIN_PATH, nrows=1).columns.tolist()
train_usecols = [
    column for column in requested_columns if column in available_train_columns
]

train_raw = pd.read_csv(TRAIN_PATH, usecols=train_usecols)
test_raw = pd.read_csv(TEST_PATH, usecols=[ID_COLUMN, TEXT_COLUMN])
sample_submission = pd.read_csv(SAMPLE_SUBMISSION_PATH)

if not np.array_equal(
    test_raw[ID_COLUMN].to_numpy(), sample_submission[ID_COLUMN].to_numpy()
):
    raise ValueError("test.csv row order does not match sample_submission.csv")

for column in IDENTITY_COLUMNS + AUXILIARY_TOXICITY_COLUMNS + ANNOTATION_COLUMNS:
    if column not in train_raw.columns:
        train_raw[column] = np.nan

raw_text_for_groups = train_raw[TEXT_COLUMN].fillna("").astype(str)
text_group_codes, _ = pd.factorize(raw_text_for_groups, sort=False)

target_binary = (train_raw[TARGET_COLUMN].to_numpy(dtype=np.float32) >= 0.5).astype(
    np.int8
)
identity_matrix = (
    train_raw[EVALUATION_IDENTITIES].fillna(0.0).to_numpy(dtype=np.float32)
)
identity_any = (identity_matrix >= 0.5).any(axis=1).astype(np.int8)

group_summary = (
    pd.DataFrame(
        {
            "group_code": text_group_codes,
            "target_binary": target_binary,
            "identity_any": identity_any,
        }
    )
    .groupby("group_code", sort=False, as_index=False)
    .agg(
        target_binary=("target_binary", "mean"),
        identity_any=("identity_any", "max"),
    )
)

group_summary["target_binary"] = (group_summary["target_binary"] >= 0.5).astype(np.int8)
group_summary["identity_any"] = group_summary["identity_any"].astype(np.int8)

group_strata = (
    group_summary["target_binary"].astype(str)
    + "_"
    + group_summary["identity_any"].astype(str)
)

stratum_counts = group_strata.value_counts()
rare_strata = stratum_counts[stratum_counts < 2].index
if len(rare_strata) > 0:
    group_strata = group_strata.where(
        ~group_strata.isin(rare_strata),
        group_summary["target_binary"].astype(str) + "_fallback",
    )

splitter = StratifiedShuffleSplit(
    n_splits=1,
    test_size=VALID_FRACTION,
    random_state=SEED,
)

group_indices = np.arange(len(group_summary))
train_group_idx, valid_group_idx = next(splitter.split(group_indices, group_strata))

is_validation_group = np.zeros(len(group_summary), dtype=bool)
is_validation_group[valid_group_idx] = True

validation_mask = is_validation_group[text_group_codes]
training_mask = ~validation_mask

if validation_mask.sum() == 0 or training_mask.sum() == 0:
    raise RuntimeError("Split construction produced an empty partition")

train_partition = train_raw.loc[training_mask].copy()
valid_partition = train_raw.loc[validation_mask].copy()

del raw_text_for_groups
del text_group_codes
del group_summary
del group_strata
del target_binary
del identity_matrix
del identity_any
del train_group_idx
del valid_group_idx
del is_validation_group
del validation_mask
del training_mask
del train_raw
gc.collect()

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
EMAIL_PATTERN = re.compile(r"(?i)\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
HTML_TAG_PATTERN = re.compile(r"(?is)<[^>]+>")
WHITESPACE_PATTERN = re.compile(r"\s+")


def normalize_comment_text(values: pd.Series) -> pd.Series:
    text = values.fillna("").astype("string")
    text = text.str.normalize("NFKC")
    text = text.map(html.unescape)
    text = text.str.replace(HTML_TAG_PATTERN, " ", regex=True)
    text = text.str.replace(URL_PATTERN, " [URL] ", regex=True)
    text = text.str.replace(EMAIL_PATTERN, " [EMAIL] ", regex=True)
    text = text.str.replace("\u200b", "", regex=False)
    text = text.str.replace("\r\n", "\n", regex=False)
    text = text.str.replace("\r", "\n", regex=False)
    text = text.str.replace(WHITESPACE_PATTERN, " ", regex=True).str.strip()
    return text.fillna("").astype(str)


def make_text_features(text_values: pd.Series, ids: pd.Series) -> pd.DataFrame:
    normalized = normalize_comment_text(text_values)

    char_count = normalized.str.len().astype(np.float32)
    word_count = normalized.str.count(r"\S+").astype(np.float32)
    letter_count = normalized.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = normalized.str.count(r"[A-Z]").astype(np.float32)

    return pd.DataFrame(
        {
            ID_COLUMN: ids.to_numpy(),
            "model_text": normalized.to_numpy(),
            "feature_log_char_count": np.log1p(char_count).astype(np.float32),
            "feature_log_word_count": np.log1p(word_count).astype(np.float32),
            "feature_log_exclamation_count": np.log1p(
                normalized.str.count("!").astype(np.float32)
            ).astype(np.float32),
            "feature_log_question_count": np.log1p(
                normalized.str.count(r"\?").astype(np.float32)
            ).astype(np.float32),
            "feature_log_quote_count": np.log1p(
                normalized.str.count(r"""["']""").astype(np.float32)
            ).astype(np.float32),
            "feature_log_digit_count": np.log1p(
                normalized.str.count(r"\d").astype(np.float32)
            ).astype(np.float32),
            "feature_url_present": normalized.str.contains(
                r"\[URL\]", regex=True
            ).astype(np.int8),
            "feature_email_present": normalized.str.contains(
                r"\[EMAIL\]", regex=True
            ).astype(np.int8),
            "feature_uppercase_ratio": (
                uppercase_count / np.maximum(letter_count, 1.0)
            ).astype(np.float32),
            "feature_has_newline_source": text_values.fillna("")
            .astype(str)
            .str.contains(r"[\r\n]", regex=True)
            .astype(np.int8),
        }
    )


def build_prepared_partition(frame: pd.DataFrame) -> pd.DataFrame:
    prepared = make_text_features(frame[TEXT_COLUMN], frame[ID_COLUMN])

    prepared["label_target"] = pd.to_numeric(
        frame[TARGET_COLUMN], errors="coerce"
    ).astype(np.float32)

    prepared["label_target_binary"] = (
        prepared["label_target"].to_numpy() >= 0.5
    ).astype(np.int8)

    for column in AUXILIARY_TOXICITY_COLUMNS + IDENTITY_COLUMNS + ANNOTATION_COLUMNS:
        prepared[f"label_{column}"] = pd.to_numeric(
            frame[column], errors="coerce"
        ).astype(np.float32)

    prepared["label_evaluation_identity_any"] = (
        (
            prepared[[f"label_{column}" for column in EVALUATION_IDENTITIES]]
            .fillna(0.0)
            .to_numpy(dtype=np.float32)
            >= 0.5
        )
        .any(axis=1)
        .astype(np.int8)
    )

    prepared["is_counterfactual"] = np.int8(0)
    prepared["source_id"] = prepared[ID_COLUMN].to_numpy()
    prepared["counterfactual_group"] = ""
    return prepared


train_prepared = build_prepared_partition(train_partition)
valid_prepared = build_prepared_partition(valid_partition)
test_prepared = make_text_features(test_raw[TEXT_COLUMN], test_raw[ID_COLUMN])

del train_partition
del valid_partition
gc.collect()

COUNTERFACTUAL_SWAPS = {
    "gender": {
        "identities": ["male", "female"],
        "mapping": {
            "men": "women",
            "women": "men",
            "man": "woman",
            "woman": "man",
            "male": "female",
            "female": "male",
            "boy": "girl",
            "girl": "boy",
        },
    },
    "sexual_orientation": {
        "identities": ["homosexual_gay_or_lesbian", "heterosexual"],
        "mapping": {
            "homosexual": "heterosexual",
            "heterosexual": "homosexual",
            "lesbian": "straight person",
            "gay": "straight",
            "lgbtq": "straight",
            "lgbt": "straight",
            "straight": "gay",
        },
    },
    "religion": {
        "identities": ["christian", "muslim", "jewish"],
        "mapping": {
            "christians": "muslims",
            "muslims": "christians",
            "christian": "muslim",
            "muslim": "christian",
            "jewish": "muslim",
            "jews": "muslims",
        },
    },
    "race": {
        "identities": ["black", "white"],
        "mapping": {
            "black": "white",
            "white": "black",
        },
    },
}

swap_group_scores = pd.DataFrame(
    {
        group_name: train_prepared[
            [f"label_{identity}" for identity in config["identities"]]
        ]
        .fillna(0.0)
        .max(axis=1)
        for group_name, config in COUNTERFACTUAL_SWAPS.items()
    }
)

train_prepared["_cf_group"] = swap_group_scores.idxmax(axis=1)
train_prepared["_cf_strength"] = swap_group_scores.max(axis=1)

counterfactual_candidates = train_prepared.loc[
    (train_prepared["_cf_strength"] >= 0.5)
    & (train_prepared["feature_log_word_count"] >= np.log1p(3))
].copy()

if len(counterfactual_candidates) > MAX_COUNTERFACTUAL_ROWS:
    candidate_strata = (
        counterfactual_candidates["label_target_binary"].astype(str)
        + "_"
        + counterfactual_candidates["_cf_group"].astype(str)
    )

    sampled_parts = []
    rng = np.random.RandomState(SEED)
    strata_sizes = candidate_strata.value_counts()

    for stratum, count in strata_sizes.items():
        part = counterfactual_candidates.loc[candidate_strata == stratum]
        take = max(
            1,
            int(
                round(MAX_COUNTERFACTUAL_ROWS * count / len(counterfactual_candidates))
            ),
        )
        take = min(take, len(part))
        sampled_parts.append(part.iloc[rng.choice(len(part), size=take, replace=False)])

    counterfactual_candidates = pd.concat(sampled_parts, ignore_index=True)

    if len(counterfactual_candidates) > MAX_COUNTERFACTUAL_ROWS:
        counterfactual_candidates = counterfactual_candidates.sample(
            n=MAX_COUNTERFACTUAL_ROWS,
            random_state=SEED,
        )


def replace_with_case(match: re.Match, replacement: str) -> str:
    token = match.group(0)

    if token.isupper():
        return replacement.upper()
    if token[:1].isupper():
        return replacement.capitalize()

    return replacement


def counterfactual_swap(text: str, group_name: str) -> str:
    mapping = COUNTERFACTUAL_SWAPS[group_name]["mapping"]
    ordered_terms = sorted(mapping, key=len, reverse=True)

    pattern = re.compile(
        r"\b(" + "|".join(re.escape(term) for term in ordered_terms) + r")\b",
        re.I,
    )

    def substitute(match: re.Match) -> str:
        replacement = mapping[match.group(0).lower()]
        return replace_with_case(match, replacement)

    return pattern.sub(substitute, text)


swapped_texts = [
    counterfactual_swap(text, group_name)
    for text, group_name in zip(
        counterfactual_candidates["model_text"].tolist(),
        counterfactual_candidates["_cf_group"].tolist(),
    )
]

changed_mask = np.fromiter(
    (
        new_text != old_text
        for new_text, old_text in zip(
            swapped_texts,
            counterfactual_candidates["model_text"].tolist(),
        )
    ),
    dtype=bool,
    count=len(swapped_texts),
)

counterfactual_candidates = counterfactual_candidates.loc[changed_mask].reset_index(
    drop=True
)
swapped_texts = [text for text, keep in zip(swapped_texts, changed_mask) if keep]

if len(counterfactual_candidates) > 0:
    counterfactual_prepared = make_text_features(
        pd.Series(swapped_texts, dtype="string"),
        pd.Series(-counterfactual_candidates["source_id"].to_numpy()),
    )

    copied_label_columns = ["label_target", "label_target_binary"] + [
        f"label_{column}" for column in AUXILIARY_TOXICITY_COLUMNS + ANNOTATION_COLUMNS
    ]

    for column in copied_label_columns:
        counterfactual_prepared[column] = counterfactual_candidates[column].to_numpy()

    for column in IDENTITY_COLUMNS:
        counterfactual_prepared[f"label_{column}"] = np.float32(np.nan)

    counterfactual_prepared["label_evaluation_identity_any"] = np.int8(0)
    counterfactual_prepared["is_counterfactual"] = np.int8(1)
    counterfactual_prepared["source_id"] = counterfactual_candidates[
        "source_id"
    ].to_numpy()
    counterfactual_prepared["counterfactual_group"] = counterfactual_candidates[
        "_cf_group"
    ].to_numpy()
else:
    counterfactual_prepared = pd.DataFrame(columns=train_prepared.columns)

train_prepared = train_prepared.drop(columns=["_cf_group", "_cf_strength"])

del counterfactual_candidates
del swap_group_scores
del swapped_texts
gc.collect()

train_prepared.to_pickle(WORKING_DIR / "train_prepared.pkl")
valid_prepared.to_pickle(WORKING_DIR / "valid_prepared.pkl")
test_prepared.to_pickle(WORKING_DIR / "test_prepared.pkl")
counterfactual_prepared.to_pickle(WORKING_DIR / "train_counterfactual_prepared.pkl")

split_manifest = {
    "seed": SEED,
    "validation_fraction": VALID_FRACTION,
    "split_strategy": "stratified_raw_text_group_holdout",
    "stratification": "binary_target_x_any_evaluation_identity",
    "target_semantics": "label_target_binary = (label_target >= 0.5)",
    "official_evaluation_identities": EVALUATION_IDENTITIES,
    "official_metric": (
        "0.25 * overall_auc + 0.25 * power_mean(subgroup_auc, p=-5) + "
        "0.25 * power_mean(bpsn_auc, p=-5) + 0.25 * power_mean(bnsp_auc, p=-5)"
    ),
    "train_rows": int(len(train_prepared)),
    "validation_rows": int(len(valid_prepared)),
    "test_rows": int(len(test_prepared)),
    "counterfactual_train_rows": int(len(counterfactual_prepared)),
    "model_input_column": "model_text",
    "numeric_inference_features": [
        column
        for column in test_prepared.columns
        if column not in [ID_COLUMN, "model_text"]
    ],
}

with open(
    WORKING_DIR / "data_processing_manifest.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(split_manifest, file, indent=2)

# The base checkpoint preserves the ModernBERT text-classification approach while
# fitting alongside other GPU processes and AdamW state.
model_id = "answerdotai/ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

if not hasattr(model, "classifier") or not isinstance(model.classifier, nn.Linear):
    raise RuntimeError(
        "Unexpected ModernBERT classification-head structure; expected a linear classifier."
    )

classifier_input_size = model.classifier.in_features
model.classifier = nn.Linear(classifier_input_size, NUM_MODEL_OUTPUTS)
model.num_labels = NUM_MODEL_OUTPUTS
model.config.num_labels = NUM_MODEL_OUTPUTS
model.config.problem_type = "multi_label_classification"
model.config.id2label = {
    index: label_name for index, label_name in enumerate(MODEL_OUTPUT_NAMES)
}
model.config.label2id = {
    label_name: index for index, label_name in enumerate(MODEL_OUTPUT_NAMES)
}

if hasattr(model, "drop"):
    model.drop = nn.Dropout(p=0.15)

# The pretrained encoder is used in every forward pass, but freezing it prevents
# gradient and AdamW-state allocation for hundreds of millions of backbone weights.
# The classification head remains trainable for this toxicity task.
for parameter_name, parameter in model.named_parameters():
    if not parameter_name.startswith("classifier."):
        parameter.requires_grad_(False)


class OfficialBiasRankingLoss(nn.Module):
    def __init__(
        self,
        pairwise_weight: float = 0.40,
        auxiliary_weight: float = 0.15,
        calibration_weight: float = 0.05,
        worst_group_temperature: float = 7.5,
        max_examples_per_class: int = 96,
    ):
        super().__init__()
        self.pairwise_weight = float(pairwise_weight)
        self.auxiliary_weight = float(auxiliary_weight)
        self.calibration_weight = float(calibration_weight)
        self.worst_group_temperature = float(worst_group_temperature)
        self.max_examples_per_class = int(max_examples_per_class)

    def _evenly_spaced_subset(self, indices: torch.Tensor) -> torch.Tensor:
        if indices.numel() <= self.max_examples_per_class:
            return indices

        positions = torch.linspace(
            0,
            indices.numel() - 1,
            self.max_examples_per_class,
            device=indices.device,
        ).long()

        return indices.index_select(0, positions)

    def _pairwise_auc_surrogate(
        self,
        toxicity_logits: torch.Tensor,
        positive_mask: torch.Tensor,
        negative_mask: torch.Tensor,
    ):
        positive_indices = torch.where(positive_mask)[0]
        negative_indices = torch.where(negative_mask)[0]

        if positive_indices.numel() == 0 or negative_indices.numel() == 0:
            return None

        positive_indices = self._evenly_spaced_subset(positive_indices)
        negative_indices = self._evenly_spaced_subset(negative_indices)

        positive_scores = toxicity_logits.index_select(0, positive_indices)
        negative_scores = toxicity_logits.index_select(0, negative_indices)

        margin_matrix = positive_scores[:, None] - negative_scores[None, :]
        return F.softplus(-margin_matrix).mean()

    def forward(
        self,
        logits: torch.Tensor,
        toxicity_targets: torch.Tensor,
        identity_targets: torch.Tensor,
        auxiliary_targets: torch.Tensor = None,
    ):
        if logits.ndim != 2 or logits.shape[1] != NUM_MODEL_OUTPUTS:
            raise ValueError(
                f"Expected logits shaped [batch, {NUM_MODEL_OUTPUTS}], received "
                f"{tuple(logits.shape)}."
            )

        if identity_targets.ndim != 2 or identity_targets.shape[1] != len(
            EVALUATION_IDENTITIES
        ):
            raise ValueError(
                "identity_targets must contain exactly the official evaluation "
                f"identities in this order: {EVALUATION_IDENTITIES}."
            )

        toxicity_targets = toxicity_targets.float().reshape(-1).clamp(0.0, 1.0)
        toxicity_logits = logits[:, TOXICITY_LOGIT_INDEX]
        binary_targets = toxicity_targets >= 0.5

        identity_matrix = torch.nan_to_num(
            identity_targets.float(),
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )
        identity_present = identity_matrix >= 0.5
        any_identity_present = identity_present.any(dim=1)

        example_weights = torch.ones_like(toxicity_targets)
        example_weights = example_weights + 1.25 * any_identity_present.float()
        example_weights = (
            example_weights + 2.50 * (any_identity_present & ~binary_targets).float()
        )
        example_weights = (
            example_weights + 2.50 * (~any_identity_present & binary_targets).float()
        )

        primary_bce = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
            reduction="none",
        )

        primary_loss = (
            primary_bce * example_weights
        ).sum() / example_weights.sum().clamp_min(1.0)

        auxiliary_loss = toxicity_logits.sum() * 0.0

        if auxiliary_targets is not None:
            expected_shape = (
                logits.shape[0],
                len(AUXILIARY_TOXICITY_COLUMNS),
            )

            if auxiliary_targets.shape != expected_shape:
                raise ValueError(
                    "auxiliary_targets must have shape "
                    f"[batch, {len(AUXILIARY_TOXICITY_COLUMNS)}]."
                )

            auxiliary_targets = auxiliary_targets.float()
            valid_auxiliary = torch.isfinite(auxiliary_targets)

            safe_auxiliary_targets = torch.nan_to_num(
                auxiliary_targets,
                nan=0.0,
                posinf=1.0,
                neginf=0.0,
            ).clamp(0.0, 1.0)

            raw_auxiliary_loss = F.binary_cross_entropy_with_logits(
                logits[:, AUXILIARY_LOGIT_SLICE],
                safe_auxiliary_targets,
                reduction="none",
            )

            auxiliary_loss = (
                raw_auxiliary_loss * valid_auxiliary.float()
            ).sum() / valid_auxiliary.float().sum().clamp_min(1.0)

        per_identity_ranking_losses = []
        calibration_losses = []

        for identity_index in range(len(EVALUATION_IDENTITIES)):
            subgroup = identity_present[:, identity_index]
            background = ~subgroup

            subgroup_auc_loss = self._pairwise_auc_surrogate(
                toxicity_logits,
                positive_mask=subgroup & binary_targets,
                negative_mask=subgroup & ~binary_targets,
            )

            bpsn_auc_loss = self._pairwise_auc_surrogate(
                toxicity_logits,
                positive_mask=background & binary_targets,
                negative_mask=subgroup & ~binary_targets,
            )

            bnsp_auc_loss = self._pairwise_auc_surrogate(
                toxicity_logits,
                positive_mask=subgroup & binary_targets,
                negative_mask=background & ~binary_targets,
            )

            identity_terms = [
                loss
                for loss in (
                    subgroup_auc_loss,
                    bpsn_auc_loss,
                    bnsp_auc_loss,
                )
                if loss is not None
            ]

            if identity_terms:
                per_identity_ranking_losses.append(torch.stack(identity_terms).mean())

            subgroup_non_toxic = subgroup & ~binary_targets
            background_non_toxic = background & ~binary_targets

            if subgroup_non_toxic.any() and background_non_toxic.any():
                subgroup_mean = toxicity_logits[subgroup_non_toxic].mean()
                background_mean = toxicity_logits[background_non_toxic].mean()

                calibration_losses.append(
                    F.smooth_l1_loss(subgroup_mean, background_mean)
                )

        ranking_loss = toxicity_logits.sum() * 0.0

        if per_identity_ranking_losses:
            stacked_group_losses = torch.stack(per_identity_ranking_losses)
            temperature = self.worst_group_temperature

            ranking_loss = (
                torch.logsumexp(temperature * stacked_group_losses, dim=0)
                - torch.log(
                    torch.tensor(
                        float(stacked_group_losses.numel()),
                        device=logits.device,
                        dtype=logits.dtype,
                    )
                )
            ) / temperature

        calibration_loss = toxicity_logits.sum() * 0.0

        if calibration_losses:
            calibration_loss = torch.stack(calibration_losses).mean()

        total_loss = (
            primary_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.pairwise_weight * ranking_loss
            + self.calibration_weight * calibration_loss
        )

        components = {
            "total_loss": total_loss.detach(),
            "primary_soft_bce": primary_loss.detach(),
            "auxiliary_bce": auxiliary_loss.detach(),
            "bias_pairwise_loss": ranking_loss.detach(),
            "non_toxic_calibration_loss": calibration_loss.detach(),
        }

        return total_loss, components


criterion = OfficialBiasRankingLoss(
    pairwise_weight=0.40,
    auxiliary_weight=0.15,
    calibration_weight=0.05,
    worst_group_temperature=7.5,
    max_examples_per_class=96,
)

no_decay_terms = (
    "bias",
    "LayerNorm.weight",
    "layer_norm.weight",
    "norm.weight",
)

classifier_parameter_ids = {
    id(parameter) for parameter in model.classifier.parameters()
}

backbone_decay_parameters = []
backbone_no_decay_parameters = []
classifier_decay_parameters = []
classifier_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_classifier_parameter = id(parameter) in classifier_parameter_ids
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_classifier_parameter and has_no_decay:
        classifier_no_decay_parameters.append(parameter)
    elif is_classifier_parameter:
        classifier_decay_parameters.append(parameter)
    elif has_no_decay:
        backbone_no_decay_parameters.append(parameter)
    else:
        backbone_decay_parameters.append(parameter)

optimizer_parameter_groups = [
    {
        "params": backbone_decay_parameters,
        "lr": 1.5e-5,
        "weight_decay": 0.01,
    },
    {
        "params": backbone_no_decay_parameters,
        "lr": 1.5e-5,
        "weight_decay": 0.0,
    },
    {
        "params": classifier_decay_parameters,
        "lr": 7.5e-5,
        "weight_decay": 0.01,
    },
    {
        "params": classifier_no_decay_parameters,
        "lr": 7.5e-5,
        "weight_decay": 0.0,
    },
]

optimizer_parameter_groups = [
    group for group in optimizer_parameter_groups if len(group["params"]) > 0
]

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
amp_scaler = torch.cuda.amp.GradScaler(enabled=device.type == "cuda")

if device.type == "cuda":
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    # Encoder gradients are frozen, so larger batches improve throughput and ensure
    # that each bias-aware ranking batch contains more useful identity examples.
    if gpu_memory_gb >= 70:
        batch_size = 64
    elif gpu_memory_gb >= 40:
        batch_size = 32
    else:
        batch_size = 16
else:
    batch_size = 2

gradient_accumulation_steps = max(
    1,
    math.ceil(TARGET_EFFECTIVE_BATCH_SIZE / batch_size),
)

if device.type == "cuda" and gpu_memory_gb < 48:
    try:
        model.gradient_checkpointing_enable()
    except (AttributeError, ValueError):
        pass

if hasattr(model.config, "use_cache"):
    model.config.use_cache = False

best_checkpoint_path = WORKING_DIR / "best_modernbert_bias_auc.pt"
metrics_path = WORKING_DIR / "training_metrics.json"

identity_label_columns = [f"label_{column}" for column in EVALUATION_IDENTITIES]
auxiliary_label_columns = [f"label_{column}" for column in AUXILIARY_TOXICITY_COLUMNS]


class PreparedToxicityDataset(Dataset):
    def __init__(self, frames):
        usable_frames = [frame for frame in frames if len(frame) > 0]

        if not usable_frames:
            raise ValueError("Training dataset received no rows.")

        self.texts = np.concatenate(
            [
                frame["model_text"].fillna("").astype(str).to_numpy(copy=False)
                for frame in usable_frames
            ]
        )

        self.toxicity_targets = np.concatenate(
            [
                frame["label_target"].to_numpy(dtype=np.float32, copy=True)
                for frame in usable_frames
            ]
        )

        self.identity_targets = np.concatenate(
            [
                frame[identity_label_columns].to_numpy(dtype=np.float32, copy=True)
                for frame in usable_frames
            ],
            axis=0,
        )

        self.auxiliary_targets = np.concatenate(
            [
                frame[auxiliary_label_columns].to_numpy(dtype=np.float32, copy=True)
                for frame in usable_frames
            ],
            axis=0,
        )

        identity_present = (
            np.nan_to_num(
                self.identity_targets,
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )
            >= 0.5
        )

        self.binary_targets = (self.toxicity_targets >= 0.5).astype(np.int8)
        self.identity_any = identity_present.any(axis=1).astype(np.int8)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.toxicity_targets[index],
            self.identity_targets[index],
            self.auxiliary_targets[index],
        )


class TextInferenceDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=False)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index]


class FullCoverageBiasBatchSampler(Sampler):
    def __init__(self, binary_targets, identity_any, batch_size, seed):
        self.batch_size = int(batch_size)
        self.seed = int(seed)
        self.epoch = 0
        self.n_samples = len(binary_targets)

        self.strata = {
            "subgroup_negative": np.flatnonzero(
                (identity_any == 1) & (binary_targets == 0)
            ),
            "background_positive": np.flatnonzero(
                (identity_any == 0) & (binary_targets == 1)
            ),
            "subgroup_positive": np.flatnonzero(
                (identity_any == 1) & (binary_targets == 1)
            ),
            "background_negative": np.flatnonzero(
                (identity_any == 0) & (binary_targets == 0)
            ),
        }

        self.anchor_order = [
            "subgroup_negative",
            "background_positive",
            "subgroup_positive",
            "background_negative",
        ]

    def __len__(self):
        return math.ceil(self.n_samples / self.batch_size)

    def __iter__(self):
        rng = np.random.RandomState(self.seed + self.epoch)
        self.epoch += 1

        shuffled_strata = {
            name: rng.permutation(indices) for name, indices in self.strata.items()
        }

        stratum_positions = {name: 0 for name in shuffled_strata}

        global_order = rng.permutation(self.n_samples)
        global_position = 0
        already_assigned = np.zeros(self.n_samples, dtype=bool)

        for _ in range(len(self)):
            batch_indices = []

            for stratum_name in self.anchor_order:
                position = stratum_positions[stratum_name]
                candidates = shuffled_strata[stratum_name]

                if position < len(candidates) and len(batch_indices) < self.batch_size:
                    selected_index = int(candidates[position])
                    stratum_positions[stratum_name] += 1

                    if not already_assigned[selected_index]:
                        already_assigned[selected_index] = True
                        batch_indices.append(selected_index)

            while (
                len(batch_indices) < self.batch_size
                and global_position < self.n_samples
            ):
                selected_index = int(global_order[global_position])
                global_position += 1

                if not already_assigned[selected_index]:
                    already_assigned[selected_index] = True
                    batch_indices.append(selected_index)

            if batch_indices:
                yield batch_indices


def training_collate_fn(rows):
    texts = [row[0] for row in rows]

    encoded = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "toxicity_targets": torch.as_tensor(
            np.asarray([row[1] for row in rows], dtype=np.float32)
        ),
        "identity_targets": torch.as_tensor(
            np.asarray([row[2] for row in rows], dtype=np.float32)
        ),
        "auxiliary_targets": torch.as_tensor(
            np.asarray([row[3] for row in rows], dtype=np.float32)
        ),
    }


def inference_collate_fn(texts):
    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
    }


def official_bias_auc_score(targets, predictions, identity_matrix):
    targets = np.asarray(targets, dtype=np.int8).reshape(-1)
    predictions = np.asarray(predictions, dtype=np.float64).reshape(-1)
    identity_matrix = np.asarray(identity_matrix, dtype=np.float32)

    if len(targets) != len(predictions) or len(targets) != len(identity_matrix):
        raise ValueError("Targets, predictions, and identity labels must align.")

    if len(np.unique(targets)) != 2:
        raise RuntimeError("Overall validation labels contain only one class.")

    overall_auc = float(roc_auc_score(targets, predictions))

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_index, identity_name in enumerate(EVALUATION_IDENTITIES):
        subgroup = (
            np.nan_to_num(
                identity_matrix[:, identity_index],
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )
            >= 0.5
        )

        subgroup_mask = subgroup
        bpsn_mask = ((~subgroup) & (targets == 1)) | (subgroup & (targets == 0))
        bnsp_mask = ((~subgroup) & (targets == 0)) | (subgroup & (targets == 1))

        for metric_name, mask in (
            ("subgroup_auc", subgroup_mask),
            ("bpsn_auc", bpsn_mask),
            ("bnsp_auc", bnsp_mask),
        ):
            if mask.sum() == 0 or len(np.unique(targets[mask])) != 2:
                raise RuntimeError(
                    f"Validation split cannot calculate {metric_name} for "
                    f"identity '{identity_name}'."
                )

        subgroup_aucs.append(
            float(
                roc_auc_score(
                    targets[subgroup_mask],
                    predictions[subgroup_mask],
                )
            )
        )

        bpsn_aucs.append(
            float(
                roc_auc_score(
                    targets[bpsn_mask],
                    predictions[bpsn_mask],
                )
            )
        )

        bnsp_aucs.append(
            float(
                roc_auc_score(
                    targets[bnsp_mask],
                    predictions[bnsp_mask],
                )
            )
        )

    def power_mean(values, power=-5):
        values = np.asarray(values, dtype=np.float64)

        with np.errstate(divide="ignore", invalid="ignore"):
            return float(np.mean(np.power(values, power)) ** (1.0 / power))

    subgroup_power_mean = power_mean(subgroup_aucs)
    bpsn_power_mean = power_mean(bpsn_aucs)
    bnsp_power_mean = power_mean(bnsp_aucs)

    final_score = 0.25 * (
        overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean
    )

    return {
        "final_score": float(final_score),
        "overall_auc": overall_auc,
        "subgroup_power_mean": subgroup_power_mean,
        "bpsn_power_mean": bpsn_power_mean,
        "bnsp_power_mean": bnsp_power_mean,
        "subgroup_aucs": {
            identity: float(value)
            for identity, value in zip(EVALUATION_IDENTITIES, subgroup_aucs)
        },
        "bpsn_aucs": {
            identity: float(value)
            for identity, value in zip(EVALUATION_IDENTITIES, bpsn_aucs)
        },
        "bnsp_aucs": {
            identity: float(value)
            for identity, value in zip(EVALUATION_IDENTITIES, bnsp_aucs)
        },
    }


def model_predict(data_loader):
    model.eval()
    prediction_parts = []

    with torch.inference_mode():
        for batch in data_loader:
            model_inputs = {
                "input_ids": batch["input_ids"].to(
                    device,
                    non_blocking=True,
                ),
                "attention_mask": batch["attention_mask"].to(
                    device,
                    non_blocking=True,
                ),
            }

            autocast_context = (
                torch.autocast(device_type="cuda", dtype=torch.float16)
                if device.type == "cuda"
                else nullcontext()
            )

            with autocast_context:
                logits = model(**model_inputs).logits[:, TOXICITY_LOGIT_INDEX]

            prediction_parts.append(torch.sigmoid(logits).float().cpu().numpy())

    predictions = np.concatenate(prediction_parts, axis=0)

    if not np.isfinite(predictions).all():
        raise RuntimeError("Model inference produced non-finite predictions.")

    return np.clip(predictions, 0.0, 1.0)


training_dataset = PreparedToxicityDataset([train_prepared, counterfactual_prepared])
validation_dataset = TextInferenceDataset(valid_prepared)
test_dataset = TextInferenceDataset(test_prepared)

training_batch_sampler = FullCoverageBiasBatchSampler(
    binary_targets=training_dataset.binary_targets,
    identity_any=training_dataset.identity_any,
    batch_size=batch_size,
    seed=TRAINING_SEED,
)

loader_kwargs = {
    "num_workers": NUM_WORKERS,
    "pin_memory": device.type == "cuda",
    "persistent_workers": NUM_WORKERS > 0,
}

if NUM_WORKERS > 0:
    loader_kwargs["prefetch_factor"] = 2

train_loader = DataLoader(
    training_dataset,
    batch_sampler=training_batch_sampler,
    collate_fn=training_collate_fn,
    **loader_kwargs,
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=batch_size * 2,
    shuffle=False,
    collate_fn=inference_collate_fn,
    **loader_kwargs,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size * 2,
    shuffle=False,
    collate_fn=inference_collate_fn,
    **loader_kwargs,
)

updates_per_epoch = math.ceil(len(train_loader) / gradient_accumulation_steps)
total_update_steps = max(1, updates_per_epoch * MAX_EPOCHS)
warmup_steps = max(1, int(total_update_steps * WARMUP_FRACTION))

scheduler = get_cosine_schedule_with_warmup(
    optimizer=optimizer,
    num_warmup_steps=warmup_steps,
    num_training_steps=total_update_steps,
)

model.to(device)
optimizer.zero_grad(set_to_none=True)

validation_targets = (
    valid_prepared["label_target"].to_numpy(dtype=np.float32) >= 0.5
).astype(np.int8)

validation_identity_matrix = valid_prepared[identity_label_columns].to_numpy(
    dtype=np.float32, copy=True
)

best_score = -np.inf
best_epoch = -1
history = []

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    epoch_loss_sum = 0.0
    epoch_examples = 0

    for batch_index, batch in enumerate(train_loader):
        model_inputs = {
            "input_ids": batch["input_ids"].to(
                device,
                non_blocking=True,
            ),
            "attention_mask": batch["attention_mask"].to(
                device,
                non_blocking=True,
            ),
        }

        toxicity_targets = batch["toxicity_targets"].to(
            device,
            non_blocking=True,
        )
        identity_targets = batch["identity_targets"].to(
            device,
            non_blocking=True,
        )
        auxiliary_targets = batch["auxiliary_targets"].to(
            device,
            non_blocking=True,
        )

        autocast_context = (
            torch.autocast(device_type="cuda", dtype=torch.float16)
            if device.type == "cuda"
            else nullcontext()
        )

        with autocast_context:
            logits = model(**model_inputs).logits

            batch_loss, _ = criterion(
                logits=logits,
                toxicity_targets=toxicity_targets,
                identity_targets=identity_targets,
                auxiliary_targets=auxiliary_targets,
            )

            scaled_loss = batch_loss / gradient_accumulation_steps

        amp_scaler.scale(scaled_loss).backward()

        is_update_step = (batch_index + 1) % gradient_accumulation_steps == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if is_update_step:
            amp_scaler.unscale_(optimizer)
            clip_grad_norm_(model.parameters(), MAX_GRAD_NORM)
            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        current_batch_size = toxicity_targets.shape[0]
        epoch_loss_sum += float(batch_loss.detach().cpu()) * current_batch_size
        epoch_examples += current_batch_size

    validation_predictions = model_predict(validation_loader)

    validation_metrics = official_bias_auc_score(
        validation_targets,
        validation_predictions,
        validation_identity_matrix,
    )

    epoch_score = validation_metrics["final_score"]

    history.append(
        {
            "epoch": epoch,
            "train_loss": float(epoch_loss_sum / max(epoch_examples, 1)),
            **validation_metrics,
        }
    )

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch

        torch.save(
            {
                "epoch": epoch,
                "validation_score": float(epoch_score),
                "model_state_dict": model.state_dict(),
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "evaluation_identities": EVALUATION_IDENTITIES,
            },
            best_checkpoint_path,
        )

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} "
        f"loss={epoch_loss_sum / max(epoch_examples, 1):.5f} "
        f"official_score={epoch_score:.6f} "
        f"overall_auc={validation_metrics['overall_auc']:.6f} "
        f"bpsn={validation_metrics['bpsn_power_mean']:.6f} "
        f"bnsp={validation_metrics['bnsp_power_mean']:.6f}"
    )

with open(metrics_path, "w", encoding="utf-8") as metrics_file:
    json.dump(
        {
            "selection_metric": "official_bias_aware_auc",
            "best_epoch": int(best_epoch),
            "best_validation_score": float(best_score),
            "history": history,
        },
        metrics_file,
        indent=2,
    )

checkpoint = torch.load(best_checkpoint_path, map_location=device)
model.load_state_dict(checkpoint["model_state_dict"])

best_validation_predictions = model_predict(validation_loader)

final_validation_metrics = official_bias_auc_score(
    validation_targets,
    best_validation_predictions,
    validation_identity_matrix,
)

score = float(final_validation_metrics["final_score"])

test_predictions = model_predict(test_loader)

if len(test_predictions) != len(test_prepared):
    raise RuntimeError(
        f"Expected {len(test_prepared)} test predictions, "
        f"received {len(test_predictions)}."
    )

submission = pd.DataFrame(
    {
        ID_COLUMN: test_prepared[ID_COLUMN].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if not np.array_equal(
    submission[ID_COLUMN].to_numpy(),
    sample_submission[ID_COLUMN].to_numpy(),
):
    raise RuntimeError("Submission IDs are not aligned to sample_submission.csv.")

submission.to_csv(SUBMISSION_DIR / "submission_648651bcf0a74e56b849316c08228f5b.csv", index=False)

del train_loader
del validation_loader
del test_loader
del training_dataset
del validation_dataset
del test_dataset
gc.collect()

print(f"Final Validation Score: {score}")
