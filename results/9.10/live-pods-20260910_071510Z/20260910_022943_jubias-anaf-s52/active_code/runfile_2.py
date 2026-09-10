import os
os.sched_setaffinity(0, {73, 71})
import os
import re
import json
import html
import math
import pickle
import random

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoTokenizer,
    ModernBertForSequenceClassification,
    ModernBertForMaskedLM,
    ModernBertForTokenClassification,
    ModernBertForQuestionAnswering,
    ModernBertForMultipleChoice,
)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"
os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

RANDOM_SEED = 2025
VALID_FRACTION = 0.10

MAX_EPOCHS = int(os.environ.get("MAX_EPOCHS", "2"))
EARLY_STOPPING_PATIENCE = int(os.environ.get("EARLY_STOPPING_PATIENCE", "2"))
TRAIN_BATCH_SIZE = int(os.environ.get("TRAIN_BATCH_SIZE", "6"))
EVAL_BATCH_SIZE = int(os.environ.get("EVAL_BATCH_SIZE", "12"))
GRADIENT_ACCUMULATION_STEPS = int(os.environ.get("GRADIENT_ACCUMULATION_STEPS", "4"))
NUM_WORKERS = max(2, int(os.environ.get("NUM_WORKERS", "4")))
MAX_SEQUENCE_LENGTH = int(os.environ.get("MAX_SEQUENCE_LENGTH", "256"))
MAX_WINDOWS_PER_COMMENT = int(os.environ.get("MAX_WINDOWS_PER_COMMENT", "2"))
WINDOW_STRIDE = int(os.environ.get("WINDOW_STRIDE", "64"))
WARMUP_FRACTION = float(os.environ.get("WARMUP_FRACTION", "0.06"))
MAX_GRAD_NORM = float(os.environ.get("MAX_GRAD_NORM", "1.0"))

BEST_CHECKPOINT_PATH = os.path.join(WORKING_DIR, "best_toxicity_model.pt")

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

AUXILIARY_LABEL_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

LABEL_COLUMNS = ["target"] + AUXILIARY_LABEL_COLUMNS + IDENTITY_COLUMNS
TRAIN_COLUMNS = ["id", "comment_text", "created_date", "target"]
TRAIN_COLUMNS += AUXILIARY_LABEL_COLUMNS + IDENTITY_COLUMNS

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(RANDOM_SEED)
    try:
        torch.set_float32_matmul_precision("high")
    except AttributeError:
        pass


def normalize_comment_text(series: pd.Series) -> pd.Series:
    text = series.fillna("").astype(str)
    text = text.str.normalize("NFKC")
    text = text.map(html.unescape)
    text = text.str.replace(r"<\s*br\s*/?\s*>", "\n", regex=True, case=False)
    text = text.str.replace(r"[\u0000-\u001f\u007f-\u009f]+", " ", regex=True)
    text = text.str.replace(
        r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]{}]+",
        " [URL] ",
        regex=True,
    )
    text = text.str.replace(
        r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b",
        " [EMAIL] ",
        regex=True,
    )
    text = text.str.replace(r"(?<![\w@])@[\w_]{2,}", " [USER] ", regex=True)
    return text.str.replace(r"\s+", " ", regex=True).str.strip()


