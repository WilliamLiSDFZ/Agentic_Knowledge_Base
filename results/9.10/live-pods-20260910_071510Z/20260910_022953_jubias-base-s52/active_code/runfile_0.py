import os
os.sched_setaffinity(0, {4, 7})
import json
import math
import os
import re
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    ModernBertForMaskedLM,
    ModernBertForMultipleChoice,
    ModernBertForQuestionAnswering,
    ModernBertForSequenceClassification,
    ModernBertForTokenClassification,
    get_cosine_schedule_with_warmup,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

RANDOM_STATE = 2025
VALID_FRACTION = 0.10

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

AUXILIARY_LABEL_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

TRAIN_REQUIRED_COLUMNS = (
    ["id", "comment_text", "target"] + IDENTITY_COLUMNS + AUXILIARY_LABEL_COLUMNS
)

train_path = INPUT_DIR / "train.csv"
test_path = INPUT_DIR / "test.csv"
sample_submission_path = INPUT_DIR / "sample_submission.csv"

train_df = pd.read_csv(
    train_path,
    usecols=lambda col: col in TRAIN_REQUIRED_COLUMNS,
    low_memory=False,
)
test_df = pd.read_csv(
    test_path,
    usecols=["id", "comment_text"],
    low_memory=False,
)
sample_submission = pd.read_csv(sample_submission_path)

if list(sample_submission.columns) != ["id", "prediction"]:
    raise ValueError(
        "sample_submission.csv must contain exactly the columns ['id', 'prediction']."
    )

if train_df["id"].duplicated().any() or test_df["id"].duplicated().any():
    raise ValueError("Each sample id must be unique.")

if len(train_df) == 0 or len(test_df) == 0:
    raise ValueError("Train and test files must both contain at least one row.")

if not np.array_equal(sample_submission["id"].to_numpy(), test_df["id"].to_numpy()):
    raise ValueError(
        "test.csv row order must match sample_submission.csv row order by id."
    )


def normalize_comment_text(series: pd.Series) -> pd.Series:
    text = series.fillna("").astype(str)
    text = text.str.normalize("NFKC")
    text = text.str.replace(r"<\s*br\s*/?\s*>", " ", regex=True, case=False)
    text = text.str.replace(r"<[^>]+>", " ", regex=True)
    text = text.str.replace(r"&(?:amp|#38);", "&", regex=True, case=False)
    text = text.str.replace(r"&(?:quot|#34);", '"', regex=True, case=False)
    text = text.str.replace(r"&(?:apos|#39);", "'", regex=True, case=False)
    text = text.str.replace(r"\s+", " ", regex=True).str.strip()
    return text


IDENTITY_CUE_PATTERN = (
    r"\b(?:woman|women|female|girl|girls|man|men|male|boy|boys|transgender|trans|"
    r"gay|lesbian|bisexual|straight|heterosexual|christian|jewish|jew|muslim|islam|"
    r"islamic|hindu|buddhist|atheist|black|white|asian|latino|hispanic|disabled|"
    r"disability|mental illness|autistic|autism)\b"
)


