"""Offline data, provenance, extraction-cache and CLI contracts for Vendi analysis."""

import contextlib
import csv
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import compare_vendi as cv


def sample(candidate="one", **changes):
    return dict(task="test-task", run_id="run-a", arm="A", candidate_id=candidate,
                stage="draft", text="model: logistic regression", **changes)


def card(model="linear classifier"):
    return dict(model=model, objective="cross entropy", data="", update="", inference="",
                change="", evidence=["CHILD:1"])


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def jsonl(self, rows):
        path = self.root / "input.jsonl"
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))
        return path

    def inventory(self, rows):
        path = self.root / "inventory.csv"
        fields = ["name", "task", "arm", "pair_id", "verdict"]
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        return path

    def journal(self, name, nodes):
        path = self.root / "runs" / name / "logs" / "journal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(dict(nodes=nodes)))
        return path

    def read_csv(self, path):
        with path.open(newline="") as stream:
            return list(csv.DictReader(stream))


class InputTests(WorkspaceTest):
    def test_required_metadata_and_embedding_identity(self):
        for key in ("task", "run_id", "arm", "candidate_id", "stage"):
            row = sample()
            del row[key]
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, key):
                cv.load_jsonl(self.jsonl([row]))
        with self.assertRaisesRegex(ValueError, "embedding_model"):
            cv.load_jsonl(self.jsonl([sample(embedding=[1, 0])]))

    def test_duplicate_exports_removed_but_repeated_mechanisms_retained(self):
        rows = cv.load_jsonl(self.jsonl([sample(), sample(), sample("two")]))
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["candidate_id"] for row in rows}, {"one", "two"})
        self.assertEqual(rows[0]["text"], rows[1]["text"])
        self.assertEqual(rows[0]["source_hash"], rows[1]["source_hash"])

    def test_conflicting_duplicate_candidate_is_rejected(self):
        other = sample() | {"text": "model: random forest"}
        with self.assertRaisesRegex(ValueError, "Conflicting duplicate"):
            cv.load_jsonl(self.jsonl([sample(), other]))

    def test_same_views_for_both_arms_with_complete_parent_child_source(self):
        nodes = [dict(id="root", stage="root"),
                 dict(id="parent", stage="draft", plan="Train a classifier.",
                      code="parent_start = 1\nparent_end = 2", is_valid=True),
                 dict(id="child", parent="parent", stage="improve", plan="Change the loss.",
                      code="child_start = 3\nchild_end = 4", is_buggy=True)]
        inventory = []
        for arm in ("A", "F"):
            name = f"run-{arm}"
            self.journal(name, nodes)
            inventory.append(dict(name=name, task="task", arm=arm, pair_id="p1", verdict="ok"))
        records, issues = cv.load_runs(self.root / "runs", self.inventory(inventory), "*",
                                      ["proposal", "implementation"])
        self.assertEqual(issues, [])
        self.assertEqual(len(records), 8)
        for view in ("proposal", "implementation"):
            selected = [r for r in records if r["candidate_id"] == "child" and r["view"] == view]
            self.assertEqual(selected[0]["source"], selected[1]["source"])
            self.assertEqual(selected[0]["pair_id"], "p1")
            self.assertTrue(selected[0]["is_buggy"])
        implementation = next(r for r in records if r["candidate_id"] == "child" and
                              r["view"] == "implementation")
        for text in ("PARENT:1: parent_start", "PARENT:2: parent_end"):
            self.assertIn(text, implementation["parent_source"])
        for text in ("CHILD:1: child_start", "CHILD:2: child_end"):
            self.assertIn(text, implementation["source"])

    def test_inventory_exclusions_and_missing_journal_are_reported(self):
        self.journal("invalid", [dict(id="x", stage="draft", code="pass", plan="Try it")])
        inventory = self.inventory([
            dict(name="invalid", task="task", arm="A", verdict="invalid"),
            dict(name="missing", task="task", arm="F", verdict="ok"),
        ])
        records, issues = cv.load_runs(self.root / "runs", inventory, "*", ["proposal"])
        self.assertEqual(records, [])
        by_run = {row["run_id"]: row["issue"] for row in issues}
        self.assertEqual(by_run["invalid"], "excluded_inventory_verdict")
        self.assertTrue(by_run["missing"].startswith("journal_unavailable:"))
        included, _ = cv.load_runs(self.root / "runs", inventory, "*", ["proposal"], True)
        self.assertEqual(len(included), 1)
        self.assertEqual(included[0]["inventory_verdict"], "invalid")

    def test_missing_source_has_coverage_instead_of_zero_score(self):
        self.journal("empty", [dict(id="x", stage="draft", plan="Use a linear model")])
        inventory = self.inventory([dict(name="empty", task="task", arm="A", verdict="ok")])
        records, issues = cv.load_runs(self.root / "runs", inventory, "*", ["implementation"])
        self.assertEqual(records[0]["extraction_status"], "missing_source")
        coverage = cv.coverage_rows(records, issues)[0]
        self.assertEqual(coverage["n_available"], 0)
        self.assertEqual(coverage["n_missing"], 1)

    def test_ambiguous_pair_is_rejected_before_summary_or_embedding(self):
        inventory = []
        for name in ("a-first", "a-second"):
            self.journal(name, [dict(id="x", stage="draft", code="x = 1", plan="Use a tree")])
            inventory.append(dict(name=name, task="task", arm="A", pair_id="same-pair", verdict="ok"))
        with patch.object(cv, "Summarizer") as summarize, patch.object(cv, "embed_samples") as embed:
            with self.assertRaisesRegex(ValueError, "Multiple runs for task/pair_id/arm"):
                cv.main(["--runs", str(self.root / "runs"), "--inventory", str(self.inventory(inventory)),
                         "--out", str(self.root / "out"), "--no-plots"])
        summarize.assert_not_called()
        embed.assert_not_called()
        self.assertFalse((self.root / "out").exists())


