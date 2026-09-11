import os
import re
import gc
import json
import math
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import Dataset, DataLoader, Sampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from engine.candidate_runtime import CandidateSession


os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

SEED = 2027
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

TOXICITY_AUX_COLUMNS = [
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

IDENTITY_MENTION_PATTERN = (
    r"\b(?:male|men|man|boys?|female|women|woman|girls?|transgender|trans|"
    r"heterosexual|straight|homosexual|gay|gays|lesbian|lesbians|bisexual|"
    r"christian|christians|jew|jews|jewish|muslim|muslims|islamic|islam|"
    r"hindu|hindus|buddhist|buddhists|atheist|atheists|black|blacks|white|"
    r"whites|asian|asians|latino|latina|latinx|disabled|disability|"
    r"autistic|autism|mental(?:ly)?\s+ill)\b"
)

URL_PATTERN = r"(?i)\b(?:https?://|www\.)\S+"
USER_PATTERN = r"(?<!\w)@[A-Za-z0-9_]+"
LETTER_RUN_PATTERN = r"([a-z])\1{2,}"
INWORD_SYMBOL_PATTERN = r"(?<=[a-z0-9])(?:[._*/-])+(?=[a-z0-9])"

np.random.seed(SEED)
torch.manual_seed(SEED)

if hasattr(torch, "set_float32_matmul_precision"):
    torch.set_float32_matmul_precision("high")


# ---------------------------------------------------------------------
# Candidate runtime split: performed before all fitted transformations.
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

train_raw = pd.read_csv(INPUT_DIR / "train.csv", low_memory=False)
test_raw = pd.read_csv(INPUT_DIR / "test.csv", low_memory=False)

train_df, valid_df, test_df = session.split(train_raw, test_raw)

del train_raw, test_raw
gc.collect()


# ---------------------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------------------
def normalize_text(text_series: pd.Series) -> pd.Series:
    text = text_series.fillna("").astype(str).str.normalize("NFKC")
    text = text.str.replace(r"[\u200b\u200c\u200d\ufeff]", "", regex=True)
    text = text.str.replace("&amp;", "&", regex=False)
    text = text.str.replace("&lt;", "<", regex=False)
    text = text.str.replace("&gt;", ">", regex=False)
    text = text.str.replace("&quot;", '"', regex=False)
    text = text.str.replace("&#39;", "'", regex=False)
    text = text.str.replace(URL_PATTERN, " <URL> ", regex=True)
    text = text.str.replace(USER_PATTERN, " <USER> ", regex=True)
    text = text.str.replace(r"[\r\n\t]+", " ", regex=True)
    return text.str.replace(r"\s+", " ", regex=True).str.strip()


def make_robust_text(normalized_text: pd.Series) -> pd.Series:
    robust = normalized_text.str.lower()
    for _ in range(2):
        robust = robust.str.replace(INWORD_SYMBOL_PATTERN, "", regex=True)
    robust = robust.str.replace(LETTER_RUN_PATTERN, r"\1\1", regex=True)
    return robust.str.replace(r"\s+", " ", regex=True).str.strip()


def make_style_features(
    original_text: pd.Series,
    normalized_text: pd.Series,
) -> pd.DataFrame:
    original = original_text.fillna("").astype(str).str.normalize("NFKC")
    char_count = normalized_text.str.len().clip(lower=0).astype(np.float32)
    word_count = normalized_text.str.count(r"\S+").astype(np.float32)
    letter_count = normalized_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = normalized_text.str.count(r"[A-Z]").astype(np.float32)

    denominator = np.maximum(letter_count.to_numpy(dtype=np.float32), 1.0)
    uppercase_ratio = uppercase_count.to_numpy(dtype=np.float32) / denominator
    average_word_length = char_count.to_numpy(dtype=np.float32) / np.maximum(
        word_count.to_numpy(dtype=np.float32), 1.0
    )

    return pd.DataFrame(
        {
            "log_char_count": np.log1p(char_count.to_numpy(dtype=np.float32)),
            "log_word_count": np.log1p(word_count.to_numpy(dtype=np.float32)),
            "average_word_length": average_word_length,
            "uppercase_letter_ratio": uppercase_ratio,
            "log_exclamation_count": np.log1p(
                normalized_text.str.count("!").to_numpy(dtype=np.float32)
            ),
            "log_question_count": np.log1p(
                normalized_text.str.count(r"\?").to_numpy(dtype=np.float32)
            ),
            "log_quote_count": np.log1p(
                normalized_text.str.count(r"""["']""").to_numpy(dtype=np.float32)
            ),
            "log_url_count": np.log1p(
                original.str.count(URL_PATTERN).to_numpy(dtype=np.float32)
            ),
            "log_user_mention_count": np.log1p(
                original.str.count(USER_PATTERN).to_numpy(dtype=np.float32)
            ),
            "log_identity_lexical_count": np.log1p(
                normalized_text.str.count(IDENTITY_MENTION_PATTERN).to_numpy(
                    dtype=np.float32
                )
            ),
            "has_repeated_punctuation": normalized_text.str.contains(
                r"(?:!{3,}|\?{3,})", regex=True
            )
            .astype(np.float32)
            .to_numpy(),
            "has_all_caps_token": normalized_text.str.contains(
                r"\b[A-Z]{4,}\b", regex=True
            )
            .astype(np.float32)
            .to_numpy(),
            "had_newline_or_tab": original.str.contains(r"[\r\n\t]", regex=True)
            .astype(np.float32)
            .to_numpy(),
        },
        index=normalized_text.index,
    ).astype(np.float32)


train_normalized_text = normalize_text(train_df["comment_text"])
train_robust_text = make_robust_text(train_normalized_text)
train_style_raw = make_style_features(train_df["comment_text"], train_normalized_text)

train_text_hash = pd.util.hash_pandas_object(
    train_normalized_text,
    index=False,
).astype("uint64")

train_frequency_lookup = pd.Series(
    train_text_hash.to_numpy(dtype=np.uint64)
).value_counts(sort=False)

train_style_raw["log_train_text_frequency"] = np.log1p(
    pd.Series(train_text_hash.to_numpy(dtype=np.uint64))
    .map(train_frequency_lookup)
    .fillna(0)
    .to_numpy(dtype=np.float32)
).astype(np.float32)

style_columns = list(train_style_raw.columns)
style_feature_names = [f"style_z_{name}" for name in style_columns]
STYLE_FEATURE_DIM = len(style_feature_names)

style_scaler = StandardScaler()
style_scaler.fit(train_style_raw[style_columns].to_numpy(dtype=np.float32))


def build_processed_partition(
    source_df: pd.DataFrame,
    partition_name: str,
    normalized_text: pd.Series | None = None,
    robust_text: pd.Series | None = None,
    raw_style_features: pd.DataFrame | None = None,
) -> pd.DataFrame:
    if normalized_text is None:
        normalized_text = normalize_text(source_df["comment_text"])
    if robust_text is None:
        robust_text = make_robust_text(normalized_text)
    if raw_style_features is None:
        raw_style_features = make_style_features(
            source_df["comment_text"],
            normalized_text,
        )

    text_hash = pd.util.hash_pandas_object(normalized_text, index=False).astype(
        "uint64"
    )
    frequency = pd.Series(text_hash.to_numpy(dtype=np.uint64)).map(
        train_frequency_lookup
    )
    frequency = frequency.fillna(0).to_numpy(dtype=np.float32)

    raw_style_features = raw_style_features.copy()
    raw_style_features["log_train_text_frequency"] = np.log1p(frequency).astype(
        np.float32
    )

    scaled_style = style_scaler.transform(
        raw_style_features[style_columns].to_numpy(dtype=np.float32)
    ).astype(np.float32)

    processed = pd.DataFrame(
        {
            "id": source_df["id"].to_numpy(),
            "model_text": normalized_text.to_numpy(),
            "robust_text": robust_text.to_numpy(),
            "is_seen_normalized_text_in_train": (frequency > 0).astype(np.float32),
        }
    )

    for feature_index, feature_name in enumerate(style_columns):
        processed[f"style_z_{feature_name}"] = scaled_style[:, feature_index]

    available_supervision = [
        column
        for column in (
            ["target"] + TOXICITY_AUX_COLUMNS + IDENTITY_COLUMNS + ANNOTATION_COLUMNS
        )
        if column in source_df.columns
    ]

    for column in available_supervision:
        processed[column] = (
            pd.to_numeric(
                source_df[column],
                errors="coerce",
            )
            .astype(np.float32)
            .to_numpy()
        )

    if partition_name == "train":
        target = processed["target"].clip(0.0, 1.0).to_numpy(dtype=np.float32)

        if "toxicity_annotator_count" in processed.columns:
            annotators = (
                processed["toxicity_annotator_count"]
                .fillna(1.0)
                .clip(lower=1.0)
                .to_numpy(dtype=np.float32)
            )
        else:
            annotators = np.ones(len(processed), dtype=np.float32)

        confidence = (0.20 + 0.80 * np.abs(target - 0.5) * 2.0) * np.log1p(annotators)
        confidence = confidence / max(float(np.mean(confidence)), 1e-6)

        processed["target_binary"] = (target >= 0.5).astype(np.float32)
        processed["train_label_confidence"] = np.clip(
            confidence,
            0.25,
            3.0,
        ).astype(np.float32)

    return processed.reset_index(drop=True)


train_processed = build_processed_partition(
    train_df,
    partition_name="train",
    normalized_text=train_normalized_text,
    robust_text=train_robust_text,
    raw_style_features=train_style_raw,
)

del train_normalized_text, train_robust_text, train_style_raw
gc.collect()

valid_processed = build_processed_partition(
    valid_df,
    partition_name="validation",
)

test_processed = build_processed_partition(
    test_df,
    partition_name="test",
)

feature_state = {
    "seed": SEED,
    "text_columns": ["model_text", "robust_text"],
    "style_feature_columns": style_columns,
    "scaled_style_feature_columns": style_feature_names,
    "identity_columns_for_official_audit": IDENTITY_COLUMNS,
    "toxicity_auxiliary_columns": TOXICITY_AUX_COLUMNS,
    "identity_mention_pattern": IDENTITY_MENTION_PATTERN,
    "style_scaler": style_scaler,
}

joblib.dump(feature_state, WORKING_DIR / "feature_engineering_state.joblib")

with open(
    WORKING_DIR / "feature_engineering_manifest.json",
    "w",
    encoding="utf-8",
) as manifest_file:
    json.dump(
        {
            "train_rows": int(len(train_processed)),
            "validation_rows": int(len(valid_processed)),
            "test_rows": int(len(test_processed)),
            "style_feature_names": style_feature_names,
            "text_columns": ["model_text", "robust_text"],
        },
        manifest_file,
        indent=2,
    )

del train_df, valid_df, test_df
gc.collect()


# ---------------------------------------------------------------------
# Dual-view DeBERTa model
# ---------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
pretrained_model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class MaskedAttentionPool(nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.projection = nn.Linear(hidden_size, hidden_size)
        self.query = nn.Parameter(torch.empty(hidden_size))
        nn.init.normal_(self.query, mean=0.0, std=hidden_size**-0.5)

    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        projected = torch.tanh(self.projection(hidden_states))
        scores = torch.einsum("bsh,h->bs", projected, self.query)
        scores = scores.masked_fill(attention_mask == 0, -1e4)
        weights = torch.softmax(scores, dim=1)
        return torch.einsum("bs,bsh->bh", weights, hidden_states)


class DualViewFairnessModel(nn.Module):
    def __init__(
        self,
        pretrained_classifier: nn.Module,
        style_feature_dim: int,
        num_toxicity_aux: int,
        num_identity_aux: int,
    ):
        super().__init__()
        self.encoder = pretrained_classifier.deberta
        self.config = pretrained_classifier.config
        hidden_size = self.config.hidden_size

        self.normal_pool = MaskedAttentionPool(hidden_size)
        self.robust_pool = MaskedAttentionPool(hidden_size)

        self.style_encoder = nn.Sequential(
            nn.LayerNorm(style_feature_dim),
            nn.Linear(style_feature_dim, 128),
            nn.GELU(),
            nn.Dropout(0.10),
            nn.Linear(128, hidden_size),
            nn.GELU(),
        )

        fusion_dim = hidden_size * 5

        self.fusion_projection = nn.Sequential(
            nn.Linear(fusion_dim, hidden_size),
            nn.GELU(),
            nn.LayerNorm(hidden_size),
            nn.Dropout(0.20),
        )

        self.fusion_gate = nn.Sequential(
            nn.Linear(fusion_dim, hidden_size),
            nn.Sigmoid(),
        )

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.20),
            nn.Linear(hidden_size // 2, 1),
        )

        self.toxicity_aux_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.15),
            nn.Linear(hidden_size // 2, num_toxicity_aux),
        )

        self.identity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(0.15),
            nn.Linear(hidden_size // 2, num_identity_aux),
        )

    def _encode(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        pooler: MaskedAttentionPool,
    ) -> torch.Tensor:
        encoded = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        ).last_hidden_state
        return pooler(encoded, attention_mask)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        robust_input_ids: torch.Tensor | None = None,
        robust_attention_mask: torch.Tensor | None = None,
        style_features: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        if robust_input_ids is None:
            robust_input_ids = input_ids
        if robust_attention_mask is None:
            robust_attention_mask = attention_mask

        normal_embedding = self._encode(
            input_ids,
            attention_mask,
            self.normal_pool,
        )

        robust_embedding = self._encode(
            robust_input_ids,
            robust_attention_mask,
            self.robust_pool,
        )

        if style_features is None:
            style_features = torch.zeros(
                normal_embedding.shape[0],
                STYLE_FEATURE_DIM,
                dtype=normal_embedding.dtype,
                device=normal_embedding.device,
            )

        style_embedding = self.style_encoder(style_features.float())

        fusion_input = torch.cat(
            [
                normal_embedding,
                robust_embedding,
                torch.abs(normal_embedding - robust_embedding),
                normal_embedding * robust_embedding,
                style_embedding,
            ],
            dim=-1,
        )

        candidate_embedding = self.fusion_projection(fusion_input)
        fusion_gate = self.fusion_gate(fusion_input)
        shared_embedding = 0.5 * (normal_embedding + robust_embedding)

        fused_embedding = (
            fusion_gate * candidate_embedding + (1.0 - fusion_gate) * shared_embedding
        )

        toxicity_logit = self.toxicity_head(fused_embedding).squeeze(-1)
        normal_toxicity_logit = self.toxicity_head(normal_embedding).squeeze(-1)
        robust_toxicity_logit = self.toxicity_head(robust_embedding).squeeze(-1)

        return {
            "toxicity_logit": toxicity_logit,
            "normal_toxicity_logit": normal_toxicity_logit,
            "robust_toxicity_logit": robust_toxicity_logit,
            "toxicity_aux_logits": self.toxicity_aux_head(fused_embedding),
            "identity_logits": self.identity_head(normal_embedding),
            "fused_embedding": fused_embedding,
        }


