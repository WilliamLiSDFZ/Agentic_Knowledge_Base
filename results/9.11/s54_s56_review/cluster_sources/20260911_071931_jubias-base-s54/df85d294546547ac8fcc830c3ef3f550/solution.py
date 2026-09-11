import os
import re
import html
import json
import pickle
import shutil
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
WORKING_DIR.mkdir(parents=True, exist_ok=True)

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
    "black",
    "christian",
    "female",
    "homosexual_gay_or_lesbian",
    "jewish",
    "male",
    "muslim",
    "psychiatric_or_mental_illness",
    "white",
]

AUXILIARY_TARGETS = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

NUMERIC_FEATURE_COLUMNS = [
    "feat_log_char_count",
    "feat_log_word_count",
    "feat_uppercase_ratio",
    "feat_digit_ratio",
    "feat_punctuation_ratio",
    "feat_log_exclamation_count",
    "feat_log_question_count",
    "feat_log_newline_count",
    "feat_log_repeated_punctuation",
    "feat_log_elongated_word_count",
    "feat_log_caps_word_count",
    "feat_log_identity_term_count",
]

TRAIN_BATCH_SIZE = 8
INFERENCE_BATCH_SIZE = 16
MAX_SEQUENCE_LENGTH = 256
GRADIENT_ACCUMULATION_STEPS = 4
MAX_EPOCHS = 4
NUM_WORKERS = 2
COUNTERFACTUAL_CONSISTENCY_WEIGHT = 0.15

session = CandidateSession.from_env()

available_train_columns = pd.read_csv(
    INPUT_DIR / "train.csv",
    nrows=0,
).columns.tolist()

train_usecols = [
    column
    for column in ["id", "target", "comment_text"]
    + AUXILIARY_TARGETS
    + IDENTITY_COLUMNS
    if column in available_train_columns
]

raw_train_df = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=train_usecols,
    low_memory=False,
)

raw_test_df = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df

for frame in (train_df, valid_df, test_df):
    frame["comment_text"] = frame["comment_text"].fillna("").astype(str)

url_pattern = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
user_pattern = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,}")
whitespace_pattern = re.compile(r"\s+")
control_pattern = re.compile(r"[\u0000-\u001f\u007f-\u009f]+")

identity_lexicon = [
    "male",
    "female",
    "man",
    "men",
    "woman",
    "women",
    "boy",
    "boys",
    "girl",
    "girls",
    "gay",
    "lesbian",
    "homosexual",
    "straight",
    "heterosexual",
    "transgender",
    "trans",
    "christian",
    "jewish",
    "muslim",
    "islam",
    "hindu",
    "buddhist",
    "atheist",
    "black",
    "white",
    "asian",
    "latino",
    "latina",
    "race",
    "racist",
    "disabled",
    "disability",
    "autistic",
    "mental illness",
    "psychiatric",
]

identity_term_pattern = re.compile(
    r"\b(?:"
    + "|".join(
        re.escape(term) for term in sorted(identity_lexicon, key=len, reverse=True)
    )
    + r")\b",
    flags=re.IGNORECASE,
)


def clean_comment_text(text):
    text = unicodedata.normalize("NFKC", html.unescape(str(text)))
    text = control_pattern.sub(" ", text)
    text = url_pattern.sub(" [URL] ", text)
    text = user_pattern.sub(" [USER] ", text)
    text = whitespace_pattern.sub(" ", text).strip()
    return text


def text_shape_features(text):
    length = len(text)
    token_count = len(text.split())
    alpha_count = sum(character.isalpha() for character in text)
    uppercase_count = sum(character.isupper() for character in text)
    digit_count = sum(character.isdigit() for character in text)
    punctuation_count = sum(character in "!?.,;:'\"-_*#$%&()[]{}" for character in text)
    exclamation_count = text.count("!")
    question_count = text.count("?")
    newline_count = text.count("\n")
    repeated_punctuation = len(re.findall(r"([!?.,])\1{1,}", text))
    elongated_words = len(re.findall(r"(?i)\b\w*([a-z])\1{2,}\w*\b", text))
    caps_words = len(re.findall(r"\b[A-Z]{3,}\b", text))
    identity_mentions = len(identity_term_pattern.findall(text))

    return (
        np.log1p(length),
        np.log1p(token_count),
        uppercase_count / max(alpha_count, 1),
        digit_count / max(length, 1),
        punctuation_count / max(length, 1),
        np.log1p(exclamation_count),
        np.log1p(question_count),
        np.log1p(newline_count),
        np.log1p(repeated_punctuation),
        np.log1p(elongated_words),
        np.log1p(caps_words),
        np.log1p(identity_mentions),
    )