class ExtractionTests(WorkspaceTest):
    def test_text_embeddings_cache_revision_and_token_limit_without_real_model(self):
        import numpy as np

        encoded, tokenized = [], []

        class Encoder:
            max_seq_length = 5

            def __init__(self, model_name, revision=None, device=None):
                self.revision = revision

            def __getitem__(self, index):
                return types.SimpleNamespace(auto_model=types.SimpleNamespace(
                    config=types.SimpleNamespace(_commit_hash=self.revision)))

            def tokenizer(self, text, truncation, verbose=False):
                tokenized.append((text, truncation))
                return {"input_ids": list(range(len(text.split())))}

            def encode(self, texts, normalize_embeddings):
                encoded.append((self.revision, texts, normalize_embeddings))
                return np.asarray([[1.0, 0.0]])

        module = types.ModuleType("sentence_transformers")
        module.SentenceTransformer = Encoder
        cache = self.root / "cache"

        def row(text="linear classifier"):
            return sample() | dict(text=text, extraction_status="ok")

        with patch.dict(sys.modules, {"sentence_transformers": module}), \
                patch("importlib.metadata.version", return_value="fixture-version"):
            first = row()
            first_identity = cv.embed_samples([first], cache, "fake/model", "revision-1")
            cached = row()
            cv.embed_samples([cached], cache, "fake/model", "revision-1")
            self.assertEqual(cached["embedding"], first["embedding"])
            self.assertEqual(len(encoded), 1)
            changed = row()
            changed_identity = cv.embed_samples([changed], cache, "fake/model", "revision-2")
            self.assertNotEqual(first_identity, changed_identity)
            self.assertNotEqual(first["embedding_model"], changed["embedding_model"])
            self.assertEqual(len(encoded), 2)
            too_long = row("one two three four five six")
            cv.embed_samples([too_long], cache, "fake/model", "revision-2")
        self.assertEqual(too_long["extraction_status"], "error")
        self.assertEqual(too_long["error"], "embedding_token_limit")
        self.assertEqual(too_long["embedding_tokens"], 6)
        self.assertNotIn("embedding", too_long)
        self.assertEqual(len(encoded), 2)
        self.assertTrue(all(truncation is False for _, truncation in tokenized))

    def test_chunks_cover_every_character_even_for_long_lines(self):
        source = "first\n" + "a" * 3500 + "\n" + "many lines\n" * 800 + "last"
        chunks = cv.split_source(source, 1000)
        self.assertGreater(len(chunks), 2)
        self.assertEqual("".join(chunks), source)
        self.assertTrue(all(0 < len(chunk) <= 1000 for chunk in chunks))

    def test_cache_reused_and_source_model_prompt_changes_invalidate(self):
        ask = Mock(return_value=json.dumps(card()))
        summarizer = cv.Summarizer(self.root / "cache", model="fixed", ask=ask)
        first, count = summarizer.summarize("source one", "implementation")
        self.assertEqual(count, 1)
        self.assertEqual(first, card())
        again = cv.Summarizer(self.root / "cache", model="fixed", ask=ask)
        self.assertEqual(again.summarize("source one", "implementation")[0], first)
        self.assertEqual(ask.call_count, 1)
        again.summarize("source two", "implementation")
        cv.Summarizer(self.root / "cache", model="changed", ask=ask).summarize("source one", "implementation")
        with patch.object(cv, "SUMMARY_PROMPT", cv.SUMMARY_PROMPT + " changed"):
            again.summarize("source one", "implementation")
        self.assertEqual(ask.call_count, 4)

    def test_parent_and_child_stay_separate_until_comparison(self):
        prompts = []

        def ask(prompt):
            prompts.append(prompt)
            if prompt.startswith("Compare"):
                evidence = json.loads(prompt.split("\n", 1)[1])
                self.assertEqual(evidence["CHILD"]["model"], "kernel classifier")
                self.assertIn(evidence["PARENT"]["model"], ("linear classifier", "tree classifier"))
                return json.dumps(card("replace " + evidence["PARENT"]["model"] + " with kernel classifier"))
            if "PARENT:1:" in prompt:
                self.assertNotIn("CHILD:1:", prompt)
                return json.dumps(card("tree classifier" if "tree" in prompt else "linear classifier"))
            self.assertNotIn("PARENT:1:", prompt)
            return json.dumps(card("kernel classifier"))

        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        result, count = summarizer.summarize("CHILD:1: kernel()", "implementation", "PARENT:1: linear()")
        self.assertEqual(count, 2)
        self.assertEqual(result["model"], "replace linear classifier with kernel classifier")
        self.assertEqual(len(prompts), 3)
        result, _ = summarizer.summarize("CHILD:1: kernel()", "implementation", "PARENT:1: tree()")
        self.assertEqual(result["model"], "replace tree classifier with kernel classifier")
        self.assertEqual(len(prompts), 5)  # Child reused; changed parent and comparison recomputed.

    def test_bad_merge_is_reported_and_never_cached_as_success(self):
        self.journal("long", [dict(id="x", stage="draft", code="v = 1\n" * 700)])
        inventory = self.inventory([dict(name="long", task="task", arm="A", verdict="ok")])

        def ask(prompt):
            return '{"model": "missing required fields"}' if prompt.startswith("Merge") else json.dumps(card())

        cache, out = self.root / "cache", self.root / "out"
        summarizer = cv.Summarizer(cache, ask=ask, chunk_chars=1000)
        with patch.object(cv, "Summarizer", return_value=summarizer), patch.object(cv.time, "sleep"), \
                contextlib.redirect_stdout(io.StringIO()):
            result = cv.main(["--runs", str(self.root / "runs"), "--inventory", str(inventory),
                              "--views", "implementation", "--out", str(out), "--no-plots"])
        self.assertEqual(result, 2)
        row = json.loads((out / "samples.jsonl").read_text())
        self.assertEqual(row["extraction_status"], "error")
        self.assertTrue(row["error"].startswith("summary_failed:"))
        self.assertNotIn("embedding", row)
        for cached in (cache / "summaries").glob("*.json"):
            self.assertEqual(cv.validate_card(cached.read_text()), card())
        self.assertEqual(self.read_csv(out / "run_scores.csv"), [])


