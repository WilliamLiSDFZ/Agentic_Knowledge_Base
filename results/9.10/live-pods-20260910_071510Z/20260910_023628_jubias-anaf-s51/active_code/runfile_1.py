import os
os.sched_setaffinity(0, {8, 7})
import os
import gc
import json
import math
import random
from collections import defaultdict

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer


os.environ["TOKENIZERS_PARALLELISM"] = "false"

INPUT_DIR = "./input"
WORKING_DIR = "./working"
SUBMISSION_DIR = "./submission"

TRAIN_PATH = os.path.join(INPUT_DIR, "train.csv")
TEST_PATH = os.path.join(INPUT_DIR, "test.csv")
BEST_MODEL_PATH = os.path.join(WORKING_DIR, "best_debiased_deberta_model.pt")
METRICS_PATH = os.path.join(WORKING_DIR, "training_metrics.json")

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)

SEED = 3407
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True


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

CORE_LABEL_COLUMNS = (
    [
        "id",
        "target",
        "toxicity_annotator_count",
        "identity_annotator_count",
    ]
    + TOXICITY_AUX_COLUMNS
    + IDENTITY_COLUMNS
)


def normalize_comment_text(text_series):
    text = text_series.fillna("").astype(str).str.normalize("NFKC")
    text = text.str.replace(r"[\u200b-\u200d\ufeff]", "", regex=True)
    text = text.str.replace(r"<\s*/?\s*[A-Za-z][^>]{0,100}>", " ", regex=True)
    text = text.str.replace(r"(?i)(?:https?://|www\.)\S+", " <URL> ", regex=True)
    text = text.str.replace(
        r"(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b",
        " <EMAIL> ",
        regex=True,
    )
    text = text.str.replace(r"(?<!\w)@\w+", " <USER> ", regex=True)
    text = text.str.replace("&amp;", "&", regex=False)
    text = text.str.replace("&lt;", "<", regex=False)
    text = text.str.replace("&gt;", ">", regex=False)
    text = text.str.replace("&quot;", '"', regex=False)
    text = text.str.replace("&#39;", "'", regex=False)
    text = text.str.replace(r"[ \t\r\f\v]+", " ", regex=True)
    text = text.str.replace(r"\n{3,}", "\n\n", regex=True)
    return text.str.strip()


def build_text_inputs(frame):
    original_text = frame["comment_text"].fillna("").astype(str)
    model_text = normalize_comment_text(original_text)

    char_count = model_text.str.len().to_numpy(dtype=np.float32)
    word_count = model_text.str.count(r"\b\w+\b").to_numpy(dtype=np.float32)
    alpha_count = model_text.str.count(r"[A-Za-z]").to_numpy(dtype=np.float32)
    uppercase_count = model_text.str.count(r"[A-Z]").to_numpy(dtype=np.float32)

    exclamation_count = model_text.str.count("!").to_numpy(dtype=np.float32)
    question_count = model_text.str.count(r"\?").to_numpy(dtype=np.float32)
    punctuation_count = model_text.str.count(r"[!?,.;:]").to_numpy(dtype=np.float32)
    digit_count = model_text.str.count(r"\d").to_numpy(dtype=np.float32)
    newline_count = original_text.str.count(r"\n").to_numpy(dtype=np.float32)
    url_count = model_text.str.count(r"<URL>").to_numpy(dtype=np.float32)
    user_count = model_text.str.count(r"<USER>").to_numpy(dtype=np.float32)
    email_count = model_text.str.count(r"<EMAIL>").to_numpy(dtype=np.float32)
    quote_count = model_text.str.count(r"""["']""").to_numpy(dtype=np.float32)
    caps_word_count = model_text.str.count(r"\b[A-Z]{2,}\b").to_numpy(dtype=np.float32)

    repeated_punctuation = model_text.str.contains(
        r"([!?.])\1{2,}",
        regex=True,
    ).to_numpy(dtype=np.float32)

    elongated_word = model_text.str.contains(
        r"(?i)([a-z])\1\1",
        regex=True,
    ).to_numpy(dtype=np.float32)

    non_ascii_count = model_text.str.count(r"[^\x00-\x7F]").to_numpy(dtype=np.float32)

    safe_char_count = np.maximum(char_count, 1.0)
    safe_alpha_count = np.maximum(alpha_count, 1.0)
    safe_word_count = np.maximum(word_count, 1.0)

    numerical_features = np.column_stack(
        [
            np.log1p(char_count),
            np.log1p(word_count),
            np.log1p(exclamation_count),
            np.log1p(question_count),
            np.log1p(punctuation_count),
            np.log1p(digit_count),
            np.log1p(newline_count),
            np.log1p(url_count),
            np.log1p(user_count),
            np.log1p(email_count),
            np.log1p(quote_count),
            np.log1p(caps_word_count),
            np.log1p(non_ascii_count),
            uppercase_count / safe_alpha_count,
            punctuation_count / safe_char_count,
            digit_count / safe_char_count,
            caps_word_count / safe_word_count,
            repeated_punctuation,
            elongated_word,
        ]
    ).astype(np.float32)

    feature_names = [
        "txt_log_char_count",
        "txt_log_word_count",
        "txt_log_exclamation_count",
        "txt_log_question_count",
        "txt_log_punctuation_count",
        "txt_log_digit_count",
        "txt_log_newline_count",
        "txt_log_url_count",
        "txt_log_user_count",
        "txt_log_email_count",
        "txt_log_quote_count",
        "txt_log_caps_word_count",
        "txt_log_non_ascii_count",
        "txt_uppercase_alpha_ratio",
        "txt_punctuation_ratio",
        "txt_digit_ratio",
        "txt_caps_word_ratio",
        "txt_repeated_punctuation",
        "txt_elongated_word",
    ]

    output = pd.DataFrame(
        {
            "id": frame["id"].to_numpy(),
            "model_text": model_text.to_numpy(),
        }
    )
    output[feature_names] = numerical_features
    return output, feature_names


