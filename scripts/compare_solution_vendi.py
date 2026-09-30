#!/usr/bin/env python3
"""Analyze complete-solution Vendi for all selected runs in one invocation."""

import argparse
from collections import Counter, defaultdict
import fnmatch
import hashlib
import json
from pathlib import Path

from vendi.metrics import full_solution_scores, score_samples
from vendi.reader import load_runs, load_samples, validate_samples
from vendi.reporting import plot_results, write_plot_data
from vendi.runtime import (EMBEDDING_MAX_LENGTH, EMBEDDING_MODEL, EMBEDDING_REVISION,
                           SOLUTION_PROMPT, SOLUTION_VERSION, SolutionSummarizer,
                           digest, embed_samples, prepare_reembedding, write_csv, write_json)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "scripts/vendi/jigsaw_runs.csv"


def coverage_rows(samples, issues):
    groups = defaultdict(list)
    for row in samples:
        groups[(row["task"], row["batch"], row["run_id"], row["arm"])].append(row)
    result = []
    for (task, batch, run_id, arm), rows in sorted(groups.items()):
        counts = Counter(row["extraction_status"] for row in rows)
        result.append(dict(task=task, batch=batch, run_id=run_id, arm=arm, pair_id=rows[0]["pair_id"],
                           n_candidates=len(rows), n_available=counts["ok"], n_missing=counts["missing_source"],
                           n_errors=counts["error"], n_pending=counts["pending"], n_excluded=counts["excluded"],
                           n_valid=sum(row.get("is_valid") is True for row in rows),
                           n_failed=sum(row.get("is_buggy") is True or row.get("status") == "failed" for row in rows),
                           stages=json.dumps(Counter(row["original_stage"] for row in rows), sort_keys=True),
                           issue="" if counts["ok"] >= 2 and counts["ok"] + counts["excluded"] == len(rows)
                           else "incomplete_or_too_few_candidates"))
    return result + issues


def write_samples(path, samples):
    temporary = path.with_suffix(".jsonl.tmp")
    with temporary.open("w") as stream:
        for row in samples:
            stream.write(json.dumps({k: v for k, v in row.items() if k != "source"},
                                    ensure_ascii=False, allow_nan=False) + "\n")
    temporary.replace(path)


