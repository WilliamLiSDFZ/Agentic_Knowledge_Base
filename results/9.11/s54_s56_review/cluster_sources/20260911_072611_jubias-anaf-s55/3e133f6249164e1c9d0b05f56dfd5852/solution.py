import html
import json
import random
import re
import shutil
import unicodedata
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
)

from engine.candidate_runtime import CandidateSession


RANDOM_SEED = 2027
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

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

MAX_LENGTH = 256
TRAIN_BATCH_SIZE = 8
EVAL_BATCH_SIZE = 24
GRADIENT_ACCUMULATION_STEPS = 2
MAX_EPOCHS = 12
NUM_WORKERS = 2

session = CandidateSession.from_env()

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)

train_usecols = ["id", "target", "comment_text"] + IDENTITY_COLUMNS

train_df_raw = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=lambda column: column in train_usecols,
)
test_df_raw = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
)

missing_train_columns = set(train_usecols) - set(train_df_raw.columns)
if missing_train_columns:
    raise ValueError(f"Missing required train columns: {sorted(missing_train_columns)}")

train_df, valid_df, test_df = session.split(train_df_raw, test_df_raw)

if not train_df["id"].is_unique:
    raise ValueError("Training ids must be unique after the runtime split.")

if len(test_df) != len(test_df_raw):
    raise ValueError("Runtime test split unexpectedly changed the number of test rows.")

HTML_BREAK_RE = re.compile(
    r"<\s*(?:br|/p|p|div|/div)\s*/?\s*>",
    flags=re.IGNORECASE,
)
HTML_TAG_RE = re.compile(r"<[^>\n]{1,200}>")
URL_RE = re.compile(
    r"(?:https?://|www\.)[^\s<>\]\[\"']+",
    flags=re.IGNORECASE,
)
EMAIL_RE = re.compile(
    r"\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b",
    flags=re.IGNORECASE,
)
USER_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,}")
CONTROL_RE = re.compile(r"[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f-\u009f]")
WHITESPACE_RE = re.compile(r"\s+")

IDENTITY_SURFACE_RE = re.compile(
    r"\b(?:"
    r"male|female|man|woman|men|women|boy|girl|boys|girls|"
    r"gay|lesbian|homosexual|heterosexual|bisexual|transgender|cisgender|"
    r"christian|jewish|jew|muslim|islamic|islam|hindu|buddhist|atheist|"
    r"black|white|asian|latino|latina|racial|race|"
    r"disabled|disability|autistic|mental(?:\s+)?illness|psychiatric"
    r")\b",
    flags=re.IGNORECASE,
)

COUNTERFACTUAL_MAP = {
    "male": "female",
    "female": "male",
    "man": "woman",
    "woman": "man",
    "men": "women",
    "women": "men",
    "boy": "girl",
    "girl": "boy",
    "boys": "girls",
    "girls": "boys",
    "gay": "straight",
    "lesbian": "straight",
    "homosexual": "heterosexual",
    "heterosexual": "homosexual",
    "christian": "muslim",
    "muslim": "christian",
    "jewish": "muslim",
    "jew": "muslim",
    "black": "white",
    "white": "black",
    "transgender": "cisgender",
    "cisgender": "transgender",
}

COUNTERFACTUAL_RE = re.compile(
    r"\b(?:"
    + "|".join(
        sorted(
            (re.escape(term) for term in COUNTERFACTUAL_MAP),
            key=len,
            reverse=True,
        )
    )
    + r")\b",
    flags=re.IGNORECASE,
)