class DualViewBiasAwareLoss(nn.Module):
    def __init__(
        self,
        positive_weight: float = 2.25,
        toxicity_aux_weight: float = 0.18,
        identity_aux_weight: float = 0.06,
        view_consistency_weight: float = 0.12,
    ):
        super().__init__()
        self.positive_weight = positive_weight
        self.toxicity_aux_weight = toxicity_aux_weight
        self.identity_aux_weight = identity_aux_weight
        self.view_consistency_weight = view_consistency_weight

    @staticmethod
    def masked_bce(
        logits: torch.Tensor,
        targets: torch.Tensor | None,
    ) -> torch.Tensor:
        if targets is None:
            return logits.sum() * 0.0

        targets = targets.to(dtype=logits.dtype, device=logits.device)
        valid = torch.isfinite(targets)

        if not torch.any(valid):
            return logits.sum() * 0.0

        return F.binary_cross_entropy_with_logits(
            logits[valid],
            targets[valid].clamp(0.0, 1.0),
            reduction="mean",
        )

    def forward(
        self,
        outputs: dict[str, torch.Tensor],
        target: torch.Tensor,
        toxicity_aux_targets: torch.Tensor | None = None,
        identity_targets: torch.Tensor | None = None,
        sample_confidence: torch.Tensor | None = None,
    ) -> torch.Tensor:
        target = target.to(
            dtype=outputs["toxicity_logit"].dtype,
            device=outputs["toxicity_logit"].device,
        ).clamp(0.0, 1.0)

        main_per_example = F.binary_cross_entropy_with_logits(
            outputs["toxicity_logit"],
            target,
            reduction="none",
        )

        class_weight = 1.0 + (self.positive_weight - 1.0) * target

        if sample_confidence is not None:
            confidence = sample_confidence.to(
                dtype=main_per_example.dtype,
                device=main_per_example.device,
            ).clamp(0.25, 3.0)
            class_weight = class_weight * confidence

        main_loss = (
            main_per_example * class_weight
        ).sum() / class_weight.sum().clamp_min(1e-6)

        toxicity_aux_loss = self.masked_bce(
            outputs["toxicity_aux_logits"],
            toxicity_aux_targets,
        )

        identity_aux_loss = self.masked_bce(
            outputs["identity_logits"],
            identity_targets,
        )

        consistency_loss = F.smooth_l1_loss(
            torch.sigmoid(outputs["normal_toxicity_logit"]),
            torch.sigmoid(outputs["robust_toxicity_logit"]),
            reduction="mean",
        )

        return (
            main_loss
            + self.toxicity_aux_weight * toxicity_aux_loss
            + self.identity_aux_weight * identity_aux_loss
            + self.view_consistency_weight * consistency_loss
        )


