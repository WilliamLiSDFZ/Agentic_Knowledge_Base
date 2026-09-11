import os
import re
import html
import json
import math
import pickle
import random

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader, Sampler, Subset
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


# Runtime owns the immutable split, official bias-aware metric, checkpoint selection,
# and final submission export.
session = CandidateSession.from_env()

INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"
os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

SEED = 1729
TRAIN_BATCH_SIZE = 16
INFERENCE_BATCH_SIZE = 32
INFERENCE_MAX_LENGTH = 256
NUM_WORKERS = 2
MAX_EPOCHS = 3

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

raw_train_df = pd.read_csv(os.path.join(INPUT_DIR, "train.csv"))
raw_test_df = pd.read_csv(os.path.join(INPUT_DIR, "test.csv"))

# Split before fitting any data-dependent preprocessing transformation.
train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

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

TOXICITY_AUXILIARY_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

IDENTITY_LEXICON_PATTERN = (
    r"\b(?:"
    r"male|men|man|boys?|father|fathers|husband|husbands|gentleman|gentlemen|"
    r"female|women|woman|girls?|mother|mothers|daughter|daughters|wife|wives|"
    r"transgender|transgendered|transsexual|cisgender|nonbinary|non-binary|"
    r"heterosexual|straight|gay|gays|lesbian|lesbians|homosexual|homosexuality|"
    r"bisexual|bisexuality|queer|lgbt|lgbtq|"
    r"christian|christians|christianity|jew|jews|jewish|judaism|"
    r"muslim|muslims|islam|islamic|hindu|hindus|hinduism|buddhist|buddhists|"
    r"atheist|atheists|atheism|religion|religious|"
    r"black|blacks|white|whites|asian|asians|latino|latina|latinos|latinas|"
    r"disabled|disability|autistic|autism|mental[\s-]?illness|"
    r"schizophrenic|schizophrenia|bipolar|depression|depressed"
    r")\b"
)

URL_PATTERN = r"(?:https?://|www\.)\S+"
EMAIL_PATTERN = r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b"
HTML_TAG_PATTERN = r"<[^>\n]{1,160}>"
CONTROL_CHAR_PATTERN = r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]"
REPEATED_PUNCT_PATTERN = r"([!?,.])\1{3,}"
REPEATED_CHAR_PATTERN = r"([A-Za-z])\1{4,}"


def retain_relevant_columns(frame):
    preferred = (
        [
            "id",
            "comment_text",
            "target",
            "toxicity_annotator_count",
            "identity_annotator_count",
        ]
        + TOXICITY_AUXILIARY_COLUMNS
        + IDENTITY_COLUMNS
    )
    columns = [column for column in preferred if column in frame.columns]
    return frame.loc[:, columns].copy()


def clean_comment_text(values):
    text = values.fillna("").astype(str).str.normalize("NFKC")
    text = text.map(html.unescape)
    text = text.str.replace(CONTROL_CHAR_PATTERN, " ", regex=True)
    text = text.str.replace(HTML_TAG_PATTERN, " ", regex=True)
    text = text.str.replace(URL_PATTERN, " urltoken ", regex=True)
    text = text.str.replace(EMAIL_PATTERN, " emailtoken ", regex=True)
    text = text.str.replace(r"[\r\n\t]+", " ", regex=True)
    text = text.str.replace(REPEATED_PUNCT_PATTERN, r"\1\1\1", regex=True)
    text = text.str.replace(REPEATED_CHAR_PATTERN, r"\1\1\1\1", regex=True)
    return text.str.replace(r"\s+", " ", regex=True).str.strip()


