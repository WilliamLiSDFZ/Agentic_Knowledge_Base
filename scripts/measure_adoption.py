"""Phase 0: did the agent actually USE the retrieved techniques, and did it help?

The score-level ablation cannot answer this. It compares whole runs and, at 3-4 draws, its
confidence intervals all contain zero — and Meta's MLE-bench study (arXiv 2507.02554) says 3
seeds is not enough for reliable comparisons at all, recommending 10-20 per competition. Closing
that gap costs hundreds of GPU-hours per task.

Adoption is a different measurement, and a cheaper one: it uses runs that already exist and no
GPU. It asks, per generated solution, whether each injected technique was implemented fully, as
a weakened proxy, or not at all — and then whether nodes that adopted scored better.

That distinction is what decides the next code change:

    low adoption                  -> the problem is BINDING. Techniques are advisory context the
                                     model may ignore at no cost; the fix is to bind them
                                     (one candidate per technique, hard constraint, selected by
                                     validation score) as MLE-STAR does.
    high adoption, no score gain  -> the problem is SELECTION. We are retrieving techniques whose
                                     preconditions the competition does not satisfy; the fix is
                                     to filter on the `Condition` field, which is extracted for
                                     every technique today and used for nothing.

The motivating observation, from essay seed 44: the baseline solution mentions
argument/annotation/discourse zero times, arm B four times, arm C fourteen. The injected
technique was "append annotated argumentative components", which the competition has no
annotations for — and the agent wrote regex discourse-marker counts instead. So knowledge is
being read and adapted, but into a proxy that may capture little of the paper's claimed gain.
This script measures how often that happens and what it is worth.

    python scripts/measure_adoption.py --runs ~/nautilus/results \\
        --inventory results/8.19/run_inventory.csv --out results/8.19

Needs `logs/injected_knowledge.md` in each run (written by MLEvolve's knowledge.py as of
2026-08-19). Older runs predate it; they are reported as unmeasurable rather than skipped
silently, because a run missing from an adoption table looks identical to a run with zero
adoption.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

# ══════════════════════════════════════════════════════════════════════════════════════
#  TUNABLES
# ══════════════════════════════════════════════════════════════════════════════════════

MAX_CODE_CHARS = 24000
"""Code sent to the judge per node. Solutions run to 40 KB; the judge only needs to spot whether
a technique is present, and the tail is usually inference/submission boilerplate."""

MAX_NODES_PER_RUN = 0
"""0 = judge every non-root node. Set a small number to sample while iterating on the prompt."""

TECHNIQUE_HEADING = re.compile(r"^###\s+(.+?)\s*$", re.M)
"""Techniques are emitted by plugin_a_methodology as `### <name>` blocks; `## Methodology
Insights from Literature` is the file header and is not a technique."""

VERDICTS = ("full", "proxy", "none")

# All techniques are judged in ONE call per node rather than one call per (technique, node).
# That is 10x fewer calls — 450 instead of 4,500 over this corpus, which matters because the
# LLM subscription behind the proxy has been exhausted twice already. It is also the better
# measurement: the judge sees the techniques side by side and can say which one the code
# actually matches, instead of answering ten independent yes/no questions about overlapping
# ideas and drifting toward "proxy" on all of them.
JUDGE_PROMPT = """You are auditing which of several research-paper techniques a machine-learning
solution implements.

TECHNIQUES
{techniques}

SOLUTION CODE (may be truncated)
```python
{code}
```

For EACH technique, decide:
- "full"  : the code implements it substantially as described, including whatever data or
            signal it depends on.
- "proxy" : the code implements a recognisably weakened stand-in — the same idea approximated
            with resources actually available. Example: hand-written keyword regexes standing in
            for human annotations the technique assumes.
- "none"  : not implemented. Superficial word overlap is NOT adoption.

Be strict, and be discriminating: if several techniques describe similar ideas, assign the
credit to the closest one and mark the rest "none". Most entries should be "none"; that is the
expected answer, not a failure.

