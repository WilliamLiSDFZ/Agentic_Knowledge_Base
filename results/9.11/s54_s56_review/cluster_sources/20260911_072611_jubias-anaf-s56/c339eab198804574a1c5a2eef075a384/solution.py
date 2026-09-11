import html
import json
import os
import pickle
import re
import unicodedata

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from engine.candidate_runtime import CandidateSession


SEED = 2027
INPUT_DIR = "./input"
WORKING_DIR = "./working/jigsaw_counterfactual_features"
os.makedirs(WORKING_DIR, exist_ok=True)

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

SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

TRAIN_COLUMNS = ["id", "target", "comment_text"] + IDENTITY_COLUMNS + SUBTYPE_COLUMNS
TEST_COLUMNS = ["id", "comment_text"]

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 4 if torch.cuda.is_available() else 2
INFERENCE_BATCH_SIZE = 8 if torch.cuda.is_available() else 4
GRADIENT_ACCUMULATION_STEPS = 8
NUM_WORKERS = 2
MAX_EPOCHS = 10

CHECKPOINT_FILE = "fair_toxicity_model.pt"
TOKENIZER_DIRNAME = "tokenizer"
CHECKPOINT_METADATA_FILE = "inference_state.json"
SCALER_FILENAME = "style_scaler.pkl"


np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

torch.backends.cuda.matmul.allow_tf32 = True
if hasattr(torch, "set_float32_matmul_precision"):
    torch.set_float32_matmul_precision("high")

session = CandidateSession.from_env()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
amp_enabled = device.type == "cuda"

train_path = os.path.join(INPUT_DIR, "train.csv")
test_path = os.path.join(INPUT_DIR, "test.csv")

available_train_columns = pd.read_csv(train_path, nrows=0).columns.tolist()
required_columns = {"id", "target", "comment_text"}
missing_required_columns = sorted(required_columns - set(available_train_columns))
if missing_required_columns:
    raise ValueError(f"Missing required train columns: {missing_required_columns}")

train_columns_to_read = [
    column for column in TRAIN_COLUMNS if column in available_train_columns
]
train_df = pd.read_csv(train_path, usecols=train_columns_to_read)
test_df = pd.read_csv(test_path, usecols=TEST_COLUMNS)

for column in IDENTITY_COLUMNS:
    if column not in train_df.columns:
        train_df[column] = np.nan

train_df, valid_df, test_df = session.split(train_df, test_df)

url_pattern = re.compile(
    r"(?i)\b(?:"
    r"(?:https?://|www\.)[^\s<>()\[\]{}]+"
    r"|[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}"
    r")"
)
html_tag_pattern = re.compile(r"<[^>\n]+>")
whitespace_pattern = re.compile(r"\s+")
control_pattern = re.compile(r"[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f-\u009f]")

identity_aliases = [
    "african american",
    "black people",
    "white people",
    "native american",
    "middle eastern",
    "gay people",
    "gay person",
    "lesbian",
    "homosexual",
    "transgender",
    "trans woman",
    "trans man",
    "lgbtq",
    "lgbt",
    "bisexual",
    "heterosexual",
    "christianity",
    "christian",
    "muslims",
    "muslim",
    "jewish",
    "judaism",
    "hindu",
    "buddhist",
    "atheist",
    "disabled",
    "disability",
    "mental illness",
    "psychiatric",
    "female",
    "woman",
    "women",
    "male",
    "man",
    "men",
    "girl",
    "girls",
    "boy",
    "boys",
    "asian",
    "latino",
    "latina",
    "latinx",
    "black",
    "white",
]
identity_aliases = sorted(set(identity_aliases), key=len, reverse=True)
identity_pattern = re.compile(
    r"(?i)\b(?:" + "|".join(re.escape(alias) for alias in identity_aliases) + r")\b"
)


def normalize_comment(value):
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = html_tag_pattern.sub(" ", text)
    text = url_pattern.sub(" [URL_OR_EMAIL] ", text)
    text = control_pattern.sub(" ", text)
    text = whitespace_pattern.sub(" ", text).strip()
    return text


