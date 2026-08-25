"""Step 1 of the run analysis: decide which experiment records are usable.

Reads every run directory under --runs and emits two tables:

    run_inventory.csv   one row per run, every extracted field plus its verdict
    groups.csv          one row per comparison group (task x seed x wiring)

Nothing here computes a result. The only job is to separate records that can carry a conclusion
from records that cannot, and to say why — because several runs are compromised in ways that are
invisible in the final numbers (API quota death mid-run, pod preemption, the pre-2026-08-08
prompt-injection bug).

    python scripts/analyze_runs.py --runs results/8.17/runs

Three verdicts, deliberately distinct:
    ok           usable
    invalid      the run itself is broken; the number it produced means nothing
    superseded   the run is fine but exercises code that has since been fixed, so it cannot be
                 pooled with current runs. Not a defect — a version boundary.

Tune behaviour by editing THRESHOLDS / TASKS below. Nothing downstream hardcodes a limit.

== measurement notes, learned the hard way =============================================
Two artifacts produced badly wrong answers in an earlier version of this script and are now
guarded against explicitly:

1. Matching rate limits with the regex ``\\b429\\b`` also matches the *millisecond field* of the
   log timestamp — ``[2026-08-16 07:09:06,429] WARNING: Node ... marked as buggy`` is not a rate
   limit. Roughly one log line in a thousand matches by accident, which manufactured 30-odd
   phantom 429s in every clean run and placed the "first 429" hours before the real one. Match
   the error signature (RE_RATELIMIT), never the bare number.

2. ``re.compile(r"^\\[...")`` without ``re.MULTILINE`` anchors to the start of the *string*, so
   ``findall`` over a whole log returns exactly one timestamp and every duration comes out 0.00.
   Zero-length spans then drove every starvation fraction to 0 and excluded most of the corpus.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
from dataclasses import asdict, dataclass, field, fields
from datetime import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))   # for plot_effects
from typing import Any

import yaml

# ══════════════════════════════════════════════════════════════════════════════════════
#  TUNABLES — every decision limit lives in this block
# ══════════════════════════════════════════════════════════════════════════════════════


@dataclass(frozen=True)
class Thresholds:
    # -- budget ------------------------------------------------------------------------
    expected_hours: float = 12.0
    """Nominal agent budget (run_single_task.sh TIME_LIMIT_SECS / 3600). Used as the denominator
    for every "how much of the run was productive" fraction, so that a run which only lasted
    five hours is penalised rather than scoring 100% of its own short life."""

    # -- API starvation ----------------------------------------------------------------
    min_usable_fraction: float = 0.60
    """Mark a run invalid when less than this share of the budget elapsed before the API died.

    Judgement call worth stating: the essay seed-43 arms hit a hard quota wall at 9.2 h, 9.7 h
    and 10.2 h of a 12 h budget (0.77 / 0.81 / 0.85). At 0.60 all three survive, on the view
    that they are equally truncated late runs rather than differentially crippled ones. Raise to
    0.90 to drop them; but max_group_usable_spread below is the rule that actually guards
    against *differential* starvation, which is the failure mode that biases a comparison."""

    max_ratelimit_errors: int = 50
    """Invalidate a run whose endpoint returned more rate-limit errors than this.

    Separate from min_usable_fraction, and stricter, because it targets a different defect. A run
    that gets rate-limited has had its effective compute budget cut by an amount nobody chose and
    that cannot be matched across arms — even when the cut lands late and the arms lose roughly
    equal time, the arms are no longer running the experiment that was designed.

    The exact value barely matters: this corpus is bimodal. The three 2026-08-16 essay runs have
    2991, 4341 and 4611 rate-limit errors; every other usable run has exactly zero. Anything
    between 1 and ~2000 gives the same answer. 50 is set where it is to tolerate a handful of
    transient retries without tolerating quota exhaustion.

    Note what this rule is NOT: it is not "drop the draw that disagreed". It is stated in terms
    of the run's own health, applies to every task equally, and fires on any future run that hits
    a quota wall. That distinction is the whole difference between a defensible exclusion and a
    cherry-pick, and it is worth keeping the rule this way even when the outcome is convenient.
    """

    max_group_usable_spread: float = 0.20
    """Invalidate a whole GROUP when its arms' usable fractions differ by more than this.

    A group where one arm generated for 10 h and another for 1 h cannot be compared however each
    arm scores on its own, because the confound is perfectly aligned with the treatment."""

    # -- truncation / preemption -------------------------------------------------------
    min_log_span_fraction: float = 0.50
    """Invalidate a run whose log spans less than this fraction of expected_hours.

    Loose on purpose. Log span is a LOWER BOUND on real duration, not the duration: the last line
    is usually ``REPL is executing code via subprocess``, after which the subprocess runs in
    silence for up to two hours and is killed mid-execution. Normal 12 h runs here log 10.3-11.7
    h, so anything under 6 h really did stop early."""

    # -- degenerate search (flags, not exclusions) -------------------------------------
    min_valid_candidates: int = 2
    """Flag runs producing fewer valid solutions than this. essay-base seed 42 produced exactly
    one, found seven minutes in — not provably invalid, definitely not a normal search."""

    max_buggy_fraction: float = 0.85

    # -- output quality ----------------------------------------------------------------
    check_submission_nan: bool = True
    """Scan ensemble CSVs for NaN. One jigsaw candidate had an incomplete id set which the fusion
    step padded with NaN, and every ensemble containing it inherited the holes."""

    max_csv_bytes_to_scan: int = 40 * 1024 * 1024

    # -- draw identity ------------------------------------------------------------------
    draw_gap_hours: float = 2.0
    """Runs of one task starting within this window are one draw (one launch batch).

    `agent.seed` is NOT a draw identifier and must not be used as one. It seeds numpy/torch
    inside the generated candidate code; it does not seed the agent's search, because the LLM
    is sampled and the model in use has no deterministic mode. Two runs at seed 43 are two
    independent draws, as the essay seed-43 pair demonstrated by flipping the sign of B-A.

    Keying groups on (task, seed) therefore silently collapses distinct draws and keeps only
    one of them — which would have discarded exactly the draw that contradicts. Observed
    separation in this corpus: arms within a draw start <= 8 minutes apart, consecutive draws
    are >= 20 hours apart, so 2 h separates them with a wide margin.
    """

    allow_cross_wiring_baseline: bool = True
    """Let a legacy-wiring arm A stand in as the baseline for a fixed-wiring draw.

    Verified, not assumed: MLEvolve's utils/verify_kb_injection.py section 1c-bis pulls the
    pre-fix source out of git and asserts that arm A's guidance string is byte-identical across
    the 2026-08-08 fix (4411 chars both ways) and that draft_agent's technique section does not
    fire without a KB. Arm A never retrieves, so the fix cannot reach it.

    This matters because jigsaw's fixed-wiring draws contain only arms B and C — without the
    borrowed baseline there is no A-vs-B contrast on jigsaw at all, which is the contrast the
    project is about. Borrowed baselines come from a different launch batch, so the contrast is
    UNPAIRED and is labelled as such wherever it is reported. Set False to forbid it.
    """


THRESHOLDS = Thresholds()


# Expected optimisation direction per competition. The agent infers this at startup via an LLM
# call; when that call fails it falls back to maximize=True, which on a log-loss task means
# twelve hours of searching in the wrong direction.
TASKS: dict[str, dict[str, Any]] = {
    "jigsaw-toxic-comment-classification-challenge":
        {"short": "jigsaw", "maximize": True,  "metric": "mean col-wise ROC AUC"},
    "learning-agency-lab-automated-essay-scoring-2":
        {"short": "essay",  "maximize": True,  "metric": "quadratic weighted kappa"},
    "lmsys-chatbot-arena":
        {"short": "lmsys",  "maximize": False, "metric": "multi-class log loss"},
    "spooky-author-identification":
        {"short": "spooky", "maximize": False, "metric": "multi-class log loss"},
    "openadmet":
        {"short": "openadmet", "maximize": False, "metric": "(custom)"},
}

# Some early runs encoded the arm in exp_id itself ("openadmet-kb"), which would otherwise split
# one competition into two incomparable tasks. The arm is recovered from the config regardless.
EXP_ID_ARM_SUFFIXES = ("-kbimp", "-kbfix", "-kb", "-base")


# -- log patterns ----------------------------------------------------------------------
LOG_TS = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", re.M)   # re.M is essential
RE_RATELIMIT = re.compile(r"Error code: 429|RateLimitError|insufficient_quota|model_cooldown")
RE_DIRECTION_DEFAULTED = re.compile(r"default value maximize", re.I)
RE_DIRECTION_OK = re.compile(r"metric direction validated: maximize=(True|False)", re.I)
RE_TASK_EXC = re.compile(r"Exception during task execution")

# A node that defines its own network or estimator rather than instantiating a known one. The
# hypothesis this measures: when the agent has no concrete technique to implement it invents an
# architecture, and bespoke architectures are likelier to fail to run. Baseline solutions in this
# corpus are full of things like `SparseResidualMultiLabelClassifier`.
RE_CUSTOM_ARCH = re.compile(r"^\s*class\s+\w+\((?:nn\.Module|torch\.nn\.Module|BaseEstimator)",
                            re.M)


# ══════════════════════════════════════════════════════════════════════════════════════
#  Parsing
# ══════════════════════════════════════════════════════════════════════════════════════


class _TagIgnoringLoader(yaml.SafeLoader):
    """config.yaml embeds ``!!python/object/apply:pathlib.PosixPath``, which SafeLoader rejects
    and which unsafe_load would happily execute."""


def _reconstruct(loader, suffix, node):
    """Rebuild pathlib paths; map every other unknown tag to None.

    Mapping *everything* to None is the obvious implementation and it is quietly lossy: the
    tagged fields here are `data_dir`, `dataset_dir`, `desc_file`, `log_dir` and `workspace_dir`,
    all stored as a tagged sequence of path components. Nothing in this script reads them today
    (`methodology_kb_path`, which decides the arm, is a plain string), but the same loader in
    utils/dump_injected.py needed `desc_file` and got None — which became `Path('.')`, whose
    `.exists()` is true, so every run died on `IsADirectoryError: Is a directory: '.'`.
    Reconstructing costs three lines and removes the trap.
    """
    if "pathlib" in suffix and isinstance(node, yaml.SequenceNode):
        parts = [str(p) for p in loader.construct_sequence(node)]
        return str(Path(*parts)) if parts else None
    return None


_TagIgnoringLoader.add_multi_constructor("", _reconstruct)


def _dig(d: Any, *keys: str, default: Any = None) -> Any:
    for k in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(k)
    return default if d is None else d


@dataclass
class Run:
    name: str = ""
    path: str = ""
    # identity
    task: str = ""
    exp_id: str = ""
    seed: Any = None
    arm: str = ""              # A = baseline | B = KB at draft | C = KB at draft+improve
    wiring: str = ""           # fixed | legacy
    retrieval: str = ""
    model: str = ""
    # timing
    started: str = ""
    log_last: str = ""
    log_span_h: float = 0.0
    node_span_h: float = 0.0
    # llm health
    n_ratelimit: int = 0
    first_ratelimit_h: float = -1.0    # hours into the run; -1 = never
    usable_h: float = 0.0              # productive time before the API died
    usable_fraction: float = 0.0       # usable_h / expected_hours, capped at 1
    direction_defaulted: bool = False
    direction_validated: Any = None
    # search
    n_nodes: int = 0
    n_buggy: int = 0
    n_valid: int = 0
    buggy_fraction: float = 0.0
    n_coded: int = 0
    custom_arch_fraction: float = 0.0
    best_metric: Any = None
    maximize_used: Any = None
    # outputs
    n_top_solutions: int = 0
    n_ensembles: int = 0
    wrapper_completed: bool = False
    nan_in_ensembles: bool = False
    n_real_crashes: int = 0
    # verdict
    verdict: str = "ok"        # ok | invalid | superseded
    reasons: str = ""
    flags: str = ""


def parse_log(run: Run, log: Path) -> None:
    if not log.exists():
        return
    text = log.read_text(errors="replace")

    stamps = LOG_TS.findall(text)
    t0 = None
    if stamps:
        run.started, run.log_last = stamps[0], stamps[-1]
        t0 = datetime.strptime(stamps[0], "%Y-%m-%d %H:%M:%S")
        t1 = datetime.strptime(stamps[-1], "%Y-%m-%d %H:%M:%S")
        run.log_span_h = round((t1 - t0).total_seconds() / 3600, 2)

    run.direction_defaulted = bool(RE_DIRECTION_DEFAULTED.search(text))
    m = RE_DIRECTION_OK.search(text)
    if m:
        run.direction_validated = m.group(1) == "True"

    # A traceback only indicates a broken run if it is not just the API refusing to serve. In the
    # quota-exhausted runs every single traceback is a 429; counting those as crashes would
    # report one problem twice.
    lines = text.splitlines()
    rl_lines = [ln for ln in lines if RE_RATELIMIT.search(ln)]
    run.n_ratelimit = len(rl_lines)
    for i, ln in enumerate(lines):
        if ln.startswith("Traceback (most recent call last)"):
            ctx = "\n".join(lines[max(0, i - 3):i])
            if RE_TASK_EXC.search(ctx) and not RE_RATELIMIT.search(ctx):
                run.n_real_crashes += 1

    if rl_lines and t0 is not None:
        m = LOG_TS.search(rl_lines[0])
        if m:
            tf = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
            run.first_ratelimit_h = round((tf - t0).total_seconds() / 3600, 2)

    # Productive time. Filled in by finalise_usable() once the outputs are known, because the
    # answer depends on whether the wrapper completed.
    run.usable_h = run.first_ratelimit_h if run.first_ratelimit_h >= 0 else run.log_span_h


def finalise_usable(run: Run) -> None:
    """Set usable_h / usable_fraction. Must run after parse_log AND parse_outputs.

    Three cases, and the middle one is easy to get wrong:

    1. The API was rate-limited -> productive time ends at the first real 429.
    2. No rate limiting AND the wrapper completed -> the run got its FULL budget, whatever the
       log says. Log span is a lower bound of unknown size: the last line is usually "REPL is
       executing code via subprocess", after which the subprocess runs silently for up to two
       hours and is killed by the 12 h timeout. Ensembles on disk prove the timeout fired and
       fusion ran afterwards, so the agent did have the whole budget.
    3. No rate limiting and the wrapper did NOT complete -> the log span is the best estimate.

    Using log span in case 2 caused a real misjudgement: the three clean 2026-08-17 essay reruns
    logged 11.3 / 8.6 / 9.4 h purely because their final silent executions differed in length,
    which read as a 0.23 spread in "productive time" and rejected the whole group for
    differential starvation that never happened.
    """
    if run.first_ratelimit_h >= 0:
        run.usable_h = run.first_ratelimit_h
    elif run.wrapper_completed:
        run.usable_h = THRESHOLDS.expected_hours
    else:
        run.usable_h = run.log_span_h
    run.usable_fraction = round(min(1.0, run.usable_h / THRESHOLDS.expected_hours), 3)


def parse_config(run: Run, cfg_path: Path) -> None:
    if not cfg_path.exists():
        return
    cfg = yaml.load(cfg_path.read_text(errors="replace"), Loader=_TagIgnoringLoader) or {}

    raw = str(cfg.get("exp_id") or "")
    for suf in EXP_ID_ARM_SUFFIXES:
        if raw.endswith(suf):
            raw = raw[: -len(suf)]
            break
    run.exp_id = raw
    run.task = TASKS.get(raw, {}).get("short", raw or "?")
    run.seed = _dig(cfg, "agent", "seed")
    run.retrieval = str(cfg.get("methodology_retrieval") or "")
    run.model = str(_dig(cfg, "agent", "code", "model") or "")

    cs = cfg.get("coldstart") or {}
    kb_on = bool(cfg.get("methodology_kb_path")) and run.retrieval == "lazy"
    run.arm = "A" if not kb_on else ("C" if bool(cs.get("inject_into_improve")) else "B")

    # `coldstart.methodology_text` was introduced by the 2026-08-08 fix that stopped retrieved
    # techniques being concatenated onto the pretrained-model guidance (which also defeated the
    # "None model" sentinel, so the arms differed by a whole extra prompt section). Its presence
    # is a structural marker of the code version — more reliable than comparing dates.
    run.wiring = "fixed" if "methodology_text" in cs else "legacy"


def parse_journal(run: Run, jr: Path) -> None:
    if not jr.exists():
        return
    try:
        j = json.loads(jr.read_text(errors="replace"))
    except json.JSONDecodeError:
        return
    nodes = j.get("nodes", j) if isinstance(j, dict) else j
    if not isinstance(nodes, list):
        return

    real = [n for n in nodes if n.get("stage") != "root"]
    run.n_nodes = len(real)
    run.n_buggy = sum(1 for n in real if n.get("is_buggy"))
    run.n_valid = sum(1 for n in real if n.get("is_valid"))
    run.buggy_fraction = round(run.n_buggy / len(real), 3) if real else 0.0

    coded = [n for n in real if n.get("code")]
    run.n_coded = len(coded)
    if coded:
        run.custom_arch_fraction = round(
            sum(1 for n in coded if RE_CUSTOM_ARCH.search(n["code"])) / len(coded), 3)

    ts = [n["ctime"] for n in real if isinstance(n.get("ctime"), (int, float))]
    if len(ts) > 1:
        run.node_span_h = round((max(ts) - min(ts)) / 3600, 2)

    vals, maxes = [], set()
    for n in real:
        m = n.get("metric")
        if isinstance(m, dict):
            if m.get("value") is not None:
                vals.append(m["value"])
            if m.get("maximize") is not None:
                maxes.add(bool(m["maximize"]))
    if len(maxes) == 1:
        run.maximize_used = maxes.pop()
    if vals:
        want_max = TASKS.get(run.exp_id, {}).get("maximize", run.maximize_used)
        run.best_metric = max(vals) if want_max else min(vals)


def parse_outputs(run: Run, ws: Path) -> None:
    ens_dir = ws / "ensembles_csv"
    ens = sorted(ens_dir.glob("*.csv")) if ens_dir.is_dir() else []
    run.n_ensembles = len(ens)
    ts = ws / "top_solution"
    run.n_top_solutions = len([p for p in ts.iterdir() if p.is_dir()]) if ts.is_dir() else 0

    # Fusion runs from run_single_task.sh AFTER the agent process exits, so ensembles on disk
    # prove the wrapper reached the end. Their absence alongside existing top_solution dirs means
    # the pod died before the wrapper got there.
    run.wrapper_completed = run.n_ensembles > 0

    if THRESHOLDS.check_submission_nan:
        for f in ens:
            if f.stat().st_size > THRESHOLDS.max_csv_bytes_to_scan:
                continue
            if re.search(r"(^|,)(nan|NaN|NAN)(,|$)", f.read_text(errors="replace"), re.M):
                run.nan_in_ensembles = True
                break


# ══════════════════════════════════════════════════════════════════════════════════════
#  Rules:  (code, verdict-if-hit, predicate)
#          verdict "" means a soft flag: recorded, does not exclude
# ══════════════════════════════════════════════════════════════════════════════════════

RULES: list[tuple[str, str, Any]] = [
    ("no_journal", "invalid",
     lambda r: r.n_nodes == 0),
    # Two rules for one threshold, so the reason names the cause. A short run with zero rate
    # limits was not starved of API — it was cut off — and mislabelling that hides which
    # problem needs fixing.
    ("ratelimit_truncated", "invalid",
     lambda r: r.n_ratelimit > THRESHOLDS.max_ratelimit_errors),
    ("api_starved", "invalid",
     lambda r: r.n_ratelimit > 0 and r.usable_fraction < THRESHOLDS.min_usable_fraction),
    ("insufficient_runtime", "invalid",
     lambda r: r.n_ratelimit == 0 and r.usable_fraction < THRESHOLDS.min_usable_fraction),
    ("terminated_early", "invalid",
     lambda r: not r.wrapper_completed and r.n_top_solutions > 0),
    ("log_truncated", "invalid",
     lambda r: r.log_span_h < THRESHOLDS.expected_hours * THRESHOLDS.min_log_span_fraction),
    ("crashed", "invalid",
     lambda r: r.n_real_crashes > 0),
    ("metric_direction_defaulted", "invalid",
     lambda r: r.direction_defaulted),
    ("metric_direction_wrong", "invalid",
     lambda r: (r.maximize_used is not None and r.exp_id in TASKS
                and r.maximize_used != TASKS[r.exp_id]["maximize"])),
    ("no_submission", "invalid",
     lambda r: r.n_ensembles == 0 and r.n_top_solutions == 0),

    ("legacy_injection_wiring", "superseded",
     lambda r: r.arm in ("B", "C") and r.wiring == "legacy"),

    ("nan_submission", "",
     lambda r: r.nan_in_ensembles),
    ("few_valid_candidates", "",
     lambda r: r.n_valid < THRESHOLDS.min_valid_candidates),
    ("mostly_buggy", "",
     lambda r: r.buggy_fraction > THRESHOLDS.max_buggy_fraction),
    ("ratelimit_minor", "",
     lambda r: 0 < r.n_ratelimit <= THRESHOLDS.max_ratelimit_errors),
]


def apply_rules(run: Run, manual: dict[str, str]) -> None:
    invalid: list[str] = []
    superseded: list[str] = []
    soft: list[str] = []
    for code, verdict, pred in RULES:
        try:
            hit = bool(pred(run))
        except Exception:
            hit = False
        if not hit:
            continue
        {"invalid": invalid, "superseded": superseded, "": soft}[verdict].append(code)

    # A manual entry beginning with "flag:" records the problem without excluding the run —
    # for known confounds you have decided to live with. The caveat still travels into
    # run_inventory.csv and onto the figures, so including the run is a visible choice rather
    # than an omission.
    note = manual.get(run.name)
    if note:
        (soft if note.strip().lower().startswith("flag:") else invalid).append(
            f"manual:{note.split(':', 1)[-1].strip() if note.strip().lower().startswith('flag:') else note}")

    run.verdict = "invalid" if invalid else ("superseded" if superseded else "ok")
    run.reasons = ";".join(invalid + superseded)
    run.flags = ";".join(soft)


# ══════════════════════════════════════════════════════════════════════════════════════
#  Groups
# ══════════════════════════════════════════════════════════════════════════════════════


@dataclass
class Group:
    task: str
    draw: int                  # 1-based launch batch within the task
    started: str = ""          # earliest arm start, identifies the batch to a human
    wiring: str = ""
    seeds: str = ""            # metadata only; see Thresholds.draw_gap_hours
    arms: dict[str, Run] = field(default_factory=dict)
    borrowed: set = field(default_factory=set)   # arms taken from another draw
    usable: bool = False
    reasons: str = ""

    @property
    def key(self) -> str:
        return f"{self.task}/draw{self.draw}"


def _cluster_draws(runs: list[Run]) -> list[Group]:
    """Split one task's runs into launch batches by start time. See Thresholds.draw_gap_hours."""
    dated = sorted((r for r in runs if r.started), key=lambda r: r.started)
    groups: list[Group] = []
    prev: datetime | None = None
    for r in dated:
        t = datetime.strptime(r.started, "%Y-%m-%d %H:%M:%S")
        if prev is None or (t - prev).total_seconds() / 3600 > THRESHOLDS.draw_gap_hours:
            groups.append(Group(task=r.task, draw=len(groups) + 1,
                                started=r.started, wiring=r.wiring))
        g = groups[-1]
        # Two runs of the same arm inside one batch means a relaunch; keep the later.
        prev_run = g.arms.get(r.arm)
        if prev_run is None or r.name > prev_run.name:
            g.arms[r.arm] = r
        prev = t
    return groups


