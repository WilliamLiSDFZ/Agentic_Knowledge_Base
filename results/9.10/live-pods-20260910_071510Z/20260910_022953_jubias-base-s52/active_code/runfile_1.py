import os
os.sched_setaffinity(0, {8, 9})
import os
import re
import html
import math
import random
import warnings
import unicodedata

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.cuda.amp import GradScaler, autocast
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import AutoModelForSequenceClassification, AutoTokenizer


# =============================================================================
# Configuration
# =============================================================================

SEED = 2025

INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"
CHECKPOINT_PATH = os.path.join(WORKING_DIR, "best_fair_deberta_checkpoint.pt")
SUBMISSION_PATH = os.path.join(SUBMISSION_DIR, "submission_977fa3cb9dd944bb99c440b9a6f89f70.csv")

TEXT_COLUMN = "comment_text"
ID_COLUMN = "id"
TARGET_COLUMN = "target"

VALIDATION_FOLDS = 5
VALIDATION_FOLD_INDEX = 0

MODEL_ID = "microsoft/deberta-v3-large"
MAX_SEQUENCE_LENGTH = 384

MAX_EPOCHS = 1
EARLY_STOPPING_PATIENCE = 1
NUM_WORKERS = 2

AUXILIARY_LOSS_WEIGHT = 0.25
IDENTITY_ADVERSARIAL_LOSS_WEIGHT = 0.05
GRADIENT_REVERSAL_STRENGTH = 0.10

ENCODER_LEARNING_RATE = 1.5e-5
HEAD_LEARNING_RATE = 8.0e-5
WEIGHT_DECAY = 0.01

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

AUXILIARY_TARGET_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True


# =============================================================================
# Data preprocessing and feature engineering
# =============================================================================

train_usecols = (
    [ID_COLUMN, TEXT_COLUMN, TARGET_COLUMN]
    + IDENTITY_COLUMNS
    + AUXILIARY_TARGET_COLUMNS
)
test_usecols = [ID_COLUMN, TEXT_COLUMN]

train_raw = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    usecols=train_usecols,
    low_memory=False,
)
test_raw = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    usecols=test_usecols,
    low_memory=False,
)
sample_submission = pd.read_csv(os.path.join(INPUT_DIR, "sample_submission.csv"))

if list(sample_submission.columns) != [ID_COLUMN, "prediction"]:
    raise ValueError(
        "sample_submission.csv must contain exactly ['id', 'prediction'] columns."
    )

if test_raw[ID_COLUMN].duplicated().any():
    raise ValueError("Test IDs must be unique.")

if set(sample_submission[ID_COLUMN]) != set(test_raw[ID_COLUMN]):
    raise ValueError("sample_submission IDs and test IDs do not match.")

test_raw = (
    test_raw.set_index(ID_COLUMN)
    .loc[sample_submission[ID_COLUMN].to_numpy()]
    .reset_index()
)

_whitespace_re = re.compile(r"\s+")
_url_re = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<]+")
_email_re = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
_control_re = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

_identity_term_re = re.compile(
    r"(?i)\b(?:"
    r"man|men|male|boy|boys|woman|women|female|girl|girls|"
    r"gay|gays|lesbian|lesbians|christian|christians|muslim|muslims|"
    r"jew|jews|jewish|black|blacks|white|whites|"
    r"mentally[\s-]ill|mental[\s-]illness|psychiatric[\s-]illness"
    r")\b"
)

_profanity_re = re.compile(
    r"(?i)\b(?:fuck|fucking|fucked|shit|shitty|bitch|bastard|asshole|"
    r"idiot|moron|stupid|retard|dumbass|racist|nazi|kill|murder|hate)\b"
)


def canonicalize_text(value):
    """Normalize text only for duplicate grouping and model-safe inputs."""
    if pd.isna(value):
        value = ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = _control_re.sub(" ", text)
    text = _url_re.sub(" <URL> ", text)
    text = _email_re.sub(" <EMAIL> ", text)
    text = _whitespace_re.sub(" ", text).strip()
    return text


def make_surface_features(frame):
    """Build inference-safe surface features using text only."""
    text = frame["clean_text"].fillna("")

    char_count = text.str.len().to_numpy(dtype=np.float32)
    alpha_count = text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    upper_count = text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    word_count = text.str.count(r"\S+").to_numpy(dtype=np.float32)

    unique_word_count = (
        text.str.lower()
        .str.findall(r"[a-z']+")
        .map(lambda tokens: len(set(tokens)))
        .to_numpy(dtype=np.float32)
    )

    feature_frame = pd.DataFrame(
        {
            "log_char_count": np.log1p(char_count),
            "log_word_count": np.log1p(word_count),
            "log_unique_word_count": np.log1p(unique_word_count),
            "uppercase_ratio": upper_count / np.maximum(alpha_count, 1.0),
            "exclamation_count": text.str.count("!").to_numpy(dtype=np.float32),
            "question_count": text.str.count(r"\?").to_numpy(dtype=np.float32),
            "ellipsis_count": text.str.count(r"\.\.\.").to_numpy(dtype=np.float32),
            "url_or_email_count": text.str.count(r"<URL>|<EMAIL>").to_numpy(
                dtype=np.float32
            ),
            "quote_count": text.str.count(r"""["']""").to_numpy(dtype=np.float32),
            "digit_count": text.str.count(r"\d").to_numpy(dtype=np.float32),
            "profanity_cue_count": text.map(
                lambda value: len(_profanity_re.findall(value))
            ).to_numpy(dtype=np.float32),
            "explicit_identity_term_count": text.map(
                lambda value: len(_identity_term_re.findall(value))
            ).to_numpy(dtype=np.float32),
        }
    )

    return feature_frame.astype(np.float32)