def identity_mask_comment(text):
    return identity_pattern.sub(" [IDENTITY] ", text).replace("  ", " ").strip()


def build_raw_style_features(text_series):
    text_series = text_series.fillna("").astype(str)

    char_count = text_series.str.len().to_numpy(dtype=np.float32)
    word_count = text_series.str.count(r"\S+").to_numpy(dtype=np.float32)
    exclamation_count = text_series.str.count(r"!").to_numpy(dtype=np.float32)
    question_count = text_series.str.count(r"\?").to_numpy(dtype=np.float32)
    newline_count = text_series.str.count(r"\n").to_numpy(dtype=np.float32)
    quote_count = text_series.str.count(r"""["']""").to_numpy(dtype=np.float32)
    uppercase_count = text_series.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    alphabetic_count = text_series.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    repeated_punctuation = text_series.str.count(r"([!?.,])\1{2,}").to_numpy(
        dtype=np.float32
    )
    url_marker_count = text_series.str.count(r"\[URL_OR_EMAIL\]").to_numpy(
        dtype=np.float32
    )
    identity_mention_count = text_series.str.count(identity_pattern).to_numpy(
        dtype=np.float32
    )

    uppercase_ratio = uppercase_count / np.maximum(alphabetic_count, 1.0)
    words_per_character = word_count / np.maximum(char_count, 1.0)

    return np.column_stack(
        [
            np.log1p(char_count),
            np.log1p(word_count),
            np.log1p(exclamation_count),
            np.log1p(question_count),
            np.log1p(newline_count),
            np.log1p(quote_count),
            uppercase_ratio,
            repeated_punctuation,
            url_marker_count,
            identity_mention_count,
            words_per_character,
        ]
    ).astype(np.float32)


STYLE_FEATURE_COLUMNS = [
    "style_log_char_count",
    "style_log_word_count",
    "style_log_exclamation_count",
    "style_log_question_count",
    "style_log_newline_count",
    "style_log_quote_count",
    "style_uppercase_ratio",
    "style_repeated_punctuation_count",
    "style_url_or_email_count",
    "style_identity_mention_count",
    "style_words_per_character",
]


def prepare_text_views(frame):
    prepared = frame.copy()
    prepared["model_text"] = prepared["comment_text"].map(normalize_comment)
    prepared["identity_masked_text"] = prepared["model_text"].map(identity_mask_comment)
    prepared["has_identity_lexicon_mention"] = (
        prepared["model_text"].str.contains(identity_pattern, na=False).astype(np.int8)
    )
    prepared["is_empty_comment"] = (prepared["model_text"].str.len() == 0).astype(
        np.int8
    )
    return prepared


train_df = prepare_text_views(train_df)
valid_df = prepare_text_views(valid_df)
test_df = prepare_text_views(test_df)

train_raw_style = build_raw_style_features(train_df["model_text"])
valid_raw_style = build_raw_style_features(valid_df["model_text"])
test_raw_style = build_raw_style_features(test_df["model_text"])

style_scaler = StandardScaler()
train_style = style_scaler.fit_transform(train_raw_style).astype(np.float32)
valid_style = style_scaler.transform(valid_raw_style).astype(np.float32)
test_style = style_scaler.transform(test_raw_style).astype(np.float32)

for feature_index, feature_name in enumerate(STYLE_FEATURE_COLUMNS):
    train_df[feature_name] = train_style[:, feature_index]
    valid_df[feature_name] = valid_style[:, feature_index]
    test_df[feature_name] = test_style[:, feature_index]

for frame in (train_df, valid_df, test_df):
    frame["id"] = frame["id"].astype(str)
    frame["comment_text"] = frame["comment_text"].fillna("").astype(str)

for column in IDENTITY_COLUMNS:
    train_df[column] = pd.to_numeric(train_df[column], errors="coerce").astype(
        np.float32
    )
    valid_df[column] = pd.to_numeric(valid_df[column], errors="coerce").astype(
        np.float32
    )

