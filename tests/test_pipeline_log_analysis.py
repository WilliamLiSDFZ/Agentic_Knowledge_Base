"""Recoverable pipeline failures must not invalidate a completed experiment."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from analyze_runs import Run, apply_rules, finalise_usable, parse_log


class PipelineLogAnalysisTests(unittest.TestCase):
    def parse(self, text, completed=True):
        run = Run(n_nodes=4, n_valid=3, n_ensembles=int(completed), wrapper_completed=completed)
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "MLEvolve.log"
            log.write_text(text)
            parse_log(run, log)
        finalise_usable(run)
        apply_rules(run, {})
        return run

    def test_recovered_pipeline_errors_are_counted_without_excluding_run(self):
        run = self.parse(
            "[2026-10-23 00:00:00,000] INFO: Starting run\n"
            "[2026-10-23 01:00:00,000] ERROR: Initial draft 2 generation failed\n"
            "Traceback (most recent call last):\nValueError: failed generation\n"
            "[2026-10-23 02:00:00,000] ERROR: Search task failed\n"
            "Traceback (most recent call last):\nValueError: failed candidate\n"
            "    logger.exception('Search task failed')\n"
            "[2026-10-23 12:00:00,000] INFO: Progress: 4/4 completed\n")
        self.assertEqual((run.n_generation_failures, run.n_search_failures), (1, 1))
        self.assertEqual(run.n_real_crashes, 0)
        self.assertEqual(run.verdict, "ok")
        self.assertIn("generation_failures", run.flags)
        self.assertIn("search_failures", run.flags)
        self.assertEqual((run.n_nodes, run.n_valid), (4, 3))

    def test_recoverable_message_does_not_hide_an_early_termination(self):
        run = self.parse(
            "[2026-10-23 00:00:00,000] INFO: Starting run\n"
            "[2026-10-23 00:05:00,000] ERROR: Search task failed\n", completed=False)
        self.assertEqual(run.verdict, "invalid")
        self.assertIn("insufficient_runtime", run.reasons)
        self.assertIn("no_submission", run.reasons)

    def test_legacy_exception_rule_is_preserved(self):
        run = self.parse(
            "[2026-10-23 00:00:00,000] INFO: Starting run\n"
            "[2026-10-23 02:00:00,000] ERROR: Exception during task execution: failure\n"
            "Traceback (most recent call last):\nValueError: failure\n"
            "[2026-10-23 12:00:00,000] INFO: Last log\n")
        self.assertEqual(run.n_real_crashes, 1)
        self.assertIn("crashed", run.reasons)


if __name__ == "__main__":
    unittest.main()