def make_text_features(raw_text: pd.Series, normalized_text: pd.Series) -> pd.DataFrame:
    raw = raw_text.fillna("").astype(str)
    text = normalized_text.fillna("").astype(str)

    char_count = text.str.len().clip(lower=0).astype(np.float32)
    word_count = text.str.count(r"\S+").clip(lower=0).astype(np.float32)
    uppercase_count = text.str.count(r"[A-Z]").astype(np.float32)
    alphabetic_count = text.str.count(r"[A-Za-z]").astype(np.float32)
    exclamation_count = text.str.count("!").astype(np.float32)
    question_count = text.str.count(r"\?").astype(np.float32)
    punctuation_count = text.str.count(r"[!?.;,:\-]").astype(np.float32)
    repeated_punctuation = text.str.count(r"[!?]{2,}").astype(np.float32)
    quote_count = text.str.count(r"""["']""").astype(np.float32)
    digit_count = text.str.count(r"\d").astype(np.float32)
    non_ascii_count = text.str.count(r"[^\x00-\x7F]").astype(np.float32)
    url_count = raw.str.count(r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]{}]+").astype(
        np.float32
    )
    email_count = raw.str.count(
        r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b"
    ).astype(np.float32)

    denom_chars = np.maximum(char_count.to_numpy(), 1.0)
    denom_letters = np.maximum(alphabetic_count.to_numpy(), 1.0)

    return pd.DataFrame(
        {
            "feat_log_char_count": np.log1p(char_count.to_numpy()),
            "feat_log_word_count": np.log1p(word_count.to_numpy()),
            "feat_log_exclamation_count": np.log1p(exclamation_count.to_numpy()),
            "feat_log_question_count": np.log1p(question_count.to_numpy()),
            "feat_log_punctuation_count": np.log1p(punctuation_count.to_numpy()),
            "feat_log_repeated_punctuation": np.log1p(repeated_punctuation.to_numpy()),
            "feat_log_quote_count": np.log1p(quote_count.to_numpy()),
            "feat_log_digit_count": np.log1p(digit_count.to_numpy()),
            "feat_log_non_ascii_count": np.log1p(non_ascii_count.to_numpy()),
            "feat_log_url_count": np.log1p(url_count.to_numpy()),
            "feat_log_email_count": np.log1p(email_count.to_numpy()),
            "feat_uppercase_ratio": uppercase_count.to_numpy() / denom_letters,
            "feat_punctuation_ratio": punctuation_count.to_numpy() / denom_chars,
            "feat_digit_ratio": digit_count.to_numpy() / denom_chars,
            "feat_is_short_comment": (word_count.to_numpy() <= 3).astype(np.float32),
            "feat_is_empty_comment": (char_count.to_numpy() == 0).astype(np.float32),
        },
        index=text.index,
        dtype=np.float32,
    )


SWAP_MAP = {
    "men": "women",
    "man": "woman",
    "male": "female",
    "boys": "girls",
    "boy": "girl",
    "women": "men",
    "woman": "man",
    "female": "male",
    "girls": "boys",
    "girl": "boy",
    "christians": "muslims",
    "christian": "muslim",
    "muslims": "christians",
    "muslim": "christian",
    "jews": "christians",
    "jewish": "christian",
    "black": "white",
    "blacks": "whites",
    "white": "black",
    "whites": "blacks",
    "asians": "latinos",
    "asian": "latino",
    "latinos": "asians",
    "latino": "asian",
    "gay": "straight",
    "gays": "straight people",
    "lesbian": "heterosexual woman",
    "lesbians": "heterosexual women",
    "straight": "gay",
    "heterosexual": "homosexual",
    "transgender": "cisgender",
    "trans": "cisgender",
    "atheists": "christians",
    "atheist": "christian",
    "buddhists": "hindus",
    "buddhist": "hindu",
    "hindus": "buddhists",
    "hindu": "buddhist",
}

identity_swap_pattern = re.compile(
    r"\b(" + "|".join(sorted(map(re.escape, SWAP_MAP), key=len, reverse=True)) + r")\b",
    flags=re.IGNORECASE,
)


def apply_identity_swap(text: str) -> str:
    def replace_match(match: re.Match) -> str:
        original = match.group(0)
        replacement = SWAP_MAP[original.lower()]
        if original.isupper():
            return replacement.upper()
        if original[:1].isupper():
            return replacement.capitalize()
        return replacement

    return identity_swap_pattern.sub(replace_match, text)


train_dtypes = {column: np.float32 for column in LABEL_COLUMNS}
train_dtypes["id"] = np.int64

train_df = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    usecols=TRAIN_COLUMNS,
    dtype=train_dtypes,
    low_memory=False,
)
test_df = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    usecols=["id", "comment_text"],
    dtype={"id": np.int64},
    low_memory=False,
)
sample_submission = pd.read_csv(os.path.join(INPUT_DIR, "sample_submission.csv"))

if list(sample_submission.columns) != ["id", "prediction"]:
    raise ValueError("sample_submission.csv must contain columns ['id', 'prediction'].")
if not np.array_equal(test_df["id"].to_numpy(), sample_submission["id"].to_numpy()):
    raise ValueError("test.csv row order must match sample_submission.csv.")

train_df["model_text"] = normalize_comment_text(train_df["comment_text"])
test_df["model_text"] = normalize_comment_text(test_df["comment_text"])

train_df["text_group"] = pd.util.hash_pandas_object(
    train_df["model_text"],
    index=False,
).to_numpy(dtype=np.uint64)

