# Update Log

A running record of notable changes to this project. Newest entries on top.

---

## 2026-09-02 — Retrieval moves to the improve stage and becomes an analogy agent (arm D)

Implements `docs/analogy_bm25_agent_design.md` (from Peijia's 8/31–9/1 direction, the
structural-analogy memo and arXiv 2605.11258). Old retrieval **deleted**, not switched off — the
change is on a branch, and `git log` keeps the code that produced every B/C result.

### What changed, in one paragraph

Retrieval used to happen once, at cold start, with the competition description as the query;
arm C then re-injected that same static block at every improve node (same digest, 9 times, in
`essay-kbimp-s47`). Now nothing is retrieved at draft time. At every improve node an agent in
MLEvolve (`engine/analogy/`) reads the node's own search state — plan, code summary, execution
summary, metric, output tail, sibling attempts, branch trajectory — diagnoses ≤3 bottlenecks of
the *current methodology*, rewrites each as 3–6-term queries in the vocabulary other subfields
use for the same relational structure, searches this repo's paper corpus with BM25, reads
abstracts, and submits ≤3 mechanisms mapped back as concrete interventions. **The LLM does the
analogy; BM25 does the lookup.** The corpus is `output/paper_corpus/records.jsonl` — title, tldr
and abstract, no preprocessing, no embeddings (`scripts/6_build_paper_corpus.py`, seconds).

### Why the probe number matters

`scripts/probe_analogy.py` runs the memo's ten Kaggle cases as two query styles. On the local
12.8k corpus, short mechanism-term queries hit the expected mechanism family far more often than
the memo's structural sentences (7/10 vs 3/10 on a strict manual read; 9/10 vs 7/10 by keyword).
That gap is why the agent prompt insists on short queries in *other* subfields' words and on
re-wording rather than adding words. The persistent miss is test-time augmentation (Jigsaw):
abstracts rarely name it, so the agent must reach it via "consistency regularization".

### Hard rules in the code

| rule | why |
|---|---|
| a mechanism may cite only paper ids returned by `search_papers` in that episode; others are dropped at validation | no hallucinated citations — the report is only ever as real as the corpus |
| every failure path returns an empty report; `_inject_analogy` imports inside its try | this project's rule that a diagnostic must not be able to end a 12 h run |
| report ≤ `analogy.report_char_budget` (8k chars), whole mechanisms only | the improve prompt is already long; the old C arm injected 48k |
| `SearchNode.analogy_report` is a declared dataclass field | so `journal.json` carries what each node saw — `measure_adoption.py` reads it per node |

### What no longer exists, and what that does to the experiments

The paired-arm machinery built around *identical knowledge across arms* — `query_cache/`,
`filter_cache/`, `prepare-task.sh`'s PROBE/WARM/VERIFY phases, `verify_filter_cache.py`,
`dump_injected.py`, the "same digest in B and C" check — has no counterpart. The agent's input is
the run's own trajectory, different in every run by construction, so there is nothing to share
and nothing to race on. The comparison is A vs D, paired by draw as before.

Removed: MLEvolve `engine/coldstart/methodology_agent.py`, `ondemand.py`, the methodology branch
of `knowledge.py`, draft-time injection, `coldstart.inject_into_improve`, 23 top-level retrieval
keys, `utils/verify_kb_injection.py`, `verify_filter_cache.py`, `dump_injected.py`; this repo's
`6_build_abstract_index.py`, `build_retrieval_index.py`, `probe_retrieval.py` and the
`--build-index` step. Added: MLEvolve `engine/analogy/{corpus,agent}.py`,
`utils/verify_analogy_injection.py` (offline, ~2 s), `utils/replay_analogy.py` (re-run the agent
on a node of an existing run), `k8s/job-essay-ad-s49.yaml`; this repo's
`6_build_paper_corpus.py`, `probe_analogy.py`; `analyze_runs.py` derives arm D from
`analogy.enabled` and strips `-ana`; `plot_effects.py` has a D–A contrast.

### What to look at first — adoption and family hit, not score

Same argument as 2026-08-26: at n=1 draw the score says nothing, but `logs/analogy/index.jsonl`
says whether reports were produced, `logs/analogy/<parent>_<n>.md` says whether the diagnosed
bottleneck is the one the execution summary shows and whether the queries left the competition's
own vocabulary, and `measure_adoption.py` says whether the improve node implemented what it was
handed. Known limitation to keep in mind when reading traces: on gpt-5.6 through
`/v1/chat/completions`, function tools require `reasoning_effort=none`, so the agent's diagnosis
is written as visible text rather than reasoned privately (same constraint as every other
tool call in MLEvolve).

---

## 2026-08-31 — Two ways a draw could stop being a paired comparison

Both found while trying to launch tf2qa. Neither changes what the KB contains; both change
whether a comparison means anything. Symptom first, in each case, because that is what a future
reader will be holding.

### 1. The agent paper filter was sampling, so arms could get different papers

**Symptom.** `k8s/prepare-task.sh tensorflow2-question-answering` ran WARM to convergence
(368 cached papers, injected 46807 chars, digest `e783bc5a`) and then VERIFY refused to launch:
`candidates 40: 15 cached, 25 missing`, injected 36494 chars, digest `a575fe7e`. Same task, same
KB, two different digests minutes apart.

**Cause.** `_agent_filter_papers` (Part A of `docs/agent_filter_design.md`, landed 2026-08-26)
is an LLM call, and `llm/openai.py::_chat` passes `temperature=0` only when
`supports_sampling_params(model)` is true. Every reasoning model we run on — `gpt-5*`,
`o1/o3/o4`, `claude-opus-4-7/8`, `fable` — is in `_NO_SAMPLING_PARAMS_PREFIXES`, so the filter
gets no temperature and samples. The embedding reranker it replaced was deterministic. Arms B
and C of one draw would each run their own filter and could keep a different 15 papers — the
same race `_distill_query`'s cache was built to prevent (`semantic_retrieval_design.md` §18),
reintroduced by a change that looked like a pure improvement. The `15` in the log was not a
coincidence: it is exactly `filter_max_keep`.

**Fix.** `filter_cache/` on disk next to `query_cache/`, keyed on (distilled query, sorted
candidate ids, model, floor/ceiling/batch size). Warmed by `prepare-task.sh`, read by every arm.
Two guards that matter: the all-batches-failed path does **not** write the cache (one bad
network minute would otherwise freeze "keep everything" into every later arm), and the cached
survivor list is rebuilt by consuming a multiset of ids rather than testing set membership, since
the abstract index does not guarantee unique ids.

Be clear about what this buys: the decision is now **consistent across arms**, not
**reproducible**. A fresh `filter_cache/` gives a different survivor set, so the cache directory
is part of an experiment's identity, like the KB snapshot. A cold cache still lets two
simultaneously-launched arms diverge, so `prepare-task.sh` now hard-fails when the filter has no
cached decision instead of warning.

**Also fixed:** VERIFY was checking all 40 stage-1 candidates for extractions, but the filter
drops ~25 of them before anything is downloaded, so those can never be raced on and `missing`
could never reach zero. It now replays the filter first. The gate was blocking for the right
reason and reporting the wrong one.

**Test.** `MLEvolve/utils/verify_filter_cache.py`, offline, ~1s. The LLM stub returns a *random*
verdict on purpose and check 1 is a negative control that must show two arms diverging without
the cache — a deterministic stub would pass even if the cache did nothing.

### 2. `activeDeadlineSeconds` counts Pending time

`activeDeadlineSeconds` is measured from `job.status.startTime`, which the Job controller sets
when it accepts the Job, **not** when a pod is scheduled. At the old 46800 (13 h) the slack over
the 12 h agent budget was exactly one hour, so a pod that queued longer got `DeadlineExceeded`
mid-run.

The experiment consequence is the reason this is here rather than in an ops note: A/B/C arms are
applied together but schedule at different times, so a queue-delayed arm gets a *smaller*
effective compute budget than its pair — an uncontrolled difference inside a paired design.
`analyze_runs.py` catches the killed run as `terminated_early -> invalid` (no ensembles, but
`top_solutions` present), so it discards the draw rather than biasing it silently; still, tasks
that queue for hours (tf2qa) would bleed draws for a reason unrelated to the KB.

Raised to 86400 (24 h) across all 67 experiment Jobs. The 12 h budget was never enforced by this
deadline anyway — `timeout --kill-after` inside `run_single_task.sh` is what enforces it, and it
always fires; `activeDeadlineSeconds` only backstops what runs outside that timeout (entrypoint
setup, and the unbounded `submission_fusion_utils.py` afterwards). Rationale recorded in
`MLEvolve/k8s/README.md` so it does not get "optimised" back down.