for column in SUBTYPE_COLUMNS:
    if column in train_df.columns:
        train_df[column] = pd.to_numeric(train_df[column], errors="coerce").astype(
            np.float32
        )
    if column in valid_df.columns:
        valid_df[column] = pd.to_numeric(valid_df[column], errors="coerce").astype(
            np.float32
        )

train_df["target"] = pd.to_numeric(train_df["target"], errors="raise").astype(
    np.float32
)
valid_df["target"] = pd.to_numeric(valid_df["target"], errors="raise").astype(
    np.float32
)

artifact_manifest = {
    "seed": SEED,
    "split_owner": "CandidateSession",
    "text_column": "model_text",
    "counterfactual_text_column": "identity_masked_text",
    "target_column": "target",
    "identity_columns": IDENTITY_COLUMNS,
    "subtype_columns": SUBTYPE_COLUMNS,
    "style_feature_columns": STYLE_FEATURE_COLUMNS,
    "counterfactual_policy": (
        "Identity aliases are replaced only in identity_masked_text; model_text "
        "retains original wording for toxicity semantics and inference."
    ),
    "leakage_policy": (
        "CandidateSession split occurs before preprocessing, and StandardScaler "
        "is fit only on the training partition."
    ),
}

with open(
    os.path.join(WORKING_DIR, "feature_manifest.json"),
    "w",
    encoding="utf-8",
) as file:
    json.dump(artifact_manifest, file, indent=2)

with open(os.path.join(WORKING_DIR, SCALER_FILENAME), "wb") as file:
    pickle.dump(style_scaler, file, protocol=pickle.HIGHEST_PROTOCOL)


"""
DeBERTa-v3-large Usage Example
Base model: microsoft/deberta-v3-large (~435M parameters)
Domain: Natural Language Processing (text classification, NLI, QA, etc.)
Input: tokenized text sequences
Output: Classification logits or hidden embeddings

Reference: https://huggingface.co/microsoft/deberta-v3-large
"""
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
base_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class ConditionalFairToxicityModel(nn.Module):
=======
        identity_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
        super().__init__()
        self.encoder = encoder