def build_labels(frame):
    label_frame = pd.DataFrame({"id": frame["id"].to_numpy()})

    for column in ["target"] + TOXICITY_AUX_COLUMNS + IDENTITY_COLUMNS:
        label_frame[column] = pd.to_numeric(
            frame[column],
            errors="coerce",
        ).astype(np.float32)

    label_frame["toxicity_annotator_count"] = (
        pd.to_numeric(
            frame["toxicity_annotator_count"],
            errors="coerce",
        )
        .fillna(0)
        .astype(np.int32)
    )

    label_frame["identity_annotator_count"] = (
        pd.to_numeric(
            frame["identity_annotator_count"],
            errors="coerce",
        )
        .fillna(0)
        .astype(np.int32)
    )

    label_frame["target_binary"] = (label_frame["target"].fillna(0.0) >= 0.5).astype(
        np.uint8
    )

    identity_values = (
        label_frame[IDENTITY_COLUMNS].fillna(0.0).to_numpy(dtype=np.float32)
    )
    label_frame["identity_any"] = (identity_values >= 0.5).any(axis=1).astype(np.uint8)

    label_frame["identity_annotation_available"] = (
        label_frame["identity_annotator_count"] > 0
    ).astype(np.uint8)

    return label_frame


def safe_roc_auc(y_true, predictions, subset_name):
    y_true = np.asarray(y_true, dtype=np.uint8)
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(y_true) == 0 or np.unique(y_true).size != 2:
        raise ValueError(
            f"Official AUC cannot be calculated for validation subset "
            f"'{subset_name}': it contains {len(y_true)} rows and "
            f"{np.unique(y_true).size} classes."
        )

    return float(roc_auc_score(y_true, predictions))


def generalized_mean(values, power=-5):
    values = np.asarray(values, dtype=np.float64)

    if np.any(~np.isfinite(values)) or np.any(values <= 0.0):
        raise ValueError("Bias AUC values must be finite and strictly positive.")

    return float(np.mean(np.power(values, power)) ** (1.0 / power))