def add_text_features(frame):
    cleaned_text = frame["comment_text"].map(clean_comment_text)
    feature_matrix = np.asarray(
        [text_shape_features(text) for text in cleaned_text],
        dtype=np.float32,
    )

    frame["model_text"] = cleaned_text

    for feature_index, feature_name in enumerate(NUMERIC_FEATURE_COLUMNS):
        frame[feature_name] = feature_matrix[:, feature_index]

    frame.drop(columns=["comment_text"], inplace=True)
    return frame


train_df = add_text_features(train_df)
valid_df = add_text_features(valid_df)
test_df = add_text_features(test_df)

train_feature_matrix = train_df[NUMERIC_FEATURE_COLUMNS].to_numpy(dtype=np.float32)
feature_median = np.nanmedian(train_feature_matrix, axis=0).astype(np.float32)
q25 = np.nanpercentile(train_feature_matrix, 25, axis=0).astype(np.float32)
q75 = np.nanpercentile(train_feature_matrix, 75, axis=0).astype(np.float32)
feature_iqr = np.maximum(q75 - q25, 1e-4).astype(np.float32)


def robust_scale_features(frame):
    values = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(dtype=np.float32)
    values = np.where(np.isfinite(values), values, feature_median)
    values = np.clip((values - feature_median) / feature_iqr, -8.0, 8.0)

    for feature_index, feature_name in enumerate(NUMERIC_FEATURE_COLUMNS):
        frame[feature_name] = values[:, feature_index].astype(np.float32)

    return frame


train_df = robust_scale_features(train_df)
valid_df = robust_scale_features(valid_df)
test_df = robust_scale_features(test_df)

for frame in (train_df, valid_df):
    frame["target_binary"] = (frame["target"].fillna(0.0) >= 0.5).astype(np.int8)

