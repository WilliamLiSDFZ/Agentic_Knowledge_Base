"""Offline contracts for explicit embedding windows and reusing saved summaries."""

import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import compare_vendi as cv


def sample(candidate="one", text="linear classifier", **changes):
    return dict(task="task", run_id="run", arm="A", candidate_id=candidate, stage="draft",
                view="implementation", text=text, extraction_status="ok") | changes


class ReembeddingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    @contextlib.contextmanager
    def model(self, model_type="bert", hard_limit=512):
        calls = dict(encoded=[], tokenized=[])

        class Encoder:
            max_seq_length = 256

            def __init__(self, model_name, revision=None, device=None):
                self.config = types.SimpleNamespace(_commit_hash="fixture-commit", model_type=model_type,
                                                    max_position_embeddings=hard_limit)

            def __getitem__(self, index):
                return types.SimpleNamespace(auto_model=types.SimpleNamespace(config=self.config))

            def tokenizer(self, text, truncation, verbose):
                calls["tokenized"].append((text, truncation, verbose))
                return {"input_ids": list(range(len(text.split())))}

            def encode(self, texts, normalize_embeddings):
                calls["encoded"].append((texts, self.max_seq_length, normalize_embeddings))
                return np.asarray([[1.0, 0.0]])

        module = types.ModuleType("sentence_transformers")
        module.SentenceTransformer = Encoder
        with patch.dict(sys.modules, {"sentence_transformers": module}), \
                patch("importlib.metadata.version", return_value="fixture-version"):
            yield calls

    def embed(self, row, max_length=None):
        return cv.embed_samples([row], self.root / "cache", "fake/model", max_length=max_length)

    def test_explicit_512_window_encodes_full_294_tokens_without_changing_default(self):
        text = " ".join(f"token{i}" for i in range(294))
        with self.model() as calls:
            default = sample(text=text)
            self.embed(default)
            self.assertEqual(default["error"], "embedding_token_limit")
            self.assertEqual(default["embedding_tokens"], 294)
            self.assertEqual(calls["encoded"], [])
            expanded = sample(text=text)
            identity = self.embed(expanded, max_length=512)
        self.assertEqual(expanded["extraction_status"], "ok")
        self.assertEqual(expanded["embedding_tokens"], 294)
        self.assertEqual(identity["max_seq_length"], 512)
        self.assertEqual(calls["encoded"], [([text], 512, True)])
        self.assertTrue(all(truncation is False and verbose is False
                            for _, truncation, verbose in calls["tokenized"]))

    def test_expansion_rejects_hard_limit_and_unverified_architectures(self):
        for model_type, hard_limit, requested in (("bert", 512, 513), ("bert", None, 512),
                                                  ("roberta", 512, 512), (None, 512, 512)):
            with self.subTest(model_type=model_type, hard_limit=hard_limit, requested=requested):
                with self.model(model_type, hard_limit) as calls:
                    with self.assertRaisesRegex(ValueError, "not verified"):
                        self.embed(sample(), max_length=requested)
                self.assertEqual(calls["encoded"], [])

    def test_different_windows_have_distinct_caches(self):
        with self.model() as calls:
            short, long, repeated = sample(), sample(), sample()
            short_identity = self.embed(short)
            long_identity = self.embed(long, max_length=512)
            repeated_identity = self.embed(repeated, max_length=512)
        self.assertEqual(short_identity["max_seq_length"], 256)
        self.assertEqual(long_identity["max_seq_length"], 512)
        self.assertEqual(long_identity, repeated_identity)
        self.assertNotEqual(short["embedding_model"], long["embedding_model"])
        self.assertEqual(len(calls["encoded"]), 2)
        self.assertEqual(len(list((self.root / "cache" / "embeddings").glob("*.json"))), 2)

    def test_reembed_clears_all_old_embedding_state_but_preserves_source(self):
        rows = [sample(embedding=[0, 1], embedding_model="old-model", embedding_tokens=21,
                       source_hash="original-code-hash", mechanism_card={"model": "linear classifier"}),
                sample("two", extraction_status="error", error="embedding_token_limit", embedding_tokens=294,
                       source_hash="second-code-hash", mechanism_card={"model": "linear classifier"})]
        originals = copy.deepcopy(rows)
        cv.prepare_reembedding(rows)
        for row, original in zip(rows, originals):
            for key in ("embedding", "embedding_model", "embedding_tokens", "error", "extraction_status"):
                self.assertNotIn(key, row)
            for key in ("text", "source_hash", "mechanism_card", "candidate_id"):
                self.assertEqual(row[key], original[key])

        # Exercise the actual CLI entry on a mixed prior result without any LLM calls.
        source, out = self.root / "input.jsonl", self.root / "out"
        source.write_text("".join(json.dumps(row) + "\n" for row in originals))
        with self.model() as calls, patch.object(cv, "Summarizer") as summarize, \
                contextlib.redirect_stdout(io.StringIO()):
            result = cv.main(["--input", str(source), "--reembed", "--embedding-max-length", "512",
                              "--cache", str(self.root / "cache"), "--out", str(out), "--no-plots"])
        summarize.assert_not_called()
        self.assertEqual(result, 0)
        exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
        self.assertEqual(len(exported), 2)
        self.assertEqual(len(calls["encoded"]), 1)  # Identical summaries reuse the new vector.
        for row, original in zip(exported, originals):
            self.assertEqual(row["extraction_status"], "ok")
            self.assertEqual(row["embedding"], [1.0, 0.0])
            self.assertNotEqual(row["embedding_model"], "old-model")
            self.assertEqual(row["source_hash"], original["source_hash"])
            self.assertEqual(row["mechanism_card"], original["mechanism_card"])
            self.assertNotIn("error", row)
        manifest = json.loads((out / "manifest.json").read_text())
        self.assertEqual(manifest["summary_api_calls"], 0)
        self.assertEqual(manifest["embedding"]["max_seq_length"], 512)

    def test_reembed_rejects_missing_text_before_mutating_any_rows(self):
        for text in ("", "   "):
            rows = [sample(embedding=[1, 0], embedding_model="old"), sample("two", text=text)]
            original = copy.deepcopy(rows)
            with self.assertRaisesRegex(ValueError, "requires nonempty text"):
                cv.prepare_reembedding(rows)
            self.assertEqual(rows, original)

    def test_precomputed_vectors_cannot_claim_new_window(self):
        row = sample(embedding=[1, 0], embedding_model="old")
        with patch.dict(sys.modules, {"sentence_transformers": None}):
            with self.assertRaisesRegex(ValueError, "use --reembed"):
                self.embed(row, max_length=512)


if __name__ == "__main__":
    unittest.main()
