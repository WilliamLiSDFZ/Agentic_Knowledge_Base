import os
import re
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F

from sklearn.preprocessing import StandardScaler
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers.modeling_outputs import SequenceClassifierOutput

from engine.candidate_runtime import CandidateSession


# ---------------------------------------------------------------------
# Runtime initialization and split before any fitted preprocessing.
# ---------------------------------------------------------------------
session = CandidateSession.from_env()

INPUT_DIR = "./input"

raw_train_df = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"),
    low_memory=False,
)
raw_test_df = pd.read_csv(
    os.path.join(INPUT_DIR, "test.csv"),
    low_memory=False,
)

train_df, valid_df, test_df = session.split(raw_train_df, raw_test_df)
del raw_train_df, raw_test_df


# ---------------------------------------------------------------------
# Data processing.
# ---------------------------------------------------------------------
ALL_IDENTITY_COLUMNS = [
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

TOXICITY_SUBTYPE_COLUMNS = [
    "severe_toxicity",
    "obscene",
    "identity_attack",
    "insult",
    "threat",
    "sexual_explicit",
]

IDENTITY_PATTERN = re.compile(
    r"\b(?:"
    r"men?|males?|women?|females?|boys?|girls?|transgender|transsexual|non[- ]?binary|"
    r"gay|gays|lesbian|lesbians|homosexual|homosexuals|bisexual|bisexuals|queer|lgbtq?\+?|"
    r"christians?|jews?|jewish|muslims?|islamic|hindu(?:s|ism)?|buddhist(?:s)?|atheist(?:s)?|"
    r"blacks?|whites?|asians?|latinos?|latinas?|hispanics?|"
    r"disabled|disability|autistic|autism|mental(?:ly)? ill|schizophrenic|bipolar"
    r")\b",
    flags=re.IGNORECASE,
)

URL_PATTERN = re.compile(r"(?:https?://\S+|www\.\S+)", flags=re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"\b[\w.\-+]+@[\w.\-]+\.[A-Za-z]{2,}\b")
REPEATED_CHAR_PATTERN = re.compile(r"(.)\1{4,}", flags=re.DOTALL)


def clean_comment_text(text_series):
    text = text_series.fillna("").astype(str).str.normalize("NFKC")
    text = text.str.replace(r"<\s*br\s*/?\s*>", " ", regex=True, case=False)
    text = text.str.replace(r"<[^>]+>", " ", regex=True)
    text = text.str.replace("&amp;", "&", regex=False)
    text = text.str.replace("&lt;", "<", regex=False)
    text = text.str.replace("&gt;", ">", regex=False)
    text = text.str.replace("&quot;", '"', regex=False)
    text = text.str.replace("&#39;", "'", regex=False)
    text = text.str.replace(URL_PATTERN, " [URL] ", regex=True)
    text = text.str.replace(EMAIL_PATTERN, " [EMAIL] ", regex=True)
    text = text.str.replace(r"[\r\n\t\f\v]+", " ", regex=True)
    text = text.str.replace(REPEATED_CHAR_PATTERN, r"\1\1\1", regex=True)
    return text.str.replace(r"\s+", " ", regex=True).str.strip()


def neutralize_identity_mentions(text_series):
    return (
        text_series.str.replace(IDENTITY_PATTERN, " [IDENTITY] ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )


def build_text_feature_frame(clean_text):
    char_count = clean_text.str.len().fillna(0).astype(np.float32)
    word_count = clean_text.str.count(r"\b[\w']+\b").astype(np.float32)
    letter_count = clean_text.str.count(r"[A-Za-z]").astype(np.float32)
    uppercase_count = clean_text.str.count(r"[A-Z]").astype(np.float32)
    digit_count = clean_text.str.count(r"\d").astype(np.float32)
    punctuation_count = clean_text.str.count(r"[!?.,;:]").astype(np.float32)
    exclamation_count = clean_text.str.count("!").astype(np.float32)
    question_count = clean_text.str.count(r"\?").astype(np.float32)
    url_count = clean_text.str.count(r"\[URL\]").astype(np.float32)
    email_count = clean_text.str.count(r"\[EMAIL\]").astype(np.float32)
    identity_term_count = clean_text.str.count(IDENTITY_PATTERN).astype(np.float32)
    all_caps_token_count = clean_text.str.count(r"\b[A-Z]{2,}\b").astype(np.float32)

    safe_word_count = np.maximum(word_count.to_numpy(), 1.0)
    safe_letter_count = np.maximum(letter_count.to_numpy(), 1.0)
    safe_char_count = np.maximum(char_count.to_numpy(), 1.0)

    return pd.DataFrame(
        {
            "log_char_count": np.log1p(char_count.to_numpy()),
            "log_word_count": np.log1p(word_count.to_numpy()),
            "log_exclamation_count": np.log1p(exclamation_count.to_numpy()),
            "log_question_count": np.log1p(question_count.to_numpy()),
            "log_url_count": np.log1p(url_count.to_numpy()),
            "log_email_count": np.log1p(email_count.to_numpy()),
            "log_identity_term_count": np.log1p(identity_term_count.to_numpy()),
            "log_all_caps_token_count": np.log1p(all_caps_token_count.to_numpy()),
            "uppercase_letter_ratio": uppercase_count.to_numpy() / safe_letter_count,
            "digit_ratio": digit_count.to_numpy() / safe_char_count,
            "punctuation_ratio": punctuation_count.to_numpy() / safe_char_count,
            "mean_token_length": char_count.to_numpy() / safe_word_count,
            "contains_identity_term": (identity_term_count.to_numpy() > 0).astype(
                np.float32
            ),
        },
        index=clean_text.index,
        dtype=np.float32,
    )


def compact_partition(frame, is_train):
    available_identities = [c for c in ALL_IDENTITY_COLUMNS if c in frame.columns]
    available_subtypes = [c for c in TOXICITY_SUBTYPE_COLUMNS if c in frame.columns]

    base_columns = ["id", "comment_text"]
    if is_train and "target" in frame.columns:
        base_columns.append("target")

    metadata_columns = [
        c
        for c in ["toxicity_annotator_count", "identity_annotator_count"]
        if c in frame.columns
    ]

    keep_columns = list(
        dict.fromkeys(
            base_columns + available_subtypes + available_identities + metadata_columns
        )
    )
    compact = frame.loc[:, keep_columns].copy()

    cleaned_text = clean_comment_text(compact.pop("comment_text"))
    compact["model_text"] = cleaned_text

    for column in available_identities + available_subtypes + metadata_columns:
        compact[column] = (
            pd.to_numeric(compact[column], errors="coerce")
            .fillna(0.0)
            .astype(np.float32)
        )

    if is_train and "target" in compact.columns:
        compact["target"] = (
            pd.to_numeric(compact["target"], errors="coerce")
            .fillna(0.0)
            .astype(np.float32)
        )
        compact["target_binary"] = (compact["target"] >= 0.5).astype(np.int8)

    return compact, build_text_feature_frame(cleaned_text)


train_df, train_text_feature_frame = compact_partition(train_df, is_train=True)
valid_df, valid_text_feature_frame = compact_partition(valid_df, is_train=True)
test_df, test_text_feature_frame = compact_partition(test_df, is_train=False)

text_feature_columns = train_text_feature_frame.columns.tolist()
text_feature_scaler = StandardScaler()

train_text_features = text_feature_scaler.fit_transform(
    train_text_feature_frame[text_feature_columns]
).astype(np.float32)

valid_text_features = text_feature_scaler.transform(
    valid_text_feature_frame[text_feature_columns]
).astype(np.float32)

test_text_features = text_feature_scaler.transform(
    test_text_feature_frame[text_feature_columns]
).astype(np.float32)

for frame, feature_matrix in (
    (train_df, train_text_features),
    (valid_df, valid_text_features),
    (test_df, test_text_features),
):
    for feature_index, feature_name in enumerate(text_feature_columns):
        frame[f"tf_{feature_name}"] = feature_matrix[:, feature_index]

available_official_identity_columns = [
    column for column in OFFICIAL_IDENTITY_COLUMNS if column in train_df.columns
]

processing_state = {
    "text_feature_columns": text_feature_columns,
    "text_feature_scaler": text_feature_scaler,
    "official_identity_columns": available_official_identity_columns,
    "identity_pattern": IDENTITY_PATTERN,
}


# ---------------------------------------------------------------------
# Model and counterfactual bias-aware loss.
# ---------------------------------------------------------------------
# The timeout is caused by exporting all test predictions through a 24-layer
# DeBERTa-large model before a complete runtime snapshot can be published.
# DeBERTa-v3-base preserves the same text-classification approach while making
# checkpoint validation and complete test inference practical within the budget.
MODEL_NAME = "microsoft/deberta-v3-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
base_model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2,
)


class FrozenDebertaRepresentationClassifier(torch.nn.Module):
    def __init__(self, sequence_classifier):
        super().__init__()
        self.config = sequence_classifier.config
        self.deberta = sequence_classifier.deberta
        self.pooler = sequence_classifier.pooler
        self.dropout = sequence_classifier.dropout
        self.classifier = sequence_classifier.classifier

        for parameter in self.deberta.parameters():
            parameter.requires_grad = False

        hidden_size = self.config.hidden_size
        self.representation_scale = torch.nn.Parameter(torch.ones(hidden_size))
        self.representation_bias = torch.nn.Parameter(torch.zeros(hidden_size))

    def forward(self, **kwargs):
        kwargs.pop("return_dict", None)

        # The frozen encoder remains in its current train/eval mode, but its
        # activations are not retained because gradients only update the head.
        with torch.no_grad():
            encoder_outputs = self.deberta(**kwargs, return_dict=True)

        sequence_output = encoder_outputs.last_hidden_state
        sequence_output = (
            sequence_output * self.representation_scale + self.representation_bias
        )
        pooled_output = self.pooler(sequence_output)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        return SequenceClassifierOutput(logits=logits)


model = FrozenDebertaRepresentationClassifier(base_model)
del base_model


def toxicity_logit(model_output):
    logits = model_output.logits
    return logits[:, 1] - logits[:, 0]


def toxicity_probability(model_output):
    return torch.sigmoid(toxicity_logit(model_output))


class CounterfactualBiasLoss(torch.nn.Module):
    def __init__(self, counterfactual_weight=0.35, confidence_floor=0.05):
        super().__init__()
        self.counterfactual_weight = float(counterfactual_weight)
        self.confidence_floor = float(confidence_floor)

    def forward(
        self,
        original_toxicity_logits,
        target,
        identity_membership=None,
        neutralized_toxicity_logits=None,
    ):
        target = target.float().view_as(original_toxicity_logits)

        supervised_loss = F.binary_cross_entropy_with_logits(
            original_toxicity_logits,
            target,
            reduction="mean",
        )

        if (
            neutralized_toxicity_logits is None
            or identity_membership is None
            or self.counterfactual_weight <= 0.0
        ):
            return supervised_loss

        if identity_membership.ndim == 1:
            has_identity = identity_membership.bool()
        else:
            has_identity = identity_membership.bool().any(dim=1)

        benign_confidence = (1.0 - 2.0 * target).clamp(min=0.0, max=1.0)
        counterfactual_mask = (
            has_identity.float() * (benign_confidence >= self.confidence_floor).float()
        )

        original_probability = torch.sigmoid(original_toxicity_logits)
        neutralized_probability = torch.sigmoid(neutralized_toxicity_logits)
        consistency_error = (original_probability - neutralized_probability).pow(2)

        weighted_consistency = (
            consistency_error * benign_confidence * counterfactual_mask
        ).sum() / (counterfactual_mask.mul(benign_confidence).sum().clamp_min(1.0))

        return supervised_loss + self.counterfactual_weight * weighted_consistency


criterion = CounterfactualBiasLoss(
    counterfactual_weight=0.35,
    confidence_floor=0.05,
)

no_decay_terms = ("bias", "LayerNorm.weight", "layer_norm.weight")
head_parameter_prefixes = ("pooler.", "classifier.")
affine_parameter_names = {"representation_scale", "representation_bias"}

head_parameters = [
    (name, parameter)
    for name, parameter in model.named_parameters()
    if parameter.requires_grad
    and (
        name in affine_parameter_names
        or name.startswith(head_parameter_prefixes)
    )
]

if len(head_parameters) != sum(
    parameter.requires_grad for parameter in model.parameters()
):
    raise RuntimeError("Only representation-affine and classification-head parameters are trainable.")

decay_parameters = [
    parameter
    for name, parameter in head_parameters
    if name not in affine_parameter_names
    and not any(term in name for term in no_decay_terms)
]
no_decay_parameters = [
    parameter
    for name, parameter in head_parameters
    if name in affine_parameter_names
    or any(term in name for term in no_decay_terms)
]

optimizer_groups = []

if decay_parameters:
    optimizer_groups.append(
        {
            "params": decay_parameters,
            "lr": 3.0e-5,
            "weight_decay": 0.01,
        }
    )

if no_decay_parameters:
    optimizer_groups.append(
        {
            "params": no_decay_parameters,
            "lr": 3.0e-5,
            "weight_decay": 0.0,
        }
    )

optimizer = AdamW(
    optimizer_groups,
    betas=(0.9, 0.999),
    eps=1e-8,
)


# ---------------------------------------------------------------------
# Training and CandidateSession-compatible inference callbacks.
# ---------------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

MAX_LENGTH = 128
TRAIN_BATCH_SIZE = 16 if torch.cuda.is_available() else 2
INFERENCE_BATCH_SIZE = 64 if torch.cuda.is_available() else 8
GRADIENT_ACCUMULATION_STEPS = 2 if torch.cuda.is_available() else 1
MAX_EPOCHS = 3
PIN_MEMORY = torch.cuda.is_available()
NUM_WORKERS = max(2, min(4, os.cpu_count() or 2))

amp_enabled = torch.cuda.is_available()
grad_scaler = torch.cuda.amp.GradScaler(enabled=amp_enabled)


class ToxicityDataset(Dataset):
    def __init__(self, frame, include_labels):
        self.texts = frame["model_text"].fillna("").astype(str).to_numpy(copy=False)
        self.include_labels = include_labels

        if include_labels:
            self.targets = frame["target"].to_numpy(dtype=np.float32, copy=False)
            self.identities = (
                frame[available_official_identity_columns].to_numpy(
                    dtype=np.float32, copy=False
                )
                >= 0.5
            ).astype(np.int8)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        if self.include_labels:
            return (
                self.texts[index],
                self.targets[index],
                self.identities[index],
            )
        return self.texts[index]


train_dataset = ToxicityDataset(train_df, include_labels=True)
valid_dataset = ToxicityDataset(valid_df, include_labels=False)
test_dataset = ToxicityDataset(test_df, include_labels=False)


def tokenize_texts(texts):
    return tokenizer(
        list(texts),
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        pad_to_multiple_of=8 if torch.cuda.is_available() else None,
        return_tensors="pt",
    )


def training_collate(batch):
    texts, targets, identities = zip(*batch)
    encoded = tokenize_texts(texts)

    target_tensor = torch.tensor(np.asarray(targets), dtype=torch.float32)
    identity_tensor = torch.tensor(np.asarray(identities), dtype=torch.int8)

    has_identity = identity_tensor.bool().any(dim=1)
    benign_identity_mask = has_identity & (target_tensor < 0.5)
    counterfactual_indices = torch.where(benign_identity_mask)[0]

    counterfactual_encoded = None
    if counterfactual_indices.numel() > 0:
        selected_texts = [texts[i] for i in counterfactual_indices.tolist()]
        neutralized_texts = neutralize_identity_mentions(
            pd.Series(selected_texts, dtype="object")
        ).tolist()
        counterfactual_encoded = tokenize_texts(neutralized_texts)

    return {
        "encoded": encoded,
        "target": target_tensor,
        "identity": identity_tensor,
        "counterfactual_indices": counterfactual_indices,
        "counterfactual_encoded": counterfactual_encoded,
    }


def inference_collate(batch):
    return tokenize_texts(batch)


train_loader = DataLoader(
    train_dataset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=PIN_MEMORY,
    persistent_workers=True,
    collate_fn=training_collate,
)


def to_device(encoded_batch):
    return {
        key: value.to(device, non_blocking=PIN_MEMORY)
        for key, value in encoded_batch.items()
    }


def predict_positions(dataset, positions):
    positions = np.asarray(positions, dtype=np.int64).reshape(-1)

    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    selected_dataset = torch.utils.data.Subset(dataset, positions.tolist())

    prediction_loader = DataLoader(
        selected_dataset,
        batch_size=INFERENCE_BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=True,
        collate_fn=inference_collate,
    )

    previous_mode = model.training
    model.eval()
    predictions = []

    try:
        with torch.inference_mode():
            for encoded in prediction_loader:
                encoded = to_device(encoded)
                output = model(**encoded)
                probabilities = toxicity_probability(output)
                predictions.append(probabilities.detach().float().cpu().numpy())
    finally:
        model.train(previous_mode)

    return np.concatenate(predictions).astype(np.float64, copy=False)


def predict_validation(positional_indices):
    return predict_positions(valid_dataset, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_dataset, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)

    torch.save(
        model.state_dict(),
        os.path.join(directory, "model_state.pt"),
    )
    model.config.save_pretrained(directory)
    tokenizer.save_pretrained(directory)

    torch.save(
        {
            "max_length": MAX_LENGTH,
            "official_identity_columns": available_official_identity_columns,
            "text_feature_columns": processing_state["text_feature_columns"],
            "text_feature_scaler": processing_state["text_feature_scaler"],
            "identity_pattern": processing_state["identity_pattern"].pattern,
        },
        os.path.join(directory, "inference_state.pt"),
    )


def load_checkpoint(directory):
    checkpoint_path = os.path.join(directory, "model_state.pt")
    state_dict = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(state_dict, strict=True)
    model.to(device)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

optimizer.zero_grad(set_to_none=True)
should_stop = False
global_updates = 0

for epoch in range(MAX_EPOCHS):
    model.train()
    epoch_loss_sum = 0.0
    epoch_batches = 0
    epoch_updates = 0

    for batch_index, batch in enumerate(train_loader):
        encoded = to_device(batch["encoded"])
        target = batch["target"].to(device, non_blocking=PIN_MEMORY)
        identity = batch["identity"].to(device, non_blocking=PIN_MEMORY)
        counterfactual_indices = batch["counterfactual_indices"].to(
            device,
            non_blocking=PIN_MEMORY,
        )

        with torch.cuda.amp.autocast(enabled=amp_enabled):
            original_output = model(**encoded)
            original_logits = toxicity_logit(original_output)

            supervised_loss = criterion(
                original_logits,
                target,
                identity_membership=identity,
                neutralized_toxicity_logits=None,
            )

            consistency_penalty = torch.zeros((), device=device)

            if counterfactual_indices.numel() > 0:
                counterfactual_encoded = to_device(batch["counterfactual_encoded"])
                counterfactual_output = model(**counterfactual_encoded)
                counterfactual_logits = toxicity_logit(counterfactual_output)

                selected_original_logits = original_logits[counterfactual_indices]
                selected_targets = target[counterfactual_indices]
                selected_identity = identity[counterfactual_indices]

                counterfactual_total = criterion(
                    selected_original_logits,
                    selected_targets,
                    identity_membership=selected_identity,
                    neutralized_toxicity_logits=counterfactual_logits,
                )

                counterfactual_supervised = criterion(
                    selected_original_logits,
                    selected_targets,
                    identity_membership=selected_identity,
                    neutralized_toxicity_logits=None,
                )

                consistency_penalty = counterfactual_total - counterfactual_supervised

            total_loss = supervised_loss + consistency_penalty

        if not torch.isfinite(total_loss).item():
            optimizer.zero_grad(set_to_none=True)
            continue

        grad_scaler.scale(total_loss / GRADIENT_ACCUMULATION_STEPS).backward()

        epoch_loss_sum += float(total_loss.detach().cpu())
        epoch_batches += 1

        is_accumulation_step = (batch_index + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (
            batch_index + 1
        ) == len(train_loader)

        if is_accumulation_step:
            grad_scaler.unscale_(optimizer)

            torch.nn.utils.clip_grad_norm_(
                [
                    parameter
                    for parameter in model.parameters()
                    if parameter.requires_grad
                ],
                max_norm=1.0,
            )

            grad_scaler.step(optimizer)
            grad_scaler.update()
            optimizer.zero_grad(set_to_none=True)

            global_updates += 1
            epoch_updates += 1
            should_stop = session.step()

            if should_stop:
                break

    mean_epoch_loss = epoch_loss_sum / max(epoch_batches, 1)
    print(
        f"epoch={epoch + 1} updates={epoch_updates} "
        f"total_updates={global_updates} loss={mean_epoch_loss:.6f}"
    )

    if should_stop:
        break

result = session.finish()
score = float(result["best_validation_score"])
print(f"Final Validation Score: {score}")