def normalize_comment(value):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "[empty_comment]"

    text = str(value)
    text = unicodedata.normalize("NFKC", html.unescape(text))
    text = text.replace("\u200b", "").replace("\ufeff", "").replace("\u00ad", "")
    text = CONTROL_RE.sub(" ", text)
    text = HTML_BREAK_RE.sub(" ", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = URL_RE.sub(" urltoken ", text)
    text = EMAIL_RE.sub(" emailtoken ", text)
    text = USER_RE.sub(" usertoken ", text)
    text = WHITESPACE_RE.sub(" ", text).strip()

    return text if text else "[empty_comment]"


def preserve_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement.capitalize()
    return replacement


def counterfactual_identity_swap(text):
    def replace_match(match):
        token = match.group(0)
        replacement = COUNTERFACTUAL_MAP[token.casefold()]
        return preserve_case(token, replacement)

    return COUNTERFACTUAL_RE.sub(replace_match, text)


def build_numeric_features(text_series):
    text = text_series.fillna("[empty_comment]").astype(str)

    char_count = text.str.len().to_numpy(dtype=np.float32)
    word_count = text.str.count(r"\S+").to_numpy(dtype=np.float32)
    alpha_count = text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    upper_count = text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)
    digit_count = text.str.count(r"\d").to_numpy(dtype=np.float32)

    safe_chars = np.maximum(char_count, 1.0)
    safe_words = np.maximum(word_count, 1.0)
    safe_alpha = np.maximum(alpha_count, 1.0)

    feature_frame = pd.DataFrame(
        {
            "log_char_count": np.log1p(char_count),
            "log_word_count": np.log1p(word_count),
            "mean_token_length": char_count / safe_words,
            "alphabetic_ratio": alpha_count / safe_chars,
            "uppercase_alpha_ratio": upper_count / safe_alpha,
            "digit_ratio": digit_count / safe_chars,
            "exclamation_density": (
                100.0 * text.str.count("!").to_numpy(dtype=np.float32) / safe_chars
            ),
            "question_density": (
                100.0 * text.str.count(r"\?").to_numpy(dtype=np.float32) / safe_chars
            ),
            "quote_density": (
                100.0 * text.str.count(r"[\"']").to_numpy(dtype=np.float32) / safe_chars
            ),
            "repeated_punctuation": text.str.count(r"([!?.,])\1{1,}").to_numpy(
                dtype=np.float32
            ),
            "urltoken_count": text.str.count(r"\burltoken\b").to_numpy(
                dtype=np.float32
            ),
            "usertoken_count": text.str.count(r"\busertoken\b").to_numpy(
                dtype=np.float32
            ),
            "all_caps_token_count": text.str.count(r"\b[A-Z]{2,}\b").to_numpy(
                dtype=np.float32
            ),
            "second_person_count": text.str.count(
                r"\b(?:you|your|yours|yourself)\b"
            ).to_numpy(dtype=np.float32),
            "identity_surface_count": text.str.count(IDENTITY_SURFACE_RE).to_numpy(
                dtype=np.float32
            ),
        },
        index=text_series.index,
    )

    return feature_frame.astype(np.float32)


for frame in (train_df, valid_df, test_df):
    frame["model_text"] = frame["comment_text"].map(normalize_comment)

train_numeric_raw = build_numeric_features(train_df["model_text"])
valid_numeric_raw = build_numeric_features(valid_df["model_text"])
test_numeric_raw = build_numeric_features(test_df["model_text"])

feature_columns = train_numeric_raw.columns.tolist()
feature_means = train_numeric_raw.mean(axis=0).astype(np.float32)
feature_scales = train_numeric_raw.std(axis=0, ddof=0).astype(np.float32)
feature_scales = feature_scales.mask(feature_scales < 1e-6, 1.0).astype(np.float32)

train_numeric_features = (
    ((train_numeric_raw - feature_means) / feature_scales)
    .clip(-8.0, 8.0)
    .astype(np.float32)
)
valid_numeric_features = (
    ((valid_numeric_raw - feature_means) / feature_scales)
    .clip(-8.0, 8.0)
    .astype(np.float32)
)
test_numeric_features = (
    ((test_numeric_raw - feature_means) / feature_scales)
    .clip(-8.0, 8.0)
    .astype(np.float32)
)

