import os
os.sched_setaffinity(0, {73, 9, 10, 74, 14, 15, 78, 79})
import html
import json
import math
import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Sequence

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from engine.candidate_runtime import CandidateSession


INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")
WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

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
    "black",
    "white",
    "christian",
    "jewish",
    "muslim",
    "homosexual_gay_or_lesbian",
    "psychiatric_or_mental_illness",
]

TOXICITY_AUX_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

AUXILIARY_LABEL_COLUMNS = TOXICITY_AUX_COLUMNS + [
    "toxicity_annotator_count",
    "identity_annotator_count",
]

STYLE_FEATURE_COLUMNS = [
    "feat_log_char_count",
    "feat_log_word_count",
    "feat_uppercase_ratio",
    "feat_log_exclamation_count",
    "feat_log_question_count",
    "feat_log_url_count",
    "feat_log_email_count",
    "feat_log_digit_count",
    "feat_log_newline_count",
    "feat_log_repeated_punct_count",
    "feat_quote_ratio",
    "feat_non_ascii_ratio",
    "feat_identity_term_count",
    "feat_has_identity_context",
]

URL_RE = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", flags=re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
REPEATED_PUNCT_RE = re.compile(r"([!?.,])\1{2,}")

IDENTITY_TERMS = (
    r"gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbtq?|queer|bisexual|"
    r"transgender|transsexual|nonbinary|cisgender|"
    r"muslim|muslims|islamic|islam|jew|jews|jewish|christian|christians|"
    r"catholic|catholics|protestant|protestants|hindu|hindus|buddhist|buddhists|"
    r"atheist|atheists|"
    r"black|blacks|white|whites|asian|asians|latino|latina|latinos|latinas|"
    r"african[\s-]american|native[\s-]american|"
    r"woman|women|female|females|man|men|male|males|"
    r"disabled|disability|autistic|autism|mental[\s-]illness|psychiatric"
)
IDENTITY_RE = re.compile(rf"\b(?:{IDENTITY_TERMS})\b", flags=re.IGNORECASE)


def normalize_comment(value):
    if pd.isna(value):
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = text.replace("\u200b", " ").replace("\ufeff", " ")
    text = CONTROL_RE.sub(" ", text)
    text = EMAIL_RE.sub(" [EMAIL] ", text)
    text = URL_RE.sub(" [URL] ", text)
    text = HTML_TAG_RE.sub(" ", text)
    return WHITESPACE_RE.sub(" ", text).strip()


def truncate_middle(text, max_chars=12000):
    if len(text) <= max_chars:
        return text
    head_chars = max_chars // 2
    tail_chars = max_chars - head_chars
    return f"{text[:head_chars]} [TRUNCATED] {text[-tail_chars:]}"


def extract_identity_context(text, context_chars=110, max_mentions=4):
    matches = list(IDENTITY_RE.finditer(text))
    if not matches:
        return ""

    snippets = []
    previous_end = -1

    for match in matches[:max_mentions]:
        left = max(0, match.start() - context_chars)
        right = min(len(text), match.end() + context_chars)

        while left > 0 and not text[left - 1].isspace():
            left -= 1
        while right < len(text) and not text[right : right + 1].isspace():
            right += 1

        if left < previous_end:
            continue

        snippet = text[left:right].strip()
        if snippet:
            snippets.append(snippet)
            previous_end = right

    return " [CONTEXT_SEP] ".join(snippets)


def add_text_representations(frame):
    frame = frame.copy()
    raw_text = frame["comment_text"].fillna("").astype(str)
    clean_text = raw_text.map(normalize_comment)
    frame["text_clean"] = clean_text.map(truncate_middle)
    frame["identity_context_text"] = clean_text.map(extract_identity_context)
    return frame


