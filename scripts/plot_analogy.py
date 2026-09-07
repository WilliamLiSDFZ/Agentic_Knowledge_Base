"""Figures for the analogy-agent arms (D: at improve nodes, E: on the task before the first
draft, F: both) — and only for them.

analyze_runs.py / plot_effects.py compare whole runs across all arms. This script looks INSIDE the
analogy runs, because the design doc (docs/analogy_bm25_agent_design.md §7) says the score is the
last thing to look at: with n<=3 draws the D-A interval always contains zero, and the questions
that decide the next code change are process questions the score cannot answer.

    <task>_analogy_funnel.png     did the agent fire? nodes -> improve nodes -> reports ->
                                  mechanisms -> valid children, one panel per valid D run
    <task>_analogy_transfer.png   per-node transfer: child-vs-parent metric change at improve
                                  nodes, D split by adopted / not adopted, paired A run as control
                                  (the negative-transfer question)
    <task>_analogy_retrieval.png  is it cross-domain? venue-family mix of the papers each run
                                  cited; share of queries in the competition's own vocabulary;
                                  mechanism repetition; citation concentration
    <task>_analogy_cost.png       what did each invocation cost — turns, tokens, seconds
    <task>_analogy_score.png      D-A at matched K per draw, paired (filled) vs borrowed (hollow),
                                  mean and 95% t interval — the same rule as plot_effects.py
                                  (E-A / F-A go to <task>_analogy_score_E.png etc.)
    <task>_analogy_branches.png   arm E only: best metric of the branch grown from the injected
                                  first draft against the run's other branches and the paired A
                                  run's branches — a draft has no parent, so "transfer" for E is
                                  a branch question, not a node question
    analogy_summary.csv           one row per D/E/F run with every number the figures draw

Only runs analyze_runs.py judged `ok` are drawn (invalid ones — crashed, disk-starved, killed —
are counted in each figure's footer); the CSV lists every D run with its verdict.

Adoption: nodes are judged by measure_adoption.py's LLM verdicts when its adoption.csv is present
(pass --adoption, or leave it next to the inventory); otherwise the word-overlap proxy from
inspect_analogy.py is used and the figure says so. The two are not mixed within one figure.

    python scripts/plot_analogy.py --runs ~/nautilus/results --out results/9.5
    python scripts/plot_analogy.py --runs ~/nautilus/results --out results/9.5 \\
        --scores ~/nautilus/results/scores.csv --adoption results/9.5/adoption.csv

Requires analyze_runs.py to have been run on the same --runs (run_inventory.csv in --out): the
arm, verdict and draw pairing come from there, so this script can never pair runs differently
from the main analysis.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt        # noqa: E402
import matplotlib.ticker               # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analyze_runs as ar               # noqa: E402  (Run, build_groups, load_scores, _matched_k)
from plot_effects import ARM_COLOR, mean_ci   # noqa: E402

# ── palette (dataviz reference instance; D/A colours shared with plot_effects) ──────────
C_D, C_A = ARM_COLOR["D"], ARM_COLOR["A"]
C_ADOPT, C_NOT = "#2a78d6", "#eb6834"           # categorical slots 1, 2
C_MUTED, C_GRID, C_TEXT2 = "#9a9a94", "#e6e6e2", "#52514e"
VENUE_FAMILY = {                                  # part-to-whole, five slots, fixed order
    "NLP": ("acl", "naacl", "emnlp", "eacl", "coling"),
    "ML": ("icml", "iclr", "neurips", "nips"),
    "Vision": ("cvpr", "iccv", "eccv", "wacv"),
    "AI": ("aaai", "ijcai", "kdd", "www", "sigir"),
}
FAMILY_ORDER = ["NLP", "ML", "Vision", "AI", "Other"]
FAMILY_COLOR = {"NLP": "#2a78d6", "ML": "#eb6834", "Vision": "#1baf7a", "AI": "#eda100", "Other": "#9a9a94"}

# Competition vocabulary the agent prompt forbids in queries. Keyed by the inventory's task name
# (analyze_runs' short name, or the exp_id when it has none). Add a task here when you add a job.
DOMAIN_WORDS = {
    "essay": ("essay", "score", "student", "writing", "grade", "kappa", "qwk"),
    "jigsaw": ("toxic", "toxicity", "comment", "identity", "insult", "obscene"),
    "jigsaw-unintended-bias-in-toxicity-classification":
        ("toxic", "toxicity", "comment", "identity", "bias", "subgroup", "civil"),
    "tensorflow2-question-answering":
        ("wikipedia", "question answering", "natural questions", "long answer", "short answer"),
    "lmsys": ("chatbot", "arena", "preference", "prompt", "response"),
    "spooky": ("author", "spooky", "poe", "lovecraft", "shelley"),
}

SHORT_TASK = {"jigsaw-unintended-bias-in-toxicity-classification": "jubias",
              "tensorflow2-question-answering": "tf2qa"}


def tname(task: str) -> str:
    return SHORT_TASK.get(task, task)


def median(xs: list[float]) -> float:
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


HEADING = re.compile(r"^### (.+?)\s*$", re.M)
CITE = re.compile(r"`([a-z0-9-]+/[^`]+)`")
STOP = set("a an the of to in on for with by and or as at from is are was were be been it its this "
           "that these those than then there via using use used based can could may might will "
           "would should not no nor do does such each any all both more most much many few less".split())


def title_words(t: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{5,}", t.lower()) if w not in STOP}


def venue_family(paper_id: str) -> str:
    v = paper_id.split("/")[0].split("-")[0].lower()
    for fam, names in VENUE_FAMILY.items():
        if v in names:
            return fam
    return "Other"


# ══════════════════════════════════════════════════════════════════════════════════════
#  Loading
# ══════════════════════════════════════════════════════════════════════════════════════


def load_inventory(path: Path) -> list[ar.Run]:
    """Rebuild analyze_runs.Run objects from its CSV so build_groups() pairs exactly as it did."""
    runs = []
    with path.open() as fh:
        for row in csv.DictReader(fh):
            r = ar.Run()
            for k, v in row.items():
                if not hasattr(r, k):
                    continue
                cur = getattr(r, k)
                try:
                    if isinstance(cur, bool):
                        v = v in ("True", "true", "1")
                    elif isinstance(cur, int):
                        v = int(float(v)) if v else 0
                    elif isinstance(cur, float):
                        v = float(v) if v else 0.0
                except ValueError:
                    pass
                setattr(r, k, v)
            runs.append(r)
    return runs


@dataclass
class NodeRec:
    idx: int                    # index among non-root nodes WITH code (measure_adoption's `node`)
    step: int
    stage: str
    metric: float | None
    parent_metric: float | None
    buggy: bool
    delta: float | None         # sign-corrected child - parent, None if either metric missing
    mechanisms: list[str] = field(default_factory=list)
    cites: list[str] = field(default_factory=list)
    adopted: bool | None = None # None = no report / not judged
    branch_id: int | None = None


@dataclass
class RunData:
    run: ar.Run
    nodes: list[NodeRec]
    invocations: list[dict]
    maximize: bool | None

    @property
    def improve(self) -> list[NodeRec]:
        return [n for n in self.nodes if n.stage == "improve"]

    @property
    def reported(self) -> list[NodeRec]:
        """Nodes whose prompt carried a report: improve nodes in D, the first draft in E, both in F."""
        return [n for n in self.nodes if n.mechanisms]

    @property
    def draft_reported(self) -> list[NodeRec]:
        return [n for n in self.nodes if n.stage == "draft" and n.mechanisms]

    def branch_best(self) -> dict:
        """branch_id -> (best valid metric, n nodes, n valid, has injected draft)."""
        out: dict = {}
        for n in self.nodes:
            b = out.setdefault(n.branch_id, {"best": None, "n": 0, "valid": 0, "injected": False})
            b["n"] += 1
            if n.stage == "draft" and n.mechanisms:
                b["injected"] = True
            if not n.buggy and isinstance(n.metric, (int, float)):
                b["valid"] += 1
                if b["best"] is None or (n.metric > b["best"] if self.maximize is not False else n.metric < b["best"]):
                    b["best"] = n.metric
        return out


def load_run(run: ar.Run, root: Path) -> RunData | None:
    jr = root / run.name / "logs" / "journal.json"
    if not jr.exists():
        return None
    try:
        j = json.loads(jr.read_text(errors="replace"))
    except json.JSONDecodeError:
        return None
    allnodes = j.get("nodes", [])
    by_id = {n["id"]: n for n in allnodes}
    n2p = j.get("node2parent", {})
    maximize = next((n["metric"]["maximize"] for n in allnodes
                     if isinstance(n.get("metric"), dict) and n["metric"].get("maximize") is not None), None)
    sign = -1.0 if maximize is False else 1.0

    def mval(n):
        m = (n or {}).get("metric")
        return m.get("value") if isinstance(m, dict) else None

    recs = []
    coded = [n for n in allnodes if n.get("stage") != "root" and n.get("code")]
    for i, n in enumerate(coded):
        pm, cm = mval(by_id.get(n2p.get(n["id"]))), mval(n)
        delta = sign * (cm - pm) if isinstance(pm, (int, float)) and isinstance(cm, (int, float)) else None
        rep = n.get("analogy_report") or ""
        recs.append(NodeRec(idx=i, step=int(n.get("step", i)), stage=str(n.get("stage")),
                            metric=cm, parent_metric=pm, buggy=bool(n.get("is_buggy")), delta=delta,
                            mechanisms=HEADING.findall(rep), cites=CITE.findall(rep),
                            branch_id=n.get("branch_id")))
        if rep:
            plan_words = set(re.findall(r"[a-z]{5,}", (n.get("plan") or "").lower()))
            recs[-1].adopted = any(len(title_words(t) & plan_words) >= 2 for t in recs[-1].mechanisms)
    inv = []
    idx = root / run.name / "logs" / "analogy" / "index.jsonl"
    if idx.exists():
        for line in idx.read_text(errors="replace").splitlines():
            if line.strip():
                try:
                    inv.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return RunData(run=run, nodes=recs, invocations=inv, maximize=maximize)


def apply_adoption(data: dict[str, RunData], path: Path) -> int:
    """Overwrite the word-overlap proxy with measure_adoption.py verdicts where they exist.
    Returns how many nodes got a judged verdict."""
    judged: dict[tuple[str, int], list[str]] = collections.defaultdict(list)
    with path.open() as fh:
        for row in csv.DictReader(fh):
            if row.get("judge_error"):
                continue
            judged[(row["run"], int(row["node"]))].append(row["verdict"])
    n = 0
    for name, rd in data.items():
        for rec in rd.nodes:
            vs = judged.get((name, rec.idx))
            if vs and rec.mechanisms:
                rec.adopted = any(v in ("full", "proxy") for v in vs)
                n += 1
    return n


# ══════════════════════════════════════════════════════════════════════════════════════
#  Figures
# ══════════════════════════════════════════════════════════════════════════════════════


def _style(ax, xlabel="", ylabel=""):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(C_GRID)
    ax.tick_params(colors=C_TEXT2, labelsize=8)
    ax.grid(axis="x", color=C_GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=8, color=C_TEXT2)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=8, color=C_TEXT2)


def _footer(fig, text, excluded=0):
    if excluded:
        text += f" · {excluded} invalid D run(s) excluded by analyze_runs.py"
    fig.text(0.01, 0.01, text, fontsize=7, color="#777777", ha="left", va="bottom")


def short(name: str) -> str:
    """20260903_010254_essay-ana-s49 -> 09-03 essay-ana-s49"""
    parts = name.split("_", 2)
    return f"{parts[0][4:6]}-{parts[0][6:8]} {parts[2]}" if len(parts) == 3 else name


def plot_funnel(task: str, rds: list[RunData], out: Path, excluded: int = 0) -> Path:
    stages = ["nodes", "improve", "with report\n(draft or improve)", "mechanisms", "valid child"]
    rows = []
    for rd in rds:
        rep = rd.reported
        rows.append([len(rd.nodes), len(rd.improve), len(rep), sum(len(n.mechanisms) for n in rep),
                     sum(1 for n in rep if not n.buggy)])
    ncol = min(4, len(rds))
    nrow = (len(rds) + ncol - 1) // ncol
    xmax = max(1, max(v[0] for v in rows))
    fig, axes = plt.subplots(nrow, ncol, figsize=(3.3 * ncol + 0.8, 2.9 * nrow + 0.8), squeeze=False)
    shades = ["#0f3f78", "#1c5aa8", "#2a78d6", "#6aa3e6", "#a9c8f0"]   # one hue, dark -> light
    for i, ax in enumerate(axes.flat):
        if i >= len(rds):
            ax.axis("off"); continue
        rd, vals = rds[i], rows[i]
        y = list(range(len(stages)))[::-1]
        ax.barh(y, vals, color=shades, height=0.62)
        for yy, v in zip(y, vals):
            ax.text(v + xmax * 0.02, yy, str(v), va="center", fontsize=8, color=C_TEXT2)
        ax.set_yticks(y)
        ax.set_yticklabels(stages if i % ncol == 0 else [""] * len(stages))
        ax.set_xlim(0, xmax * 1.22)
        ax.set_title(short(rd.run.name), fontsize=9)
        _style(ax)
    arms = "/".join(sorted({rd.run.arm for rd in rds}))
    fig.suptitle(f"{tname(task)} · arm {arms}: how often the analogy agent fired, and what came of it", fontsize=10)
    _footer(fig, "'with report' = nodes whose prompt carried a report (D: improve nodes; E: the first draft); "
                 "'valid child' = those nodes that ran without a bug; same x scale on every panel", excluded)
    fig.tight_layout(rect=(0, 0.04, 1, 0.94))
    p = out / f"{task}_analogy_funnel.png"
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p


def plot_transfer(task: str, rds: list[RunData], controls: dict[str, RunData | None],
                  judged: bool, out: Path, excluded: int = 0) -> Path | None:
    cols = []   # (label, values, n_buggy, color)
    a_vals, a_bug = [], 0
    for rd in rds:
        ctl = controls.get(rd.run.name)
        if ctl:
            a_vals += [n.delta for n in ctl.improve if n.delta is not None]
            a_bug += sum(1 for n in ctl.improve if n.buggy)
    cols.append(("A control\nimprove nodes", a_vals, a_bug, C_A))
    for flag, label, color in ((False, "report, not adopted", C_NOT), (True, "report, adopted", C_ADOPT)):
        vals, bug = [], 0
        for rd in rds:
            for n in rd.reported:
                if n.adopted is flag:
                    if n.delta is not None:
                        vals.append(n.delta)
                    bug += n.buggy
        cols.append((label, vals, bug, color))
    if not any(v for _, v, _, _ in cols):
        return None
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    rng = __import__("random").Random(0)
    for x, (label, vals, bug, color) in enumerate(cols):
        xs = [x + rng.uniform(-0.16, 0.16) for _ in vals]
        ax.scatter(xs, vals, s=34, color=color, alpha=0.85, edgecolor="white", linewidth=1, zorder=3)
        if vals:
            med = median(vals)
            ax.hlines(med, x - 0.3, x + 0.3, color=color, linewidth=2, zorder=4)
            ax.text(x, med, f"median {med:+.4f}", fontsize=7, color=C_TEXT2, ha="center", va="bottom",
                    bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.8))
    ax.axhline(0, color=C_MUTED, linewidth=1, zorder=1)
    ax.set_xlim(-0.6, len(cols) - 0.4)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels([f"{l}\nn={len(v)} · buggy {b}" for l, v, b, _ in cols], fontsize=8)
    _style(ax, ylabel="child − parent metric (sign-corrected, up = better)")
    ax.grid(axis="y", color=C_GRID, linewidth=0.8)
    ax.grid(axis="x", visible=False)
    ax.set_title(f"{tname(task)} · transfer at improve nodes: did following a suggestion help?", fontsize=10)
    src = ("adoption = measure_adoption.py LLM verdict" if judged else
           "adoption = word-overlap proxy (plan vs mechanism title); run measure_adoption.py for judged verdicts")
    _footer(fig, src + "\nbuggy children have no metric and are counted, not plotted", excluded)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    p = out / f"{task}_analogy_transfer.png"
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p


def retrieval_stats(rd: RunData, task: str) -> dict:
    cites = collections.Counter()
    titles = collections.Counter()
    for n in rd.reported:
        for c in n.cites:
            cites[c] += 1
        for t in n.mechanisms:
            titles[re.sub(r"[^a-z]+", " ", t.lower()).strip()] += 1
    fam = collections.Counter(venue_family(c) for c in cites.elements())
    total_c = sum(cites.values())
    queries = [q.lower() for inv in rd.invocations for q in inv.get("queries", [])]
    dw = DOMAIN_WORDS.get(task, ())
    return {
        "family": {f: fam.get(f, 0) / total_c if total_c else 0.0 for f in FAMILY_ORDER},
        "n_cites": total_c, "n_papers": len(cites),
        "top3_share": sum(c for _, c in cites.most_common(3)) / total_c if total_c else 0.0,
        "distinct_title_ratio": len(titles) / sum(titles.values()) if titles else 0.0,
        "n_queries": len(queries),
        "domain_query_share": (sum(1 for q in queries if any(w in q for w in dw)) / len(queries)) if queries and dw else None,
    }


def plot_retrieval(task: str, rds: list[RunData], stats: dict[str, dict], out: Path, excluded: int = 0) -> Path | None:
    if not any(stats[rd.run.name]["n_cites"] for rd in rds):
        return None
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 0.6 * len(rds) + 3.2),
                                   gridspec_kw={"width_ratios": [1.3, 1]})
    labels = [short(rd.run.name) for rd in rds]
    y = list(range(len(rds)))[::-1]
    left = [0.0] * len(rds)
    for fam in FAMILY_ORDER:
        vals = [stats[rd.run.name]["family"][fam] for rd in rds]
        ax1.barh(y, vals, left=left, color=FAMILY_COLOR[fam], height=0.6, label=fam,
                 edgecolor="white", linewidth=1.5)
        for yy, l, v in zip(y, left, vals):
            if v >= 0.12:
                ax1.text(l + v / 2, yy, f"{v:.0%}", ha="center", va="center", fontsize=7, color="white")
        left = [l + v for l, v in zip(left, vals)]
    ax1.set_yticks(y)
    ax1.set_yticklabels([f"{l}\n{stats[rd.run.name]['n_cites']} citations, {stats[rd.run.name]['n_papers']} papers"
                         for l, rd in zip(labels, rds)], fontsize=8)
    ax1.set_xlim(0, 1)
    ax1.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax1.legend(ncol=5, fontsize=7, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0))
    ax1.set_title("venue family of cited papers", fontsize=9, pad=22)
    _style(ax1)

    metrics = [("share of queries in competition vocabulary", "domain_query_share", C_NOT),
               ("distinct mechanism titles / mechanism blocks", "distinct_title_ratio", C_ADOPT),
               ("share of citations on the top-3 papers", "top3_share", C_MUTED)]
    h = 0.6 / len(metrics)
    for i, (label, key, color) in enumerate(metrics):
        vals = [stats[rd.run.name][key] for rd in rds]
        ys = [yy + 0.3 - h * (i + 0.5) for yy in y]
        ax2.barh(ys, [v or 0 for v in vals], height=h * 0.9, color=color, label=label)
        for yy, v in zip(ys, vals):
            ax2.text((v or 0) + 0.01, yy, "n/a" if v is None else f"{v:.0%}", va="center", fontsize=7, color=C_TEXT2)
    ax2.set_yticks(y)
    ax2.set_yticklabels([""] * len(y))
    ax2.set_xlim(0, 1.15)
    ax2.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax2.legend(fontsize=7, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0))
    ax2.set_title("query and report hygiene", fontsize=9, pad=50)
    _style(ax2)
    fig.suptitle(f"{tname(task)} · is the retrieval actually cross-domain?", fontsize=10)
    _footer(fig, "competition vocabulary list: DOMAIN_WORDS in plot_analogy.py · queries need logs/analogy/index.jsonl (fetch-run.sh >= 2026-09-03)", excluded)
    fig.tight_layout(rect=(0, 0.04, 1, 0.9))
    p = out / f"{task}_analogy_retrieval.png"
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p


def plot_cost(task: str, rds: list[RunData], out: Path, excluded: int = 0) -> Path | None:
    if not any(rd.invocations for rd in rds):
        return None
    fig, axes = plt.subplots(1, 3, figsize=(10, 0.7 * len(rds) + 2.2), sharey=True)
    y = list(range(len(rds)))[::-1]
    rng = __import__("random").Random(0)
    for ax, (label, key, scale) in zip(axes, (("turns", "turns", 1), ("input tokens (k)", "in_tokens", 1e-3),
                                             ("seconds", "seconds", 1))):
        for yy, rd in zip(y, rds):
            vals = [inv.get(key, 0) * scale for inv in rd.invocations]
            ax.scatter(vals, [yy + rng.uniform(-0.15, 0.15) for _ in vals], s=22, color=C_D,
                       alpha=0.7, edgecolor="white", linewidth=0.8, zorder=3)
            if vals:
                m = sum(vals) / len(vals)
                ax.vlines(m, yy - 0.3, yy + 0.3, color=C_D, linewidth=2, zorder=4)
                ax.text(m, yy - 0.42, f"mean {m:.1f}", fontsize=7, color=C_TEXT2, ha="center", va="top")
        ax.set_ylim(-0.8, len(rds) - 0.4)
        ax.set_xlim(left=0)
        ax.set_title(label, fontsize=9)
        _style(ax)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels([f"{short(rd.run.name)}\n{len(rd.invocations)} calls, "
                             f"{sum(1 for i in rd.invocations if i.get('ok'))} ok" for rd in rds], fontsize=8)
    fig.suptitle(f"{tname(task)} · cost per analogy-agent invocation (mean marked)", fontsize=10)
    _footer(fig, "one dot per invocation", excluded)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    p = out / f"{task}_analogy_cost.png"
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p


def plot_score(task: str, draws: list[dict], k: int, lower_better: bool, out: Path,
               arm: str = "D") -> tuple[Path | None, dict]:
    C_X = ARM_COLOR.get(arm, C_D)
    vals, labels, hollow = [], [], []
    for d in draws:
        a, b = d["scores"].get(arm), d["scores"].get("A")
        if a is None or b is None:
            continue
        vals.append((b - a) if lower_better else (a - b))
        labels.append(d["label"])
        hollow.append("A" in d["borrowed"] or arm in d["borrowed"])
    if not vals:
        return None, {}
    paired = [v for v, h in zip(vals, hollow) if not h]
    m, lo, hi, n = mean_ci(paired) if len(paired) >= 1 else (float("nan"),) * 3 + (0,)
    fig, ax = plt.subplots(figsize=(6.4, 0.45 * len(vals) + 2.0))
    y = list(range(len(vals)))[::-1]
    for yy, v, h, l in zip(y, vals, hollow, labels):
        ax.scatter([v], [yy], s=70, facecolor="white" if h else C_X, edgecolor=C_X, linewidth=2, zorder=3)
        ax.hlines(yy, 0, v, color=C_X, linewidth=1.2, alpha=0.6, zorder=2)
    ax.axvline(0, color=C_MUTED, linewidth=1)
    if n >= 2 and hi == hi:
        ax.axvspan(lo, hi, color=C_X, alpha=0.10, zorder=0)
        ax.axvline(m, color=C_X, linewidth=1.5, linestyle="--")
    ax.set_yticks(y)
    ax.set_yticklabels([l + ("  (unpaired)" if h else "") for l, h in zip(labels, hollow)], fontsize=8)
    _style(ax, xlabel=f"{arm} − A at K={k} (sign-corrected, right = analogy better)")
    ax.set_title(f"{tname(task)} · score effect of arm {arm} · paired n={n}"
                 + (f", mean {m:+.4f} [{lo:+.4f}, {hi:+.4f}]" if n >= 2 else ""), fontsize=9)
    _footer(fig, "hollow = baseline from another launch batch (excluded from the mean/CI) · CI is a 95% t interval")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    p = out / (f"{task}_analogy_score.png" if arm == "D" else f"{task}_analogy_score_{arm}.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p, {"n_paired": n, "mean": m, "lo": lo, "hi": hi, "k": k, "values": dict(zip(labels, vals))}


def plot_branches(task: str, rds: list[RunData], controls: dict[str, RunData | None],
                  out: Path, excluded: int = 0) -> Path | None:
    """Arm E: the branch grown from the injected first draft vs the run's other branches vs the
    paired A run's branches. Raw metric on x (same task, same metric); direction in the label."""
    rows = []   # (label, best, n, valid, kind)  kind: injected | other | control
    for rd in rds:
        if not rd.draft_reported:
            continue
        for bid, b in sorted(rd.branch_best().items(), key=lambda kv: (kv[0] is None, kv[0])):
            rows.append((f"{short(rd.run.name)} · branch {bid}", b["best"], b["n"], b["valid"],
                         "injected" if b["injected"] else "other"))
        ctl = controls.get(rd.run.name)
        if ctl:
            for bid, b in sorted(ctl.branch_best().items(), key=lambda kv: (kv[0] is None, kv[0])):
                rows.append((f"{short(ctl.run.name)} · branch {bid}", b["best"], b["n"], b["valid"], "control"))
    if not rows:
        return None
    maximize = next((rd.maximize for rd in rds if rd.maximize is not None), None)
    fig, ax = plt.subplots(figsize=(7.2, 0.32 * len(rows) + 2.0))
    y = list(range(len(rows)))[::-1]
    style = {"injected": (C_ADOPT, "injected first draft"), "other": (C_MUTED, "other branch, same run"),
             "control": (C_A, "paired A run")}
    seen = set()
    for yy, (label, best, n, valid, kind) in zip(y, rows):
        color, name = style[kind]
        if best is not None:
            ax.scatter([best], [yy], s=60 if kind == "injected" else 36, color=color, zorder=3,
                       edgecolor="white", linewidth=1, label=None if kind in seen else name)
        else:
            ax.text(0.01, yy, "no valid node", transform=ax.get_yaxis_transform(), fontsize=7, color=color, va="center")
            if kind not in seen:
                ax.scatter([], [], s=36, color=color, label=name)
        seen.add(kind)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{l}  ({v}/{n} valid)" for l, _, n, v, _ in rows], fontsize=7)
    ax.legend(fontsize=7, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3)
    _style(ax, xlabel="best validation metric in the branch" + (" (higher is better)" if maximize is not False else " (lower is better)"))
    ax.set_title(f"{tname(task)} · arm E: did the injected first draft grow a better branch?", fontsize=10, pad=24)
    _footer(fig, "validation metrics of one task only; each branch = one draft and its descendants", excluded)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    p = out / f"{task}_analogy_branches.png"
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p


