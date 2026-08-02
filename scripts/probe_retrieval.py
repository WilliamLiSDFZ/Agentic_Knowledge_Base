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

# Keep in sync with MLEvolve engine/coldstart/ondemand.py::_QUERY_DROP_HEADINGS
DROP_HEADINGS = (
    "submission file", "file descriptions", "citation", "prizes", "timeline",
    "getting started", "required submission format", "task and metric alignment",
    "evaluation",
)
QUERY_MAX_CHARS = 2500
DEFAULT_KEYWORDS = "molecul,smiles,admet,drug,chem,compound,protein,ligand,qsar,graph neural"


def focus_query(task_desc: str) -> str:
    kept, skipping = [], False
    for line in task_desc.splitlines():
        s = line.strip()
        if s.startswith("#"):
            heading = s.lstrip("#").strip().lower()
            skipping = any(h in heading for h in DROP_HEADINGS)
            if not skipping:
                kept.append(s.lstrip("#").strip())
            continue
        if skipping or s.startswith(("```", "|", "---", "===")) or not s:
            continue
        kept.append(s)
    q = " ".join(kept).strip()
    return (q if len(q) >= 100 else task_desc.strip())[:QUERY_MAX_CHARS]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", required=True, help="path to description.md (or a raw query with --raw)")
    ap.add_argument("--raw", action="store_true", help="treat --task as a literal query string")
    ap.add_argument("--index", default=str(REPO_ROOT / "output" / "abstract_index"))
    ap.add_argument("--topk", type=int, default=10)
    ap.add_argument("--center", action="store_true", help="mean-center the dense vectors")
    ap.add_argument("--focus", action="store_true", help="use the focused query")
    ap.add_argument("--all", action="store_true", help="compare all 4 center/focus combinations")
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

    def run(center: bool, focus: bool):
        q = focus_query(task) if focus else task.strip()
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
        label = f"center={'on ' if center else 'off'} focus={'on ' if focus else 'off'}"
        print(f"\n=== {label} | query {len(q)} chars | "
              f"on-topic {hits}/{args.topk} | spread {s[top[0]] - s[top[-1]]:.3f} ===")
        for i in top:
            mark = "*" if any(k in records[i]["title"].lower() for k in kws) else " "
            print(f" {mark} {s[i]:.3f} [{records[i]['venue']}] {records[i]['title'][:72]}")
        return hits

    if args.all:
        results = {}
        for center in (False, True):
            for focus in (False, True):
                results[(center, focus)] = run(center, focus)
        print("\n" + "=" * 60)
        print(f"on-topic out of {args.topk}   (* = title matches a keyword)")
        for (c, f), h in results.items():
            print(f"  center={'on ' if c else 'off'} focus={'on ' if f else 'off'} -> {h}")
        best = max(results, key=results.get)
        print(f"\nbest: center={'on' if best[0] else 'off'}, focus={'on' if best[1] else 'off'}")
    else:
        run(args.center, args.focus)


if __name__ == "__main__":
    main()
