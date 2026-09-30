"""Read complete candidates and explicit experiment identities, without model calls."""

import csv
import fnmatch
import hashlib
import json
from pathlib import Path

from .runtime import SOLUTION_VERSION, digest


def read_manifest(path):
    if path is None:
        return {}
    records = {}
    with Path(path).open(newline="") as stream:
        for row in csv.DictReader(stream):
            name = row.get("name") or row.get("run_id")
            if not name or name in records:
                raise ValueError("Manifest needs unique name (or run_id) rows")
            if any(not row.get(key, "").strip() for key in ("task", "arm", "batch")):
                raise ValueError(f"Manifest run {name} needs task, arm and batch")
            records[name] = row
    return records


def deduplicate(samples):
    seen = {}
    for row in samples:
        key = (row["task"], row["run_id"], row["candidate_id"])
        if key in seen:
            previous = seen[key]
            if ({k: v for k, v in previous.items() if k != "source_refs"} !=
                    {k: v for k, v in row.items() if k != "source_refs"}):
                raise ValueError(f"Conflicting duplicate candidate: {key}")
            previous["source_refs"] = sorted(set(previous["source_refs"] + row["source_refs"]))
        else:
            seen[key] = row.copy()
    return [seen[key] for key in sorted(seen)]


def load_runs(root, manifest=None, pattern="*"):
    root = Path(root)
    metadata = read_manifest(manifest)
    names = sorted(metadata) if manifest else sorted(p.name for p in root.iterdir() if p.is_dir())
    samples, issues = [], []
    for name in names:
        if not fnmatch.fnmatch(name, pattern):
            continue
        path, meta = root / name, dict(metadata.get(name, {}))
        if not meta.get("task") or not meta.get("arm"):
            from analyze_runs import Run, parse_config
            run = Run()
            parse_config(run, path / "logs/config.yaml")
            meta.update(task=run.task, arm=run.arm)
        common = dict(task=meta.get("task", ""), arm=meta.get("arm", ""), run_id=name,
                      batch=meta.get("batch") or "unassigned", pair_id=meta.get("pair_id") or "")
        if meta.get("verdict", "ok") not in ("", "ok") or meta.get("exclude_reason"):
            issues.append(common | dict(issue="excluded_manifest", reason=meta.get("exclude_reason") or meta["verdict"]))
            continue
        if not common["task"] or not common["arm"]:
            issues.append(common | dict(issue="missing_task_or_arm"))
            continue
        journal = path / "logs/journal.json"
        try:
            data = json.loads(journal.read_text())
            nodes = data.get("nodes", []) if isinstance(data, dict) else data
            if not isinstance(nodes, list) or any(not isinstance(n, dict) for n in nodes):
                raise ValueError("journal nodes must be a list of objects")
        except (OSError, ValueError) as error:
            issues.append(common | dict(issue=f"journal_unavailable:{type(error).__name__}"))
            continue
        count, candidate_ids = 0, set()
        for index, node in enumerate(nodes):
            if node.get("stage") == "root":
                continue
            count += 1
            candidate_id = str(node.get("id") or f"node-{index}")
            if candidate_id in candidate_ids:
                raise ValueError(f"Duplicate candidate ID in {journal}: {candidate_id}")
            candidate_ids.add(candidate_id)
            code = node.get("code") or ""
            if not isinstance(code, str):
                code = ""
            samples.append(common | dict(
                candidate_id=candidate_id, stage="solution", view="solution",
                original_stage=node.get("stage") or "unknown", status=node.get("execution_status") or "unknown",
                is_valid=node.get("is_valid"), is_buggy=node.get("is_buggy"), artifact_status=node.get("artifact_status"),
                source="\n".join(f"SOURCE:{i}: {line}" for i, line in enumerate(code.splitlines(), 1)), text="",
                source_hash=hashlib.sha256(code.encode()).hexdigest(), source_refs=[f"{journal}#nodes[{index}]"],
                representation_version=SOLUTION_VERSION, extraction_status="pending" if code.strip() else "missing_source"))
        if not count:
            issues.append(common | dict(issue="no_candidates"))
    return deduplicate(samples), issues