---

## 2026-08-26 — Agent filters papers before extraction; truncation relaxed

Implements Parts A-C of `docs/agent_filter_design.md`, from Peijia's review. Part D (moving to a
larger task) is deliberately separate — doing both at once produces a number attributable to
neither.

### Why an LLM and not a better embedding

Second-stage filtering was embedding similarity over techniques (`_rerank_techniques`). That
cannot express the failure it needed to catch. jigsaw was handed `Fine-tuned CLIP multimodal
encoder`, `Image captions for targeted-harmful memes`, `Multimodal image-text modeling` for a
**text-only** competition, and adopted 3 of 89 nodes. Those methods are genuinely *near* text
toxicity classification in embedding space — that is a correct embedding, not a broken one.
Cosine similarity has no way to represent "this method requires a modality the dataset does not
contain". A reader does.

Every extracted technique has carried a `**Condition**` field stating its preconditions since the
pipeline was written, and nothing has ever read it. This finally makes something read the
equivalent information.

### What changed

`_agent_filter_papers` runs **before** extraction, on title + abstract, classifying each candidate
`keep` / `irrelevant` / `infeasible`. Placing it before extraction is what makes it cheaper than
the stage it replaces: the old path paid up to 20 full-PDF extraction calls and then discarded
most of the resulting techniques; this pays one small call per batch of 10 abstracts and drops
papers before any PDF is fetched.

`_describe_data` supplies an `AVAILABLE DATA` block — a listing of `data_dir` file names and
extensions. This did not exist before and is what makes `infeasible` decidable at all: without
knowing jigsaw is text-only, the model cannot rule out a CLIP method.

When the filter runs, **every surviving paper's techniques are injected whole** — no second
filter, per the review. `_rerank_techniques` and the old paper-level path remain reachable with
`agent_paper_filter: False`, because every result to date was produced with them and re-running
them is what makes this change measurable rather than merely different.

### Truncation

Three caps were doing the truncating. Measured over the 223 extracted papers: **9.9 `[POSITIVE]`
techniques per paper, 611 chars each**, so 15 papers is ~149 techniques ~91k chars ~23k tokens.

| parameter | was | now |
|---|---:|---:|
| `retr_token_budget` | 6000 (24k chars) | 25000 (~100k chars) |
| `improve_token_budget` | **2000 (8k chars)** | 12000 (~48k chars) |
| `lazy_tech_top_n` | 12 | 0 (unlimited) |

`improve_token_budget` was by far the tightest and is repeated at every improve node.

### Guards, and why each exists

| guard | reason |
|---|---|
| `filter_min_keep: 5` floor | an empty injection turns the KB arm into an expensive baseline, which reads as a null result rather than a broken filter |
| `filter_max_keep: 15` ceiling | prompt size must not depend on how strict the agent happened to be |
| every batch failed -> return candidates **unfiltered** | degrade to the previous behaviour, not to "top 15 by score", which is a third behaviour nobody chose |
| partial batch failure -> that batch passes through | one blip must not silently drop 10 papers |
| `logs/paper_filter.md` | records every decision and its reason. Without it "the filter dropped the wrong papers" is unfalsifiable — this project has twice been misled by diagnostics that recorded nothing |

Verified offline against seven cases: normal filtering, agent keeps nothing (floor fires), agent
keeps everything (ceiling fires), total LLM failure (passes 40 through unchanged), partial failure
(15 kept, failed batch preserved), unparseable reply, and the log file's contents. The old path is
unchanged with the switch off; `verify_kb_injection.py` still passes all 33 checks.

### What to look at first, and it is not the score

jigsaw adoption is 3% today. If the filter works it should rise substantially, and that is visible
at **n=1 draw with no statistics**. Score would need 8+ draws. Run jigsaw A/B/C, then
`measure_adoption.py`, and compare `logs/paper_filter.md` against the multimodal papers listed
above — they must be marked `infeasible`.

The untested assumption is volume: injecting ~150 techniques instead of 12 may not help, and the
alternative reading of the adoption data is that the agent adopts 1-2 techniques regardless of how
many it is offered. Keeping the old path runnable is what lets that be answered.

---

## 2026-08-25 — A draw is a time cluster AND a seed, not just a time cluster

`_cluster_draws` grouped runs of a task purely by launch time (`draw_gap_hours = 2.0`). essay
seeds 45 and 46 were launched **31 minutes apart**, so all six runs collapsed into one "draw".
The per-arm dedup then kept the latest run of each arm and discarded three:

| arm | kept | discarded |
|---|---|---|
| A | `essay-base-s45` 02:30:46 (11/37) | `essay-base-s46` 02:17:26 (3/11) |
| B | `essay-kb-s46` 02:29:34 (4/12) | `essay-kb-s45` 01:59:47 (13/45) |
| C | `essay-kbimp-s46` 02:30:26 (4/17) | `essay-kbimp-s45` 02:27:19 (5/25) |

Half the newest data was thrown away, and the half that survived was **wrong**: the resulting draw
paired arm A from seed 45 against arms B and C from seed 46 — a "paired" comparison spanning two
different experiments. Arm B differs enormously between them (13/45 vs 4/12), so this was not a
small distortion.

Fixed: cluster by time, then split each cluster by seed. Neither key works alone —

- **seed alone** fails because `agent.seed` does not reproduce a run, so two batches a week apart
  at seed 43 are two independent draws (this is why the original rule ignored seed);
- **time alone** fails in the other direction, as above.

Two runs of the same arm surviving in one draw after both splits really is a relaunch, and the
later one still wins. essay now correctly shows 5 draws (seeds 42–46), each with A, B and C.

### What this changed in the results

The essay C−A valid-fraction result — the one contrast in the project whose interval had excluded
zero — **does not survive**, exactly as `job-essay-abc-s46.yaml` warned it might:

| | n=3 (as reported earlier) | n=5 (corrected) |
|---|---|---|
| essay C−A valid fraction | **+0.265 [+0.135, +0.394]** | +0.132 [−0.100, +0.364], signs `+++--` |

What stands in its place is narrower and needs its own caveat:

    essay B-A valid COUNT   n=5  +2.800  [+0.109, +5.491]  +++++   CI excludes zero
    essay B-A valid FRAC    n=5  +0.137  [-0.094, +0.367]  ++--+   contains zero

The KB arm produces about three more valid solutions per run, positive in 5 of 5 draws — but not
at a higher *rate*, because it also runs more nodes (120 vs 103 across the five draws). "More
valid solutions" and "code more likely to run" are different claims and only the first is
supported. Separating them needs an analysis change (normalise by compute), not more runs.

---

## 2026-08-25 — Record the KB's composition at the start of every run

New `MLEvolve/engine/coldstart/kb_snapshot.py`, called from `build_guidance_description`, writes
`<run>/logs/kb_snapshot.json`: which venues and years were in the abstract index and how many
papers each contributed, how many papers had extracted methodology per venue, the index
manifest's identity (embedding model, dim, count), and a `digest` over all of it.

### The gap it closes

`injected_knowledge.md` records what a run *received*. Nothing recorded what it *could have*
received. Two runs can be handed byte-identical techniques while the corpus underneath differs,
and that is unnoticeable from the run directory.

Worse, it is unrecoverable after the fact. Checking the repo:

| artifact | versioned? |
|---|---|
| `output/` (paper corpus) | yes — 23,589 files in git |
| `methodology_kb/` | yes — 243 files in git |
| **`output/abstract_index/`** | **no — zero files tracked** |

The one artifact retrieval actually queries is the one with no history. And `methodology_kb`
*grows during normal operation*, because lazy mode caches on-demand extractions back into it, so
even the tracked part does not reflect what any past run saw on the cluster — only one commit
touched `output/` or `methodology_kb/` in the whole 2026-08-01…08-26 experiment window, while the
PVC copy changed continuously. Cold start is the only point where this is both cheap and certain.

Retroactive reconstruction was considered and rejected: the index has no history, and the existing
per-run injection digest is stronger evidence for the question it can answer (it already proved
essay's injected text was byte-identical from 08-14 to 08-25, and caught the one case where it
was not).

### Two semantics that would otherwise be misread, so they are stated in the file itself

- **The snapshot is the state BEFORE the run's own extractions.** Lazy mode writes into
  `methodology_kb` as it goes, so the end-of-run directory will not match. That is intended — it
  describes the pool the run started from — but the file embeds a `note` saying so, because
  anyone diffing the two will otherwise conclude the snapshot is broken.
- **Arms of one draw can legitimately differ.** `methodology_kb` is shared mutable state, so an
  arm launched later sees what earlier arms just cached. Comparing digests across arms is a real
  check, not a formality: that is exactly what invalidated the essay seed-42 draw.

