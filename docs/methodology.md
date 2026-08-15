# Methodology: paper-derived knowledge base for an MCGS ML-engineering agent

A description of what this system actually does, at the level of detail needed to compare it
against other knowledge-augmented data-science agents (see `related_work.md`). Written
2026-08-07 against the code as it stands; parameter values are the committed defaults.

The system spans two repositories:

- **`Agentic_Knowledge_Base` (AKB)** — offline corpus construction. Scrapes conference
  proceedings, organises them into topic categories, and builds two retrieval artefacts.
- **`MLEvolve`** — the agent. Monte Carlo Graph Search over a tree of candidate solutions
  for MLE-bench (Kaggle) competitions. Consumes the KB at cold start.

---

## 1. Corpus construction (offline)

### 1.1 Fetch — `scripts/1_fetch.py`

One fetcher module per source, all subclassing `ConferenceFetcher` and returning a uniform
paper dict (`title`, `abstract`, `url`, `pdf_url`, `id`, `venue`, `year`).

| venue | source | mechanism |
|---|---|---|
| NeurIPS, ICML | proceedings site | HTML scrape |
| CVPR, ICCV | openaccess.thecvf.com | HTML scrape (shared `CVFFetcher`) |
| ACL, NAACL | ACL Anthology | Anthology parse (shared `ACLFetcher`) |
| ICLR | OpenReview API | requires credentials |
| AAAI | Semantic Scholar | API |

Output: `cache/{venue}_{year}_papers.json`. Only titles and abstracts are collected at this
stage — no full text.

### 1.2 Cluster and name — `scripts/2_embed_cluster.py`

- Embedding: `all-MiniLM-L6-v2` (384-d) over `"{title}. {abstract}"`, batch 64.
- Clustering: `AgglomerativeClustering(n_clusters=80, metric="cosine", linkage="average")`
  on the raw (un-normalised, un-reduced) embedding matrix. Fixed *k*, not distance-threshold.
- Naming: for each cluster the first 20 titles are shown to an LLM, which returns a 3–7 word
  lowercase hyphenated category name (`max_tokens=64`).
- Collision handling: if two clusters receive the same generated name, the second cluster's
  indices are **appended** to the first rather than overwriting it. The realised number of
  categories can therefore be below 80.

Output: `cache/{venue}_{year}_clusters.json` — `{name: [paper indices]}`.

### 1.3 Re-classify — `scripts/3_classify.py`

The cluster assignment from 1.2 is geometric; this step replaces it with an LLM judgement
against the *named* vocabulary, which also allows multi-label assignment.

- Batching: 30 papers per call, 8 concurrent threads.
- Each paper is rendered as `[{i}] {title}\n{abstract[:300]}` — abstracts truncated to
  **300 characters**.
- The model returns one line per paper: `[n] CATS:1,3 | TAGS:a,b,c | TLDR:one sentence`.
- `max_tokens = max(1024, 110 × batch_size)`. A fixed 1024 silently truncated batch tails.
- **Alignment guard:** output lines are matched back by the explicit `[n]` index, not by
  position. A dropped, duplicated or reordered line therefore cannot shift another paper's
  labels; unmatched papers are flagged `unparsed` and given a fallback category.
- Retries with exponential backoff plus jitter; sparse checkpoint every 10 batches, so an
  interrupted run resumes.

Output: `cache/{venue}_{year}_classified.json`, in original paper order.

### 1.4 Emit topic skills — `scripts/4_generate_skills.py`

```
output/{venue}-{year}/{category}/SKILL.md
output/{venue}-{year}/{category}/references/{paper-slug}.md
```

`SKILL.md` holds an LLM-written 1–2 sentence category description (generated from the first
15 titles) and an index table `| # | Title | Tags | File |`. Each `references/*.md` holds
YAML frontmatter (`title`, `source`, `pdf_url`, `categories`, `tags`, `venue`, `tldr`)
followed by the **full abstract**. A multi-label paper is written into every category it
belongs to. Filename collisions inside a category are suffixed `-1`, `-2`, …

This directory is committed as the product; `cache/` is scratch.

### 1.5 Abstract index — `scripts/6_build_abstract_index.py`

The retrieval artefact used at run time. Zero LLM calls.

- One record per `(venue, paper)`; a paper appearing in several categories keeps the first as
  primary (it determines the extraction-cache path) and lists the rest.