def add_style_features(frame):
    frame = frame.copy()
    raw_text = frame["comment_text"].fillna("").astype(str)
    clean_text = frame["text_clean"].fillna("").astype(str)

    char_count = clean_text.str.len().astype(np.float32)
    alphabetic_count = clean_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").astype(np.float32)

    frame["feat_log_char_count"] = np.log1p(char_count).astype(np.float32)
    frame["feat_log_word_count"] = np.log1p(clean_text.str.count(r"\S+")).astype(
        np.float32
    )
    frame["feat_uppercase_ratio"] = (
        uppercase_count / np.maximum(alphabetic_count, 1.0)
    ).astype(np.float32)
    frame["feat_log_exclamation_count"] = np.log1p(clean_text.str.count("!")).astype(
        np.float32
    )
    frame["feat_log_question_count"] = np.log1p(clean_text.str.count(r"\?")).astype(
        np.float32
    )
    frame["feat_log_url_count"] = np.log1p(raw_text.str.count(URL_RE)).astype(
        np.float32
    )
    frame["feat_log_email_count"] = np.log1p(raw_text.str.count(EMAIL_RE)).astype(
        np.float32
    )
    frame["feat_log_digit_count"] = np.log1p(clean_text.str.count(r"\d")).astype(
        np.float32
    )
    frame["feat_log_newline_count"] = np.log1p(raw_text.str.count(r"\n")).astype(
        np.float32
    )
    frame["feat_log_repeated_punct_count"] = np.log1p(
        clean_text.str.count(REPEATED_PUNCT_RE)
    ).astype(np.float32)
    frame["feat_quote_ratio"] = (
        clean_text.str.count(r"""["']""").astype(np.float32)
        / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    frame["feat_non_ascii_ratio"] = (
        clean_text.str.count(r"[^\x00-\x7F]").astype(np.float32)
        / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    frame["feat_identity_term_count"] = np.log1p(
        clean_text.str.count(IDENTITY_RE)
    ).astype(np.float32)
    frame["feat_has_identity_context"] = (
        frame["identity_context_text"].str.len() > 0
    ).astype(np.float32)

    return frame


def add_label_views(frame):
    frame = frame.copy()

    if "target" in frame.columns:
        frame["target_binary"] = (
            pd.to_numeric(frame["target"], errors="coerce").fillna(0.0) >= 0.5
        ).astype(np.int8)

    for column in IDENTITY_COLUMNS:
        if column in frame.columns:
            frame[f"{column}_binary"] = (
                pd.to_numeric(frame[column], errors="coerce").fillna(0.0) >= 0.5
            ).astype(np.int8)

    return frame


def apply_feature_pipeline(frame, include_labels):
    frame = add_text_representations(frame)
    frame = add_style_features(frame)
    if include_labels:
        frame = add_label_views(frame)
    return frame


session = CandidateSession.from_env()

train_header = pd.read_csv(INPUT_DIR / "train.csv", nrows=0).columns.tolist()
test_header = pd.read_csv(INPUT_DIR / "test.csv", nrows=0).columns.tolist()

required_train_columns = ["id", "target", "comment_text"]
optional_train_columns = [
    column
    for column in IDENTITY_COLUMNS + AUXILIARY_LABEL_COLUMNS
    if column in train_header
]
train_usecols = list(dict.fromkeys(required_train_columns + optional_train_columns))
test_usecols = [column for column in ["id", "comment_text"] if column in test_header]

raw_train_df = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=train_usecols,
    low_memory=False,
)
raw_test_df = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=test_usecols,
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)

train_df = apply_feature_pipeline(train_df, include_labels=True)
valid_df = apply_feature_pipeline(valid_df, include_labels=True)
test_df = apply_feature_pipeline(test_df, include_labels=False)

train_style = train_df[STYLE_FEATURE_COLUMNS].replace([np.inf, -np.inf], np.nan)
valid_style = valid_df[STYLE_FEATURE_COLUMNS].replace([np.inf, -np.inf], np.nan)
test_style = test_df[STYLE_FEATURE_COLUMNS].replace([np.inf, -np.inf], np.nan)

train_upper_caps = train_style.quantile(0.995).to_numpy(dtype=np.float32)
train_upper_caps = np.where(
    np.isfinite(train_upper_caps) & (train_upper_caps > 0),
    train_upper_caps,
    1.0,
).astype(np.float32)

imputer = SimpleImputer(strategy="median")
scaler = RobustScaler(quantile_range=(5.0, 95.0))

train_style_array = np.minimum(
    train_style.to_numpy(dtype=np.float32),
    train_upper_caps[None, :],
)
valid_style_array = np.minimum(
    valid_style.to_numpy(dtype=np.float32),
    train_upper_caps[None, :],
)
test_style_array = np.minimum(
    test_style.to_numpy(dtype=np.float32),
    train_upper_caps[None, :],
)