def load_samples(paths, manifest=None):
    """Combine saved representations; a manifest can explicitly assign legacy run identities."""
    metadata, samples, issues = read_manifest(manifest), [], []
    seen_runs = set()
    for path in paths:
        path = Path(path)
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"{path}:{number}: sample must be an object")
            for key in ("task", "run_id", "arm", "candidate_id"):
                if not isinstance(row.get(key), str) or not row[key].strip():
                    raise ValueError(f"{path}:{number}: missing string {key}")
            card = row.get("mechanism_card")
            if (row.get("stage") != "solution" or row.get("view") != "solution"
                    or row.get("representation_version") != SOLUTION_VERSION
                    or "assessment_status" in row or "change_packet" in row
                    or (isinstance(card, dict) and ("change" in card or "status" in card))):
                raise ValueError("Only solution-v1 inputs are supported; re-extract legacy/diff samples from source")
            name = row["run_id"]
            if manifest:
                if name not in metadata:
                    issues.append(dict(run_id=name, task=row["task"], arm=row["arm"], issue="excluded_manifest"))
                    continue
                meta = metadata[name]
                if meta.get("verdict", "ok") not in ("", "ok") or meta.get("exclude_reason"):
                    issues.append(dict(run_id=name, task=row["task"], arm=row["arm"], issue="excluded_manifest"))
                    continue
                for key in ("task", "arm", "batch", "pair_id"):
                    if key == "pair_id" and key not in meta:
                        continue
                    value = meta.get(key) or ("unassigned" if key == "batch" else "")
                    if row.get(key) not in (None, "", "unassigned", value):
                        raise ValueError(f"Manifest conflicts with {key} for run {name}")
                    row[key] = value
            seen_runs.add(name)
            if not row.get("batch") or row["batch"] == "unassigned":
                raise ValueError(f"Run {name} needs batch metadata; pass --manifest when importing old samples")
            row.setdefault("pair_id", "")
            row.setdefault("original_stage", "unknown")
            row.setdefault("text", "")
            row.setdefault("source_refs", [f"{path}:{number}"])
            if not isinstance(row["text"], str):
                raise ValueError("Solution text must be a string")
            if not isinstance(row["source_refs"], list) or any(not isinstance(ref, str) for ref in row["source_refs"]):
                raise ValueError("source_refs must be a list of strings")
            if "embedding" in row and (not isinstance(row.get("embedding_model"), str)
                                       or not row["embedding_model"].strip()):
                raise ValueError("Precomputed vectors need embedding_model")
            row.setdefault("source_hash", digest([row["text"], row.get("embedding")]))
            if row.get("extraction_status") != "excluded":
                if row["text"].strip() or "embedding" in row:
                    row["extraction_status"] = "ok"
                    row.pop("error", None)
                elif row.get("extraction_status") != "error":
                    row["extraction_status"] = "missing_source"
            samples.append(row)
    for name, meta in metadata.items():
        if name not in seen_runs and meta.get("verdict", "ok") in ("", "ok") and not meta.get("exclude_reason"):
            issues.append(dict(run_id=name, task=meta["task"], arm=meta["arm"], batch=meta["batch"],
                               pair_id=meta.get("pair_id", ""), issue="samples_unavailable"))
    # One run-level issue is sufficient even when many unlisted candidates were supplied.
    issues = list({json.dumps(row, sort_keys=True): row for row in issues}.values())
    return deduplicate(samples), issues


def validate_samples(samples):
    runs, pairs = {}, {}
    for row in samples:
        for key in ("batch", "pair_id"):
            if not isinstance(row.get(key), str) or (key == "batch" and not row[key].strip()):
                raise ValueError(f"Invalid {key} in run {row['run_id']}")
        identity = (row["batch"], row["arm"], row["pair_id"])
        run_key = (row["task"], row["run_id"])
        if run_key in runs and runs[run_key] != identity:
            raise ValueError(f"Inconsistent run metadata: {run_key}")
        runs[run_key] = identity
        if row["pair_id"]:
            pair_key = (row["task"], row["batch"], row["pair_id"], row["arm"])
            if pair_key in pairs and pairs[pair_key] != row["run_id"]:
                raise ValueError(f"Multiple runs for task/batch/pair_id/arm: {pair_key}")
            pairs[pair_key] = row["run_id"]
    for field in ("summary_model", "summary_prompt_sha256"):
        identities = {row[field] for row in samples if row.get(field) and row.get("extraction_status") == "ok"}
        if len(identities) > 1:
            raise ValueError(f"Mixed {field}; use consistent solution representations")
