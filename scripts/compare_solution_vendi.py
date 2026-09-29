#!/usr/bin/env python3
"""Compare complete MLEvolve solutions, using the autoresearch summary convention."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

from compare_vendi import (digest, embed_samples, load_jsonl, load_runs, plot_results,
                           validate_run_metadata, write_csv, write_json)
from vendi_metrics import compare_samples, vendi_score
from vendi_solutions import SOLUTION_PROMPT, SOLUTION_VERSION, SolutionSummarizer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_REVISION = "1110a243fdf4706b3f48f1d95db1a4f5529b4d41"


def load_solution_runs(root, inventory=None, pattern="*", include_invalid=False):
    return load_runs(root, inventory, pattern, [], include_invalid, whole_solutions=True)


def load_solution_jsonl(path, reembed=False):
    rows = load_jsonl(path)
    for row in rows:
        card = row.get("mechanism_card")
        if (row["stage"] != "solution" or row["view"] != "solution"
                or row.get("representation_version") != SOLUTION_VERSION
                or "assessment_status" in row or "change_packet" in row
                or (isinstance(card, dict) and ("change" in card or "status" in card))):
            raise ValueError("Only solution-v1 samples are supported; re-extract legacy/diff inputs from source")
        if row.get("extraction_status") == "excluded":
            continue
        if reembed and "embedding" in row and not row["text"].strip():
            raise ValueError("--reembed requires summary text for every existing embedding")
        if reembed and row["text"].strip():
            for key in ("embedding", "embedding_model", "embedding_tokens"):
                row.pop(key, None)
        if row["text"].strip() or "embedding" in row:
            row["extraction_status"] = "ok"
            row.pop("error", None)
        elif row.get("extraction_status") != "error":
            row["extraction_status"] = "missing_source"
    return rows


def coverage_rows(samples, issues):
    groups = defaultdict(list)
    for row in samples:
        groups[(row["task"], row["run_id"], row["arm"])].append(row)
    result = []
    for (task, run_id, arm), rows in sorted(groups.items()):
        counts = Counter(row["extraction_status"] for row in rows)
        result.append(dict(task=task, run_id=run_id, arm=arm, pair_id=rows[0].get("pair_id", ""),
                           stage="solution", view="solution", n_candidates=len(rows),
                           n_available=counts["ok"], n_missing=counts["missing_source"],
                           n_errors=counts["error"], n_pending=counts["pending"], n_excluded=counts["excluded"],
                           n_valid=sum(row.get("is_valid") is True for row in rows),
                           n_failed=sum(row.get("is_buggy") is True or row.get("status") == "failed" for row in rows),
                           stages=json.dumps(Counter(row.get("original_stage", "unknown") for row in rows), sort_keys=True),
                           issue="" if counts["ok"] >= 2 and counts["ok"] + counts["excluded"] == len(rows)
                           else "incomplete_or_too_few_candidates"))
    return result + issues


def full_solution_scores(ready):
    groups = defaultdict(list)
    for row in ready:
        groups[(row["task"], row["run_id"])].append(row)
    return [dict(task=task, run_id=run_id, arm=rows[0]["arm"], pair_id=rows[0].get("pair_id", ""),
                 n_total=len(rows), vendi=vendi_score([row["embedding"] for row in rows]),
                 status="descriptive_unmatched_counts")
            for (task, run_id), rows in sorted(groups.items())]


def write_samples(path, samples):
    with path.open("w") as stream:
        for row in samples:
            stream.write(json.dumps({k: v for k, v in row.items() if k != "source"},
                                    ensure_ascii=False, allow_nan=False) + "\n")


def write_report(out, samples, ready, coverage, issues, prefix=""):
    lines = ["# Complete solution Vendi", "",
             f"Available representations: {len(ready)}/{len(samples)}. Run-level issues: {len(issues)}.", "",
             "Each non-root candidate is one complete solution, including draft, improve, debug and fusion. "
             "Only its neutral source-grounded summary is embedded. Parent differences, analogy reports, "
             "arm labels and scores are not summary inputs. Identical solutions in different candidates "
             "retain their frequency; debug retries and related descendants are correlated observations.", "",
             "Within each task, runs with at least two available candidates form a fixed cohort with "
             "shared m=2..minimum candidate count. Compare run_scores.csv and comparisons.csv at matched m. "
             "full_run_scores.csv uses all available candidates and unequal counts are descriptive only; "
             "a singleton scores 1 but cannot enter matched comparisons. Keep different experiment versions, "
             "models, draft counts and budgets in separate invocations; budget is not automatically matched.", "",
             "Failed/pending training candidates are included unless --valid-only is used (is_valid must be true). "
             "Missing source and extraction/embedding failures are not zero scores. Check coverage before "
             "interpreting differences. Source references establish provenance, not successful execution.", "",
             "Vendi measures diversity, not scientific novelty or task performance. Independent runs are the "
             "experimental repeats; candidate-subset bands are NOT effect confidence intervals. Pairing requires "
             "explicit inventory pair_id, never inferred seeds. The paper embeds solution titles; our complete "
             "code summaries follow autoresearch's adaptation and are not a numerical reproduction of the paper.", "",
             "## Coverage", "", "| Run | Arm | Candidates | Available | Missing | Errors | Excluded | Stages |",
             "|---|---|---:|---:|---:|---:|---:|---|"]
    for row in coverage:
        if "n_candidates" in row:
            values = [row[k] for k in ("run_id", "arm", "n_candidates", "n_available", "n_missing",
                                      "n_errors", "n_excluded", "stages")]
            lines.append("| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in values) + " |")
    lines += ["", "See solution_cards.csv for titles, summaries and evidence; samples.jsonl for reusable vectors; "
              "coverage.csv for exclusions; manifest.json for measurement settings and code identities.", ""]
    report = "\n".join(lines)
    for name in ("run_scores.csv", "comparisons.csv", "full_run_scores.csv", "solution_cards.csv",
                 "samples.jsonl", "coverage.csv", "manifest.json"):
        # Token boundaries avoid replacing run_scores inside full_run_scores.
        report = re.sub(r"(?<![\w])" + re.escape(name), prefix + name, report)
    (out / f"{prefix}REPORT.md").write_text(report)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--runs", type=Path)
    source.add_argument("--input", type=Path, help="Previously exported solution-v1 samples.jsonl")
    parser.add_argument("--inventory", type=Path, help="CSV allow-list; optional explicit pair_id")
    parser.add_argument("--run-glob", default="*")
    parser.add_argument("--arms", nargs="+")
    parser.add_argument("--baseline", default="A")
    parser.add_argument("--valid-only", action="store_true")
    parser.add_argument("--include-invalid", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--prefix", default="", help="Batch filename prefix within --out (e.g. s61_s62)")
    parser.add_argument("--cache", type=Path, default=Path(__file__).resolve().parents[1] / "cache/vendi_solutions")
    parser.add_argument("--summary-model", help="Defaults to scripts/llm.py LLM_MODEL")
    parser.add_argument("--summary-api", choices=["chat", "responses"], default="chat")
    parser.add_argument("--embedding-model", default=EMBEDDING_MODEL)
    parser.add_argument("--embedding-revision")
    parser.add_argument("--embedding-max-length", type=int, default=512)
    parser.add_argument("--reembed", action="store_true", help="With --input: re-embed saved summaries without LLM calls")
    parser.add_argument("--repeats", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true", help="Read-only inventory; no clients, downloads or output files")
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args(argv)
    if args.prefix and not re.fullmatch(r"[A-Za-z0-9_-]+", args.prefix):
        parser.error("--prefix may contain only letters, digits, underscores and hyphens")
    prefix = args.prefix + "_" if args.prefix else ""
    if args.repeats < 1 or args.embedding_max_length < 8:
        parser.error("--repeats must be positive and --embedding-max-length must be >=8")
    if args.reembed and not args.input:
        parser.error("--reembed requires --input")
    if args.inventory and args.input:
        parser.error("--inventory is for --runs")
    if args.embedding_revision is None and args.embedding_model == EMBEDDING_MODEL:
        args.embedding_revision = EMBEDDING_REVISION
    if args.runs:
        samples, issues = load_solution_runs(args.runs, args.inventory, args.run_glob, args.include_invalid)
    else:
        samples, issues = load_solution_jsonl(args.input, args.reembed), []
    samples = [row for row in samples if not args.arms or row["arm"] in args.arms]
    issues = [row for row in issues if not args.arms or not row.get("arm") or row["arm"] in args.arms]
    validate_run_metadata(samples)
    if args.valid_only:
        for row in samples:
            if row.get("is_valid") is not True:
                row.update(extraction_status="excluded", error="excluded_valid_only")
    if args.dry_run:
        print(json.dumps(dict(samples=len(samples), runs=len({row["run_id"] for row in samples}),
                              stages=dict(Counter(row.get("original_stage", "unknown") for row in samples)),
                              statuses=dict(Counter(row["extraction_status"] for row in samples)),
                              coverage=coverage_rows(samples, issues)), indent=2))
        return 0
    manifest_path = args.out / f"{prefix}manifest.json"
    if manifest_path.exists() and json.loads(manifest_path.read_text()).get("representation_version") != SOLUTION_VERSION:
        raise ValueError("Use a separate output directory for complete solution results")
    args.out.mkdir(parents=True, exist_ok=True)
    summarizer = None
    for index, row in enumerate(samples, 1):
        if not args.runs or row["extraction_status"] != "pending":
            continue
        if summarizer is None:
            summarizer = SolutionSummarizer(args.cache, args.summary_model, args.summary_api)
        print(f"[{index}/{len(samples)}] {row['run_id']} {row['candidate_id']} solution", flush=True)
        try:
            card, chunks = summarizer.summarize_solution(row["source"])
            row.update(text=card["summary"], solution_title=card["title"], mechanism_card=card,
                       source_chunks=chunks, extraction_status="ok", summary_model=summarizer.model,
                       summary_prompt_sha256=digest(SOLUTION_PROMPT))
        except Exception as error:
            row.update(extraction_status="error", error=f"summary_failed:{type(error).__name__}")
    # Keep full summaries recoverable even if loading the embedding model fails.
    if args.runs:
        write_samples(args.out / f"{prefix}samples.jsonl", samples)
    precomputed = any("embedding" in row for row in samples if row["extraction_status"] == "ok")
    identity = embed_samples(samples, args.cache, args.embedding_model, args.embedding_revision,
                             None if precomputed else args.embedding_max_length)
    ready = [row for row in samples if row["extraction_status"] == "ok"]
    scores, comparisons = compare_samples(ready, baseline=args.baseline, repeats=args.repeats, seed=args.seed)
    coverage = coverage_rows(samples, issues)
    cards = [dict(run_id=row["run_id"], candidate_id=row["candidate_id"], arm=row["arm"],
                  original_stage=row.get("original_stage", "unknown"), source_sha256=row["source_hash"],
                  is_valid=row.get("is_valid"), status=row["extraction_status"],
                  title=row.get("solution_title", ""), summary=row["text"],
                  evidence=json.dumps(row.get("mechanism_card", {}).get("evidence", [])),
                  error=row.get("error", "")) for row in samples]
    for name, rows, fallback in [
        ("solution_cards", cards, ["run_id", "candidate_id", "title", "summary"]),
        ("full_run_scores", full_solution_scores(ready), ["run_id", "n_total", "vendi"]),
        ("run_scores", scores, ["run_id", "m", "vendi"]),
        ("comparisons", comparisons, ["task", "arm", "baseline", "m", "delta", "status"]),
        ("coverage", coverage, ["run_id", "issue"]),
    ]:
        write_csv(args.out / f"{prefix}{name}.csv", rows, fallback)
    write_samples(args.out / f"{prefix}samples.jsonl", samples)
    source_files = [Path(__file__).with_name(name) for name in
                    ("compare_solution_vendi.py", "compare_vendi.py", "vendi_solutions.py", "vendi_metrics.py")]
    write_json(manifest_path, dict(
        representation_version=SOLUTION_VERSION, args={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        embedding=identity, summary_model=summarizer.model if summarizer else None,
        summary_prompt_sha256=digest(SOLUTION_PROMPT), summary_api_calls=summarizer.calls if summarizer else 0,
        source_hashes={path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in source_files},
        samples=len(samples), available=len(ready),
        comparison="q=1 cosine Vendi; complete solutions; matched counts within runs; descriptive"))
    write_report(args.out, samples, ready, coverage, issues, prefix)
    for path in [*args.out.glob(f"{prefix}vendi_[0-9][0-9].png"), args.out / f"{prefix}paired_deltas.png"]:
        path.unlink(missing_ok=True)
    if not args.no_plots:
        plot_results(args.out, scores, comparisons, coverage, prefix=prefix)
    print(f"Saved {len(scores)} run-score rows to {args.out / (prefix + 'run_scores.csv')}; available {len(ready)}/{len(samples)}")
    failures = Counter(row.get("error", row["extraction_status"]) for row in samples
                       if row["extraction_status"] not in ("ok", "excluded"))
    failures.update(row["issue"] for row in issues if row["issue"] != "excluded_inventory_verdict")
    if failures:
        print(f"INCOMPLETE coverage (inspect {prefix}coverage.csv): " + ", ".join(f"{k}={v}" for k, v in failures.items()))
    return 2 if failures or not scores else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        raise SystemExit(f"compare_solution_vendi: {exc}")