training_target_is_toxic = (
    train_df["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5
)
training_evaluation_identity_membership = (
    train_df.reindex(columns=EVALUATION_IDENTITIES)
    .fillna(0.0)
    .to_numpy(dtype=np.float32)
    >= 0.5
)

# The four cells directly support subgroup, BPSN, and BNSP comparisons.
training_identity_cell_names = (
    "subgroup_negative",
    "subgroup_positive",
    "background_negative",
    "background_positive",
)
training_identity_cell_ids = np.where(
    training_evaluation_identity_membership,
    np.where(training_target_is_toxic[:, None], 1, 0),
    np.where(training_target_is_toxic[:, None], 3, 2),
).astype(np.int8)

# Each nonempty cell contributes equal conceptual mass for each official identity.
sampling_row_weights = np.zeros(len(train_df), dtype=np.float64)
for identity_index, identity_column in enumerate(EVALUATION_IDENTITIES):
    identity_cell_ids = training_identity_cell_ids[:, identity_index]
    identity_cell_counts = np.bincount(
        identity_cell_ids,
        minlength=len(training_identity_cell_names),
    )

    for cell_index, cell_count in enumerate(identity_cell_counts):
        if cell_count > 0:
            sampling_row_weights[identity_cell_ids == cell_index] += (
                1.0 / float(cell_count)
            )

# Cap only extreme multi-identity overlaps, then retain strictly positive finite weights.
sampling_weight_cap = max(
    float(np.percentile(sampling_row_weights, 99.9)),
    np.finfo(np.float64).tiny,
)
sampling_row_weights = np.nan_to_num(
    sampling_row_weights,
    nan=np.finfo(np.float64).tiny,
    posinf=sampling_weight_cap,
    neginf=np.finfo(np.float64).tiny,
)
sampling_row_weights = np.clip(
    sampling_row_weights,
    np.finfo(np.float64).tiny,
    sampling_weight_cap,
)
sampling_row_weights /= sampling_row_weights.sum()

counterfactual_swaps = {
    "women": "men",
    "woman": "man",
    "female": "male",
    "girls": "boys",
    "girl": "boy",
    "she": "he",
    "her": "his",
    "hers": "his",
    "men": "women",
    "man": "woman",
    "male": "female",
    "boys": "girls",
    "boy": "girl",
    "he": "she",
    "his": "her",
    "christian": "muslim",
    "muslim": "christian",
    "jewish": "atheist",
    "atheist": "jewish",
    "black": "white",
    "white": "black",
    "gay": "straight",
    "straight": "gay",
    "lesbian": "heterosexual",
    "heterosexual": "lesbian",
}

counterfactual_pattern = re.compile(
    r"\b(?:"
    + "|".join(
        re.escape(word) for word in sorted(counterfactual_swaps, key=len, reverse=True)
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


def create_counterfactual_text(text):
    def replace_match(match):
        source = match.group(0)
        replacement = counterfactual_swaps[source.lower()]
        return preserve_case(source, replacement)

    return counterfactual_pattern.sub(replace_match, text)


available_identity_columns = [
    column for column in IDENTITY_COLUMNS if column in train_df.columns
]

if available_identity_columns:
    benign_identity_mask = (train_df["target"].fillna(0.0) < 0.5) & (
        train_df[available_identity_columns].fillna(0.0).max(axis=1) >= 0.5
    )
else:
    benign_identity_mask = pd.Series(False, index=train_df.index)

counterfactual_candidates = train_df.loc[
    benign_identity_mask,
    ["id", "target", "model_text"]
    + [column for column in AUXILIARY_TARGETS if column in train_df.columns],
].copy()

MAX_COUNTERFACTUAL_ROWS = 200_000
if len(counterfactual_candidates) > MAX_COUNTERFACTUAL_ROWS:
    counterfactual_candidates = counterfactual_candidates.sample(
        n=MAX_COUNTERFACTUAL_ROWS,
        random_state=SEED,
    )

counterfactual_candidates["counterfactual_text"] = counterfactual_candidates[
    "model_text"
].map(create_counterfactual_text)

counterfactual_train_df = counterfactual_candidates.loc[
    counterfactual_candidates["counterfactual_text"]
    != counterfactual_candidates["model_text"]
].reset_index(drop=True)

preprocessing_state = {
    "version": 1,
    "numeric_feature_columns": NUMERIC_FEATURE_COLUMNS,
    "feature_median": feature_median,
    "feature_iqr": feature_iqr,
    "identity_columns": IDENTITY_COLUMNS,
    "evaluation_identity_columns": EVALUATION_IDENTITIES,
    "auxiliary_targets": AUXILIARY_TARGETS,
    "text_normalization": (
        "NFKC + HTML unescape + URL/mention tokens + whitespace normalization"
    ),
    "counterfactual_strategy": "benign identity mention swaps, training partition only",
}

with open(WORKING_DIR / "jigsaw_preprocessing_state.pkl", "wb") as state_file:
    pickle.dump(
        preprocessing_state,
        state_file,
        protocol=pickle.HIGHEST_PROTOCOL,
    )

counterfactual_train_df.to_pickle(
    WORKING_DIR / "jigsaw_benign_counterfactual_pairs.pkl"
)

MODEL_ID = "microsoft/deberta-v3-large"
NUMERIC_FEATURE_DIM = len(NUMERIC_FEATURE_COLUMNS)
IDENTITY_TARGET_DIM = len(IDENTITY_COLUMNS)

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
AMP_ENABLED = DEVICE.type == "cuda"
PIN_MEMORY = DEVICE.type == "cuda"

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
pretrained_sequence_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, coefficient):
        ctx.coefficient = float(coefficient)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, grad_outputs):
        return grad_outputs.neg().mul(ctx.coefficient), None


def gradient_reverse(inputs, coefficient):
    return GradientReversalFunction.apply(inputs, coefficient)


class BiasAdversarialDeberta(nn.Module):
    def __init__(
        self,
        pretrained_classifier,
        numeric_feature_dim,
        identity_target_dim,
        dropout=0.15,
        adversarial_scale=1.0,
    ):
        super().__init__()

        self.backbone = pretrained_classifier.deberta
        hidden_size = int(pretrained_classifier.config.hidden_size)

        self.numeric_adapter = nn.Sequential(
            nn.Linear(numeric_feature_dim, 96),
            nn.LayerNorm(96),
            nn.GELU(),
            nn.Dropout(dropout),
        )

        self.text_projection = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
        )

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size + 96, hidden_size // 2),
            nn.LayerNorm(hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )

        adversary_hidden = max(hidden_size // 2, 256)
        self.identity_adversary = nn.Sequential(
            nn.Linear(hidden_size, adversary_hidden),
            nn.LayerNorm(adversary_hidden),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(adversary_hidden, identity_target_dim),
        )

        self.adversarial_scale = float(adversarial_scale)
        self.architecture_config = {
            "model_id": MODEL_ID,
            "numeric_feature_dim": int(numeric_feature_dim),
            "identity_target_dim": int(identity_target_dim),
            "dropout": float(dropout),
        }

        def initialize_linear(module):
            if isinstance(module, nn.Linear):
                nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

        self.numeric_adapter.apply(initialize_linear)
        self.text_projection.apply(initialize_linear)
        self.toxicity_head.apply(initialize_linear)
        self.identity_adversary.apply(initialize_linear)

    def set_adversarial_scale(self, scale):
        self.adversarial_scale = float(max(0.0, scale))

    def forward(self, input_ids, attention_mask, numeric_features=None):
        encoder_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        cls_representation = encoder_outputs.last_hidden_state[:, 0]
        text_features = self.text_projection(cls_representation)

        if numeric_features is None:
            numeric_features = torch.zeros(
                (
                    input_ids.shape[0],
                    self.architecture_config["numeric_feature_dim"],
                ),
                dtype=text_features.dtype,
                device=text_features.device,
            )
        else:
            numeric_features = numeric_features.to(
                dtype=text_features.dtype,
                device=text_features.device,
            )

        numeric_representation = self.numeric_adapter(numeric_features)
        fused_representation = torch.cat(
            [text_features, numeric_representation],
            dim=-1,
        )

        toxicity_logit = self.toxicity_head(fused_representation).squeeze(-1)
        identity_logits = self.identity_adversary(
            gradient_reverse(text_features, self.adversarial_scale)
        )

        return {
            "toxicity_logit": toxicity_logit,
            "identity_logits": identity_logits,
        }

    @torch.inference_mode()
    def predict_proba(self, input_ids, attention_mask, numeric_features=None):
        outputs = self.forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            numeric_features=numeric_features,
        )
        return torch.sigmoid(outputs["toxicity_logit"])