train_style_scaled = scaler.fit_transform(
    imputer.fit_transform(train_style_array)
).astype(np.float32)
valid_style_scaled = scaler.transform(imputer.transform(valid_style_array)).astype(
    np.float32
)
test_style_scaled = scaler.transform(imputer.transform(test_style_array)).astype(
    np.float32
)

scaled_style_columns = [f"{column}_scaled" for column in STYLE_FEATURE_COLUMNS]
train_df.loc[:, scaled_style_columns] = train_style_scaled
valid_df.loc[:, scaled_style_columns] = valid_style_scaled
test_df.loc[:, scaled_style_columns] = test_style_scaled

feature_state = {
    "normalization_version": "identity_preserving_context_v1",
    "style_feature_columns": STYLE_FEATURE_COLUMNS,
    "scaled_style_columns": scaled_style_columns,
    "upper_caps": train_upper_caps,
    "imputer": imputer,
    "scaler": scaler,
    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    "max_model_text_chars": 12000,
}
joblib.dump(feature_state, WORKING_DIR / "data_processing_state.joblib")

MODEL_MAX_LENGTH = 320
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
AMP_ENABLED = DEVICE.type == "cuda"
grad_scaler = torch.cuda.amp.GradScaler(enabled=AMP_ENABLED)

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)
tokenizer.model_max_length = MODEL_MAX_LENGTH

MODEL_IDENTITY_COLUMNS = list(IDENTITY_COLUMNS)
FAIRNESS_IDENTITY_COLUMNS = list(OFFICIAL_IDENTITY_COLUMNS)
fairness_identity_indices = [
    MODEL_IDENTITY_COLUMNS.index(column)
    for column in FAIRNESS_IDENTITY_COLUMNS
    if column in MODEL_IDENTITY_COLUMNS
]


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = float(coefficient)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return -ctx.coefficient * gradient_output, None


class GradientReversal(nn.Module):
    def __init__(self, coefficient=0.0):
        super().__init__()
        self.coefficient = float(coefficient)

    def forward(self, inputs):
        return GradientReversalFunction.apply(inputs, self.coefficient)


