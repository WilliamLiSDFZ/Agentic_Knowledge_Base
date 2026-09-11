import html
import json
import os
import pickle
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset, Sampler
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
)

from engine.candidate_runtime import CandidateSession


RANDOM_SEED = 2025
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

session = CandidateSession.from_env()

input_dir = Path("./input")
raw_train_df = pd.read_csv(input_dir / "train.csv")
raw_test_df = pd.read_csv(input_dir / "test.csv")

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df

for frame in (train_df, valid_df, test_df):
    if "comment_text" not in frame.columns:
        frame["comment_text"] = ""
    frame["comment_text"] = frame["comment_text"].fillna("").astype(str)

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

URL_PATTERN = re.compile(r"(?i)\b(?:https?://|www\.)\S+")
USER_PATTERN = re.compile(r"(?<!\w)@[A-Za-z0-9_]{1,64}")
HTML_TAG_PATTERN = re.compile(r"<[^>\n]{1,200}>")
ZERO_WIDTH_PATTERN = re.compile(r"[\u200b-\u200f\u202a-\u202e\ufeff]")
WHITESPACE_PATTERN = re.compile(r"\s+")

IDENTITY_TERMS = [
    r"\b(?:men|man|male|males|boy|boys|guy|guys|gentlemen)\b",
    r"\b(?:women|woman|female|females|girl|girls|ladies)\b",
    r"\b(?:transgender|transsexual|trans|nonbinary|non-binary)\b",
    r"\b(?:straight|heterosexual)\b",
    r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|lgbt|lgbtq)\b",
    r"\b(?:bisexual|bisexuals)\b",
    r"\b(?:christian|christians|christianity)\b",
    r"\b(?:jew|jews|jewish|judaism)\b",
    r"\b(?:muslim|muslims|islamic|islam)\b",
    r"\b(?:hindu|hindus|hinduism)\b",
    r"\b(?:buddhist|buddhists|buddhism)\b",
    r"\b(?:atheist|atheists|atheism)\b",
    r"\b(?:black|blacks|african-american|african american)\b",
    r"\b(?:white|whites|caucasian)\b",
    r"\b(?:asian|asians)\b",
    r"\b(?:latino|latina|latinx|hispanic)\b",
    r"\b(?:disabled|disability|autistic|autism|mental illness|mentally ill)\b",
]
IDENTITY_PATTERN = "(" + "|".join(IDENTITY_TERMS) + ")"

PROFANITY_OBFUSCATION_PATTERN = re.compile(
    r"(?i)\b(?:f[\W_]*u[\W_]*c[\W_]*k|s[\W_]*h[\W_]*i[\W_]*t|"
    r"b[\W_]*i[\W_]*t[\W_]*c[\W_]*h|a[\W_]*s[\W_]*s[\W_]*h[\W_]*o[\W_]*l[\W_]*e)\b"
)


def normalize_comment(text):
    text = html.unescape(str(text))
    text = unicodedata.normalize("NFKC", text)
    text = ZERO_WIDTH_PATTERN.sub("", text)
    text = URL_PATTERN.sub(" [URL] ", text)
    text = USER_PATTERN.sub(" [USER] ", text)
    text = HTML_TAG_PATTERN.sub(" ", text)
    text = text.replace("\u00a0", " ")
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    return text