### Design details

- `digest` covers corpus composition and index identity only, deliberately **excluding**
  `captured_at`, so two runs over an unchanged corpus produce the same digest. Verified: repeated
  snapshots match, and adding one extracted paper changes it.
- Called **outside** the `if methodology_text` branch. A run that retrieved nothing is exactly the
  case where knowing which venues were in the pool matters most.
- Arm A writes **no file** (no KB paths configured), so absence unambiguously means "no knowledge
  base". A *failed* snapshot writes a file containing `"error"` instead, so the two cannot be
  confused.
- `methodology_kb/paperinsight/` is excluded from venue counting — it is cross-paper synthesis,
  not a venue.
- Never raises. Verified against five cases: normal arm, arm A, repeat-same-corpus, corpus-grew,
  and missing index directory (writes a partial rather than crashing).

Added to `fetch-run.sh`'s download list. `utils/verify_kb_injection.py` still passes.

**Incidental finding this immediately surfaced:** only **5** venues are actually built
(aaai / acl / icml / naacl / neurips, all 2024; 23,166 papers). The README claimed 8 supported
conferences — cvpr, iccv and iclr have never been built. That is the kind of drift this record
exists to catch.

---

## 2026-08-23 — Process figures: what the search did, not what it scored

`<task>_process.png`, one panel per metric, paired differences per contrast:

| metric | direction |
|---|---|
| valid solutions (count) | higher = more |
| valid fraction of nodes | higher = more |
| buggy fraction of nodes | lower = fewer failures |
| nodes defining their own architecture (`class X(nn.Module)`) | mechanism variable, no "better" |

Differences are plotted **raw, not sign-corrected**, because "better" is not uniform across these
metrics and silently flipping some would make the panel unreadable. Each panel states its own
direction. A contrast whose CI excludes zero is bolded and listed on the figure footer and in the
console.

Two implementation notes:

- `custom_arch_fraction` is new in `run_inventory.csv`, counted over nodes that carry code.
- These figures **do not need `--scores`** and are emitted before the grading check, so they still
  render when mle-bench grading is unavailable. That is the point of them: they read the inventory
  only.

### Why this is worth charting at all

Process metrics are far less noisy than the score. Pooled across tasks, the paired B−A difference
in valid-solution count is +2.57 with a 95% CI of [+0.19, +4.95] at n=7 — the first contrast in
this project whose interval excludes zero — while no score contrast manages it at n=10. There is
independent prior support: AutoMind's ablation reports a **valid-rate** drop of 5.6% alongside its
win-rate drop, so this was not a hypothesis fished out of this data.

A mechanism is visible in the same direction, though its intervals still contain zero: KB arms
define their own architectures less often (B−A −0.154, 6 of 7 negative) and have a lower bug rate
(B−A −0.091, 5 of 7). That fits what `show_models.py` shows in the baselines — solutions full of
bespoke classes like `SparseResidualMultiLabelClassifier`, which are likelier to fail to run.

### But the per-task figures immediately qualify it

The pooled +2.57 is **not uniform across tasks**, and plotting per task is what revealed it: on
jigsaw the B−A valid-count differences are mostly negative. The pooled effect is carried by essay
and lmsys. What clears zero in the per-task view is narrower and different — essay C−A on valid
fraction (+0.265) and on buggy fraction (−0.265), both n=3.

Pooling paired differences across tasks with different metrics, different dynamics and different
node budgets was the wrong default, and the figure is what caught it. Report per task.

Standing caveat: six contrasts were computed, so one crossing zero by chance is roughly a
one-in-four event under the null. These are exploratory.

---

## 2026-08-19 — Re-fuse every run with the time cap lifted, keeping the capped results

The `[WARN] Total time ... > 32400.0s limit, stopping.` lines are not runs that failed to finish
ensembling. They are a deliberate cap: `submission_fusion_utils.py` sums the constituent
solutions' execution times and breaks once they exceed `max_total_time_hours = 9.0`.

Two problems with it, both found by inspecting the corpus rather than the code:

1. **It is a confound aligned with the treatment.** The cap throttles ensemble size by how fast an
   arm's solutions happened to train, not by how good they are. It binds on about half the usable
   runs, and the throttling is severe — `essay-kbimp-s43` accumulated 11 valid candidates and was
   allowed to fuse 2; `jigsaw-kbimp-s42` had 11 and fused 3. It also sums training times
   *serially* although candidates were trained in parallel (`parallel_search_num: 3`), so it is
   conservative by roughly that factor.
2. **It was not applied consistently.** `20260817_022101_lmsys-kb` has ensembles at 9.87 h,
   10.09 h and 15.24 h — all past the cap, all written — while contemporaneous runs were cut at
   8.5 h. The ensemble sizes in the corpus are therefore not the product of one rule.

`utils/refuse_all.py` re-runs fusion for every run into `workspace/ensembles_uncapped/`, leaving
`workspace/ensembles_csv/` byte-for-byte alone. Cheap: fusion re-averages `submission.csv` files
that already exist under `top_solution/`, so nothing is retrained. Supporting changes:

- `submission_fusion_utils.py` gains `--max_total_hours`, `--max_candidates` and `--out_subdir`.
  All default to None and leave existing behaviour identical.
- `grade_all.py` now grades both directories and emits a **`variant`** column
  (`capped` | `uncapped`).
- `analyze_runs.py` gains `--variant` (default `capped`, so existing output is unchanged) and
  writes uncapped figures to a separate `charts_uncapped/`. A missing `variant` column is read as
  `capped`, so older scores.csv files still work. Verified: the default path reproduces 10 of 19
  usable groups and 12 chart files exactly as before.

**This does not make anything significant.** Confidence-interval width is driven by between-draw
variance, and adding K adds no draws. On essay it will not even move the numbers — K = 1/2/3 give
identical scores there, because fusion votes on integer labels. The point is different: it turns
the cap from an invisible assumption inside the evaluation into a measured variable, so "does the
ranking of the arms depend on the fusion budget?" becomes answerable. If it does, that is a
finding about the evaluation protocol, not about the knowledge base.

Two disciplines this shifts onto the analyst, recorded here so they are not forgotten:

- With K = 1..N available for every run it becomes possible to report whichever K flatters the
  result. Decide the K before looking, or report the whole curve. The cap was at least a rule
  fixed in advance.
- An uncapped ensemble whose members total 15 h of training could not be retrained inside a 12 h
  budget on one GPU. MLE-bench grades the submitted CSV and does not require retraining, so this
  is legitimate — but any reported number must say the cap was lifted.

Also worth re-checking on the new outputs: fusion pads missing ids via `_align_submission` with
NaN and `quality_check.py` has no NaN guard, so more fusion means more exposure. The NaN scan in
`analyze_runs.py` already covers it.

---

## 2026-08-19 — Phase 0: measure whether retrieved techniques are actually used

The score-level ablation has stopped being informative. Across 10 usable draws every contrast's
confidence interval contains zero, and Meta's MLE-bench study (arXiv 2507.02554) states that 3
seeds is insufficient for reliable comparison at all, recommending 10-20 per competition —
hundreds of GPU-hours per task to close. So the next question is not "run more", it is "measure
something cheaper that discriminates".

### What prompted this: the knowledge IS being used

Counting argument/annotation/discourse terms in `best_solution.py` for essay seed 44:

| arm | occurrences |
|---|---:|
| A baseline | 0 |
| B KB @ draft | 4 |
| C KB @ draft+improve | 14 |

The injected technique was "append annotated argumentative components" (paper reports +0.038
QWK). The competition has no such annotations — and the agent wrote regex discourse-marker
counts instead (`discourse_claim_count`, `discourse_reason_count`, …). So the technique was read,
adopted, and deliberately degraded into a proxy that needs no annotations.

This overturns the earlier working assumption that prose techniques were being ignored. The
mechanism is not indifference; it is lossy adaptation. Whether that proxy is worth anything is
now the question, and it is measurable without a GPU.

### The measurement

`scripts/measure_adoption.py` judges, per generated solution and per injected technique, whether
it was implemented `full` / `proxy` / `none`, then reports adoption rates and compares the
validation metric of adopting versus non-adopting nodes. What it finds decides the next code
change:

- **low adoption** → the problem is *binding*. Techniques are advisory context that costs nothing
  to ignore; the fix is MLE-STAR's pattern — one candidate per technique, a hard "you must use
  this" constraint, and selection by validation score.
- **high adoption, no score gain** → the problem is *selection*. We retrieve techniques whose
  preconditions the competition does not satisfy. Every extracted technique already carries a
  `Condition` field ("requires annotated argument components") and it is currently decorative;
  the fix is to filter on it.