def build_model_frame(source_frame, surface_frame, include_labels):
    result = pd.DataFrame(
        {
            ID_COLUMN: source_frame[ID_COLUMN].to_numpy(),
            "model_text": source_frame["clean_text"].to_numpy(),
        }
    )

    result = pd.concat(
        [result.reset_index(drop=True), surface_frame.reset_index(drop=True)],
        axis=1,
    )

    if include_labels:
        result[TARGET_COLUMN] = (
            source_frame[TARGET_COLUMN].astype(np.float32).to_numpy()
        )
        result["target_binary"] = (
            source_frame[TARGET_COLUMN].ge(0.5).astype(np.uint8).to_numpy()
        )

        for column in AUXILIARY_TARGET_COLUMNS:
            result[f"aux_{column}"] = (
                source_frame[column].fillna(0.0).astype(np.float32).to_numpy()
            )

    return result


train_raw["clean_text"] = train_raw[TEXT_COLUMN].map(canonicalize_text)
test_raw["clean_text"] = test_raw[TEXT_COLUMN].map(canonicalize_text)

train_group_keys = pd.util.hash_pandas_object(
    train_raw["clean_text"],
    index=False,
).to_numpy(dtype=np.uint64)

identity_binary_all = train_raw[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).astype(np.uint16)
identity_mask = np.zeros(len(train_raw), dtype=np.uint16)

for bit_position, identity_name in enumerate(IDENTITY_COLUMNS):
    identity_mask |= (
        identity_binary_all[identity_name].to_numpy(dtype=np.uint16) << bit_position
    )

toxicity_binary_all = train_raw[TARGET_COLUMN].ge(0.5).to_numpy(dtype=np.uint16)
split_strata = toxicity_binary_all.astype(np.int32) * (2 ** len(IDENTITY_COLUMNS))
split_strata += identity_mask.astype(np.int32)

