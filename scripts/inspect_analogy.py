"""What did the analogy agent inject into a run, and what did the improve nodes do with it?

Reads one arm-D run directory and answers, per improve node and in aggregate, the questions the
design doc says to ask before looking at any score (`docs/analogy_bm25_agent_design.md` §7):

  - did the agent fire, and did it produce a report (mechanisms) or come back empty;
  - WHAT it diagnosed (bottlenecks) and WHAT it suggested (mechanism titles, cited papers);
  - whether the suggestions repeat from node to node — the same mechanism re-injected six
    times is a different failure from six different mechanisms nobody adopted;
  - which subfields the citations come from (venue mix; an NLP task citing only ACL/NAACL is
    not analogical retrieval);
  - whether the child's plan picked a suggestion up (word overlap with the mechanism title —
    a cheap proxy; `measure_adoption.py` is the real judge) and how the child's metric moved
    against its parent, split by adopted / not — the negative-transfer question.

Everything comes from `logs/journal.json` (`analogy_report` on each improve node, written by
MLEvolve), which `fetch-run.sh` always copies. If `logs/analogy/index.jsonl` is present too
(fetch-run.sh copies `logs/analogy` since 2026-09-03), the queries, turn counts and token
costs are shown as well, and `--domain-words` flags queries that use the competition's own
vocabulary — the thing the agent prompt forbids.

    python scripts/inspect_analogy.py --run ~/nautilus/results/<run>
    python scripts/inspect_analogy.py --run <run> --domain-words essay,score,student,writing,grade
    python scripts/inspect_analogy.py --run <run> --show 19        # full report injected at step 19
"""
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

HEADING = re.compile(r"^### (.+?)\s*$", re.M)
BOTTLENECK = re.compile(r"^\d+\. (.+?)(?: — evidence:.*)?$", re.M)
CITE = re.compile(r"`([a-z0-9-]+/[^`]+)`")
STOP = set("a an the of to in on for with by and or as at from is are was were be been it its this "
           "that these those than then there via using use used based can could may might will "
           "would should not no nor do does such each any all both more most much many few less".split())


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z]+", " ", t.lower()).strip()