model = DualViewFairnessModel(
    pretrained_classifier=pretrained_model,
    style_feature_dim=STYLE_FEATURE_DIM,
    num_toxicity_aux=len(TOXICITY_AUX_COLUMNS),
    num_identity_aux=len(IDENTITY_COLUMNS),
)

criterion = DualViewBiasAwareLoss()

del pretrained_model
gc.collect()

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")
encoder_decay, encoder_no_decay = [], []
head_decay, head_no_decay = [], []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_encoder = parameter_name.startswith("encoder.")
    has_no_decay = parameter_name.endswith(no_decay_terms)

    if is_encoder and has_no_decay:
        encoder_no_decay.append(parameter)
    elif is_encoder:
        encoder_decay.append(parameter)
    elif has_no_decay:
        head_no_decay.append(parameter)
    else:
        head_decay.append(parameter)

optimizer = AdamW(
    [
        {"params": encoder_decay, "lr": 1.2e-5, "weight_decay": 0.01},
        {"params": encoder_no_decay, "lr": 1.2e-5, "weight_decay": 0.0},
        {"params": head_decay, "lr": 7.0e-5, "weight_decay": 0.01},
        {"params": head_no_decay, "lr": 7.0e-5, "weight_decay": 0.0},
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)


# ---------------------------------------------------------------------
# Datasets, sampling, bridge loss, prediction callbacks
# ---------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

if torch.cuda.is_available():
    gpu_memory_gb = torch.cuda.get_device_properties(device).total_memory / (1024**3)
    micro_batch_size = 8 if gpu_memory_gb >= 28 else 4
    inference_batch_size = 32 if gpu_memory_gb >= 28 else 16
else:
    micro_batch_size = 2
    inference_batch_size = 4

gradient_accumulation_steps = 1 if micro_batch_size >= 8 else 2
max_sequence_length = 192
pin_memory = device.type == "cuda"

amp_scaler = torch.amp.GradScaler(
    "cuda",
    enabled=torch.cuda.is_available(),
)


class ProcessedCommentDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, include_labels: bool):
        self.model_text = frame["model_text"].fillna("").astype(str).to_numpy()
        self.robust_text = frame["robust_text"].fillna("").astype(str).to_numpy()
        self.style_features = frame[style_feature_names].to_numpy(dtype=np.float32)
        self.include_labels = include_labels

        if include_labels:
            self.target = (
                pd.to_numeric(frame["target"], errors="coerce")
                .fillna(0.0)
                .clip(0.0, 1.0)
                .to_numpy(dtype=np.float32)
            )

            self.toxicity_aux = frame.reindex(columns=TOXICITY_AUX_COLUMNS).to_numpy(
                dtype=np.float32
            )

            self.identity_aux = frame.reindex(columns=IDENTITY_COLUMNS).to_numpy(
                dtype=np.float32
            )

            self.confidence = (
                pd.to_numeric(
                    frame.get(
                        "train_label_confidence",
                        pd.Series(1.0, index=frame.index),
                    ),
                    errors="coerce",
                )
                .fillna(1.0)
                .clip(0.25, 3.0)
                .to_numpy(dtype=np.float32)
            )

    def __len__(self):
        return len(self.model_text)

    def __getitem__(self, index: int):
        item = {
            "model_text": self.model_text[index],
            "robust_text": self.robust_text[index],
            "style_features": self.style_features[index],
        }

        if self.include_labels:
            item.update(
                {
                    "target": self.target[index],
                    "toxicity_aux": self.toxicity_aux[index],
                    "identity_aux": self.identity_aux[index],
                    "confidence": self.confidence[index],
                }
            )

        return item