def build_transferable_features(text: pd.Series) -> pd.DataFrame:
    character_count = text.str.len().astype(np.float32)
    word_count = text.str.count(r"\S+").astype(np.float32)
    letter_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = text.str.count(r"[A-Z]").astype(np.float32)
    digit_count = text.str.count(r"\d").astype(np.float32)
    punctuation_count = text.str.count(r"[!?.;,:'\"()\-\[\]]").astype(np.float32)

    safe_character_count = character_count.clip(lower=1.0)
    safe_letter_count = letter_count.clip(lower=1.0)

    features = pd.DataFrame(
        {
            "log_character_count": np.log1p(character_count),
            "log_word_count": np.log1p(word_count),
            "log_exclamation_count": np.log1p(text.str.count(r"!").astype(np.float32)),
            "log_question_count": np.log1p(text.str.count(r"\?").astype(np.float32)),
            "log_url_count": np.log1p(
                text.str.count(r"(?:https?://|www\.)").astype(np.float32)
            ),
            "log_user_mention_count": np.log1p(
                text.str.count(r"(?<!\w)@\w+").astype(np.float32)
            ),
            "uppercase_letter_ratio": uppercase_count / safe_letter_count,
            "digit_character_ratio": digit_count / safe_character_count,
            "punctuation_character_ratio": punctuation_count / safe_character_count,
            "repeated_punctuation_flag": text.str.contains(
                r"[!?]{2,}|\.{3,}",
                regex=True,
            ).astype(np.float32),
            "all_caps_word_flag": text.str.contains(
                r"\b[A-Z]{3,}\b",
                regex=True,
            ).astype(np.float32),
            "identity_cue_count": text.str.count(
                IDENTITY_CUE_PATTERN,
                flags=re.IGNORECASE,
            ).astype(np.float32),
            "has_identity_cue": text.str.contains(
                IDENTITY_CUE_PATTERN,
                flags=re.IGNORECASE,
                regex=True,
            ).astype(np.float32),
            "empty_comment_flag": (character_count == 0).astype(np.float32),
        }
    )
    return features.astype(np.float32)


train_df["transformer_text"] = normalize_comment_text(train_df["comment_text"])
test_df["transformer_text"] = normalize_comment_text(test_df["comment_text"])

train_lexical_features = build_transferable_features(train_df["transformer_text"])
test_lexical_features = build_transferable_features(test_df["transformer_text"])
FEATURE_COLUMNS = train_lexical_features.columns.tolist()

train_df = pd.concat(
    [train_df.drop(columns=["comment_text"]), train_lexical_features],
    axis=1,
)
test_df = pd.concat(
    [test_df.drop(columns=["comment_text"]), test_lexical_features],
    axis=1,
)

train_df["toxicity_label"] = (train_df["target"] >= 0.5).astype(np.int8)

identity_annotations_available = train_df[IDENTITY_COLUMNS].notna().any(axis=1)
identity_mentioned = train_df[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).any(axis=1)

split_strata = (
    train_df["toxicity_label"].astype(np.int8) * 4
    + identity_annotations_available.astype(np.int8) * 2
    + identity_mentioned.astype(np.int8)
).to_numpy()

comment_groups = pd.util.hash_pandas_object(
    train_df["transformer_text"],
    index=False,
).to_numpy(dtype=np.uint64)

try:
    splitter = StratifiedGroupKFold(
        n_splits=10,
        shuffle=True,
        random_state=RANDOM_STATE,
    )
    train_indices, valid_indices = next(
        splitter.split(
            X=np.zeros(len(train_df), dtype=np.int8),
            y=split_strata,
            groups=comment_groups,
        )
    )
except ValueError:
    fallback_splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=VALID_FRACTION,
        random_state=RANDOM_STATE,
    )
    train_indices, valid_indices = next(
        fallback_splitter.split(
            X=np.zeros(len(train_df), dtype=np.int8),
            groups=comment_groups,
        )
    )

train_processed = train_df.iloc[train_indices].copy()
valid_processed = train_df.iloc[valid_indices].copy()
test_processed = test_df.copy()

scaler = StandardScaler()

train_processed.loc[:, FEATURE_COLUMNS] = scaler.fit_transform(
    train_processed[FEATURE_COLUMNS]
).astype(np.float32)

valid_processed.loc[:, FEATURE_COLUMNS] = scaler.transform(
    valid_processed[FEATURE_COLUMNS]
).astype(np.float32)

test_processed.loc[:, FEATURE_COLUMNS] = scaler.transform(
    test_processed[FEATURE_COLUMNS]
).astype(np.float32)

train_subgroup = train_processed[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).any(axis=1)
train_is_toxic = train_processed["toxicity_label"].astype(bool)