- `embed_text = "{title}. {tldr} {abstract[:2000]}"`.
- Embedding: `BAAI/bge-m3`, normalised.
- Output: `records.jsonl`, `embeddings.npy` (float32, row-aligned), `manifest.json`
  (`embedding_model`, `dim`, `count`, `venues`, `schema_version`). The manifest is the
  contract — retrieval refuses to run if the query model does not match.

### 1.6 Deep extraction — `scripts/plugin_a_methodology.py`

Turns a PDF into a structured technique list. This is the expensive stage.

- PDF URL resolution, in priority order: the fetcher's `pdf_url` field → `aclanthology.org`
  URL + `.pdf` → OpenReview forum id → `https://openreview.net/pdf?id={id}`. Unresolvable
  papers are skipped.
- Text: `pymupdf4llm.to_markdown(...)`, truncated to **64,000 characters**.
- One LLM call per paper (`temperature=0`) returning JSON:

  ```
  {"techniques": [{name, description, effect: positive|negative|neutral,
                   delta, evidence (direct quote), condition}]}
  ```

- Rendered to `methodology_kb/{venue}-{year}/{category}/{stem}_methodology.md` with one
  `## [POSITIVE|NEGATIVE|NEUTRAL] {name}` section per technique, each carrying
  `**Delta**`, `**Condition**` and a quoted `**Evidence**` line.

The positive/negative/neutral labelling is the load-bearing design choice: only `[POSITIVE]`
sections are ever injected, so the extractor doubles as a filter on the paper's own
self-reported ablations.

Measured over the 223 papers extracted so far (3,066 techniques, 13.7 per paper):

| label | count | share |
|---|---:|---:|
| POSITIVE | 2,214 | 72.2% |
| NEGATIVE | 530 | 17.3% |
| NEUTRAL | 322 | 10.5% |

Two things follow. First, 27.8% of the extraction output is never read by anything — it is
generated, stored, and unused. Second, and more importantly, **`[NEGATIVE]` does not mean
"this technique is bad"**. Inspecting the extracted entries shows the label collapses three
distinct situations:

1. a component the authors tried and found unhelpful — genuinely useful negative knowledge;
2. a **baseline or competitor method that lost** on that paper's dataset (e.g. Reflexion
   prompting labelled NEGATIVE because the paper's own method beat it) — misleading;
3. an ablation dimension where the main method merely failed to win.

Case (2) makes injecting `[NEGATIVE]` sections as "what not to do" actively hazardous: the
agent would learn that perfectly good methods are bad because they lost one comparison. The
extraction prompt would need to separate "the authors tried it and it hurt" from "it was the
control group" before this material is usable.

The 72.2% POSITIVE share is itself a bias signal: papers are written to argue for their own
contribution, so POSITIVE tracks *what the paper proposes*, not *what has been independently
validated*.

### 1.7 Cross-paper synthesis — `scripts/plugin_a2_insighter.py`

An LLM **tool-use agent** (tools: `list_files`, `read_file`, `write_file`, `git_commit`;
`MAX_TURNS = 60`, tool output truncated to 64,000 chars) reads every `*_methodology.md` in a
category and writes insights that each cite **at least two papers** with direct quotes.
Single-paper observations are explicitly not insights. The agent is instructed to perform a
self-review pass and delete weak insights before finishing. Each insight carries a
`HIGH`/`MEDIUM`/`LOW` confidence label.

Output: `methodology_kb/paperinsight/{venue}-{year}/{category}/insight.md` + `references/`.

`scripts/5_build_methodology.py` drives 1.6 and 1.7 together: 8 threads over papers, then 3
threads over categories, resumable (existing outputs are skipped), with a single git commit
at the end (per-agent git is disabled to avoid concurrent-commit races).

### 1.8 Experience KB — `plugin_b_experience.py`, `plugin_c_dreamer.py`

A second, structurally independent knowledge base built from the agent's **own training-run
logs** rather than from papers.

- **Plugin B** ingests a run directory, reads `judge_*/output.json` and `designer*/output.json`,
  and extracts three files: `wins.md` (techniques with positive outcomes), `failures.md`
  (errors, blocked dependencies, wrong assumptions), `hypotheses.md` (confirmed / falsified /
  untested). Every claim must cite a source node and a direct quote. New entries are
  LLM-deduplicated against the existing file (strict binary skip/add — never merge). Each run
  gets its own git branch; merge conflicts between parallel runs are resolved by an LLM that
  classifies the conflict (`direct_contradiction` / `condition_difference` /
  `environment_factor` / `sample_size`) and writes a reconciled entry, with an audit log.