created_datetime = pd.to_datetime(
    train_df["created_date"],
    errors="coerce",
    utc=True,
)
valid_dates = created_datetime.dropna()

if len(valid_dates) < 1000:
    ordered_ids = train_df["id"].rank(method="first", pct=True)
    initial_valid_mask = ordered_ids >= (1.0 - VALID_FRACTION)
    split_strategy = "forward_id_fallback_with_duplicate_purge"
else:
    cutoff_date = valid_dates.quantile(1.0 - VALID_FRACTION)
    initial_valid_mask = created_datetime >= cutoff_date
    split_strategy = "forward_created_date_with_duplicate_purge"

if int(initial_valid_mask.sum()) < 1000:
    raise RuntimeError("Validation split unexpectedly contains fewer than 1,000 rows.")

validation_groups = train_df.loc[initial_valid_mask, "text_group"].unique()
validation_mask = train_df["text_group"].isin(validation_groups)
training_mask = ~validation_mask

if int(training_mask.sum()) == 0 or int(validation_mask.sum()) == 0:
    raise RuntimeError("Duplicate-purged split produced an empty partition.")

raw_train_df = train_df.loc[training_mask].copy()
raw_valid_df = train_df.loc[validation_mask].copy()
del train_df


def finalize_partition(frame: pd.DataFrame, is_training: bool) -> pd.DataFrame:
    text_features = make_text_features(frame["comment_text"], frame["model_text"])

    output = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(),
            "model_text": frame["model_text"].to_numpy(),
        },
        index=frame.index,
    )
    output = pd.concat([output, text_features], axis=1)

    if is_training:
        for label_column in LABEL_COLUMNS:
            output[label_column] = frame[label_column].astype(np.float32)

        output["target_binary"] = (output["target"].to_numpy() >= 0.5).astype(np.int8)

        identity_values = frame[IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
        output["identity_annotated"] = (
            frame[IDENTITY_COLUMNS].notna().any(axis=1).to_numpy()
        ).astype(np.int8)
        output["any_identity_mentioned"] = (identity_values.max(axis=1) >= 0.5).astype(
            np.int8
        )

        official_values = (
            frame[OFFICIAL_IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
        )
        output["any_official_identity_mentioned"] = (
            official_values.max(axis=1) >= 0.5
        ).astype(np.int8)

        output["counterfactual_text"] = ""
        output["identity_swap_applied"] = np.int8(0)

        eligible = output["any_identity_mentioned"].to_numpy(dtype=bool)
        eligible_indices = output.index[eligible]
        if len(eligible_indices) > 0:
            swapped = output.loc[eligible_indices, "model_text"].map(
                apply_identity_swap
            )
            changed = (
                swapped.to_numpy()
                != output.loc[eligible_indices, "model_text"].to_numpy()
            )
            output.loc[eligible_indices, "counterfactual_text"] = swapped.to_numpy()
            output.loc[eligible_indices, "identity_swap_applied"] = changed.astype(
                np.int8
            )

    return output.reset_index(drop=True)


train_processed = finalize_partition(raw_train_df, is_training=True)
valid_processed = finalize_partition(raw_valid_df, is_training=True)

test_feature_frame = pd.DataFrame(
    {
        "id": test_df["id"].to_numpy(),
        "model_text": test_df["model_text"].to_numpy(),
    }
)
test_features = make_text_features(test_df["comment_text"], test_df["model_text"])
test_processed = pd.concat([test_feature_frame, test_features], axis=1).reset_index(
    drop=True
)

feature_columns = [
    column for column in train_processed.columns if column.startswith("feat_")
]

feature_scaler = StandardScaler()
train_processed.loc[:, feature_columns] = feature_scaler.fit_transform(
    train_processed[feature_columns]
).astype(np.float32)
valid_processed.loc[:, feature_columns] = feature_scaler.transform(
    valid_processed[feature_columns]
).astype(np.float32)
test_processed.loc[:, feature_columns] = feature_scaler.transform(
    test_processed[feature_columns]
).astype(np.float32)

train_processed.to_pickle(
    os.path.join(WORKING_DIR, "train_processed.pkl"),
    protocol=pickle.HIGHEST_PROTOCOL,
)
valid_processed.to_pickle(
    os.path.join(WORKING_DIR, "valid_processed.pkl"),
    protocol=pickle.HIGHEST_PROTOCOL,
)
test_processed.to_pickle(
    os.path.join(WORKING_DIR, "test_processed.pkl"),
    protocol=pickle.HIGHEST_PROTOCOL,
)

with open(os.path.join(WORKING_DIR, "text_feature_scaler.pkl"), "wb") as file:
    pickle.dump(feature_scaler, file, protocol=pickle.HIGHEST_PROTOCOL)

manifest = {
    "split_strategy": split_strategy,
    "random_seed": RANDOM_SEED,
    "valid_fraction_requested": VALID_FRACTION,
    "train_rows": int(len(train_processed)),
    "validation_rows": int(len(valid_processed)),
    "test_rows": int(len(test_processed)),
    "feature_columns": feature_columns,
    "label_columns": LABEL_COLUMNS,
    "official_identity_columns": OFFICIAL_IDENTITY_COLUMNS,
    "submission_columns": ["id", "prediction"],
    "validation_is_duplicate_disjoint": True,
}
with open(
    os.path.join(WORKING_DIR, "data_manifest.json"), "w", encoding="utf-8"
) as file:
    json.dump(manifest, file, indent=2)

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)


class HierarchicalModernBertToxicityModel(nn.Module):
    def __init__(self, num_numeric_features: int, dropout: float = 0.20) -> None:
        super().__init__()

        self.encoder_with_head = ModernBertForSequenceClassification.from_pretrained(
            model_id,
            num_labels=1,
            ignore_mismatched_sizes=True,
        )
        self.encoder = self.encoder_with_head.model
        hidden_size = self.encoder.config.hidden_size

        self.token_norm = nn.LayerNorm(hidden_size)
        self.window_attention = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )
        self.numeric_tower = nn.Sequential(
            nn.LayerNorm(num_numeric_features),
            nn.Linear(num_numeric_features, 64),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(64, 64),
            nn.GELU(),
        )
        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_size + 64),
            nn.Dropout(dropout),
            nn.Linear(hidden_size + 64, hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 1),
        )

    @staticmethod
    def masked_mean_pool(
        token_embeddings: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        mask = attention_mask.unsqueeze(-1).to(token_embeddings.dtype)
        summed = (token_embeddings * mask).sum(dim=1)
        denominator = mask.sum(dim=1).clamp_min(1.0)
        return summed / denominator

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        numeric_features: torch.Tensor,
        window_mask: torch.Tensor = None,
    ) -> torch.Tensor:
        if input_ids.ndim == 2:
            input_ids = input_ids.unsqueeze(1)
            attention_mask = attention_mask.unsqueeze(1)

        if input_ids.ndim != 3 or attention_mask.ndim != 3:
            raise ValueError(
                "Expected [batch, sequence] or [batch, windows, sequence]."
            )

        batch_size, num_windows, sequence_length = input_ids.shape
        flat_input_ids = input_ids.reshape(batch_size * num_windows, sequence_length)
        flat_attention_mask = attention_mask.reshape(
            batch_size * num_windows,
            sequence_length,
        )

        encoder_output = self.encoder(
            input_ids=flat_input_ids,
            attention_mask=flat_attention_mask,
            return_dict=True,
        )

        pooled_tokens = self.masked_mean_pool(
            encoder_output.last_hidden_state,
            flat_attention_mask,
        )
        window_embeddings = self.token_norm(
            pooled_tokens.reshape(batch_size, num_windows, -1)
        )

        if window_mask is None:
            window_mask = attention_mask.any(dim=-1)
        window_mask = window_mask.bool()

        window_scores = self.window_attention(window_embeddings).squeeze(-1)
        window_scores = window_scores.masked_fill(~window_mask, -1e4)
        window_weights = torch.softmax(window_scores, dim=1)

        document_embedding = torch.sum(
            window_embeddings * window_weights.unsqueeze(-1),
            dim=1,
        )
        numeric_embedding = self.numeric_tower(numeric_features.float())

        return self.classifier(
            torch.cat([document_embedding, numeric_embedding], dim=-1)
        ).squeeze(-1)