train_processed["fairness_sample_weight"] = (
    1.0
    + 1.5 * train_subgroup.astype(np.float32)
    + 2.5 * (train_subgroup & ~train_is_toxic).astype(np.float32)
    + 0.5 * train_is_toxic.astype(np.float32)
).astype(np.float32)

valid_processed["fairness_sample_weight"] = np.ones(
    len(valid_processed),
    dtype=np.float32,
)

for frame in (train_processed, valid_processed):
    frame["identity_annotation_available"] = (
        frame[IDENTITY_COLUMNS].notna().any(axis=1).astype(np.int8)
    )
    frame["any_identity_mentioned"] = (
        frame[IDENTITY_COLUMNS].fillna(0.0).ge(0.5).any(axis=1).astype(np.int8)
    )

model_input_columns = ["transformer_text"] + FEATURE_COLUMNS
label_columns = (
    ["target", "toxicity_label"] + AUXILIARY_LABEL_COLUMNS + IDENTITY_COLUMNS
)

artifact_paths = {}
for artifact_name, frame in {
    "train": train_processed,
    "valid": valid_processed,
    "test": test_processed,
}.items():
    parquet_path = WORKING_DIR / f"toxicity_{artifact_name}_features.parquet"
    try:
        frame.to_parquet(parquet_path, index=False)
        artifact_paths[artifact_name] = str(parquet_path)
    except Exception:
        pickle_path = WORKING_DIR / f"toxicity_{artifact_name}_features.pkl"
        frame.to_pickle(pickle_path)
        artifact_paths[artifact_name] = str(pickle_path)

scaler_path = WORKING_DIR / "lexical_feature_scaler.joblib"
joblib.dump(scaler, scaler_path)

metadata = {
    "random_state": RANDOM_STATE,
    "split_strategy": "StratifiedGroupKFold on normalized-comment hashes",
    "validation_fraction_approximate": VALID_FRACTION,
    "model_input_columns": model_input_columns,
    "lexical_feature_columns": FEATURE_COLUMNS,
    "target_column": "target",
    "binary_target_column": "toxicity_label",
    "identity_columns": IDENTITY_COLUMNS,
    "evaluated_identity_columns": EVALUATED_IDENTITY_COLUMNS,
    "auxiliary_label_columns": AUXILIARY_LABEL_COLUMNS,
    "train_only_weight_column": "fairness_sample_weight",
    "scaler_path": str(scaler_path),
    "artifacts": artifact_paths,
    "n_train": int(len(train_processed)),
    "n_validation": int(len(valid_processed)),
    "n_test": int(len(test_processed)),
}

with open(
    WORKING_DIR / "feature_metadata.json",
    "w",
    encoding="utf-8",
) as metadata_file:
    json.dump(metadata, metadata_file, indent=2)

MODEL_ID = "answerdotai/ModernBERT-large"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
pretrained_classifier = ModernBertForSequenceClassification.from_pretrained(MODEL_ID)


