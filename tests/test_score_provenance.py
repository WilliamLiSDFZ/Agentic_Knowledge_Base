"""Prevent comparisons across grading definitions or reuse of broken jubias scores."""

import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from analyze_runs import load_scores

JUBIAS = "jigsaw-unintended-bias-in-toxicity-classification"


class ScoreProvenanceTests(unittest.TestCase):
    def load(self, rows, variant="capped"):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scores.csv"
            with path.open("w", newline="") as fh:
                fields = ["run", "competition", "variant", "k", "score", "lower_better",
                          "metric_version", "grader_sha256"]
                writer = csv.DictWriter(fh, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            return load_scores(path, variant)

    def row(self, **changes):
        row = dict(run="run-a", competition=JUBIAS, variant="capped", k=1, score=0.92,
                   lower_better=0, metric_version="jubias-continuous-auc-v1", grader_sha256="fixed")
        return row | changes

    def test_corrected_scores_and_other_legacy_tasks(self):
        scores, _ = self.load([self.row(), self.row(run="run-b", competition="jigsaw-toxic-comment-classification-challenge",
                                                   metric_version="", grader_sha256="")])
        self.assertEqual(scores["run-a"][1], 0.92)
        self.assertIn("run-b", scores)

    def test_mixed_versions_or_hashes_are_rejected(self):
        for changes in ({"metric_version": "", "grader_sha256": ""},
                        {"grader_sha256": "different"}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "Mixed grading versions"):
                self.load([self.row(), self.row(run="run-b", **changes)])

    def test_all_legacy_jubias_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Uncorrected/unversioned"):
            self.load([self.row(metric_version="", grader_sha256="")])

    def test_other_fusion_variant_is_not_mixed(self):
        scores, _ = self.load([self.row(), self.row(run="run-b", variant="uncapped", metric_version="old")])
        self.assertEqual(set(scores), {"run-a"})


if __name__ == "__main__":
    unittest.main()