def add_text_features(frame):
    output = frame.copy()
    cleaned = clean_comment_text(output["comment_text"])
    lower = cleaned.str.lower()

    char_count = cleaned.str.len().astype(np.float32)
    word_count = cleaned.str.count(r"\S+").astype(np.float32)
    alphabetic_count = cleaned.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = cleaned.str.count(r"[A-Z]").astype(np.float32)

    output["comment_text_model"] = cleaned
    output["text_log_char_count"] = np.log1p(char_count).astype(np.float32)
    output["text_log_word_count"] = np.log1p(word_count).astype(np.float32)
    output["text_caps_ratio"] = (
        uppercase_count / np.maximum(alphabetic_count, 1.0)
    ).astype(np.float32)
    output["text_exclamation_count"] = np.minimum(
        cleaned.str.count("!").astype(np.float32), 20.0
    )
    output["text_question_count"] = np.minimum(
        cleaned.str.count(r"\?").astype(np.float32), 20.0
    )
    output["text_uppercase_token_count"] = np.minimum(
        cleaned.str.count(r"\b[A-Z]{2,}\b").astype(np.float32), 20.0
    )
    output["text_digit_count"] = np.minimum(
        cleaned.str.count(r"\d").astype(np.float32), 30.0
    )
    output["text_url_count"] = np.minimum(
        lower.str.count(r"\burltoken\b").astype(np.float32), 10.0
    )
    output["text_identity_lexicon_count"] = np.minimum(
        lower.str.count(IDENTITY_LEXICON_PATTERN).astype(np.float32), 10.0
    )
    output["text_has_identity_lexicon"] = (
        output["text_identity_lexicon_count"] > 0
    ).astype(np.float32)
    output["text_is_empty"] = (char_count == 0).astype(np.float32)
    return output


train_df = retain_relevant_columns(train_df)
valid_df = retain_relevant_columns(valid_df)
test_df = retain_relevant_columns(test_df)

train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

nonempty_train_text = train_df.loc[
    train_df["comment_text_model"].str.len() > 0, "comment_text_model"
]
train_text_frequency = nonempty_train_text.value_counts(dropna=False)


def add_train_fitted_frequency(frame):
    output = frame.copy()
    frequency = output["comment_text_model"].map(train_text_frequency).fillna(0)
    output["text_train_log_frequency"] = np.log1p(frequency.astype(np.float32)).astype(
        np.float32
    )
    output["text_seen_in_training"] = (frequency > 0).astype(np.float32)
    return output


train_df = add_train_fitted_frequency(train_df)
valid_df = add_train_fitted_frequency(valid_df)
test_df = add_train_fitted_frequency(test_df)

NUMERIC_TEXT_FEATURE_COLUMNS = [
    "text_log_char_count",
    "text_log_word_count",
    "text_caps_ratio",
    "text_exclamation_count",
    "text_question_count",
    "text_uppercase_token_count",
    "text_digit_count",
    "text_url_count",
    "text_identity_lexicon_count",
    "text_has_identity_lexicon",
    "text_is_empty",
    "text_train_log_frequency",
    "text_seen_in_training",
]

feature_scaler = StandardScaler()
feature_scaler.fit(train_df[NUMERIC_TEXT_FEATURE_COLUMNS].astype(np.float32))
SCALED_TEXT_FEATURE_COLUMNS = [f"{column}_z" for column in NUMERIC_TEXT_FEATURE_COLUMNS]


def add_scaled_features(frame):
    output = frame.copy()
    scaled = feature_scaler.transform(
        output[NUMERIC_TEXT_FEATURE_COLUMNS].astype(np.float32)
    ).astype(np.float32)
    output.loc[:, SCALED_TEXT_FEATURE_COLUMNS] = scaled
    return output


train_df = add_scaled_features(train_df)
valid_df = add_scaled_features(valid_df)
test_df = add_scaled_features(test_df)

model_text_column = "comment_text_model"
model_numeric_feature_columns = SCALED_TEXT_FEATURE_COLUMNS

preprocessing_artifacts = {
    "model_text_column": model_text_column,
    "numeric_feature_columns": model_numeric_feature_columns,
    "raw_numeric_feature_columns": NUMERIC_TEXT_FEATURE_COLUMNS,
    "identity_columns": [
        column for column in IDENTITY_COLUMNS if column in train_df.columns
    ],
    "official_identity_columns": [
        column for column in OFFICIAL_IDENTITY_COLUMNS if column in valid_df.columns
    ],
    "identity_lexicon_pattern": IDENTITY_LEXICON_PATTERN,
    "feature_scaler": feature_scaler,
}


# Required pretrained checkpoint setup.
model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id)

OFFICIAL_IDENTITY_COLUMNS_MODEL = OFFICIAL_IDENTITY_COLUMNS
TOXICITY_SUBTYPE_COLUMNS_MODEL = TOXICITY_AUXILIARY_COLUMNS


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = coefficient
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradients):
        return -ctx.coefficient * gradients, None


class GradientReversal(nn.Module):
    def __init__(self, coefficient=0.08):
        super().__init__()
        self.coefficient = float(coefficient)

    def forward(self, inputs):
        return GradientReversalFunction.apply(inputs, self.coefficient)