def add_engineered_columns(frame):
    normalized = frame["comment_text"].map(normalize_comment)
    frame["model_text"] = normalized

    lower_text = normalized.str.lower()
    frame["identity_masked_text"] = (
        normalized.str.replace(
            IDENTITY_PATTERN,
            " [IDENTITY] ",
            regex=True,
            flags=re.IGNORECASE,
        )
        .str.replace(WHITESPACE_PATTERN, " ", regex=True)
        .str.strip()
    )

    char_count = normalized.str.len().astype(np.float32)
    word_count = normalized.str.count(r"\S+").astype(np.float32)
    alphabetic_count = normalized.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = normalized.str.count(r"[A-Z]").astype(np.float32)

    frame["style_char_count"] = char_count
    frame["style_word_count"] = word_count
    frame["style_mean_word_length"] = (char_count / np.maximum(word_count, 1.0)).astype(
        np.float32
    )
    frame["style_uppercase_ratio"] = (
        uppercase_count / np.maximum(alphabetic_count, 1.0)
    ).astype(np.float32)
    frame["style_digit_ratio"] = (
        normalized.str.count(r"\d").astype(np.float32) / np.maximum(char_count, 1.0)
    ).astype(np.float32)
    frame["style_exclamation_count"] = normalized.str.count("!").astype(np.float32)
    frame["style_question_count"] = normalized.str.count(r"\?").astype(np.float32)
    frame["style_quote_count"] = normalized.str.count(r"""["']""").astype(np.float32)
    frame["style_url_count"] = normalized.str.count(r"\[URL\]").astype(np.float32)
    frame["style_user_count"] = normalized.str.count(r"\[USER\]").astype(np.float32)
    frame["style_repeated_punctuation"] = normalized.str.contains(
        r"[!?.,]{3,}", regex=True
    ).astype(np.float32)
    frame["style_repeated_characters"] = normalized.str.contains(
        r"(?i)(.)\1{3,}", regex=True
    ).astype(np.float32)
    frame["style_obfuscated_profanity"] = normalized.str.contains(
        PROFANITY_OBFUSCATION_PATTERN, regex=True
    ).astype(np.float32)
    frame["style_identity_term_count"] = lower_text.str.count(
        IDENTITY_PATTERN, flags=re.IGNORECASE
    ).astype(np.float32)
    frame["style_has_identity_term"] = (frame["style_identity_term_count"] > 0).astype(
        np.float32
    )

    return frame


train_df = add_engineered_columns(train_df)
valid_df = add_engineered_columns(valid_df)
test_df = add_engineered_columns(test_df)

STYLE_FEATURE_COLUMNS = [
    "style_char_count",
    "style_word_count",
    "style_mean_word_length",
    "style_uppercase_ratio",
    "style_digit_ratio",
    "style_exclamation_count",
    "style_question_count",
    "style_quote_count",
    "style_url_count",
    "style_user_count",
    "style_repeated_punctuation",
    "style_repeated_characters",
    "style_obfuscated_profanity",
    "style_identity_term_count",
    "style_has_identity_term",
]

style_scaler = StandardScaler()
style_scaler.fit(train_df[STYLE_FEATURE_COLUMNS].fillna(0.0))

SCALED_STYLE_FEATURE_COLUMNS = [f"{column}_z" for column in STYLE_FEATURE_COLUMNS]
for frame in (train_df, valid_df, test_df):
    scaled_values = style_scaler.transform(frame[STYLE_FEATURE_COLUMNS].fillna(0.0))
    frame[SCALED_STYLE_FEATURE_COLUMNS] = scaled_values.astype(np.float32)

for frame in (train_df, valid_df):
    if "target" in frame.columns:
        frame["target"] = frame["target"].clip(0.0, 1.0).astype(np.float32)
        frame["target_binary"] = (frame["target"] >= 0.5).astype(np.int8)

available_identity_columns = [
    column for column in IDENTITY_COLUMNS if column in train_df.columns
]
available_evaluated_identity_columns = [
    column for column in EVALUATED_IDENTITY_COLUMNS if column in train_df.columns
]

if available_identity_columns:
    train_identity_targets = train_df[available_identity_columns].astype(np.float32)
    valid_identity_targets = valid_df[
        [column for column in available_identity_columns if column in valid_df.columns]
    ].astype(np.float32)
    train_identity_label_mask = train_identity_targets.notna().astype(np.float32)
    valid_identity_label_mask = valid_identity_targets.notna().astype(np.float32)
else:
    train_identity_targets = pd.DataFrame(index=train_df.index)
    valid_identity_targets = pd.DataFrame(index=valid_df.index)
    train_identity_label_mask = pd.DataFrame(index=train_df.index)
    valid_identity_label_mask = pd.DataFrame(index=valid_df.index)

sparse_text_vectorizer = TfidfVectorizer(
    analyzer="word",
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.995,
    max_features=160_000,
    sublinear_tf=True,
    strip_accents="unicode",
    lowercase=True,
    dtype=np.float32,
)
sparse_text_vectorizer.fit(train_df["model_text"])

model_feature_columns = [
    "model_text",
    "identity_masked_text",
    *SCALED_STYLE_FEATURE_COLUMNS,
]

train_ids = train_df["id"].astype(str).to_numpy()
valid_ids = valid_df["id"].astype(str).to_numpy()
test_ids = test_df["id"].astype(str).to_numpy()

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
backbone_classifier = ModernBertForSequenceClassification.from_pretrained(model_id)