- **Plugin C ("dreamer")** performs sleep-time consolidation and forgetting: merges duplicate
  entries (summing their `Seen` counts), extracts 2–5 meta-insights, then ages entries out.
  An entry becomes an archive candidate once `dreamer_runs ≥ 10 + (seen − 1)` — each extra
  sighting buys one more run of survival — capped at 3 candidates per file per run, with an
  LLM making the final keep/archive call. Archived entries are permanently deleted at
  `archived_runs = 5`. Minimum lifetime for a `seen=1` entry: 14 dreamer runs.

**This half of the system has never been included in an experimental arm.** All A/B results
below use `methodology_kb` only.

### 1.9 LLM plumbing

All AKB chat completions go through `scripts/llm.py`: a single `OpenAI` client pointed at an
OpenAI-compatible endpoint, configured by `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY`,
defaulting to OpenRouter + `anthropic/claude-sonnet-4.6`. Embeddings are local
(`sentence-transformers`), so only chat completions incur cost. One model serves every stage
— cluster naming, classification, skill descriptions, extraction, synthesis, deduplication,
conflict resolution, consolidation and forgetting. There is no per-stage model selection.

---

## 2. Retrieval at cold start (online)

`run.py` calls `build_guidance_description(cfg, task_desc)` **once**, before the search
begins, and stores the result in `cfg.coldstart.description`.

### 2.1 Four modes

`methodology_retrieval` selects between:

| mode | mechanism |
|---|---|
| `static` | a hand-maintained `methodology_map.json` maps competition id → category folders |
| `llm` | the LLM is shown all category *names* and picks ≤ 5; their HIGH-confidence references are read |
| `vector` | hybrid retrieval over a prebuilt index of distilled insights (one record per insight) |
| `lazy` | abstract-level retrieval + on-demand deep extraction (current default for experiments) |

`llm` was the original design. Its weakness is that a category name is a very lossy
representation of ~50 papers, and the selection is capped at 5 regardless of the task. The
`vector` and `lazy` modes were built to replace it.

**Which layer each mode consumes matters and is easy to miss.** `llm` and `vector` read the
cross-paper insights of §1.7 (`paperinsight/*/insight.md`); `static` and `lazy` read the
per-paper technique files of §1.6 (`*_methodology.md`). Since every experiment in §6 ran in
`lazy` mode, **the cross-paper synthesis layer has never been part of any experiment**. That
was a cost decision rather than a design one — `vector` needs plugin A plus A2 to have been
run over the relevant categories in advance, and the corpus currently holds 223
`*_methodology.md` files against only 2 `insight.md` files, so insight coverage would have
been near zero for these tasks. The consequence is that "insight-level versus
technique-level retrieval" is an untested comparison, and one AutoMind cannot make either,
since it retrieves at paper granularity.

### 2.2 Lazy mode, step by step

This is what the reported experiments run.

**Step 1 — query distillation.** One LLM call compresses the competition description into a
50–80 word ML-task statement covering input type and scale, task type, evaluation metric, and
the modelling techniques likely to matter; prizes, timelines, file lists and narrative text
are explicitly excluded. The result is cached on disk keyed by `sha1(description)[:16]`, so a
task is distilled once and **both arms of an A/B reuse a byte-identical query**.

Why an LLM rather than rules: a heading-based extractor was implemented first and did not
generalise. On OpenADMET the signal sat in a trailing "data characteristics" section; on
spooky-author-identification it sat under "Evaluation", which the rules discarded, leaving
only horror-story flavour text. Measured top-10 on-topic hits: raw description 2/10,
rule-extracted 0/10, distilled 9/10.

**Step 2 — abstract retrieval.** `HybridRetriever` (BM25 + FAISS, combined by Reciprocal Rank
Fusion, `alpha = 0.5`) returns `lazy_pool = 40` candidates. The relative-score threshold is
deliberately **low** (`lazy_min_score = 0.05`): this stage is recall-oriented, because
extraction cost is capped downstream and precision is recovered in step 4.