### Two supporting changes

`engine/coldstart/knowledge.py` now writes the full injected text to
`<run>/logs/injected_knowledge.md` (the log carries only an elided preview, so a finished run did
not record what knowledge it received). Write-only, wrapped in try/except so it can never affect
a 12-hour run. Added to `fetch-run.sh`'s download list.

`utils/dump_injected.py` recovers that file for the 18 existing KB runs by replaying retrieval
with extraction capped at 0. It **verifies rather than trusts**: the replayed text's sha1[:8] is
compared against the digest the run logged at the time, and the file is written only on a match.
The knowledge base has grown since those runs, so mismatches are expected and are reported as
unrecoverable — substituting today's retrieval would score nodes against techniques the run never
received, which would look like data rather than like the error it is.

### Literature checked

- **MLE-STAR** (NeurIPS 2025) retrieves `{model_name, example_code}` pairs, with the retriever
  prompt explicitly saying *"do not just mention GitHubs or papers"*. Each retrieved item becomes
  its own executed, scored script under a hard "you must use the model as described" constraint.
  Its search ablation is 4 tasks × 3 seeds with no error bars, and its only qualitative evidence
  is vision model-choice diversification — a weaker result than it is usually cited as.
- **Meta FAIR** (arXiv 2507.02554) ranks the levers on MLE-bench: scaffold/environment +10.7 pts,
  final-node selection +9–13, operators +5.7, search policy +1.5, in-run memory ≈0. External
  knowledge retrieval is not studied anywhere in it. Single-competition standard errors reach
  ±11.5 points at 20 seeds.

Both are compatible with a papers-only knowledge base: what MLE-STAR demonstrates is that the
*form* matters (executable, constrained, scored), not the *source*.

---

## 2026-08-18 — Per-task effect figures, and two fixes that change which runs count

`analyze_runs.py` now goes past filtering: given graded scores it writes per-task figures and a
`summary.md` with effect sizes, confidence intervals and required sample sizes.

```bash
./fetch-run.sh --all                     # grades on the pod, brings back scores.csv
python scripts/analyze_runs.py --runs results/8.17/runs \
    --manual-exclusions results/8.17/manual_exclusions.yaml \
    --scores results/scores.csv --charts
```

### The score bridge

mle-bench's private answers exist only on the cluster, so nothing here can grade a downloaded
run directory. New `MLEvolve/utils/grade_all.py` grades every run's ensembles on the pod and
emits `scores.csv` (`run, competition, k, cum_hours, score, medal, lower_better`). `fetch-run.sh`
now runs it as part of every fetch, because a `scores.csv` that predates the newest run is worse
than no chart at all. `--charts` without `--scores` explains this rather than failing quietly,
and any usable run missing from `scores.csv` is reported as a warning.

### Fix 1: seed is not a draw identifier

Groups were keyed on `(task, seed, wiring)`, and `build_groups` kept only the newest run per arm.
`lmsys/seed42/fixed` already had two complete launch batches, so **one entire batch was being
discarded silently**. Once the 2026-08-17 essay runs are downloaded the same logic would have
dropped the 2026-08-16 seed-43 batch — which is precisely the batch whose result contradicts.

The underlying error is treating `agent.seed` as a replication key. It seeds numpy/torch inside
the generated candidate code; it does not seed the agent's search, because the LLM is sampled and
the model has no deterministic mode. The two seed-43 essay batches proved it by flipping the sign
of B−A. A "draw" is therefore a launch batch, now derived by clustering start times
(`draw_gap_hours = 2.0`; arms within a batch start ≤ 8 min apart, batches ≥ 20 h apart). Seed is
retained as metadata only.

### Fix 2: legacy baselines are reusable, which unblocks jigsaw

jigsaw's fixed-wiring draws contained **only arms B and C** — there was no baseline at all for the
contrast the project is about. Three legacy baselines existed but were excluded as `superseded`.

Arm A never retrieves, so the 2026-08-08 injection fix should not have reached it. That is now
*verified* rather than assumed: `MLEvolve/utils/verify_kb_injection.py` §1c-bis pulls the pre-fix
source out of git (`651fbdc^`), runs both versions against an arm-A config, and asserts the
guidance string is byte-identical (4411 chars both ways) and that `draft_agent`'s technique
section does not fire without a KB. With that established, a legacy arm A may stand in as the
baseline for a fixed-wiring draw.

Two guards, both of which matter:

- **each donor is spent once.** Reusing one baseline across two draws would enter the same number
  twice as two observations, shrinking the variance estimate and inventing significance.
- **borrowed contrasts are labelled UNPAIRED** everywhere — console, `groups.csv`, figure
  annotation, and `summary.md` — because the donor came from a different launch batch.

Effect on the corpus: **6 usable groups instead of 5**, and jigsaw goes from zero A-vs-B contrasts
to three.

### The figures, and why these and not others

| file | content |
|---|---|
| `<task>_paired.png` | one line per draw across arms at matched K |
| `<task>_effect.png` | per-contrast differences, mean and 95% CI, zero line |
| `<task>_vs_k.png` | score against ensemble size, one panel per draw |
| `_legacy_<task>.png` | the paired view for superseded runs, greyed and marked |

- A **bar chart of per-arm means is the wrong default**: the design is paired within a draw, bars
  discard the pairing, and error bars from between-draw variance make a null look like a finding.
  Slope charts keep pairing visible — a sign flip appears as crossing lines, which is exactly what
  essay does.
- Effects are **sign-corrected** so up is always better (jigsaw/essay maximise, lmsys/spooky
  minimise), and raw scores are never pooled across tasks.
- Comparisons are at **matched K only**. Arms stop fusing at different K because they can afford
  different numbers of candidates; comparing across K measures fusion budget, not the KB.
- Every figure states **n** and the **count of excluded runs**. A chart that quietly drops half the
  corpus is a cherry-pick even when each exclusion was justified.
- CIs are t intervals with a hardcoded df 1–30 table, so no scipy dependency. `required_n` is
  floored at 2 and flagged as an order-of-magnitude estimate when computed from n = 2, where the
  sd has one degree of freedom and the answer scales with its square.

Verified against hand-computed values: essay draw 2 at K=3 reproduces B−A = −0.01559 and
C−A = −0.04343 exactly, and the t interval matches a hand-checked textbook case.

`matplotlib` added to `requirements.txt`.

### Rate-limited runs are now excluded by rule, not by name

New threshold `max_ratelimit_errors = 50`, new rule `ratelimit_truncated`. A run whose endpoint
returned more rate-limit errors than this is invalid: its effective compute budget was cut by an
amount nobody chose and that cannot be matched across arms.

This exists because the 2026-08-16 essay seed-43 batch had to go, and *how* it goes matters. The
corpus is bimodal — those three runs have 2991 / 4341 / 4611 rate-limit errors and **every other
usable run has exactly zero** — so any cutoff between 1 and ~2000 gives the same answer, and the
rule can be stated in terms of a run's own health rather than by listing run names. It applies to
every task equally and will fire on any future run that hits a quota wall. Removing those three by
name would have produced identical numbers and been a cherry-pick; the distinction is worth
keeping even when the outcome is the same.

Effect: exactly 3 runs change verdict, nothing else. The clean 2026-08-17 reruns take over as
essay draw 2.

Rejected alternative: raising `min_usable_fraction` to 0.90. It would have dropped 11 of 22
usable runs, most with zero rate limits, because that metric is contaminated (see below).

### `usable_fraction` was punishing runs for finishing quietly

`usable_fraction` fell back to `log_span / 12 h` whenever there was no rate limiting. Log span is a
lower bound of unknown size — the last line is usually "REPL is executing code via subprocess",
after which the subprocess runs silently for up to two hours until the 12 h timeout kills it. So
the metric measured *how long the final silent execution happened to be*, not productive time.

It produced a false rejection immediately: the three clean 2026-08-17 essay reruns logged 11.3 /
8.6 / 9.4 h, which read as a 0.23 spread in "productive time" and rejected the whole group for
differential starvation that never occurred.

`finalise_usable()` now distinguishes three cases, and runs after `parse_outputs` because the
answer depends on the outputs:

| case | productive time |
|---|---|
| rate-limited | up to the first real 429 |
| clean **and** wrapper completed | the full budget — ensembles on disk prove the timeout fired and fusion ran after it |
| clean but wrapper did not complete | log span (best available estimate) |

All seven usable groups now show `usable_frac 1.00` across their arms, which is correct: they are
all runs that completed the wrapper without rate limiting. Genuinely truncated runs still score
low (0.00–0.58) and remain invalid.