class ConditionalFairToxicityModel(nn.Module):
    def __init__(
        self,
        encoder,
        hidden_size,
        subtype_count,
        identity_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
=======
class ConditionalFairToxicityModel(nn.Module):
    def __init__(
        self,
        encoder,
        hidden_size,
        subtype_count,
        identity_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
=======
class ConditionalFairToxicityModel(nn.Module):
=======
        identity_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
        super().__init__()
        self.encoder = encoder


class ConditionalFairToxicityModel(nn.Module):
    def __init__(
        self,
        encoder,
        hidden_size,
        subtype_count,
        identity_count,
        dropout_probability=0.15,
        adversarial_strength=0.08,
    ):
        super().__init__()
        self.encoder = encoder
        self.adversarial_strength = float(adversarial_strength)

        projection_size = hidden_size // 2
        self.representation = nn.Sequential(
            nn.Linear(hidden_size, projection_size),
            nn.LayerNorm(projection_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )
        self.toxicity_head = nn.Linear(projection_size, 1)
        self.subtype_head = nn.Linear(projection_size, subtype_count)

        nn.init.normal_(self.toxicity_head.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.toxicity_head.bias)
        nn.init.normal_(self.subtype_head.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.subtype_head.bias)

    def forward(self, input_ids, attention_mask, **kwargs):
        encoder_kwargs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }
        if "token_type_ids" in kwargs:
            encoder_kwargs["token_type_ids"] = kwargs["token_type_ids"]

        encoder_outputs = self.encoder(**encoder_kwargs)
        hidden_states = encoder_outputs.last_hidden_state

        token_mask = attention_mask.unsqueeze(-1).to(hidden_states.dtype)
        pooled_output = (hidden_states * token_mask).sum(dim=1)
        pooled_output = pooled_output / token_mask.sum(dim=1).clamp_min(1.0)

        representation = self.representation(pooled_output)
        toxicity_logits = self.toxicity_head(representation).squeeze(-1)
        subtype_logits = self.subtype_head(representation)

        return {
            "toxicity_logits": toxicity_logits,
            "toxicity_probability": torch.sigmoid(toxicity_logits),
            "subtype_logits": subtype_logits,
        }


class FairToxicityObjective(nn.Module):
    def __init__(
        self,
        main_identity_weight=1.75,
        subtype_weight=0.30,
        adversarial_weight=0.10,
    ):
        super().__init__()
        self.main_identity_weight = float(main_identity_weight)
        self.subtype_weight = float(subtype_weight)
        self.ranking_weight = 0.15

    @staticmethod
    def _masked_binary_cross_entropy(logits, targets):
        valid_mask = torch.isfinite(targets)
        safe_targets = torch.nan_to_num(targets, nan=0.0).clamp(0.0, 1.0)
        losses = F.binary_cross_entropy_with_logits(
            logits,
            safe_targets,
            reduction="none",
        )
        valid_mask = valid_mask.to(losses.dtype)
        return (losses * valid_mask).sum() / valid_mask.sum().clamp_min(1.0)

    def forward(
        self,
        outputs,
        target,
        subtype_targets=None,
        identity_targets=None,
    ):
        target = target.float().view(-1).clamp(0.0, 1.0)
        main_losses = F.binary_cross_entropy_with_logits(
            outputs["toxicity_logits"],
            target,
            reduction="none",
        )

        if identity_targets is not None:
            valid_identity = torch.isfinite(identity_targets)
            safe_identity = torch.nan_to_num(
                identity_targets,
                nan=0.0,
            ).clamp(0.0, 1.0)
            identity_mention_strength = safe_identity.max(dim=1).values
            has_identity_annotation = valid_identity.any(dim=1).to(main_losses.dtype)
            sample_weights = 1.0 + (
                self.main_identity_weight
                * identity_mention_strength
                * has_identity_annotation
            )
        else:
            sample_weights = torch.ones_like(main_losses)

        main_loss = (
            main_losses * sample_weights
        ).sum() / sample_weights.sum().clamp_min(1.0)

        subtype_loss = outputs["toxicity_logits"].sum() * 0.0
        if subtype_targets is not None:
            subtype_loss = self._masked_binary_cross_entropy(
                outputs["subtype_logits"],
                subtype_targets.float(),
            )

        ranking_loss = outputs["toxicity_logits"].sum() * 0.0
        if identity_targets is not None:
            fully_observed_identity = torch.isfinite(identity_targets).all(dim=1)
            safe_identity = torch.nan_to_num(
                identity_targets.float(),
                nan=0.0,
            ).clamp(0.0, 1.0)
            subgroup_mask = safe_identity.max(dim=1).values >= 0.5
            toxic_mask = target >= 0.5
            benign_mask = ~toxic_mask

            toxic_observed_background = (
                fully_observed_identity & toxic_mask & ~subgroup_mask
            )
            benign_subgroup = fully_observed_identity & benign_mask & subgroup_mask
            toxic_subgroup = fully_observed_identity & toxic_mask & subgroup_mask
            benign_observed_background = (
                fully_observed_identity & benign_mask & ~subgroup_mask
            )

            ranking_terms = []
            logits = outputs["toxicity_logits"]

            if toxic_observed_background.any() and benign_subgroup.any():
                positive_logits = logits[toxic_observed_background]
                negative_logits = logits[benign_subgroup]
                ranking_terms.append(
                    F.softplus(
                        -(positive_logits[:, None] - negative_logits[None, :])
                    ).mean()
                )

            if toxic_subgroup.any() and benign_observed_background.any():
                positive_logits = logits[toxic_subgroup]
                negative_logits = logits[benign_observed_background]
                ranking_terms.append(
                    F.softplus(
                        -(positive_logits[:, None] - negative_logits[None, :])
                    ).mean()
                )

            if ranking_terms:
                ranking_loss = torch.stack(ranking_terms).mean()

        total_loss = (
            main_loss
            + self.subtype_weight * subtype_loss
            + self.ranking_weight * ranking_loss
        )

        return {
            "loss": total_loss,
            "main_loss": main_loss.detach(),
            "subtype_loss": subtype_loss.detach(),
            "ranking_loss": ranking_loss.detach(),
        }


pretrained_encoder = base_classifier.deberta
hidden_size = pretrained_encoder.config.hidden_size

model = ConditionalFairToxicityModel(
    encoder=pretrained_encoder,
    hidden_size=hidden_size,
    subtype_count=len(SUBTYPE_COLUMNS),
    identity_count=len(IDENTITY_COLUMNS),
).to(device)

criterion = FairToxicityObjective()

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")
backbone_decay_parameters = []
backbone_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_backbone_parameter = parameter_name.startswith("encoder.")
    has_no_decay = any(term in parameter_name for term in no_decay_terms)

    if is_backbone_parameter and has_no_decay:
        backbone_no_decay_parameters.append(parameter)
    elif is_backbone_parameter:
        backbone_decay_parameters.append(parameter)
    elif has_no_decay:
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
            "lr": 7e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_parameters,
            "lr": 7e-5,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy()
        self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
        self.identities = frame.loc[:, IDENTITY_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )

        self.has_subtypes = all(column in frame.columns for column in SUBTYPE_COLUMNS)
        self.subtypes = None
        if self.has_subtypes:
            self.subtypes = frame.loc[:, SUBTYPE_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        subtype_values = None if self.subtypes is None else self.subtypes[index]
        return (
            self.texts[index],
            self.targets[index],
            self.identities[index],
            subtype_values,
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, texts):
        self.texts = np.asarray(texts, dtype=object)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return str(self.texts[index])


def tokenize_text_batch(texts):
    return tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )


def training_collate(records):
    texts, targets, identities, subtypes = zip(*records)
    batch = tokenize_text_batch(texts)
    batch["target"] = torch.as_tensor(np.asarray(targets), dtype=torch.float32)
    batch["identity_targets"] = torch.as_tensor(
        np.stack(identities),
        dtype=torch.float32,
    )

    if subtypes[0] is not None:
        batch["subtype_targets"] = torch.as_tensor(
            np.stack(subtypes),
            dtype=torch.float32,
        )
    else:
        batch["subtype_targets"] = None

    return batch


def inference_collate(texts):
    return tokenize_text_batch(texts)


def move_model_inputs_to_device(encoded_batch):
    return {
        key: value.to(device, non_blocking=(device.type == "cuda"))
        for key, value in encoded_batch.items()
    }


def predict_frame_positions(frame, positional_indices):
    positional_indices = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(frame):
        raise IndexError(
            "Prediction callback received out-of-range positional indices."
        )

    selected_texts = (
        frame.iloc[positional_indices]["model_text"].fillna("").astype(str).to_numpy()
    )
    prediction_dataset = ToxicityInferenceDataset(selected_texts)
    prediction_loader = DataLoader(
        prediction_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=(device.type == "cuda"),
        collate_fn=inference_collate,
        persistent_workers=False,
    )

    was_training = model.training
    model.eval()
    prediction_batches = []

    try:
        with torch.inference_mode():
            for encoded_batch in prediction_loader:
                encoded_batch = move_model_inputs_to_device(encoded_batch)
                with torch.cuda.amp.autocast(enabled=amp_enabled):
                    outputs = model(**encoded_batch)
                    probabilities = outputs["toxicity_probability"]
                prediction_batches.append(probabilities.detach().float().cpu().numpy())
    finally:
        model.train(was_training)

    predictions = np.concatenate(prediction_batches).astype(np.float64, copy=False)
    if predictions.shape[0] != positional_indices.shape[0]:
        raise RuntimeError(
            "Inference prediction count does not match requested indices."
        )

    return np.clip(predictions, 0.0, 1.0)


def predict_validation(positional_indices):
    return predict_frame_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_df, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)
    tokenizer_directory = os.path.join(directory, TOKENIZER_DIRNAME)
    os.makedirs(tokenizer_directory, exist_ok=True)

    checkpoint_payload = {
        "model_state_dict": {
            key: value.detach().cpu() for key, value in model.state_dict().items()
        },
        "max_length": MAX_LENGTH,
        "text_column": "model_text",
        "identity_columns": list(IDENTITY_COLUMNS),
        "subtype_columns": list(SUBTYPE_COLUMNS),
        "prediction_semantics": "sigmoid(toxicity_logit)",
        "normalization_version": "nfkc_html_url_identity_mask_v1",
    }
    torch.save(checkpoint_payload, os.path.join(directory, CHECKPOINT_FILE))
    tokenizer.save_pretrained(tokenizer_directory)

    with open(os.path.join(directory, SCALER_FILENAME), "wb") as file:
        pickle.dump(style_scaler, file, protocol=pickle.HIGHEST_PROTOCOL)

    with open(
        os.path.join(directory, CHECKPOINT_METADATA_FILE),
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            {
                "max_length": MAX_LENGTH,
                "text_column": "model_text",
                "prediction_semantics": "sigmoid(toxicity_logit)",
                "identity_columns": list(IDENTITY_COLUMNS),
                "subtype_columns": list(SUBTYPE_COLUMNS),
                "normalization_version": "nfkc_html_url_identity_mask_v1",
            },
            file,
            indent=2,
        )


def load_checkpoint(directory):
    global tokenizer, style_scaler

    checkpoint_path = os.path.join(directory, CHECKPOINT_FILE)
    checkpoint_payload = torch.load(checkpoint_path, map_location="cpu")
    model.load_state_dict(checkpoint_payload["model_state_dict"], strict=True)
    model.to(device)

    restored_max_length = int(checkpoint_payload["max_length"])
    if restored_max_length != MAX_LENGTH:
        raise ValueError(
            f"Checkpoint max length {restored_max_length} does not match "
            f"configured max length {MAX_LENGTH}."
        )

    tokenizer = AutoTokenizer.from_pretrained(
        os.path.join(directory, TOKENIZER_DIRNAME),
        use_fast=True,
    )

    scaler_path = os.path.join(directory, SCALER_FILENAME)
    if os.path.exists(scaler_path):
        with open(scaler_path, "rb") as file:
            style_scaler = pickle.load(file)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

fully_observed_identity = np.isfinite(
    train_df.loc[:, IDENTITY_COLUMNS].to_numpy(dtype=np.float32, copy=True)
).all(axis=1)
train_identity_values = train_df.loc[:, IDENTITY_COLUMNS].to_numpy(
    dtype=np.float32,
    copy=True,
)
train_subgroup_membership = (
    np.nan_to_num(train_identity_values, nan=0.0).max(axis=1) >= 0.5
)
train_toxicity_binary = train_df["target"].to_numpy(dtype=np.float32) >= 0.5

ranking_strata_pools = {
    "benign_subgroup": np.flatnonzero(
        fully_observed_identity
        & ~train_toxicity_binary
        & train_subgroup_membership
    ),
    "toxic_observed_background": np.flatnonzero(
        fully_observed_identity
        & train_toxicity_binary
        & ~train_subgroup_membership
    ),
    "toxic_subgroup": np.flatnonzero(
        fully_observed_identity
        & train_toxicity_binary
        & train_subgroup_membership
    ),
    "benign_observed_background": np.flatnonzero(
        fully_observed_identity
        & ~train_toxicity_binary
        & ~train_subgroup_membership
    ),
}


class ConservativeRankingMixtureBatchSampler(Sampler):
    def __init__(self, dataset_size, ranking_pools, batch_size, seed, ranking_interval=4):
        self.dataset_size = int(dataset_size)
        self.ranking_pools = {
            name: np.asarray(indices, dtype=np.int64).copy()
            for name, indices in ranking_pools.items()
        }
        self.batch_size = int(batch_size)
        self.seed = int(seed)
        self.ranking_interval = int(ranking_interval)
        self.epoch_index = 0
        self.pool_orders = {}
        self.pool_positions = {}
        self.rng = np.random.RandomState(self.seed)

        for name in self.ranking_pools:
            self._refresh_pool(name)

    def _refresh_pool(self, name):
        order = self.ranking_pools[name].copy()
        self.rng.shuffle(order)
        self.pool_orders[name] = order
        self.pool_positions[name] = 0

    def _next_from_pool(self, name):
        if self.pool_positions[name] >= len(self.pool_orders[name]):
            self._refresh_pool(name)

        position = self.pool_positions[name]
        self.pool_positions[name] += 1
        return int(self.pool_orders[name][position])

    def __iter__(self):
        epoch_rng = np.random.RandomState(self.seed + self.epoch_index)
        self.epoch_index += 1
        shuffled_indices = epoch_rng.permutation(self.dataset_size)
        batch_count = len(self)
        ranking_ready = (
            self.batch_size >= 4
            and all(len(indices) > 0 for indices in self.ranking_pools.values())
        )

        for batch_index in range(batch_count):
            if ranking_ready and batch_index % self.ranking_interval == 0:
                ranking_batch = [
                    self._next_from_pool("benign_subgroup"),
                    self._next_from_pool("toxic_observed_background"),
                    self._next_from_pool("toxic_subgroup"),
                    self._next_from_pool("benign_observed_background"),
                ]
                if self.batch_size > 4:
                    start = batch_index * self.batch_size
                    stop = min(start + self.batch_size - 4, self.dataset_size)
                    ranking_batch.extend(shuffled_indices[start:stop].tolist())
                yield ranking_batch
            else:
                start = batch_index * self.batch_size
                stop = min(start + self.batch_size, self.dataset_size)
                yield shuffled_indices[start:stop].tolist()

    def __len__(self):
        return int(np.ceil(self.dataset_size / self.batch_size))


training_dataset = ToxicityTrainingDataset(train_df)
training_batch_sampler = ConservativeRankingMixtureBatchSampler(
    dataset_size=len(training_dataset),
    ranking_pools=ranking_strata_pools,
    batch_size=TRAIN_BATCH_SIZE,
    seed=SEED,
)
training_loader = DataLoader(
    training_dataset,
    batch_sampler=training_batch_sampler,
    num_workers=NUM_WORKERS,
    pin_memory=(device.type == "cuda"),
    collate_fn=training_collate,
    persistent_workers=True,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_requested = False
completed_updates = 0

for epoch_index in range(MAX_EPOCHS):
    if stop_requested:
        break

    model.train()
    epoch_loss_sum = 0.0
    epoch_examples = 0
    epoch_updates = 0

    for batch_index, batch in enumerate(training_loader):
        encoded_batch = {
            key: value
            for key, value in batch.items()
            if key not in {"target", "identity_targets", "subtype_targets"}
        }
        encoded_batch = move_model_inputs_to_device(encoded_batch)

        target_values = batch["target"].to(
            device,
            non_blocking=(device.type == "cuda"),
        )
        identity_values = batch["identity_targets"].to(
            device,
            non_blocking=(device.type == "cuda"),
        )

        subtype_values = batch["subtype_targets"]
        if subtype_values is not None:
            subtype_values = subtype_values.to(
                device,
                non_blocking=(device.type == "cuda"),
            )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(**encoded_batch)
            loss_components = criterion(
                outputs=outputs,
                target=target_values,
                subtype_targets=subtype_values,
                identity_targets=identity_values,
            )
            raw_loss = loss_components["loss"]
            scaled_loss = raw_loss / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()

        batch_size = int(target_values.shape[0])
        epoch_loss_sum += float(raw_loss.detach().item()) * batch_size
        epoch_examples += batch_size

        is_accumulation_boundary = (
            batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0 or (batch_index + 1) == len(
            training_loader
        )

        if is_accumulation_boundary:
            grad_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)

            completed_updates += 1
            epoch_updates += 1
            stop_requested = session.step()

            if stop_requested:
                break

    mean_epoch_loss = epoch_loss_sum / max(epoch_examples, 1)
    print(
        f"Epoch {epoch_index + 1}: loss={mean_epoch_loss:.6f}, "
        f"optimizer_updates={epoch_updates}"
    )

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")