def calculate_official_jigsaw_metric(labels, predictions):
    predictions = np.asarray(predictions, dtype=np.float64)

    if len(labels) != len(predictions):
        raise ValueError("Validation labels and predictions have different lengths.")

    toxicity = labels["target_binary"].to_numpy(dtype=np.uint8, copy=True)
    overall_auc = safe_roc_auc(toxicity, predictions, "overall")

    subgroup_aucs = {}
    bpsn_aucs = {}
    bnsp_aucs = {}

    for identity_column in OFFICIAL_IDENTITY_COLUMNS:
        subgroup = (
            pd.to_numeric(labels[identity_column], errors="coerce")
            .fillna(0.0)
            .to_numpy(dtype=np.float32)
            >= 0.5
        )

        subgroup_auc_mask = subgroup
        bpsn_auc_mask = (subgroup & (toxicity == 0)) | ((~subgroup) & (toxicity == 1))
        bnsp_auc_mask = (subgroup & (toxicity == 1)) | ((~subgroup) & (toxicity == 0))

        subgroup_aucs[identity_column] = safe_roc_auc(
            toxicity[subgroup_auc_mask],
            predictions[subgroup_auc_mask],
            f"{identity_column}_subgroup",
        )
        bpsn_aucs[identity_column] = safe_roc_auc(
            toxicity[bpsn_auc_mask],
            predictions[bpsn_auc_mask],
            f"{identity_column}_bpsn",
        )
        bnsp_aucs[identity_column] = safe_roc_auc(
            toxicity[bnsp_auc_mask],
            predictions[bnsp_auc_mask],
            f"{identity_column}_bnsp",
        )

    subgroup_generalized_mean = generalized_mean(
        list(subgroup_aucs.values()),
        power=-5,
    )
    bpsn_generalized_mean = generalized_mean(
        list(bpsn_aucs.values()),
        power=-5,
    )
    bnsp_generalized_mean = generalized_mean(
        list(bnsp_aucs.values()),
        power=-5,
    )

    final_score = float(
        0.25
        * (
            overall_auc
            + subgroup_generalized_mean
            + bpsn_generalized_mean
            + bnsp_generalized_mean
        )
    )

    metric_details = {
        "official_metric": final_score,
        "overall_auc": overall_auc,
        "subgroup_generalized_mean": subgroup_generalized_mean,
        "bpsn_generalized_mean": bpsn_generalized_mean,
        "bnsp_generalized_mean": bnsp_generalized_mean,
        "subgroup_auc_by_identity": subgroup_aucs,
        "bpsn_auc_by_identity": bpsn_aucs,
        "bnsp_auc_by_identity": bnsp_aucs,
    }

    return final_score, metric_details


train_header = pd.read_csv(TRAIN_PATH, nrows=0).columns.tolist()
available_train_columns = set(train_header)

required_train_columns = [
    "id",
    "comment_text",
    "created_date",
] + [column for column in CORE_LABEL_COLUMNS if column in available_train_columns]

raw_train = pd.read_csv(
    TRAIN_PATH,
    usecols=lambda column: column in set(required_train_columns),
    low_memory=False,
)

raw_test = pd.read_csv(
    TEST_PATH,
    usecols=["id", "comment_text"],
    low_memory=False,
)

for column in IDENTITY_COLUMNS + TOXICITY_AUX_COLUMNS:
    if column not in raw_train.columns:
        raw_train[column] = np.nan

for column in ["toxicity_annotator_count", "identity_annotator_count"]:
    if column not in raw_train.columns:
        raw_train[column] = 0

raw_train["comment_text"] = raw_train["comment_text"].fillna("").astype(str)
raw_test["comment_text"] = raw_test["comment_text"].fillna("").astype(str)