### `fetch-run.sh --all` was aborting after one run, silently

```bash
ls "${OUT_DIR}/${RUN}/workspace/ensembles_csv" 2>/dev/null | sed 's/^/  submission: /'
```

The `2>/dev/null` hides the message but not the exit status. Under `set -euo pipefail` the failing
`ls` fails the pipeline, and because this was the last command in the loop body, `set -e` ended
the script. A run that is still in progress has no `ensembles_csv` yet, and `--all` visits the
newest run first — so a single in-flight job made the whole batch fetch exactly one run and skip
grading entirely, with a zero exit status and no error.

Fixed by testing the directory instead of relying on redirection, and by making every fragile
step in the loop (`tar` on the pod, `kubectl cp`, local extraction) report and `continue` rather
than abort. Failed runs are now listed at the end, because a partial download that looks complete
is how a chart silently loses an arm. Verified against a fake `kubectl` covering all three cases:
complete run, in-progress run, and unpackable run.

### Manual entries can flag instead of exclude

`manual_exclusions.yaml` values beginning with `flag:` keep the run usable and record the caveat
in the `flags` column instead of removing it. This exists so that "I know about this confound and
choose to include it anyway" is a visible, documented decision rather than an undocumented
omission — the alternative was deleting lines from the file, which loses the knowledge.

The essay seed-42 cache-warm race is now a flag rather than an exclusion, by decision. Note which
contrast it actually threatens: the race is between the two KB arms' technique sets, so **B-vs-C**
is the compromised comparison. A-vs-B and A-vs-C are far less affected, because arm A retrieves
nothing at all. essay consequently has 2 usable draws instead of 1.

---

## 2026-08-17 — `scripts/analyze_runs.py`: decide which runs can carry a conclusion

New script. Reads every run directory under `results/8.17/runs/` and writes
`run_inventory.csv` (one row per run) and `groups.csv` (one row per task x seed x wiring
comparison group). It computes no results — step 1 only separates usable records from
compromised ones. All decision limits sit in a single `Thresholds` dataclass at the top of the
file so they can be retuned without touching the rules.

Three verdicts, kept deliberately distinct:

| verdict | meaning |
|---|---|
| `ok` | usable |
| `invalid` | the run is broken; its number means nothing |
| `superseded` | the run is fine but exercises pre-2026-08-08 injection code, so it cannot be pooled with current runs — a version boundary, not a defect |

Result over the 46 downloaded runs: **22 ok, 7 superseded, 17 invalid; 5 of 11 groups usable**
(`essay/seed43`, `jigsaw/seed42,43,44` fixed-wiring, `lmsys/seed42`).

Design points worth keeping in mind when extending it:

- **Arm identity comes from the config, not the directory name.** `methodology_retrieval` +
  `methodology_kb_path` + `coldstart.inject_into_improve` give A/B/C. Directory names are
  inconsistent across the corpus (`-kb`, `-kbfix`, `-base`) and two runs even encoded the arm
  into `exp_id` itself (`openadmet-kb`), which would otherwise split one competition into two
  incomparable tasks.
- **Code version is detected structurally.** The presence of the `coldstart.methodology_text`
  key marks the post-fix wiring. More reliable than comparing dates against a changelog.
- **`config.yaml` needs a tag-ignoring YAML loader.** It embeds
  `!!python/object/apply:pathlib.PosixPath`, which `safe_load` rejects and which `unsafe_load`
  would execute. A `SafeLoader` subclass with `add_multi_constructor("", ...)` mapping unknown
  tags to `None` is the right tool.
- **Group-level comparability is judged separately from run-level validity.** The rule that
  matters is `max_group_usable_spread`: arms whose productive time differs by more than 20% of
  the budget cannot be compared however each one scores alone, because the confound aligns with
  the treatment.
- **`manual_exclusions.yaml`** carries problems that leave no trace in the run directory, and
  the verdict prefixes them `manual:` so automatic detection is never confused with recorded
  human knowledge. Currently one entry: the essay seed-42 cache-warm race (arms B and C
  extracted papers concurrently against a deterministic tmp path, so their technique sets are
  unrecoverable). That entry is what moves `essay/seed42` from usable to invalid.

### Two measurement bugs found and fixed during development

Both were in the first version of this script, and both produced confidently wrong answers.
They are now documented in the module docstring so they are not reintroduced.

1. **`\b429\b` matches the millisecond field of the log timestamp.**
   `[2026-08-16 07:09:06,429] WARNING: Node ... marked as buggy` is not a rate limit. About one
   log line in a thousand matches by accident, which manufactured ~32 phantom 429s in every
   clean run. Fixed by matching the error signature (`Error code: 429`, `RateLimitError`,
   `insufficient_quota`, `model_cooldown`). Real counts: **only 6 of 46 runs contain any rate
   limit at all**, where the naive regex reported nearly all 46.

2. **`re.compile(r"^\[...")` without `re.MULTILINE`** anchors to the start of the *string*, so
   `findall` over a whole log returns exactly one timestamp and every duration is 0.00 h. The
   zero-length spans then drove every starvation fraction to 0 and excluded 36 of 46 runs.

**This corrects a previously reported finding.** The claim that essay seed 43 had to be dropped
because its arms got 0.54 h / 7.07 h / 10.21 h of working API — a ~20x differential favouring
the KB arms — was an artifact of bug 1. The `,429]` hits were a "marked as buggy" line at
07:09:06 (arm A) and a "Successfully applied review patch" line at 13:29:58 (arm B). Measured
against the real error signature:

| arm | first real rate limit | productive time | usable fraction of 12 h |
|---|---|---:|---:|
| A base | 16:13:48 | 9.67 h | 0.81 |
| B kb | 15:36:28 | 9.18 h | 0.77 |
| C kbimp | 16:46:33 | 10.21 h | 0.85 |

The spread is 8 percentage points, not 20x. All three arms ran cleanly for 9–10 h of a 12 h
budget and hit the wall late, together. **essay seed 43 is a usable group** and is now included.

Also corrected: `crashed` no longer fires on any traceback. In the quota-exhausted runs every
traceback *is* a 429, so the old rule reported one problem twice. It now requires a traceback
whose preceding "Exception during task execution" context is not a rate limit — which leaves
exactly one genuinely crashed run (`20260726_082638_openadmet`). Likewise `api_starved` and
`insufficient_runtime` are separate rules sharing one threshold, so a run cut off with zero rate
limits is not mislabelled as an API problem.

---

## 2026-08-08 — Widen where the KB reaches the prompt, and fix a mislabelling bug

Changes live in the MLEvolve repo but are recorded here with the rest of the KB work.
**`coldstart.inject_into_improve` defaults to `False`, so run behaviour is unchanged** —
this lands as an ablation switch, not a new default.

### Motivation: two findings from reading the injection path

1. **The KB reached only `draft_agent`.** `run.py` calls `build_guidance_description` once
   and stores the result in `cfg.coldstart.description`, which only `draft_agent` (and
   `stepwise_coder`) read. With `initial_drafts = 3` out of 14–19 nodes per 12 h run, the
   KB's causal footprint was under 20% of the search, all of it at the very start.
2. **`improve_agent` already contained a dangling reference.** Its plateau branch says
   *"You can refer to the expert technique suggestions above, which are distilled from the
   kaggle award-winning solutions"* — but nothing ever injected technique suggestions into
   that prompt. Wiring the KB in also repairs this.

### Mislabelling bug: techniques were presented as pretrained-model recommendations

`build_guidance_description` **appended** the retrieved techniques to the pretrained-model
guidance and returned one string. `draft_agent` renders that string inside:

```
**Pretrained Model Strategy**:
  • **Option A [RECOMMENDED]**: {coldstart_description}
    → SOTA models with proven performance...
  **CRITICAL: ... you MUST copy the Code template EXACTLY as provided ...**
```

So paper-derived prose techniques were labelled as recommended pretrained models and fell
under a "copy the Code template exactly" instruction that does not apply to them. This was
true for every KB run to date (OpenADMET, spooky, jigsaw), and is a plausible contributor to
the negative results on the first two.

Fix: `build_guidance_description` now returns the model guidance only and writes the
techniques to `cfg.coldstart.methodology_text`; each is rendered under its own heading.

### Changes

- `engine/coldstart/knowledge.py` — split the two kinds of guidance; new
  `trim_methodology_text(text, token_budget)` which cuts on the `\n\n---\n\n` technique
  separator so a budget never truncates a technique mid-sentence; new
  `TECHNIQUE_SEPARATOR` constant shared with the builders.
