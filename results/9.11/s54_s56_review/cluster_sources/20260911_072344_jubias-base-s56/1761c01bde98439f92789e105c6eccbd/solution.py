import html
import json
import os
import re
import shutil
import unicodedata
from contextlib import nullcontext

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from engine.candidate_runtime import CandidateSession

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

INPUT_DIR = "./input"
WORKING_DIR = "./working"
os.makedirs(WORKING_DIR, exist_ok=True)

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

SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

session = CandidateSession.from_env()

train_header = pd.read_csv(os.path.join(INPUT_DIR, "train.csv"), nrows=0)
train_columns = [
    c
    for c in ["id", "target", "comment_text"] + SUBTYPE_COLUMNS + IDENTITY_COLUMNS
    if c in train_header.columns
]

train_raw = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    usecols=train_columns,
    low_memory=False,
)
test_raw = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    usecols=["id", "comment_text"],
    low_memory=False,
)

train_df, valid_df, test_df = session.split(train_raw, test_raw)
del train_raw, test_raw

for frame in (train_df, valid_df):
    for column in ["target"] + [
        c for c in SUBTYPE_COLUMNS + IDENTITY_COLUMNS if c in frame.columns
    ]:
        frame[column] = (
            pd.to_numeric(frame[column], errors="coerce")
            .fillna(0.0)
            .clip(0.0, 1.0)
            .astype(np.float32)
        )