splitter = StratifiedGroupKFold(
    n_splits=VALIDATION_FOLDS,
    shuffle=True,
    random_state=SEED,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    fold_iterator = splitter.split(
        X=np.zeros(len(train_raw), dtype=np.uint8),
        y=split_strata,
        groups=train_group_keys,
    )

    for fold_index, (
        candidate_train_indices,
        candidate_validation_indices,
    ) in enumerate(fold_iterator):
        if fold_index == VALIDATION_FOLD_INDEX:
            train_indices = candidate_train_indices
            validation_indices = candidate_validation_indices
            break

train_indices = np.sort(train_indices)
validation_indices = np.sort(validation_indices)

train_partition = train_raw.iloc[train_indices].copy().reset_index(drop=True)
validation_partition = train_raw.iloc[validation_indices].copy().reset_index(drop=True)

del train_raw
del train_group_keys
del identity_binary_all
del identity_mask
del toxicity_binary_all
del split_strata

train_surface_features = make_surface_features(train_partition)
validation_surface_features = make_surface_features(validation_partition)
test_surface_features = make_surface_features(test_raw)

surface_feature_columns = train_surface_features.columns.tolist()

surface_scaler = StandardScaler()

train_surface_features.loc[:, surface_feature_columns] = surface_scaler.fit_transform(
    train_surface_features[surface_feature_columns]
).astype(np.float32)

validation_surface_features.loc[:, surface_feature_columns] = surface_scaler.transform(
    validation_surface_features[surface_feature_columns]
).astype(np.float32)

test_surface_features.loc[:, surface_feature_columns] = surface_scaler.transform(
    test_surface_features[surface_feature_columns]
).astype(np.float32)

train_original_features = build_model_frame(
    train_partition,
    train_surface_features,
    include_labels=True,
)

validation_features = build_model_frame(
    validation_partition,
    validation_surface_features,
    include_labels=True,
)

test_features = build_model_frame(
    test_raw,
    test_surface_features,
    include_labels=False,
)

COUNTERFACTUAL_REPLACEMENTS = {
    "male": {
        "men": "women",
        "man": "woman",
        "male": "female",
        "boys": "girls",
        "boy": "girl",
    },
    "female": {
        "women": "men",
        "woman": "man",
        "female": "male",
        "girls": "boys",
        "girl": "boy",
    },
    "homosexual_gay_or_lesbian": {
        "lesbians": "heterosexuals",
        "lesbian": "heterosexual",
        "gays": "straight people",
        "gay": "straight",
    },
    "christian": {
        "christians": "muslims",
        "christian": "muslim",
    },
    "jewish": {
        "jews": "christians",
        "jewish": "christian",
    },
    "muslim": {
        "muslims": "christians",
        "muslim": "christian",
    },
    "black": {
        "blacks": "whites",
        "black": "white",
    },
    "white": {
        "whites": "blacks",
        "white": "black",
    },
    "psychiatric_or_mental_illness": {
        "mentally ill": "physically disabled",
        "mental illness": "physical disability",
        "psychiatric illness": "physical disability",
    },
}


def preserve_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source.istitle():
        return replacement.title()
    return replacement


def create_counterfactual_text(text, active_identity_names):
    """Swap one explicitly present annotated identity while preserving toxicity intent."""
    for identity_name in active_identity_names:
        replacements = COUNTERFACTUAL_REPLACEMENTS.get(identity_name)

        if not replacements:
            continue

        replacement_pattern = re.compile(
            r"\b(?:"
            + "|".join(
                sorted(
                    (re.escape(term) for term in replacements),
                    key=len,
                    reverse=True,
                )
            )
            + r")\b",
            flags=re.IGNORECASE,
        )

        replaced = replacement_pattern.sub(
            lambda match: preserve_case(
                match.group(0),
                replacements[match.group(0).lower()],
            ),
            text,
        )

        if replaced != text:
            return replaced

    return None


train_identity_binary = train_partition[IDENTITY_COLUMNS].fillna(0.0).ge(0.5)

counterfactual_candidates = train_partition.loc[
    train_identity_binary.any(axis=1),
    [ID_COLUMN, "clean_text", TARGET_COLUMN] + AUXILIARY_TARGET_COLUMNS,
].copy()

candidate_identity_matrix = train_identity_binary.loc[counterfactual_candidates.index]
candidate_identity_rows = candidate_identity_matrix.to_numpy(dtype=bool)

counterfactual_texts = []

for original_text, active_row in zip(
    counterfactual_candidates["clean_text"].to_numpy(),
    candidate_identity_rows,
):
    active_names = [
        identity_name
        for identity_name, is_active in zip(IDENTITY_COLUMNS, active_row)
        if is_active
    ]
    counterfactual_texts.append(create_counterfactual_text(original_text, active_names))

counterfactual_candidates["model_text"] = counterfactual_texts
counterfactual_candidates = counterfactual_candidates.loc[
    counterfactual_candidates["model_text"].notna()
].copy()

train_original_features["sample_weight"] = np.float32(1.0)
train_original_features["is_counterfactual"] = np.uint8(0)

if len(counterfactual_candidates) > 0:
    counterfactual_surface_source = pd.DataFrame(
        {"clean_text": counterfactual_candidates["model_text"].to_numpy()}
    )

    counterfactual_surface_features = make_surface_features(
        counterfactual_surface_source
    )

    counterfactual_surface_features.loc[:, surface_feature_columns] = (
        surface_scaler.transform(
            counterfactual_surface_features[surface_feature_columns]
        ).astype(np.float32)
    )

    counterfactual_features = pd.DataFrame(
        {
            ID_COLUMN: counterfactual_candidates[ID_COLUMN].to_numpy(),
            "model_text": counterfactual_candidates["model_text"].to_numpy(),
            TARGET_COLUMN: counterfactual_candidates[TARGET_COLUMN]
            .astype(np.float32)
            .to_numpy(),
            "target_binary": counterfactual_candidates[TARGET_COLUMN]
            .ge(0.5)
            .astype(np.uint8)
            .to_numpy(),
        }
    )

    counterfactual_features = pd.concat(
        [
            counterfactual_features.reset_index(drop=True),
            counterfactual_surface_features.reset_index(drop=True),
        ],
        axis=1,
    )

    for column in AUXILIARY_TARGET_COLUMNS:
        counterfactual_features[f"aux_{column}"] = (
            counterfactual_candidates[column].fillna(0.0).astype(np.float32).to_numpy()
        )

    counterfactual_features["sample_weight"] = np.float32(0.35)
    counterfactual_features["is_counterfactual"] = np.uint8(1)

    train_features = pd.concat(
        [train_original_features, counterfactual_features],
        axis=0,
        ignore_index=True,
    )
else:
    train_features = train_original_features.copy()

validation_features["sample_weight"] = np.float32(1.0)
validation_features["is_counterfactual"] = np.uint8(0)

train_identity_targets = (
    train_partition[[ID_COLUMN] + IDENTITY_COLUMNS].copy().reset_index(drop=True)
)
train_identity_targets[IDENTITY_COLUMNS] = (
    train_identity_targets[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).astype(np.uint8)
)

validation_identity_targets = (
    validation_partition[[ID_COLUMN] + IDENTITY_COLUMNS].copy().reset_index(drop=True)
)
validation_identity_targets[IDENTITY_COLUMNS] = (
    validation_identity_targets[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).astype(np.uint8)
)

validation_identity_targets["identity_annotated"] = (
    validation_partition[IDENTITY_COLUMNS]
    .notna()
    .any(axis=1)
    .astype(np.uint8)
    .to_numpy()
)

submission_ids = sample_submission[ID_COLUMN].to_numpy()


# =============================================================================
# Fairness-aware DeBERTa model
# =============================================================================


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, strength):
        ctx.strength = float(strength)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return -ctx.strength * gradient_output, None