class IdentityGroupDROSoftBCELoss(nn.Module):
    def __init__(
        self,
        num_identity_groups: int,
        robust_weight: float = 0.60,
        dro_eta: float = 0.08,
        min_group_examples: int = 2,
    ) -> None:
        super().__init__()
        self.num_identity_groups = num_identity_groups
        self.robust_weight = robust_weight
        self.dro_eta = dro_eta
        self.min_group_examples = min_group_examples

        self.register_buffer(
            "group_logits",
            torch.zeros(1 + 2 * num_identity_groups, dtype=torch.float32),
        )

    @torch.no_grad()
    def update_group_distribution(
        self,
        group_losses: torch.Tensor,
        group_available: torch.Tensor,
    ) -> None:
        updated_logits = self.group_logits.clone()
        updated_logits[group_available] += (
            self.dro_eta * group_losses[group_available].detach().float()
        )
        updated_logits.clamp_(min=-8.0, max=8.0)
        self.group_logits.copy_(updated_logits)

    def forward(
        self,
        logits: torch.Tensor,
        soft_targets: torch.Tensor,
        identity_values: torch.Tensor,
        identity_annotated: torch.Tensor,
    ) -> torch.Tensor:
        per_example_loss = F.binary_cross_entropy_with_logits(
            logits.float(),
            soft_targets.float().clamp(0.0, 1.0),
            reduction="none",
        )

        target_positive = soft_targets >= 0.5
        labels_known = identity_annotated.bool()

        group_masks = [torch.ones_like(target_positive, dtype=torch.bool)]
        for identity_index in range(self.num_identity_groups):
            subgroup = (
                identity_values[:, identity_index].float() >= 0.5
            ) & labels_known
            group_masks.append(subgroup & ~target_positive)
            group_masks.append(subgroup & target_positive)

        group_losses = []
        group_available = []

        for group_mask in group_masks:
            available = group_mask.sum() >= self.min_group_examples
            group_available.append(available)
            if bool(available):
                group_losses.append(per_example_loss[group_mask].mean())
            else:
                group_losses.append(per_example_loss.mean().detach())

        group_losses = torch.stack(group_losses)
        group_available = torch.stack(group_available).bool()

        if self.training:
            self.update_group_distribution(group_losses, group_available)

        active_logits = self.group_logits.masked_fill(~group_available, -1e4)
        robust_weights = torch.softmax(active_logits, dim=0)
        robust_loss = torch.sum(robust_weights * group_losses)
        global_loss = per_example_loss.mean()

        return (
            1.0 - self.robust_weight
        ) * global_loss + self.robust_weight * robust_loss