Return ONLY a JSON array, one object per technique, in the same order, no other text:
[{{"i": 1, "verdict": "full|proxy|none", "evidence": "<=20 words quoting a symbol or line, or empty"}}]"""


# ══════════════════════════════════════════════════════════════════════════════════════


JUDGE_ATTEMPTS = 3
JUDGE_BACKOFF = (2, 8, 20)      # seconds before retry 2, 3 — most blips self-heal in the first


@dataclass
class NodeResult:
    run: str
    task: str
    arm: str
    node: int
    stage: str
    metric: float | None
    is_buggy: bool
    verdicts: dict = field(default_factory=dict)   # technique name -> verdict
    error: str = ""
    """Non-empty when judging this node failed after every retry.

    An errored node must never be counted as 'not adopted'. The first version of this script
    caught judge exceptions and recorded "none" for every technique, which means a flaky network
    would have manufactured exactly the finding we are looking for — low adoption. Errors are
    kept as errors, excluded from the statistics, and reported separately."""

    @property
    def adopted(self) -> bool:
        return any(v in ("full", "proxy") for v in self.verdicts.values())

    def to_json(self) -> dict:
        return {"run": self.run, "task": self.task, "arm": self.arm, "node": self.node,
                "stage": self.stage, "metric": self.metric, "is_buggy": self.is_buggy,
                "verdicts": self.verdicts, "error": self.error}

    @staticmethod
    def from_json(d: dict) -> "NodeResult":
        return NodeResult(run=d["run"], task=d["task"], arm=d["arm"], node=int(d["node"]),
                          stage=d.get("stage", ""), metric=d.get("metric"),
                          is_buggy=bool(d.get("is_buggy")), verdicts=d.get("verdicts", {}),
                          error=d.get("error", ""))


def split_techniques(text: str) -> dict[str, str]:
    """Split injected_knowledge.md into {technique name: full block}."""
    out: dict[str, str] = {}
    marks = list(TECHNIQUE_HEADING.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out[m.group(1).strip()] = text[m.start():end].strip()
    return out


def load_inventory(path: Path) -> dict[str, dict]:
    with path.open() as fh:
        return {r["name"]: r for r in csv.DictReader(fh)}


def judge_node(client, model: str, techs: dict[str, str], code: str) -> dict[str, str]:
    """Judge every technique against one solution in a single call. Returns {name: verdict}.

    An unparseable or short reply yields "none" for everything, which is the conservative
    direction: it can only understate adoption, never invent it.
    """
    names = list(techs)
    listing = "\n\n".join(f"[{i + 1}] {techs[n][:1800]}" for i, n in enumerate(names))
    prompt = JUDGE_PROMPT.format(techniques=listing, code=code[:MAX_CODE_CHARS])

    params = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    budget = 120 * len(names) + 300
    base = model.lower().split("/")[-1]
    if any(base.startswith(p) for p in ("gpt-5", "o1", "o3", "o4")):
        params["max_completion_tokens"] = budget      # reasoning models reject the others
    else:
        params["max_tokens"] = budget
        params["temperature"] = 0

    # Retry transient failures before giving up. A raised exception here becomes a recorded
    # `error` on the node, never a set of "none" verdicts.
    last = None
    for attempt in range(JUDGE_ATTEMPTS):
        try:
            raw = (client.chat.completions.create(**params)
                   .choices[0].message.content or "").strip()
            break
        except Exception as e:                       # noqa: BLE001 - any transport failure
            last = e
            if attempt < JUDGE_ATTEMPTS - 1:
                time.sleep(JUDGE_BACKOFF[attempt])
    else:
        raise RuntimeError(f"{type(last).__name__}: {last}")

    out = {n: "none" for n in names}
    m = re.search(r"\[.*\]", raw, re.S)
    if not m:
        return out
    try:
        for item in json.loads(m.group(0)):
            i = int(item.get("i", 0)) - 1
            v = item.get("verdict")
            if 0 <= i < len(names) and v in VERDICTS:
                out[names[i]] = v
    except (json.JSONDecodeError, TypeError, ValueError):
        pass
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True, help="directory of run directories")
    ap.add_argument("--inventory", required=True, help="run_inventory.csv from analyze_runs.py")
    ap.add_argument("--out", default=None, help="output dir (default: alongside the inventory)")
    ap.add_argument("--only-usable", action="store_true", default=True,
                    help="restrict to runs analyze_runs.py rated ok (default)")
    ap.add_argument("--restart", action="store_true",
                    help="ignore any existing adoption.jsonl checkpoint and judge everything "
                         "again (default: resume, skipping nodes already judged)")
    ap.add_argument("--dry-run", action="store_true",
                    help="report coverage and how many judge calls would be made, then stop")
    args = ap.parse_args()

    root = Path(args.runs)
    out = Path(args.out) if args.out else Path(args.inventory).parent
    out.mkdir(parents=True, exist_ok=True)
    inv = load_inventory(Path(args.inventory))

    # -- gather what is measurable ------------------------------------------------------
    measurable, missing = [], []
    for name, row in sorted(inv.items()):
        if row["arm"] not in ("B", "C"):
            continue                      # arm A receives no knowledge; nothing to adopt
        if args.only_usable and row["verdict"] != "ok":
            continue
        kfile = root / name / "logs" / "injected_knowledge.md"
        (measurable if kfile.exists() else missing).append((name, row, kfile))

    print(f"KB-arm runs rated usable : {len(measurable) + len(missing)}")
    print(f"  with injected_knowledge.md : {len(measurable)}")
    print(f"  without (predate the dump) : {len(missing)}")
    if missing:
        print("\nThese runs CANNOT be measured — they are not zero-adoption, they are unknown:")
        for n, _, _ in missing[:10]:
            print(f"    {n}")
        print("  Recover by replaying retrieval on the pod and checking the recovered text's\n"
              "  sha1[:8] against the 'digest' in each run's MLEvolve.log, or simply measure\n"
              "  adoption on runs launched from now on.")
    if not measurable:
        print("\nNothing measurable yet. Relaunch at least one KB arm with the current code.")
        return 1

    # -- count the work ------------------------------------------------------------------
    plan = []
    for name, row, kfile in measurable:
        techs = split_techniques(kfile.read_text(errors="replace"))
        jr = root / name / "logs" / "journal.json"
        nodes = []
        if jr.exists():
            try:
                allnodes = json.loads(jr.read_text(errors="replace")).get("nodes", [])
                nodes = [n for n in allnodes if n.get("stage") != "root" and n.get("code")]
            except json.JSONDecodeError:
                pass
        if MAX_NODES_PER_RUN:
            nodes = nodes[:MAX_NODES_PER_RUN]
        plan.append((name, row, techs, nodes))
        print(f"  {name:<40} {len(techs):>3} techniques x {len(nodes):>3} nodes "
              f"= {len(nodes):>4} judge calls")
    total = sum(len(n) for _, _, _, n in plan)
    print(f"\ntotal judge calls: {total}  (one per node; all techniques judged together)")
    if args.dry_run:
        return 0

    # -- judge ---------------------------------------------------------------------------
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        from llm import MODEL, client            # repo-standard client, reads .env
    except Exception as e:
        print(f"\nFATAL: cannot load the LLM client ({e}). scripts/llm.py needs LLM_API_KEY.")
        return 1
    model = os.environ.get("ADOPTION_JUDGE_MODEL", MODEL)
    print(f"judging with {model}\n")

    # Checkpoint every judged node immediately. A 536-call pass costs real money and real time;
    # losing it to a dropped connection at call 400 is avoidable with one append per node.
    ckpt = out / "adoption.jsonl"
    results: list[NodeResult] = []
    if ckpt.exists() and not args.restart:
        with ckpt.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        results.append(NodeResult.from_json(json.loads(line)))
                    except (json.JSONDecodeError, KeyError):
                        pass          # a half-written final line from a hard kill; drop it
        # Errored nodes are NOT treated as done — retry them on resume.
        done_keys = {(r.run, r.node) for r in results if not r.error}
        results = [r for r in results if not r.error]
        print(f"resuming: {len(done_keys)} node(s) already judged in {ckpt.name}")
    else:
        done_keys = set()
        if ckpt.exists():
            ckpt.unlink()

    todo = sum(1 for _, _, _, nodes in plan for i in range(len(nodes)) if True) - len(done_keys)
    print(f"{todo} node(s) to judge\n")

    done, errors = 0, 0
    with ckpt.open("a", encoding="utf-8") as fh:
        for name, row, techs, nodes in plan:
            for i, n in enumerate(nodes):
                if (name, i) in done_keys:
                    continue
                m = n.get("metric") or {}
                nr = NodeResult(run=name, task=row["task"], arm=row["arm"], node=i,
                                stage=n.get("stage", ""),
                                metric=m.get("value") if isinstance(m, dict) else None,
                                is_buggy=bool(n.get("is_buggy")))
                try:
                    nr.verdicts = judge_node(client, model, techs, n["code"])
                except Exception as e:
                    nr.error = f"{type(e).__name__}: {e}"
                    nr.verdicts = {}
                    errors += 1
                    print(f"  JUDGE FAILED {name} node {i}: {nr.error}")
                fh.write(json.dumps(nr.to_json()) + "\n")
                fh.flush()
                done += 1
                if done % 20 == 0:
                    print(f"  {done}/{todo}" + (f"  ({errors} failed)" if errors else ""))
                results.append(nr)

    if errors:
        print(f"\n{errors} node(s) could not be judged after {JUDGE_ATTEMPTS} attempts. They are "
              f"recorded with an `error` and EXCLUDED from the statistics below — they are not "
              f"evidence of non-adoption. Re-run to retry just those.")
    results = [r for r in results if not r.error] or results

    # -- write + report ------------------------------------------------------------------
    detail = out / "adoption.csv"
    with detail.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["run", "task", "arm", "node", "stage", "metric", "is_buggy",
                    "technique", "verdict", "judge_error"])
        for r in results:
            if r.error:
                # One row so the failure is visible in the CSV too, rather than the node simply
                # being absent — an absent node looks identical to a node with no adoption.
                w.writerow([r.run, r.task, r.arm, r.node, r.stage, r.metric, r.is_buggy,
                            "", "", r.error])
                continue
            for t, v in r.verdicts.items():
                w.writerow([r.run, r.task, r.arm, r.node, r.stage, r.metric, r.is_buggy,
                            t, v, ""])

    print(f"\n{'run':<40}{'arm':>4}{'nodes':>7}{'adopted':>9}{'full':>6}{'proxy':>7}")
    print("-" * 76)
    for name, row, _, _ in plan:
        rs = [r for r in results if r.run == name]
        if not rs:
            continue
        ad = sum(1 for r in rs if r.adopted)
        full = sum(sum(1 for v in r.verdicts.values() if v == "full") for r in rs)
        prox = sum(sum(1 for v in r.verdicts.values() if v == "proxy") for r in rs)
        print(f"{name:<40}{row['arm']:>4}{len(rs):>7}{ad:>6}/{len(rs):<3}{full:>6}{prox:>7}")

    # The question the next code change turns on: do adopting nodes score better?
    print("\nadopted vs not, among nodes with a metric (per task, direction-aware):")
    for task in sorted({r.task for r in results}):
        rs = [r for r in results if r.task == task and r.metric is not None and not r.is_buggy]
        a = [r.metric for r in rs if r.adopted]
        b = [r.metric for r in rs if not r.adopted]
        if not a or not b:
            print(f"  {task:<10} not enough of both groups (adopted {len(a)}, not {len(b)})")
            continue
        print(f"  {task:<10} adopted n={len(a):<3} mean {sum(a)/len(a):.5f}   "
              f"not-adopted n={len(b):<3} mean {sum(b)/len(b):.5f}")
    print("\n  (raw node metrics are the agent's own validation scores and are NOT comparable\n"
          "   across runs; read the within-run direction, not the absolute level.)")
    print(f"\nwrote {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