def gradient_reverse(inputs, strength):
    return GradientReversalFunction.apply(inputs, strength)


class FairDebertaToxicityModel(nn.Module):
    """DeBERTa encoder with toxicity, auxiliary, and adversarial identity heads."""

    def __init__(
        self,
        backbone,
        surface_feature_dim,
        auxiliary_target_dim,
        identity_target_dim,
        dropout_probability=0.20,
    ):
        super().__init__()

        self.backbone = backbone
        hidden_size = int(backbone.config.hidden_size)

        self.surface_encoder = nn.Sequential(
            nn.LayerNorm(surface_feature_dim),
            nn.Linear(surface_feature_dim, 96),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(96, 96),
            nn.GELU(),
        )

        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden_size + 96),
            nn.Linear(hidden_size + 96, 512),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(512, 256),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.toxicity_head = nn.Linear(256, 1)
        self.auxiliary_head = nn.Linear(256, auxiliary_target_dim)

        self.identity_adversary = nn.Sequential(
            nn.Linear(hidden_size, 384),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(384, identity_target_dim),
        )

    @staticmethod
    def _masked_mean_pool(last_hidden_state, attention_mask):
        token_weights = attention_mask.unsqueeze(-1).to(last_hidden_state.dtype)
        weighted_sum = (last_hidden_state * token_weights).sum(dim=1)
        normalizer = token_weights.sum(dim=1).clamp_min(1.0)
        return weighted_sum / normalizer

    def forward(
        self,
        input_ids,
        attention_mask,
        surface_features,
        adversarial_strength=GRADIENT_REVERSAL_STRENGTH,
    ):
        encoder_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        semantic_features = self._masked_mean_pool(
            encoder_outputs.last_hidden_state,
            attention_mask,
        )

        encoded_surface_features = self.surface_encoder(surface_features)

        fused_features = self.fusion(
            torch.cat(
                [semantic_features, encoded_surface_features],
                dim=-1,
            )
        )

        toxicity_logit = self.toxicity_head(fused_features).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(fused_features)

        reversed_semantic_features = gradient_reverse(
            semantic_features,
            adversarial_strength,
        )

        identity_logits = self.identity_adversary(reversed_semantic_features)

        return {
            "toxicity_logit": toxicity_logit,
            "auxiliary_logits": auxiliary_logits,
            "identity_logits": identity_logits,
        }

    @torch.no_grad()
    def toxicity_probability(self, input_ids, attention_mask, surface_features):
        outputs = self.forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            surface_features=surface_features,
            adversarial_strength=0.0,
        )
        return torch.sigmoid(outputs["toxicity_logit"])


class FairToxicityLoss(nn.Module):
    """Weighted toxicity, subtype, and adversarial identity objectives."""

    def __init__(
        self,
        auxiliary_loss_weight=AUXILIARY_LOSS_WEIGHT,
        identity_adversarial_loss_weight=IDENTITY_ADVERSARIAL_LOSS_WEIGHT,
    ):
        super().__init__()
        self.auxiliary_loss_weight = float(auxiliary_loss_weight)
        self.identity_adversarial_loss_weight = float(identity_adversarial_loss_weight)

    @staticmethod
    def _weighted_mean(values, weights):
        weights = weights.to(dtype=values.dtype)
        return (values * weights).sum() / weights.sum().clamp_min(1e-8)

    def forward(
        self,
        model_outputs,
        toxicity_targets,
        sample_weight=None,
        fairness_weight=None,
        auxiliary_targets=None,
        identity_targets=None,
        identity_label_mask=None,
    ):
        toxicity_targets = toxicity_targets.to(
            dtype=model_outputs["toxicity_logit"].dtype
        )

        main_losses = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logit"],
            toxicity_targets,
            reduction="none",
        )

        effective_weight = torch.ones_like(main_losses)

        if sample_weight is not None:
            effective_weight = effective_weight * sample_weight.to(
                device=effective_weight.device,
                dtype=effective_weight.dtype,
            )

        if fairness_weight is not None:
            effective_weight = effective_weight * fairness_weight.to(
                device=effective_weight.device,
                dtype=effective_weight.dtype,
            )

        main_loss = self._weighted_mean(main_losses, effective_weight)
        auxiliary_loss = main_loss.new_zeros(())
        identity_adversarial_loss = main_loss.new_zeros(())

        if auxiliary_targets is not None:
            auxiliary_targets = auxiliary_targets.to(
                device=model_outputs["auxiliary_logits"].device,
                dtype=model_outputs["auxiliary_logits"].dtype,
            )

            auxiliary_element_losses = F.binary_cross_entropy_with_logits(
                model_outputs["auxiliary_logits"],
                auxiliary_targets,
                reduction="none",
            )

            auxiliary_per_example = auxiliary_element_losses.mean(dim=-1)
            auxiliary_loss = self._weighted_mean(
                auxiliary_per_example,
                effective_weight,
            )

        if identity_targets is not None:
            identity_targets = identity_targets.to(
                device=model_outputs["identity_logits"].device,
                dtype=model_outputs["identity_logits"].dtype,
            )

            if identity_label_mask is None:
                identity_label_mask = torch.isfinite(identity_targets)
            else:
                identity_label_mask = identity_label_mask.to(
                    device=model_outputs["identity_logits"].device,
                    dtype=torch.bool,
                )

            valid_identity_targets = torch.nan_to_num(
                identity_targets,
                nan=0.0,
            )

            identity_element_losses = F.binary_cross_entropy_with_logits(
                model_outputs["identity_logits"],
                valid_identity_targets,
                reduction="none",
            )

            if identity_label_mask.any():
                identity_adversarial_loss = (
                    identity_element_losses
                    * identity_label_mask.to(identity_element_losses.dtype)
                ).sum() / identity_label_mask.sum().clamp_min(1)

        total_loss = (
            main_loss
            + self.auxiliary_loss_weight * auxiliary_loss
            + self.identity_adversarial_loss_weight * identity_adversarial_loss
        )

        return {
            "loss": total_loss,
            "main_loss": main_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "identity_adversarial_loss": identity_adversarial_loss.detach(),
        }


tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")

base_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)

model = FairDebertaToxicityModel(
    backbone=base_model.deberta,
    surface_feature_dim=len(surface_feature_columns),
    auxiliary_target_dim=len(AUXILIARY_TARGET_COLUMNS),
    identity_target_dim=len(IDENTITY_COLUMNS),
)

criterion = FairToxicityLoss()

no_decay_terms = (
    "bias",
    "LayerNorm.weight",
    "layer_norm.weight",
)

optimizer_parameter_groups = []

for parameter_scope, learning_rate in (
    ("backbone.", ENCODER_LEARNING_RATE),
    ("head.", HEAD_LEARNING_RATE),
):
    scoped_parameters = [
        (name, parameter)
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
        and (
            name.startswith("backbone.")
            if parameter_scope == "backbone."
            else not name.startswith("backbone.")
        )
    ]

    decayed_parameters = [
        parameter
        for name, parameter in scoped_parameters
        if not any(no_decay_term in name for no_decay_term in no_decay_terms)
    ]

    non_decayed_parameters = [
        parameter
        for name, parameter in scoped_parameters
        if any(no_decay_term in name for no_decay_term in no_decay_terms)
    ]

    if decayed_parameters:
        optimizer_parameter_groups.append(
            {
                "params": decayed_parameters,
                "lr": learning_rate,
                "weight_decay": WEIGHT_DECAY,
            }
        )

    if non_decayed_parameters:
        optimizer_parameter_groups.append(
            {
                "params": non_decayed_parameters,
                "lr": learning_rate,
                "weight_decay": 0.0,
            }
        )

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)


def build_warmup_cosine_scheduler(
    optimizer_instance,
    total_training_steps,
    warmup_ratio=0.06,
):
    if total_training_steps <= 0:
        raise ValueError("total_training_steps must be positive.")

    warmup_steps = max(1, int(total_training_steps * warmup_ratio))

    def learning_rate_multiplier(current_step):
        if current_step < warmup_steps:
            return float(current_step + 1) / float(warmup_steps)

        remaining_progress = (current_step - warmup_steps) / max(
            1,
            total_training_steps - warmup_steps,
        )

        return max(
            0.05,
            0.5 * (1.0 + math.cos(math.pi * remaining_progress)),
        )

    return LambdaLR(
        optimizer_instance,
        lr_lambda=learning_rate_multiplier,
    )


# =============================================================================
# Datasets, tokenization, sampling, and official metric
# =============================================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda = device.type == "cuda"

if use_cuda:
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    if gpu_memory_gb >= 70:
        train_batch_size = 24
    elif gpu_memory_gb >= 40:
        train_batch_size = 12
    elif gpu_memory_gb >= 20:
        train_batch_size = 6
    else:
        train_batch_size = 2
else:
    train_batch_size = 2

gradient_accumulation_steps = max(1, 32 // train_batch_size)

# Non-reentrant checkpointing supports multiple gradient paths from the fused toxicity
# and adversarial identity heads. The reentrant implementation can re-enter DeBERTa's
# checkpointed layers during backward and attempt to reuse already-freed activations.
if hasattr(model.backbone, "gradient_checkpointing_enable") and use_cuda:
    model.backbone.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )

model.to(device)

train_frame = train_features.reset_index(drop=True)
validation_frame = validation_features.reset_index(drop=True)
test_frame = test_features.reset_index(drop=True)

validation_identity_frame = validation_identity_targets.reset_index(drop=True)
train_identity_frame = train_identity_targets.reset_index(drop=True)