class ToxicityFrameDataset(Dataset):
    def __init__(self, frame: pd.DataFrame, include_labels: bool) -> None:
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=False)
        self.numeric_features = frame.loc[:, feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.include_labels = include_labels

        if include_labels:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=True)
            self.identity_values = (
                frame.loc[:, OFFICIAL_IDENTITY_COLUMNS]
                .fillna(0.0)
                .to_numpy(dtype=np.float32, copy=True)
            )
            self.identity_annotated = frame["identity_annotated"].to_numpy(
                dtype=np.int64,
                copy=True,
            )

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, index: int):
        if self.include_labels:
            return (
                self.texts[index],
                self.numeric_features[index],
                self.targets[index],
                self.identity_values[index],
                self.identity_annotated[index],
            )
        return self.texts[index], self.numeric_features[index], None, None, None


class HierarchicalBatchCollator:
    def __init__(
        self,
        tokenizer_object,
        max_length: int,
        max_windows: int,
        stride: int,
    ) -> None:
        self.tokenizer = tokenizer_object
        self.max_length = max_length
        self.max_windows = max_windows
        self.stride = stride
        self.pad_token_id = (
            tokenizer_object.pad_token_id
            if tokenizer_object.pad_token_id is not None
            else 0
        )

    def __call__(self, records):
        texts = [record[0] for record in records]
        numeric_features = torch.as_tensor(
            np.stack([record[1] for record in records]),
            dtype=torch.float32,
        )

        tokenized = self.tokenizer(
            texts,
            truncation=True,
            max_length=self.max_length,
            stride=self.stride,
            return_overflowing_tokens=True,
            padding=True,
            pad_to_multiple_of=8,
            return_tensors="pt",
        )

        overflow_mapping = tokenized.pop("overflow_to_sample_mapping").tolist()
        flat_input_ids = tokenized["input_ids"]
        flat_attention_mask = tokenized["attention_mask"]

        per_example_windows = [[] for _ in range(len(records))]
        for flat_index, example_index in enumerate(overflow_mapping):
            per_example_windows[example_index].append(flat_index)

        selected_windows = []
        for windows in per_example_windows:
            if len(windows) <= self.max_windows:
                selected_windows.append(windows)
            elif self.max_windows == 1:
                selected_windows.append([windows[0]])
            else:
                selected_windows.append([windows[0], windows[-1]])

        windows_in_batch = max(len(windows) for windows in selected_windows)
        batch_size = len(records)
        sequence_length = flat_input_ids.shape[1]

        input_ids = torch.full(
            (batch_size, windows_in_batch, sequence_length),
            fill_value=self.pad_token_id,
            dtype=flat_input_ids.dtype,
        )
        attention_mask = torch.zeros(
            (batch_size, windows_in_batch, sequence_length),
            dtype=flat_attention_mask.dtype,
        )
        window_mask = torch.zeros(
            (batch_size, windows_in_batch),
            dtype=torch.bool,
        )

        for batch_index, windows in enumerate(selected_windows):
            window_count = len(windows)
            input_ids[batch_index, :window_count] = flat_input_ids[windows]
            attention_mask[batch_index, :window_count] = flat_attention_mask[windows]
            window_mask[batch_index, :window_count] = True

        batch = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "window_mask": window_mask,
            "numeric_features": numeric_features,
        }

        if records[0][2] is not None:
            batch["targets"] = torch.as_tensor(
                np.asarray([record[2] for record in records], dtype=np.float32),
                dtype=torch.float32,
            )
            batch["identity_values"] = torch.as_tensor(
                np.stack([record[3] for record in records]),
                dtype=torch.float32,
            )
            batch["identity_annotated"] = torch.as_tensor(
                np.asarray([record[4] for record in records], dtype=np.int64),
                dtype=torch.bool,
            )

        return batch