class BiasAdversarialToxicityLoss(nn.Module):
    def __init__(
        self,
        positive_class_weight=2.0,
        identity_adversarial_weight=0.08,
    ):
        super().__init__()

        self.register_buffer(
            "positive_class_weight",
            torch.tensor(float(positive_class_weight), dtype=torch.float32),
        )

        self.identity_adversarial_weight = float(identity_adversarial_weight)

    def forward(self, model_outputs, toxicity_targets, identity_targets=None):
        toxicity_targets = toxicity_targets.float().clamp_(0.0, 1.0)
        toxicity_logits = model_outputs["toxicity_logit"]

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
            pos_weight=self.positive_class_weight.to(toxicity_logits.dtype),
            reduction="mean",
        )

        identity_loss = toxicity_loss.new_zeros(())

        if identity_targets is not None:
            identity_targets = identity_targets.to(
                dtype=model_outputs["identity_logits"].dtype,
                device=model_outputs["identity_logits"].device,
            )

            valid_identity_labels = torch.isfinite(identity_targets)

            if valid_identity_labels.any():
                safe_identity_targets = torch.nan_to_num(
                    identity_targets,
                    nan=0.0,
                    posinf=1.0,
                    neginf=0.0,
                ).clamp_(0.0, 1.0)

                per_label_identity_loss = F.binary_cross_entropy_with_logits(
                    model_outputs["identity_logits"],
                    safe_identity_targets,
                    reduction="none",
                )

                identity_loss = (
                    per_label_identity_loss
                    * valid_identity_labels.to(per_label_identity_loss.dtype)
                ).sum() / valid_identity_labels.sum().clamp_min(1)

        total_loss = toxicity_loss + self.identity_adversarial_weight * identity_loss

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "identity_adversarial_loss": identity_loss.detach(),
        }


