"""Keep Top-25 comparisons paired, separate from legacy KB arms, and honest about gaps."""

from contextlib import redirect_stderr, redirect_stdout
import csv
import io
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import analyze_runs as ar
import plot_effects as pe

JUBIAS = "jigsaw-unintended-bias-in-toxicity-classification"


class DraftRerankAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_from_config(self, seed=42, **changes):
        cfg = {"exp_id": JUBIAS, "agent": {"seed": seed}, **changes}
        path = self.root / "config.yaml"
        path.write_text(yaml.safe_dump(cfg))
        run = ar.Run(started="2026-10-23 02:30:00", usable_fraction=1,
                     wrapper_completed=True, log_span_h=12, n_ensembles=1,
                     n_nodes=10, n_valid=8, n_buggy=2, buggy_fraction=0.2,
                     maximize_used=True)
        ar.parse_config(run, path)
        run.name = f"20261023_023000_{run.arm}_s{seed}"
        return run

    def paired_runs(self):
        return [self.run_from_config(seed, draft_techniques={"enabled": enabled})
                for seed in (42, 43, 44) for enabled in (False, True)]

    def test_legacy_arms_are_unchanged(self):
        cases = [
            ("A", {}),
            ("B", {"methodology_kb_path": "kb", "methodology_retrieval": "lazy"}),
            ("C", {"methodology_kb_path": "kb", "methodology_retrieval": "lazy",
                   "coldstart": {"inject_into_improve": True}}),
            ("D", {"analogy": {"enabled": True}}),
            ("E", {"analogy": {"enabled": True, "draft": True, "improve": False}}),
            ("F", {"analogy": {"enabled": True, "draft": True, "improve": True}}),
        ]
        for arm, cfg in cases:
            with self.subTest(arm=arm):
                self.assertEqual(self.run_from_config(**cfg).arm, arm)

    def test_new_configs_identify_fixed_baseline_and_top25(self):
        for enabled, arm in ((False, "A"), (True, "G")):
            with self.subTest(enabled=enabled):
                run = self.run_from_config(draft_techniques={"enabled": enabled})
                self.assertEqual((run.arm, run.wiring, run.task), (arm, "fixed", JUBIAS))
                if enabled:
                    self.assertEqual(run.retrieval, "corpus_top25")
        run = self.run_from_config(draft_techniques={"enabled": True},
                                   analogy={"enabled": True},
                                   methodology_kb_path="kb", methodology_retrieval="lazy")
        self.assertEqual((run.arm, run.retrieval), ("G", "corpus_top25"))

    def test_six_runs_form_three_seed_pairs(self):
        runs = self.paired_runs()
        groups = ar.build_groups(runs)
        self.assertEqual(len(groups), 3)
        self.assertEqual({g.seeds for g in groups}, {"42", "43", "44"})
        for group in groups:
            self.assertEqual(set(group.arms), {"A", "G"})
            self.assertTrue(group.usable)
            self.assertFalse(group.borrowed)
            self.assertEqual(group.arms["A"].seed, group.arms["G"].seed)

    def test_missing_baseline_borrows_nearest_same_seed_before_or_after(self):
        for nearest_day in (22, 24):
            with self.subTest(nearest_day=nearest_day):
                baselines = []
                for day in (20, nearest_day, 26):
                    baseline = self.run_from_config(draft_techniques={"enabled": False})
                    baseline.started = f"2026-10-{day} 02:30:00"
                    baseline.name = f"baseline-{day}"
                    baselines.append(baseline)
                treatment = self.run_from_config(draft_techniques={"enabled": True})
                for runs in (baselines + [treatment], [treatment] + baselines[::-1]):
                    group = next(g for g in ar.build_groups(runs) if "G" in g.arms)
                    self.assertIs(group.arms["A"], baselines[1])
                    self.assertTrue(group.usable)
                    self.assertEqual(group.borrowed, {"A"})

    def test_missing_baseline_requires_known_same_seed_task_and_valid_donor(self):
        for changes in ({"seed": 43}, {"task": "essay"}, {"verdict": "invalid"},
                        {"verdict": "superseded"}, {"seed": None}):
            with self.subTest(changes=changes):
                baseline = self.run_from_config(draft_techniques={"enabled": False})
                baseline.started = "2026-10-24 02:30:00"
                for key, value in changes.items():
                    setattr(baseline, key, value)
                treatment = self.run_from_config(draft_techniques={"enabled": True})
                if changes == {"seed": None}:
                    treatment.seed = None
                group = next(g for g in ar.build_groups([baseline, treatment]) if "G" in g.arms)
                self.assertEqual(set(group.arms), {"G"})
                self.assertFalse(group.usable)
                self.assertFalse(group.borrowed)

    def test_baseline_is_borrowed_only_once_and_can_be_disabled(self):
        baseline = self.run_from_config(draft_techniques={"enabled": False})
        baseline.started = "2026-10-24 02:30:00"
        treatments = [self.run_from_config(draft_techniques={"enabled": True}) for _ in range(2)]
        treatments[1].started = "2026-10-25 02:30:00"
        treatments[1].name = "later-G"
        runs = [baseline] + treatments
        groups = [g for g in ar.build_groups(runs) if "G" in g.arms]
        self.assertEqual([g.borrowed for g in groups], [{"A"}, set()])
        with patch.object(ar, "THRESHOLDS", ar.Thresholds(allow_cross_wiring_baseline=False)):
            groups = [g for g in ar.build_groups(runs) if "G" in g.arms]
        self.assertTrue(all(set(g.arms) == {"G"} for g in groups))

    def test_g_donor_is_not_consumed_by_older_legacy_arm(self):
        baseline = self.run_from_config(draft_techniques={"enabled": False})
        baseline.started = "2026-10-24 02:30:00"
        treatment = self.run_from_config(draft_techniques={"enabled": True})
        old = self.run_from_config(methodology_kb_path="kb", methodology_retrieval="lazy")
        old.started = "2026-10-20 02:30:00"
        group = next(g for g in ar.build_groups([old, treatment, baseline]) if "G" in g.arms)
        self.assertIs(group.arms["A"], baseline)
        self.assertEqual(group.borrowed, {"A"})

    def test_wrong_metric_direction_is_excluded(self):
        run = self.run_from_config(draft_techniques={"enabled": True})
        ar.apply_rules(run, {})
        self.assertEqual(run.verdict, "ok")
        run.maximize_used = False
        ar.apply_rules(run, {})
        self.assertEqual(run.verdict, "invalid")
        self.assertIn("metric_direction_wrong", run.reasons)

    def test_four_charts_and_paired_statistics(self):
        runs = self.paired_runs()
        groups = ar.build_groups(runs)
        # Synthetic private scores are test fixtures, never written into a results directory.
        scores = {r.name: {1: 0.8 + 0.001 * r.seed + (0.01 if r.arm == "G" else 0)}
                  for r in runs}
        for run in runs:
            if run.arm == "G":
                scores[run.name][2] = 0.99
        files = ar.build_charts(groups, scores, {}, runs, self.root)
        process_files, process_stats = ar.build_process_charts(groups, runs, self.root)
        self.assertEqual(set(files + process_files), {
            f"{JUBIAS}_paired.png", f"{JUBIAS}_effect.png", f"{JUBIAS}_vs_k.png",
            f"{JUBIAS}_process.png", "summary.md",
        })
        for filename in files + process_files:
            if filename.endswith(".png"):
                self.assertTrue((self.root / filename).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
        summary = (self.root / "summary.md").read_text()
        self.assertIn("3 usable draw(s), compared at K=1", summary)
        self.assertIn("| G-A | 3 | +0.01000 |", summary)
        self.assertEqual({s["contrast"] for _, stats in process_stats for s in stats}, {"G-A"})
        self.assertTrue(all(s["n"] == 3 for _, stats in process_stats for s in stats))
        self.assertIn("G", pe.ARMS)
        self.assertEqual(pe.ARM_LABEL["G"], "G  Top-25 @ every draft")

    def test_missing_scores_do_not_create_a_comparison(self):
        runs = self.paired_runs()
        scores = {r.name: {1: 0.9} for r in runs if r.arm == "A"}
        files = ar.build_charts(ar.build_groups(runs), scores, {}, runs, self.root)
        self.assertEqual(files, ["summary.md"])
        self.assertNotIn("| G-A |", (self.root / "summary.md").read_text())

    def test_borrowed_baseline_is_reported_as_unpaired(self):
        runs = self.paired_runs()
        runs[0].started = "2026-10-24 02:30:00"
        groups = ar.build_groups(runs)
        scores = {r.name: {1: 0.9} for r in runs}
        ar.build_charts(groups, scores, {}, runs, self.root)
        summary = (self.root / "summary.md").read_text()
        row = next(line for line in summary.splitlines() if line.startswith("| G-A |"))
        self.assertIn("| G-A | 3 |", row)
        self.assertIn("(unpaired)", row)
        _, process_stats = ar.build_process_charts(groups, runs, self.root)
        self.assertTrue(all(s["unpaired"] for _, stats in process_stats for s in stats))

    def test_one_valid_pair_still_has_process_points_without_intervals(self):
        runs = self.paired_runs()
        for run in runs:
            if (run.seed, run.arm) in {(43, "G"), (44, "A")}:
                run.n_ensembles = 0
            ar.apply_rules(run, {})
        groups = ar.build_groups(runs)
        self.assertEqual(sum(group.usable for group in groups), 1)

        with patch.object(pe.plt, "close"):
            files, all_stats = ar.build_process_charts(groups, runs, self.root)
            figure = pe.plt.gcf()
        try:
            self.assertEqual(files, [f"{JUBIAS}_process.png"])
            stats = all_stats[0][1]
            self.assertEqual(len(stats), len(pe.PROCESS_METRICS))
            for stat in stats:
                self.assertEqual((stat["contrast"], stat["n"]), ("G-A", 1))
                self.assertTrue(math.isnan(stat["lo"]) and math.isnan(stat["hi"]))
            for axis in figure.axes:
                self.assertIn("G-A (n=1)", [text.get_text() for text in axis.texts])
                # A point estimate and the vertical zero line are allowed; an interval is not.
                for line in axis.lines:
                    xs = line.get_xdata()
                    self.assertTrue(len(xs) == 1 or xs[0] == xs[1])
            self.assertTrue((self.root / files[0]).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
        finally:
            pe.plt.close(figure)

    def test_cli_selects_six_runs_from_shared_results(self):
        shared = self.root / "results"
        out = self.root / "analysis"
        runs = self.paired_runs()
        old = self.run_from_config(draft_techniques={"enabled": False})
        old.name = "20261020_023000_old_baseline"
        old.started = "2026-10-20 02:30:00"
        for run in runs + [old]:
            logs = shared / run.name / "logs"
            logs.mkdir(parents=True)
            (logs / "config.yaml").write_text(yaml.safe_dump({
                "exp_id": JUBIAS, "agent": {"seed": run.seed},
                "draft_techniques": {"enabled": run.arm == "G"},
            }))
            day = run.started[:10]
            (logs / "MLEvolve.log").write_text(
                f"[{day} 02:30:00] INFO: Starting run\n"
                f"[{day} 14:30:00] INFO: Completed run\n")
            (logs / "journal.json").write_text(json.dumps({"nodes": [{"is_valid": True}]}))
            ensembles = shared / run.name / "workspace" / "ensembles_csv"
            ensembles.mkdir(parents=True)
            (ensembles / "1.csv").write_text("id,prediction\n0,0.9\n")
        argv = ["analyze_runs.py", "--runs", str(shared), "--out", str(out),
                "--run-names", *(run.name for run in runs)]
        with patch.object(sys, "argv", argv), redirect_stdout(io.StringIO()):
            self.assertEqual(ar.main(), 0)
        with (out / "run_inventory.csv").open() as fh:
            inventory = list(csv.DictReader(fh))
        with (out / "groups.csv").open() as fh:
            groups = list(csv.DictReader(fh))
        self.assertEqual({row["name"] for row in inventory}, {run.name for run in runs})
        self.assertEqual(len(inventory), 6)
        self.assertEqual(len(groups), 3)
        self.assertTrue(all(row["arms"] == "AG" for row in groups))

    def test_cli_rejects_missing_selected_run(self):
        argv = ["analyze_runs.py", "--runs", str(self.root), "--out", str(self.root / "out"),
                "--run-names", "missing-run"]
        stderr = io.StringIO()
        with patch.object(sys, "argv", argv), redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as caught:
                ar.main()
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("missing-run", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