- `config/config.yaml`, `config/__init__.py` — `coldstart.methodology_text` (runtime),
  `coldstart.inject_into_improve` (default `False`), `coldstart.improve_token_budget`
  (default 2000, vs 6000 at draft: the improve prompt is already very long and this text
  repeats at every improve node, where over-long context degrades adherence to the strict
  CHANGES/WHY/HOW output format).
- `engine/agent_search.py` — expose `self.methodology_text`.
- `agents/draft_agent.py` — techniques get their own "Techniques from recent literature"
  section, framed as hypotheses to evaluate rather than a recipe.
- `agents/improve_agent.py` — new `_inject_methodology()`, added **before** the strategy
  blocks so the plateau branch's "suggestions above" is accurate. Instructs the model to
  adopt at most one technique per step (keeping improvements atomic and attributable) and to
  skip anything already tried in Memory.
- `utils/verify_kb_injection.py` — new, no GPU/API.

### Why the injection is written into `prompt["Instructions"]`

`agent.use_diff_mode` defaults to `True`, so improve runs through `_diff_improve` →
`planner_with_memory.generate_initial_plan`, which does `prompt_base.copy()` and renders
`["Instructions"]`. Injecting into the final prompt string instead would have missed the path
actually taken. The verifier asserts both paths see it.

### Verification

`python utils/verify_kb_injection.py` — all pass: boundary-respecting truncation; baseline
arm (empty `methodology_kb_path`) unaffected; techniques land on the config rather than the
return value; own heading rather than inside the pretrained block; switch off → nothing
injected; switch on → present in both generation paths within budget.

### Effect on the experiment record

The baseline arm never had methodology text at all, so **existing baseline runs stay valid
controls**. The KB arm's draft prompt does change, so jigsaw repeats 1–3 become the "old
injection scheme" and the KB arm needs re-running. Planned decomposition, one variable per
step: **A** baseline · **B** KB with the relabelled draft only · **C** B plus improve-stage
injection.

## 2026-08-05 — First real KB-on test scores, and the infrastructure bugs that hid them

All changes in this entry live in the MLEvolve repo, but they gate every KB experiment, so
they are recorded here.

### Result: spooky-author-identification, KB arm

First run where retrieval demonstrably fired (`[Lazy] distilled query (cached)`,
40 candidates → 20 extracted). Official mle-bench test scores, multi-class log loss
(lower is better):

| submission | local CV | test |
|---|---|---|
| top1 ensemble | 0.31385 | 0.30270 |
| top2 | — | 0.30156 |
| top3 | — | 0.29532 |
| top4 | — | 0.28988 |
| top6 | — | 0.28829 |

Two findings independent of whether the KB helps:

- **Local validation tracked the test set here** (0.31385 vs 0.30270, test slightly better).
  On OpenADMET the same pipeline reported 0.19 locally against 0.74 on the real test set.
  So "local metrics are untrustworthy" was task-specific, not systemic — spooky is a sound
  testbed and its local metric can be used for model selection.
- **Fusion helps monotonically**, 0.3027 → 0.2883 (4.8% relative), even though members 3–6
  had *worse* local metrics (0.339, 0.345). Classic diversity gain. `ensemble_sizes` stops
  at 6; larger ensembles are untested and may still be improving.

No conclusion about the KB yet — the control arm was OOM-killed before finishing.

### Bug: control arm OOMKilled at 8h37m (exit 137)

16Gi was not enough, for a reason that is easy to miss: the `dshm` volume is an `emptyDir`
with `medium: Memory`, i.e. a tmpfs whose pages are **charged to the container's own memory
cgroup**. Its `sizeLimit: 8Gi` therefore let `/dev/shm` claim half the budget, leaving ~8Gi
for the three parallel training subprocesses (`agent.search.parallel_search_num: 3`).

Fix (`k8s/job-spooky-{baseline,kb}.yaml`): memory 16Gi → 32Gi, dshm 8Gi → 2Gi.
Job specs are immutable, so this requires `kubectl delete job` before re-applying.

### Bug: `mlebench grade-sample` unusable — LFS pointer files

`pip install git+https://github.com/openai/mle-bench.git` without git-lfs present fetches
LFS **pointer stubs** instead of the real files, so every bundled `leaderboard.csv` is a
~130-byte text file whose sole "column" is `version https://git-lfs.github.com/spec/v1`.
`grade_csv` computes the score fine and then dies in `rank_score`:

    AssertionError: Leaderboard must have a `score` column.

Two consequences, both previously misdiagnosed: no official scores, and the grading server
never started (`format_server.py` imports `mlebench.grade` at module scope).

- Repair: install `git-lfs`, `git lfs pull` a real clone, `pip install -e .`.
- Workaround added regardless — **`MLEvolve/utils/grade_local.py`**: grades submissions
  offline against the private answers, treats the leaderboard as optional (auto-detecting a
  renamed score column when possible), accepts directories, and supports `--cutoff-hours`
  so two runs with unequal wall-clock budgets can be compared at a matched budget.

### Bug: grading-server health check depended on curl

`run_single_task.sh` probed `/health` with `curl ... >/dev/null 2>&1`. The slim pytorch
runtime image has no curl, and the redirect swallowed "command not found", so the check
always timed out. Replaced with a Python socket probe (python is guaranteed present).
Independent of the LFS bug above — both had to be fixed.

### New: jigsaw-toxic-comment-classification-challenge A/B

`k8s/job-jigsaw-{baseline,kb}.yaml`. Chosen because it is the **best corpus match to date**:
~390 papers across four directly on-topic categories
(`acl-2024/hate-speech-and-toxic-content-detection` 30,
`neurips-2024/toxicity-detection-and-classification-datasets` 7,
`naacl-2024/llm-alignment-safety-detoxification` 66,
`aaai-2024/llm-safety-adversarial-robustness` 287), versus 3 of 423 categories relevant to
OpenADMET. That makes it the cleanest test of the coverage hypothesis: if the KB still fails
to help when the corpus does cover the task, the problem is the injection mechanism or the
paper-vs-competition genre gap, not coverage.

Task-specific risks recorded in the manifests:

- **Metric direction is inverted** vs spooky — mean column-wise ROC AUC, higher is better.
  `result_parse_agent` decides direction once at startup via an LLM call; getting it wrong
  wastes the full 12 h. Must be verified in the logs within the first 30 minutes.
- **8× the data** (159,571 vs 19,579 rows) → far fewer search steps in the same budget.
- **Multi-label, rows do not sum to 1.** Verified safe: `submission_fusion_utils.py`
  `_detect_format` decides row normalization from the data (only when |row_sum − 1| < 0.05),
  so it will not misapply the sum-to-1 step it correctly used for spooky.
- Resources raised to 48Gi / 8 CPU for both arms, ports 5011/5012 to avoid the spooky jobs.

## 2026-07-22 — Lazy mode: second-stage technique-level rerank (switchable)

Lazy mode's final selection now has two flavours, chosen by `lazy_technique_rerank`
(MLEvolve config):

- **True (default):** after on-demand extraction, all `[POSITIVE]` sections are split into
  individual techniques, embedded with the same model as the abstract index (already
  loaded — no extra LLM cost), and ranked by similarity to the task
  (`lazy_tech_min_score` = 0.3 relative, `lazy_tech_top_n` = 12). This filters out a
  relevant paper's irrelevant techniques — stage 1 (abstracts) is recall-oriented and
  paper-level; precision is recovered here at technique granularity. Injected blocks carry
  source-paper attribution.
- **False:** previous behaviour — inject candidate papers' `[POSITIVE]` sections wholesale,
  ordered by the abstract-retrieval score.

Changes live in MLEvolve (`engine/coldstart/ondemand.py`, config); design doc §16 (EN+ZH)
updated. Verified by logic tests with a stubbed embedding model, including the key case: an
off-topic technique from an on-topic paper is dropped by the rerank.
Each entry notes the symptom (what was wrong) and the fix (what changed), with the
affected files.

---

## 2026-08-04 — Query distillation replaces the rule-based extractor (it did not generalise)

Validating the 2026-08-02 fixes on a second task (`spooky-author-identification`, chosen
because the corpus is deep in NLP) showed one of them was wrong. Design doc §18 (EN + ZH).

### What the probe showed on spooky

| ranking | on-topic top-10 | spread |
|---|---|---|
| raw description | 4/10 | 0.018 |
| raw description + centering | 2/10 | 0.062 |
| **rule-extracted query** | **0/10** | 0.013 |
| **hand-written 379-char task summary + centering** | **9/10** | **0.183** |