def checked_auc(binary_labels, predictions, subset_name: str) -> float:
    binary_labels = np.asarray(binary_labels, dtype=np.int8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if binary_labels.size == 0 or np.unique(binary_labels).size != 2:
        raise RuntimeError(
            f"Official AUC is undefined for validation subset '{subset_name}'."
        )
    return float(roc_auc_score(binary_labels, predictions))


def generalized_power_mean(metric_values, power: int = -5) -> float:
    metric_values = np.asarray(metric_values, dtype=np.float64)

    if metric_values.size == 0:
        raise RuntimeError("Cannot compute generalized mean of an empty metric set.")
    if np.any(metric_values < 0.0) or np.any(metric_values > 1.0):
        raise RuntimeError("AUC values must be in [0, 1].")
    if power < 0 and np.any(metric_values == 0.0):
        return 0.0

    return float(np.mean(np.power(metric_values, power)) ** (1.0 / power))


def official_jigsaw_metric(
    validation_frame: pd.DataFrame,
    predictions: np.ndarray,
) -> float:
    targets = (
        validation_frame["target"].to_numpy(dtype=np.float32, copy=False) >= 0.5
    ).astype(np.int8)

    if len(targets) != len(predictions):
        raise RuntimeError("Validation labels and predictions have different lengths.")

    overall_auc = checked_auc(targets, predictions, "overall")

    identity_matrix = (
        validation_frame.loc[:, OFFICIAL_IDENTITY_COLUMNS]
        .fillna(0.0)
        .to_numpy(dtype=np.float32, copy=False)
        >= 0.5
    )

    subgroup_aucs = []
    bpsn_aucs = []
    bnsp_aucs = []

    for identity_index, identity_name in enumerate(OFFICIAL_IDENTITY_COLUMNS):
        subgroup = identity_matrix[:, identity_index]

        subgroup_mask = subgroup
        bpsn_mask = (subgroup & (targets == 0)) | ((~subgroup) & (targets == 1))
        bnsp_mask = (subgroup & (targets == 1)) | ((~subgroup) & (targets == 0))

        subgroup_aucs.append(
            checked_auc(
                targets[subgroup_mask],
                predictions[subgroup_mask],
                f"{identity_name}_subgroup",
            )
        )
        bpsn_aucs.append(
            checked_auc(
                targets[bpsn_mask],
                predictions[bpsn_mask],
                f"{identity_name}_bpsn",
            )
        )
        bnsp_aucs.append(
            checked_auc(
                targets[bnsp_mask],
                predictions[bnsp_mask],
                f"{identity_name}_bnsp",
            )
        )

    bias_score = (
        generalized_power_mean(subgroup_aucs, power=-5)
        + generalized_power_mean(bpsn_aucs, power=-5)
        + generalized_power_mean(bnsp_aucs, power=-5)
    )

    return float(0.25 * overall_auc + 0.25 * bias_score)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"

model = HierarchicalModernBertToxicityModel(
    num_numeric_features=len(feature_columns),
    dropout=0.20,
)

if hasattr(model.encoder, "gradient_checkpointing_enable"):
    model.encoder.gradient_checkpointing_enable()

model = model.to(device)

criterion = IdentityGroupDROSoftBCELoss(
    num_identity_groups=len(OFFICIAL_IDENTITY_COLUMNS),
    robust_weight=0.60,
    dro_eta=0.08,
    min_group_examples=2,
).to(device)

encoder_parameter_names = {
    name for name, _ in model.named_parameters() if name.startswith("encoder.")
}
encoder_parameters = [
    parameter
    for name, parameter in model.named_parameters()
    if name in encoder_parameter_names and parameter.requires_grad
]
head_parameters = [
    parameter
    for name, parameter in model.named_parameters()
    if name not in encoder_parameter_names and parameter.requires_grad
]

optimizer = AdamW(
    [
        {
            "params": encoder_parameters,
            "lr": 1.5e-5,
            "weight_decay": 0.01,
        },
        {
            "params": head_parameters,
            "lr": 1.0e-4,
            "weight_decay": 0.01,
        },
    ],
    betas=(0.9, 0.999),
    eps=1e-8,
)

collator = HierarchicalBatchCollator(
    tokenizer_object=tokenizer,
    max_length=MAX_SEQUENCE_LENGTH,
    max_windows=MAX_WINDOWS_PER_COMMENT,
    stride=WINDOW_STRIDE,
)

train_dataset = ToxicityFrameDataset(train_processed, include_labels=True)
valid_dataset = ToxicityFrameDataset(valid_processed, include_labels=True)
test_dataset = ToxicityFrameDataset(test_processed, include_labels=False)

loader_kwargs = {
    "num_workers": NUM_WORKERS,
    "pin_memory": use_amp,
    "persistent_workers": NUM_WORKERS > 0,
    "collate_fn": collator,
}
if NUM_WORKERS > 0:
    loader_kwargs["prefetch_factor"] = 2

train_generator = torch.Generator()
train_generator.manual_seed(RANDOM_SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    drop_last=False,
    generator=train_generator,
    **loader_kwargs,
)
valid_loader = DataLoader(
    valid_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)
test_loader = DataLoader(
    test_dataset,
    batch_size=EVAL_BATCH_SIZE,
    shuffle=False,
    drop_last=False,
    **loader_kwargs,
)

updates_per_epoch = math.ceil(len(train_loader) / max(GRADIENT_ACCUMULATION_STEPS, 1))
total_updates = max(updates_per_epoch * MAX_EPOCHS, 1)
warmup_updates = int(total_updates * WARMUP_FRACTION)


def learning_rate_multiplier(update_number: int) -> float:
    if warmup_updates > 0 and update_number < warmup_updates:
        return float(update_number + 1) / float(max(warmup_updates, 1))

    progress = float(update_number - warmup_updates) / float(
        max(total_updates - warmup_updates, 1)
    )
    progress = min(max(progress, 0.0), 1.0)
    return max(0.10, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)
amp_scaler = torch.cuda.amp.GradScaler(enabled=use_amp)


def move_batch_to_device(batch: dict, include_labels: bool) -> dict:
    moved = {
        "input_ids": batch["input_ids"].to(device, non_blocking=True),
        "attention_mask": batch["attention_mask"].to(device, non_blocking=True),
        "window_mask": batch["window_mask"].to(device, non_blocking=True),
        "numeric_features": batch["numeric_features"].to(device, non_blocking=True),
    }

    if include_labels:
        moved["targets"] = batch["targets"].to(device, non_blocking=True)
        moved["identity_values"] = batch["identity_values"].to(
            device,
            non_blocking=True,
        )
        moved["identity_annotated"] = batch["identity_annotated"].to(
            device,
            non_blocking=True,
        )

    return moved


@torch.inference_mode()
def predict_from_loader(data_loader: DataLoader) -> np.ndarray:
    model.eval()
    prediction_parts = []

    for batch in data_loader:
        batch = move_batch_to_device(
            batch,
            include_labels=("targets" in batch),
        )

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
                window_mask=batch["window_mask"],
            )

        prediction_parts.append(torch.sigmoid(logits.float()).cpu().numpy())

    predictions = np.concatenate(prediction_parts).astype(np.float64, copy=False)

    if not np.isfinite(predictions).all():
        raise RuntimeError("Model inference produced non-finite predictions.")

    return predictions


