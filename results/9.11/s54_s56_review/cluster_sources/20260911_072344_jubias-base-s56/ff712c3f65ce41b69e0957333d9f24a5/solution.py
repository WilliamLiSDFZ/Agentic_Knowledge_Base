import os
import re
import joblib
import numpy as np
import pandas as pd

from scipy.sparse import hstack
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier

from engine.candidate_runtime import CandidateSession


# The challenge is not only toxicity ranking, but avoiding elevated scores for
# benign identity mentions.  The training weights emphasize the three exact
# populations involved in subgroup, BPSN, and BNSP AUCs.  CandidateSession owns
# the official generalized bias-AUC validation and checkpoint selection.
session = CandidateSession.from_env()

INPUT_DIR = "./input"
WORK_DIR = "./working/hashed_subword_model"
os.makedirs(WORK_DIR, exist_ok=True)

OFFICIAL_BIAS_IDENTITIES = [
    "black",
    "christian",
    "female",
    "homosexual_gay_or_lesbian",
    "jewish",
    "male",
    "muslim",
    "psychiatric_or_mental_illness",
    "white",
]

available_columns = pd.read_csv(
    os.path.join(INPUT_DIR, "train.csv"), nrows=0
).columns.tolist()

train_columns = [
    column
    for column in ["id", "target", "comment_text"] + OFFICIAL_BIAS_IDENTITIES
    if column in available_columns
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

# The runtime-owned split occurs before any learned transformation.
train_df, valid_df, test_df = session.split(train_raw, test_raw)

for frame in (train_df, valid_df):
    frame["target"] = (
        pd.to_numeric(frame["target"], errors="coerce")
        .fillna(0.0)
        .clip(0.0, 1.0)
        .astype(np.float32)
    )
    for column in OFFICIAL_BIAS_IDENTITIES:
        if column not in frame.columns:
            frame[column] = np.float32(0.0)
        else:
            frame[column] = (
                pd.to_numeric(frame[column], errors="coerce")
                .fillna(0.0)
                .clip(0.0, 1.0)
                .astype(np.float32)
            )

URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()]+")
USER_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_]{1,32}")
HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>\n]{0,120}>")
REPEATED_PUNCT_RE = re.compile(r"([!?.,])\1{2,}")
WHITESPACE_RE = re.compile(r"\s+")


def normalize_comment_series(text_series):
    """Stateless preprocessing shared exactly by train, validation, and test."""
    normalized = text_series.fillna("").astype(str).str.normalize("NFKC")
    normalized = normalized.str.replace(HTML_TAG_RE, " ", regex=True)
    normalized = normalized.str.replace(URL_RE, " URLTOKEN ", regex=True)
    normalized = normalized.str.replace(USER_RE, " USERTOKEN ", regex=True)
    normalized = normalized.str.replace(REPEATED_PUNCT_RE, r"\1\1", regex=True)
    normalized = normalized.str.replace(WHITESPACE_RE, " ", regex=True).str.strip()
    return normalized.tolist()


word_vectorizer = HashingVectorizer(
    analyzer="word",
    ngram_range=(1, 2),
    n_features=2**19,
    alternate_sign=False,
    binary=True,
    norm="l2",
    lowercase=True,
    strip_accents="unicode",
    dtype=np.float32,
)

char_vectorizer = HashingVectorizer(
    analyzer="char_wb",
    ngram_range=(3, 5),
    n_features=2**20,
    alternate_sign=False,
    binary=True,
    norm="l2",
    lowercase=True,
    strip_accents="unicode",
    dtype=np.float32,
)


def make_model_matrix(texts):
    word_matrix = word_vectorizer.transform(texts)
    char_matrix = char_vectorizer.transform(texts)
    return hstack([word_matrix, char_matrix], format="csr", dtype=np.float32)


model = SGDClassifier(
    loss="log_loss",
    penalty="elasticnet",
    alpha=1.5e-6,
    l1_ratio=0.03,
    fit_intercept=True,
    learning_rate="optimal",
    average=10000,
    max_iter=1,
    tol=None,
    shuffle=False,
    random_state=2025,
)
optimizer = model