class BiasAwareModernBert(nn.Module):
    def __init__(
        self,
        encoder,
        numeric_feature_dim,
        subtype_count=6,
        identity_count=9,
        dropout=0.15,
        adversarial_coefficient=0.08,
    ):
        super().__init__()
        self.encoder = encoder
        self.hidden_size = int(encoder.config.hidden_size)
        self.numeric_feature_dim = int(numeric_feature_dim)

        if self.numeric_feature_dim > 0:
            numeric_hidden = min(128, max(32, self.hidden_size // 8))
            self.numeric_adapter = nn.Sequential(
                nn.Linear(self.numeric_feature_dim, numeric_hidden),
                nn.LayerNorm(numeric_hidden),
                nn.GELU(),
                nn.Dropout(dropout),
            )
            fusion_dim = self.hidden_size + numeric_hidden
        else:
            self.numeric_adapter = None
            fusion_dim = self.hidden_size

        self.fusion = nn.Sequential(
            nn.LayerNorm(fusion_dim),
            nn.Linear(fusion_dim, self.hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.toxicity_head = nn.Linear(self.hidden_size, 1)
        self.subtype_head = nn.Linear(self.hidden_size, subtype_count)

        self.identity_reversal = GradientReversal(adversarial_coefficient)
        self.identity_head = nn.Sequential(
            nn.Linear(self.hidden_size, self.hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(self.hidden_size // 2, identity_count),
        )

        nn.init.normal_(self.toxicity_head.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.toxicity_head.bias)
        nn.init.normal_(self.subtype_head.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.subtype_head.bias)

    def forward(self, input_ids, attention_mask, numeric_features=None):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        token_embeddings = encoder_outputs.last_hidden_state
        token_mask = attention_mask.unsqueeze(-1).to(token_embeddings.dtype)

        pooled_embedding = (token_embeddings * token_mask).sum(dim=1)
        pooled_embedding = pooled_embedding / token_mask.sum(dim=1).clamp_min(1.0)

        if self.numeric_adapter is not None:
            if numeric_features is None:
                numeric_features = pooled_embedding.new_zeros(
                    (pooled_embedding.shape[0], self.numeric_feature_dim)
                )
            numeric_embedding = self.numeric_adapter(
                numeric_features.to(dtype=pooled_embedding.dtype)
            )
            fused_embedding = torch.cat([pooled_embedding, numeric_embedding], dim=-1)
        else:
            fused_embedding = pooled_embedding

        shared_embedding = self.fusion(fused_embedding)
        return {
            "toxicity_logit": self.toxicity_head(shared_embedding).squeeze(-1),
            "subtype_logits": self.subtype_head(shared_embedding),
            "identity_logits": self.identity_head(
                self.identity_reversal(shared_embedding)
            ),
        }


class OfficialBiasAwareLoss(nn.Module):
    def __init__(
        self,
        toxicity_weight=1.0,
        subtype_weight=0.18,
        adversarial_identity_weight=0.045,
        pairwise_bias_weight=0.30,
        rank_temperature=0.75,
        robust_temperature=0.20,
        max_pairs_per_slice=96,
    ):
        super().__init__()
        self.toxicity_weight = float(toxicity_weight)
        self.subtype_weight = float(subtype_weight)
        self.adversarial_identity_weight = float(adversarial_identity_weight)
        self.pairwise_bias_weight = float(pairwise_bias_weight)
        self.rank_temperature = float(rank_temperature)
        self.robust_temperature = float(robust_temperature)
        self.max_pairs_per_slice = int(max_pairs_per_slice)

    @staticmethod
    def _finite_mask(values):
        return torch.isfinite(values)

    def _pairwise_rank_loss(self, positive_scores, negative_scores):
        if positive_scores.numel() == 0 or negative_scores.numel() == 0:
            return None

        pair_count = min(
            self.max_pairs_per_slice,
            positive_scores.numel(),
            negative_scores.numel(),
        )
        positive_indices = torch.randint(
            positive_scores.numel(),
            (pair_count,),
            device=positive_scores.device,
        )
        negative_indices = torch.randint(
            negative_scores.numel(),
            (pair_count,),
            device=negative_scores.device,
        )

        margin = positive_scores[positive_indices] - negative_scores[negative_indices]
        return F.softplus(-margin / self.rank_temperature).mean()

    def _robust_group_aggregate(self, group_losses):
        if not group_losses:
            return None

        losses = torch.stack(group_losses)
        temperature = max(self.robust_temperature, 1e-4)
        return temperature * torch.logsumexp(losses / temperature, dim=0) - (
            temperature * math.log(float(losses.numel()))
        )

    def _bias_pairwise_loss(self, toxicity_logits, toxicity_targets, identity_targets):
        if identity_targets is None or identity_targets.numel() == 0:
            return toxicity_logits.new_zeros(())

        binary_target = toxicity_targets.ge(0.5)
        clean_identity = torch.nan_to_num(
            identity_targets,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )

        metric_losses = [[], [], []]
        usable_count = min(
            clean_identity.shape[1],
            len(OFFICIAL_IDENTITY_COLUMNS_MODEL),
        )

        for identity_index in range(usable_count):
            subgroup = clean_identity[:, identity_index].ge(0.5)
            background = ~subgroup

            subgroup_loss = self._pairwise_rank_loss(
                toxicity_logits[subgroup & binary_target],
                toxicity_logits[subgroup & ~binary_target],
            )
            bpsn_loss = self._pairwise_rank_loss(
                toxicity_logits[background & binary_target],
                toxicity_logits[subgroup & ~binary_target],
            )
            bnsp_loss = self._pairwise_rank_loss(
                toxicity_logits[subgroup & binary_target],
                toxicity_logits[background & ~binary_target],
            )

            if subgroup_loss is not None:
                metric_losses[0].append(subgroup_loss)
            if bpsn_loss is not None:
                metric_losses[1].append(bpsn_loss)
            if bnsp_loss is not None:
                metric_losses[2].append(bnsp_loss)

        robust_losses = [
            self._robust_group_aggregate(losses) for losses in metric_losses if losses
        ]
        if not robust_losses:
            return toxicity_logits.new_zeros(())
        return torch.stack(robust_losses).mean()

    def forward(
        self,
        outputs,
        toxicity_targets,
        subtype_targets=None,
        identity_targets=None,
        identity_observed_mask=None,
    ):
        toxicity_logits = outputs["toxicity_logit"]
        toxicity_targets = toxicity_targets.to(toxicity_logits.dtype).view_as(
            toxicity_logits
        )

        primary_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets.clamp(0.0, 1.0),
        )
        total_loss = self.toxicity_weight * primary_loss

        if subtype_targets is not None and subtype_targets.numel() > 0:
            subtype_logits = outputs["subtype_logits"]
            subtype_targets = subtype_targets.to(subtype_logits.dtype)
            valid_subtype = self._finite_mask(subtype_targets)

            if valid_subtype.any():
                subtype_loss_all = F.binary_cross_entropy_with_logits(
                    subtype_logits,
                    torch.nan_to_num(subtype_targets, nan=0.0).clamp(0.0, 1.0),
                    reduction="none",
                )
                subtype_loss = (
                    subtype_loss_all * valid_subtype.to(subtype_loss_all.dtype)
                ).sum() / valid_subtype.sum().clamp_min(1)
                total_loss = total_loss + self.subtype_weight * subtype_loss

        if identity_targets is not None and identity_targets.numel() > 0:
            identity_logits = outputs["identity_logits"]
            usable_columns = min(identity_logits.shape[1], identity_targets.shape[1])

            identity_targets = identity_targets[:, :usable_columns].to(
                identity_logits.dtype
            )
            identity_logits = identity_logits[:, :usable_columns]

            benign_examples = toxicity_targets.lt(0.5).unsqueeze(1)
            observed_identity = self._finite_mask(identity_targets)

            if identity_observed_mask is not None:
                observed_identity = observed_identity & identity_observed_mask[
                    :, :usable_columns
                ].to(torch.bool)

            identity_training_mask = benign_examples & observed_identity
            if identity_training_mask.any():
                identity_loss_all = F.binary_cross_entropy_with_logits(
                    identity_logits,
                    torch.nan_to_num(identity_targets, nan=0.0).clamp(0.0, 1.0),
                    reduction="none",
                )
                identity_loss = (
                    identity_loss_all
                    * identity_training_mask.to(identity_loss_all.dtype)
                ).sum() / identity_training_mask.sum().clamp_min(1)
                total_loss = (
                    total_loss + self.adversarial_identity_weight * identity_loss
                )

        pairwise_loss = self._bias_pairwise_loss(
            toxicity_logits,
            toxicity_targets,
            identity_targets,
        )
        return total_loss + self.pairwise_bias_weight * pairwise_loss


numeric_feature_dim = len(model_numeric_feature_columns)
pretrained_sequence_classifier = model

model = BiasAwareModernBert(
    encoder=pretrained_sequence_classifier.model,
    numeric_feature_dim=numeric_feature_dim,
    subtype_count=len(TOXICITY_SUBTYPE_COLUMNS_MODEL),
    identity_count=len(OFFICIAL_IDENTITY_COLUMNS_MODEL),
    dropout=0.15,
    adversarial_coefficient=0.08,
)
del pretrained_sequence_classifier

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

criterion = OfficialBiasAwareLoss(
    toxicity_weight=1.0,
    subtype_weight=0.18,
    adversarial_identity_weight=0.045,
    pairwise_bias_weight=0.30,
    rank_temperature=0.75,
    robust_temperature=0.20,
    max_pairs_per_slice=96,
).to(device)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
optimizer_parameter_groups = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_encoder_parameter = parameter_name.startswith("encoder.")
    learning_rate = 1.5e-5 if is_encoder_parameter else 2.0e-4
    weight_decay = (
        0.0 if any(term in parameter_name for term in no_decay_terms) else 0.01
    )

    optimizer_parameter_groups.append(
        {
            "params": [parameter],
            "lr": learning_rate,
            "weight_decay": weight_decay,
        }
    )

optimizer = AdamW(
    optimizer_parameter_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=(device.type == "cuda"))


def safe_float_matrix(frame, columns, default_value=np.nan):
    if not columns:
        return np.empty((len(frame), 0), dtype=np.float32)

    values = np.full((len(frame), len(columns)), default_value, dtype=np.float32)
    for index, column in enumerate(columns):
        if column in frame.columns:
            values[:, index] = frame[column].to_numpy(dtype=np.float32)
    return values


train_identity_targets = safe_float_matrix(
    train_df,
    OFFICIAL_IDENTITY_COLUMNS_MODEL,
)
valid_identity_targets = safe_float_matrix(
    valid_df,
    OFFICIAL_IDENTITY_COLUMNS_MODEL,
)

train_identity_observed = np.isfinite(train_identity_targets).astype(np.bool_)
valid_identity_observed = np.isfinite(valid_identity_targets).astype(np.bool_)

train_subtype_targets = safe_float_matrix(
    train_df,
    TOXICITY_SUBTYPE_COLUMNS_MODEL,
)
valid_subtype_targets = safe_float_matrix(
    valid_df,
    TOXICITY_SUBTYPE_COLUMNS_MODEL,
)

train_numeric_features = train_df[model_numeric_feature_columns].to_numpy(
    dtype=np.float32,
    copy=True,
)
valid_numeric_features = valid_df[model_numeric_feature_columns].to_numpy(
    dtype=np.float32,
    copy=True,
)
test_numeric_features = test_df[model_numeric_feature_columns].to_numpy(
    dtype=np.float32,
    copy=True,
)

train_texts = train_df[model_text_column].fillna("").astype(str).to_numpy()
valid_texts = valid_df[model_text_column].fillna("").astype(str).to_numpy()
test_texts = test_df[model_text_column].fillna("").astype(str).to_numpy()

train_targets = train_df["target"].to_numpy(dtype=np.float32, copy=True)
valid_targets = valid_df["target"].to_numpy(dtype=np.float32, copy=True)


class ToxicityDataset(Dataset):
    def __init__(
        self,
        texts,
        numeric_features,
        targets=None,
        subtype_targets=None,
        identity_targets=None,
        identity_observed_mask=None,
    ):
        self.texts = texts
        self.numeric_features = numeric_features
        self.targets = targets
        self.subtype_targets = subtype_targets
        self.identity_targets = identity_targets
        self.identity_observed_mask = identity_observed_mask

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {
            "text": self.texts[index],
            "numeric_features": self.numeric_features[index],
        }
        if self.targets is not None:
            item["target"] = self.targets[index]
        if self.subtype_targets is not None:
            item["subtype_targets"] = self.subtype_targets[index]
        if self.identity_targets is not None:
            item["identity_targets"] = self.identity_targets[index]
        if self.identity_observed_mask is not None:
            item["identity_observed_mask"] = self.identity_observed_mask[index]
        return item


def toxicity_collate(batch):
    texts = [item["text"] for item in batch]
    encoded = tokenizer(
        texts,
        truncation=True,
        max_length=INFERENCE_MAX_LENGTH,
        padding=True,
        return_tensors="pt",
    )

    output = {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "numeric_features": torch.as_tensor(
            np.stack([item["numeric_features"] for item in batch]),
            dtype=torch.float32,
        ),
    }

    if "target" in batch[0]:
        output["target"] = torch.as_tensor(
            np.asarray([item["target"] for item in batch], dtype=np.float32),
            dtype=torch.float32,
        )
    if "subtype_targets" in batch[0]:
        output["subtype_targets"] = torch.as_tensor(
            np.stack([item["subtype_targets"] for item in batch]),
            dtype=torch.float32,
        )
    if "identity_targets" in batch[0]:
        output["identity_targets"] = torch.as_tensor(
            np.stack([item["identity_targets"] for item in batch]),
            dtype=torch.float32,
        )
    if "identity_observed_mask" in batch[0]:
        output["identity_observed_mask"] = torch.as_tensor(
            np.stack([item["identity_observed_mask"] for item in batch]),
            dtype=torch.bool,
        )

    return output


class CoveragePreservingBiasSampler(Sampler):
    def __init__(self, targets, identity_targets, extra_fraction=0.20, seed=SEED):
        self.targets = np.asarray(targets, dtype=np.float32)
        self.identity_targets = np.asarray(identity_targets, dtype=np.float32)
        self.extra_fraction = float(extra_fraction)
        self.seed = int(seed)
        self.epoch = 0
        self.n_samples = len(self.targets)

        identity_present = (
            np.nan_to_num(
                self.identity_targets,
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            ).max(axis=1)
            >= 0.5
        )
        binary_target = self.targets >= 0.5

        benign_identity = np.flatnonzero(identity_present & ~binary_target)
        toxic_identity = np.flatnonzero(identity_present & binary_target)

        self.focus_indices = np.concatenate([benign_identity, toxic_identity])
        if len(self.focus_indices) == 0:
            self.focus_indices = np.arange(self.n_samples, dtype=np.int64)

        self.extra_count = max(0, int(round(self.n_samples * self.extra_fraction)))

    def set_epoch(self, epoch):
        self.epoch = int(epoch)

    def __iter__(self):
        generator = np.random.default_rng(self.seed + self.epoch)
        base_order = generator.permutation(self.n_samples).astype(np.int64)

        if self.extra_count > 0:
            focused_order = generator.choice(
                self.focus_indices,
                size=self.extra_count,
                replace=True,
            ).astype(np.int64)
            order = np.concatenate([base_order, focused_order])
        else:
            order = base_order

        return iter(order.tolist())

    def __len__(self):
        return self.n_samples + self.extra_count


train_dataset = ToxicityDataset(
    texts=train_texts,
    numeric_features=train_numeric_features,
    targets=train_targets,
    subtype_targets=train_subtype_targets,
    identity_targets=train_identity_targets,
    identity_observed_mask=train_identity_observed,
)

valid_dataset = ToxicityDataset(
    texts=valid_texts,
    numeric_features=valid_numeric_features,
    targets=valid_targets,
    subtype_targets=valid_subtype_targets,
    identity_targets=valid_identity_targets,
    identity_observed_mask=valid_identity_observed,
)

test_dataset = ToxicityDataset(
    texts=test_texts,
    numeric_features=test_numeric_features,
)

bias_sampler = CoveragePreservingBiasSampler(
    targets=train_targets,
    identity_targets=train_identity_targets,
    extra_fraction=0.20,
    seed=SEED,
)


def move_to_device(batch):
    return {
        key: (
            value.to(device, non_blocking=True)
            if isinstance(value, torch.Tensor)
            else value
        )
        for key, value in batch.items()
    }


def predict_positions(dataset, positions):
    positions = np.asarray(positions, dtype=np.int64)
    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    previous_mode = model.training
    model.eval()

    prediction_loader = DataLoader(
        Subset(dataset, positions.tolist()),
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=(device.type == "cuda"),
        persistent_workers=False,
        collate_fn=toxicity_collate,
    )

    predictions = []
    try:
        with torch.inference_mode():
            for batch in prediction_loader:
                batch = move_to_device(batch)
                with torch.cuda.amp.autocast(enabled=(device.type == "cuda")):
                    outputs = model(
                        input_ids=batch["input_ids"],
                        attention_mask=batch["attention_mask"],
                        numeric_features=batch["numeric_features"],
                    )
                    probabilities = torch.sigmoid(outputs["toxicity_logit"])
                predictions.append(probabilities.detach().float().cpu().numpy())
    finally:
        if previous_mode:
            model.train()

    return np.concatenate(predictions, axis=0).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_positions(valid_dataset, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_dataset, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "inference_max_length": INFERENCE_MAX_LENGTH,
            "numeric_feature_columns": list(model_numeric_feature_columns),
            "model_text_column": model_text_column,
            "official_identity_columns": list(OFFICIAL_IDENTITY_COLUMNS_MODEL),
            "subtype_columns": list(TOXICITY_SUBTYPE_COLUMNS_MODEL),
        },
        os.path.join(directory, "model_state.pt"),
    )

    model_configuration = {
        "encoder_config": model.encoder.config.to_dict(),
        "numeric_feature_dim": int(model.numeric_feature_dim),
        "hidden_size": int(model.hidden_size),
        "identity_count": len(OFFICIAL_IDENTITY_COLUMNS_MODEL),
        "subtype_count": len(TOXICITY_SUBTYPE_COLUMNS_MODEL),
    }

    with open(
        os.path.join(directory, "model_configuration.json"),
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(model_configuration, handle)

    tokenizer.save_pretrained(directory)

    with open(
        os.path.join(directory, "preprocessing_artifacts.pkl"),
        "wb",
    ) as handle:
        pickle.dump(
            {
                "preprocessing_artifacts": preprocessing_artifacts,
                "model_text_column": model_text_column,
                "numeric_feature_columns": list(model_numeric_feature_columns),
            },
            handle,
            protocol=pickle.HIGHEST_PROTOCOL,
        )


def load_checkpoint(directory):
    global tokenizer
    global INFERENCE_MAX_LENGTH

    checkpoint = torch.load(
        os.path.join(directory, "model_state.pt"),
        map_location=device,
    )
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    INFERENCE_MAX_LENGTH = int(
        checkpoint.get("inference_max_length", INFERENCE_MAX_LENGTH)
    )

    tokenizer = tokenizer.__class__.from_pretrained(
        directory,
        local_files_only=True,
    )

    artifact_path = os.path.join(directory, "preprocessing_artifacts.pkl")
    if os.path.exists(artifact_path):
        with open(artifact_path, "rb") as handle:
            restored = pickle.load(handle)

        if restored.get("model_text_column") != model_text_column:
            raise RuntimeError("Checkpoint text preprocessing is incompatible.")

        if restored.get("numeric_feature_columns") != list(
            model_numeric_feature_columns
        ):
            raise RuntimeError("Checkpoint numeric preprocessing is incompatible.")


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

stop_training = False
optimizer_steps = 0

for epoch in range(MAX_EPOCHS):
    if stop_training:
        break

    bias_sampler.set_epoch(epoch)

    train_loader = DataLoader(
        train_dataset,
        batch_size=TRAIN_BATCH_SIZE,
        sampler=bias_sampler,
        num_workers=NUM_WORKERS,
        pin_memory=(device.type == "cuda"),
        persistent_workers=True,
        prefetch_factor=2,
        collate_fn=toxicity_collate,
        drop_last=False,
    )

    model.train()
    epoch_loss_sum = 0.0
    epoch_updates = 0

    for batch in train_loader:
        batch = move_to_device(batch)
        optimizer.zero_grad(set_to_none=True)

        with torch.cuda.amp.autocast(enabled=(device.type == "cuda")):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
            )
            loss = criterion(
                outputs=outputs,
                toxicity_targets=batch["target"],
                subtype_targets=batch["subtype_targets"],
                identity_targets=batch["identity_targets"],
                identity_observed_mask=batch["identity_observed_mask"],
            )

        amp_scaler.scale(loss).backward()
        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        amp_scaler.step(optimizer)
        amp_scaler.update()

        optimizer_steps += 1
        epoch_updates += 1
        epoch_loss_sum += float(loss.detach().cpu())

        if session.step():
            stop_training = True
            break

    if hasattr(train_loader, "_iterator") and train_loader._iterator is not None:
        train_loader._iterator._shutdown_workers()

    if epoch_updates > 0:
        print(
            f"Epoch {epoch + 1}: updates={epoch_updates}, "
            f"loss={epoch_loss_sum / epoch_updates:.6f}"
        )

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