URL_RE = re.compile(r"(?:(?:https?://|www\.)\S+)", flags=re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", flags=re.IGNORECASE)
USER_RE = re.compile(r"(?<!\w)@\w{2,}(?!\w)")
WHITESPACE_RE = re.compile(r"\s+")
REPEATED_PUNCT_RE = re.compile(r"([!?.,])\1{3,}")

IDENTITY_TERMS = [
    "homosexual",
    "gay",
    "lesbian",
    "bisexual",
    "transgender",
    "transsexual",
    "straight",
    "heterosexual",
    "christian",
    "christianity",
    "muslim",
    "islamic",
    "islam",
    "jewish",
    "jew",
    "judaism",
    "buddhist",
    "buddhism",
    "hindu",
    "hinduism",
    "atheist",
    "black",
    "white",
    "asian",
    "latino",
    "latina",
    "hispanic",
    "african american",
    "native american",
    "disabled",
    "disability",
    "autistic",
    "autism",
    "mental illness",
    "mentally ill",
    "schizophrenic",
    "male",
    "female",
    "woman",
    "women",
    "man",
    "men",
    "girl",
    "girls",
    "boy",
    "boys",
    "mother",
    "father",
    "son",
    "daughter",
]

IDENTITY_TERMS = sorted(set(IDENTITY_TERMS), key=len, reverse=True)
IDENTITY_RE = re.compile(
    r"(?<![a-z0-9_])(?:"
    + "|".join(re.escape(term) for term in IDENTITY_TERMS)
    + r")(?![a-z0-9_])",
    flags=re.IGNORECASE,
)


def normalize_comment(value):
    if pd.isna(value):
        return "[empty_comment]"
    text = unicodedata.normalize("NFKC", html.unescape(str(value)))
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = EMAIL_RE.sub(" [email] ", text)
    text = URL_RE.sub(" [url] ", text)
    text = USER_RE.sub(" [user] ", text)
    text = text.replace("\n", " [newline] ")
    text = text.lower()
    text = REPEATED_PUNCT_RE.sub(r"\1\1\1", text)
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text if text else "[empty_comment]"


def build_unscaled_features(frame):
    raw_text = frame["comment_text"].fillna("").astype(str)
    model_text = raw_text.map(normalize_comment)

    raw_char_count = raw_text.str.len().clip(lower=0).astype(np.float32)
    clean_char_count = model_text.str.len().clip(lower=0).astype(np.float32)
    word_count = model_text.str.count(r"\S+").astype(np.float32)
    uppercase_count = raw_text.str.count(r"[A-Z]").astype(np.float32)
    exclamation_count = raw_text.str.count("!").astype(np.float32)
    question_count = raw_text.str.count(r"\?").astype(np.float32)
    newline_count = raw_text.str.count(r"[\r\n]").astype(np.float32)
    quote_count = raw_text.str.count(r"""["']""").astype(np.float32)
    digit_count = raw_text.str.count(r"\d").astype(np.float32)
    allcaps_word_count = raw_text.str.count(r"\b[A-Z]{2,}\b").astype(np.float32)
    repeated_punctuation_count = raw_text.str.count(r"([!?.,])\1{2,}").astype(
        np.float32
    )
    url_count = model_text.str.count(r"\[url\]").astype(np.float32)
    user_count = model_text.str.count(r"\[user\]").astype(np.float32)
    identity_term_count = model_text.str.count(IDENTITY_RE).astype(np.float32)

    counterfactual_text = (
        model_text.str.replace(IDENTITY_RE, " identity_term ", regex=True)
        .str.replace(WHITESPACE_RE, " ", regex=True)
        .str.strip()
    )

    numeric_features = (
        pd.DataFrame(
            {
                "log_char_count": np.log1p(clean_char_count),
                "log_word_count": np.log1p(word_count),
                "uppercase_ratio": uppercase_count / np.maximum(raw_char_count, 1.0),
                "log_exclamation_count": np.log1p(exclamation_count),
                "log_question_count": np.log1p(question_count),
                "log_newline_count": np.log1p(newline_count),
                "log_quote_count": np.log1p(quote_count),
                "digit_ratio": digit_count / np.maximum(raw_char_count, 1.0),
                "log_allcaps_word_count": np.log1p(allcaps_word_count),
                "log_repeated_punctuation_count": np.log1p(repeated_punctuation_count),
                "log_url_count": np.log1p(url_count),
                "log_user_count": np.log1p(user_count),
                "log_identity_term_count": np.log1p(identity_term_count),
            },
            index=frame.index,
        )
        .replace([np.inf, -np.inf], 0.0)
        .fillna(0.0)
    )

    return model_text, counterfactual_text, numeric_features.astype(np.float32)


train_model_text, train_counterfactual_text, train_numeric = build_unscaled_features(
    train_df
)
valid_model_text, valid_counterfactual_text, valid_numeric = build_unscaled_features(
    valid_df
)
test_model_text, test_counterfactual_text, test_numeric = build_unscaled_features(
    test_df
)

numeric_scaler = StandardScaler()
numeric_scaler.fit(train_numeric)

NUMERIC_FEATURE_COLUMNS = [f"text_feature_{column}" for column in train_numeric.columns]


def assemble_processed_frame(
    frame, model_text, counterfactual_text, numeric_features, has_labels
):
    base_columns = ["id"]
    if has_labels:
        base_columns += ["target"]
        base_columns += [c for c in SUBTYPE_COLUMNS if c in frame.columns]
        base_columns += [c for c in IDENTITY_COLUMNS if c in frame.columns]

    processed = frame.loc[:, base_columns].copy()
    processed["id"] = processed["id"].astype(str)
    processed["model_text"] = model_text.to_numpy()
    processed["counterfactual_text"] = counterfactual_text.to_numpy()

    scaled_features = numeric_scaler.transform(numeric_features).astype(np.float32)
    processed[NUMERIC_FEATURE_COLUMNS] = scaled_features

    if has_labels:
        identity_columns_available = [
            c for c in IDENTITY_COLUMNS if c in processed.columns
        ]
        processed["hard_target"] = (processed["target"] >= 0.5).astype(np.int8)
        processed["any_annotated_identity"] = (
            processed[identity_columns_available].max(axis=1) >= 0.5
        ).astype(np.int8)

    return processed.reset_index(drop=True)


train_df = assemble_processed_frame(
    train_df,
    train_model_text,
    train_counterfactual_text,
    train_numeric,
    has_labels=True,
)
valid_df = assemble_processed_frame(
    valid_df,
    valid_model_text,
    valid_counterfactual_text,
    valid_numeric,
    has_labels=True,
)
test_df = assemble_processed_frame(
    test_df,
    test_model_text,
    test_counterfactual_text,
    test_numeric,
    has_labels=False,
)

feature_state = {
    "numeric_feature_columns": NUMERIC_FEATURE_COLUMNS,
    "identity_columns": IDENTITY_COLUMNS,
    "subtype_columns": SUBTYPE_COLUMNS,
    "normalization_version": "nfkc_html_url_email_user_lower_counterfactual_identity_v1",
    "counterfactual_token": "identity_term",
}

joblib.dump(
    numeric_scaler,
    os.path.join(WORKING_DIR, "text_numeric_scaler.joblib"),
)
with open(
    os.path.join(WORKING_DIR, "feature_state.json"),
    "w",
    encoding="utf-8",
) as feature_file:
    json.dump(feature_state, feature_file, indent=2)

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
sequence_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, strength):
        ctx.strength = float(strength)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, grad_outputs):
        return grad_outputs.neg().mul(ctx.strength), None