def compute_training_weights(frame):
    target_binary = (frame["target"].to_numpy(dtype=np.float32) >= 0.5).astype(np.int8)

    subgroup = (
        frame[OFFICIAL_BIAS_IDENTITIES].to_numpy(dtype=np.float32).max(axis=1) >= 0.5
    )

    # Explicitly prioritize the ranking populations that define the official
    # subgroup, BPSN, and BNSP bias metrics.
    weights = np.ones(len(frame), dtype=np.float32)
    weights += 3.0 * (subgroup & (target_binary == 0))
    weights += 2.0 * (subgroup & (target_binary == 1))
    weights += 1.0 * ((~subgroup) & (target_binary == 1))
    weights /= max(float(weights.mean()), 1e-6)

    return target_binary, weights


def predict_positions(frame, positional_indices):
    positions = np.asarray(positional_indices, dtype=np.int64)
    if positions.size == 0:
        return np.empty(0, dtype=np.float64)

    outputs = np.empty(positions.size, dtype=np.float64)
    inference_batch_size = 8192

    for start in range(0, positions.size, inference_batch_size):
        stop = min(start + inference_batch_size, positions.size)
        batch_positions = positions[start:stop]

        batch_texts = normalize_comment_series(
            frame.iloc[batch_positions]["comment_text"]
        )
        batch_features = make_model_matrix(batch_texts)

        # Every returned score comes from the fitted model forward pass.
        outputs[start:stop] = model.predict_proba(batch_features)[:, 1]

    return np.clip(outputs, 1e-6, 1.0 - 1e-6)


def predict_validation(positional_indices):
    return predict_positions(valid_df, positional_indices)


def predict_test(positional_indices):
    return predict_positions(test_df, positional_indices)


def save_checkpoint(directory):
    os.makedirs(directory, exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "identity_columns": OFFICIAL_BIAS_IDENTITIES,
            "normalization": {
                "unicode_normalization": "NFKC",
                "url_token": "URLTOKEN",
                "user_token": "USERTOKEN",
            },
            "vectorizer_config": {
                "word": {
                    "analyzer": "word",
                    "ngram_range": (1, 2),
                    "n_features": 2**19,
                    "alternate_sign": False,
                    "binary": True,
                    "norm": "l2",
                },
                "character": {
                    "analyzer": "char_wb",
                    "ngram_range": (3, 5),
                    "n_features": 2**20,
                    "alternate_sign": False,
                    "binary": True,
                    "norm": "l2",
                },
            },
        },
        os.path.join(directory, "hashed_subword_bundle.joblib"),
    )


def load_checkpoint(directory):
    restored_model = joblib.load(
        os.path.join(directory, "hashed_subword_bundle.joblib")
    )["model"]

    # Restore into the existing estimator object, preserving optimizer references.
    model.__dict__.clear()
    model.__dict__.update(restored_model.__dict__)


session.bind(
    predict_validation=predict_validation,
    predict_test=predict_test,
    save_checkpoint=save_checkpoint,
    load_checkpoint=load_checkpoint,
)

session.start_training(train_df["id"].astype(str).tolist())

rng = np.random.default_rng(2025)
batch_size = 16384
max_epochs = 2
first_update = True
stop_training = False

for _epoch in range(max_epochs):
    row_order = rng.permutation(len(train_df))

    for batch_start in range(0, len(row_order), batch_size):
        batch_positions = row_order[batch_start : batch_start + batch_size]
        batch_frame = train_df.iloc[batch_positions]

        batch_texts = normalize_comment_series(batch_frame["comment_text"])
        batch_features = make_model_matrix(batch_texts)
        batch_targets, batch_weights = compute_training_weights(batch_frame)

        if first_update:
            optimizer.partial_fit(
                batch_features,
                batch_targets,
                classes=np.array([0, 1], dtype=np.int8),
                sample_weight=batch_weights,
            )
            first_update = False
        else:
            optimizer.partial_fit(
                batch_features,
                batch_targets,
                sample_weight=batch_weights,
            )

        if session.step():
            stop_training = True
            break

    if stop_training:
        break

result = session.finish()
score = result["best_validation_score"]
print(f"Final Validation Score: {score}")
