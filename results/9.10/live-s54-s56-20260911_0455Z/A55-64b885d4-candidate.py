import html
import json
import pickle
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import RobustScaler
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

from engine.candidate_runtime import CandidateSession


SEED = 2025
INPUT_DIR = Path("./input")
WORKING_DIR = Path("./working")
SUBMISSION_DIR = Path("./submission")
CHECKPOINT_ROOT = WORKING_DIR / "checkpoints"

WORKING_DIR.mkdir(parents=True, exist_ok=True)
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
CHECKPOINT_ROOT.mkdir(parents=True, exist_ok=True)

np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

session = CandidateSession.from_env()

identity_columns = [
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

evaluated_identity_columns = [
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

train_usecols = {"id", "target", "comment_text", *identity_columns}

train_raw = pd.read_csv(
    INPUT_DIR / "train.csv",
    usecols=lambda column: column in train_usecols,
)
test_raw = pd.read_csv(
    INPUT_DIR / "test.csv",
    usecols=["id", "comment_text"],
)

train_df, valid_df, test_df = session.split(train_raw, test_raw)

identity_patterns = {
    "gender": (
        r"\b(?:man|men|male|males|woman|women|female|females|girl|girls|boy|boys|"
        r"transgender|trans|nonbinary)\b"
    ),
    "sexuality": (
        r"\b(?:gay|gays|lesbian|lesbians|homosexual|homosexuals|bisexual|bisexuals|"
        r"heterosexual|straight|lgbt|lgbtq)\b"
    ),
    "religion": (
        r"\b(?:christian|christians|christianity|jew|jews|jewish|judaism|muslim|"
        r"muslims|islam|islamic|hindu|hindus|hinduism|buddhist|buddhists|atheist|"
        r"atheists)\b"
    ),
    "race": (
        r"\b(?:black|blacks|white|whites|asian|asians|latino|latina|latinos|latinas|"
        r"hispanic|african[\s-]american|caucasian)\b"
    ),
    "disability": (
        r"\b(?:disabled|disability|autistic|autism|mental[\s-]illness|"
        r"mentally[\s-]ill|schizophrenic|depression|depressed|bipolar|blind|deaf)\b"
    ),
}

combined_identity_pattern = re.compile(
    "|".join(f"(?:{pattern})" for pattern in identity_patterns.values()),
    flags=re.IGNORECASE,
)
compiled_identity_patterns = {
    name: re.compile(pattern, flags=re.IGNORECASE)
    for name, pattern in identity_patterns.items()
}

url_pattern = re.compile(r"(?:https?://|www\.)\S+", flags=re.IGNORECASE)
email_pattern = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", flags=re.IGNORECASE)
ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
number_pattern = re.compile(r"\b\d+(?:[.,:/-]\d+)*\b")
whitespace_pattern = re.compile(r"\s+")
html_tag_pattern = re.compile(r"<[^>]+>")
repeated_punctuation_pattern = re.compile(r"([!?.,])\1{2,}")
word_pattern = re.compile(r"\b[\w']+\b", flags=re.UNICODE)


def normalize_comment(value):
    text = "" if pd.isna(value) else str(value)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", " ").replace("\ufeff", " ")
    text = html_tag_pattern.sub(" ", text)
    text = url_pattern.sub(" [URL] ", text)
    text = email_pattern.sub(" [EMAIL] ", text)
    text = ip_pattern.sub(" [IP] ", text)
    text = number_pattern.sub(" [NUM] ", text)
    text = repeated_punctuation_pattern.sub(r"\1\1", text)
    text = whitespace_pattern.sub(" ", text).strip()
    return text


def mask_identity_mentions(text):
    return combined_identity_pattern.sub(" [IDENTITY] ", text)


def make_text_features(frame):
    raw_text = frame["comment_text"].fillna("").astype(str)
    normalized = raw_text.map(normalize_comment)

    raw_length = raw_text.str.len().clip(lower=0)
    word_count = normalized.map(lambda value: len(word_pattern.findall(value)))
    alpha_count = raw_text.map(
        lambda value: sum(character.isalpha() for character in value)
    )
    uppercase_count = raw_text.map(
        lambda value: sum(character.isupper() for character in value)
    )

    output = pd.DataFrame(index=frame.index)
    output["model_text"] = normalized
    output["identity_masked_text"] = normalized.map(mask_identity_mentions)
    output["char_length"] = np.log1p(raw_length).astype(np.float32)
    output["word_count"] = np.log1p(word_count).astype(np.float32)
    output["mean_word_length"] = (
        (raw_length / np.maximum(word_count, 1)).clip(0, 100).astype(np.float32)
    )
    output["uppercase_ratio"] = (
        (uppercase_count / np.maximum(alpha_count, 1)).clip(0, 1).astype(np.float32)
    )
    output["exclamation_count"] = np.log1p(raw_text.str.count("!")).astype(np.float32)
    output["question_count"] = np.log1p(raw_text.str.count(r"\?")).astype(np.float32)
    output["newline_count"] = np.log1p(raw_text.str.count(r"[\r\n]")).astype(np.float32)
    output["quote_count"] = np.log1p(raw_text.str.count(r"""["']""")).astype(np.float32)
    output["url_count"] = np.log1p(raw_text.str.count(url_pattern)).astype(np.float32)
    output["all_caps_token_count"] = np.log1p(
        raw_text.map(lambda value: len(re.findall(r"\b[A-Z]{2,}\b", value)))
    ).astype(np.float32)
    output["repeated_punctuation_count"] = np.log1p(
        raw_text.str.count(repeated_punctuation_pattern)
    ).astype(np.float32)

    for category, pattern in compiled_identity_patterns.items():
        output[f"lexical_identity_{category}"] = normalized.str.contains(
            pattern,
            na=False,
        ).astype(np.float32)

    output["lexical_identity_any"] = normalized.str.contains(
        combined_identity_pattern,
        na=False,
    ).astype(np.float32)
    output["lexical_identity_mentions"] = np.log1p(
        normalized.str.count(combined_identity_pattern)
    ).astype(np.float32)

    return output


def prepare_partition(frame, include_labels):
    prepared = frame[["id"]].copy()

    if include_labels:
        prepared["target"] = (
            pd.to_numeric(frame["target"], errors="coerce")
            .fillna(0.0)
            .astype(np.float32)
        )

        for column in identity_columns:
            values = frame[column] if column in frame.columns else 0.0
            prepared[column] = (
                pd.to_numeric(values, errors="coerce").fillna(0.0).astype(np.float32)
            )

        prepared["identity_annotation_available"] = (
            prepared[identity_columns].sum(axis=1) > 0
        ).astype(np.float32)
        prepared["identity_label_any"] = (
            prepared[identity_columns].max(axis=1) >= 0.5
        ).astype(np.float32)
        prepared["identity_label_count"] = (
            (prepared[identity_columns] >= 0.5).sum(axis=1).astype(np.float32)
        )

    text_features = make_text_features(frame)

    return pd.concat(
        [
            prepared.reset_index(drop=True),
            text_features.reset_index(drop=True),
        ],
        axis=1,
    )


train_processed = prepare_partition(train_df, include_labels=True)
valid_processed = prepare_partition(valid_df, include_labels=True)
test_processed = prepare_partition(test_df, include_labels=False)

numeric_feature_columns = [
    "char_length",
    "word_count",
    "mean_word_length",
    "uppercase_ratio",
    "exclamation_count",
    "question_count",
    "newline_count",
    "quote_count",
    "url_count",
    "all_caps_token_count",
    "repeated_punctuation_count",
    "lexical_identity_gender",
    "lexical_identity_sexuality",
    "lexical_identity_religion",
    "lexical_identity_race",
    "lexical_identity_disability",
    "lexical_identity_any",
    "lexical_identity_mentions",
]

numeric_scaler = RobustScaler(quantile_range=(5.0, 95.0))

train_processed[numeric_feature_columns] = numeric_scaler.fit_transform(
    train_processed[numeric_feature_columns]
).astype(np.float32)

valid_processed[numeric_feature_columns] = numeric_scaler.transform(
    valid_processed[numeric_feature_columns]
).astype(np.float32)

test_processed[numeric_feature_columns] = numeric_scaler.transform(
    test_processed[numeric_feature_columns]
).astype(np.float32)

artifacts = {
    "seed": SEED,
    "numeric_feature_columns": numeric_feature_columns,
    "identity_columns": identity_columns,
    "evaluated_identity_columns": evaluated_identity_columns,
    "text_column": "model_text",
    "counterfactual_text_column": "identity_masked_text",
    "numeric_scaler": numeric_scaler,
}

with open(WORKING_DIR / "feature_artifacts.pkl", "wb") as artifact_file:
    pickle.dump(artifacts, artifact_file, protocol=pickle.HIGHEST_PROTOCOL)

with open(
    WORKING_DIR / "feature_manifest.json", "w", encoding="utf-8"
) as manifest_file:
    json.dump(
        {
            "text_column": artifacts["text_column"],
            "counterfactual_text_column": artifacts["counterfactual_text_column"],
            "numeric_feature_columns": numeric_feature_columns,
            "identity_columns": identity_columns,
            "evaluated_identity_columns": evaluated_identity_columns,
            "train_rows": int(len(train_processed)),
            "valid_rows": int(len(valid_processed)),
            "test_rows": int(len(test_processed)),
        },
        manifest_file,
        indent=2,
    )

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)

MODEL_MAX_LENGTH = 256
NUMERIC_FEATURE_DIM = len(numeric_feature_columns)
EVALUATED_IDENTITY_DIM = len(evaluated_identity_columns)
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class CounterfactualGatedModernBert(nn.Module):
    def __init__(self, backbone, numeric_feature_dim, dropout=0.15):
        super().__init__()
        self.backbone = backbone
        self.numeric_feature_dim = int(numeric_feature_dim)

        gate_input_dim = self.numeric_feature_dim + 3
        self.gate_network = nn.Sequential(
            nn.LayerNorm(gate_input_dim),
            nn.Linear(gate_input_dim, 64),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
        )
        self.numeric_head = nn.Sequential(
            nn.LayerNorm(self.numeric_feature_dim),
            nn.Linear(self.numeric_feature_dim, 32),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(32, 1),
        )

        nn.init.zeros_(self.gate_network[-1].weight)
        nn.init.constant_(self.gate_network[-1].bias, 0.65)
        nn.init.zeros_(self.numeric_head[-1].bias)

    def _encode_logits(self, input_ids, attention_mask):
        return self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        ).logits.squeeze(-1)

    def forward(
        self,
        full_input_ids,
        full_attention_mask,
        masked_input_ids,
        masked_attention_mask,
        numeric_features,
    ):
        full_logits = self._encode_logits(full_input_ids, full_attention_mask)
        masked_logits = self._encode_logits(masked_input_ids, masked_attention_mask)

        gate_inputs = torch.cat(
            [
                numeric_features,
                full_logits.unsqueeze(-1),
                masked_logits.unsqueeze(-1),
                (full_logits - masked_logits).abs().unsqueeze(-1),
            ],
            dim=-1,
        )

        full_context_gate = torch.sigmoid(self.gate_network(gate_inputs).squeeze(-1))

        blended_logits = (
            full_context_gate * full_logits + (1.0 - full_context_gate) * masked_logits
        )

        final_logits = blended_logits + 0.15 * self.numeric_head(
            numeric_features
        ).squeeze(-1)

        return {
            "logits": final_logits,
            "probabilities": torch.sigmoid(final_logits),
            "full_logits": full_logits,
            "masked_logits": masked_logits,
            "full_context_gate": full_context_gate,
        }