class FairDebertaToxicityModel(nn.Module):
    def __init__(
        self,
        pretrained_sequence_classifier,
        num_auxiliary_labels,
        num_identity_labels,
        representation_dropout=0.15,
    ):
        super().__init__()
        self.deberta = pretrained_sequence_classifier.deberta
        self.backbone_config = pretrained_sequence_classifier.config

        hidden_size = int(self.backbone_config.hidden_size)
        self.representation_norm = nn.LayerNorm(hidden_size)
        self.representation_dropout = nn.Dropout(representation_dropout)

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(representation_dropout),
            nn.Linear(hidden_size // 2, 1),
        )
        self.auxiliary_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(representation_dropout),
            nn.Linear(hidden_size // 2, num_auxiliary_labels),
        )
        self.gradient_reversal = GradientReversal(coefficient=0.0)
        self.identity_adversary = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(representation_dropout),
            nn.Linear(hidden_size // 2, num_identity_labels),
        )
        self._initialize_new_heads()

    def _initialize_new_heads(self):
        for module in (
            self.toxicity_head,
            self.auxiliary_head,
            self.identity_adversary,
        ):
            for layer in module.modules():
                if isinstance(layer, nn.Linear):
                    nn.init.xavier_uniform_(layer.weight)
                    nn.init.zeros_(layer.bias)

    def set_adversarial_strength(self, coefficient):
        self.gradient_reversal.coefficient = float(max(0.0, coefficient))

    def forward(self, input_ids, attention_mask):
        encoder_outputs = self.deberta(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        cls_representation = encoder_outputs.last_hidden_state[:, 0]
        representation = self.representation_dropout(
            self.representation_norm(cls_representation)
        )

        toxicity_logit = self.toxicity_head(representation).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(representation)
        identity_logits = self.identity_adversary(
            self.gradient_reversal(representation)
        )

        return {
            "toxicity_logit": toxicity_logit,
            "toxicity_probability": torch.sigmoid(toxicity_logit),
            "auxiliary_logits": auxiliary_logits,
            "identity_logits": identity_logits,
        }


@dataclass
class FairLossOutput:
    total: torch.Tensor
    toxicity: torch.Tensor
    auxiliary: torch.Tensor
    adversarial_identity: torch.Tensor
    ranking: torch.Tensor


class BiasAwareRankingLoss(nn.Module):
    def __init__(
        self,
        fairness_indices: Sequence[int],
        main_weight=1.0,
        auxiliary_weight=0.16,
        identity_adversary_weight=0.10,
        ranking_weight=0.30,
        max_examples_per_side=72,
    ):
        super().__init__()
        self.register_buffer(
            "fairness_indices",
            torch.tensor(list(fairness_indices), dtype=torch.long),
            persistent=True,
        )
        self.main_weight = float(main_weight)
        self.auxiliary_weight = float(auxiliary_weight)
        self.identity_adversary_weight = float(identity_adversary_weight)
        self.ranking_weight = float(ranking_weight)
        self.max_examples_per_side = int(max_examples_per_side)

    @staticmethod
    def _masked_bce(logits, targets, valid_mask, weights=None):
        if valid_mask.sum().item() == 0:
            return logits.sum() * 0.0

        safe_targets = torch.where(valid_mask, targets, torch.zeros_like(targets))
        values = F.binary_cross_entropy_with_logits(
            logits,
            safe_targets,
            reduction="none",
        )
        if weights is not None:
            values = values * weights

        valid_values = values[valid_mask]
        return valid_values.mean() if valid_values.numel() else logits.sum() * 0.0

    def _sample_indices(self, mask):
        indices = torch.where(mask)[0]
        if indices.numel() <= self.max_examples_per_side:
            return indices
        permutation = torch.randperm(indices.numel(), device=indices.device)
        return indices[permutation[: self.max_examples_per_side]]

    def _ordered_pair_loss(self, logits, lower_mask, higher_mask):
        lower_indices = self._sample_indices(lower_mask)
        higher_indices = self._sample_indices(higher_mask)

        if lower_indices.numel() == 0 or higher_indices.numel() == 0:
            return None

        lower_scores = logits[lower_indices].unsqueeze(1)
        higher_scores = logits[higher_indices].unsqueeze(0)
        return F.softplus(lower_scores - higher_scores).mean()

    def _bias_ranking_loss(self, logits, binary_targets, identity_targets):
        losses = []
        known_identity = torch.isfinite(identity_targets)

        for identity_index in self.fairness_indices.tolist():
            identity_known = known_identity[:, identity_index]
            identity_member = identity_targets[:, identity_index].nan_to_num(0.0) >= 0.5
            background_member = ~identity_member

            subgroup_negative = identity_known & identity_member & (binary_targets == 0)
            subgroup_positive = identity_known & identity_member & (binary_targets == 1)
            background_negative = (
                identity_known & background_member & (binary_targets == 0)
            )
            background_positive = (
                identity_known & background_member & (binary_targets == 1)
            )

            components = [
                self._ordered_pair_loss(
                    logits,
                    lower_mask=subgroup_negative,
                    higher_mask=subgroup_positive,
                ),
                self._ordered_pair_loss(
                    logits,
                    lower_mask=subgroup_negative,
                    higher_mask=background_positive,
                ),
                self._ordered_pair_loss(
                    logits,
                    lower_mask=background_negative,
                    higher_mask=subgroup_positive,
                ),
            ]

            for component in components:
                if component is not None:
                    losses.append(component)

        if not losses:
            return logits.sum() * 0.0

        return torch.stack(losses).mean()

    def forward(
        self,
        outputs: Dict[str, torch.Tensor],
        target: torch.Tensor,
        auxiliary_targets: Optional[torch.Tensor] = None,
        identity_targets: Optional[torch.Tensor] = None,
    ):
        toxicity_logits = outputs["toxicity_logit"]
        binary_target = (target >= 0.5).to(dtype=toxicity_logits.dtype)

        if identity_targets is None:
            identity_targets = torch.full(
                (toxicity_logits.shape[0], len(MODEL_IDENTITY_COLUMNS)),
                float("nan"),
                device=toxicity_logits.device,
                dtype=toxicity_logits.dtype,
            )
        else:
            identity_targets = identity_targets.to(
                device=toxicity_logits.device,
                dtype=toxicity_logits.dtype,
            )

        any_known_member = (
            torch.isfinite(identity_targets) & (identity_targets.nan_to_num(0.0) >= 0.5)
        ).any(dim=1)

        toxicity_weights = (
            1.0
            + 0.45 * binary_target
            + 3.0 * ((binary_target == 0) & any_known_member).to(toxicity_logits.dtype)
            + 0.80 * ((binary_target == 1) & any_known_member).to(toxicity_logits.dtype)
        )

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            binary_target,
            weight=toxicity_weights,
        )

        auxiliary_loss = toxicity_logits.sum() * 0.0
        if auxiliary_targets is not None:
            auxiliary_targets = auxiliary_targets.to(
                device=toxicity_logits.device,
                dtype=toxicity_logits.dtype,
            )
            auxiliary_valid = torch.isfinite(auxiliary_targets)
            auxiliary_loss = self._masked_bce(
                outputs["auxiliary_logits"],
                auxiliary_targets,
                auxiliary_valid,
            )

        identity_valid = torch.isfinite(identity_targets)
        identity_positive = identity_targets.nan_to_num(0.0)
        identity_weights = 1.0 + 2.5 * identity_positive
        identity_loss = self._masked_bce(
            outputs["identity_logits"],
            identity_targets,
            identity_valid,
            weights=identity_weights,
        )

        ranking_loss = self._bias_ranking_loss(
            toxicity_logits,
            binary_target,
            identity_targets,
        )

        total_loss = (
            self.main_weight * toxicity_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.identity_adversary_weight * identity_loss
            + self.ranking_weight * ranking_loss
        )

        return FairLossOutput(
            total=total_loss,
            toxicity=toxicity_loss.detach(),
            auxiliary=auxiliary_loss.detach(),
            adversarial_identity=identity_loss.detach(),
            ranking=ranking_loss.detach(),
        )