class OfflineCliTests(WorkspaceTest):
    def run_cli(self, arguments):
        # Fail on any attempt to initialize a chat client or load/download a model.
        runner = """
import importlib.abc, pathlib, runpy, sys
class BlockOnlineImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] in {'llm', 'openai', 'sentence_transformers'}:
            raise AssertionError('Offline CLI imported ' + fullname)
sys.meta_path.insert(0, BlockOnlineImports())
script = sys.argv[1]
sys.argv = sys.argv[1:]
sys.path.insert(0, str(pathlib.Path(script).parent))
runpy.run_path(script, run_name='__main__')
"""
        environment = os.environ | dict(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
        return subprocess.run([sys.executable, "-c", runner, str(ROOT / "scripts/compare_vendi.py"),
                               *arguments], cwd=self.root, env=environment, capture_output=True,
                              text=True, timeout=30)

    def test_precomputed_embeddings_complete_comparison_without_api(self):
        rows = []
        for arm, vectors in (("A", [[1, 0], [1, 0]]), ("F", [[1, 0], [0, 1]])):
            for index, vector in enumerate(vectors):
                rows.append(sample(str(index)) | dict(run_id=f"run-{arm}", arm=arm, pair_id="pair-1",
                                                      embedding=vector, embedding_model="fixture-v1"))
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(len(self.read_csv(out / "run_scores.csv")), 2)
        comparisons = self.read_csv(out / "comparisons.csv")
        pair = next(row for row in comparisons if row["kind"] == "pair")
        self.assertAlmostEqual(float(pair["delta"]), 1)
        self.assertEqual(pair["pair_id"], "pair-1")
        self.assertEqual(len(self.read_csv(out / "coverage.csv")), 2)
        manifest = json.loads((out / "manifest.json").read_text())
        self.assertEqual(manifest["summary_api_calls"], 0)
        self.assertEqual(manifest["embedding"]["backend"], "precomputed")
        self.assertTrue((out / "REPORT.md").is_file())

    def test_nonfinite_embeddings_are_exported_as_errors_without_crashing(self):
        rows = [sample(str(i), embedding=vector, embedding_model="fixture-v1")
                for i, vector in enumerate(([1, 0], [0, 1], [float("nan"), 1], [float("inf"), 1]))]
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
        self.assertEqual(len(exported), 4)
        errors = [row for row in exported if row["extraction_status"] == "error"]
        self.assertEqual(len(errors), 2)
        self.assertTrue(all(row["error"] == "invalid_embedding" and "embedding" not in row for row in errors))
        coverage = self.read_csv(out / "coverage.csv")[0]
        self.assertEqual(coverage["n_available"], "2")
        self.assertEqual(coverage["n_errors"], "2")
        self.assertEqual(len(self.read_csv(out / "run_scores.csv")), 1)
        self.assertTrue((out / "manifest.json").is_file())

    def test_mle_dry_run_creates_nothing_and_loads_no_online_client(self):
        self.journal("example", [dict(id="x", stage="draft", code="print(1)", plan="Train a tree")])
        inventory = self.inventory([dict(name="example", task="task", arm="F", verdict="ok")])
        out, cache = self.root / "out", self.root / "cache"
        result = self.run_cli(["--runs", str(self.root / "runs"), "--inventory", str(inventory),
                               "--out", str(out), "--cache", str(cache), "--dry-run"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["samples"], 2)
        self.assertEqual(report["runs"], 1)
        self.assertFalse(out.exists())
        self.assertFalse(cache.exists())


if __name__ == "__main__":
    unittest.main()