class TextBatchCollator:
    def __init__(self, active_tokenizer, include_labels: bool):
        self.tokenizer = active_tokenizer
        self.include_labels = include_labels

    def __call__(self, examples):
        normal_encoding = self.tokenizer(
            [example["model_text"] for example in examples],
            padding=True,
            truncation=True,
            max_length=max_sequence_length,
            return_tensors="pt",
        )

        robust_encoding = self.tokenizer(
            [example["robust_text"] for example in examples],
            padding=True,
            truncation=True,
            max_length=max_sequence_length,
            return_tensors="pt",
        )

        batch = {
            "input_ids": normal_encoding["input_ids"],
            "attention_mask": normal_encoding["attention_mask"],
            "robust_input_ids": robust_encoding["input_ids"],
            "robust_attention_mask": robust_encoding["attention_mask"],
            "style_features": torch.as_tensor(
                np.stack([example["style_features"] for example in examples]),
                dtype=torch.float32,
            ),
        }

        if self.include_labels:
            batch["target"] = torch.as_tensor(
                [example["target"] for example in examples],
                dtype=torch.float32,
            )

            batch["toxicity_aux_targets"] = torch.as_tensor(
                np.stack([example["toxicity_aux"] for example in examples]),
                dtype=torch.float32,
            )

            batch["identity_targets"] = torch.as_tensor(
                np.stack([example["identity_aux"] for example in examples]),
                dtype=torch.float32,
            )

            batch["sample_confidence"] = torch.as_tensor(
                [example["confidence"] for example in examples],
                dtype=torch.float32,
            )

        return batch