The heading rules were tuned on the OpenADMET description, where the signal sat in a trailing
"data characteristics" section and `Evaluation` was formula plumbing. A classic Kaggle
description inverts this: spooky's ML content ("multi-class, log loss") sits *in* `Evaluation`,
which the rules discarded — leaving prize rules and horror-story flavour text. Worse than no
processing at all.

Conversely, **centering generalised**: 8/10 → 9/10 and spread 0.061 → 0.183 on this task too.
Where it looked harmful (4/10 → 2/10) the query itself was noise; centering amplifies whatever
signal exists, including none. It stays on by default.

### Changed (MLEvolve repo)

- **`_build_query` now distils the description with one LLM call** into a 50–80 word statement
  of the ML problem (input/scale, task type, metric, likely techniques), explicitly excluding
  prizes, timelines, submission formats and flavour text — automating what the hand-written
  query did.
- **Cached** to `<abstract_index_path>/../query_cache/<sha1>.txt`, so a task is distilled once
  and every later run — *including both arms of an A/B* — reuses the identical query. This
  answers the original objection to using an LLM here (non-reproducibility); cost is one call
  per task, then zero.
- Fallback order: cache hit → LLM → raw description truncated to 2500 chars (the 8/10 tier).
  The rule-based path is **removed**, not demoted: 0/10, with no regime where it won.
  Outputs under 40 chars count as failures and are not cached.
- Config: `retr_focus_query` (bool) → `retr_query_mode: llm | raw` (default `llm`), plus
  `retr_query_cache_dir`.

### Changed (this repo)

- **`scripts/probe_retrieval.py`**: `--query-mode llm|raw` and `--cache-dir`; `--all` now
  compares centering × query-mode. Mirrors the MLEvolve distillation prompt and cache contract.

### Notes

- Verified with a stubbed LLM: distil-once-then-cache, cache survives an LLM outage (so A/B
  runs stay reproducible), fallback to raw text on failure, too-short outputs rejected without
  polluting the cache, `raw` mode makes no call, and different descriptions get separate keys.
- Process lesson worth keeping: both fixes were tuned on n=1 and one was wrong. Probe a
  **second, structurally different** task before trusting any retrieval change — seconds of
  probing versus a 12-hour run.

---

## 2026-08-02 — Retrieval quality: fix anisotropy + query dilution

The first KB-on run retrieved almost entirely off-topic papers for a molecular ADMET task
(clinical-NLP work on opioid behaviour detection, medication-change prompt tuning, LLM
paraphrase augmentation). Probing the index isolated two independent causes — neither of
which is "the corpus lacks relevant papers". Design doc §17 (EN + ZH) documents both.

### Diagnosis (retrieval-only probe, no LLM calls)

- **Anisotropy.** Cosine similarity sat in a 0.62–0.65 band *regardless of topic* — molecular
  learning, African-language MT and emotion recognition all scored the same. ~12k ML abstracts
  share a dominant common direction, so cosine barely encodes topic.
- **Query dilution.** The query was the entire `description.md` (~5.5k chars, including
  submission format, field tables and citation), producing a diffuse vector — and degrading
  the BM25 half too, which is why the *hybrid* retriever failed rather than just the dense one.

| ranking | on-topic in top-10 | spread |
|---|---|---|
| raw cosine (before) | 5/10 | 0.017 |
| mean-centered | 8/10 | 0.048 |
| TF-IDF lexical | 10/10 | 0.037 |

### Added

- **`scripts/probe_retrieval.py`** — runs the retrieval stage alone and reports on-topic
  count and score spread per configuration; `--all` compares the four center/focus
  combinations. Validates retrieval changes in seconds instead of a 12-hour run.

### Changed (MLEvolve repo)

- **`_CenteredEmbedding`** wrapper mean-centers the dense vectors (index + query). The mean is
  computed from the loaded `embeddings.npy`, so **existing indexes stay valid — no rebuild**.
  Toggle `retr_center_embeddings` (default True).
- **`_build_query`** keeps only the ML-problem sections, dropping submission mechanics,
  citation and metric formulas; cap 2500 chars (generous, because the most informative
  "data characteristics" section usually sits at the END of a description). Rule-based — no
  extra LLM call, deterministic, reproducible for A/B runs; falls back to truncation if the
  headings don't parse. Toggle `retr_focus_query` (default True).
  Verified on the OpenADMET description: 5527 → 2500 chars, submission examples and citation
  dropped, ADMET/SMILES/sparse/masked/skewed retained.
- The same focused query now also drives the second-stage technique rerank, which had the
  same dilution problem.

### Also

- ICLR 2024 added to the corpus (abstract index 10,190 → **12,450** papers).
- `requirements.txt`: added the missing `beautifulsoup4` and `requests` (every fetcher in
  `scripts/fetch/` imports them, so `1_fetch.py` failed on a fresh environment), plus a note
  that on images shipping torch, the venv's own torch must be removed to avoid a
  torch/torchvision mismatch (`operator torchvision::nms does not exist`).

---

## 2026-07-22 — Lazy methodology mode: abstract index + on-demand extraction

Replaces the pay-everything-up-front step 5 default with a lazy path: index abstracts
cheaply (no LLM), retrieve at cold-start with a low threshold, and deep-extract only the
retrieved papers, caching results permanently. ~70M+ up-front tokens → ~0.3M per task,
amortizing toward zero. Design doc updated (EN + ZH, §16).

### Added

- **`scripts/6_build_abstract_index.py`** — abstract-level index: one record per paper
  (title/tldr/abstract, `source`/`pdf_url`, primary category for the cache path; papers in
  multiple categories deduped). Local embeddings only — zero LLM cost.
- **MLEvolve `engine/coldstart/ondemand.py`** (consumer repo) — lazy cold-start path:
  abstract retrieval (low relative threshold, recall-oriented) → split cached/missing →
  extract at most `max_extractions_per_coldstart` (20) missing papers now (PDF + one LLM
  call each, thread pool, atomic writes) into the **standard**
  `methodology_kb/{venue}/{category}/` layout → inject `[POSITIVE]` sections ordered by
  retrieval score under the token budget. `pymupdf4llm` is a soft dependency.
- **MLEvolve config**: `methodology_retrieval: lazy` mode + `abstract_index_path`,
  `lazy_pool` (40), `lazy_min_score` (0.05), `max_extractions_per_coldstart` (20),
  `lazy_extract_workers` (4).

### Changed

- **`run_all.sh`** — the heavy batch step 5 is now **opt-in** (`FULL_METHODOLOGY=1`); the
  default final step builds the abstract index (`SKIP_INDEX=1` to skip; non-fatal on
  failure).

### Also today (earlier)

- **`scripts/fetch/icml.py`** — the `div.paper` selector broke against current
  proceedings.mlr.press markup (fetch returned 0 papers); now collects `/{vol}/*.html`
  paper links directly (deduped, relative/absolute handled).
- **`scripts/2_embed_cluster.py`** — clean `SystemExit` when step 1 produced 0 papers,
  instead of a cryptic sklearn crash.

### Notes

- Verified: builder parses 922 unique papers from the real naacl-2024 output (802
  multi-category, deduped); lazy-mode PDF resolution priority, cache split, POSITIVE-only
  score-ordered assembly, and token budget all pass logic tests; all files `py_compile`.
- The batch path (step 5 + insight index + `vector` mode) remains fully supported — lazy
  is an additional mode, not a replacement.

---

## 2026-07-22 — Multi-venue PDF support (beyond ACL/NAACL)

plugin A no longer skips every non-aclanthology paper; it resolves a downloadable PDF per
paper across venues, so NeurIPS / ICML / CVPR / ICCV / ICLR (and AAAI where available) can
now build methodology_kb.

### Changed

- **`scripts/4_generate_skills.py`** — reference frontmatter now includes `pdf_url` (the
  fetchers already capture it; it was being dropped). Re-run step 4 to backfill existing KBs.
- **`scripts/plugin_a_methodology.py`**
  - New `resolve_pdf_url(source, pdf_url)`: prefers the fetcher-captured `pdf_url`, else a
    source-URL rule (`aclanthology.org` → `+.pdf`; `openreview.net` `forum?id` → `pdf?id`),
    else "". The hard `aclanthology-only` skip is removed.
  - New `--allow-abstract-fallback`: when no PDF is resolvable, extract from the abstract
    (lower quality). **Off by default** to protect KB quality.
- **`scripts/5_build_methodology.py`** — Stage 1 uses the resolver + optional
  `--allow-abstract-fallback`; papers with no PDF are counted as `skip`, not `fail`.

### Coverage

- ACL / NAACL / EMNLP: full (source rule). ICLR: full (captured or forum→pdf rule).
- NeurIPS / ICML / CVPR / ICCV: work when the fetcher captured a PDF link.
- AAAI (Semantic Scholar): partial — only papers with an open-access PDF.