best_score = -np.inf
epochs_without_improvement = 0
optimizer.zero_grad(set_to_none=True)

for epoch_index in range(MAX_EPOCHS):
    model.train()
    running_loss = 0.0
    seen_examples = 0

    for batch_index, batch in enumerate(train_loader):
        batch = move_batch_to_device(batch, include_labels=True)

        with torch.cuda.amp.autocast(enabled=use_amp):
            logits = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                numeric_features=batch["numeric_features"],
                window_mask=batch["window_mask"],
            )
            batch_loss = criterion(
                logits=logits,
                soft_targets=batch["targets"],
                identity_values=batch["identity_values"],
                identity_annotated=batch["identity_annotated"],
            )
            scaled_loss = batch_loss / GRADIENT_ACCUMULATION_STEPS

        if not torch.isfinite(scaled_loss):
            raise FloatingPointError("Encountered non-finite training loss.")

        amp_scaler.scale(scaled_loss).backward()

        should_update = (
            batch_index + 1
        ) % GRADIENT_ACCUMULATION_STEPS == 0 or batch_index + 1 == len(train_loader)

        if should_update:
            amp_scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), MAX_GRAD_NORM)
            amp_scaler.step(optimizer)
            amp_scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

        batch_examples = batch["targets"].shape[0]
        running_loss += float(batch_loss.detach().cpu()) * batch_examples
        seen_examples += batch_examples

    validation_predictions = predict_from_loader(valid_loader)
    validation_score = official_jigsaw_metric(
        valid_processed,
        validation_predictions,
    )
    mean_train_loss = running_loss / max(seen_examples, 1)

    if validation_score > best_score:
        best_score = validation_score
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": epoch_index + 1,
                "validation_score": float(validation_score),
                "model_state_dict": model.state_dict(),
                "criterion_state_dict": criterion.state_dict(),
                "feature_columns": list(feature_columns),
                "official_identity_columns": list(OFFICIAL_IDENTITY_COLUMNS),
                "max_sequence_length": MAX_SEQUENCE_LENGTH,
                "max_windows_per_comment": MAX_WINDOWS_PER_COMMENT,
                "window_stride": WINDOW_STRIDE,
            },
            BEST_CHECKPOINT_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch_index + 1}/{MAX_EPOCHS} "
        f"loss={mean_train_loss:.6f} official_score={validation_score:.6f}"
    )

    if epochs_without_improvement >= EARLY_STOPPING_PATIENCE:
        break