class FairBridgeBatchSampler(Sampler):
    def __init__(
        self,
        total_rows: int,
        subgroup_negative: np.ndarray,
        subgroup_positive: np.ndarray,
        batch_size: int,
        seed: int,
    ):
        self.total_rows = int(total_rows)
        self.subgroup_negative = np.asarray(subgroup_negative, dtype=np.int64)
        self.subgroup_positive = np.asarray(subgroup_positive, dtype=np.int64)
        self.batch_size = int(batch_size)
        self.seed = int(seed)
        self.epoch = 0
        self.steps_per_epoch = int(math.ceil(self.total_rows / self.batch_size))

    def __len__(self):
        return self.steps_per_epoch

    def __iter__(self):
        rng = np.random.default_rng(self.seed + self.epoch)
        self.epoch += 1
        all_indices = np.arange(self.total_rows, dtype=np.int64)

        for _ in range(self.steps_per_epoch):
            selected = []

            if len(self.subgroup_negative) > 0:
                selected.append(
                    self.subgroup_negative[rng.integers(0, len(self.subgroup_negative))]
                )

            if len(self.subgroup_positive) > 0:
                selected.append(
                    self.subgroup_positive[rng.integers(0, len(self.subgroup_positive))]
                )

            remaining = self.batch_size - len(selected)

            if remaining > 0:
                selected.extend(
                    rng.choice(
                        all_indices,
                        size=remaining,
                        replace=remaining > self.total_rows,
                    ).tolist()
                )

            rng.shuffle(selected)
            yield selected