toxicity_model = FairDebertaToxicityModel(
    pretrained_sequence_classifier=model,
    num_auxiliary_labels=len(TOXICITY_AUX_COLUMNS),
    num_identity_labels=len(MODEL_IDENTITY_COLUMNS),
    representation_dropout=0.15,
)

for parameter in toxicity_model.deberta.embeddings.parameters():
    parameter.requires_grad = False

encoder_layers = getattr(toxicity_model.deberta.encoder, "layer", [])
for layer in list(encoder_layers)[:8]:
    for parameter in layer.parameters():
        parameter.requires_grad = False

toxicity_model.to(DEVICE)
del model

criterion = BiasAwareRankingLoss(
    fairness_indices=fairness_identity_indices,
    main_weight=1.0,
    auxiliary_weight=0.16,
    identity_adversary_weight=0.10,
    ranking_weight=0.30,
    max_examples_per_side=72,
).to(DEVICE)

no_decay_tokens = ("bias", "LayerNorm.weight", "layer_norm.weight")
backbone_decay, backbone_no_decay = [], []
head_decay, head_no_decay = [], []

for parameter_name, parameter in toxicity_model.named_parameters():
    if not parameter.requires_grad:
        continue

    belongs_to_backbone = parameter_name.startswith("deberta.")
    has_no_decay = any(token in parameter_name for token in no_decay_tokens)

    if belongs_to_backbone and has_no_decay:
        backbone_no_decay.append(parameter)
    elif belongs_to_backbone:
        backbone_decay.append(parameter)
    elif has_no_decay:
        head_no_decay.append(parameter)
    else:
        head_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": backbone_decay, "lr": 8e-6, "weight_decay": 0.01},
        {"params": backbone_no_decay, "lr": 8e-6, "weight_decay": 0.0},
        {"params": head_decay, "lr": 7e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 7e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

model_design_state = {
    "model_id": "microsoft/deberta-v3-large",
    "max_length": MODEL_MAX_LENGTH,
    "auxiliary_columns": TOXICITY_AUX_COLUMNS,
    "identity_columns": MODEL_IDENTITY_COLUMNS,
    "fairness_identity_columns": FAIRNESS_IDENTITY_COLUMNS,
    "frozen_encoder_layers": 8,
    "adversarial_strength_schedule": {
        "start": 0.0,
        "maximum": 0.10,
        "warmup_fraction": 0.15,
    },
}


def compose_model_text(base_text, context_text):
    base_text = "" if base_text is None else str(base_text)
    context_text = "" if context_text is None else str(context_text)

    if context_text.strip():
        return f"{context_text} [CONTEXT_SEP] {base_text}"

    return base_text


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["text_clean"].fillna("").astype(str).to_numpy()
        self.contexts = frame["identity_context_text"].fillna("").astype(str).to_numpy()
        self.targets = (
            frame["target"].astype(np.float32).fillna(0.0).to_numpy(dtype=np.float32)
        )
        self.auxiliary_targets = (
            frame.reindex(columns=TOXICITY_AUX_COLUMNS)
            .apply(pd.to_numeric, errors="coerce")
            .to_numpy(dtype=np.float32)
        )
        self.identity_targets = (
            frame.reindex(columns=MODEL_IDENTITY_COLUMNS)
            .apply(pd.to_numeric, errors="coerce")
            .to_numpy(dtype=np.float32)
        )

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.contexts[index],
            self.targets[index],
            self.auxiliary_targets[index],
            self.identity_targets[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, frame, positional_indices):
        positional_indices = np.asarray(positional_indices, dtype=np.int64)
        self.texts = (
            frame["text_clean"].fillna("").astype(str).to_numpy()[positional_indices]
        )
        self.contexts = (
            frame["identity_context_text"]
            .fillna("")
            .astype(str)
            .to_numpy()[positional_indices]
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index], self.contexts[index]


def training_collate_fn(batch):
    texts, contexts, targets, auxiliary_targets, identity_targets = zip(*batch)
    model_texts = [
        compose_model_text(text, context) for text, context in zip(texts, contexts)
    ]

    encoded = tokenizer(
        model_texts,
        padding=True,
        truncation=True,
        max_length=MODEL_MAX_LENGTH,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "target": torch.as_tensor(np.asarray(targets, dtype=np.float32)),
        "auxiliary_targets": torch.as_tensor(
            np.asarray(auxiliary_targets, dtype=np.float32)
        ),
        "identity_targets": torch.as_tensor(
            np.asarray(identity_targets, dtype=np.float32)
        ),
    }


def inference_collate_fn(batch):
    texts, contexts = zip(*batch)
    model_texts = [
        compose_model_text(text, context) for text, context in zip(texts, contexts)
    ]

    encoded = tokenizer(
        model_texts,
        padding=True,
        truncation=True,
        max_length=MODEL_MAX_LENGTH,
        pad_to_multiple_of=8,
        return_tensors="pt",
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
    }


TRAIN_BATCH_SIZE = 8 if DEVICE.type == "cuda" else 2
INFERENCE_BATCH_SIZE = 16 if DEVICE.type == "cuda" else 4
GRADIENT_ACCUMULATION_STEPS = 2
NUM_EPOCHS = 3
NUM_WORKERS = 2
MAX_GRAD_NORM = 1.0
ADVERSARIAL_WARMUP_UPDATES = 2500


@torch.inference_mode()
def predict_frame_positions(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    inference_dataset = ToxicityInferenceDataset(frame, positional_indices)
    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=(DEVICE.type == "cuda"),
        persistent_workers=(NUM_WORKERS > 0),
        collate_fn=inference_collate_fn,
    )

    previous_mode = toxicity_model.training
    toxicity_model.eval()
    prediction_chunks = []

    for batch in inference_loader:
        input_ids = batch["input_ids"].to(DEVICE, non_blocking=True)
        attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=True)

        with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
            outputs = toxicity_model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )

        prediction_chunks.append(
            outputs["toxicity_probability"]
            .float()
            .cpu()
            .numpy()
            .astype(np.float64, copy=False)
        )

    toxicity_model.train(previous_mode)
    return np.concatenate(prediction_chunks, axis=0)