class FairToxicityModernBert(nn.Module):
    def __init__(
        self,
        pretrained_model: ModernBertForSequenceClassification,
        numeric_feature_dim: int,
        num_auxiliary_labels: int,
        num_identity_labels: int,
        dropout_probability: float = 0.15,
    ) -> None:
        super().__init__()

        self.backbone = pretrained_model.model
        hidden_size = self.backbone.config.hidden_size

        self.numeric_encoder = nn.Sequential(
            nn.Linear(numeric_feature_dim, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size, hidden_size),
        )

        self.numeric_gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Sigmoid(),
        )

        self.fusion_norm = nn.LayerNorm(hidden_size)
        self.shared_dropout = nn.Dropout(dropout_probability)

        self.toxicity_head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(hidden_size // 2, 1),
        )

        self.auxiliary_head = nn.Linear(hidden_size, num_auxiliary_labels)
        self.identity_head = nn.Linear(hidden_size, num_identity_labels)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        numeric_features: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        backbone_output = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True,
        )

        token_embeddings = backbone_output.last_hidden_state
        token_mask = attention_mask.unsqueeze(-1).to(token_embeddings.dtype)

        pooled_text = (token_embeddings * token_mask).sum(dim=1)
        pooled_text = pooled_text / token_mask.sum(dim=1).clamp_min(1.0)

        numeric_embedding = self.numeric_encoder(numeric_features.to(pooled_text.dtype))

        fusion_gate = self.numeric_gate(
            torch.cat([pooled_text, numeric_embedding], dim=-1)
        )

        fused_embedding = self.fusion_norm(
            pooled_text + fusion_gate * numeric_embedding
        )
        fused_embedding = self.shared_dropout(fused_embedding)

        toxicity_logits = self.toxicity_head(fused_embedding).squeeze(-1)
        auxiliary_logits = self.auxiliary_head(fused_embedding)
        identity_logits = self.identity_head(fused_embedding)

        return {
            "toxicity_logits": toxicity_logits,
            "toxicity_probability": torch.sigmoid(toxicity_logits),
            "auxiliary_logits": auxiliary_logits,
            "identity_logits": identity_logits,
        }