class ConditionalIdentityAdversary(nn.Module):
    def __init__(self, hidden_size, identity_count, dropout):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(hidden_size + 1, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, identity_count),
        )

    def forward(self, reversed_features, toxicity_condition):
        features = torch.cat([reversed_features, toxicity_condition], dim=-1)
        return self.network(features)


class FairDebertaToxicityModel(nn.Module):
    def __init__(
        self,
        sequence_classifier_model,
        numeric_feature_names,
        identity_count,
        dropout=0.15,
        adversarial_strength=0.20,
    ):
        super().__init__()
        self.encoder = sequence_classifier_model.deberta
        self.hidden_size = int(sequence_classifier_model.config.hidden_size)
        self.adversarial_strength = float(adversarial_strength)

        kept_numeric_indices = [
            index
            for index, feature_name in enumerate(numeric_feature_names)
            if "identity_term" not in feature_name
        ]
        self.register_buffer(
            "kept_numeric_indices",
            torch.tensor(kept_numeric_indices, dtype=torch.long),
            persistent=True,
        )

        self.expected_raw_numeric_dim = len(numeric_feature_names)
        self.numeric_dim = len(kept_numeric_indices)
        self.text_norm = nn.LayerNorm(self.hidden_size)
        self.text_dropout = nn.Dropout(dropout)

        if self.numeric_dim > 0:
            self.numeric_tower = nn.Sequential(
                nn.LayerNorm(self.numeric_dim),
                nn.Linear(self.numeric_dim, 64),
                nn.GELU(),
                nn.Dropout(dropout),
            )
            fused_dim = self.hidden_size + 64
        else:
            self.numeric_tower = None
            fused_dim = self.hidden_size

        self.toxicity_head = nn.Sequential(
            nn.Linear(fused_dim, self.hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(self.hidden_size // 2, 1),
        )

        self.identity_adversary = ConditionalIdentityAdversary(
            hidden_size=self.hidden_size,
            identity_count=identity_count,
            dropout=dropout,
        )

    def _select_numeric_features(self, numeric_features):
        if numeric_features is None or self.numeric_tower is None:
            return None

        if numeric_features.shape[1] == self.numeric_dim:
            return numeric_features

        if numeric_features.shape[1] != self.expected_raw_numeric_dim:
            raise ValueError(
                "numeric_features must contain all engineered features or "
                "the selected non-identity feature subset."
            )

        return numeric_features.index_select(
            dim=1,
            index=self.kept_numeric_indices.to(numeric_features.device),
        )

    def forward(
        self,
        input_ids,
        attention_mask,
        numeric_features=None,
        conditional_target=None,
    ):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        pooled_text = self.text_dropout(
            self.text_norm(encoder_outputs.last_hidden_state[:, 0])
        )

        selected_numeric = self._select_numeric_features(numeric_features)
        if selected_numeric is not None:
            numeric_embedding = self.numeric_tower(selected_numeric.float())
            fused_features = torch.cat([pooled_text, numeric_embedding], dim=-1)
        else:
            fused_features = pooled_text

        toxicity_logits = self.toxicity_head(fused_features).squeeze(-1)

        if conditional_target is None:
            toxicity_condition = torch.sigmoid(toxicity_logits).detach().unsqueeze(-1)
        else:
            toxicity_condition = conditional_target.float().reshape(-1, 1).detach()

        reversed_text = GradientReversalFunction.apply(
            pooled_text,
            self.adversarial_strength,
        )
        identity_logits = self.identity_adversary(
            reversed_text,
            toxicity_condition,
        )

        return {
            "toxicity_logits": toxicity_logits,
            "identity_logits": identity_logits,
        }


class ConditionalAdversarialToxicityLoss(nn.Module):
    def __init__(self, adversarial_weight=0.10, confidence_weighting=True):
        super().__init__()
        self.adversarial_weight = float(adversarial_weight)
        self.confidence_weighting = bool(confidence_weighting)

    def forward(
        self,
        model_outputs,
        toxicity_targets,
        identity_targets=None,
        identity_annotation_mask=None,
        sample_weights=None,
    ):
        toxicity_targets = toxicity_targets.float().reshape(-1)

        per_example_toxicity = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logits"],
            toxicity_targets,
            reduction="none",
        )

        if self.confidence_weighting:
            annotation_confidence = 0.75 + torch.abs(toxicity_targets - 0.5)
            per_example_toxicity = per_example_toxicity * annotation_confidence

        if sample_weights is not None:
            normalized_weights = sample_weights.float().reshape(-1)
            normalized_weights = (
                normalized_weights / normalized_weights.mean().clamp_min(1e-6)
            )
            toxicity_loss = (per_example_toxicity * normalized_weights).mean()
        else:
            toxicity_loss = per_example_toxicity.mean()

        identity_loss = toxicity_loss.new_zeros(())
        if identity_targets is not None:
            per_identity_loss = F.binary_cross_entropy_with_logits(
                model_outputs["identity_logits"],
                identity_targets.float(),
                reduction="none",
            )

            if identity_annotation_mask is not None:
                annotation_mask = identity_annotation_mask.float()
                identity_loss = (
                    per_identity_loss * annotation_mask
                ).sum() / annotation_mask.sum().clamp_min(1.0)
            else:
                identity_loss = per_identity_loss.mean()

        return {
            "loss": toxicity_loss + self.adversarial_weight * identity_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "identity_adversary_loss": identity_loss.detach(),
        }


model = FairDebertaToxicityModel(
    sequence_classifier_model=sequence_classifier,
    numeric_feature_names=NUMERIC_FEATURE_COLUMNS,
    identity_count=len(IDENTITY_COLUMNS),
    dropout=0.15,
    adversarial_strength=0.20,
)

criterion = ConditionalAdversarialToxicityLoss(
    adversarial_weight=0.10,
    confidence_weighting=True,
)

optimizer = AdamW(
    [
        {
            "params": [p for p in model.encoder.parameters() if p.requires_grad],
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": [
                p
                for name, p in model.named_parameters()
                if p.requires_grad and not name.startswith("encoder.")
            ],
            "lr": 8.0e-5,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

model_design_config = {
    "backbone": "microsoft/deberta-v3-large",
    "pooling": "last_hidden_state_cls",
    "dropout": 0.15,
    "adversarial_strength": 0.20,
    "adversarial_weight": 0.10,
    "identity_count": len(IDENTITY_COLUMNS),
    "raw_numeric_feature_names": NUMERIC_FEATURE_COLUMNS,
    "used_numeric_feature_names": [
        name for name in NUMERIC_FEATURE_COLUMNS if "identity_term" not in name
    ],
}

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
USE_AMP = DEVICE.type == "cuda"
MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 4
INFERENCE_BATCH_SIZE = 16
GRADIENT_ACCUMULATION_STEPS = 8
NUM_WORKERS = 2
MAX_EPOCHS = 6
WARMUP_UPDATES = 400
SCHEDULE_UPDATES = 30000

if USE_AMP:
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

model.to(DEVICE)
if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable()

identity_columns_available = [
    column for column in IDENTITY_COLUMNS if column in train_df.columns
]

if len(identity_columns_available) != len(IDENTITY_COLUMNS):
    raise RuntimeError("All configured identity columns must be present in train_df.")

if not all(column in train_df.columns for column in NUMERIC_FEATURE_COLUMNS):
    raise RuntimeError("Expected processed numeric features are missing from train_df.")

numeric_feature_count = len(NUMERIC_FEATURE_COLUMNS)


class ToxicityTrainingDataset(Dataset):
    def __init__(self, frame):
        self.texts = (
            frame["model_text"].fillna("[empty_comment]").astype(str).to_numpy()
        )
        self.numeric_features = frame.loc[:, NUMERIC_FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
        self.identity_targets = frame.loc[:, identity_columns_available].to_numpy(
            dtype=np.float32,
            copy=True,
        )

        subgroup = (self.identity_targets >= 0.5).any(axis=1)
        toxic = self.targets >= 0.5

        self.sample_weights = np.full(len(frame), 0.85, dtype=np.float32)
        self.sample_weights[toxic & ~subgroup] = 1.35
        self.sample_weights[toxic & subgroup] = 1.80
        self.sample_weights[~toxic & subgroup] = 4.00

        known_identity_annotation = subgroup.astype(np.float32)
        self.identity_annotation_mask = np.repeat(
            known_identity_annotation[:, None],
            len(identity_columns_available),
            axis=1,
        ).astype(np.float32)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return (
            self.texts[index],
            self.numeric_features[index],
            self.targets[index],
            self.identity_targets[index],
            self.identity_annotation_mask[index],
            self.sample_weights[index],
        )


class ToxicityInferenceDataset(Dataset):
    def __init__(self, frame, positional_indices):
        positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
        self.texts = (
            frame["model_text"]
            .iloc[positions]
            .fillna("[empty_comment]")
            .astype(str)
            .to_numpy()
        )
        self.numeric_features = (
            frame.loc[:, NUMERIC_FEATURE_COLUMNS]
            .iloc[positions]
            .to_numpy(dtype=np.float32, copy=True)
        )

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        return self.texts[index], self.numeric_features[index]


def training_collate(batch):
    texts, numeric, targets, identities, annotation_masks, weights = zip(*batch)

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "numeric_features": torch.as_tensor(np.stack(numeric), dtype=torch.float32),
        "targets": torch.as_tensor(targets, dtype=torch.float32),
        "identity_targets": torch.as_tensor(
            np.stack(identities),
            dtype=torch.float32,
        ),
        "identity_annotation_mask": torch.as_tensor(
            np.stack(annotation_masks),
            dtype=torch.float32,
        ),
        "sample_weights": torch.as_tensor(weights, dtype=torch.float32),
    }


def inference_collate(batch):
    texts, numeric = zip(*batch)

    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
        return_token_type_ids=False,
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "numeric_features": torch.as_tensor(np.stack(numeric), dtype=torch.float32),
    }


def predict_frame_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if len(positions) == 0:
        return np.empty(0, dtype=np.float64)

    was_training = model.training
    model.eval()

    prediction_dataset = ToxicityInferenceDataset(frame, positions)
    prediction_loader = DataLoader(
        prediction_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=USE_AMP,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=inference_collate,
    )

    predictions = []
    with torch.inference_mode():
        for batch in prediction_loader:
            input_ids = batch["input_ids"].to(DEVICE, non_blocking=USE_AMP)
            attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=USE_AMP)
            numeric_features = batch["numeric_features"].to(
                DEVICE,
                non_blocking=USE_AMP,
            )

            amp_context = torch.cuda.amp.autocast() if USE_AMP else nullcontext()
            with amp_context:
                outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    numeric_features=numeric_features,
                )
                probabilities = torch.sigmoid(outputs["toxicity_logits"])

            predictions.append(probabilities.float().cpu().numpy())

    if was_training:
        model.train()

    return np.clip(
        np.concatenate(predictions, axis=0).astype(np.float64, copy=False),
        1e-6,
        1.0 - 1e-6,
    )