if not np.array_equal(
    validation_frame[ID_COLUMN].to_numpy(),
    validation_identity_frame[ID_COLUMN].to_numpy(),
):
    raise RuntimeError(
        "Validation identity labels are not aligned with validation features."
    )

original_training_rows = len(train_identity_frame)

if original_training_rows > len(train_frame):
    raise RuntimeError(
        "Training identity labels exceed the number of training examples."
    )

train_identity_values = np.zeros(
    (len(train_frame), len(IDENTITY_COLUMNS)),
    dtype=np.float32,
)

train_identity_mask = np.zeros(
    (len(train_frame), len(IDENTITY_COLUMNS)),
    dtype=bool,
)

train_identity_values[:original_training_rows] = train_identity_frame[
    IDENTITY_COLUMNS
].to_numpy(dtype=np.float32)

known_identity_labels = train_partition[IDENTITY_COLUMNS].notna().to_numpy(dtype=bool)

train_identity_mask[:original_training_rows] = known_identity_labels

train_targets = train_frame[TARGET_COLUMN].to_numpy(dtype=np.float32)
train_sample_weights = train_frame["sample_weight"].to_numpy(dtype=np.float32)

train_toxic_binary = train_frame["target_binary"].to_numpy(dtype=bool)
train_has_identity = train_identity_values.max(axis=1) >= 0.5

fairness_weights = np.ones(len(train_frame), dtype=np.float32)
fairness_weights += 2.0 * train_has_identity.astype(np.float32)
fairness_weights += 2.0 * (train_has_identity & ~train_toxic_binary).astype(np.float32)
fairness_weights += 1.0 * (~train_has_identity & train_toxic_binary).astype(np.float32)

counterfactual_mask = train_frame["is_counterfactual"].to_numpy(dtype=bool)
train_identity_mask[counterfactual_mask] = False
fairness_weights[counterfactual_mask] = 1.0

train_auxiliary_targets = train_frame[
    [f"aux_{column}" for column in AUXILIARY_TARGET_COLUMNS]
].to_numpy(dtype=np.float32)

validation_targets = validation_frame["target_binary"].to_numpy(dtype=np.uint8)

validation_identity_values = validation_identity_frame[IDENTITY_COLUMNS].to_numpy(
    dtype=np.float32
)


class ToxicityDataset(Dataset):
    def __init__(
        self,
        frame,
        surface_columns,
        targets=None,
        sample_weights=None,
        fairness_weights=None,
        auxiliary_targets=None,
        identity_targets=None,
        identity_masks=None,
    ):
        self.texts = frame["model_text"].fillna("").astype(str).tolist()
        self.surface_features = frame[surface_columns].to_numpy(dtype=np.float32)
        self.targets = targets
        self.sample_weights = sample_weights
        self.fairness_weights = fairness_weights
        self.auxiliary_targets = auxiliary_targets
        self.identity_targets = identity_targets
        self.identity_masks = identity_masks

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {
            "row_index": index,
            "text": self.texts[index],
            "surface_features": self.surface_features[index],
        }

        if self.targets is not None:
            item["target"] = self.targets[index]
            item["sample_weight"] = self.sample_weights[index]
            item["fairness_weight"] = self.fairness_weights[index]
            item["auxiliary_targets"] = self.auxiliary_targets[index]
            item["identity_targets"] = self.identity_targets[index]
            item["identity_mask"] = self.identity_masks[index]

        return item


class TokenizingCollator:
    def __init__(self, tokenizer_instance, max_length):
        self.tokenizer_instance = tokenizer_instance
        self.max_length = int(max_length)

    def __call__(self, examples):
        texts = [example["text"] for example in examples]

        encoded = self.tokenizer_instance(
            texts,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
            return_token_type_ids=False,
        )

        batch = {
            "row_index": torch.tensor(
                [example["row_index"] for example in examples],
                dtype=torch.long,
            ),
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "surface_features": torch.from_numpy(
                np.stack([example["surface_features"] for example in examples])
            ).float(),
        }

        if "target" in examples[0]:
            batch["target"] = torch.tensor(
                [example["target"] for example in examples],
                dtype=torch.float32,
            )

            batch["sample_weight"] = torch.tensor(
                [example["sample_weight"] for example in examples],
                dtype=torch.float32,
            )

            batch["fairness_weight"] = torch.tensor(
                [example["fairness_weight"] for example in examples],
                dtype=torch.float32,
            )

            batch["auxiliary_targets"] = torch.from_numpy(
                np.stack([example["auxiliary_targets"] for example in examples])
            ).float()

            batch["identity_targets"] = torch.from_numpy(
                np.stack([example["identity_targets"] for example in examples])
            ).float()

            batch["identity_mask"] = torch.from_numpy(
                np.stack([example["identity_mask"] for example in examples])
            ).bool()

        return batch