def predict_validation(positional_indices):
    return predict_frame_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_df, positional_indices)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    checkpoint_payload = {
        "model_state_dict": toxicity_model.state_dict(),
        "model_id": model_design_state["model_id"],
        "max_length": int(MODEL_MAX_LENGTH),
        "input_representation": "identity_context_then_full_comment_v1",
        "identity_columns": list(MODEL_IDENTITY_COLUMNS),
        "auxiliary_columns": list(TOXICITY_AUX_COLUMNS),
        "fairness_identity_columns": list(FAIRNESS_IDENTITY_COLUMNS),
    }
    torch.save(checkpoint_payload, directory / "toxicity_model.pt")

    with open(directory / "inference_config.json", "w", encoding="utf-8") as handle:
        json.dump(
            {
                "model_design_state": model_design_state,
                "model_max_length": int(MODEL_MAX_LENGTH),
                "probability_transform": "sigmoid(toxicity_logit)",
                "input_representation": "identity_context_then_full_comment_v1",
            },
            handle,
            indent=2,
            sort_keys=True,
        )

    tokenizer.save_pretrained(str(directory / "tokenizer"))
    toxicity_model.backbone_config.save_pretrained(str(directory / "encoder_config"))

    feature_state_path = WORKING_DIR / "data_processing_state.joblib"
    if feature_state_path.exists():
        shutil.copy2(feature_state_path, directory / "data_processing_state.joblib")