canonical_for_grouping = (
    raw_train["comment_text"]
    .str.normalize("NFKC")
    .str.replace(r"[\u200b-\u200d\ufeff]", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    .str.casefold()
)

group_codes, _ = pd.factorize(canonical_for_grouping, sort=False)
del canonical_for_grouping
gc.collect()

timestamps = pd.to_datetime(
    raw_train["created_date"],
    errors="coerce",
    utc=True,
)

timestamp_ns = timestamps.astype("int64").to_numpy(copy=True)
nat_value = np.iinfo(np.int64).min
observed_timestamp_ns = timestamp_ns[timestamp_ns != nat_value]
group_latest_timestamp = None

if len(observed_timestamp_ns) > 0:
    temporal_cutoff = int(np.quantile(observed_timestamp_ns, 0.90))
    group_latest_timestamp = np.full(
        int(group_codes.max()) + 1,
        nat_value,
        dtype=np.int64,
    )
    np.maximum.at(group_latest_timestamp, group_codes, timestamp_ns)
    validation_mask = group_latest_timestamp[group_codes] >= temporal_cutoff
else:
    stable_group_hash = pd.util.hash_pandas_object(
        pd.Series(group_codes),
        index=False,
    ).to_numpy(dtype=np.uint64)
    validation_mask = (stable_group_hash % np.uint64(10)) == 0
    temporal_cutoff = None

validation_fraction = float(validation_mask.mean())

if validation_fraction < 0.05 or validation_fraction > 0.30:
    stable_group_hash = pd.util.hash_pandas_object(
        pd.Series(group_codes),
        index=False,
    ).to_numpy(dtype=np.uint64)
    validation_mask = (stable_group_hash % np.uint64(10)) == 0
    validation_fraction = float(validation_mask.mean())
    temporal_cutoff = None

train_mask = ~validation_mask

assert train_mask.any()
assert validation_mask.any()
assert not np.intersect1d(
    np.unique(group_codes[train_mask]),
    np.unique(group_codes[validation_mask]),
).size

train_source = raw_train.loc[train_mask].reset_index(drop=True)
valid_source = raw_train.loc[validation_mask].reset_index(drop=True)

train_features, text_feature_columns = build_text_inputs(train_source)
valid_features, valid_feature_columns = build_text_inputs(valid_source)
test_features, test_feature_columns = build_text_inputs(raw_test)

assert text_feature_columns == valid_feature_columns == test_feature_columns

text_feature_scaler = StandardScaler(copy=True)

train_features.loc[:, text_feature_columns] = text_feature_scaler.fit_transform(
    train_features[text_feature_columns]
).astype(np.float32)

valid_features.loc[:, text_feature_columns] = text_feature_scaler.transform(
    valid_features[text_feature_columns]
).astype(np.float32)

test_features.loc[:, text_feature_columns] = text_feature_scaler.transform(
    test_features[text_feature_columns]
).astype(np.float32)

train_labels = build_labels(train_source)
valid_labels = build_labels(valid_source)

assert len(train_features) == len(train_labels)
assert len(valid_features) == len(valid_labels)
assert len(test_features) == len(raw_test)
assert train_features["id"].equals(train_labels["id"])
assert valid_features["id"].equals(valid_labels["id"])
assert test_features["id"].equals(raw_test["id"])

artifact_compression = {"method": "gzip", "compresslevel": 1}

train_features.to_pickle(
    os.path.join(WORKING_DIR, "train_features.pkl.gz"),
    compression=artifact_compression,
)
valid_features.to_pickle(
    os.path.join(WORKING_DIR, "valid_features.pkl.gz"),
    compression=artifact_compression,
)
test_features.to_pickle(
    os.path.join(WORKING_DIR, "test_features.pkl.gz"),
    compression=artifact_compression,
)
train_labels.to_pickle(
    os.path.join(WORKING_DIR, "train_labels.pkl.gz"),
    compression=artifact_compression,
)
valid_labels.to_pickle(
    os.path.join(WORKING_DIR, "valid_labels.pkl.gz"),
    compression=artifact_compression,
)

joblib.dump(
    {
        "scaler": text_feature_scaler,
        "feature_columns": text_feature_columns,
    },
    os.path.join(WORKING_DIR, "text_feature_preprocessor.joblib"),
)

data_config = {
    "split_strategy": "forward_time_with_normalized_text_group_isolation",
    "temporal_cutoff_ns": temporal_cutoff,
    "validation_fraction": validation_fraction,
    "text_column": "model_text",
    "text_feature_columns": text_feature_columns,
    "identity_columns": IDENTITY_COLUMNS,
    "toxicity_auxiliary_columns": TOXICITY_AUX_COLUMNS,
    "target_column": "target",
    "binary_target_column": "target_binary",
}

with open(
    os.path.join(WORKING_DIR, "data_processing_config.json"),
    "w",
    encoding="utf-8",
) as config_file:
    json.dump(data_config, config_file, indent=2)

del raw_train, raw_test, train_source, valid_source
del timestamps, timestamp_ns, group_latest_timestamp, group_codes
gc.collect()


MODEL_ID = "microsoft/deberta-v3-large"
NUM_STYLE_FEATURES = len(data_config["text_feature_columns"])
NUM_AUXILIARY_TASKS = len(data_config["toxicity_auxiliary_columns"])
NUM_IDENTITY_TASKS = len(data_config["identity_columns"])

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
pretrained_sequence_classifier = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/deberta-v3-large",
    num_labels=2,
)


class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs, scale):
        ctx.scale = float(scale)
        return inputs.view_as(inputs)

    @staticmethod
    def backward(ctx, gradient_output):
        return -ctx.scale * gradient_output, None


def gradient_reverse(inputs, scale):
    return GradientReversalFunction.apply(inputs, scale)