class LengthBucketBatchSampler(Sampler):
    """Length-homogeneous batches reduce padding while retaining every sample."""

    def __init__(self, texts, batch_size, seed, drop_last=False):
        self.lengths = np.asarray(
            [
                max(
                    1,
                    min(
                        MAX_SEQUENCE_LENGTH,
                        len(text.split()) + 2,
                    ),
                )
                for text in texts
            ],
            dtype=np.int32,
        )

        self.batch_size = int(batch_size)
        self.seed = int(seed)
        self.epoch = 0
        self.drop_last = bool(drop_last)

    def set_epoch(self, epoch):
        self.epoch = int(epoch)

    def __iter__(self):
        rng = np.random.default_rng(self.seed + self.epoch)
        ordered_indices = np.argsort(self.lengths, kind="stable")

        batches = [
            ordered_indices[start : start + self.batch_size].tolist()
            for start in range(
                0,
                len(ordered_indices),
                self.batch_size,
            )
        ]

        if self.drop_last and batches and len(batches[-1]) < self.batch_size:
            batches.pop()

        for batch in batches:
            rng.shuffle(batch)

        rng.shuffle(batches)

        for batch in batches:
            yield batch

    def __len__(self):
        if self.drop_last:
            return len(self.lengths) // self.batch_size

        return int(math.ceil(len(self.lengths) / self.batch_size))


def make_inference_loader(dataset, batch_size):
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=use_cuda,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=TokenizingCollator(
            tokenizer,
            MAX_SEQUENCE_LENGTH,
        ),
    )


def move_batch_to_device(batch):
    return {
        key: (
            value.to(device, non_blocking=True)
            if torch.is_tensor(value) and key != "row_index"
            else value
        )
        for key, value in batch.items()
    }


@torch.no_grad()
def predict_dataset(dataset, batch_size):
    model.eval()

    loader = make_inference_loader(
        dataset,
        batch_size,
    )

    predictions = np.empty(
        len(dataset),
        dtype=np.float32,
    )

    for batch in loader:
        row_indices = batch["row_index"].numpy()
        batch = move_batch_to_device(batch)

        with autocast(enabled=use_cuda):
            probabilities = model.toxicity_probability(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                surface_features=batch["surface_features"],
            )

        predictions[row_indices] = probabilities.float().cpu().numpy()

    if not np.isfinite(predictions).all():
        raise RuntimeError("Non-finite predictions encountered during inference.")

    return predictions


def generalized_mean(values, power=-5.0):
    values = np.asarray(values, dtype=np.float64)

    if np.any(values < 0.0):
        raise ValueError("AUC values must be non-negative.")

    if np.any(values == 0.0):
        return 0.0

    return float(np.mean(values**power) ** (1.0 / power))


def official_bias_metric(binary_targets, predictions, identity_matrix):
    """
    Official competition metric:
    0.25 * overall AUC +
    0.25 * power_mean(subgroup AUCs, p=-5) +
    0.25 * power_mean(BPSN AUCs, p=-5) +
    0.25 * power_mean(BNSP AUCs, p=-5).
    """
    binary_targets = np.asarray(binary_targets, dtype=bool)
    predictions = np.asarray(predictions, dtype=np.float64)
    identity_matrix = np.asarray(identity_matrix, dtype=np.float32) >= 0.5

    overall_auc = roc_auc_score(binary_targets, predictions)

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_index in range(identity_matrix.shape[1]):
        subgroup = identity_matrix[:, identity_index]

        subgroup_examples = subgroup

        bpsn_examples = (subgroup & ~binary_targets) | (~subgroup & binary_targets)

        bnsp_examples = (subgroup & binary_targets) | (~subgroup & ~binary_targets)

        subgroup_aucs.append(
            roc_auc_score(
                binary_targets[subgroup_examples],
                predictions[subgroup_examples],
            )
        )

        bpsn_aucs.append(
            roc_auc_score(
                binary_targets[bpsn_examples],
                predictions[bpsn_examples],
            )
        )

        bnsp_aucs.append(
            roc_auc_score(
                binary_targets[bnsp_examples],
                predictions[bnsp_examples],
            )
        )

    subgroup_mean = generalized_mean(
        subgroup_aucs,
        power=-5.0,
    )

    bpsn_mean = generalized_mean(
        bpsn_aucs,
        power=-5.0,
    )

    bnsp_mean = generalized_mean(
        bnsp_aucs,
        power=-5.0,
    )

    final_score = 0.25 * (overall_auc + subgroup_mean + bpsn_mean + bnsp_mean)

    return float(final_score), {
        "overall_auc": float(overall_auc),
        "subgroup_mean": float(subgroup_mean),
        "bpsn_mean": float(bpsn_mean),
        "bnsp_mean": float(bnsp_mean),
    }


# =============================================================================
# Training, checkpoint selection, validation, and submission creation
# =============================================================================

train_dataset = ToxicityDataset(
    frame=train_frame,
    surface_columns=surface_feature_columns,
    targets=train_targets,
    sample_weights=train_sample_weights,
    fairness_weights=fairness_weights,
    auxiliary_targets=train_auxiliary_targets,
    identity_targets=train_identity_values,
    identity_masks=train_identity_mask,
)

validation_dataset = ToxicityDataset(
    frame=validation_frame,
    surface_columns=surface_feature_columns,
)