def build_groups(runs: list[Run]) -> list[Group]:
    by_task: dict[str, list[Run]] = {}
    for r in runs:
        if r.task and r.task != "?" and r.verdict != "invalid":
            by_task.setdefault(r.task, []).append(r)

    groups: list[Group] = []
    for task, rs in by_task.items():
        groups.extend(_cluster_draws(rs))

    # Borrow a baseline for draws that have KB arms but no control. Only arm A, only when the
    # donor is itself usable, and only from the same task. Recorded in `borrowed` so every
    # downstream report can mark the contrast unpaired.
    if THRESHOLDS.allow_cross_wiring_baseline:
        for task in by_task:
            tg = sorted((g for g in groups if g.task == task), key=lambda x: x.draw)
            # Each donor may be spent ONCE. Reusing one baseline for two draws would enter the
            # same number twice as if it were two independent observations, shrinking the
            # variance estimate and inventing significance.
            pool = [g.arms["A"] for g in tg if "A" in g.arms and g.arms["A"].verdict == "ok"]
            needy = [g for g in tg if "A" not in g.arms and ({"B", "C"} & set(g.arms))]

            # Prefer the donor whose seed matches, purely to preserve the original pairing
            # intent; seed carries no statistical meaning here (see draw_gap_hours). Anything
            # left over is matched in draw order.
            for g in needy:
                want = {r.seed for r in g.arms.values() if r.seed is not None}
                match = next((d for d in pool if d.seed in want), None)
                if match is None and pool:
                    match = pool[0]
                if match is None:
                    continue
                pool.remove(match)
                g.arms["A"] = match
                g.borrowed.add("A")

    for g in groups:
        g.seeds = ",".join(sorted({str(r.seed) for r in g.arms.values() if r.seed is not None}))
        why = []
        if len(g.arms) < 2:
            why.append(f"only_{len(g.arms)}_arm")

        bad = [f"{a}={r.verdict}({r.reasons})"
               for a, r in sorted(g.arms.items()) if r.verdict != "ok"]
        if bad:
            why.append("arm_" + ",".join(bad))

        # differential starvation: the confound that aligns with the treatment. Skip borrowed
        # arms — they come from a different batch, so a spread against them says nothing about
        # whether THIS batch was starved unevenly.
        us = [r.usable_fraction for a, r in g.arms.items() if a not in g.borrowed]
        if len(us) > 1 and (max(us) - min(us)) > THRESHOLDS.max_group_usable_spread:
            why.append(f"usable_spread={max(us) - min(us):.2f}"
                       f">{THRESHOLDS.max_group_usable_spread}")

        g.reasons = ";".join(why)
        g.usable = not why
    return sorted(groups, key=lambda g: (g.task, g.draw))