model = BiasAdversarialDeberta(
    pretrained_classifier=pretrained_sequence_classifier,
    numeric_feature_dim=NUMERIC_FEATURE_DIM,
    identity_target_dim=IDENTITY_TARGET_DIM,
    dropout=0.15,
    adversarial_scale=1.0,
).to(DEVICE)

criterion = BiasAdversarialToxicityLoss(
    positive_class_weight=2.0,
    identity_adversarial_weight=0.08,
).to(DEVICE)

backbone_decay_parameters = []
backbone_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    normalized_name = parameter_name.lower()
    no_decay = (
        parameter_name.endswith(".bias")
        or "layernorm" in normalized_name
        or "layer_norm" in normalized_name
        or ".norm." in normalized_name
    )

    is_backbone_parameter = parameter_name.startswith("backbone.")

    if is_backbone_parameter and no_decay:
        backbone_no_decay_parameters.append(parameter)
    elif is_backbone_parameter:
        backbone_decay_parameters.append(parameter)
    elif no_decay:
        head_no_decay_parameters.append(parameter)
    else:
        head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_decay_parameters,
            "lr": 8e-6,
            "weight_decay": 0.01,
        },
        {
            "params": backbone_no_decay_parameters,
            "lr": 8e-6,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_parameters,
            "lr": 8e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_parameters,
            "lr": 8e-5,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-6,
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=AMP_ENABLED)

