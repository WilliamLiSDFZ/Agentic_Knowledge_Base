"""Per-task figures for the KB ablation. Driven by analyze_runs.py --charts.

Three figures per task, plus a grey appendix for superseded (pre-fix) runs:

    <task>_paired.png     one line per draw across the arms, at matched K
    <task>_effect.png     per-contrast differences, sign-corrected, with mean and 95% CI
    <task>_vs_k.png       score against ensemble size, one panel per draw
    _legacy_<task>.png    the same paired view for pre-2026-08-08 runs, greyed

── the reasoning behind these choices, since chart type is an analysis decision ────────
* A bar chart of per-arm means is the obvious thing and the wrong thing. The design is paired
  within a draw; a bar chart discards the pairing, and error bars drawn from between-draw
  variance make a null result look like a difference. Slope charts keep the pairing visible —
  a sign flip between draws shows up as crossing lines, which is precisely what essay does.
* Effects are SIGN-CORRECTED so up is always better, because jigsaw/essay maximise and
  lmsys/spooky minimise. Raw scores are never compared across tasks: different metrics, and
  pooling them would be meaningless.
* n is small (2-4 draws). The CI is a t interval and will usually contain zero; that is the
  honest picture, and the figure states n so nobody reads three points as a trend.
* Excluded runs are counted on every figure. A chart that quietly drops half the corpus is a
  cherry-pick even when every individual exclusion was justified.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt        # noqa: E402

# Two-sided t critical values at 95%, indexed by degrees of freedom. Hardcoded so the analysis
# does not depend on scipy, which is not installed and is a heavy dependency for one number.
_T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
        9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
        16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 25: 2.060, 30: 2.042}

ARMS = ("A", "B", "C", "D")
ARM_LABEL = {"A": "A  baseline", "B": "B  KB @ draft", "C": "C  KB @ draft+improve",
             "D": "D  analogy @ improve"}
ARM_COLOR = {"A": "#555555", "B": "#1f77b4", "C": "#d62728", "D": "#2ca02c"}
# B/C are the retired cold-start retrieval arms (historical runs); D is the improve-stage
# analogy agent. D is only ever launched against A, so it gets no B/C contrasts.
CONTRASTS = [("B", "A"), ("C", "A"), ("C", "B"), ("D", "A")]


def _t95(df: int) -> float:
    if df <= 0:
        return float("nan")
    if df in _T95:
        return _T95[df]
    keys = sorted(_T95)
    return _T95[min(keys, key=lambda k: abs(k - df))] if df < 30 else 1.96


def mean_ci(values: list[float]) -> tuple[float, float, float, int]:
    """Return (mean, lo, hi, n) for a two-sided 95% t interval. n<2 gives a nan interval."""
    n = len(values)
    if n == 0:
        return (float("nan"),) * 3 + (0,)
    m = sum(values) / n
    if n < 2:
        return m, float("nan"), float("nan"), n
    sd = math.sqrt(sum((v - m) ** 2 for v in values) / (n - 1))
    half = _t95(n - 1) * sd / math.sqrt(n)
    return m, m - half, m + half, n


def required_n(values: list[float], target: float) -> float:
    """Repeats needed to detect `target` at ~80% power, from the observed paired sd.

    Floored at 2: a "1 draw" answer is arithmetic, not advice — one draw yields no variance
    estimate and so can never establish anything. Callers should mark the result unstable when
    len(values) < 3, since an sd on 1 degree of freedom can be off by a large factor and this
    number scales with its square.
    """
    if len(values) < 2 or target <= 0:
        return float("nan")
    m = sum(values) / len(values)
    sd = math.sqrt(sum((v - m) ** 2 for v in values) / (len(values) - 1))
    return max(2.0, 8 * (sd / target) ** 2)


def _footer(fig, task: str, n_excluded: int, extra: str = "") -> None:
    note = f"{task} · {n_excluded} run(s) excluded by analyze_runs.py"
    if extra:
        note += f" · {extra}"
    fig.text(0.01, 0.01, note, fontsize=7, color="#777777", ha="left", va="bottom")


# ══════════════════════════════════════════════════════════════════════════════════════


def plot_paired(task: str, draws: list[dict], k: int, lower_better: bool,
                out: Path, n_excluded: int, legacy: bool = False) -> Path | None:
    """One line per draw across arms. Crossing lines = the effect changes sign between draws."""
    arms = [a for a in ARMS if any(a in d["scores"] for d in draws)]
    if len(arms) < 2 or not draws:
        return None

    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    xs = range(len(arms))
    for d in draws:
        ys = [d["scores"].get(a) for a in arms]
        pts = [(x, y) for x, y in zip(xs, ys) if y is not None]
        if len(pts) < 2:
            continue
        style = dict(color="#999999", alpha=0.6) if legacy else {}
        line, = ax.plot([p[0] for p in pts], [p[1] for p in pts], "-o", ms=6,
                        lw=1.8, label=d["label"], **style)
        # Mark a borrowed baseline: it comes from another launch batch, so that segment is an
        # unpaired comparison drawn on a paired chart. Saying so on the figure is the point.
        if "A" in d.get("borrowed", set()) and "A" in arms:
            ax.plot([0], [d["scores"]["A"]], "o", ms=12, mfc="none",
                    mec=line.get_color(), mew=1.6, zorder=1)

    ax.set_xticks(list(xs))
    ax.set_xticklabels([ARM_LABEL.get(a, a) for a in arms], fontsize=9)
    ax.set_ylabel(f"score at K={k}  ({'lower' if lower_better else 'higher'} is better)")
    ax.set_title(f"{task} — paired by draw" + ("  [SUPERSEDED CODE]" if legacy else ""),
                 fontsize=11)
    if lower_better:
        ax.invert_yaxis()          # so "up" always means "better" on every figure
    ax.grid(axis="y", alpha=0.25)
    ax.legend(fontsize=7.5, frameon=False, loc="best")
    if any("A" in d.get("borrowed", set()) for d in draws):
        ax.annotate("hollow ring = baseline borrowed from another batch (unpaired)",
                    xy=(0.5, -0.14), xycoords="axes fraction", ha="center",
                    fontsize=7, color="#a05000")
    _footer(fig, task, n_excluded)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    path = out / (f"_legacy_{task}.png" if legacy else f"{task}_paired.png")
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def plot_effects(task: str, draws: list[dict], k: int, lower_better: bool,
                 out: Path, n_excluded: int) -> tuple[Path | None, list[dict]]:
    """Per-contrast differences, sign-corrected so positive always means the later arm won."""
    stats = []
    for hi, lo in CONTRASTS:
        vals, labels, unpaired = [], [], False
        for d in draws:
            a, b = d["scores"].get(hi), d["scores"].get(lo)
            if a is None or b is None:
                continue
            diff = (b - a) if lower_better else (a - b)   # positive = `hi` is better
            vals.append(diff)
            labels.append(d["label"])
            if lo in d.get("borrowed", set()) or hi in d.get("borrowed", set()):
                unpaired = True
        if vals:
            m, lo_ci, hi_ci, n = mean_ci(vals)
            stats.append({"contrast": f"{hi}-{lo}", "values": vals, "labels": labels,
                          "mean": m, "lo": lo_ci, "hi": hi_ci, "n": n, "unpaired": unpaired})
    if not stats:
        return None, []

    fig, ax = plt.subplots(figsize=(7.4, 0.85 * len(stats) + 1.9))
    for i, s in enumerate(stats):
        y = len(stats) - 1 - i
        ax.scatter(s["values"], [y] * len(s["values"]), s=42, zorder=3,
                   color=ARM_COLOR.get(s["contrast"][0], "#1f77b4"), alpha=0.85)
        if s["n"] >= 2 and not math.isnan(s["lo"]):
            ax.plot([s["lo"], s["hi"]], [y - 0.22] * 2, lw=2.4, color="#333333", zorder=2)
        ax.plot([s["mean"]], [y - 0.22], "|", ms=16, mew=2.4, color="#333333", zorder=4)
        tag = f"{s['contrast']}  (n={s['n']}{', unpaired' if s['unpaired'] else ''})"
        ax.text(-0.02, y, tag, transform=ax.get_yaxis_transform(),
                ha="right", va="center", fontsize=9)

    ax.axvline(0, color="#cc0000", lw=1.2, ls="--", zorder=1)
    ax.set_yticks([])
    ax.set_ylim(-0.7, len(stats) - 0.3)
    ax.set_xlabel("improvement over the reference arm\n(positive = better, sign-corrected)",
                  fontsize=9)
    ax.set_title(f"{task} — effect at K={k}\ndots are draws, bar is 95% CI", fontsize=10.5)
    ax.grid(axis="x", alpha=0.25)

    zero_in = [s["contrast"] for s in stats
               if s["n"] >= 2 and not math.isnan(s["lo"]) and s["lo"] <= 0 <= s["hi"]]
    extra = (f"CI contains zero for {', '.join(zero_in)} — no detectable effect"
             if zero_in else "")
    _footer(fig, task, n_excluded, extra)
    fig.tight_layout(rect=(0.17, 0.06, 0.99, 1))
    path = out / f"{task}_effect.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path, stats


# Process metrics: what the search DID, as opposed to what it scored. These come from the run
# inventory, not from grading, so they are available without mle-bench and — more usefully — they
# are far less noisy than the score. The paired B-A difference in valid-node count clears zero at
# n=7, while no score contrast clears it at n=10.
#
# `better` is stated per metric because it is not uniform: more valid nodes is good, a higher bug
# rate is not, and for custom-architecture rate there is no "good" — it is a mechanism variable,
# so it is plotted raw and labelled.
PROCESS_METRICS = [
    ("n_valid", "valid solutions (count)", "higher = more"),
    ("valid_fraction", "valid fraction of nodes", "higher = more"),
    ("buggy_fraction", "buggy fraction of nodes", "lower = fewer failures"),
    ("custom_arch_fraction", "nodes defining their own architecture", "mechanism, no 'better'"),
]


def plot_process(task: str, draws: list[dict], out: Path, n_excluded: int) -> tuple:
    """Paired differences on process metrics, one panel per metric.

    Differences are plotted RAW, not sign-corrected, because "better" differs per metric and
    silently flipping some of them would make the figure unreadable. Each panel says its own
    direction.
    """
    stats: list[dict] = []
    for key, label, direction in PROCESS_METRICS:
        for hi, lo in CONTRASTS:
            vals, unpaired = [], False
            for d in draws:
                a, b = d["process"].get(hi), d["process"].get(lo)
                if a is None or b is None or a.get(key) is None or b.get(key) is None:
                    continue
                vals.append(a[key] - b[key])
                if {hi, lo} & set(d.get("borrowed", ())):
                    unpaired = True
            if len(vals) >= 2:
                m, lo_ci, hi_ci, n = mean_ci(vals)
                stats.append({"key": key, "label": label, "direction": direction,
                              "contrast": f"{hi}-{lo}", "values": vals, "mean": m,
                              "lo": lo_ci, "hi": hi_ci, "n": n, "unpaired": unpaired})
    if not stats:
        return None, []

    keys = [k for k, _, _ in PROCESS_METRICS if any(s["key"] == k for s in stats)]
    fig, axes = plt.subplots(len(keys), 1, figsize=(7.4, 2.1 * len(keys) + 1.0), squeeze=False)
    for ax, key in zip(axes[:, 0], keys):
        rows = [s for s in stats if s["key"] == key]
        for i, s in enumerate(rows):
            y = len(rows) - 1 - i
            ax.scatter(s["values"], [y] * len(s["values"]), s=38, zorder=3,
                       color=ARM_COLOR.get(s["contrast"][0], "#1f77b4"), alpha=0.85)
            if not math.isnan(s["lo"]):
                ax.plot([s["lo"], s["hi"]], [y - 0.2] * 2, lw=2.2, color="#333333", zorder=2)
            ax.plot([s["mean"]], [y - 0.2], "|", ms=14, mew=2.2, color="#333333", zorder=4)
            clears = not math.isnan(s["lo"]) and s["lo"] * s["hi"] > 0
            tag = f"{s['contrast']} (n={s['n']}{', unpaired' if s['unpaired'] else ''})"
            ax.text(-0.02, y, tag, transform=ax.get_yaxis_transform(),
                    ha="right", va="center", fontsize=8.5,
                    fontweight="bold" if clears else "normal")
        ax.axvline(0, color="#cc0000", lw=1.1, ls="--", zorder=1)
        ax.set_yticks([])
        ax.set_ylim(-0.6, len(rows) - 0.4)
        ax.set_title(f"{rows[0]['label']}   ({rows[0]['direction']})", fontsize=9.5, loc="left")
        ax.grid(axis="x", alpha=0.25)
    axes[-1, 0].set_xlabel("difference vs the reference arm", fontsize=9)

    cleared = [f"{s['contrast']} {s['key']}" for s in stats
               if not math.isnan(s["lo"]) and s["lo"] * s["hi"] > 0]
    extra = ("CI excludes zero: " + ", ".join(cleared)) if cleared else ""
    fig.suptitle(f"{task} — what the search did (not what it scored)", fontsize=11)
    _footer(fig, task, n_excluded, extra)
    fig.tight_layout(rect=(0.20, 0.04, 0.99, 0.96))
    path = out / f"{task}_process.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path, stats


def plot_vs_k(task: str, draws: list[dict], lower_better: bool,
              out: Path, n_excluded: int) -> Path | None:
    """Score against ensemble size. Flat lines mean fusion is doing nothing on this task."""
    usable = [d for d in draws if any(d["by_k"].get(a) for a in ARMS)]
    if not usable:
        return None
    fig, axes = plt.subplots(1, len(usable), figsize=(3.5 * len(usable) + 0.6, 3.4),
                             sharey=True, squeeze=False)
    for ax, d in zip(axes[0], usable):
        for arm in ARMS:
            series = d["by_k"].get(arm)
            if not series:
                continue
            ks = sorted(series)
            ax.plot(ks, [series[k] for k in ks], "-o", ms=4.5, lw=1.6,
                    color=ARM_COLOR[arm], label=arm)
        ax.set_title(d["label"], fontsize=9)
        ax.set_xlabel("ensemble size K")
        ax.grid(alpha=0.25)
        ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    axes[0][0].set_ylabel(f"score ({'lower' if lower_better else 'higher'} is better)")
    if lower_better:
        axes[0][0].invert_yaxis()
    axes[0][-1].legend(fontsize=8, frameon=False)
    fig.suptitle(f"{task} — score vs ensemble size", fontsize=11)
    _footer(fig, task, n_excluded)
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    path = out / f"{task}_vs_k.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path