# ══════════════════════════════════════════════════════════════════════════════════════
#  Scores + charts
# ══════════════════════════════════════════════════════════════════════════════════════


def load_scores(path: Path, variant: str = "capped") -> tuple[dict, dict]:
    """Read scores.csv from MLEvolve/utils/grade_all.py.

    Returns (by_run_k, lower_better_by_task) where by_run_k[run][k] = score. Scores cannot be
    computed here: mle-bench's private answers only exist on the cluster.

    `variant` selects which fusion the figures describe — "capped" is the 9 h serial-time budget
    the runs were originally ensembled under, "uncapped" is the replay from utils/refuse_all.py.
    Never mix them: a capped arm and an uncapped arm are two different systems. Files written
    before the variant column existed are all capped, so an absent column means "capped".
    """
    by_run: dict[str, dict[int, float]] = {}
    lower: dict[str, bool] = {}
    with path.open() as fh:
        for row in csv.DictReader(fh):
            if not row.get("score"):
                continue
            if row.get("variant", "capped") != variant:
                continue
            by_run.setdefault(row["run"], {})[int(row["k"] or 0)] = float(row["score"])
            comp = row.get("competition", "")
            short = TASKS.get(comp, {}).get("short", comp)
            if row.get("lower_better") not in (None, ""):
                lower[short] = bool(int(row["lower_better"]))
            elif short in TASKS:
                lower.setdefault(short, not TASKS[short.replace(short, comp)]["maximize"]
                                 if comp in TASKS else False)
    return by_run, lower