class DebiasedDebertaToxicityModel(nn.Module):
    def __init__(
        self,
        pretrained_model,
        num_style_features,
        num_auxiliary_tasks,
        num_identity_tasks,
        dropout_probability=0.15,
        adversarial_scale=0.08,
    ):
        super().__init__()

        self.encoder = pretrained_model.deberta
        self.hidden_size = int(pretrained_model.config.hidden_size)
        self.adversarial_scale = float(adversarial_scale)

        style_hidden_size = 96
        fusion_hidden_size = self.hidden_size

        self.style_network = nn.Sequential(
            nn.LayerNorm(num_style_features),
            nn.Linear(num_style_features, style_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(style_hidden_size, style_hidden_size),
            nn.GELU(),
        )

        self.fusion_network = nn.Sequential(
            nn.Linear(self.hidden_size + style_hidden_size, fusion_hidden_size),
            nn.LayerNorm(fusion_hidden_size),
            nn.GELU(),
            nn.Dropout(dropout_probability),
        )

        self.toxicity_head = nn.Linear(fusion_hidden_size, 1)
        self.subtype_head = nn.Linear(fusion_hidden_size, num_auxiliary_tasks)

        self.identity_adversary = nn.Sequential(
            nn.Linear(fusion_hidden_size, fusion_hidden_size // 2),
            nn.GELU(),
            nn.Dropout(dropout_probability),
            nn.Linear(fusion_hidden_size // 2, num_identity_tasks),
        )

        self._initialize_new_layers()

    def _initialize_new_layers(self):
        def initialize(module):
            if isinstance(module, nn.Linear):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

        self.style_network.apply(initialize)
        self.fusion_network.apply(initialize)
        self.toxicity_head.apply(initialize)
        self.subtype_head.apply(initialize)
        self.identity_adversary.apply(initialize)

    def set_adversarial_scale(self, scale):
        self.adversarial_scale = float(scale)

    @staticmethod
    def masked_mean_pool(sequence_output, attention_mask):
        mask = attention_mask.unsqueeze(-1).to(sequence_output.dtype)
        summed_embeddings = (sequence_output * mask).sum(dim=1)
        token_count = mask.sum(dim=1).clamp_min(1.0)
        return summed_embeddings / token_count

    def forward(
        self,
        input_ids,
        attention_mask,
        style_features,
        token_type_ids=None,
    ):
        encoder_inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "return_dict": True,
        }

        if token_type_ids is not None:
            encoder_inputs["token_type_ids"] = token_type_ids

        encoder_outputs = self.encoder(**encoder_inputs)
        pooled_text = self.masked_mean_pool(
            encoder_outputs.last_hidden_state,
            attention_mask,
        )

        style_representation = self.style_network(style_features)
        fused_representation = self.fusion_network(
            torch.cat([pooled_text, style_representation], dim=-1)
        )

        toxicity_logit = self.toxicity_head(fused_representation).squeeze(-1)
        subtype_logits = self.subtype_head(fused_representation)

        reversed_representation = gradient_reverse(
            fused_representation,
            self.adversarial_scale,
        )
        identity_logits = self.identity_adversary(reversed_representation)

        return {
            "toxicity_logit": toxicity_logit,
            "subtype_logits": subtype_logits,
            "identity_logits": identity_logits,
        }


class FairToxicityMultitaskLoss(nn.Module):
    def __init__(
        self,
        subtype_weight=0.22,
        identity_adversary_weight=0.06,
        benign_identity_weight=2.75,
        toxic_identity_weight=1.35,
    ):
        super().__init__()
        self.subtype_weight = float(subtype_weight)
        self.identity_adversary_weight = float(identity_adversary_weight)
        self.benign_identity_weight = float(benign_identity_weight)
        self.toxic_identity_weight = float(toxic_identity_weight)

    @staticmethod
    def _masked_bce_with_logits(logits, targets, valid_mask):
        targets = torch.nan_to_num(targets.float(), nan=0.0).clamp(0.0, 1.0)
        elementwise_loss = F.binary_cross_entropy_with_logits(
            logits,
            targets,
            reduction="none",
        )
        valid_mask = valid_mask.to(elementwise_loss.dtype)

        return (elementwise_loss * valid_mask).sum() / valid_mask.sum().clamp_min(1.0)

    def forward(
        self,
        model_outputs,
        target,
        subtype_targets,
        identity_targets,
        identity_any,
        identity_annotation_available,
    ):
        target = target.float()
        target_valid = torch.isfinite(target)
        clean_target = torch.nan_to_num(target, nan=0.0).clamp(0.0, 1.0)

        identity_annotated = identity_annotation_available.bool()
        identity_mentioned = identity_annotated & identity_any.bool()
        toxic_target = clean_target >= 0.5

        sample_weights = torch.ones_like(clean_target)
        sample_weights = torch.where(
            identity_mentioned & ~toxic_target,
            torch.full_like(sample_weights, self.benign_identity_weight),
            sample_weights,
        )
        sample_weights = torch.where(
            identity_mentioned & toxic_target,
            torch.full_like(sample_weights, self.toxic_identity_weight),
            sample_weights,
        )

        target_losses = F.binary_cross_entropy_with_logits(
            model_outputs["toxicity_logit"],
            clean_target,
            reduction="none",
        )
        target_mask = target_valid.to(target_losses.dtype)

        weighted_target_loss = (target_losses * sample_weights * target_mask).sum() / (
            sample_weights * target_mask
        ).sum().clamp_min(1.0)

        subtype_valid = torch.isfinite(subtype_targets)
        subtype_loss = self._masked_bce_with_logits(
            model_outputs["subtype_logits"],
            subtype_targets,
            subtype_valid,
        )

        identity_valid = torch.isfinite(identity_targets) & (
            identity_annotation_available.bool().unsqueeze(1)
        )
        identity_loss = self._masked_bce_with_logits(
            model_outputs["identity_logits"],
            identity_targets,
            identity_valid,
        )

        total_loss = (
            weighted_target_loss
            + self.subtype_weight * subtype_loss
            + self.identity_adversary_weight * identity_loss
        )

        return {
            "loss": total_loss,
            "target_loss": weighted_target_loss.detach(),
            "subtype_loss": subtype_loss.detach(),
            "identity_adversary_loss": identity_loss.detach(),
        }


def build_layerwise_optimizer(
    neural_model,
    backbone_learning_rate=1.25e-5,
    head_learning_rate=1.2e-4,
    layer_decay=0.90,
    weight_decay=0.01,
):
    num_layers = len(neural_model.encoder.encoder.layer)
    grouped_parameters = defaultdict(list)

    for parameter_name, parameter in neural_model.named_parameters():
        if not parameter.requires_grad:
            continue

        no_decay = (
            parameter_name.endswith(".bias")
            or "LayerNorm.weight" in parameter_name
            or "layer_norm.weight" in parameter_name
            or ".norm.weight" in parameter_name
        )

        parameter_weight_decay = 0.0 if no_decay else weight_decay

        if parameter_name.startswith("encoder.encoder.layer."):
            layer_index = int(parameter_name.split(".")[3])
            learning_rate = backbone_learning_rate * (
                layer_decay ** (num_layers - 1 - layer_index)
            )
        elif parameter_name.startswith("encoder.embeddings."):
            learning_rate = backbone_learning_rate * (layer_decay**num_layers)
        elif parameter_name.startswith("encoder."):
            learning_rate = backbone_learning_rate
        else:
            learning_rate = head_learning_rate

        grouped_parameters[(learning_rate, parameter_weight_decay)].append(parameter)

    parameter_groups = [
        {
            "params": parameters,
            "lr": learning_rate,
            "weight_decay": group_weight_decay,
        }
        for (
            learning_rate,
            group_weight_decay,
        ), parameters in grouped_parameters.items()
    ]

    return AdamW(
        parameter_groups,
        betas=(0.9, 0.98),
        eps=1e-6,
    )


model = DebiasedDebertaToxicityModel(
    pretrained_model=pretrained_sequence_classifier,
    num_style_features=NUM_STYLE_FEATURES,
    num_auxiliary_tasks=NUM_AUXILIARY_TASKS,
    num_identity_tasks=NUM_IDENTITY_TASKS,
    dropout_probability=0.15,
    adversarial_scale=0.08,
)

del pretrained_sequence_classifier
gc.collect()

criterion = FairToxicityMultitaskLoss(
    subtype_weight=0.22,
    identity_adversary_weight=0.06,
    benign_identity_weight=2.75,
    toxic_identity_weight=1.35,
)

optimizer = build_layerwise_optimizer(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda = device.type == "cuda"

if use_cuda:
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)

    if gpu_memory_gb >= 48:
        batch_size = 16
    elif gpu_memory_gb >= 24:
        batch_size = 10
    else:
        batch_size = 8
else:
    batch_size = 2

gradient_accumulation_steps = max(1, int(math.ceil(32 / batch_size)))
max_length = 256
num_workers = max(2, min(4, os.cpu_count() or 2))
max_epochs = int(os.environ.get("NUM_EPOCHS", "1"))
early_stopping_patience = int(os.environ.get("EARLY_STOPPING_PATIENCE", "1"))
warmup_fraction = 0.06

style_feature_columns = list(data_config["text_feature_columns"])
identity_columns = list(data_config["identity_columns"])
toxicity_auxiliary_columns = list(data_config["toxicity_auxiliary_columns"])


class ToxicityDataset(Dataset):
    def __init__(self, features, labels=None):
        self.texts = features["model_text"].fillna("").astype(str).tolist()
        self.style_features = features[style_feature_columns].to_numpy(
            dtype=np.float32,
            copy=True,
        )
        self.has_labels = labels is not None

        if self.has_labels:
            self.targets = labels["target"].to_numpy(dtype=np.float32, copy=True)
            self.subtype_targets = labels[toxicity_auxiliary_columns].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_targets = labels[identity_columns].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_any = labels["identity_any"].to_numpy(
                dtype=np.float32,
                copy=True,
            )
            self.identity_annotation_available = labels[
                "identity_annotation_available"
            ].to_numpy(dtype=np.float32, copy=True)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        item = {
            "text": self.texts[index],
            "style_features": self.style_features[index],
        }

        if self.has_labels:
            item.update(
                {
                    "target": self.targets[index],
                    "subtype_targets": self.subtype_targets[index],
                    "identity_targets": self.identity_targets[index],
                    "identity_any": self.identity_any[index],
                    "identity_annotation_available": self.identity_annotation_available[
                        index
                    ],
                }
            )

        return item


class DynamicPaddingCollator:
    def __init__(self, tokenizer_instance, max_sequence_length):
        self.tokenizer = tokenizer_instance
        self.max_sequence_length = int(max_sequence_length)

    def __call__(self, samples):
        texts = [sample["text"] for sample in samples]

        encoded = self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=self.max_sequence_length,
            return_tensors="pt",
        )

        batch = {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "style_features": torch.from_numpy(
                np.stack([sample["style_features"] for sample in samples]).astype(
                    np.float32,
                    copy=False,
                )
            ),
        }

        if "token_type_ids" in encoded:
            batch["token_type_ids"] = encoded["token_type_ids"]

        if "target" in samples[0]:
            batch["target"] = torch.tensor(
                [sample["target"] for sample in samples],
                dtype=torch.float32,
            )
            batch["subtype_targets"] = torch.from_numpy(
                np.stack([sample["subtype_targets"] for sample in samples]).astype(
                    np.float32,
                    copy=False,
                )
            )
            batch["identity_targets"] = torch.from_numpy(
                np.stack([sample["identity_targets"] for sample in samples]).astype(
                    np.float32,
                    copy=False,
                )
            )
            batch["identity_any"] = torch.tensor(
                [sample["identity_any"] for sample in samples],
                dtype=torch.float32,
            )
            batch["identity_annotation_available"] = torch.tensor(
                [sample["identity_annotation_available"] for sample in samples],
                dtype=torch.float32,
            )

        return batch


collator = DynamicPaddingCollator(tokenizer, max_length)


def move_batch_to_device(batch):
    return {
        name: tensor.to(device, non_blocking=use_cuda) for name, tensor in batch.items()
    }


def predict_with_model(feature_frame, inference_batch_size=batch_size):
    inference_dataset = ToxicityDataset(feature_frame, labels=None)

    inference_loader = DataLoader(
        inference_dataset,
        batch_size=inference_batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=use_cuda,
        persistent_workers=False,
        prefetch_factor=2,
        collate_fn=collator,
    )

    model.eval()
    prediction_chunks = []

    with torch.inference_mode():
        for batch in inference_loader:
            batch = move_batch_to_device(batch)

            with torch.cuda.amp.autocast(enabled=use_cuda):
                outputs = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    style_features=batch["style_features"],
                    token_type_ids=batch.get("token_type_ids"),
                )
                probabilities = torch.sigmoid(outputs["toxicity_logit"])

            prediction_chunks.append(
                probabilities.float().cpu().numpy().astype(np.float64, copy=False)
            )

    del inference_loader, inference_dataset
    gc.collect()

    return np.concatenate(prediction_chunks, axis=0)