### Notes

- Verified (stubbed, no network): resolver priority + ACL/OpenReview rules, frontmatter/
  abstract parsing, and that a non-ACL NeurIPS paper with a captured PDF is now picked up
  (and a no-PDF paper only under `--allow-abstract-fallback`). All 3 files `py_compile`.

---

## 2026-07-17 — Merged, concurrent methodology builder (plugin A + A2)

Adds one orchestrator that runs the whole plugin A → A2 pipeline for a venue with
two-stage concurrency, replacing the serial `build_methodology_all.sh`.

### Added

- **`scripts/build_methodology.py`** — merged, concurrent builder.
  - **Stage 1 (plugin A):** per-paper extraction for every paper across all categories,
    parallel over papers (`--paper-workers`, default 8).
  - **Stage 2 (plugin A2):** cross-paper synthesis per category, parallel over categories
    (`--category-workers`, default 3); per-agent git is withheld and a **single** commit is
    made at the end (avoids concurrent-commit corruption of the paperinsight repo).
  - Resumable: Stage 1 skips papers with an existing `*_methodology.md`; Stage 2 skips
    categories with an existing `insight.md`. Per-task failures are isolated, not fatal.
  - `--categories all|slug,slug`, `--skip-a`, `--skip-a2`, `--build-index`.
  - Reuses the plugin functions (no logic rewrite); output paths unchanged.

### Changed

- **`scripts/plugin_a_methodology.py`**
  - `download_pdf` now uses `urlopen` with a **30s timeout + User-Agent** (urlretrieve had
    no timeout and hung forever on a flaky/blocked connection).
  - `extract_methodology` now **retries with backoff** (API errors and malformed JSON).
- **`scripts/plugin_a2_insighter.py`**
  - `run_agent(..., allow_git=False)` withholds the `git_commit` tool so it is safe to run
    concurrently; the caller commits once at the end.

### Notes

- Still aclanthology-only (bug #5 intentionally not touched) — use `acl` / `naacl`.
- Verified with stubbed deps (no network): ACL-only + resume filtering for both stages,
  and the `git_commit` tool is withheld under `allow_git=False`. All 3 files `py_compile`.

Usage: `python scripts/build_methodology.py --venue naacl --year 2024 --build-index`

---

## 2026-07-17 — Semantic retrieval index builder (design Phase 1)

Implements the build side of `docs/semantic_retrieval_design.md`: a portable index that lets
the consumer retrieve at the level of an individual technique instead of picking topic
categories by name.

### Added

- **`scripts/build_retrieval_index.py`** — builds a semantic-retrieval index over a KB.
  - One record per cross-paper insight (an `insight.md` row → its `references/{slug}.md`).
  - Handles both KB layouts: flat (`{kb}/category/`) and nested (`{kb}/venue-year/category/`).
  - `embed_text` = title + `Actionable Guidance` + `Condition` (what we match the task
    against); `guidance_text` = the cleaned body (what the consumer injects).
  - Writes `{kb}/index/`: `records.jsonl`, `embeddings.npy` (float32, row-aligned), and
    `manifest.json` (`embedding_model`, `dim`, `count`, `kb_content_hash`, `schema_version`).
  - Defaults to `BAAI/bge-m3` — multilingual, because experience_kb insights are partly
    Chinese while task descriptions are English. Override with `--model`.
  - No new dependencies: uses `sentence-transformers` + `numpy` already in requirements.
    FAISS lives on the consumer side, which builds its index from `embeddings.npy`.

Usage: `python scripts/build_retrieval_index.py --kb experience_kb`

### Notes

- The manifest is the build/query contract: the consumer instantiates the *same* embedding
  model and asserts the dimension matches.
- Verified by parsing the real KBs without embedding: 15 records from `experience_kb`
  (10 HIGH / 5 MEDIUM) and 37 from `methodology_kb/paperinsight` (28 HIGH / 9 MEDIUM);
  frontmatter and `Papers & Evidence` correctly stripped from `guidance_text`.
- Consumer side (vector retrieval + `methodology_retrieval` mode switch) landed in the
  clean MLEvolve repo, not here.

---

## 2026-06-23 — Step 3: concurrent classification + truncation fix

`scripts/3_classify.py` was rewritten to run classification batches concurrently and to
stop silently dropping the tail of each batch.

### Fixed

- **Batch-tail papers no longer default to the first category** — the LLM output was
  capped at a fixed `max_tokens=1024`, too small for a full batch, so the last papers'
  lines were never generated and fell back to `categories[0]`. `max_tokens` now scales
  with batch size (`max(1024, 110 * len(batch))`).

### Changed / Performance

- **Batches run concurrently** via `ThreadPoolExecutor` (`--workers`, default 8), turning a
  long serial chain of API calls into parallel ones. Results are written back by global
  paper index, so output order is unchanged regardless of completion order.
- **Resume is now checkpoint-based.** Progress is saved to
  `cache/{venue}_{year}_classify_ckpt.json` (sparse array, atomic writes, flushed every 10
  batches and on exit); a re-run only reprocesses papers still missing, and the final,
  in-order `classified.json` is written once at the end. (Previously resume used
  `len(classified)`, which breaks under out-of-order completion.)
- **One failing batch no longer aborts the run** — it is logged and its papers are left for
  the next run instead of crashing the pool.
- **Per-batch parse warnings replaced by an end-of-run summary** listing the positions of
  defaulted (`unparsed`) and failed papers, so output isn't interleaved across threads.
- `--batch-size` default raised 20 → 30; `llm()` retry now uses exponential backoff with
  jitter (helps under rate limits).

### Notes

- Pure-logic unit tests pass (index-keyed parsing with a missing/reordered line, `max_tokens`
  scaling, atomic checkpoint round-trip); file passes `python -m py_compile`.
- After pulling this in, delete any stale `*_classified.json` from a pre-fix run so the new
  logic regenerates it cleanly.

---

## 2026-06-23 — Correctness fixes in the core pipeline + insighter

Four data-correctness bugs that silently corrupted the knowledge base were fixed.
None of them raised errors before, so they were invisible at runtime.

### Fixed

- **Cluster-name collisions no longer drop papers** — `scripts/2_embed_cluster.py`
  - *Was:* `named[name] = indices` overwrote the entry when the LLM gave two
    different clusters the same name, silently discarding every paper in the first
    cluster.
  - *Now:* on a name collision the papers are merged into the existing cluster
    (`named[name].extend(indices)`) and a notice is printed. No papers are lost.

- **Classification is now matched to papers by explicit index** — `scripts/3_classify.py`
  - *Was:* the parser appended one result per output line in order, then padded any
    shortfall with `categories[0]`. A missing, extra, or reordered line shifted every
    subsequent paper's labels, and the padding hid the misalignment.
  - *Now:* each paper is asked to be answered on a line prefixed with its `[n]` index;
    results are keyed back to the paper by that index, so a bad line only affects that
    one paper. Unmatched papers are marked `unparsed: True` and a `WARN` lists their
    positions instead of being silently defaulted. (Added `import re`.)

- **Reference filenames are unique per category; missing fields no longer crash** — `scripts/4_generate_skills.py`
  - *Was:* reference files were named `slugify(paper["id"]).md`; two papers whose ids
    slugified to the same string overwrote each other, and the `SKILL.md` index row
    could point at the wrong file. Direct indexing of `paper["id"/"title"/"abstract"]`
    also raised `KeyError` on any incomplete record.
  - *Now:* each paper gets a unique filename within its category (a numeric suffix is
    appended on collision), and the same name is used for both the file and its
    `SKILL.md` row. All paper fields are read with `.get(...)` defaults; `slugify`
    tolerates non-string / empty input and falls back to `untitled`.

- **`plugin_a2_insighter` agent loop is now bounded** — `scripts/plugin_a2_insighter.py`
  - *Was:* the tool-use agent ran in `while True:` with no iteration cap; a model that
    never stopped calling tools (or looped) would run forever and keep spending tokens.
  - *Now:* the loop is capped at `MAX_TURNS = 60`; if the agent hasn't finished by then
    it stops and prints a `WARN`.

### Notes

- All four files pass `python -m py_compile`.
- These were tracked as bugs 1, 2, 3, and 6 in the project review. Still open from
  that review: plugin_a is ACL-only (bug 5), YAML frontmatter is f-string-interpolated
  without escaping (bug 4), `temperature=0` is hardcoded at the plugin call sites rather
  than centralized in `llm.py`, and the pipeline's resume/caching gaps (step-2 naming and
  embeddings are not checkpointed; step 4 is not resumable).