**Mean-centring.** Both the indexed vectors and the query are mean-centred before use.
Sentence embeddings of a homogeneous corpus are strongly anisotropic — every vector shares a
large "this is an ML paper" component that dominates cosine similarity and suppresses topic
signal. Measured on this corpus: top-10 score spread 0.017 with 5/10 on-topic before, 0.048
with 8/10 after. The mean is computed from the loaded vectors at run time, so no index
rebuild is required. Centring is applied by wrapping the embedding model, which leaves the
BM25 half untouched.

**Step 3 — on-demand extraction.** Candidates are split into cached (a `*_methodology.md`
already exists) and missing. At most `max_extractions_per_coldstart = 20` missing papers are
extracted *now*, using the plugin-A logic (PDF download → pymupdf → one LLM call), 4 threads,
written into the standard `methodology_kb` layout. The cache is permanent and shared with the
batch pipeline, so per-task cost amortises toward zero as it warms.

**Step 4 — technique-level rerank** (`lazy_technique_rerank`, default on). All `[POSITIVE]`
sections of the available papers are split into individual techniques, each embedded as
`"{technique title}\n{body[:800]}"` with the same model as the index (already loaded, so no
extra cost), and ranked by cosine similarity **to the distilled query**. Techniques scoring
below `lazy_tech_min_score = 0.3` *relative to the best* are dropped, near-duplicate titles
are removed, and the top `lazy_tech_top_n = 12` survive.

This stage exists because stage 2 is paper-level and recall-oriented: a relevant paper
usually contains several irrelevant techniques, and only this stage can filter them. Setting
the switch to `False` reverts to injecting whole papers' `[POSITIVE]` sections ordered by the
stage-1 score.

**Step 5 — assembly.** Selected techniques are concatenated under a budget of
`retr_token_budget = 6000` tokens (≈ 24,000 characters), each block carrying its source-paper
attribution, under the header *"Methodology Insights from Literature"*.

### 2.3 Injection point

`run.py` calls the builder once and stores the result on the config. The techniques then
reach `draft_agent` under their own heading, *"Techniques from recent literature"*, framed as
hypotheses to evaluate rather than a recipe. With `coldstart.inject_into_improve` (default
**off**) they additionally reach `improve_agent`, trimmed to
`coldstart.improve_token_budget` = 2000 tokens and added ahead of the strategy blocks so the
plateau branch's existing line *"refer to the expert technique suggestions above"* — a
dangling reference until now — resolves. They never reach `debug_agent`,
`evolution_agent`, `fusion_agent` or `aggregation_agent`.

Consequence for interpretation: with injection at draft only, the knowledge base can
influence the *initial* solutions and nothing else. With `initial_drafts = 3` out of 14–19
nodes on a 12-hour run, the KB's causal footprint is under 20% of the search, all of it at
the start, and any measured effect propagates through which branches the search begins from
rather than through per-step guidance.

#### A defect that invalidates the wiring used in every experiment below

Until 2026-08-08 the retrieved techniques were **string-concatenated** onto the
pretrained-model guidance and returned as one value, which `draft_agent` interpolated into
the middle of this block:

```
• **Option A [RECOMMENDED]**: {coldstart_description}
  → SOTA models with proven performance. Use for end-to-end fine-tuning OR as frozen …
  …
**CRITICAL: When using any recommended pretrained model (Option A), you MUST copy the Code
template EXACTLY as provided …**
```

Four consequences, all present in every run reported in §6:

1. The techniques landed *between* "Option A:" and the line describing them as "SOTA models
   with proven performance", so prose technique descriptions were labelled as recommended
   pretrained models.
2. The "copy the Code template EXACTLY" instruction covered them, although a technique
   description contains no code template — an unfollowable instruction.
3. A `---` rule and a `##` heading were injected mid-bullet-list, so `Option B` and
   `Option C` became subordinate to that heading.
4. **The `"None model"` sentinel was defeated.** `draft_agent` gates the whole block on
   `coldstart_description != "None model"`, the value `_build_guidance_text` returns when the
   competition has no pretrained-model entry. Appending technique text broke that equality,
   so the block fired — **in the KB arm only**, since the control's technique text is empty.
   The two arms therefore differed by an entire extra section of pretrained-model
   instructions, not only by the knowledge. This is a confound, not just untidy prompting,
   and it applies to text tasks in particular, which is what spooky and jigsaw are.

The fix keeps the two apart: `build_guidance_description` returns model guidance only and
writes the techniques to `cfg.coldstart.methodology_text`. `utils/verify_kb_injection.py`
asserts all of the above, including that the sentinel is restored.

---

## 3. Cost model