counterfactual_lookup = {}
if len(counterfactual_train_df) > 0:
    counterfactual_lookup = dict(
        zip(
            counterfactual_train_df["id"].astype(str).tolist(),
            counterfactual_train_df["counterfactual_text"].astype(str).tolist(),
        )
    )


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame):
        self.ids = frame["id"].astype(str).to_numpy()
        self.texts = frame["model_text"].astype(str).to_numpy()
        self.numeric_features = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.targets = (
            frame["target"]
            .fillna(0.0)
            .to_numpy(
                dtype=np.float32,
                copy=True,
            )
        )
        self.identity_targets = frame.reindex(columns=IDENTITY_COLUMNS).to_numpy(
            dtype=np.float32,
            copy=True,
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        sample_id = self.ids[index]
        counterfactual_text = counterfactual_lookup.get(sample_id, "")

        return {
            "text": self.texts[index],
            "numeric_features": self.numeric_features[index],
            "target": self.targets[index],
            "identity_targets": self.identity_targets[index],
            "counterfactual_text": counterfactual_text,
        }


class ToxicityInferenceDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["model_text"].astype(str).to_numpy()
        self.numeric_features = frame[NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return {
            "text": self.texts[index],
            "numeric_features": self.numeric_features[index],
        }


def tokenize_text_batch(texts):
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


def training_collate(batch):
    primary_inputs = tokenize_text_batch([row["text"] for row in batch])

    result = {
        **primary_inputs,
        "numeric_features": torch.tensor(
            np.stack([row["numeric_features"] for row in batch]),
            dtype=torch.float32,
        ),
        "targets": torch.tensor(
            np.asarray([row["target"] for row in batch], dtype=np.float32),
            dtype=torch.float32,
        ),
        "identity_targets": torch.tensor(
            np.stack([row["identity_targets"] for row in batch]),
            dtype=torch.float32,
        ),
    }

    counterfactual_positions = [
        position
        for position, row in enumerate(batch)
        if isinstance(row["counterfactual_text"], str)
        and row["counterfactual_text"].strip()
    ]

    if counterfactual_positions:
        counterfactual_inputs = tokenize_text_batch(
            [
                batch[position]["counterfactual_text"]
                for position in counterfactual_positions
            ]
        )

        result["counterfactual_input_ids"] = counterfactual_inputs["input_ids"]
        result["counterfactual_attention_mask"] = counterfactual_inputs[
            "attention_mask"
        ]
        result["counterfactual_positions"] = torch.tensor(
            counterfactual_positions,
            dtype=torch.long,
        )
    else:
        result["counterfactual_input_ids"] = None
        result["counterfactual_attention_mask"] = None
        result["counterfactual_positions"] = None

    return result


def inference_collate(batch):
    model_inputs = tokenize_text_batch([row["text"] for row in batch])
    model_inputs["numeric_features"] = torch.tensor(
        np.stack([row["numeric_features"] for row in batch]),
        dtype=torch.float32,
    )
    return model_inputs


train_dataset = ToxicityTrainingDataset(train_df)

train_sampler_generator = torch.Generator()
train_sampler_generator.manual_seed(SEED)

train_sampler = WeightedRandomSampler(
    weights=torch.as_tensor(sampling_row_weights, dtype=torch.double),
    num_samples=len(train_dataset),
    replacement=True,
    generator=train_sampler_generator,
)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    sampler=train_sampler,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=NUM_WORKERS > 0,
    collate_fn=training_collate,
    drop_last=False,
)


def move_primary_batch_to_device(batch):
    return {
        "input_ids": batch["input_ids"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        ),
        "attention_mask": batch["attention_mask"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        ),
        "numeric_features": batch["numeric_features"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        ),
        "targets": batch["targets"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        ),
        "identity_targets": batch["identity_targets"].to(
            DEVICE,
            non_blocking=PIN_MEMORY,
        ),
    }


@torch.inference_mode()
def predict_frame(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64)

    if positional_indices.ndim != 1:
        raise ValueError("Prediction callback indices must be one-dimensional.")

    if len(positional_indices) == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(frame):
        raise IndexError("Prediction callback received an out-of-range index.")

    was_training = model.training
    model.eval()

    try:
        subset = frame.iloc[positional_indices]
        inference_dataset = ToxicityInferenceDataset(subset)

        inference_loader = DataLoader(
            inference_dataset,
            batch_size=INFERENCE_BATCH_SIZE,
            shuffle=False,
            num_workers=NUM_WORKERS,
            pin_memory=PIN_MEMORY,
            persistent_workers=False,
            collate_fn=inference_collate,
        )

        predictions = []

        for batch in inference_loader:
            input_ids = batch["input_ids"].to(
                DEVICE,
                non_blocking=PIN_MEMORY,
            )
            attention_mask = batch["attention_mask"].to(
                DEVICE,
                non_blocking=PIN_MEMORY,
            )
            numeric_features = batch["numeric_features"].to(
                DEVICE,
                non_blocking=PIN_MEMORY,
            )

            with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
                probabilities = model.predict_proba(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    numeric_features=numeric_features,
                )

            predictions.append(probabilities.float().cpu().numpy())

        return np.clip(
            np.concatenate(predictions, axis=0).astype(
                np.float64,
                copy=False,
            ),
            0.0,
            1.0,
        )
    finally:
        model.train(was_training)


def stable_generalized_mean(scores, power=-5.0):
    values = np.asarray(scores, dtype=np.float64)
    values = values[np.isfinite(values)]

    if len(values) == 0:
        return float("nan")

    return float(
        np.exp(
            np.mean(
                power * np.log(
                    np.clip(values, np.finfo(np.float64).tiny, 1.0)
                )
            )
            / power
        )
    )


def safe_roc_auc(targets, predictions):
    targets = np.asarray(targets, dtype=np.int8)

    if len(targets) == 0 or np.unique(targets).size < 2:
        return float("nan")

    positive_predictions = np.asarray(predictions, dtype=np.float64)[targets == 1]
    negative_predictions = np.asarray(predictions, dtype=np.float64)[targets == 0]

    comparisons = positive_predictions[:, None] - negative_predictions[None, :]
    return float(
        (
            (comparisons > 0.0).mean()
            + 0.5 * (comparisons == 0.0).mean()
        )
    )


def log_validation_fairness_diagnostics(positional_indices, predictions):
    validation_subset = valid_df.iloc[
        np.asarray(positional_indices, dtype=np.int64)
    ]
    targets = validation_subset["target_binary"].to_numpy(dtype=np.int8)

    subgroup_scores = {}
    bpsn_scores = {}
    bnsp_scores = {}

    for identity_column in EVALUATION_IDENTITIES:
        subgroup_mask = (
            validation_subset[identity_column]
            .fillna(0.0)
            .to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_scores[identity_column] = safe_roc_auc(
            targets[subgroup_mask],
            predictions[subgroup_mask],
        )

        bpsn_mask = (
            (subgroup_mask & (targets == 0))
            | (~subgroup_mask & (targets == 1))
        )
        bpsn_scores[identity_column] = safe_roc_auc(
            targets[bpsn_mask],
            predictions[bpsn_mask],
        )

        bnsp_mask = (
            (subgroup_mask & (targets == 1))
            | (~subgroup_mask & (targets == 0))
        )
        bnsp_scores[identity_column] = safe_roc_auc(
            targets[bnsp_mask],
            predictions[bnsp_mask],
        )

    diagnostics = {
        "overall_auc": safe_roc_auc(targets, predictions),
        "subgroup_auc": subgroup_scores,
        "bpsn_auc": bpsn_scores,
        "bnsp_auc": bnsp_scores,
        "subgroup_generalized_mean_p_minus_5": stable_generalized_mean(
            list(subgroup_scores.values())
        ),
        "bpsn_generalized_mean_p_minus_5": stable_generalized_mean(
            list(bpsn_scores.values())
        ),
        "bnsp_generalized_mean_p_minus_5": stable_generalized_mean(
            list(bnsp_scores.values())
        ),
    }
    print(
        "validation_fairness_diagnostics="
        + json.dumps(diagnostics, sort_keys=True)
    )


def predict_validation(positional_indices):
    predictions = predict_frame(valid_df, positional_indices)
    log_validation_fairness_diagnostics(positional_indices, predictions)
    return predictions


def predict_test(positional_indices):
    return predict_frame(test_df, positional_indices)


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "criterion_state_dict": criterion.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scaler_state_dict": amp_scaler.state_dict(),
            "model_training_mode": bool(model.training),
            "architecture_config": model.architecture_config,
            "max_sequence_length": MAX_SEQUENCE_LENGTH,
            "numeric_feature_columns": list(NUMERIC_FEATURE_COLUMNS),
            "identity_columns": list(IDENTITY_COLUMNS),
        },
        checkpoint_directory / "training_state.pt",
    )

    with open(checkpoint_directory / "inference_config.json", "w") as config_file:
        json.dump(
            {
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "numeric_feature_columns": list(NUMERIC_FEATURE_COLUMNS),
                "identity_columns": list(IDENTITY_COLUMNS),
                "counterfactual_consistency_weight": (
                    COUNTERFACTUAL_CONSISTENCY_WEIGHT
                ),
                "model_architecture": model.architecture_config,
            },
            config_file,
            indent=2,
        )

    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")

    preprocessing_source = WORKING_DIR / "jigsaw_preprocessing_state.pkl"
    if preprocessing_source.exists():
        shutil.copy2(
            preprocessing_source,
            checkpoint_directory / "jigsaw_preprocessing_state.pkl",
        )


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)

    checkpoint = torch.load(
        checkpoint_directory / "training_state.pt",
        map_location=DEVICE,
    )

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    criterion.load_state_dict(checkpoint["criterion_state_dict"])

    if "optimizer_state_dict" in checkpoint:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

    if "scaler_state_dict" in checkpoint:
        amp_scaler.load_state_dict(checkpoint["scaler_state_dict"])

    model.train(bool(checkpoint.get("model_training_mode", True)))


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_training = False
global_optimizer_steps = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    running_loss = 0.0
    completed_updates = 0
    accumulation_batches = 0

    # Clone the sampler state so this audit exactly mirrors, but never changes,
    # the WeightedRandomSampler sequence consumed by the DataLoader.
    sampled_generator = torch.Generator()
    sampled_generator.set_state(train_sampler_generator.get_state())
    sampled_indices = torch.multinomial(
        train_sampler.weights,
        train_sampler.num_samples,
        train_sampler.replacement,
        generator=sampled_generator,
    )
    sampled_identity_cell_counts = np.zeros(
        (
            len(EVALUATION_IDENTITIES),
            len(training_identity_cell_names),
        ),
        dtype=np.int64,
    )
    sampled_row_cursor = 0

    for batch in train_loader:
        primary_batch = move_primary_batch_to_device(batch)

        current_batch_size = int(batch["targets"].shape[0])
        current_sampled_indices = sampled_indices[
            sampled_row_cursor : sampled_row_cursor + current_batch_size
        ].numpy()
        current_identity_cell_ids = training_identity_cell_ids[
            current_sampled_indices
        ]

        for identity_index in range(len(EVALUATION_IDENTITIES)):
            sampled_identity_cell_counts[identity_index] += np.bincount(
                current_identity_cell_ids[:, identity_index],
                minlength=len(training_identity_cell_names),
            )

        sampled_row_cursor += current_batch_size

        model.set_adversarial_scale(
            min(
                1.0,
                max(
                    0.05,
                    (global_optimizer_steps + 1) / 1000.0,
                ),
            )
        )

        with torch.cuda.amp.autocast(enabled=AMP_ENABLED):
            model_outputs = model(
                input_ids=primary_batch["input_ids"],
                attention_mask=primary_batch["attention_mask"],
                numeric_features=primary_batch["numeric_features"],
            )

            loss_components = criterion(
                model_outputs=model_outputs,
                toxicity_targets=primary_batch["targets"],
                identity_targets=primary_batch["identity_targets"],
            )

            total_loss = loss_components["loss"]

            if batch["counterfactual_input_ids"] is not None:
                counterfactual_positions = batch["counterfactual_positions"].to(
                    DEVICE,
                    non_blocking=PIN_MEMORY,
                )

                counterfactual_outputs = model(
                    input_ids=batch["counterfactual_input_ids"].to(
                        DEVICE,
                        non_blocking=PIN_MEMORY,
                    ),
                    attention_mask=batch["counterfactual_attention_mask"].to(
                        DEVICE,
                        non_blocking=PIN_MEMORY,
                    ),
                    numeric_features=primary_batch["numeric_features"].index_select(
                        0,
                        counterfactual_positions,
                    ),
                )

                factual_probabilities = torch.sigmoid(
                    model_outputs["toxicity_logit"].index_select(
                        0,
                        counterfactual_positions,
                    )
                )

                counterfactual_probabilities = torch.sigmoid(
                    counterfactual_outputs["toxicity_logit"]
                )

                consistency_loss = F.smooth_l1_loss(
                    factual_probabilities,
                    counterfactual_probabilities,
                )

                total_loss = (
                    total_loss + COUNTERFACTUAL_CONSISTENCY_WEIGHT * consistency_loss
                )

            scaled_loss = total_loss / GRADIENT_ACCUMULATION_STEPS

        amp_scaler.scale(scaled_loss).backward()

        running_loss += float(total_loss.detach().cpu())
        accumulation_batches += 1

        if accumulation_batches < GRADIENT_ACCUMULATION_STEPS:
            continue

        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        amp_scaler.step(optimizer)
        amp_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        accumulation_batches = 0
        completed_updates += 1
        global_optimizer_steps += 1

        stop_training = session.step()
        if stop_training:
            break

    if not stop_training and accumulation_batches > 0:
        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        amp_scaler.step(optimizer)
        amp_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        completed_updates += 1
        global_optimizer_steps += 1
        stop_training = session.step()

    mean_epoch_loss = running_loss / max(
        1,
        completed_updates * GRADIENT_ACCUMULATION_STEPS,
    )

    sampled_identity_cell_report = {
        identity_column: {
            cell_name: {
                "count": int(
                    sampled_identity_cell_counts[identity_index, cell_index]
                ),
                "proportion": float(
                    sampled_identity_cell_counts[identity_index, cell_index]
                    / max(sampled_row_cursor, 1)
                ),
            }
            for cell_index, cell_name in enumerate(training_identity_cell_names)
        }
        for identity_index, identity_column in enumerate(EVALUATION_IDENTITIES)
    }
    print(
        f"epoch={epoch} updates={completed_updates} "
        f"train_loss={mean_epoch_loss:.6f} "
        f"sampled_identity_cell_counts={sampled_identity_cell_report}"
    )

    if stop_training:
        break

result = session.finish()