def predict_validation(positional_indices):
    return predict_frame_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_df, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_length": MAX_LENGTH,
            "numeric_feature_count": numeric_feature_count,
            "numeric_feature_columns": list(NUMERIC_FEATURE_COLUMNS),
            "identity_columns": list(identity_columns_available),
        },
        os.path.join(directory, "fair_deberta_state.pt"),
    )

    tokenizer.save_pretrained(os.path.join(directory, "tokenizer"))

    checkpoint_config = {
        "model_design_config": model_design_config,
        "max_length": MAX_LENGTH,
        "numeric_feature_columns": list(NUMERIC_FEATURE_COLUMNS),
        "identity_columns": list(identity_columns_available),
        "inference_probability_transform": "sigmoid_clipped_1e-6",
    }

    with open(
        os.path.join(directory, "inference_config.json"),
        "w",
        encoding="utf-8",
    ) as config_file:
        json.dump(checkpoint_config, config_file, indent=2, default=str)

    for filename in ("feature_state.json", "text_numeric_scaler.joblib"):
        source_path = os.path.join(WORKING_DIR, filename)
        if os.path.exists(source_path):
            shutil.copy2(source_path, os.path.join(directory, filename))


def load_checkpoint(directory):
    checkpoint_path = os.path.join(directory, "fair_deberta_state.pt")
    checkpoint = torch.load(checkpoint_path, map_location=DEVICE)

    if checkpoint.get("numeric_feature_columns", []) != list(NUMERIC_FEATURE_COLUMNS):
        raise RuntimeError(
            "Checkpoint numeric feature schema does not match inference data."
        )

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(DEVICE)


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
    generator=torch.Generator().manual_seed(2029),
    num_workers=NUM_WORKERS,
    pin_memory=USE_AMP,
    persistent_workers=False,
    prefetch_factor=2,
    collate_fn=training_collate,
)