test_dataset = ToxicityDataset(
    frame=test_frame,
    surface_columns=surface_feature_columns,
)

train_batch_sampler = LengthBucketBatchSampler(
    texts=train_dataset.texts,
    batch_size=train_batch_size,
    seed=SEED,
    drop_last=False,
)

train_loader = DataLoader(
    train_dataset,
    batch_sampler=train_batch_sampler,
    num_workers=NUM_WORKERS,
    pin_memory=use_cuda,
    persistent_workers=False,
    prefetch_factor=2,
    collate_fn=TokenizingCollator(
        tokenizer,
        MAX_SEQUENCE_LENGTH,
    ),
)

total_optimizer_steps = int(
    math.ceil((len(train_loader) * MAX_EPOCHS) / gradient_accumulation_steps)
)

scheduler = build_warmup_cosine_scheduler(
    optimizer,
    total_training_steps=max(1, total_optimizer_steps),
)

scaler = GradScaler(enabled=use_cuda)

best_score = -np.inf
best_epoch = -1
epochs_without_improvement = 0

for epoch in range(MAX_EPOCHS):
    train_batch_sampler.set_epoch(epoch)
    model.train()
    optimizer.zero_grad(set_to_none=True)

    cumulative_loss = 0.0
    processed_batches = 0
    total_batches = len(train_loader)

    final_group_size = total_batches % gradient_accumulation_steps

    if final_group_size == 0:
        final_group_size = gradient_accumulation_steps

    for batch_number, batch in enumerate(train_loader, start=1):
        batch = move_batch_to_device(batch)

        is_final_partial_group = (
            batch_number > total_batches - final_group_size
            and total_batches % gradient_accumulation_steps != 0
        )

        current_group_size = (
            final_group_size if is_final_partial_group else gradient_accumulation_steps
        )

        with autocast(enabled=use_cuda):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                surface_features=batch["surface_features"],
            )

            loss_parts = criterion(
                model_outputs=outputs,
                toxicity_targets=batch["target"],
                sample_weight=batch["sample_weight"],
                fairness_weight=batch["fairness_weight"],
                auxiliary_targets=batch["auxiliary_targets"],
                identity_targets=batch["identity_targets"],
                identity_label_mask=batch["identity_mask"],
            )

            unscaled_loss = loss_parts["loss"]
            loss = unscaled_loss / current_group_size

        if not torch.isfinite(loss):
            raise RuntimeError("Encountered non-finite training loss.")

        scaler.scale(loss).backward()

        cumulative_loss += float(unscaled_loss.detach().cpu())

        processed_batches += 1

        should_update = (
            batch_number % gradient_accumulation_steps == 0
            or batch_number == total_batches
        )

        if should_update:
            scaler.unscale_(optimizer)

            clip_grad_norm_(
                model.parameters(),
                max_norm=1.0,
            )

            scaler.step(optimizer)
            scaler.update()

            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

    validation_predictions = predict_dataset(
        validation_dataset,
        batch_size=train_batch_size,
    )

    epoch_score, epoch_components = official_bias_metric(
        validation_targets,
        validation_predictions,
        validation_identity_values,
    )

    mean_training_loss = cumulative_loss / max(
        1,
        processed_batches,
    )

    print(
        f"Epoch {epoch + 1}/{MAX_EPOCHS} "
        f"loss={mean_training_loss:.6f} "
        f"official_score={epoch_score:.6f} "
        f"overall_auc={epoch_components['overall_auc']:.6f} "
        f"subgroup={epoch_components['subgroup_mean']:.6f} "
        f"bpsn={epoch_components['bpsn_mean']:.6f} "
        f"bnsp={epoch_components['bnsp_mean']:.6f}"
    )

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_score": epoch_score,
                "model_state_dict": model.state_dict(),
            },
            CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

        if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
            break

if best_epoch < 0 or not os.path.exists(CHECKPOINT_PATH):
    raise RuntimeError("No valid checkpoint was saved during training.")

checkpoint = torch.load(
    CHECKPOINT_PATH,
    map_location=device,
)

model.load_state_dict(checkpoint["model_state_dict"])
model.to(device)
model.eval()

final_validation_predictions = predict_dataset(
    validation_dataset,
    batch_size=train_batch_size,
)

score, final_components = official_bias_metric(
    validation_targets,
    final_validation_predictions,
    validation_identity_values,
)

test_predictions = predict_dataset(
    test_dataset,
    batch_size=train_batch_size,
)

if len(test_predictions) != len(submission_ids):
    raise RuntimeError("Test prediction count does not match submission ID count.")

if not np.array_equal(
    test_frame[ID_COLUMN].to_numpy(),
    submission_ids,
):
    raise RuntimeError("Test feature order does not match sample submission order.")

submission = pd.DataFrame(
    {
        ID_COLUMN: submission_ids,
        "prediction": np.clip(
            test_predictions,
            0.0,
            1.0,
        ),
    }
)

submission.to_csv(
    SUBMISSION_PATH,
    index=False,
)

print(f"Final Validation Score: {score}")