def load_checkpoint(directory):
    checkpoint_path = Path(directory) / "toxicity_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location=DEVICE,
        weights_only=False,
    )
    toxicity_model.load_state_dict(checkpoint_payload["model_state_dict"], strict=True)
    toxicity_model.to(DEVICE)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

training_dataset = ToxicityTrainingDataset(train_df)
training_loader = DataLoader(
    training_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=(DEVICE.type == "cuda"),
    persistent_workers=(NUM_WORKERS > 0),
    collate_fn=training_collate_fn,
)

estimated_updates_per_epoch = math.ceil(
    len(training_loader) / GRADIENT_ACCUMULATION_STEPS
)
total_estimated_updates = max(1, estimated_updates_per_epoch * NUM_EPOCHS)
warmup_updates = min(1200, max(100, total_estimated_updates // 50))


def learning_rate_multiplier(update_index):
    if update_index < warmup_updates:
        return float(update_index + 1) / float(warmup_updates)

    progress = (update_index - warmup_updates) / max(
        1,
        total_estimated_updates - warmup_updates,
    )
    return max(
        0.15,
        0.5 * (1.0 + math.cos(math.pi * min(progress, 1.0))),
    )


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
optimizer_updates = 0
stop_requested = False

for epoch_index in range(NUM_EPOCHS):
    toxicity_model.train()
    total_epoch_loss = 0.0
    completed_batches = 0
    completed_updates = 0

    for batch_index, batch in enumerate(training_loader):
        adversarial_strength = 0.10 * min(
            1.0,
            optimizer_updates / float(ADVERSARIAL_WARMUP_UPDATES),
        )
        toxicity_model.set_adversarial_strength(adversarial_strength)

        input_ids = batch["input_ids"].to(DEVICE, non_blocking=True)
        attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=True)
        target = batch["target"].to(DEVICE, non_blocking=True)
        auxiliary_targets = batch["auxiliary_targets"].to(
            DEVICE,
            non_blocking=True,
        )
        identity_targets = batch["identity_targets"].to(
            DEVICE,
            non_blocking=True,
        )

        with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
            outputs = toxicity_model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )
            loss_output = criterion(
                outputs=outputs,
                target=target,
                auxiliary_targets=auxiliary_targets,
                identity_targets=identity_targets,
            )
            scaled_loss = loss_output.total / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()
        total_epoch_loss += float(loss_output.total.detach().float().cpu())
        completed_batches += 1

        is_update_boundary = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(training_loader)
        if not is_update_boundary:
            continue

        grad_scaler.unscale_(optimizer)
        clip_grad_norm_(toxicity_model.parameters(), max_norm=MAX_GRAD_NORM)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

        optimizer_updates += 1
        completed_updates += 1

        stop_requested = session.step()
        if stop_requested:
            break

    mean_epoch_loss = total_epoch_loss / max(1, completed_batches)
    print(
        f"Epoch {epoch_index + 1}: loss={mean_epoch_loss:.6f}, "
        f"updates={completed_updates}"
    )

    if stop_requested:
        break

finish_result = session.finish()

if isinstance(finish_result, dict):
    score = finish_result.get(
        "score",
        finish_result.get("final_score", finish_result.get("best_score")),
    )
elif finish_result is not None:
    score = finish_result
else:
    score = getattr(
        session,
        "final_score",
        getattr(session, "best_score", getattr(session, "score", None)),
    )

if score is None:
    raise RuntimeError("CandidateSession did not provide an official validation score.")

score = float(score)
print(f"Final Validation Score: {score}")