class BiasRobustCounterfactualLoss(nn.Module):
    def __init__(
        self,
        robust_weight=0.45,
        counterfactual_weight=0.20,
        smoothmax_temperature=0.20,
    ):
        super().__init__()
        self.robust_weight = float(robust_weight)
        self.counterfactual_weight = float(counterfactual_weight)
        self.smoothmax_temperature = float(smoothmax_temperature)

    @staticmethod
    def _masked_mean(values, mask):
        if bool(mask.any()):
            return values[mask].mean()
        return None

    def forward(self, model_output, targets, identity_targets):
        binary_targets = (targets >= 0.5).to(dtype=model_output["logits"].dtype)

        per_example_bce = F.binary_cross_entropy_with_logits(
            model_output["logits"],
            binary_targets,
            reduction="none",
        )
        primary_loss = per_example_bce.mean()

        identity_targets = identity_targets[:, :EVALUATED_IDENTITY_DIM]
        identity_mentions = identity_targets >= 0.5
        slice_losses = []

        for identity_index in range(identity_mentions.shape[1]):
            subgroup = identity_mentions[:, identity_index]
            background = ~subgroup

            subgroup_loss = self._masked_mean(per_example_bce, subgroup)
            if subgroup_loss is not None:
                slice_losses.append(subgroup_loss)

            bpsn_mask = (subgroup & (binary_targets == 0)) | (
                background & (binary_targets == 1)
            )
            bpsn_loss = self._masked_mean(per_example_bce, bpsn_mask)
            if bpsn_loss is not None:
                slice_losses.append(bpsn_loss)

            bnsp_mask = (subgroup & (binary_targets == 1)) | (
                background & (binary_targets == 0)
            )
            bnsp_loss = self._masked_mean(per_example_bce, bnsp_mask)
            if bnsp_loss is not None:
                slice_losses.append(bnsp_loss)

        if slice_losses:
            grouped_losses = torch.stack(slice_losses)
            temperature = self.smoothmax_temperature
            robust_loss = temperature * torch.logsumexp(
                grouped_losses / temperature,
                dim=0,
            ) - temperature * torch.log(
                torch.tensor(
                    float(grouped_losses.numel()),
                    dtype=grouped_losses.dtype,
                    device=grouped_losses.device,
                )
            )
        else:
            robust_loss = primary_loss.new_zeros(())

        benign_identity = identity_mentions.any(dim=1) & (binary_targets == 0)

        if bool(benign_identity.any()):
            counterfactual_loss = F.mse_loss(
                torch.sigmoid(model_output["full_logits"][benign_identity]),
                torch.sigmoid(model_output["masked_logits"][benign_identity]),
            )
        else:
            counterfactual_loss = primary_loss.new_zeros(())

        return (
            primary_loss
            + self.robust_weight * robust_loss
            + self.counterfactual_weight * counterfactual_loss
        )