train_identity_values = train_df[IDENTITY_COLUMNS].apply(
    pd.to_numeric,
    errors="coerce",
)
train_identity_is_annotated = train_identity_values.notna().any(axis=1)
train_identity_present = train_identity_values.fillna(0.0).max(axis=1).ge(0.5)

counterfactual_eligible_mask = (
    train_df["target"].astype(float).lt(0.5)
    & train_identity_is_annotated
    & train_identity_present
)

train_counterfactual_text = train_df["model_text"].copy()
eligible_text = train_df.loc[counterfactual_eligible_mask, "model_text"]
train_counterfactual_text.loc[eligible_text.index] = eligible_text.map(
    counterfactual_identity_swap
)

train_df["counterfactual_text"] = train_counterfactual_text
valid_df["counterfactual_text"] = valid_df["model_text"]
test_df["counterfactual_text"] = test_df["model_text"]

processed_data = {
    "train_df": train_df,
    "valid_df": valid_df,
    "test_df": test_df,
    "train_numeric_features": train_numeric_features.to_numpy(
        dtype=np.float32,
        copy=True,
    ),
    "valid_numeric_features": valid_numeric_features.to_numpy(
        dtype=np.float32,
        copy=True,
    ),
    "test_numeric_features": test_numeric_features.to_numpy(
        dtype=np.float32,
        copy=True,
    ),
    "counterfactual_eligible_mask": counterfactual_eligible_mask.to_numpy(
        dtype=bool,
        copy=True,
    ),
    "identity_columns": IDENTITY_COLUMNS,
    "feature_columns": feature_columns,
}

feature_state = {
    "version": 1,
    "random_seed": RANDOM_SEED,
    "text_column": "model_text",
    "counterfactual_text_column": "counterfactual_text",
    "identity_columns": IDENTITY_COLUMNS,
    "numeric_feature_columns": feature_columns,
    "feature_means": {name: float(feature_means[name]) for name in feature_columns},
    "feature_scales": {name: float(feature_scales[name]) for name in feature_columns},
    "normalization": {
        "unicode": "NFKC",
        "html_unescape": True,
        "replace_urls": "urltoken",
        "replace_emails": "emailtoken",
        "replace_user_handles": "usertoken",
        "preserve_identity_language": True,
    },
    "counterfactual_policy": {
        "train_only": True,
        "eligible_when": "target < 0.5 and an annotated identity mention >= 0.5",
        "purpose": "benign identity-invariance augmentation",
    },
}

with open(WORKING_DIR / "feature_state.json", "w", encoding="utf-8") as state_file:
    json.dump(feature_state, state_file, indent=2, sort_keys=True)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ModernBertForSequenceClassification.from_pretrained(model_id, num_labels=1)

numeric_feature_count = int(processed_data["train_numeric_features"].shape[1])
if numeric_feature_count <= 0:
    raise ValueError("At least one standardized numeric feature is required.")


class CounterfactualFairModernBERT(nn.Module):
    def __init__(self, pretrained_classifier, numeric_dim, dropout=0.15):
        super().__init__()

        self.backbone = pretrained_classifier.model
        hidden_size = int(pretrained_classifier.config.hidden_size)

        self.numeric_adapter = nn.Sequential(
            nn.LayerNorm(numeric_dim),
            nn.Linear(numeric_dim, hidden_size),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, hidden_size),
        )

        self.fusion_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )

        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_size),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )

        nn.init.zeros_(self.numeric_adapter[-1].bias)
        nn.init.normal_(
            self.numeric_adapter[-1].weight,
            mean=0.0,
            std=0.01,
        )

    def forward(self, input_ids, attention_mask, numeric_features):
        backbone_outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        text_features = backbone_outputs.last_hidden_state[:, 0]

        numeric_features = numeric_features.to(
            device=text_features.device,
            dtype=text_features.dtype,
        )

        structural_features = self.numeric_adapter(numeric_features)
        gate = self.fusion_gate(torch.cat([text_features, structural_features], dim=-1))

        fused_features = text_features + gate * structural_features
        return self.classifier(fused_features).squeeze(-1)