def write_report(out, samples, ready, coverage, scores, comparisons):
    endpoints = [r for r in comparisons if r["kind"] == "pair" and r.get("delta") is not None
                 and r["m"] == r["task_common_m"]]
    lines = ["# Complete solution Vendi", "",
             f"Available representations: {len(ready)}/{len(samples)}; "
             f"scored runs: {len({(r['task'], r['run_id']) for r in scores})}; "
             f"complete explicit pairs: {len(endpoints)}.", "",
             "Each non-root candidate contributes its complete code's neutral summary, including draft, "
             "improve, debug and fusion. Identical implementations in distinct candidates retain their frequency. "
             "Summary text alone is embedded; titles, arm labels, analogy reports, parents and scores are excluded.", "",
             "Runs with at least two available candidates use a shared m=2..minimum count across ALL batches "
             "within each task. Vendi is calculated inside each run, never by pooling candidates across runs. "
             "Batch identities remain separate: there is no cross-version overall effect. Explicit pairs come "
             "from the run manifest, not inferred seeds. Job pairing does not match realized hardware or search paths.", "",
             "vendi.csv contains every run curve; effect.csv contains within-batch pair differences (or descriptive "
             "unpaired means when no complete pair exists); paired.csv contains explicit A/F endpoints at the "
             "task's largest shared m. Each has a PNG/PDF figure unless --no-plots is used. comparisons.csv also retains unmatched pairs "
             "and batch means. full_run_scores.csv uses all available candidates and is descriptive when counts differ.", "",
             "Vendi measures diversity, not novelty or task performance. Runs are experimental repeats; related "
             "candidates are correlated. Candidate-subset bands in run_scores.csv are NOT confidence intervals "
             "for an arm effect. Failed training candidates remain included unless --valid-only is used. Missing "
             "sources, failed representations and excluded records are visible in coverage.csv, never zero scores.", "",
             "## Coverage", "", "| Batch | Run | Arm | Candidates | Available | Missing | Errors | Excluded | Issue |",
             "|---|---|---|---:|---:|---:|---:|---:|---|"]
    for row in coverage:
        keys = ("batch", "run_id", "arm", "n_candidates", "n_available", "n_missing", "n_errors", "n_excluded", "issue")
        lines.append("| " + " | ".join(str(row.get(k, "")).replace("|", "\\|").replace("\n", " ") for k in keys) + " |")
    lines += ["", "See solution_cards.csv for summaries and evidence, samples.jsonl for reusable vectors, "
              "and manifest.json for measurement settings, input/code hashes and pairing metadata.", ""]
    (out / "REPORT.md").write_text("\n".join(lines))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--runs", type=Path, help="Fetched runs; default ~/nautilus/results")
    source.add_argument("--input", type=Path, nargs="+", help="One or more saved solution-v1 samples.jsonl files")
    parser.add_argument("--manifest", type=Path, help="Run allow-list with task, arm, batch, pair_id; raw runs default to bundled Jigsaw list")
    parser.add_argument("--run-glob", default="*")
    parser.add_argument("--arms", nargs="+")
    parser.add_argument("--baseline", default="A")
    parser.add_argument("--valid-only", action="store_true")
    parser.add_argument("--out", type=Path, default=ROOT / "results/vendi_solutions")
    parser.add_argument("--cache", type=Path, default=ROOT / "cache/vendi_solutions")
    parser.add_argument("--summary-model", help="Defaults to scripts/llm.py LLM_MODEL")
    parser.add_argument("--summary-api", choices=["chat", "responses"], default="chat")
    parser.add_argument("--embedding-model", default=EMBEDDING_MODEL)
    parser.add_argument("--embedding-revision")
    parser.add_argument("--embedding-max-length", type=int, default=EMBEDDING_MAX_LENGTH)
    parser.add_argument("--reembed", action="store_true", help="Re-embed saved summaries without LLM calls")
    parser.add_argument("--repeats", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true", help="Check inputs without clients, downloads or writes")
    parser.add_argument("--no-plots", action="store_true", help="Export all tables, skip PNG/PDF rendering")
    args = parser.parse_args(argv)
    if args.repeats < 1 or args.embedding_max_length < 8:
        parser.error("--repeats must be positive and --embedding-max-length must be >=8")
    if args.reembed and not args.input:
        parser.error("--reembed requires --input")
    if args.embedding_revision is None and args.embedding_model == EMBEDDING_MODEL:
        args.embedding_revision = EMBEDDING_REVISION
    if not args.input:
        args.runs = args.runs or Path.home() / "nautilus/results"
        args.manifest = args.manifest or DEFAULT_MANIFEST
        samples, issues = load_runs(args.runs, args.manifest, args.run_glob)
    else:
        samples, issues = load_samples(args.input, args.manifest)
    def selected(row):
        return fnmatch.fnmatch(row["run_id"], args.run_glob) and (not args.arms or row.get("arm") in args.arms)
    samples, issues = [r for r in samples if selected(r)], [r for r in issues if selected(r)]
    validate_samples(samples)
    if args.valid_only:
        for row in samples:
            if row.get("is_valid") is not True:
                row.update(extraction_status="excluded", error="excluded_valid_only")
    if args.reembed:
        prepare_reembedding(samples)
    if args.dry_run:
        print(json.dumps(dict(samples=len(samples), runs=len({r["run_id"] for r in samples}),
                              statuses=dict(Counter(r["extraction_status"] for r in samples)),
                              coverage=coverage_rows(samples, issues)), indent=2))
        return 0
    if args.runs and (args.out.resolve() == args.runs.resolve() or args.runs.resolve() in args.out.resolve().parents):
        raise ValueError("Output must be outside the raw runs directory")
    manifest_path = args.out / "manifest.json"
    if manifest_path.exists() and json.loads(manifest_path.read_text()).get("representation_version") != SOLUTION_VERSION:
        raise ValueError("Use a separate output directory for complete solution results")
    input_files = (args.input or []) + ([args.manifest] if args.manifest else [])
    input_hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in input_files}
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
    if args.runs:
        write_samples(args.out / "samples.jsonl", samples)
    validate_samples(samples)
    precomputed = any("embedding" in r for r in samples if r["extraction_status"] == "ok")
    identity = embed_samples(samples, args.cache, args.embedding_model, args.embedding_revision,
                             None if precomputed else args.embedding_max_length)
    ready = [r for r in samples if r["extraction_status"] == "ok"]
    scores, comparisons = score_samples(samples, args.baseline, args.repeats, args.seed)
    coverage = coverage_rows(samples, issues)
    cards = [dict(task=r["task"], batch=r["batch"], run_id=r["run_id"], candidate_id=r["candidate_id"], arm=r["arm"],
                  pair_id=r["pair_id"], original_stage=r["original_stage"], source_sha256=r["source_hash"],
                  is_valid=r.get("is_valid"), status=r["extraction_status"], title=r.get("solution_title", ""),
                  summary=r["text"], evidence=json.dumps(r.get("mechanism_card", {}).get("evidence", [])),
                  source_refs=json.dumps(r["source_refs"]), error=r.get("error", "")) for r in samples]
    for name, rows, fallback in [
        ("solution_cards", cards, ["run_id", "candidate_id", "title", "summary"]),
        ("full_run_scores", full_solution_scores(samples), ["run_id", "n_total", "vendi"]),
        ("run_scores", scores, ["run_id", "m", "vendi"]),
        ("comparisons", comparisons, ["task", "batch", "arm", "baseline", "m", "delta", "status"]),
        ("coverage", coverage, ["run_id", "issue"]),
    ]:
        write_csv(args.out / f"{name}.csv", rows, fallback)
    write_samples(args.out / "samples.jsonl", samples)
    if args.no_plots:
        write_plot_data(args.out, scores, comparisons)
        artifacts = [f"{name}.csv" for name in ("vendi", "effect", "paired")]
        for name in ("vendi", "effect", "paired"):
            for extension in ("png", "pdf"):
                (args.out / f"{name}.{extension}").unlink(missing_ok=True)
    else:
        artifacts = plot_results(args.out, scores, comparisons)
    source_files = [Path(__file__), *sorted((ROOT / "scripts/vendi").glob("*.py"))]
    write_json(manifest_path, dict(
        representation_version=SOLUTION_VERSION, args=vars(args) | dict(
            **{k: str(v) for k, v in vars(args).items() if isinstance(v, Path)},
            input=[str(p) for p in args.input] if args.input else None),
        embedding=identity, summary_models=sorted({r["summary_model"] for r in ready if r.get("summary_model")}),
        summary_prompt_sha256=next(iter({r["summary_prompt_sha256"] for r in ready if r.get("summary_prompt_sha256")}), None),
        configured_summary_prompt_sha256=digest(SOLUTION_PROMPT), summary_api_calls=summarizer.calls if summarizer else 0,
        source_hashes={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
        input_hashes=input_hashes, samples=len(samples), available=len(ready), plots=artifacts,
        run_metadata=[{k: r[k] for k in ("task", "batch", "run_id", "arm", "pair_id")} for r in coverage if "n_candidates" in r],
        comparison="q=1 cosine Vendi; complete solutions; common m within task; effects within batch; descriptive"))
    write_report(args.out, samples, ready, coverage, scores, comparisons)
    print(f"Saved {len(scores)} run-score rows to {args.out}; available {len(ready)}/{len(samples)}")
    failures = Counter(r.get("error", r["extraction_status"]) for r in samples if r["extraction_status"] not in ("ok", "excluded"))
    failures.update(r["issue"] for r in issues if r["issue"] != "excluded_manifest")
    if failures:
        print("INCOMPLETE coverage (inspect coverage.csv): " + ", ".join(f"{k}={v}" for k, v in failures.items()))
    return 2 if failures or not scores else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        raise SystemExit(f"compare_solution_vendi: {exc}")