def learning_rate_multiplier(update_number):
    if update_number < WARMUP_UPDATES:
        return max(0.05, float(update_number + 1) / float(WARMUP_UPDATES))

    progress = min(
        1.0,
        float(update_number - WARMUP_UPDATES)
        / float(max(1, SCHEDULE_UPDATES - WARMUP_UPDATES)),
    )
    return max(0.10, 0.5 * (1.0 + np.cos(np.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
scaler = torch.cuda.amp.GradScaler(enabled=USE_AMP)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_training = False

for _epoch in range(MAX_EPOCHS):
    model.train()

    for batch_index, batch in enumerate(training_loader):
        input_ids = batch["input_ids"].to(DEVICE, non_blocking=USE_AMP)
        attention_mask = batch["attention_mask"].to(DEVICE, non_blocking=USE_AMP)
        numeric_features = batch["numeric_features"].to(
            DEVICE,
            non_blocking=USE_AMP,
        )
        targets = batch["targets"].to(DEVICE, non_blocking=USE_AMP)
        identity_targets = batch["identity_targets"].to(DEVICE, non_blocking=USE_AMP)
        identity_annotation_mask = batch["identity_annotation_mask"].to(
            DEVICE,
            non_blocking=USE_AMP,
        )
        sample_weights = batch["sample_weights"].to(DEVICE, non_blocking=USE_AMP)

        amp_context = torch.cuda.amp.autocast() if USE_AMP else nullcontext()
        with amp_context:
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                numeric_features=numeric_features,
                conditional_target=targets,
            )

            loss_details = criterion(
                model_outputs=outputs,
                toxicity_targets=targets,
                identity_targets=identity_targets,
                identity_annotation_mask=identity_annotation_mask,
                sample_weights=sample_weights,
            )

            scaled_loss = loss_details["loss"] / GRADIENT_ACCUMULATION_STEPS

        scaler.scale(scaled_loss).backward()

        is_last_batch = batch_index + 1 == len(training_loader)
        should_update = (
            (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0
        ) or is_last_batch

        if should_update:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

            if session.step():
                stop_training = True
                break

    if stop_training:
        break

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
