"""Regression checks for runtime artifact accounting (synthetic data only)."""

import json
from pathlib import Path
import tempfile
import unittest

from analyze_runs import Run, parse_candidate_results


class RuntimeAnalysisTests(unittest.TestCase):
    def test_execution_and_artifact_counts_are_separate(self):
        candidates = []
        for status, usable in [("completed", True), ("budget_exhausted", True),
                               ("failed", True), ("timeout", True), ("running", True),
                               ("failed", False), ("completed", False)]:
            candidates.append(dict(execution={"status": status},
                                   artifact_status="scoreable" if usable else "unavailable",
                                   first_published_at=4600 if usable else None,
                                   validation_seconds=36, export_seconds=18))
        summary = dict(contract={"metric_version": "jubias-continuous-auc-v1"},
                       run={"started_at": 1000}, candidates=candidates)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "summary.json"
            path.write_text(json.dumps(summary))
            run = Run(n_nodes=3, n_valid=1, n_buggy=2)
            parse_candidate_results(run, path)
        self.assertEqual((run.n_nodes, run.n_valid, run.n_buggy), (3, 1, 2))
        self.assertEqual(run.runtime_scoreable, 5)
        self.assertEqual(run.runtime_completed, 1)
        self.assertEqual(run.runtime_budget_stops, 1)
        self.assertEqual(run.runtime_failed_with_result, 2)
        self.assertEqual(run.runtime_unfinished_with_result, 1)
        self.assertEqual(run.runtime_without_result, 2)
        self.assertEqual(run.runtime_first_result_h, 1.0)
        self.assertAlmostEqual(run.runtime_validation_h, 0.07)
        self.assertAlmostEqual(run.runtime_export_h, 0.035)

    def test_legacy_runs_have_no_invented_runtime_measurements(self):
        with tempfile.TemporaryDirectory() as directory:
            run = Run(n_nodes=7, n_valid=1)
            parse_candidate_results(run, Path(directory) / "absent.json")
        self.assertEqual(run.runtime_candidates, 0)
        self.assertIsNone(run.runtime_first_result_h)
        self.assertEqual(run.n_nodes, 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