backbone = ModernBertForSequenceClassification.from_pretrained(
    model_id,
    num_labels=1,
    ignore_mismatched_sizes=True,
)

model = CounterfactualGatedModernBert(
    backbone=backbone,
    numeric_feature_dim=NUMERIC_FEATURE_DIM,
).to(DEVICE)

criterion = BiasRobustCounterfactualLoss(
    robust_weight=0.45,
    counterfactual_weight=0.20,
    smoothmax_temperature=0.20,
)

backbone_parameters = []
task_head_parameters = []

for parameter_name, parameter in model.named_parameters():
    if parameter_name.startswith("backbone."):
        backbone_parameters.append(parameter)
    else:
        task_head_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": backbone_parameters,
            "lr": 1.25e-5,
            "weight_decay": 0.01,
        },
        {
            "params": task_head_parameters,
            "lr": 2.5e-4,
            "weight_decay": 0.02,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

amp_scaler = torch.cuda.amp.GradScaler(enabled=torch.cuda.is_available())

train_processed = train_processed.reset_index(drop=True)
valid_processed = valid_processed.reset_index(drop=True)
test_processed = test_processed.reset_index(drop=True)

if len(train_processed) != len(train_df):
    raise ValueError("Training processed features are not aligned with train_df.")
if len(valid_processed) != len(valid_df):
    raise ValueError("Validation processed features are not aligned with valid_df.")
if len(test_processed) != len(test_df):
    raise ValueError("Test processed features are not aligned with test_df.")


class ToxicityCounterfactualDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.full_text = frame["model_text"].fillna("").astype(str).to_numpy()
        self.masked_text = (
            frame["identity_masked_text"].fillna("").astype(str).to_numpy()
        )
        self.numeric_features = (
            frame[numeric_feature_columns]
            .fillna(0.0)
            .to_numpy(dtype=np.float32, copy=True)
        )
        self.include_labels = bool(include_labels)

        if self.include_labels:
            self.targets = (
                pd.to_numeric(frame["target"], errors="coerce")
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )
            self.identity_targets = (
                frame[evaluated_identity_columns]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )
        else:
            self.targets = None
            self.identity_targets = None

    def __len__(self):
        return len(self.full_text)

    def __getitem__(self, index):
        example = {
            "full_text": self.full_text[index],
            "masked_text": self.masked_text[index],
            "numeric_features": self.numeric_features[index],
        }

        if self.include_labels:
            example["target"] = self.targets[index]
            example["identity_targets"] = self.identity_targets[index]

        return example


class DualTextBatchCollator:
    def __init__(self, tokenizer_object, max_length):
        self.tokenizer_object = tokenizer_object
        self.max_length = int(max_length)

    def __call__(self, examples):
        full_texts = [example["full_text"] for example in examples]
        masked_texts = [example["masked_text"] for example in examples]

        full_encoded = self.tokenizer_object(
            full_texts,
            max_length=self.max_length,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )

        masked_encoded = self.tokenizer_object(
            masked_texts,
            max_length=self.max_length,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )

        batch = {
            "full_input_ids": full_encoded["input_ids"],
            "full_attention_mask": full_encoded["attention_mask"],
            "masked_input_ids": masked_encoded["input_ids"],
            "masked_attention_mask": masked_encoded["attention_mask"],
            "numeric_features": torch.tensor(
                np.stack([example["numeric_features"] for example in examples]),
                dtype=torch.float32,
            ),
        }

        if "target" in examples[0]:
            batch["targets"] = torch.tensor(
                np.asarray([example["target"] for example in examples]),
                dtype=torch.float32,
            )
            batch["identity_targets"] = torch.tensor(
                np.stack([example["identity_targets"] for example in examples]),
                dtype=torch.float32,
            )

        return batch


collator = DualTextBatchCollator(tokenizer, MODEL_MAX_LENGTH)
pin_memory = torch.cuda.is_available()
train_batch_size = 4 if torch.cuda.is_available() else 1
inference_batch_size = 8 if torch.cuda.is_available() else 1
num_workers = 2

train_dataset = ToxicityCounterfactualDataset(
    train_processed,
    include_labels=True,
)

train_loader = DataLoader(
    train_dataset,
    batch_size=train_batch_size,
    shuffle=True,
    num_workers=num_workers,
    pin_memory=pin_memory,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=collator,
    drop_last=False,
)


def move_batch_to_device(batch):
    return {
        key: value.to(DEVICE, non_blocking=pin_memory) for key, value in batch.items()
    }


@torch.no_grad()
def predict_frame_positions(frame, positional_indices):
    positional_indices = np.asarray(
        positional_indices,
        dtype=np.int64,
    ).reshape(-1)

    if positional_indices.size == 0:
        return np.empty(0, dtype=np.float64)

    if positional_indices.min() < 0 or positional_indices.max() >= len(frame):
        raise IndexError(
            "Prediction callback received out-of-range positional indices."
        )

    ordered_frame = frame.iloc[positional_indices].reset_index(drop=True)

    prediction_dataset = ToxicityCounterfactualDataset(
        ordered_frame,
        include_labels=False,
    )

    prediction_loader = DataLoader(
        prediction_dataset,
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=pin_memory,
        persistent_workers=True,
        prefetch_factor=2,
        collate_fn=collator,
        drop_last=False,
    )

    previous_mode = model.training
    model.eval()
    prediction_chunks = []

    try:
        for batch in prediction_loader:
            batch = move_batch_to_device(batch)

            with torch.cuda.amp.autocast(enabled=torch.cuda.is_available()):
                model_output = model(
                    full_input_ids=batch["full_input_ids"],
                    full_attention_mask=batch["full_attention_mask"],
                    masked_input_ids=batch["masked_input_ids"],
                    masked_attention_mask=batch["masked_attention_mask"],
                    numeric_features=batch["numeric_features"],
                )

            prediction_chunks.append(
                model_output["probabilities"].float().cpu().numpy()
            )
    finally:
        model.train(previous_mode)

    predictions = np.concatenate(prediction_chunks).astype(
        np.float64,
        copy=False,
    )

    if len(predictions) != len(positional_indices):
        raise RuntimeError("Prediction callback returned an incorrect number of rows.")

    return np.clip(predictions, 1e-7, 1.0 - 1e-7)


def predict_validation(positional_indices):
    return predict_frame_positions(valid_processed, positional_indices)


def predict_test(positional_indices):
    return predict_frame_positions(test_processed, positional_indices)


training_state = {
    "epoch": 0,
    "optimizer_updates": 0,
}


def save_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_directory.mkdir(parents=True, exist_ok=True)

    model_state_cpu = {
        name: tensor.detach().cpu() for name, tensor in model.state_dict().items()
    }

    torch.save(
        {
            "model_state_dict": model_state_cpu,
            "optimizer_state_dict": optimizer.state_dict(),
            "amp_scaler_state_dict": amp_scaler.state_dict(),
            "training_state": dict(training_state),
            "model_id": model_id,
            "max_length": int(MODEL_MAX_LENGTH),
            "numeric_feature_columns": list(numeric_feature_columns),
            "evaluated_identity_columns": list(evaluated_identity_columns),
        },
        checkpoint_directory / "model_state.pt",
    )

    model.backbone.config.save_pretrained(checkpoint_directory / "backbone_config")
    tokenizer.save_pretrained(checkpoint_directory / "tokenizer")

    with open(
        checkpoint_directory / "feature_artifacts.pkl",
        "wb",
    ) as artifact_file:
        pickle.dump(
            {
                "artifacts": artifacts,
                "numeric_feature_columns": list(numeric_feature_columns),
                "evaluated_identity_columns": list(evaluated_identity_columns),
                "model_max_length": int(MODEL_MAX_LENGTH),
            },
            artifact_file,
            protocol=pickle.HIGHEST_PROTOCOL,
        )

    with open(
        checkpoint_directory / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as inference_file:
        json.dump(
            {
                "model_id": model_id,
                "model_max_length": int(MODEL_MAX_LENGTH),
                "numeric_feature_dim": int(NUMERIC_FEATURE_DIM),
                "evaluated_identity_dim": int(EVALUATED_IDENTITY_DIM),
                "numeric_feature_columns": list(numeric_feature_columns),
                "evaluated_identity_columns": list(evaluated_identity_columns),
            },
            inference_file,
            indent=2,
        )


def load_checkpoint(directory):
    checkpoint_directory = Path(directory)
    checkpoint_path = checkpoint_directory / "model_state.pt"

    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint is missing: {checkpoint_path}")

    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)

    if "optimizer_state_dict" in checkpoint:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

    if "amp_scaler_state_dict" in checkpoint:
        amp_scaler.load_state_dict(checkpoint["amp_scaler_state_dict"])

    if "training_state" in checkpoint:
        training_state.clear()
        training_state.update(checkpoint["training_state"])

    model.to(DEVICE)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

stop_training = False
max_epochs = 3

for epoch in range(max_epochs):
    if stop_training:
        break

    model.train()
    epoch_loss_sum = 0.0
    epoch_updates = 0

    for batch in train_loader:
        batch = move_batch_to_device(batch)
        optimizer.zero_grad(set_to_none=True)

        with torch.cuda.amp.autocast(enabled=torch.cuda.is_available()):
            model_output = model(
                full_input_ids=batch["full_input_ids"],
                full_attention_mask=batch["full_attention_mask"],
                masked_input_ids=batch["masked_input_ids"],
                masked_attention_mask=batch["masked_attention_mask"],
                numeric_features=batch["numeric_features"],
            )

            loss = criterion(
                model_output=model_output,
                targets=batch["targets"],
                identity_targets=batch["identity_targets"],
            )

        if not torch.isfinite(loss):
            raise FloatingPointError("Encountered a non-finite training loss.")

        amp_scaler.scale(loss).backward()
        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        amp_scaler.step(optimizer)
        amp_scaler.update()

        training_state["optimizer_updates"] += 1
        epoch_updates += 1
        epoch_loss_sum += float(loss.detach().cpu())

        stop_training = bool(session.step())
        if stop_training:
            break

    training_state["epoch"] = epoch + 1
    mean_epoch_loss = epoch_loss_sum / max(epoch_updates, 1)

    print(
        f"Epoch {epoch + 1}/{max_epochs} "
        f"updates={epoch_updates} train_loss={mean_epoch_loss:.6f}"
    )


finish_result = session.finish()


def official_jigsaw_score(validation_frame, predictions):
    predictions = np.asarray(predictions, dtype=np.float64).reshape(-1)

    if len(predictions) != len(validation_frame):
        raise ValueError("Validation predictions and labels have different lengths.")

    target = (
        pd.to_numeric(validation_frame["target"], errors="coerce")
        .fillna(0.0)
        .to_numpy()
        >= 0.5
    ).astype(np.int8)

    def safe_auc(labels, scores):
        labels = np.asarray(labels, dtype=np.int8)
        if np.unique(labels).size < 2:
            raise ValueError("Official AUC subset unexpectedly contains one class.")
        return float(roc_auc_score(labels, scores))

    overall_auc = safe_auc(target, predictions)
    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_column in evaluated_identity_columns:
        subgroup = (
            pd.to_numeric(validation_frame[identity_column], errors="coerce")
            .fillna(0.0)
            .to_numpy()
            >= 0.5
        )

        subgroup_aucs.append(safe_auc(target[subgroup], predictions[subgroup]))

        bpsn_mask = ((~subgroup) & (target == 1)) | (subgroup & (target == 0))
        bpsn_aucs.append(safe_auc(target[bpsn_mask], predictions[bpsn_mask]))

        bnsp_mask = ((~subgroup) & (target == 0)) | (subgroup & (target == 1))
        bnsp_aucs.append(safe_auc(target[bnsp_mask], predictions[bnsp_mask]))

    power = -5.0

    def generalized_mean(values):
        values = np.clip(
            np.asarray(values, dtype=np.float64),
            1e-15,
            1.0,
        )
        return float(np.mean(values**power) ** (1.0 / power))

    return float(
        0.25
        * (
            overall_auc
            + generalized_mean(subgroup_aucs)
            + generalized_mean(bpsn_aucs)
            + generalized_mean(bnsp_aucs)
        )
    )


def runtime_score(runtime_session, runtime_finish_result):
    score_keys = (
        "final_validation_score",
        "best_validation_score",
        "validation_score",
        "best_score",
        "score",
    )

    for source in (runtime_finish_result, runtime_session):
        if isinstance(source, dict):
            for key in score_keys:
                value = source.get(key)
                if isinstance(value, (int, float, np.floating)):
                    return float(value)

        for key in score_keys:
            value = getattr(source, key, None)
            if isinstance(value, (int, float, np.floating)):
                return float(value)

    return None


score = runtime_score(session, finish_result)

if score is None or not np.isfinite(score):
    final_validation_predictions = predict_validation(
        np.arange(len(valid_processed), dtype=np.int64)
    )
    score = official_jigsaw_score(
        valid_processed,
        final_validation_predictions,
    )

print(f"Final Validation Score: {score}")