def _matched_k(draws: list[dict]) -> int | None:
    """Largest K present in every arm of every draw. Comparing across K measures how many
    candidates each arm could afford to fuse, not whether the knowledge base helped."""
    per_arm = [set(s) for d in draws for s in d["by_k"].values() if s]
    return max(set.intersection(*per_arm)) if per_arm and set.intersection(*per_arm) else None


def _process_of(r: Run) -> dict:
    """Per-run process metrics. Deliberately independent of grading."""
    return {"n_valid": r.n_valid,
            "valid_fraction": (r.n_valid / r.n_nodes) if r.n_nodes else None,
            "buggy_fraction": r.buggy_fraction,
            "custom_arch_fraction": r.custom_arch_fraction}


def build_process_charts(groups: list[Group], runs: list[Run], out: Path) -> tuple[list[str], list]:
    """Figures for what the search did. No scores needed — these read the inventory only, which
    is why they still render when mle-bench grading is unavailable."""
    import plot_effects as pe

    out.mkdir(parents=True, exist_ok=True)
    written, all_stats = [], []
    for task in sorted({g.task for g in groups}):
        draws = [{"label": f"draw{g.draw}",
                  "process": {a: _process_of(r) for a, r in g.arms.items()},
                  "borrowed": g.borrowed}
                 for g in groups if g.task == task and g.usable and g.wiring != "legacy"]
        if len(draws) < 2:
            continue
        n_excluded = sum(1 for r in runs if r.task == task and r.verdict != "ok")
        p, stats = pe.plot_process(task, draws, out, n_excluded)
        if p:
            written.append(p.name)
            all_stats.append((task, stats))
    return written, all_stats