class BiasAwareToxicityLoss(nn.Module):
    def __init__(
        self,
        toxicity_weight: float = 1.0,
        auxiliary_weight: float = 0.20,
        identity_weight: float = 0.08,
        ranking_weight: float = 0.35,
        ranking_temperature: float = 0.50,
    ) -> None:
        super().__init__()
        self.toxicity_weight = toxicity_weight
        self.auxiliary_weight = auxiliary_weight
        self.identity_weight = identity_weight
        self.ranking_weight = ranking_weight
        self.ranking_temperature = ranking_temperature

    @staticmethod
    def _masked_bce(
        logits: torch.Tensor,
        targets: torch.Tensor,
        valid_mask: torch.Tensor,
    ) -> torch.Tensor:
        elementwise_loss = F.binary_cross_entropy_with_logits(
            logits,
            torch.nan_to_num(targets, nan=0.0).to(logits.dtype),
            reduction="none",
        )

        valid_mask = valid_mask.to(elementwise_loss.dtype)

        return (elementwise_loss * valid_mask).sum() / valid_mask.sum().clamp_min(1.0)

    def _pairwise_auc_surrogate(
        self,
        positive_logits: torch.Tensor,
        negative_logits: torch.Tensor,
    ) -> torch.Tensor | None:
        if positive_logits.numel() == 0 or negative_logits.numel() == 0:
            return None

        margin = (
            positive_logits[:, None] - negative_logits[None, :]
        ) / self.ranking_temperature

        return F.softplus(-margin).mean()

    def _bias_ranking_loss(
        self,
        toxicity_logits: torch.Tensor,
        toxicity_targets: torch.Tensor,
        identity_targets: torch.Tensor,
    ) -> torch.Tensor:
        binary_toxicity = toxicity_targets.ge(0.5)
        identity_available = torch.isfinite(identity_targets)
        identity_mentioned = torch.nan_to_num(
            identity_targets,
            nan=0.0,
        ).ge(0.5)

        subgroup_losses = []

        for identity_index in range(identity_targets.shape[1]):
            available = identity_available[:, identity_index]
            subgroup = identity_mentioned[:, identity_index] & available
            background = (~identity_mentioned[:, identity_index]) & available

            subgroup_positive = toxicity_logits[subgroup & binary_toxicity]
            subgroup_negative = toxicity_logits[subgroup & ~binary_toxicity]
            background_positive = toxicity_logits[background & binary_toxicity]
            background_negative = toxicity_logits[background & ~binary_toxicity]

            subgroup_auc_loss = self._pairwise_auc_surrogate(
                subgroup_positive,
                subgroup_negative,
            )
            bpsn_auc_loss = self._pairwise_auc_surrogate(
                background_positive,
                subgroup_negative,
            )
            bnsp_auc_loss = self._pairwise_auc_surrogate(
                subgroup_positive,
                background_negative,
            )

            valid_terms = [
                loss
                for loss in (
                    subgroup_auc_loss,
                    bpsn_auc_loss,
                    bnsp_auc_loss,
                )
                if loss is not None
            ]

            if valid_terms:
                subgroup_losses.append(torch.stack(valid_terms).mean())

        if not subgroup_losses:
            return toxicity_logits.new_zeros(())

        return torch.stack(subgroup_losses).mean()

    def forward(
        self,
        model_outputs: dict[str, torch.Tensor],
        toxicity_targets: torch.Tensor,
        auxiliary_targets: torch.Tensor,
        identity_targets: torch.Tensor,
        fairness_sample_weight: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        toxicity_logits = model_outputs["toxicity_logits"]

        target_values = toxicity_targets.to(toxicity_logits.dtype).clamp(0.0, 1.0)
        sample_weight = fairness_sample_weight.to(toxicity_logits.dtype).clamp(
            min=0.1,
            max=8.0,
        )

        toxicity_elementwise = F.binary_cross_entropy_with_logits(
            toxicity_logits,
            target_values,
            reduction="none",
        )

        toxicity_loss = (
            toxicity_elementwise * sample_weight
        ).sum() / sample_weight.sum()

        auxiliary_mask = torch.isfinite(auxiliary_targets)
        auxiliary_loss = self._masked_bce(
            model_outputs["auxiliary_logits"],
            auxiliary_targets,
            auxiliary_mask,
        )

        identity_mask = torch.isfinite(identity_targets)
        identity_loss = self._masked_bce(
            model_outputs["identity_logits"],
            identity_targets,
            identity_mask,
        )

        ranking_loss = self._bias_ranking_loss(
            toxicity_logits=toxicity_logits,
            toxicity_targets=toxicity_targets,
            identity_targets=identity_targets,
        )

        total_loss = (
            self.toxicity_weight * toxicity_loss
            + self.auxiliary_weight * auxiliary_loss
            + self.identity_weight * identity_loss
            + self.ranking_weight * ranking_loss
        )

        return {
            "loss": total_loss,
            "toxicity_loss": toxicity_loss.detach(),
            "auxiliary_loss": auxiliary_loss.detach(),
            "identity_loss": identity_loss.detach(),
            "bias_ranking_loss": ranking_loss.detach(),
        }


NUMERIC_FEATURE_DIM = len(FEATURE_COLUMNS)

model = FairToxicityModernBert(
    pretrained_model=pretrained_classifier,
    numeric_feature_dim=NUMERIC_FEATURE_DIM,
    num_auxiliary_labels=len(AUXILIARY_LABEL_COLUMNS),
    num_identity_labels=len(IDENTITY_COLUMNS),
)

if hasattr(model.backbone, "gradient_checkpointing_enable"):
    model.backbone.gradient_checkpointing_enable()

criterion = BiasAwareToxicityLoss()

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight", "norm.weight")

encoder_decay_parameters = []
encoder_no_decay_parameters = []
head_decay_parameters = []
head_no_decay_parameters = []

for parameter_name, parameter in model.named_parameters():
    if not parameter.requires_grad:
        continue

    is_no_decay = any(term in parameter_name for term in no_decay_terms)

    if parameter_name.startswith("backbone."):
        if is_no_decay:
            encoder_no_decay_parameters.append(parameter)
        else:
            encoder_decay_parameters.append(parameter)
    else:
        if is_no_decay:
            head_no_decay_parameters.append(parameter)
        else:
            head_decay_parameters.append(parameter)

optimizer = AdamW(
    [
        {
            "params": encoder_decay_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": encoder_no_decay_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.0,
        },
        {
            "params": head_decay_parameters,
            "lr": 1.0e-4,
            "weight_decay": 0.01,
        },
        {
            "params": head_no_decay_parameters,
            "lr": 1.0e-4,
            "weight_decay": 0.0,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
PIN_MEMORY = DEVICE.type == "cuda"
NUM_WORKERS = max(2, min(4, (os.cpu_count() or 2) // 2))

MAX_SEQUENCE_LENGTH = min(384, int(tokenizer.model_max_length))

if DEVICE.type == "cuda":
    total_vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    if total_vram_gb >= 70:
        TRAIN_BATCH_SIZE = 32
    elif total_vram_gb >= 40:
        TRAIN_BATCH_SIZE = 16
    elif total_vram_gb >= 24:
        TRAIN_BATCH_SIZE = 8
    else:
        TRAIN_BATCH_SIZE = 4
else:
    TRAIN_BATCH_SIZE = 2

EVAL_BATCH_SIZE = max(2, TRAIN_BATCH_SIZE * 2)
GRADIENT_ACCUMULATION_STEPS = max(1, 64 // TRAIN_BATCH_SIZE)
MAX_EPOCHS = 2
EARLY_STOPPING_PATIENCE = 1
MAX_GRAD_NORM = 1.0

amp_enabled = torch.cuda.is_available()
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)

best_checkpoint_path = WORKING_DIR / "best_fair_modernbert_checkpoint.pt"


class ToxicityFrameDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, include_labels: bool) -> None:
        self.texts = frame["transformer_text"].fillna("").astype(str).tolist()
        self.numeric_features = frame[FEATURE_COLUMNS].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.include_labels = include_labels

        if include_labels:
            self.toxicity_targets = frame["target"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.auxiliary_targets = frame[AUXILIARY_LABEL_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_targets = frame[IDENTITY_COLUMNS].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.fairness_weights = frame["fairness_sample_weight"].to_numpy(
                dtype=np.float32,
                copy=True,
            )

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int) -> dict:
        sample = {
            "text": self.texts[index],
            "numeric_features": self.numeric_features[index],
        }

        if self.include_labels:
            sample.update(
                {
                    "toxicity_targets": self.toxicity_targets[index],
                    "auxiliary_targets": self.auxiliary_targets[index],
                    "identity_targets": self.identity_targets[index],
                    "fairness_sample_weight": self.fairness_weights[index],
                }
            )

        return sample


def collate_toxicity_batch(samples: list[dict]) -> dict[str, torch.Tensor]:
    encoded = tokenizer(
        [sample["text"] for sample in samples],
        padding=True,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        return_attention_mask=True,
        return_tensors="pt",
    )

    batch = {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "numeric_features": torch.from_numpy(
            np.stack([sample["numeric_features"] for sample in samples]).astype(
                np.float32, copy=False
            )
        ),
    }

    if "toxicity_targets" in samples[0]:
        batch["toxicity_targets"] = torch.tensor(
            [sample["toxicity_targets"] for sample in samples],
            dtype=torch.float32,
        )
        batch["auxiliary_targets"] = torch.from_numpy(
            np.stack([sample["auxiliary_targets"] for sample in samples]).astype(
                np.float32, copy=False
            )
        )
        batch["identity_targets"] = torch.from_numpy(
            np.stack([sample["identity_targets"] for sample in samples]).astype(
                np.float32, copy=False
            )
        )
        batch["fairness_sample_weight"] = torch.tensor(
            [sample["fairness_sample_weight"] for sample in samples],
            dtype=torch.float32,
        )

    return batch


train_dataset = ToxicityFrameDataset(train_processed, include_labels=True)
valid_dataset = ToxicityFrameDataset(valid_processed, include_labels=True)
test_dataset = ToxicityFrameDataset(test_processed, include_labels=False)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=collate_toxicity_batch,
)

valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=collate_toxicity_batch,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    prefetch_factor=2,
    collate_fn=collate_toxicity_batch,
)

updates_per_epoch = math.ceil(len(train_loader) / GRADIENT_ACCUMULATION_STEPS)
total_updates = max(1, updates_per_epoch * MAX_EPOCHS)
warmup_updates = max(1, int(0.05 * total_updates))

scheduler = get_cosine_schedule_with_warmup(
    optimizer,
    num_warmup_steps=warmup_updates,
    num_training_steps=total_updates,
)

model.to(DEVICE)


def move_batch_to_device(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
    return {
        key: value.to(DEVICE, non_blocking=PIN_MEMORY) for key, value in batch.items()
    }


@torch.inference_mode()
def predict_probabilities(data_loader: DataLoader) -> np.ndarray:
    model.eval()
    probability_chunks = []

    for batch in data_loader:
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
            )
            probabilities = torch.sigmoid(outputs["toxicity_logits"])

        probability_chunks.append(probabilities.float().cpu().numpy())

    if not probability_chunks:
        raise RuntimeError("Inference loader produced no batches.")

    return np.concatenate(probability_chunks).astype(np.float64, copy=False)


def binary_auc(labels: np.ndarray, predictions: np.ndarray) -> float:
    labels = np.asarray(labels, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if np.unique(labels).size != 2:
        return float("nan")

    return float(roc_auc_score(labels, predictions))


def official_bias_aware_auc(
    toxicity_targets: np.ndarray,
    identity_values: np.ndarray,
    predictions: np.ndarray,
) -> tuple[float, dict[str, float]]:
    binary_targets = np.asarray(toxicity_targets >= 0.5, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    overall_auc = binary_auc(binary_targets, predictions)

    if not np.isfinite(overall_auc):
        raise ValueError("Validation data does not contain both toxicity classes.")

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    detailed_metrics = {
        "overall_auc": overall_auc,
    }

    for identity_index, identity_name in enumerate(EVALUATED_IDENTITY_COLUMNS):
        subgroup = np.asarray(
            np.nan_to_num(
                identity_values[:, identity_index],
                nan=0.0,
            )
            >= 0.5,
            dtype=bool,
        )

        subgroup_mask = subgroup

        bpsn_mask = ((binary_targets == 0) & subgroup) | (
            (binary_targets == 1) & ~subgroup
        )

        bnsp_mask = ((binary_targets == 1) & subgroup) | (
            (binary_targets == 0) & ~subgroup
        )

        subgroup_auc = binary_auc(
            binary_targets[subgroup_mask],
            predictions[subgroup_mask],
        )

        bpsn_auc = binary_auc(
            binary_targets[bpsn_mask],
            predictions[bpsn_mask],
        )

        bnsp_auc = binary_auc(
            binary_targets[bnsp_mask],
            predictions[bnsp_mask],
        )

        if not (
            np.isfinite(subgroup_auc)
            and np.isfinite(bpsn_auc)
            and np.isfinite(bnsp_auc)
        ):
            raise ValueError(
                f"Official bias AUC cannot be computed for identity '{identity_name}'."
            )

        subgroup_aucs.append(subgroup_auc)
        bpsn_aucs.append(bpsn_auc)
        bnsp_aucs.append(bnsp_auc)

        detailed_metrics[f"{identity_name}_subgroup_auc"] = subgroup_auc
        detailed_metrics[f"{identity_name}_bpsn_auc"] = bpsn_auc
        detailed_metrics[f"{identity_name}_bnsp_auc"] = bnsp_auc

    power = -5.0

    def generalized_mean(values: list[float]) -> float:
        values_array = np.asarray(values, dtype=np.float64)
        return float(np.mean(np.power(values_array, power)) ** (1.0 / power))

    subgroup_power_mean = generalized_mean(subgroup_aucs)
    bpsn_power_mean = generalized_mean(bpsn_aucs)
    bnsp_power_mean = generalized_mean(bnsp_aucs)

    final_score = float(
        0.25 * (overall_auc + subgroup_power_mean + bpsn_power_mean + bnsp_power_mean)
    )

    detailed_metrics.update(
        {
            "subgroup_power_mean": subgroup_power_mean,
            "bpsn_power_mean": bpsn_power_mean,
            "bnsp_power_mean": bnsp_power_mean,
            "official_score": final_score,
        }
    )

    return final_score, detailed_metrics


validation_targets = valid_processed["target"].to_numpy(
    dtype=np.float32,
    copy=True,
)

validation_identities = valid_processed[EVALUATED_IDENTITY_COLUMNS].to_numpy(
    dtype=np.float32,
    copy=True,
)

best_score = -float("inf")
best_epoch = -1
epochs_without_improvement = 0

for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    optimizer.zero_grad(set_to_none=True)

    accumulated_train_loss = 0.0
    observed_batches = 0

    for batch_index, batch in enumerate(train_loader, start=1):
        batch = move_batch_to_device(batch)

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
            )

            loss_components = criterion(
                model_outputs=outputs,
                toxicity_targets=batch["toxicity_targets"],
                auxiliary_targets=batch["auxiliary_targets"],
                identity_targets=batch["identity_targets"],
                fairness_sample_weight=batch["fairness_sample_weight"],
            )

            scaled_loss = loss_components["loss"] / GRADIENT_ACCUMULATION_STEPS

        grad_scaler.scale(scaled_loss).backward()

        accumulated_train_loss += float(loss_components["loss"].detach().cpu())
        observed_batches += 1

        should_update = (
            batch_index % GRADIENT_ACCUMULATION_STEPS == 0
            or batch_index == len(train_loader)
        )

        if should_update:
            grad_scaler.unscale_(optimizer)
            clip_grad_norm_(model.parameters(), MAX_GRAD_NORM)
            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

    validation_predictions = predict_probabilities(valid_loader)

    epoch_score, epoch_metrics = official_bias_aware_auc(
        toxicity_targets=validation_targets,
        identity_values=validation_identities,
        predictions=validation_predictions,
    )

    mean_train_loss = accumulated_train_loss / max(1, observed_batches)

    if epoch_score > best_score:
        best_score = epoch_score
        best_epoch = epoch
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch,
                "official_validation_score": epoch_score,
                "validation_metrics": epoch_metrics,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
            },
            best_checkpoint_path,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch}/{MAX_EPOCHS} | train_loss={mean_train_loss:.5f} | "
        f"overall_auc={epoch_metrics['overall_auc']:.6f} | "
        f"subgroup_pm={epoch_metrics['subgroup_power_mean']:.6f} | "
        f"bpsn_pm={epoch_metrics['bpsn_power_mean']:.6f} | "
        f"bnsp_pm={epoch_metrics['bnsp_power_mean']:.6f} | "
        f"official_score={epoch_score:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if best_epoch < 0 or not best_checkpoint_path.exists():
    raise RuntimeError("No valid model checkpoint was saved during training.")

best_checkpoint = torch.load(best_checkpoint_path, map_location=DEVICE)

model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(DEVICE)

best_validation_predictions = predict_probabilities(valid_loader)

score, final_validation_metrics = official_bias_aware_auc(
    toxicity_targets=validation_targets,
    identity_values=validation_identities,
    predictions=best_validation_predictions,
)

test_predictions = predict_probabilities(test_loader)

if len(test_predictions) != len(test_processed):
    raise RuntimeError(
        "Test prediction count mismatch: "
        f"{len(test_predictions)} != {len(test_processed)}"
    )

submission = pd.DataFrame(
    {
        "id": sample_submission["id"].to_numpy(),
        "prediction": np.clip(test_predictions, 0.0, 1.0),
    }
)

submission.to_csv(SUBMISSION_DIR / "submission_13f8a4526f79414b83447057e24b56f3.csv", index=False)

print(f"Final Validation Score: {score}")