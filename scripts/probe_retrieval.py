"""Probe the abstract index: what would a given task actually retrieve?

Runs the retrieval stage alone — no LLM calls, no extraction, no 12-hour job — so retrieval
changes can be validated in seconds instead of a full run.

Compares the two fixes that matter on this corpus:
  --center   mean-center the dense vectors (ML-paper abstracts are highly anisotropic: every
             vector shares a big "this is an ML paper" component that swamps topic signal)
  --focus    query = the task-describing sections only, dropping submission format / file
             lists / citation, which dilute both the dense vector and BM25 term statistics

Usage:
    python scripts/probe_retrieval.py --task /workspace/data/mlevolve/openadmet/description.md
    python scripts/probe_retrieval.py --task ... --all        # 4-way comparison
    python scripts/probe_retrieval.py --task ... --keywords molecul,smiles,admet,drug,chem

`spread` = score(top1) - score(topK). A flat spread means the scorer is NOT discriminating,
which is the symptom this script exists to catch.
"""
import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

QUERY_MAX_CHARS = 2500
DEFAULT_KEYWORDS = "molecul,smiles,admet,drug,chem,compound,protein,ligand,qsar,graph neural"

# Mirrors MLEvolve engine/coldstart/ondemand.py::_DISTILL_PROMPT
DISTILL_PROMPT = """Below is a machine-learning competition description. Write a single
compact paragraph (50-80 words) that will be used as a SEARCH QUERY to find relevant
research papers.

Describe only the machine-learning problem:
- input data type and scale
- task type (e.g. multi-class classification, multi-task regression)
- evaluation metric
- modelling techniques and data characteristics likely to matter

Exclude everything else: prizes, timelines, eligibility, submission file formats, file
lists, citations, and narrative/flavour text. Write plain prose, no headings or bullets.

Competition description:
{desc}

Search query:"""


def distil_query(task_desc: str, cache_dir: Path) -> str:
    """One LLM call, cached on disk by description hash (same contract as MLEvolve)."""
    import hashlib
    key = hashlib.sha1(task_desc.encode("utf-8")).hexdigest()[:16]
    cache_file = cache_dir / f"{key}.txt"
    if cache_file.exists():
        cached = cache_file.read_text(encoding="utf-8").strip()
        if cached:
            return cached

    import os
    from openai import OpenAI
    model = os.environ.get("LLM_MODEL", "gpt-5.6-terra")
    client = OpenAI(api_key=os.environ.get("LLM_API_KEY"),
                    base_url=os.environ.get("LLM_BASE_URL") or None)
    params = {"model": model,
              "messages": [{"role": "user",
                            "content": DISTILL_PROMPT.format(desc=task_desc[:12000])}]}
    # GPT-5 / o-series reject max_tokens and sampling params.
    if any(model.lower().split("/")[-1].startswith(p) for p in ("gpt-5", "o1", "o3", "o4")):
        params["max_completion_tokens"] = 300
    else:
        params["max_tokens"] = 300
        params["temperature"] = 0
    q = (client.chat.completions.create(**params).choices[0].message.content or "").strip()

    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(q, encoding="utf-8")
    return q


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", required=True, help="path to description.md (or a raw query with --raw)")
    ap.add_argument("--raw", action="store_true", help="treat --task as a literal query string")
    ap.add_argument("--index", default=str(REPO_ROOT / "output" / "abstract_index"))
    ap.add_argument("--topk", type=int, default=10)
    ap.add_argument("--center", action="store_true", help="mean-center the dense vectors")
    ap.add_argument("--query-mode", choices=("llm", "raw"), default="raw",
                    help="llm = distil the description first (cached); raw = use it as-is")
    ap.add_argument("--cache-dir", default=str(REPO_ROOT / "output" / "query_cache"))
    ap.add_argument("--all", action="store_true",
                    help="compare center on/off x query-mode raw/llm")
    ap.add_argument("--keywords", default=DEFAULT_KEYWORDS,
                    help="comma-separated substrings counted as on-topic (title match)")
    args = ap.parse_args()

    import numpy as np
    from sentence_transformers import SentenceTransformer

    idx = Path(args.index)
    records = [json.loads(l) for l in (idx / "records.jsonl").read_text().splitlines() if l.strip()]
    V0 = np.load(idx / "embeddings.npy").astype("float32")
    manifest = json.loads((idx / "manifest.json").read_text())
    print(f"index: {len(records)} papers | model={manifest['embedding_model']}")

    task = args.task if args.raw else Path(args.task).read_text(encoding="utf-8")
    kws = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]
    model = SentenceTransformer(manifest["embedding_model"])

    def get_query(mode: str) -> str:
        if mode == "llm" and not args.raw:
            return distil_query(task, Path(args.cache_dir))
        return task.strip()[:QUERY_MAX_CHARS]

    def run(center: bool, mode: str):
        q = get_query(mode)
        qv = np.asarray(model.encode([q], normalize_embeddings=True), dtype="float32")[0]
        V = V0
        if center:
            mu = V0.mean(axis=0)
            V = V0 - mu
            V = V / (np.linalg.norm(V, axis=1, keepdims=True) + 1e-9)
            qv = qv - mu
            qv = qv / (np.linalg.norm(qv) + 1e-9)
        s = V @ qv
        top = np.argsort(-s)[:args.topk]
        hits = sum(1 for i in top if any(k in records[i]["title"].lower() for k in kws))
        print(f"\n=== center={'on ' if center else 'off'} query={mode:<3} | {len(q)} chars | "
              f"on-topic {hits}/{args.topk} | spread {s[top[0]] - s[top[-1]]:.3f} ===")
        if mode == "llm" and not args.raw:
            print(f"    query: {q[:200]}")
        for i in top:
            mark = "*" if any(k in records[i]["title"].lower() for k in kws) else " "
            print(f" {mark} {s[i]:.3f} [{records[i]['venue']}] {records[i]['title'][:72]}")
        return hits

    if args.all:
        modes = ("raw",) if args.raw else ("raw", "llm")
        results = {}
        for center in (False, True):
            for mode in modes:
                results[(center, mode)] = run(center, mode)
        print("\n" + "=" * 60)
        print(f"on-topic out of {args.topk}   (* = title matches a keyword)")
        for (c, m), h in results.items():
            print(f"  center={'on ' if c else 'off'} query={m:<3} -> {h}")
        best = max(results, key=results.get)
        print(f"\nbest: center={'on' if best[0] else 'off'}, query={best[1]}")
    else:
        run(args.center, args.query_mode)


if __name__ == "__main__":
    main()
