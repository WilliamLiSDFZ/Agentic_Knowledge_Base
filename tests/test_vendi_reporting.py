"""Plots use explicit pairs and retain separate task/batch identities."""

import csv
from pathlib import Path
import tempfile
import unittest

from scripts.vendi.metrics import score_samples
from scripts.vendi.reporting import plot_results, plotting_rows, write_plot_data


def samples(run, arm, vectors, batch="early", pair_id="", task="task"):
    return [dict(task=task, batch=batch, run_id=run, arm=arm, pair_id=pair_id,
                 stage="solution", view="solution", extraction_status="ok", embedding=vector)
            for vector in vectors]


class PlottingRowsTests(unittest.TestCase):
    def test_complete_pairs_and_unpaired_batch_means_have_separate_roles(self):
        data = (samples("a", "A", [[1, 0]] * 3, pair_id="p1")
                + samples("f", "F", [[1, 0], [0, 1], [1, 0]], pair_id="p1")
                + samples("a2", "A", [[1, 0]] * 2, batch="late")
                + samples("f2", "F", [[1, 0], [0, 1]], batch="late"))
        scores, comparisons = score_samples(data)
        curves, effects, paired = plotting_rows(scores, comparisons)
        self.assertEqual(curves, scores)
        self.assertEqual({(row["batch"], row["kind"]) for row in effects},
                         {("early", "pair"), ("late", "unpaired_mean")})
        self.assertEqual(len(paired), 1)
        self.assertEqual((paired[0]["m"], paired[0]["task_common_m"]), (2, 2))
        self.assertEqual((paired[0]["baseline_run_id"], paired[0]["run_id"]), ("a", "f"))

    def test_endpoint_uses_each_tasks_common_maximum_not_every_m(self):
        data = (samples("a", "A", [[1, 0]] * 3, pair_id="p1")
                + samples("f", "F", [[1, 0], [0, 1], [1, 0]], pair_id="p1")
                + samples("a2", "A", [[1, 0]] * 2, pair_id="p2", task="second")
                + samples("f2", "F", [[1, 0], [0, 1]], pair_id="p2", task="second"))
        _, effects, paired = plotting_rows(*score_samples(data))
        self.assertEqual(len(effects), 3)
        self.assertEqual({(row["task"], row["m"]) for row in paired}, {("task", 3), ("second", 2)})

    def test_missing_explicit_pairs_are_never_connected(self):
        data = (samples("a", "A", [[1, 0]] * 2, pair_id="p1")
                + samples("f", "F", [[1, 0], [0, 1]], pair_id="p2"))
        _, effects, paired = plotting_rows(*score_samples(data))
        self.assertEqual(paired, [])
        self.assertEqual([row["kind"] for row in effects], ["unpaired_mean"])

    def test_one_set_of_three_figures_and_csvs_even_without_pairs(self):
        data = samples("a", "A", [[1, 0]] * 2) + samples("f", "F", [[1, 0], [0, 1]])
        scores, comparisons = score_samples(data)
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            artifacts = plot_results(out, scores, comparisons)
            self.assertEqual(set(artifacts), {f"{name}.{ext}" for name in ("vendi", "effect", "paired")
                                             for ext in ("png", "pdf", "csv")})
            self.assertTrue(all((out / name).stat().st_size > 0 for name in artifacts))
            with (out / "paired.csv").open(newline="") as stream:
                self.assertEqual(list(csv.DictReader(stream)), [])
            with (out / "effect.csv").open(newline="") as stream:
                effect = list(csv.DictReader(stream))
            self.assertEqual(len(effect), 1)
            self.assertEqual(effect[0]["kind"], "unpaired_mean")
            self.assertEqual(effect[0]["batch"], "early")
            with (out / "vendi.csv").open(newline="") as stream:
                self.assertEqual(len(list(csv.DictReader(stream))), len(scores))

    def test_empty_data_exports_csv_headers_without_plotting(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            self.assertEqual(write_plot_data(out, [], []), dict(vendi=[], effect=[], paired=[]))
            self.assertEqual({path.name for path in out.iterdir()}, {"vendi.csv", "effect.csv", "paired.csv"})
            for path in out.iterdir():
                with path.open(newline="") as stream:
                    reader = csv.DictReader(stream)
                    self.assertIn("batch", reader.fieldnames)
                    self.assertEqual(list(reader), [])


if __name__ == "__main__":
    unittest.main()