def title_words(t: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{5,}", t.lower()) if w not in STOP}


def load_run(run: Path):
    j = json.loads((run / "logs" / "journal.json").read_text(encoding="utf-8", errors="replace"))
    nodes = j.get("nodes", [])
    by_id = {n["id"]: n for n in nodes}
    n2p = j.get("node2parent", {})
    index = []
    idx = run / "logs" / "analogy" / "index.jsonl"
    if idx.exists():
        for line in idx.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                try:
                    index.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return nodes, by_id, n2p, index


def metric_of(n: dict | None):
    m = (n or {}).get("metric") or {}
    return m.get("value") if isinstance(m, dict) else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True, help="run directory (contains logs/journal.json)")
    ap.add_argument("--domain-words", default="",
                    help="comma-separated competition vocabulary; queries containing any are flagged")
    ap.add_argument("--show", type=int, default=None, help="print the full report injected at this step")
    args = ap.parse_args()

    run = Path(args.run)
    nodes, by_id, n2p, index = load_run(run)
    maximize = None
    for n in nodes:
        m = n.get("metric")
        if isinstance(m, dict) and m.get("maximize") is not None:
            maximize = m["maximize"]
            break
    sign = -1.0 if maximize is False else 1.0

    improve = [n for n in nodes if n.get("stage") == "improve"]
    with_report = [n for n in improve if n.get("analogy_report")]
    if args.show is not None:
        for n in with_report:
            if int(n.get("step", -1)) == args.show:
                print(n["analogy_report"])
                return 0
        print(f"no analogy_report on step {args.show}")
        return 1

    print(f"run: {run.name}")
    stages = collections.Counter(n.get("stage") for n in nodes if n.get("stage") != "root")
    print(f"nodes: {dict(stages)}; improve nodes with a report: {len(with_report)}/{len(improve)}"
          + (f"; agent invocations in index.jsonl: {len(index)}" if index else
             "; (no logs/analogy/index.jsonl — queries/turns unavailable; re-fetch with the updated fetch-run.sh)"))

    # ------------------------------------------------------------ per node
    print(f"\n{'step':>4} {'parent':>7} {'child':>7} {'delta':>8}  {'bug':<3} {'#m':>2}  mentioned  mechanisms")
    print("-" * 110)
    cites, venues, titles, families = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    deltas_adopted, deltas_not, buggy_adopted, buggy_not = [], [], 0, 0
    for n in improve:
        rep = n.get("analogy_report") or ""
        parent = by_id.get(n2p.get(n["id"]))
        pm, cm = metric_of(parent), metric_of(n)
        mech = HEADING.findall(rep)
        plan = (n.get("plan") or "").lower()
        mentioned = [t for t in mech if len(title_words(t) & set(re.findall(r"[a-z]{5,}", plan))) >= 2]
        for pid in CITE.findall(rep):
            cites[pid] += 1
            venues[pid.split("/")[0]] += 1
        for t in mech:
            titles[norm_title(t)] += 1
            for w in title_words(t):
                families[w] += 1
        delta = (sign * (cm - pm)) if (pm is not None and cm is not None) else None
        if mech:
            if mentioned:
                (deltas_adopted.append(delta) if delta is not None else None)
                buggy_adopted += bool(n.get("is_buggy"))
            else:
                (deltas_not.append(delta) if delta is not None else None)
                buggy_not += bool(n.get("is_buggy"))
        fmt = lambda v: f"{v:.4f}" if isinstance(v, (int, float)) else "   -  "
        print(f"{n.get('step', '?'):>4} {fmt(pm):>7} {fmt(cm):>7} {('%+.4f' % delta) if delta is not None else '    -   ':>8}  "
              f"{'Y' if n.get('is_buggy') else '-':<3} {len(mech):>2}  {len(mentioned):>3}/{len(mech):<3}    "
              + ("; ".join(t[:48] for t in mech) if mech else "(no report)"))

    # ------------------------------------------------------------ aggregates
    print("\nrepetition: %d mechanism blocks, %d distinct titles; most frequent title words:"
          % (sum(titles.values()), len(titles)))
    print("  " + ", ".join(f"{w}×{c}" for w, c in families.most_common(12)))
    print("\ncitations (paper × times cited):")
    for p, c in cites.most_common(15):
        print(f"  {c:>2}  {p}")
    if len(cites) > 15:
        print(f"  ... {len(cites) - 15} more")
    print("venue mix:", ", ".join(f"{v}:{c}" for v, c in venues.most_common()))

    def stats(vals):
        vals = [v for v in vals if v is not None]
        return (f"n={len(vals)} mean {sum(vals) / len(vals):+.4f} "
                f"(+{sum(1 for v in vals if v > 0)}/-{sum(1 for v in vals if v < 0)})") if vals else "n=0"
    print(f"\nchild metric change vs parent (sign-corrected, positive = better):")
    print(f"  plan mentions a suggested mechanism : {stats(deltas_adopted)}; buggy children {buggy_adopted}")
    print(f"  plan mentions none                  : {stats(deltas_not)}; buggy children {buggy_not}")
    print("  (word-overlap proxy — run measure_adoption.py for judged adoption)")

    # ------------------------------------------------------------ queries (if fetched)
    if index:
        dw = [w.strip().lower() for w in args.domain_words.split(",") if w.strip()]
        print(f"\nagent invocations: {len(index)}; ok {sum(1 for r in index if r.get('ok'))}; "
              f"turns mean {sum(r.get('turns', 0) for r in index) / len(index):.1f}; "
              f"tokens in/out total {sum(r.get('in_tokens', 0) for r in index)}/{sum(r.get('out_tokens', 0) for r in index)}; "
              f"seconds mean {sum(r.get('seconds', 0) for r in index) / len(index):.0f}")
        flagged, total = 0, 0
        allq = collections.Counter()
        for r in index:
            for q in r.get("queries", []):
                total += 1
                allq[q.lower()] += 1
                if dw and any(w in q.lower() for w in dw):
                    flagged += 1
        if dw:
            print(f"queries using competition vocabulary ({', '.join(dw)}): {flagged}/{total}")
        print("most repeated queries:")
        for q, c in allq.most_common(12):
            print(f"  {c:>2}  {q}")
        for r in index:
            if not r.get("ok"):
                print(f"  no report: invocation {r.get('invocation')} parent {str(r.get('parent_id'))[:8]} — {r.get('reason')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