def fairness_bridge_loss(
    fused_embedding: torch.Tensor,
    target: torch.Tensor,
    identity_targets: torch.Tensor,
) -> torch.Tensor:
    finite_identity = torch.isfinite(identity_targets)
    identity_known = finite_identity.any(dim=1)

    identity_mentioned = (
        torch.where(
            finite_identity,
            identity_targets,
            torch.zeros_like(identity_targets),
        )
        >= 0.5
    ).any(dim=1)

    binary_target = target >= 0.5
    normalized = F.normalize(fused_embedding.float(), dim=-1, eps=1e-6)
    similarity = normalized @ normalized.transpose(0, 1)

    valid_pair = identity_known[:, None] & identity_known[None, :]
    cross_context = identity_mentioned[:, None] != identity_mentioned[None, :]

    non_diagonal = ~torch.eye(
        similarity.shape[0],
        dtype=torch.bool,
        device=similarity.device,
    )

    pair_mask = valid_pair & cross_context & non_diagonal
    same_class = binary_target[:, None] == binary_target[None, :]

    positive_pairs = pair_mask & same_class
    negative_pairs = pair_mask & ~same_class

    zero = fused_embedding.sum() * 0.0

    positive_loss = (
        (1.0 - similarity[positive_pairs]).mean() if torch.any(positive_pairs) else zero
    )

    negative_loss = (
        F.relu(similarity[negative_pairs] - 0.20).mean()
        if torch.any(negative_pairs)
        else zero
    )

    return positive_loss + 0.35 * negative_loss