class CounterfactualFairnessLoss(nn.Module):
    def __init__(self, consistency_weight=0.50, confidence_weight=0.20):
        super().__init__()
        self.consistency_weight = float(consistency_weight)
        self.confidence_weight = float(confidence_weight)

    @staticmethod
    def _bernoulli_kl(probability_a, probability_b):
        eps = torch.finfo(probability_a.dtype).eps
        probability_a = probability_a.clamp(eps, 1.0 - eps)
        probability_b = probability_b.clamp(eps, 1.0 - eps)

        return probability_a * (probability_a.log() - probability_b.log()) + (
            1.0 - probability_a
        ) * ((1.0 - probability_a).log() - (1.0 - probability_b).log())

    def forward(
        self,
        toxicity_logits,
        toxicity_targets,
        counterfactual_logits=None,
        counterfactual_mask=None,
    ):
        toxicity_targets = toxicity_targets.to(
            device=toxicity_logits.device,
            dtype=toxicity_logits.dtype,
        ).clamp(0.0, 1.0)

        label_confidence = 1.0 + self.confidence_weight * (
            2.0 * (toxicity_targets - 0.5).abs()
        )

        toxicity_loss = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            toxicity_targets,
            reduction="none",
        )
        toxicity_loss = (toxicity_loss * label_confidence).mean()

        if counterfactual_logits is None or counterfactual_mask is None:
            return toxicity_loss

        counterfactual_mask = counterfactual_mask.to(
            device=toxicity_logits.device,
            dtype=torch.bool,
        )

        if not torch.any(counterfactual_mask):
            return toxicity_loss

        original_probability = torch.sigmoid(toxicity_logits[counterfactual_mask])
        swapped_probability = torch.sigmoid(counterfactual_logits[counterfactual_mask])

        symmetric_kl = 0.5 * (
            self._bernoulli_kl(original_probability, swapped_probability)
            + self._bernoulli_kl(swapped_probability, original_probability)
        )

        return toxicity_loss + self.consistency_weight * symmetric_kl.mean()


fair_model = CounterfactualFairModernBERT(
    pretrained_classifier=model,
    numeric_dim=numeric_feature_count,
    dropout=0.15,
)

criterion = CounterfactualFairnessLoss(
    consistency_weight=0.50,
    confidence_weight=0.20,
)

backbone_parameter_ids = {
    id(parameter) for parameter in fair_model.backbone.parameters()
}