# ══════════════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True, help="directory of fetched run directories")
    ap.add_argument("--out", required=True, help="analyze_runs.py output dir (has run_inventory.csv); charts go to <out>/charts/analogy")
    ap.add_argument("--scores", default=None, help="scores.csv (default: <runs>/scores.csv)")
    ap.add_argument("--adoption", default=None, help="adoption.csv from measure_adoption.py (default: <out>/adoption.csv if present)")
    ap.add_argument("--variant", default="capped", choices=("capped", "uncapped"))
    args = ap.parse_args()

    root, out = Path(args.runs).expanduser(), Path(args.out)
    inv = out / "run_inventory.csv"
    if not inv.exists():
        print(f"no {inv} — run analyze_runs.py --runs {root} --out {out} first"); return 1
    chart_dir = out / "charts" / "analogy"
    chart_dir.mkdir(parents=True, exist_ok=True)

    runs = load_inventory(inv)
    ARMS_HERE = ("D", "E", "F")
    d_runs = [r for r in runs if r.arm in ARMS_HERE]
    if not d_runs:
        print("no arm D/E/F runs in the inventory"); return 1
    data: dict[str, RunData] = {}
    for r in runs:
        if r.arm in ("A",) + ARMS_HERE:
            rd = load_run(r, root)
            if rd:
                data[r.name] = rd
    adoption = Path(args.adoption) if args.adoption else out / "adoption.csv"
    judged = 0
    if adoption.exists():
        judged = apply_adoption(data, adoption)
        print(f"adoption: {judged} node(s) carry measure_adoption.py verdicts from {adoption}")
    else:
        print("adoption: word-overlap proxy (no adoption.csv)")

    # pairing exactly as analyze_runs does it
    groups = ar.build_groups(runs)
    control: dict[str, RunData | None] = {}
    for g in groups:
        for arm in ARMS_HERE:
            if arm in g.arms:
                a = g.arms.get("A")
                control[g.arms[arm].name] = data.get(a.name) if a and "A" not in g.borrowed else None

    scores_path = Path(args.scores) if args.scores else root / "scores.csv"
    scores, lower_map = ar.load_scores(scores_path, args.variant) if scores_path.exists() else ({}, {})

    summary_rows = []
    written = []
    for task in sorted({r.task for r in d_runs}):
        rds = [data[r.name] for r in d_runs if r.task == task and r.name in data]
        if not rds:
            continue
        rds.sort(key=lambda rd: rd.run.name)
        stats = {rd.run.name: retrieval_stats(rd, task) for rd in rds}
        # Figures draw only runs analyze_runs.py judged valid (a crashed or disk-starved run says
        # nothing about the agent); the CSV below keeps every D run, with its verdict.
        ok = [rd for rd in rds if rd.run.verdict == "ok"]
        excluded = len(rds) - len(ok)
        if ok:
            written.append(plot_funnel(task, ok, chart_dir, excluded))
            written.append(plot_transfer(task, ok, control, judged > 0, chart_dir, excluded))
            written.append(plot_retrieval(task, ok, stats, chart_dir, excluded))
            written.append(plot_cost(task, ok, chart_dir, excluded))
            written.append(plot_branches(task, [rd for rd in ok if rd.run.arm in ("E", "F")], control, chart_dir, excluded))
        else:
            print(f"{task}: no valid D/E/F run ({excluded} excluded) — no figures")

        # score: <arm>-A draws from the same groups, one figure per arm present
        score_stats: dict[str, dict] = {}
        for arm in ARMS_HERE:
            draws = []
            for g in groups:
                if g.task != task or arm not in g.arms:
                    continue
                by_k = {a: scores.get(r.name, {}) for a, r in g.arms.items() if a in ("A", arm) and scores.get(r.name)}
                if len(by_k) == 2:
                    draws.append({"label": f"draw{g.draw} · seed {g.arms[arm].seed}", "by_k": by_k, "borrowed": g.borrowed})
            if draws:
                k = ar._matched_k(draws)
                if k is not None:
                    for d in draws:
                        d["scores"] = {a: s.get(k) for a, s in d["by_k"].items()}
                    p, score_stats[arm] = plot_score(task, draws, k, lower_map.get(task, False), chart_dir, arm=arm)
                    written.append(p)

        for rd in rds:
            st = stats[rd.run.name]
            rep = rd.reported
            adopted = [n for n in rep if n.adopted]
            def _mean(xs):
                xs = [x for x in xs if x is not None]
                return round(sum(xs) / len(xs), 5) if xs else ""
            ctl = control.get(rd.run.name)
            bb = rd.branch_best()
            inj = [b for b in bb.values() if b["injected"]]
            oth = [b["best"] for b in bb.values() if not b["injected"] and b["best"] is not None]
            sv = score_stats.get(rd.run.arm, {}).get("values", {})
            summary_rows.append({
                "run": rd.run.name, "task": task, "arm": rd.run.arm, "verdict": rd.run.verdict,
                "control_run": ctl.run.name if ctl else "",
                "n_nodes": len(rd.nodes), "n_improve": len(rd.improve), "n_with_report": len(rep),
                "draft_with_report": len(rd.draft_reported),
                "injected_branch_best": inj[0]["best"] if inj and inj[0]["best"] is not None else "",
                "injected_branch_valid": f"{inj[0]['valid']}/{inj[0]['n']}" if inj else "",
                "other_branches_best": (max(oth) if rd.maximize is not False else min(oth)) if oth else "",
                "n_invocations": len(rd.invocations), "n_invocations_ok": sum(1 for i in rd.invocations if i.get("ok")),
                "n_mechanisms": sum(len(n.mechanisms) for n in rep),
                "n_valid_children": sum(1 for n in rep if not n.buggy),
                "n_adopted": len(adopted), "adoption_source": "judged" if judged else "proxy",
                "delta_adopted_mean": _mean([n.delta for n in adopted]),
                "delta_not_adopted_mean": _mean([n.delta for n in rep if n.adopted is False]),
                "delta_control_mean": _mean([n.delta for n in ctl.improve]) if ctl else "",
                "n_cites": st["n_cites"], "n_papers": st["n_papers"],
                **{f"venue_{f.lower()}": round(st["family"][f], 3) for f in FAMILY_ORDER},
                "top3_share": round(st["top3_share"], 3), "distinct_title_ratio": round(st["distinct_title_ratio"], 3),
                "n_queries": st["n_queries"],
                "domain_query_share": "" if st["domain_query_share"] is None else round(st["domain_query_share"], 3),
                "mean_turns": _mean([i.get("turns") for i in rd.invocations]),
                "mean_in_tokens": _mean([i.get("in_tokens") for i in rd.invocations]),
                "mean_seconds": _mean([i.get("seconds") for i in rd.invocations]),
                "score_effect_vs_A": sv.get(next((l for l in sv if l.endswith(f"seed {rd.run.seed}")), ""), ""),
            })

    csv_path = out / "analogy_summary.csv"
    if summary_rows:
        with csv_path.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(summary_rows[0].keys()))
            w.writeheader()
            w.writerows(summary_rows)
    print(f"\n{len([p for p in written if p])} figure(s) in {chart_dir}:")
    for p in written:
        if p:
            print("  ", p.name)
    print(f"summary: {csv_path}")
    print(f"\n{'run':<38}{'arm':>4}{'impr':>5}{'rep':>5}{'mech':>5}{'adopt':>6}{'valid':>6}{'d_adopt':>9}{'d_ctl':>8}{'inj_best':>10}")
    for r in summary_rows:
        print(f"{short(r['run']):<38}{r['arm']:>4}{r['n_improve']:>5}{r['n_with_report']:>5}{r['n_mechanisms']:>5}"
              f"{r['n_adopted']:>6}{r['n_valid_children']:>6}{str(r['delta_adopted_mean']):>9}{str(r['delta_control_mean']):>8}"
              f"{str(r['injected_branch_best'])[:9]:>10}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