def predict_partition(
    processed_frame: pd.DataFrame,
    positional_indices: np.ndarray,
) -> np.ndarray:
    positions = np.asarray(positional_indices, dtype=np.int64)

    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    subset = processed_frame.iloc[positions].reset_index(drop=True)
    inference_dataset = ProcessedCommentDataset(subset, include_labels=False)

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=2,
        pin_memory=pin_memory,
        persistent_workers=True,
        collate_fn=TextBatchCollator(tokenizer, include_labels=False),
    )

    was_training = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for batch in inference_loader:
                model_inputs = {
                    "input_ids": batch["input_ids"].to(device, non_blocking=True),
                    "attention_mask": batch["attention_mask"].to(
                        device,
                        non_blocking=True,
                    ),
                    "robust_input_ids": batch["robust_input_ids"].to(
                        device,
                        non_blocking=True,
                    ),
                    "robust_attention_mask": batch["robust_attention_mask"].to(
                        device,
                        non_blocking=True,
                    ),
                    "style_features": batch["style_features"].to(
                        device,
                        non_blocking=True,
                    ),
                }

                with torch.autocast(
                    device_type=device.type,
                    dtype=torch.float16,
                    enabled=device.type == "cuda",
                ):
                    outputs = model(**model_inputs)
                    probabilities = torch.sigmoid(outputs["toxicity_logit"])

                predictions.append(
                    probabilities.float().cpu().numpy().astype(np.float64)
                )
    finally:
        model.train(was_training)

    return np.concatenate(predictions, axis=0)


def predict_validation(positional_indices: np.ndarray) -> np.ndarray:
    return predict_partition(valid_processed, positional_indices)


def predict_test(positional_indices: np.ndarray) -> np.ndarray:
    return predict_partition(test_processed, positional_indices)


def save_checkpoint(directory: str):
    checkpoint_dir = Path(directory)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        {"model_state_dict": model.state_dict()},
        checkpoint_dir / "model_state.pt",
    )

    model.config.to_json_file(checkpoint_dir / "backbone_config.json")
    tokenizer.save_pretrained(checkpoint_dir / "tokenizer")

    with open(
        checkpoint_dir / "inference_state.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(
            {
                "max_sequence_length": max_sequence_length,
                "style_feature_names": style_feature_names,
                "toxicity_aux_columns": TOXICITY_AUX_COLUMNS,
                "identity_columns": IDENTITY_COLUMNS,
                "architecture": "DualViewFairnessModel",
                "prediction_semantics": "sigmoid(toxicity_logit)",
            },
            handle,
            indent=2,
        )

    joblib.dump(
        {
            "style_scaler": style_scaler,
            "style_columns": style_columns,
            "feature_state": feature_state,
        },
        checkpoint_dir / "feature_transformations.joblib",
    )


