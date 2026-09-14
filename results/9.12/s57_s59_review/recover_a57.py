"""Read-only post-run scoring of saved A57 predictions; no training or run writes."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, "/workspace/MLEvolve")
from mlebench.registry import registry
from mlebench.utils import load_answers, read_csv
from utils.mlebench_patch import grading_metadata
from utils.submission_fusion_utils import EnsembleConfig, get_weights

root = Path("/workspace/MLEvolve/runs")
run = root / "20260912_081234_jubias-base-gpt56sol-s57"
task = "jigsaw-unintended-bias-in-toxicity-classification"
competition = registry.set_data_dir(Path("/workspace/data/mlebench")).get_competition(task)
answers = load_answers(competition.answers)
selection = json.loads((run / "logs/candidate_results/selection.json").read_text())["selected"]
cfg = EnsembleConfig()
frames, verified = [], []
for index, item in enumerate(selection):
    snap = item["snapshot"]
    path = run / "workspace/candidate_results/candidates" / snap["node_id"] / "snapshots" / snap["snapshot_id"] / "submission.csv"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == snap["files"]["submission.csv"]
    frame = read_csv(path)
    assert list(frame.columns) == ["id", "prediction"]
    assert len(frame) == 97320 and frame["id"].is_unique
    assert frame["prediction"].between(0, 1).all()
    if frames:
        assert frame["id"].equals(frames[0]["id"])
    frames.append(frame)
    verified.append({"node": snap["node_id"], "snapshot": snap["snapshot_id"],
                     "public_score": snap["metric"], "charged_seconds": item["charged_seconds"],
                     "submission_sha256": digest})
assert [v["public_score"] for v in verified] == sorted([v["public_score"] for v in verified], reverse=True)
scores = []
for k in cfg.ensemble_sizes:
    if k > len(frames):
        continue
    hours = sum(x["charged_seconds"] for x in verified[:k]) / 3600
    if hours > cfg.max_total_time_hours:
        break
    weights = get_weights([v["public_score"] for v in verified[:k]], [True] * k, cfg)
    frame = frames[0].copy()
    frame["prediction"] = sum(frames[i]["prediction"] * float(weights[i]) for i in range(k))
    scores.append({"k": k, "cum_hours": hours, "score": float(competition.grader(frame, answers)),
                   "weights": weights.tolist()})
f57 = root / "20260912_082449_jubias-anaf-gpt56sol-s57"
f57_score = float(competition.grader(read_csv(f57 / "workspace/top_solution/top1/submission.csv"), answers))
print(json.dumps({"run": run.name, "method": "post-hoc recovery from saved selection; same rank/metric weights and 9h cap",
                  "provenance": grading_metadata(task), "candidates": verified, "scores": scores,
                  "f57_top1_crosscheck": f57_score, "writes_to_source_run": False}))