train_dataset = ToxicityDataset(train_features, train_labels)

updates_per_epoch = int(
    math.ceil(len(train_dataset) / (batch_size * gradient_accumulation_steps))
)
total_training_updates = max(1, updates_per_epoch * max_epochs)
warmup_updates = max(1, int(total_training_updates * warmup_fraction))


def learning_rate_multiplier(update_index):
    if update_index < warmup_updates:
        return float(update_index + 1) / float(warmup_updates)

    progress = float(update_index - warmup_updates) / float(
        max(1, total_training_updates - warmup_updates)
    )
    progress = min(max(progress, 0.0), 1.0)

    return max(0.05, 0.5 * (1.0 + math.cos(math.pi * progress)))


scheduler = LambdaLR(optimizer, lr_lambda=learning_rate_multiplier)

model.to(device)
scaler = torch.cuda.amp.GradScaler(enabled=use_cuda)
base_adversarial_scale = float(model.adversarial_scale)

best_score = -np.inf
best_metric_details = None
best_epoch = -1
epochs_without_improvement = 0
global_update = 0
training_history = []

for epoch in range(max_epochs):
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=use_cuda,
        persistent_workers=True,
        prefetch_factor=2,
        collate_fn=collator,
        drop_last=False,
    )

    model.train()
    optimizer.zero_grad(set_to_none=True)

    accumulated_batches = 0
    total_loss_sum = 0.0
    total_examples = 0

    for batch_index, batch in enumerate(train_loader):
        batch = move_batch_to_device(batch)
        current_batch_size = int(batch["target"].shape[0])

        adversarial_progress = min(
            1.0,
            float(global_update) / float(max(1, int(total_training_updates * 0.15))),
        )
        model.set_adversarial_scale(base_adversarial_scale * adversarial_progress)

        with torch.cuda.amp.autocast(enabled=use_cuda):
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                style_features=batch["style_features"],
                token_type_ids=batch.get("token_type_ids"),
            )

            loss_outputs = criterion(
                model_outputs=outputs,
                target=batch["target"],
                subtype_targets=batch["subtype_targets"],
                identity_targets=batch["identity_targets"],
                identity_any=batch["identity_any"],
                identity_annotation_available=batch["identity_annotation_available"],
            )

            unscaled_loss = loss_outputs["loss"]
            loss = unscaled_loss / gradient_accumulation_steps

        scaler.scale(loss).backward()

        accumulated_batches += 1
        total_loss_sum += (
            float(unscaled_loss.detach().float().cpu()) * current_batch_size
        )
        total_examples += current_batch_size

        is_update_step = (
            accumulated_batches == gradient_accumulation_steps
            or batch_index == len(train_loader) - 1
        )

        if is_update_step:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()

            accumulated_batches = 0
            global_update += 1

    del train_loader
    gc.collect()

    if use_cuda:
        torch.cuda.empty_cache()

    validation_predictions = predict_with_model(valid_features)
    epoch_score, epoch_metric_details = calculate_official_jigsaw_metric(
        valid_labels,
        validation_predictions,
    )

    epoch_train_loss = total_loss_sum / max(1, total_examples)

    training_history.append(
        {
            "epoch": epoch + 1,
            "train_loss": float(epoch_train_loss),
            **epoch_metric_details,
        }
    )

    if epoch_score > best_score:
        best_score = epoch_score
        best_metric_details = epoch_metric_details
        best_epoch = epoch + 1
        epochs_without_improvement = 0

        torch.save(
            {
                "epoch": best_epoch,
                "official_validation_score": float(best_score),
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "metric_details": best_metric_details,
                "max_length": max_length,
                "style_feature_columns": style_feature_columns,
            },
            BEST_MODEL_PATH,
        )
    else:
        epochs_without_improvement += 1

    print(
        f"Epoch {epoch + 1}/{max_epochs} "
        f"train_loss={epoch_train_loss:.6f} "
        f"official_score={epoch_score:.6f} "
        f"overall_auc={epoch_metric_details['overall_auc']:.6f} "
        f"bpsn_gm={epoch_metric_details['bpsn_generalized_mean']:.6f}"
    )

    if epochs_without_improvement >= early_stopping_patience:
        break