| item | cost |
|---|---|
| abstract index build | local embeddings only, no API |
| query distillation | 1 LLM call per distinct competition, cached forever |
| retrieval | local (FAISS + BM25), no API |
| deep extraction | ≤ 20 LLM calls + 20 PDF downloads per cold start, amortising to 0 |
| technique rerank | local embeddings, model already in memory |

The design goal was that the marginal cost of a KB-enabled run approaches zero once the cache
is warm, which is what makes repeated A/B runs affordable.

## 4. Parameter reference

| parameter | default | stage |
|---|---|---|
| `N_CLUSTERS` | 80 | clustering |
| classify batch / workers | 30 / 8 | classification |
| abstract truncation (classify) | 300 chars | classification |
| index embedding model | `BAAI/bge-m3` | index |
| PDF text truncation | 64,000 chars | extraction |
| `lazy_pool` | 40 | retrieval stage 1 |
| `lazy_min_score` | 0.05 (relative) | retrieval stage 1 |
| `retr_alpha` (BM25 ↔ dense) | 0.5 | retrieval stage 1 |
| `retr_center_embeddings` | `True` | retrieval stage 1 |
| `retr_query_mode` | `llm` | query |
| `max_extractions_per_coldstart` | 20 | extraction |
| `lazy_extract_workers` | 4 | extraction |
| `lazy_technique_rerank` | `True` | retrieval stage 2 |
| `lazy_tech_min_score` | 0.3 (relative) | retrieval stage 2 |
| `lazy_tech_top_n` | 12 | retrieval stage 2 |
| `retr_token_budget` | 6000 tokens | assembly (draft) |
| `coldstart.inject_into_improve` | `False` | injection surface |
| `coldstart.improve_token_budget` | 2000 tokens | assembly (improve) |

---

## 5. Evaluation protocol

**Benchmark.** MLE-bench competitions, scored with the official private answers.
`mlebench grade-sample` computes the score and then ranks it against a bundled
`leaderboard.csv`; several of those files ship as git-LFS pointer stubs, which crashes the
ranking step *after* the score is known. `MLEvolve/utils/grade_local.py` performs the same
grading call, treats the leaderboard as optional, accepts directories, and supports
`--cutoff-hours` so runs with unequal wall-clock budgets can be compared at a matched budget.

**Paired A/B.** Two Kubernetes Jobs per competition, differing only in `EXTRA_RUN_ARGS`
(`methodology_retrieval=lazy` plus the two KB paths). Image, CPU, memory, GPU, time budget,
model and seed policy are identical, and this is asserted programmatically before launch.

**Retrieval gate.** Before spending 12 GPU-hours, `scripts/probe_retrieval.py` runs the
retrieval stage alone in seconds and reports on-topic hits in the top 10 plus the score
*spread* (`score(top1) − score(topK)`); a flat spread means the scorer is not discriminating.
The pre-registered bar is ≥ 8/10 on-topic with `center=on, query=llm`.

*"On-topic" is a smoke test, not an IR metric.* It counts top-10 papers whose **title**
contains any of a comma-separated keyword list supplied by hand per task. It therefore misses
relevant papers whose titles avoid the keywords, cannot see whether a paper is *useful* as
opposed to merely on-topic, and the keywords are chosen after seeing the task rather than
pre-registered. It is adequate for catching a query that returns unrelated ML papers, which is
what it exists for; it is not evidence of retrieval quality in a publishable sense.

**Selection rule.** The fusion step emits ensembles of size 1, 2, 3, 4 and 6. The comparison
is made at **matched K** across both arms, with the full table reported — not each arm's own
best, which would be test-set selection.

**Statistical power.** The paired difference between arms has, on jigsaw, sd ≈ 0.006 AUC
across repeats. At 80% power and α = 0.05 that requires roughly 12 paired runs to detect an
effect of 0.005, 31 for 0.003 and 70 for 0.002 — 288, 744 and 1,680 GPU-hours respectively at
12 h per run. Effects below ~0.005 per task are therefore not affordable to measure under the
current protocol. AutoMind sidesteps this by aggregating a win-rate over 15 tasks × 3 runs
rather than reporting per-task raw metrics.

## 6. Results to date

**All runs below used the defective injection wiring described in §2.3** and should be
re-measured. Metric direction differs per competition.