optimizer = AdamW(
    [
        {
            "params": [
                parameter
                for parameter in fair_model.parameters()
                if id(parameter) in backbone_parameter_ids
            ],
            "lr": 1.2e-5,
            "weight_decay": 0.01,
        },
        {
            "params": [
                parameter
                for parameter in fair_model.parameters()
                if id(parameter) not in backbone_parameter_ids
            ],
            "lr": 6.0e-5,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

model = fair_model
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()

train_texts = train_df["model_text"].fillna("[empty_comment]").astype(str).tolist()

train_counterfactual_texts = (
    train_df["counterfactual_text"].fillna("[empty_comment]").astype(str).tolist()
)

train_targets = train_df["target"].to_numpy(dtype=np.float32, copy=True)

train_numeric = np.ascontiguousarray(
    processed_data["train_numeric_features"],
    dtype=np.float32,
)

train_counterfactual_mask = np.asarray(
    processed_data["counterfactual_eligible_mask"],
    dtype=bool,
)

valid_numeric = np.ascontiguousarray(
    processed_data["valid_numeric_features"],
    dtype=np.float32,
)

test_numeric = np.ascontiguousarray(
    processed_data["test_numeric_features"],
    dtype=np.float32,
)

if not (
    len(train_texts)
    == len(train_counterfactual_texts)
    == len(train_targets)
    == len(train_numeric)
    == len(train_counterfactual_mask)
):
    raise ValueError(
        "Training texts, labels, numeric features, and masks are misaligned."
    )

if len(valid_numeric) != len(valid_df) or len(test_numeric) != len(test_df):
    raise ValueError(
        "Validation/test numeric features are not aligned with their frames."
    )


class ToxicityTrainingDataset(Dataset):
    def __init__(
        self,
        texts,
        counterfactual_texts,
        targets,
        numeric_features,
        cf_mask,
    ):
        self.texts = texts
        self.counterfactual_texts = counterfactual_texts
        self.targets = targets
        self.numeric_features = numeric_features
        self.cf_mask = cf_mask

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, index):
        return {
            "text": self.texts[index],
            "counterfactual_text": self.counterfactual_texts[index],
            "target": self.targets[index],
            "numeric_features": self.numeric_features[index],
            "counterfactual_mask": self.cf_mask[index],
        }


train_dataset = ToxicityTrainingDataset(
    texts=train_texts,
    counterfactual_texts=train_counterfactual_texts,
    targets=train_targets,
    numeric_features=train_numeric,
    cf_mask=train_counterfactual_mask,
)

loader_generator = torch.Generator()
loader_generator.manual_seed(RANDOM_SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    generator=loader_generator,
    num_workers=NUM_WORKERS,
    pin_memory=(device.type == "cuda"),
    persistent_workers=(NUM_WORKERS > 0),
    prefetch_factor=2,
    drop_last=False,
)

amp_enabled = device.type == "cuda"
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


def autocast_context():
    if amp_enabled:
        return torch.cuda.amp.autocast(enabled=True)
    return nullcontext()


def tokenize_batch(texts):
    encoded = tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )

    return {
        "input_ids": encoded["input_ids"].to(
            device,
            non_blocking=True,
        ),
        "attention_mask": encoded["attention_mask"].to(
            device,
            non_blocking=True,
        ),
    }


def predict_frame_positions(frame, numeric_features, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64).reshape(-1)

    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    if positions.min() < 0 or positions.max() >= len(frame):
        raise IndexError("Inference callback received out-of-range positional indices.")

    previous_training_state = model.training
    model.eval()

    output_predictions = np.empty(len(positions), dtype=np.float64)

    try:
        with torch.inference_mode():
            for start in range(0, len(positions), EVAL_BATCH_SIZE):
                stop = min(start + EVAL_BATCH_SIZE, len(positions))
                batch_positions = positions[start:stop]

                batch_texts = (
                    frame["model_text"]
                    .iloc[batch_positions]
                    .fillna("[empty_comment]")
                    .astype(str)
                    .tolist()
                )

                batch_numeric = torch.from_numpy(
                    np.ascontiguousarray(numeric_features[batch_positions])
                ).to(
                    device,
                    non_blocking=True,
                )

                tokenized = tokenize_batch(batch_texts)

                with autocast_context():
                    logits = model(
                        input_ids=tokenized["input_ids"],
                        attention_mask=tokenized["attention_mask"],
                        numeric_features=batch_numeric,
                    )
                    probabilities = torch.sigmoid(logits)

                output_predictions[start:stop] = (
                    probabilities.float().detach().cpu().numpy()
                )
    finally:
        model.train(previous_training_state)

    return np.clip(output_predictions, 1e-7, 1.0 - 1e-7)


def predict_validation(positional_indices):
    return predict_frame_positions(
        valid_df,
        valid_numeric,
        positional_indices,
    )


def predict_test(positional_indices):
    return predict_frame_positions(
        test_df,
        test_numeric,
        positional_indices,
    )


def save_checkpoint(directory):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "max_length": MAX_LENGTH,
            "numeric_feature_count": int(train_numeric.shape[1]),
            "model_class": model.__class__.__name__,
        },
        checkpoint_dir / "model_state.pt",
    )

    tokenizer.save_pretrained(str(checkpoint_dir / "tokenizer"))
    model.backbone.config.save_pretrained(str(checkpoint_dir / "backbone_config"))

    feature_state_source = WORKING_DIR / "feature_state.json"
    if feature_state_source.exists():
        shutil.copy2(
            feature_state_source,
            checkpoint_dir / "feature_state.json",
        )

    inference_state = {
        "max_length": MAX_LENGTH,
        "numeric_feature_count": int(train_numeric.shape[1]),
        "text_column": "model_text",
        "prediction_transform": "sigmoid",
        "counterfactual_training_only": True,
    }

    with open(
        checkpoint_dir / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(inference_state, handle, indent=2, sort_keys=True)


def load_checkpoint(directory):
    checkpoint_dir = Path(directory)

    checkpoint_payload = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location=device,
    )

    if int(checkpoint_payload["max_length"]) != MAX_LENGTH:
        raise ValueError(
            "Checkpoint max sequence length does not match inference state."
        )

    if int(checkpoint_payload["numeric_feature_count"]) != int(train_numeric.shape[1]):
        raise ValueError("Checkpoint numeric feature dimensionality does not match.")

    model.load_state_dict(
        checkpoint_payload["model_state_dict"],
        strict=True,
    )
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)