del train_dataset
gc.collect()

try:
    best_checkpoint = torch.load(
        BEST_MODEL_PATH,
        map_location=device,
        weights_only=True,
    )
except Exception:
    best_checkpoint = torch.load(BEST_MODEL_PATH, map_location=device)

model.load_state_dict(best_checkpoint["model_state_dict"])
model.to(device)
model.eval()

final_validation_predictions = predict_with_model(valid_features)
score, final_metric_details = calculate_official_jigsaw_metric(
    valid_labels,
    final_validation_predictions,
)

test_predictions = predict_with_model(test_features)
test_predictions = np.clip(test_predictions, 1e-7, 1.0 - 1e-7)

submission = pd.DataFrame(
    {
        "id": test_features["id"].to_numpy(),
        "prediction": test_predictions.astype(np.float64),
    }
)

if len(submission) != len(test_features):
    raise RuntimeError("Submission row count does not match the complete test set.")

if not submission["id"].equals(test_features["id"]):
    raise RuntimeError("Submission IDs are not in the required test-file row order.")

submission.to_csv(
    os.path.join(SUBMISSION_DIR, "submission_11c7f08185ff46ed815a59f22fbb3db1.csv"),
    index=False,
)

with open(METRICS_PATH, "w", encoding="utf-8") as metrics_file:
    json.dump(
        {
            "split_strategy": data_config.get("split_strategy"),
            "best_epoch_during_training": int(best_epoch),
            "best_training_validation_score": float(best_score),
            "reloaded_best_checkpoint_validation_score": float(score),
            "best_training_metric_details": best_metric_details,
            "final_reloaded_metric_details": final_metric_details,
            "history": training_history,
            "official_metric_formula": (
                "0.25*(overall_auc + generalized_mean_p_minus_5(subgroup_auc) + "
                "generalized_mean_p_minus_5(bpsn_auc) + "
                "generalized_mean_p_minus_5(bnsp_auc))"
            ),
        },
        metrics_file,
        indent=2,
    )

print(f"Final Validation Score: {score}")
