"""Numerical definitions and comparison boundaries for offline Vendi scoring."""

import math
import unittest

import numpy as np

from scripts.vendi_metrics import compare_samples, vendi_score


def samples(run, arm, vectors, task="task", pair_id="", stage="draft", view="proposal"):
    return [dict(task=task, run_id=run, arm=arm, pair_id=pair_id, stage=stage,
                 view=view, embedding=vector) for vector in vectors]


class VendiScoreTests(unittest.TestCase):
    def test_identical_orthogonal_and_singleton(self):
        self.assertAlmostEqual(vendi_score([[1, 2], [2, 4], [3, 6]]), 1)
        self.assertAlmostEqual(vendi_score(np.eye(5)), 5)
        self.assertEqual(vendi_score([[1, 0]]), 1)

    def test_repeated_frequencies_are_not_deduplicated(self):
        expected = math.exp(-0.75 * math.log(0.75) - 0.25 * math.log(0.25))
        self.assertAlmostEqual(vendi_score([[1, 0]] * 3 + [[0, 1]]), expected)

    def test_permutation_scale_and_negative_cosine(self):
        values = np.array([[1, 0], [0, 1], [-1, 0]], dtype=float)
        expected = vendi_score(values)
        self.assertAlmostEqual(vendi_score(values[[2, 0, 1]]), expected)
        self.assertAlmostEqual(vendi_score(values * [[100], [0.01], [2]]), expected)
        # Opposite vectors yield one nonzero spectral eigenvalue, not score 2.
        self.assertAlmostEqual(vendi_score([[1, 0], [-1, 0]]), 1)

    def test_official_readme_kernel_example(self):
        # Gram matrix [[1, .9, 0], [.9, 1, 0], [0, 0, 1]].
        vectors = [[1, 0, 0], [0.9, math.sqrt(0.19), 0], [0, 0, 1]]
        probabilities = np.array([0.1, 1, 1.9]) / 3
        expected = float(np.exp(-np.sum(probabilities * np.log(probabilities))))
        self.assertAlmostEqual(vendi_score(vectors), expected)
        self.assertAlmostEqual(expected, 2.1573, places=4)

    def test_invalid_vectors_and_extreme_scales(self):
        for values in ([], [[0, 0]], [[float("nan"), 1]], [[float("inf"), 1]],
                       [1, 2], [[1, 2], [1]]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                vendi_score(values)
        self.assertAlmostEqual(vendi_score([[1e300, 0], [0, 1e-300]]), 2)


class VendiComparisonTests(unittest.TestCase):
    def test_equal_n_fixed_cohort_and_explicit_pair(self):
        data = (samples("a", "A", [[1, 0]] * 4, pair_id="p1")
                + samples("f", "F", [[1, 0], [0, 1]], pair_id="p1")
                + samples("a-short", "A", [[1, 0]]))
        scores, comparisons = compare_samples(data)
        self.assertEqual({row["m"] for row in scores}, {2})
        self.assertEqual({row["run_id"] for row in scores}, {"a", "f"})
        self.assertEqual({row["n_total"] for row in scores}, {2, 4})
        a = next(row for row in scores if row["arm"] == "A")
        self.assertEqual(a["n_subsets"], 6)
        for row in comparisons:
            self.assertAlmostEqual(row["delta"], 1)
        self.assertEqual({row["kind"] for row in comparisons},
                         {"pair", "paired_mean", "unpaired_mean"})

    def test_task_stage_and_view_are_isolated(self):
        data = (samples("a", "A", [[1, 0], [0, 1]], task="first")
                + samples("f", "F", [[1, 0], [0, 1]], task="second")
                + samples("a", "A", [[1, 0], [0, 1]], task="first", stage="improve")
                + samples("f", "F", [[1, 0], [0, 1]], task="first", view="implementation"))
        scores, comparisons = compare_samples(data)
        self.assertEqual(len(scores), 4)
        self.assertEqual(len(comparisons), 2)
        for row in comparisons:
            self.assertIsNone(row["delta"])
            self.assertEqual(row["status"], "missing_baseline")

    def test_no_automatic_pairing_or_zero_imputation(self):
        data = (samples("a", "A", [[1, 0], [0, 1]], pair_id="p1")
                + samples("f", "F", [[1, 0], [0, 1]], pair_id="p2"))
        _, comparisons = compare_samples(data)
        pairs = [r for r in comparisons if r["kind"] == "pair"]
        self.assertEqual(len(pairs), 2)
        self.assertTrue(all(r["delta"] is None and r["status"] == "missing_pair" for r in pairs))
        mean = next(r for r in comparisons if r["kind"] == "paired_mean")
        self.assertEqual(mean["n_pairs"], 0)
        self.assertIsNone(mean["delta"])

    def test_duplicate_pair_or_inconsistent_run_is_rejected(self):
        for second in (samples("b", "A", [[1, 0], [0, 1]], pair_id="same"),
                       samples("a", "F", [[1, 0], [0, 1]], pair_id="same")):
            with self.assertRaises(ValueError):
                compare_samples(samples("a", "A", [[1, 0], [0, 1]], pair_id="same") + second)

    def test_missing_candidates_and_dimension_mismatch(self):
        scores, comparisons = compare_samples(samples("a", "A", [[1, 0]])
                                                + samples("f", "F", [[0, 1]]))
        self.assertEqual(scores, [])
        self.assertIsNone(comparisons[0]["delta"])
        self.assertIsNone(comparisons[0]["m"])
        self.assertEqual(comparisons[0]["status"], "insufficient_candidates")
        with self.assertRaisesRegex(ValueError, "dimensions"):
            compare_samples(samples("a", "A", [[1, 0], [0, 1]])
                            + samples("f", "F", [[1, 0, 0], [0, 1, 0]]))

    def test_seeded_subsampling_is_reproducible_and_order_independent(self):
        rng = np.random.default_rng(123)
        data = (samples("a", "A", rng.normal(size=(9, 5)).tolist())
                + samples("f", "F", rng.normal(size=(6, 5)).tolist()))
        first = compare_samples(data, repeats=5, seed=17)
        self.assertEqual(first, compare_samples(list(reversed(data)), repeats=5, seed=17))
        self.assertNotEqual(first, compare_samples(data, repeats=5, seed=18))
        self.assertEqual({r["m"] for r in first[0]}, {2, 3, 4, 5, 6})
        self.assertTrue(all(r["n_subsets"] <= 5 for r in first[0]))

    def test_empty_and_invalid_repeat_count(self):
        self.assertEqual(compare_samples([]), ([], []))
        with self.assertRaises(ValueError):
            compare_samples([], repeats=0)


if __name__ == "__main__":
    unittest.main()