def load_checkpoint(directory: str):
    checkpoint_dir = Path(directory)

    payload = torch.load(
        checkpoint_dir / "model_state.pt",
        map_location="cpu",
    )

    model.load_state_dict(payload["model_state_dict"], strict=True)
    model.to(device)


# ---------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------
train_targets = (
    pd.to_numeric(train_processed["target"], errors="coerce")
    .fillna(0.0)
    .clip(0.0, 1.0)
    .to_numpy(dtype=np.float32)
)

train_identity_matrix = train_processed.reindex(columns=IDENTITY_COLUMNS).to_numpy(
    dtype=np.float32
)

identity_known = np.isfinite(train_identity_matrix).any(axis=1)

identity_mentioned = (
    np.where(
        np.isfinite(train_identity_matrix),
        train_identity_matrix,
        0.0,
    ).max(axis=1)
    >= 0.5
)

binary_train_target = train_targets >= 0.5

subgroup_negative_indices = np.flatnonzero(
    identity_known & identity_mentioned & ~binary_train_target
)

subgroup_positive_indices = np.flatnonzero(
    identity_known & identity_mentioned & binary_train_target
)

train_dataset = ProcessedCommentDataset(train_processed, include_labels=True)

train_sampler = FairBridgeBatchSampler(
    total_rows=len(train_dataset),
    subgroup_negative=subgroup_negative_indices,
    subgroup_positive=subgroup_positive_indices,
    batch_size=micro_batch_size,
    seed=SEED,
)

train_loader = DataLoader(
    train_dataset,
    batch_sampler=train_sampler,
    num_workers=2,
    pin_memory=pin_memory,
    persistent_workers=True,
    collate_fn=TextBatchCollator(tokenizer, include_labels=True),
)

warmup_steps = 100
schedule_horizon = 12000


def learning_rate_multiplier(step_number: int) -> float:
    if step_number < warmup_steps:
        return max(0.05, float(step_number + 1) / float(warmup_steps))

    progress = min(
        1.0,
        float(step_number - warmup_steps)
        / float(max(1, schedule_horizon - warmup_steps)),
    )

    return max(0.10, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(
    optimizer,
    lr_lambda=learning_rate_multiplier,
)

session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_processed["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
stop_training = False

for _ in range(8):
    if stop_training:
        break

    for micro_step, batch in enumerate(train_loader):
        model.train()

        model_inputs = {
            "input_ids": batch["input_ids"].to(device, non_blocking=True),
            "attention_mask": batch["attention_mask"].to(
                device,
                non_blocking=True,
            ),
            "robust_input_ids": batch["robust_input_ids"].to(
                device,
                non_blocking=True,
            ),
            "robust_attention_mask": batch["robust_attention_mask"].to(
                device,
                non_blocking=True,
            ),
            "style_features": batch["style_features"].to(
                device,
                non_blocking=True,
            ),
        }

        target = batch["target"].to(device, non_blocking=True)
        toxicity_aux_targets = batch["toxicity_aux_targets"].to(
            device,
            non_blocking=True,
        )
        identity_targets = batch["identity_targets"].to(
            device,
            non_blocking=True,
        )
        sample_confidence = batch["sample_confidence"].to(
            device,
            non_blocking=True,
        )

        with torch.autocast(
            device_type=device.type,
            dtype=torch.float16,
            enabled=device.type == "cuda",
        ):
            outputs = model(**model_inputs)

            supervised_loss = criterion(
                outputs=outputs,
                target=target,
                toxicity_aux_targets=toxicity_aux_targets,
                identity_targets=identity_targets,
                sample_confidence=sample_confidence,
            )

            bridge_loss = fairness_bridge_loss(
                outputs["fused_embedding"],
                target,
                identity_targets,
            )

            total_loss = supervised_loss + 0.035 * bridge_loss
            scaled_loss = total_loss / gradient_accumulation_steps

        amp_scaler.scale(scaled_loss).backward()

        if (micro_step + 1) % gradient_accumulation_steps != 0:
            continue

        amp_scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        amp_scaler.step(optimizer)
        amp_scaler.update()

        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

        stop_training = session.step()

        if stop_training:
            break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