stop_training = False
completed_updates = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()

    epoch_loss_sum = 0.0
    epoch_loss_count = 0
    optimizer.zero_grad(set_to_none=True)

    total_batches = len(train_loader)

    for batch_index, batch in enumerate(train_loader, start=1):
        numeric_batch = batch["numeric_features"].to(
            device,
            dtype=torch.float32,
            non_blocking=True,
        )

        target_batch = batch["target"].to(
            device,
            dtype=torch.float32,
            non_blocking=True,
        )

        cf_mask_batch = batch["counterfactual_mask"].to(
            device,
            dtype=torch.bool,
            non_blocking=True,
        )

        original_tokens = tokenize_batch(batch["text"])

        with autocast_context():
            original_logits = model(
                input_ids=original_tokens["input_ids"],
                attention_mask=original_tokens["attention_mask"],
                numeric_features=numeric_batch,
            )

            counterfactual_logits = None

            if torch.any(cf_mask_batch):
                cf_positions = torch.nonzero(
                    cf_mask_batch,
                    as_tuple=False,
                ).squeeze(1)

                cf_text_batch = [
                    batch["counterfactual_text"][int(position)]
                    for position in cf_positions.detach().cpu().tolist()
                ]

                cf_tokens = tokenize_batch(cf_text_batch)
                cf_numeric = numeric_batch.index_select(0, cf_positions)

                swapped_logits = model(
                    input_ids=cf_tokens["input_ids"],
                    attention_mask=cf_tokens["attention_mask"],
                    numeric_features=cf_numeric,
                )

                counterfactual_logits = original_logits.clone()
                counterfactual_logits = counterfactual_logits.index_copy(
                    0,
                    cf_positions,
                    swapped_logits,
                )

            loss = criterion(
                toxicity_logits=original_logits,
                toxicity_targets=target_batch,
                counterfactual_logits=counterfactual_logits,
                counterfactual_mask=(
                    cf_mask_batch if counterfactual_logits is not None else None
                ),
            )

        scaled_loss = loss / GRADIENT_ACCUMULATION_STEPS
        grad_scaler.scale(scaled_loss).backward()

        epoch_loss_sum += float(loss.detach().cpu())
        epoch_loss_count += 1

        should_step = (
            batch_index % GRADIENT_ACCUMULATION_STEPS == 0
            or batch_index == total_batches
        )

        if not should_step:
            continue

        grad_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        grad_scaler.step(optimizer)
        grad_scaler.update()
        optimizer.zero_grad(set_to_none=True)

        completed_updates += 1
        stop_training = session.step()

        if stop_training:
            break

    mean_epoch_loss = epoch_loss_sum / max(epoch_loss_count, 1)
    print(f"epoch={epoch} updates={completed_updates} " f"loss={mean_epoch_loss:.6f}")

    if stop_training:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