| competition | metric | n per arm | baseline | KB | KB effect |
|---|---|---|---|---|---|
| OpenADMET ExpansionRx | lower better | 1 | 0.678 | 0.741 / 0.726 | worse |
| spooky-author-identification | log loss, lower better | 1 | **0.2366** (silver) | 0.2883 (bronze) | worse at every K |
| jigsaw-toxic-comment | mean col-wise ROC AUC, higher better | 3 | — | — | **no difference** |

jigsaw, paired difference (KB − baseline) at each ensemble size:

| seed | K=1 | K=2 | K=3 | K=4 | K=6 | mean |
|---:|---:|---:|---:|---:|---:|---:|
| 42 | +0.00506 | +0.00482 | +0.00421 | +0.00197 | — | +0.00401 |
| 43 | +0.00021 | +0.00035 | +0.00039 | +0.00025 | −0.00002 | +0.00024 |
| 44 | −0.00679 | −0.00708 | −0.00833 | −0.00788 | −0.00910 | −0.00784 |

Mean of the three repeat-level means −0.00120, sd 0.00605, t(2) = −0.342, 95% CI
[−0.0162, +0.0138]. The single best score in the whole series is a **baseline** gold medal
(seed 44, K=3, 0.98748).

Two observations about the structure of that variance. Within a repeat the sign is almost
perfectly consistent across K (4/4, 4/5, 0/5), so **a run is good or bad as a whole** — the
K values are not independent samples, and the earlier K=1-only comparison was already
representative. Across repeats, each arm swings ~0.007, about 14× the mean treatment effect.

An earlier version of this document reported jigsaw as a positive result. That was based on
the first repeat alone and did not survive replication.

Corpus coverage was the variable that appeared to track the sign of the effect, and no longer
does cleanly. A keyword audit of the 423 categories found that topics covering competition
craft — gradient boosting, feature engineering, cross-validation strategy, ensembling,
hyperparameter search, class imbalance, missing data — total **49 papers, 0.2%** of ~23k,
against 21% theory/optimisation and 19% LLM research. OpenADMET had 3 of 423 relevant
categories; jigsaw has four directly on-topic categories totalling ~390 papers and cleared the
retrieval gate at 9/10 — and still showed no benefit. Coverage may be necessary; it is
evidently not sufficient.

## 7. Known limitations

1. **Every result above measures a defective wiring.** The §2.3 mislabelling bug — including
   the `"None model"` sentinel confound, which made the two arms differ by more than the
   knowledge — was present throughout. Re-runs on the fixed path are pending.
2. **n = 1 per arm on two of three tasks**, 3 on jigsaw. MLE-bench recommends ≥ 3, and the
   power analysis in §5 shows even 3 is far short of what this variance requires.
3. **Local validation is unreliable and inconsistently so.** On spooky it correctly ranked the
   arms; on jigsaw it ranked them backwards in one repeat and correctly in another; on
   OpenADMET it was off by ~4×. Model selection inside the agent depends on it.
4. **Narrow injection point.** Until 2026-08-08 the KB reached only `draft_agent`, so it could
   not help during improvement, debugging or fusion — the large majority of search steps. The
   improve-stage option now exists but is untested.
5. **Papers only.** No Kaggle solution writeups, notebooks or discussion posts. This is the
   clearest structural difference from AutoMind (see `related_work.md`), whose knowledge base
   is majority Kaggle solutions and which reports a positive ablation.
6. **No contamination guard.** AutoMind filters out knowledge belonging to the target
   competition; we do not. Less acute for papers than for solution posts, but spooky (2017)
   and jigsaw (2018) are old enough to sit in the backbone's pretraining data, and we run no
   post-cutoff task as a control.
7. **The cross-paper insight layer has never been exercised** (§2.1). Two `insight.md` files
   exist against 223 per-paper extractions.
8. **27.8% of extraction output is dead data** (§1.6), and the `[NEGATIVE]` label conflates
   "the authors tried it and it hurt" with "it was the losing control group".
9. **`experience_kb` is unused.** Built, versioned, and never placed in an experimental arm.
   (Outside the current scope of this work.)
10. **Coverage is uneven and undocumented per venue.** The corpus has grown across sessions
    (2024 and 2025 venues, ICLR added) without a re-audit of composition — the 0.2% figure in
    §6 predates the most recent additions.
11. **Extraction is PDF-dependent.** Papers whose PDF URL cannot be resolved are silently
    skipped, which biases the extractable subset toward ACL Anthology and OpenReview.
