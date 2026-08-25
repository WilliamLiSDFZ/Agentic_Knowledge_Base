"""Show which models each run's solutions actually used, across the whole search.

Read this before trusting any claim about "arm B used TF-IDF". The obvious way to answer that
question is to grep `logs/best_solution.py`, and it gives the wrong answer: that file is ONE
solution out of roughly twenty, so it tells you which approach won, not which approaches the
agent explored. Doing exactly that produced a confident and wrong conclusion once — that a KB arm
had "abandoned transformers" — when in fact 18 of its 19 nodes contained a transformer and only
its single best-scoring node happened to be TF-IDF.

So this reads every node in `logs/journal.json` and reports both numbers separately:
  * how many nodes used each model  (what the agent explored)
  * what the best-scoring valid node used  (what won)

Model names are extracted rather than matched against a keyword list, so a model nobody thought
to grep for still shows up:
  * HuggingFace ids from `from_pretrained("org/name")` and bare "org/name" strings
  * scikit-learn / boosting estimators by class-name shape (…Classifier, …Regressor, …Vectorizer)

    python scripts/show_models.py --runs ~/nautilus/results --task jigsaw
    python scripts/show_models.py --runs ~/nautilus/results --task jigsaw --per-node
    python scripts/show_models.py --runs ~/nautilus/results --only s45
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

# "org/model-name" as it appears in HuggingFace ids. Excludes anything that looks like a file
# path or a local directory, which otherwise dominate the output.
HF = re.compile(r"""["']([A-Za-z0-9][\w.-]*/[\w.-]+)["']""")
HF_REJECT = re.compile(r"\.(pt|pth|bin|csv|json|npy|h5|txt|md|py|safetensors)$|^\.{0,2}/|workspace|input/|output/")

# Estimator classes by shape, not by a fixed list, so unfamiliar ones are still caught.
EST = re.compile(r"\b([A-Z][A-Za-z0-9]{2,}(?:Classifier|Regressor|Vectorizer|Encoder|Ranker|CV))\b")
# A few common ones the shape rule misses.
EST_EXTRA = re.compile(r"\b(LinearSVC|SVC|Ridge|Lasso|ElasticNet|CatBoost|LightGBM|XGBoost|NBSVM)\b")

TRANSFORMERY = re.compile(r"bert|roberta|deberta|electra|xlnet|distil|gpt|t5|bart|longformer|e5|gte|mpnet|minilm",
                          re.I)


def models_in(code: str) -> set[str]:
    out: set[str] = set()
    for m in HF.findall(code or ""):
        if not HF_REJECT.search(m):
            out.add(m)
    for m in EST.findall(code or "") + EST_EXTRA.findall(code or ""):
        out.add(m)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True)
    ap.add_argument("--task", default=None, help="filter by task short name (jigsaw/essay/lmsys)")
    ap.add_argument("--only", default=None, help="substring filter on run directory names")
    ap.add_argument("--inventory", default=None,
                    help="run_inventory.csv, to label arms and skip invalid runs")
    ap.add_argument("--per-node", action="store_true", help="list every node, not just a summary")
    ap.add_argument("--top", type=int, default=8, help="how many models to list per run")
    args = ap.parse_args()

    inv = {}
    if args.inventory and Path(args.inventory).exists():
        with open(args.inventory) as fh:
            inv = {r["name"]: r for r in csv.DictReader(fh)}

    root = Path(args.runs)
    for run in sorted(p for p in root.iterdir() if p.is_dir()):
        if args.only and args.only not in run.name:
            continue
        meta = inv.get(run.name, {})
        if args.task and meta and meta.get("task") != args.task:
            continue
        if args.task and not meta and args.task not in run.name:
            continue
        jr = run / "logs" / "journal.json"
        if not jr.exists():
            continue
        try:
            nodes = [n for n in json.loads(jr.read_text(errors="replace")).get("nodes", [])
                     if n.get("stage") != "root" and n.get("code")]
        except json.JSONDecodeError:
            continue
        if not nodes:
            continue

        counts: Counter = Counter()
        n_tr = 0
        for n in nodes:
            ms = models_in(n["code"])
            counts.update(ms)
            if any(TRANSFORMERY.search(m) for m in ms):
                n_tr += 1

        valid = [n for n in nodes
                 if n.get("is_valid") and isinstance(n.get("metric"), dict)
                 and n["metric"].get("value") is not None]
        best = None
        if valid:
            maximize = bool(valid[0]["metric"].get("maximize"))
            best = (max if maximize else min)(valid, key=lambda n: n["metric"]["value"])

        arm = meta.get("arm", "?")
        verdict = meta.get("verdict", "")
        print(f"\n=== {run.name}   arm={arm}  {verdict}")
        print(f"    {len(nodes)} nodes, {len(valid)} valid, "
              f"{n_tr} nodes ({n_tr / len(nodes) * 100:.0f}%) use a transformer")
        for m, c in counts.most_common(args.top):
            bar = "#" * min(30, c)
            print(f"      {c:>3}/{len(nodes):<3} {m:<38} {bar}")
        if best:
            bm = sorted(models_in(best["code"]))
            print(f"    BEST node (metric {best['metric']['value']:.5f}): "
                  f"{', '.join(bm) if bm else '(no model identified)'}")
        else:
            print("    BEST node: none — no valid solution in this run")

        if args.per_node:
            for i, n in enumerate(nodes):
                v = n.get("metric", {})
                v = v.get("value") if isinstance(v, dict) else None
                tag = "OK " if n.get("is_valid") else ("BUG" if n.get("is_buggy") else "   ")
                print(f"      [{i:>3}] {tag} {('%.5f' % v) if v is not None else '  -  ':>9}  "
                      f"{', '.join(sorted(models_in(n['code']))[:4]) or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