class FairPairModernBERT(nn.Module):
    def __init__(self, pretrained_classifier, num_style_features, dropout=0.15):
        super().__init__()
        self.backbone = pretrained_classifier.model
        hidden_size = self.backbone.config.hidden_size

        self.text_projection = nn.Sequential(
            nn.Linear(hidden_size * 3, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.style_projection = nn.Sequential(
            nn.Linear(num_style_features, 96),
            nn.LayerNorm(96),
            nn.GELU(),
            nn.Dropout(dropout),
        )
        self.gate = nn.Sequential(
            nn.Linear(hidden_size * 2 + 96, hidden_size),
            nn.GELU(),
            nn.Linear(hidden_size, hidden_size),
            nn.Sigmoid(),
        )
        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size + 96, hidden_size // 2),
            nn.LayerNorm(hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )
        self.masked_toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.LayerNorm(hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )

    @staticmethod
    def _pool(outputs, attention_mask):
        hidden_states = outputs.last_hidden_state
        mask = attention_mask.unsqueeze(-1).to(hidden_states.dtype)
        return (hidden_states * mask).sum(dim=1) / mask.sum(dim=1).clamp_min(1.0)

    def encode(self, input_ids, attention_mask):
        outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )
        return self._pool(outputs, attention_mask)

    def forward(
        self,
        input_ids,
        attention_mask,
        masked_input_ids,
        masked_attention_mask,
        style_features,
    ):
        original_embedding = self.encode(input_ids, attention_mask)
        masked_embedding = self.encode(masked_input_ids, masked_attention_mask)

        text_difference = original_embedding - masked_embedding
        text_features = self.text_projection(
            torch.cat(
                [original_embedding, masked_embedding, text_difference],
                dim=-1,
            )
        )
        style_embedding = self.style_projection(style_features.float())

        gate = self.gate(
            torch.cat([original_embedding, masked_embedding, style_embedding], dim=-1)
        )
        fused_embedding = gate * text_features + (1.0 - gate) * original_embedding

        toxicity_logit = self.toxicity_head(
            torch.cat([fused_embedding, style_embedding], dim=-1)
        ).squeeze(-1)
        masked_logit = self.masked_toxicity_head(masked_embedding).squeeze(-1)

        return {
            "logits": toxicity_logit,
            "masked_logits": masked_logit,
        }


class BiasAwareCounterfactualLoss(nn.Module):
    def __init__(
        self,
        benign_identity_weight=3.0,
        toxic_identity_weight=1.5,
        counterfactual_weight=0.35,
        permitted_logit_gap=0.10,
    ):
        super().__init__()
        self.benign_identity_weight = benign_identity_weight
        self.toxic_identity_weight = toxic_identity_weight
        self.counterfactual_weight = counterfactual_weight
        self.permitted_logit_gap = permitted_logit_gap

    def forward(self, outputs, targets, identity_strength):
        targets = targets.float().clamp(0.0, 1.0)
        identity_strength = identity_strength.float().clamp(0.0, 1.0)

        logits = outputs["logits"]
        masked_logits = outputs["masked_logits"]

        benign_identity = identity_strength * (1.0 - targets)
        toxic_identity = identity_strength * targets

        sample_weight = (
            1.0
            + self.benign_identity_weight * benign_identity
            + self.toxic_identity_weight * toxic_identity
        )
        bce_loss = F.binary_cross_entropy_with_logits(
            logits,
            targets,
            reduction="none",
        )
        weighted_bce = (sample_weight * bce_loss).sum() / sample_weight.sum().clamp_min(
            1.0
        )

        excessive_identity_score = F.softplus(
            logits - masked_logits - self.permitted_logit_gap
        )
        counterfactual_loss = (
            benign_identity * excessive_identity_score
        ).sum() / benign_identity.sum().clamp_min(1.0)

        return weighted_bce + self.counterfactual_weight * counterfactual_loss


model = FairPairModernBERT(
    pretrained_classifier=backbone_classifier,
    num_style_features=len(SCALED_STYLE_FEATURE_COLUMNS),
)
del backbone_classifier

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()

criterion = BiasAwareCounterfactualLoss()

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
backbone_decay, backbone_no_decay, head_decay, head_no_decay = [], [], [], []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_backbone = parameter_name.startswith("backbone.")
    uses_weight_decay = not any(term in parameter_name for term in no_decay_terms)

    if is_backbone and uses_weight_decay:
        backbone_decay.append(parameter)
    elif is_backbone:
        backbone_no_decay.append(parameter)
    elif uses_weight_decay:
        head_decay.append(parameter)
    else:
        head_no_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": backbone_decay, "lr": 1.5e-5, "weight_decay": 0.01},
        {"params": backbone_no_decay, "lr": 1.5e-5, "weight_decay": 0.0},
        {"params": head_decay, "lr": 7.5e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 7.5e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
USE_AMP = DEVICE.type == "cuda"
MAX_LENGTH = 192
TRAIN_BATCH_SIZE = 2
INFERENCE_BATCH_SIZE = 8
GRADIENT_ACCUMULATION_STEPS = 8
MAX_EPOCHS = 3
NUM_WORKERS = 2

model.to(DEVICE)
optimizer.zero_grad(set_to_none=True)
scaler = torch.cuda.amp.GradScaler(enabled=USE_AMP)


class CommentPairDataset(Dataset):
    def __init__(self, frame, include_targets=False):
        self.original_texts = frame["model_text"].fillna("").astype(str).tolist()
        self.masked_texts = (
            frame["identity_masked_text"].fillna("").astype(str).tolist()
        )
        self.style_features = (
            frame[SCALED_STYLE_FEATURE_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
        )
        self.include_targets = include_targets

        if include_targets:
            self.targets = (
                frame["target"].fillna(0.0).clip(0.0, 1.0).to_numpy(dtype=np.float32)
            )

            identity_columns_for_loss = [
                column
                for column in available_identity_columns
                if column in frame.columns
            ]

            if identity_columns_for_loss:
                identity_values = (
                    frame[identity_columns_for_loss]
                    .fillna(0.0)
                    .clip(0.0, 1.0)
                    .to_numpy(dtype=np.float32)
                )
                self.identity_strength = identity_values.max(axis=1).astype(np.float32)
            else:
                self.identity_strength = np.zeros(len(frame), dtype=np.float32)

    def __len__(self):
        return len(self.original_texts)

    def __getitem__(self, index):
        if self.include_targets:
            return (
                self.original_texts[index],
                self.masked_texts[index],
                self.style_features[index],
                self.targets[index],
                self.identity_strength[index],
            )

        return (
            self.original_texts[index],
            self.masked_texts[index],
            self.style_features[index],
        )


def pair_collate(batch):
    original_texts = [row[0] for row in batch]
    masked_texts = [row[1] for row in batch]

    original_inputs = tokenizer(
        original_texts,
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )
    masked_inputs = tokenizer(
        masked_texts,
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )

    result = {
        "input_ids": original_inputs["input_ids"],
        "attention_mask": original_inputs["attention_mask"],
        "masked_input_ids": masked_inputs["input_ids"],
        "masked_attention_mask": masked_inputs["attention_mask"],
        "style_features": torch.from_numpy(
            np.stack([row[2] for row in batch]).astype(np.float32, copy=False)
        ),
    }

    if len(batch[0]) == 5:
        result["targets"] = torch.tensor([row[3] for row in batch], dtype=torch.float32)
        result["identity_strength"] = torch.tensor(
            [row[4] for row in batch],
            dtype=torch.float32,
        )

    return result


class FixedOrderSampler(Sampler):
    def __init__(self, order):
        self.order = np.asarray(order, dtype=np.int64)

    def __iter__(self):
        return (int(index) for index in self.order)

    def __len__(self):
        return len(self.order)


def make_fair_curriculum_order(frame, epoch_number):
    target_binary = frame["target"].fillna(0.0).to_numpy(dtype=np.float32) >= 0.5

    curriculum_identity_columns = [
        column
        for column in available_evaluated_identity_columns
        if column in frame.columns
    ]

    if curriculum_identity_columns:
        identity_matrix = (
            frame[curriculum_identity_columns]
            .fillna(0.0)
            .clip(0.0, 1.0)
            .to_numpy(dtype=np.float32)
        )
        has_identity = identity_matrix.max(axis=1) >= 0.5
    else:
        has_identity = np.zeros(len(frame), dtype=bool)

    sampling_weight = np.ones(len(frame), dtype=np.float32)
    sampling_weight[has_identity & ~target_binary] = 4.0
    sampling_weight[has_identity & target_binary] = 2.25
    sampling_weight[~has_identity & target_binary] = 1.35

    rng = np.random.default_rng(RANDOM_SEED + epoch_number)
    exponential_keys = rng.exponential(
        scale=1.0 / sampling_weight.astype(np.float64),
        size=len(sampling_weight),
    )
    return np.argsort(exponential_keys, kind="stable")


def move_batch_to_device(batch):
    return {
        name: tensor.to(DEVICE, non_blocking=USE_AMP) for name, tensor in batch.items()
    }


def predict_from_frame(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)
    if positions.size == 0:
        return np.empty(0, dtype=np.float32)

    subset = frame.iloc[positions]
    inference_dataset = CommentPairDataset(subset, include_targets=False)
    inference_loader = DataLoader(
        inference_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=USE_AMP,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=pair_collate,
    )

    previous_training_mode = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                batch = move_batch_to_device(batch)

                with torch.cuda.amp.autocast(enabled=USE_AMP):
                    outputs = model(
                        input_ids=batch["input_ids"],
                        attention_mask=batch["attention_mask"],
                        masked_input_ids=batch["masked_input_ids"],
                        masked_attention_mask=batch["masked_attention_mask"],
                        style_features=batch["style_features"],
                    )
                    probabilities = torch.sigmoid(outputs["logits"])

                predictions.append(probabilities.float().cpu().numpy())
    finally:
        model.train(previous_training_mode)

    return np.clip(np.concatenate(predictions), 0.0, 1.0).astype(np.float32)


def predict_validation(positional_indices):
    return predict_from_frame(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_from_frame(test_df, positional_indices)


def save_checkpoint(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "model_training_mode": bool(model.training),
            "max_length": MAX_LENGTH,
            "style_feature_columns": list(SCALED_STYLE_FEATURE_COLUMNS),
        },
        directory / "model_state.pt",
    )

    with open(directory / "feature_state.pkl", "wb") as feature_file:
        pickle.dump(
            {
                "style_scaler": style_scaler,
                "style_feature_columns": list(SCALED_STYLE_FEATURE_COLUMNS),
            },
            feature_file,
            protocol=pickle.HIGHEST_PROTOCOL,
        )

    tokenizer.save_pretrained(str(directory / "tokenizer"))

    with open(
        directory / "inference_config.json", "w", encoding="utf-8"
    ) as config_file:
        json.dump(
            {
                "architecture": "FairPairModernBERT",
                "max_length": MAX_LENGTH,
                "style_feature_columns": list(SCALED_STYLE_FEATURE_COLUMNS),
                "probability_postprocessing": "sigmoid(logits), clipped_to_[0,1]",
            },
            config_file,
            indent=2,
        )


def load_checkpoint(directory):
    directory = Path(directory)
    checkpoint = torch.load(directory / "model_state.pt", map_location=DEVICE)
    saved_columns = checkpoint["style_feature_columns"]

    if list(saved_columns) != list(SCALED_STYLE_FEATURE_COLUMNS):
        raise RuntimeError("Checkpoint style-feature schema does not match this run.")

    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.to(DEVICE)
    model.train(bool(checkpoint.get("model_training_mode", False)))


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

train_dataset = CommentPairDataset(train_df, include_targets=True)
stop_training = False
total_optimizer_updates = 0

for epoch in range(MAX_EPOCHS):
    curriculum_order = make_fair_curriculum_order(train_df, epoch)

    train_loader = DataLoader(
        train_dataset,
        batch_size=TRAIN_BATCH_SIZE,
        sampler=FixedOrderSampler(curriculum_order),
        num_workers=NUM_WORKERS,
        pin_memory=USE_AMP,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=pair_collate,
    )

    model.train()
    epoch_losses = []
    epoch_updates = 0

    for batch_index, batch in enumerate(train_loader, start=1):
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=USE_AMP):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                masked_input_ids=batch["masked_input_ids"],
                masked_attention_mask=batch["masked_attention_mask"],
                style_features=batch["style_features"],
            )
            loss = criterion(
                outputs=outputs,
                targets=batch["targets"],
                identity_strength=batch["identity_strength"],
            )

        if not torch.isfinite(loss):
            optimizer.zero_grad(set_to_none=True)
            continue

        scaler.scale(loss / GRADIENT_ACCUMULATION_STEPS).backward()

        is_update_step = (
            batch_index % GRADIENT_ACCUMULATION_STEPS == 0
            or batch_index == len(train_loader)
        )

        if is_update_step:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)

            epoch_losses.append(float(loss.detach().cpu()))
            epoch_updates += 1
            total_optimizer_updates += 1

            stop_training = session.step()
            if stop_training:
                break

    mean_epoch_loss = float(np.mean(epoch_losses)) if epoch_losses else float("nan")
    epoch_status = "partial" if stop_training else "complete"
    print(
        f"Epoch {epoch + 1} ({epoch_status}) - "
        f"loss={mean_epoch_loss:.6f} optimizer_updates={epoch_updates}"
    )

    del train_loader

    if stop_training:
        break

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