def build_charts(groups: list[Group], scores: dict, lower_map: dict,
                 runs: list[Run], out: Path) -> list[str]:
    import plot_effects as pe

    out.mkdir(parents=True, exist_ok=True)
    lines: list[str] = ["# KB ablation — per-task effects", "",
                        "Scores are graded against mle-bench private answers "
                        "(`MLEvolve/utils/grade_all.py`). The agent's own validation metric is "
                        "not used anywhere here: arms hold out different data, so it is not "
                        "comparable across arms.", ""]
    written: list[str] = []

    tasks = sorted({g.task for g in groups})
    for task in tasks:
        lower = bool(lower_map.get(task, not TASKS.get(
            next((k for k, v in TASKS.items() if v["short"] == task), ""), {}
        ).get("maximize", True)))
        n_excluded = sum(1 for r in runs if r.task == task and r.verdict != "ok")

        for legacy in (False, True):
            sel = [g for g in groups if g.task == task
                   and (g.wiring == "legacy") == legacy
                   and (g.usable or legacy) and len(g.arms) >= 2]
            draws = []
            for g in sel:
                by_k = {a: scores.get(r.name, {}) for a, r in g.arms.items()
                        if scores.get(r.name)}
                if len(by_k) < 2:
                    continue
                draws.append({"label": f"draw{g.draw} ({g.started[:10]}, seed {g.seeds})",
                              "by_k": by_k, "borrowed": g.borrowed})
            if not draws:
                continue

            k = _matched_k(draws)
            if k is None:
                lines += [f"## {task}" + (" (superseded)" if legacy else ""), "",
                          "No ensemble size is shared by every arm, so no fair comparison is "
                          "possible from the ensembles alone.", ""]
                continue
            for d in draws:
                d["scores"] = {a: s.get(k) for a, s in d["by_k"].items() if k in s}

            p = pe.plot_paired(task, draws, k, lower, out, n_excluded, legacy=legacy)
            if p:
                written.append(p.name)
            if legacy:
                continue

            pe_path, stats = pe.plot_effects(task, draws, k, lower, out, n_excluded)
            if pe_path:
                written.append(pe_path.name)
            vk = pe.plot_vs_k(task, draws, lower, out, n_excluded)
            if vk:
                written.append(vk.name)

            lines += [f"## {task}", "",
                      f"{len(draws)} usable draw(s), compared at K={k}. "
                      f"{n_excluded} run(s) excluded.", "",
                      "| contrast | n | mean | 95% CI | signs | verdict |",
                      "|---|---:|---:|---|---|---|"]
            for s in stats:
                signs = "".join("+" if v > 0 else "-" for v in s["values"])
                ci = ("—" if s["n"] < 2 or math.isnan(s["lo"])
                      else f"[{s['lo']:+.5f}, {s['hi']:+.5f}]")
                if s["n"] < 2:
                    verdict = "n=1, no interval"
                elif s["lo"] <= 0 <= s["hi"]:
                    verdict = "**CI contains zero — no detectable effect**"
                else:
                    verdict = "CI excludes zero"
                if s["unpaired"]:
                    verdict += " (unpaired)"
                lines.append(f"| {s['contrast']} | {s['n']} | {s['mean']:+.5f} | {ci} "
                             f"| {signs} | {verdict} |")
            lines.append("")
            for s in stats:
                if s["n"] >= 2:
                    need = pe.required_n(s["values"], 0.005)
                    if not math.isnan(need):
                        # An sd from 2 draws has 1 degree of freedom and the sample-size
                        # estimate scales with its square, so it can be wrong by an order of
                        # magnitude. Quote it, but never let it read as a firm budget.
                        caveat = ("  *(from n=2 — sd has 1 df, treat as a rough order of "
                                  "magnitude only)*" if s["n"] < 3 else "")
                        lines.append(f"- `{s['contrast']}`: to detect 0.005 at ~80% power needs "
                                     f"**{need:.0f} draws** ({need * 2 * 12:.0f} GPU-hours "
                                     f"at 12 h/run, 2 arms).{caveat}")
            lines.append("")

    (out / "summary.md").write_text("\n".join(lines))
    written.append("summary.md")
    return written


