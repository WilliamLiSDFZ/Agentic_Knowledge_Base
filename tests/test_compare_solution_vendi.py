"""Offline regression tests for whole-solution inputs and Vendi reports."""

import contextlib
import csv
import hashlib
import io
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import compare_solution_vendi as sv


def sample(candidate="one", **changes):
    return dict(task="test-task", run_id="run-A", arm="A", candidate_id=candidate,
                stage="solution", view="solution", original_stage="draft",
                representation_version="solution-v1", text="Linear classifier.") | changes


class SolutionVendiTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def jsonl(self, rows):
        path = self.root / "input.jsonl"
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))
        return path

    def journal(self, name, nodes, **extra):
        path = self.root / "runs" / name / "logs" / "journal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(dict(nodes=nodes) | extra))
        return path

    def inventory(self, rows):
        path = self.root / "inventory.csv"
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["name", "task", "arm", "pair_id", "verdict"])
            writer.writeheader()
            writer.writerows(rows)
        return path

    def read_csv(self, path):
        with path.open(newline="") as stream:
            return list(csv.DictReader(stream))

    def run_cli(self, arguments):
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
        return subprocess.run(
            [sys.executable, "-c", runner, str(ROOT / "scripts/compare_solution_vendi.py"), *arguments],
            cwd=self.root, env=os.environ | dict(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1"),
            capture_output=True, text=True, timeout=30)

    def test_all_candidate_stages_use_full_code_without_parent_dependency(self):
        code = "model = Linear()\ntrain(model)\n"
        nodes = [dict(id="root", stage="root", code="root is not a solution")]
        for index, stage in enumerate(("draft", "improve", "debug", "fusion_draft")):
            nodes.append(dict(id=str(index), stage=stage, code=code, parent="missing",
                              is_buggy=stage == "debug", is_valid=stage != "debug"))
        # A broken ancestry map must not make available whole implementations unusable.
        self.journal("example", nodes, node2parent={"unknown-child": 123})
        inventory = self.inventory([dict(name="example", task="task", arm="F", pair_id="p1", verdict="ok")])
        rows, issues = sv.load_solution_runs(self.root / "runs", inventory)
        self.assertEqual(issues, [])
        self.assertEqual(len(rows), 4)
        self.assertEqual({r["original_stage"] for r in rows}, {"draft", "improve", "debug", "fusion_draft"})
        for row in rows:
            self.assertEqual((row["stage"], row["view"], row["representation_version"]),
                             ("solution", "solution", "solution-v1"))
            self.assertEqual(row["source"], "SOURCE:1: model = Linear()\nSOURCE:2: train(model)")
            self.assertEqual(row["source_hash"], hashlib.sha256(code.encode()).hexdigest())
            self.assertEqual(row["extraction_status"], "pending")
            self.assertEqual(row["pair_id"], "p1")
            self.assertNotIn("change_packet", row)
            self.assertNotIn("assessment_status", row)
            self.assertFalse(row.get("parent_source"))
        self.assertTrue(next(r for r in rows if r["original_stage"] == "debug")["is_buggy"])

    def test_missing_code_is_not_replaced_by_plan_or_parent(self):
        self.journal("example", [dict(id="parent", stage="draft", code="print(1)"),
                                 dict(id="child", stage="improve", parent="parent", plan="Use a tree")])
        inventory = self.inventory([dict(name="example", task="task", arm="A", verdict="ok")])
        rows, _ = sv.load_solution_runs(self.root / "runs", inventory)
        child = next(row for row in rows if row["candidate_id"] == "child")
        self.assertEqual(child["extraction_status"], "missing_source")
        self.assertFalse(child["source"])

    def test_inventory_allowlist_verdicts_and_missing_journals(self):
        for name in ("valid", "invalid", "unlisted"):
            self.journal(name, [dict(id="x", stage="draft", code="print(1)")])
        inventory = self.inventory([
            dict(name="valid", task="task", arm="A", verdict="ok"),
            dict(name="invalid", task="task", arm="F", verdict="invalid"),
            dict(name="missing", task="task", arm="F", verdict="ok"),
        ])
        rows, issues = sv.load_solution_runs(self.root / "runs", inventory)
        self.assertEqual([row["run_id"] for row in rows], ["valid"])
        by_run = {row["run_id"]: row["issue"] for row in issues}
        self.assertEqual(by_run["invalid"], "excluded_inventory_verdict")
        self.assertTrue(by_run["missing"].startswith("journal_unavailable:"))
        included, _ = sv.load_solution_runs(self.root / "runs", inventory, include_invalid=True)
        self.assertEqual({row["run_id"] for row in included}, {"valid", "invalid"})

    def test_dry_run_reads_candidates_without_clients_or_writes(self):
        self.journal("example", [dict(id="d", stage="draft", code="print(1)"),
                                 dict(id="b", stage="debug", code="print(2)")])
        inventory = self.inventory([dict(name="example", task="task", arm="F", verdict="ok")])
        out, cache = self.root / "out", self.root / "cache"
        result = self.run_cli(["--runs", str(self.root / "runs"), "--inventory", str(inventory),
                               "--out", str(out), "--cache", str(cache), "--dry-run"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["samples"], 2)
        self.assertFalse(out.exists())
        self.assertFalse(cache.exists())

    def test_legacy_diff_inputs_are_rejected_before_model_calls(self):
        for changes in ({"representation_version": "diff-v1"}, {"stage": "improve"},
                        {"view": "implementation"}, {"representation_version": None},
                        {"mechanism_card": dict(model="linear", objective="cross entropy", data="",
                                                update="", inference="", change="loss reweighting",
                                                evidence=["CHILD:1"])}):
            with self.subTest(changes=changes):
                source = self.jsonl([sample(embedding=[1, 0], embedding_model="fixture-v1", **changes)])
                out = self.root / "out"
                result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Offline CLI imported", result.stderr)
                self.assertFalse(out.exists())

    def test_precomputed_full_and_matched_scores_preserve_duplicate_frequency(self):
        rows = []
        for arm, vectors in (("A", [[1, 0], [1, 0], [0, 1]]), ("F", [[1, 0], [0, 1]]), ("E", [[1, 0]])):
            for index, vector in enumerate(vectors):
                rows.append(sample(str(index), run_id=f"run-{arm}", arm=arm,
                                   pair_id="pair-1" if arm in ("A", "F") else "",
                                   embedding=vector, embedding_model="fixture-v1"))
        rows.append(rows[0].copy())  # Duplicate export, unlike two distinct identical candidates.
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        scores = {r["arm"]: r for r in self.read_csv(out / "run_scores.csv")}
        self.assertEqual(set(scores), {"A", "F"})
        self.assertEqual(scores["A"]["m"], "2")
        self.assertEqual(scores["A"]["n_total"], "3")
        self.assertAlmostEqual(float(scores["A"]["vendi"]), 5 / 3)
        self.assertAlmostEqual(float(scores["F"]["vendi"]), 2)
        full = {r["arm"]: r for r in self.read_csv(out / "full_run_scores.csv")}
        expected = math.exp(-(2 / 3) * math.log(2 / 3) - (1 / 3) * math.log(1 / 3))
        self.assertAlmostEqual(float(full["A"]["vendi"]), expected)
        self.assertEqual(float(full["E"]["vendi"]), 1)
        pair = next(r for r in self.read_csv(out / "comparisons.csv") if r["kind"] == "pair" and r["arm"] == "F")
        self.assertEqual(pair["pair_id"], "pair-1")
        self.assertAlmostEqual(float(pair["delta"]), 1 / 3)
        manifest = json.loads((out / "manifest.json").read_text())
        self.assertEqual(manifest["summary_api_calls"], 0)
        self.assertEqual(manifest["embedding"]["backend"], "precomputed")
        self.assertEqual(manifest["samples"], 6)
        for filename in ("coverage.csv", "solution_cards.csv", "samples.jsonl", "REPORT.md"):
            self.assertTrue((out / filename).is_file(), filename)

    def test_missing_solution_stays_in_coverage_and_never_becomes_zero(self):
        rows = [sample(str(i), embedding=vector, embedding_model="fixture-v1")
                for i, vector in enumerate(([1, 0], [0, 1]))]
        rows += [sample("one", arm="F", run_id="run-F", embedding=[1, 0], embedding_model="fixture-v1"),
                 sample("missing", arm="F", run_id="run-F", text="", extraction_status="missing_source")]
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        coverage = next(r for r in self.read_csv(out / "coverage.csv") if r["arm"] == "F")
        self.assertEqual((coverage["n_candidates"], coverage["n_available"], coverage["n_missing"]), ("2", "1", "1"))
        comparison = next(r for r in self.read_csv(out / "comparisons.csv") if r["kind"] == "unpaired_mean")
        self.assertEqual(comparison["delta"], "")
        self.assertEqual(comparison["status"], "insufficient_candidates")
        self.assertEqual({r["arm"] for r in self.read_csv(out / "run_scores.csv")}, {"A"})

    def test_reembed_reuses_surviving_text_and_preserves_missing_rows(self):
        rows = [sample("old", embedding=[0, 1], embedding_model="old-model"),
                sample("limited", text="Tree classifier.", extraction_status="error", error="embedding_token_limit"),
                sample("missing", text="", extraction_status="missing_source")]
        source, out = self.jsonl(rows), self.root / "out"

        def fake_embed(samples, *args, **kwargs):
            for row in samples:
                if row["text"]:
                    self.assertNotIn("embedding", row)
                    self.assertNotIn("error", row)
                    row.update(embedding=[1, 0], embedding_model="new-model", extraction_status="ok")
                else:
                    self.assertEqual(row["extraction_status"], "missing_source")
            return {"backend": "test"}

        with patch.object(sv, "embed_samples", side_effect=fake_embed) as embed, contextlib.redirect_stdout(io.StringIO()):
            result = sv.main(["--input", str(source), "--out", str(out), "--reembed", "--no-plots"])
        self.assertEqual(result, 2)
        embed.assert_called_once()
        exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
        self.assertEqual(len(exported), 3)
        missing = next(row for row in exported if row["candidate_id"] == "missing")
        self.assertNotIn("embedding", missing)
        self.assertEqual(missing["extraction_status"], "missing_source")

    def test_runs_extract_full_source_but_embed_only_neutral_summary(self):
        self.journal("example", [
            dict(id="a", stage="draft", code="model = Linear()", is_valid=True,
                 plan="F arm improves accuracy by analogy to paper X"),
            dict(id="b", stage="debug", code="model = Tree()", is_valid=False, is_buggy=True),
        ])
        inventory = self.inventory([dict(name="example", task="task", arm="F", verdict="ok")])
        summaries = ["Linear classification with cross entropy.", "Decision tree classification."]
        cards = [dict(title=f"Title {i}", summary=summary, evidence=["SOURCE:1"])
                 for i, summary in enumerate(summaries)]

        def fake_embed(rows, cache, model, revision, max_length):
            self.assertEqual([row["text"] for row in rows], summaries)
            self.assertEqual(max_length, 512)
            self.assertEqual(revision, sv.EMBEDDING_REVISION)
            for row, vector in zip(rows, ([1, 0], [0, 1])):
                row.update(embedding=vector, embedding_model="fixture-v1")
            return {"backend": "test"}

        out = self.root / "out"
        with patch.object(sv, "SolutionSummarizer") as factory, \
                patch.object(sv, "embed_samples", side_effect=fake_embed), \
                contextlib.redirect_stdout(io.StringIO()):
            summarizer = factory.return_value
            summarizer.model, summarizer.calls = "fixture-summary", 2
            summarizer.summarize_solution.side_effect = [(card, 1) for card in cards]
            result = sv.main(["--runs", str(self.root / "runs"), "--inventory", str(inventory),
                              "--out", str(out), "--no-plots"])
        self.assertEqual(result, 0)
        supplied = [call.args for call in summarizer.summarize_solution.call_args_list]
        self.assertEqual(supplied, [("SOURCE:1: model = Linear()",), ("SOURCE:1: model = Tree()",)])
        exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
        self.assertEqual([row["text"] for row in exported], summaries)
        self.assertEqual(exported[1]["original_stage"], "debug")
        self.assertFalse(exported[1]["is_valid"])
        self.assertNotIn("source", exported[0])
        self.assertEqual(self.read_csv(out / "solution_cards.csv")[0]["title"], "Title 0")

    def test_ambiguous_explicit_pair_fails_before_extraction_or_output(self):
        inventory_rows = []
        for name in ("a-first", "a-second"):
            self.journal(name, [dict(id="x", stage="draft", code="print(1)")])
            inventory_rows.append(dict(name=name, task="task", arm="A", pair_id="same", verdict="ok"))
        inventory, out = self.inventory(inventory_rows), self.root / "out"
        with patch.object(sv, "SolutionSummarizer") as summarize, patch.object(sv, "embed_samples") as embed:
            with self.assertRaisesRegex(ValueError, "Multiple runs for task/pair_id/arm"):
                sv.main(["--runs", str(self.root / "runs"), "--inventory", str(inventory), "--out", str(out)])
        summarize.assert_not_called()
        embed.assert_not_called()
        self.assertFalse(out.exists())

    def test_valid_only_preserves_excluded_candidate_in_coverage(self):
        rows = [sample(str(i), is_valid=i < 2, embedding=vector, embedding_model="fixture-v1")
                for i, vector in enumerate(([1, 0], [0, 1], [1, 0]))]
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--valid-only", "--no-plots"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        coverage = self.read_csv(out / "coverage.csv")[0]
        self.assertEqual((coverage["n_candidates"], coverage["n_available"], coverage["n_excluded"]), ("3", "2", "1"))
        self.assertEqual(self.read_csv(out / "full_run_scores.csv")[0]["n_total"], "2")

    def test_missing_journal_fails_but_intentional_inventory_exclusion_does_not(self):
        self.journal("baseline", [dict(id="a", stage="draft", code="model = Linear()"),
                                  dict(id="b", stage="debug", code="model = Tree()")])
        card = dict(title="Classifier", summary="Train a classifier.", evidence=["SOURCE:1"])

        def fake_embed(rows, *args):
            for row in rows:
                row.update(embedding=[1, 0], embedding_model="fixture-v1")
            return {"backend": "test"}

        for verdict, expected in (("ok", 2), ("invalid", 0)):
            with self.subTest(verdict=verdict):
                inventory = self.inventory([
                    dict(name="baseline", task="task", arm="A", verdict="ok"),
                    dict(name="missing", task="task", arm="F", verdict=verdict),
                ])
                out, stdout = self.root / verdict, io.StringIO()
                with patch.object(sv, "SolutionSummarizer") as factory, \
                        patch.object(sv, "embed_samples", side_effect=fake_embed), \
                        contextlib.redirect_stdout(stdout):
                    summarizer = factory.return_value
                    summarizer.model, summarizer.calls = "fixture-summary", 2
                    summarizer.summarize_solution.return_value = (card, 1)
                    result = sv.main(["--runs", str(self.root / "runs"), "--inventory", str(inventory),
                                      "--out", str(out), "--no-plots"])
                self.assertEqual(result, expected, stdout.getvalue())
                self.assertEqual(len(self.read_csv(out / "run_scores.csv")), 1)
                missing = next(r for r in self.read_csv(out / "coverage.csv") if r["run_id"] == "missing")
                if verdict == "ok":
                    self.assertIn("INCOMPLETE", stdout.getvalue())
                    self.assertIn("journal_unavailable", stdout.getvalue())
                    self.assertTrue(missing["issue"].startswith("journal_unavailable:"))
                else:
                    self.assertNotIn("INCOMPLETE", stdout.getvalue())
                    self.assertEqual(missing["issue"], "excluded_inventory_verdict")

    def test_nonfinite_precomputed_vectors_become_reported_errors(self):
        rows = [sample(str(i), embedding=vector, embedding_model="fixture-v1")
                for i, vector in enumerate(([1, 0], [0, 1], [float("nan"), 1], [float("inf"), 1]))]
        source, out = self.jsonl(rows), self.root / "out"
        result = self.run_cli(["--input", str(source), "--out", str(out), "--no-plots"])
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("invalid_embedding", result.stdout)
        coverage = self.read_csv(out / "coverage.csv")[0]
        self.assertEqual((coverage["n_candidates"], coverage["n_available"], coverage["n_errors"]), ("4", "2", "2"))
        self.assertAlmostEqual(float(self.read_csv(out / "run_scores.csv")[0]["vendi"]), 2)
        exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
        failed = [row for row in exported if row["extraction_status"] == "error"]
        self.assertEqual(len(failed), 2)
        self.assertTrue(all(row["error"] == "invalid_embedding" and "embedding" not in row for row in failed))
        self.assertTrue((out / "manifest.json").exists())

    def test_prefixes_share_folder_and_cleanup_only_their_own_plots(self):
        source = self.jsonl([sample(str(i), embedding=vector, embedding_model="fixture-v1")
                             for i, vector in enumerate(([1, 0], [0, 1]))])
        out = self.root / "out"

        def fake_plots(directory, scores, comparisons, coverage=None, prefix=""):
            (directory / f"{prefix}vendi_01.png").write_bytes(b"plot")
            (directory / f"{prefix}paired_deltas.png").write_bytes(b"pairs")

        filenames = ("solution_cards.csv", "full_run_scores.csv", "run_scores.csv", "comparisons.csv",
                     "coverage.csv", "samples.jsonl", "manifest.json", "REPORT.md", "vendi_01.png", "paired_deltas.png")
        with patch.object(sv, "plot_results", side_effect=fake_plots), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sv.main(["--input", str(source), "--out", str(out), "--prefix", "first"]), 0)
            first = {name: (out / f"first_{name}").read_bytes() for name in filenames}
            self.assertEqual(sv.main(["--input", str(source), "--out", str(out), "--prefix", "second"]), 0)
            second = {name: (out / f"second_{name}").read_bytes() for name in filenames}
            self.assertEqual(first, {name: (out / f"first_{name}").read_bytes() for name in filenames})
            for name in ("vendi_01.png", "paired_deltas.png", "unrelated_vendi_01.png"):
                (out / name).write_bytes(b"unrelated")
            (out / "first_vendi_02.png").write_bytes(b"stale")
            self.assertEqual(sv.main(["--input", str(source), "--out", str(out), "--prefix", "first", "--no-plots"]), 0)
        self.assertEqual(second, {name: (out / f"second_{name}").read_bytes() for name in filenames})
        for name in ("first_vendi_01.png", "first_vendi_02.png", "first_paired_deltas.png"):
            self.assertFalse((out / name).exists(), name)
        for name in ("vendi_01.png", "paired_deltas.png", "unrelated_vendi_01.png"):
            self.assertEqual((out / name).read_bytes(), b"unrelated")
        for name in filenames[:-2]:
            self.assertFalse((out / name).exists(), name)
        report = (out / "first_REPORT.md").read_text()
        for name in ("run_scores.csv", "comparisons.csv", "full_run_scores.csv", "solution_cards.csv",
                     "samples.jsonl", "coverage.csv", "manifest.json"):
            self.assertIn(f"first_{name}", report)

    def test_prefix_rejects_paths_globs_and_non_ascii_before_writes(self):
        source = self.jsonl([sample(embedding=[1, 0], embedding_model="fixture-v1")])
        for prefix in ("../escape", "path/name", "path\\name", "all*", "x[ab]", "with space", "a.b", "中文"):
            with self.subTest(prefix=prefix):
                out = self.root / "out"
                result = self.run_cli(["--input", str(source), "--out", str(out), "--prefix", prefix, "--no-plots"])
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("prefix", result.stderr)
                self.assertNotIn("Offline CLI imported", result.stderr)
                self.assertFalse(out.exists())

    def test_prefixed_manifest_guard_only_checks_its_own_artifacts(self):
        source = self.jsonl([sample(str(i), embedding=vector, embedding_model="fixture-v1")
                             for i, vector in enumerate(([1, 0], [0, 1]))])
        out = self.root / "out"
        out.mkdir()
        legacy = json.dumps({"representation_version": "diff-v1"})
        for name in ("manifest.json", "legacy_manifest.json"):
            (out / name).write_text(legacy)
        result = self.run_cli(["--input", str(source), "--out", str(out), "--prefix", "fresh", "--no-plots"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_cli(["--input", str(source), "--out", str(out), "--prefix", "legacy", "--no-plots"])
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Offline CLI imported", result.stderr)
        self.assertFalse((out / "legacy_run_scores.csv").exists())
        for name in ("manifest.json", "legacy_manifest.json"):
            self.assertEqual((out / name).read_text(), legacy)


if __name__ == "__main__":
    unittest.main()
