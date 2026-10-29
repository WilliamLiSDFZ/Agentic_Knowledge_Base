"""Exercise the local fetch script without Kubernetes or grading calls."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


FETCH_SCRIPT = Path.home() / "nautilus" / "fetch-run.sh"
COMMON = (
    "workspace/ensembles_csv/ensemble_1.csv", "workspace/best_submission/submission.csv",
    "workspace/best_solution/solution.py", "logs/best_solution.py", "logs/journal.json",
    "logs/config.yaml", "logs/MLEvolve.log", "logs/injected_knowledge.md",
    "logs/kb_snapshot.json", "logs/analogy/trace.json", "logs/candidate_results/node.json",
)
SNAPSHOTS = (
    "logs/draft_technique_rerank.json", "logs/draft_techniques.json",
    "logs/draft_techniques.md",
)
FULL = ("workspace/top_solution/node.py", "logs/MLEvolve.verbose.log")
EXECUTION = "logs/executions/node.json"
FAKE_KUBECTL = '''
import os, re, shutil, subprocess, sys
from pathlib import Path

args = sys.argv[1:]
if args[:1] == ["-n"]:
    args = args[2:]
def local_archive(value):
    return re.sub(r"/tmp/([^/\\s'\\\";]+\\.tgz|scores\\.csv)",
                  lambda match: str(Path(os.environ["FAKE_REMOTE_TMP"]) / match[1]), value)
if args[:2] == ["get", "pod"]:
    sys.exit(0)
if args[0] == "exec":
    if "python utils/grade_all.py" in args[-1]:
        if os.environ.get("FAKE_GRADE_MODE") == "grade_failure":
            sys.exit("grading failed")
        Path(local_archive("/tmp/scores.csv")).write_text("new scores\\n")
        sys.exit(0)
    command = [local_archive(arg) for arg in args[args.index("--") + 1:]]
    sys.exit(subprocess.run(command).returncode)
if args[0] == "cp":
    if args[1].endswith(".tgz") and os.environ.get("FAKE_GRADE_MODE") == "download_failure":
        sys.exit("archive copy failed")
    if args[1].endswith("/scores.csv") and os.environ.get("FAKE_GRADE_MODE") == "copy_failure":
        Path(args[2]).write_text("partial scores\\n")
        sys.exit("copy failed")
    shutil.copyfile(local_archive(args[1].split(":", 1)[1]), args[2])
    sys.exit(0)
raise SystemExit("unexpected kubectl command: " + repr(args))
'''


@unittest.skipUnless(FETCH_SCRIPT.is_file(), "local nautilus/fetch-run.sh is unavailable")
class FetchRunTests(unittest.TestCase):
    def test_six_experiments_and_legacy_run_in_default_and_full_modes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runs = root / "runs"
            fixtures = {}
            for seed in (42, 43, 44):
                for arm in ("base", "rerank"):
                    name = f"20261023_010000_jubias-draft-{arm}-s{seed}"
                    fixtures[name] = COMMON + (EXECUTION,) + FULL
                    if arm == "rerank":
                        fixtures[name] += SNAPSHOTS
            fixtures["20260901_010000_jubias-legacy"] = COMMON
            for name, paths in fixtures.items():
                for relative in paths:
                    path = runs / name / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(f"{name}/{relative}\n")

            remote_tmp = root / "remote_tmp"
            remote_tmp.mkdir()
            binary = root / "bin"
            binary.mkdir()
            kubectl = binary / "kubectl"
            kubectl.write_text(f"#!{sys.executable}\n" + FAKE_KUBECTL)
            kubectl.chmod(0o755)
            for full in (False, True):
                with self.subTest(full=full):
                    output = root / ("full" if full else "default")
                    env = dict(os.environ, PATH=f"{binary}{os.pathsep}{os.environ['PATH']}",
                               RUNS_DIR=str(runs), OUT_DIR=str(output), SKIP_GRADE="1",
                               POD="fake-pod", NS="fake-namespace", FAKE_REMOTE_TMP=str(remote_tmp))
                    command = ["bash", str(FETCH_SCRIPT), "--all", "jubias"]
                    if full:
                        command.append("--full")
                    result = subprocess.run(command, env=env, text=True, capture_output=True, timeout=60)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertNotIn("SKIP:", result.stdout)
                    for name, paths in fixtures.items():
                        expected = {p for p in paths if full or p not in FULL}
                        downloaded = {str(p.relative_to(output / name))
                                      for p in (output / name).rglob("*") if p.is_file()}
                        self.assertEqual(downloaded, expected, name)
                        for relative in expected:
                            self.assertEqual((output / name / relative).read_text(),
                                             f"{name}/{relative}\n")
                    self.assertEqual(list(remote_tmp.iterdir()), [])

    def test_grading_success_and_failures_preserve_valid_scores(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runs = root / "runs"
            log = runs / "20261023_010000_jubias-draft-base-s42" / "logs" / "MLEvolve.log"
            log.parent.mkdir(parents=True)
            log.write_text("run complete\n")
            remote_tmp = root / "remote_tmp"
            remote_tmp.mkdir()
            binary = root / "bin"
            binary.mkdir()
            kubectl = binary / "kubectl"
            kubectl.write_text(f"#!{sys.executable}\n" + FAKE_KUBECTL)
            kubectl.chmod(0o755)
            for mode in ("grade_failure", "copy_failure", "download_failure", "success"):
                with self.subTest(mode=mode):
                    output = root / mode
                    output.mkdir()
                    scores = output / "scores.csv"
                    scores.write_text("old scores\n")
                    env = dict(os.environ, PATH=f"{binary}{os.pathsep}{os.environ['PATH']}",
                               RUNS_DIR=str(runs), OUT_DIR=str(output), SKIP_GRADE="0",
                               POD="fake-pod", NS="fake-namespace", FAKE_REMOTE_TMP=str(remote_tmp),
                               FAKE_GRADE_MODE=mode)
                    result = subprocess.run(["bash", str(FETCH_SCRIPT), "jubias"], env=env,
                                            text=True, capture_output=True, timeout=60)
                    if mode == "success":
                        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                        self.assertIn("Done. Results", result.stdout)
                    else:
                        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                        self.assertNotIn("Done. Results", result.stdout)
                        self.assertNotIn("Next:", result.stdout)
                    expected_scores = "old scores\n" if mode in ("grade_failure", "copy_failure") else "new scores\n"
                    self.assertEqual(scores.read_text(), expected_scores)
                    self.assertEqual({p.name for p in output.iterdir() if p.is_file()}, {"scores.csv"})
                    self.assertEqual(list(remote_tmp.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