# ══════════════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True, help="directory containing the run folders")
    ap.add_argument("--out", default=None, help="output dir (default: parent of --runs)")
    ap.add_argument("--manual-exclusions", default=None,
                    help="YAML mapping run name -> reason, for problems that leave no trace in "
                         "the run directory (e.g. the essay seed-42 cache-warm race)")
    ap.add_argument("--scores", default=None,
                    help="scores.csv from MLEvolve/utils/grade_all.py, produced on the cluster "
                         "(private answers are not available locally). fetch-run.sh writes it.")
    ap.add_argument("--variant", choices=("capped", "uncapped"), default="capped",
                    help="which fusion to analyse (default capped = the original 9 h budget). "
                         "Never compare arms across variants; they are different systems.")
    ap.add_argument("--charts", nargs="?", const="charts", default=None,
                    help="write per-task figures + summary.md into this subdirectory of --out")
    args = ap.parse_args()

    root = Path(args.runs)
    out = Path(args.out) if args.out else root.parent
    out.mkdir(parents=True, exist_ok=True)
    manual: dict[str, str] = {}
    if args.manual_exclusions and Path(args.manual_exclusions).exists():
        manual = yaml.safe_load(Path(args.manual_exclusions).read_text()) or {}

    runs: list[Run] = []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        r = Run(name=d.name, path=str(d))
        parse_log(r, d / "logs" / "MLEvolve.log")
        parse_config(r, d / "logs" / "config.yaml")
        parse_journal(r, d / "logs" / "journal.json")
        parse_outputs(r, d / "workspace")
        finalise_usable(r)                 # needs both the log and the outputs
        apply_rules(r, manual)
        runs.append(r)

    inv = out / "run_inventory.csv"
    with inv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[f.name for f in fields(Run)])
        w.writeheader()
        for r in runs:
            w.writerow(asdict(r))

    groups = build_groups(runs)
    grp = out / "groups.csv"
    with grp.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["group", "task", "draw", "started", "wiring", "seeds",
                    "arms", "borrowed", "usable", "reasons"])
        for g in groups:
            w.writerow([g.key, g.task, g.draw, g.started, g.wiring, g.seeds,
                        "".join(sorted(g.arms)), "".join(sorted(g.borrowed)),
                        g.usable, g.reasons])

    # -- report ------------------------------------------------------------------------
    n_ok = sum(1 for r in runs if r.verdict == "ok")
    n_sup = sum(1 for r in runs if r.verdict == "superseded")
    print(f"\n{len(runs)} runs: {n_ok} ok, {n_sup} superseded, "
          f"{len(runs) - n_ok - n_sup} invalid\n")

    print(f"{'run':<44}{'task':>10}{'arm':>4}{'seed':>5}{'wire':>7}"
          f"{'logh':>6}{'use%':>6}{'valid':>6}  verdict")
    print("-" * 132)
    for r in runs:
        v = "ok" if r.verdict == "ok" else f"{r.verdict}: {r.reasons}"
        print(f"{r.name:<44}{r.task:>10}{r.arm:>4}{str(r.seed):>5}{r.wiring:>7}"
              f"{r.log_span_h:>6.1f}{r.usable_fraction * 100:>5.0f}%{r.n_valid:>6}  {v}"
              + (f"  [{r.flags}]" if r.flags else ""))

    print(f"\n{'group':<20}{'started':>18}{'wiring':>8}{'seeds':>8}{'arms':>6}"
          f"{'borrow':>8}{'usable':>8}  reasons")
    print("-" * 132)
    for g in groups:
        print(f"{g.key:<20}{g.started:>18}{g.wiring:>8}{g.seeds:>8}"
              f"{''.join(sorted(g.arms)):>6}{''.join(sorted(g.borrowed)) or '-':>8}"
              f"{str(g.usable):>8}  {g.reasons}")

    ok = [g for g in groups if g.usable]
    print(f"\n{len(ok)} of {len(groups)} comparison groups usable")
    for g in ok:
        detail = "  ".join(f"{a}:{r.usable_fraction:.2f}" for a, r in sorted(g.arms.items()))
        note = (f"   [baseline borrowed from another batch -> A-contrasts are UNPAIRED]"
                if g.borrowed else "")
        print(f"    {g.key:<20} arms={''.join(sorted(g.arms))}   usable_frac {detail}{note}")

    print(f"\nwrote {inv}\nwrote {grp}")

    if args.charts:
        chart_dir = out / (args.charts if args.variant == "capped"
                           else f"{args.charts}_{args.variant}")
        # Process figures first: they need no grading, so they must not be gated behind --scores.
        proc, proc_stats = build_process_charts(groups, runs, chart_dir)
        if proc:
            print(f"\nprocess figures (no grading needed) -> {chart_dir}/")
            for w in proc:
                print(f"    {w}")
            for task, stats in proc_stats:
                for st in stats:
                    if not math.isnan(st["lo"]) and st["lo"] * st["hi"] > 0:
                        print(f"    {task} {st['contrast']} {st['key']}: "
                              f"{st['mean']:+.3f} [{st['lo']:+.3f}, {st['hi']:+.3f}] "
                              f"n={st['n']}  <- CI excludes zero")
        if not args.scores:
            print("\n--charts needs --scores: mle-bench's private answers only exist on the\n"
                  "cluster, so this script cannot grade anything itself. Run fetch-run.sh\n"
                  "(which grades and downloads scores.csv), or on the pod:\n"
                  "  python utils/grade_all.py --runs /workspace/MLEvolve/runs -o scores.csv")
        elif not Path(args.scores).exists():
            print(f"\n--scores file not found: {args.scores}")
        else:
            scores, lower_map = load_scores(Path(args.scores), args.variant)
            missing = [r.name for r in runs if r.verdict == "ok" and r.name not in scores]
            if missing:
                print(f"\nWARNING: {len(missing)} usable run(s) have no score in "
                      f"{args.scores} — regrade, or the charts are drawn from a stale file:")
                for m in missing[:8]:
                    print(f"    {m}")
            written = build_charts(groups, scores, lower_map, runs, chart_dir)
            print(f"\nwrote {len(written)} file(s) to {chart_dir}/")
            for w in written:
                print(f"    {w}")

    if not manual:
        print("\nNo manual exclusions supplied. At least one known problem leaves NO trace in\n"
              "the run directories: the essay seed-42 cache-warm race, where arms B and C\n"
              "extracted papers concurrently and may have held different technique sets.\n"
              "Record it in a YAML file and pass --manual-exclusions, or it passes as usable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