if not os.path.exists(BEST_CHECKPOINT_PATH):
    raise RuntimeError("No valid model checkpoint was saved.")

checkpoint = torch.load(BEST_CHECKPOINT_PATH, map_location=device)
model.load_state_dict(checkpoint["model_state_dict"])
criterion.load_state_dict(checkpoint["criterion_state_dict"])

validation_predictions = predict_from_loader(valid_loader)
score = official_jigsaw_metric(valid_processed, validation_predictions)

test_predictions = predict_from_loader(test_loader)

if len(test_predictions) != len(test_processed):
    raise RuntimeError("Test prediction count does not match test rows.")

submission = pd.DataFrame(
    {
        "id": test_processed["id"].to_numpy(copy=False),
        "prediction": test_predictions.astype(np.float64, copy=False),
    }
)

if list(submission.columns) != ["id", "prediction"]:
    raise RuntimeError("Submission columns do not match required format.")
if submission["id"].duplicated().any():
    raise RuntimeError("Submission contains duplicate IDs.")
if not np.isfinite(submission["prediction"].to_numpy()).all():
    raise RuntimeError("Submission contains non-finite predictions.")

submission.to_csv(
    os.path.join(SUBMISSION_DIR, "submission_c84551911dc149dea5440dad19965f21.csv"),
    index=False,
)

print(f"Final Validation Score: {score}")
