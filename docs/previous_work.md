# Previous work: the system as inherited

What existed in `Mlevolve-memory/` before this work began, written from the code rather than
from its README. Author of the original pipeline: Haoming. This document exists so that the
methodology write-up can state precisely what was inherited and what was changed; for the
current design see `methodology.md`.

Two halves, in one repository:

- **`paper-skills/`** — the offline pipeline that turns conference proceedings into a
  knowledge base. Four numbered scripts plus four out-of-band "plugin" scripts.
- **`mlevolve/`** — the MCGS agent. `engine/coldstart/` is the only place the knowledge base
  is consumed.

---

## 1. The offline pipeline

`run_all.sh <venue> <year>` runs steps 1–4 in sequence. The plugins are not wired into it and
are invoked by hand.

### Step 1 — fetch (`scripts/1_fetch.py`, `scripts/fetch/`)

Eight venue keys mapping to six fetcher classes, all subclassing `ConferenceFetcher` and
emitting an identical 7-key dict (`title`, `abstract`, `url`, `pdf_url`, `id`, `venue`,
`year`). Titles and abstracts only — no authors, no full text.

| venue | source |
|---|---|
| NeurIPS | papers.nips.cc (HTML) |
| ICML | proceedings.mlr.press (HTML, `VOLUME_MAP` 2022–2024) |
| CVPR / ICCV | openaccess.thecvf.com (HTML, shared `CVFFetcher`) |
| ACL / NAACL | ACL Anthology (shared `ACLFetcher`) |
| ICLR | OpenReview API v2 (credentials required) |
| AAAI | Semantic Scholar bulk search |

Output: `cache/{venue}_{year}_papers.json`, a flat list. Sequential, no retry, no concurrency.

### Step 2 — embed and cluster (`scripts/2_embed_cluster.py`)

`all-MiniLM-L6-v2` (384-d) over `"{title}. {abstract}"`, then
`AgglomerativeClustering(n_clusters=80, metric="cosine", linkage="average")`. `N_CLUSTERS` is
a module constant, not a CLI flag. Each cluster is named by one LLM call over its **first 20
titles**, `max_tokens=64`, and the reply is lowercased and hyphenated.

Output: `cache/{venue}_{year}_clusters.json` — `{name: [paper indices]}`.

### Step 3 — classify (`scripts/3_classify.py`)

Re-assigns every paper against the *named* vocabulary from step 2, allowing multi-label.
Batches of 20, **fully sequential** (no threads), `max_tokens=1024`, abstracts truncated to
300 characters. Requested output format, one line per paper:

```
CATS:1,3 | TAGS:tag1,tag2,tag3 | TLDR:one sentence summary
```

Resume is by count: `done = len(classified)` against the checkpoint file.

### Step 4 — emit skills (`scripts/4_generate_skills.py`)

```
output/{venue}-{year}/{category}/SKILL.md
output/{venue}-{year}/{category}/references/{slugify(paper_id)}.md
```

`SKILL.md` carries an LLM-written category description (from the first 15 titles,
`max_tokens=80`) and an index table `| # | Title | Tags | File |`. Each reference file has
YAML frontmatter (`title`, `source`, `categories`, `tags`, `venue`, `tldr`) and the full
abstract. A multi-label paper is copied into every category it belongs to.

### Plugins (manual, not in `run_all.sh`)

- **`plugin_a_methodology.py`** — downloads a paper PDF, `pymupdf4llm` to markdown truncated
  to 64,000 chars, one LLM call extracting a list of techniques, each with
  `effect ∈ {positive, negative, neutral}`, `delta`, a verbatim `evidence` quote and a
  `condition`. Rendered as `## [POSITIVE|NEGATIVE|NEUTRAL] {name}` sections into
  `methodology_kb/{venue}-{year}/{category}/{stem}_methodology.md`. **This design — signed,
  evidence-carrying technique extraction — is the strongest idea in the inherited system and
  is carried forward unchanged.**
- **`plugin_a2_insighter.py`** — an LLM tool-use agent (`list_files`, `read_file`,
  `write_file`, `git_commit`) that reads a category's methodology files and writes insights
  that must each cite **≥2 papers** with direct quotes, labelled HIGH/MEDIUM/LOW, with a
  self-review pass. Output: `methodology_kb/paperinsight/{venue}-{year}/{category}/insight.md`
  plus `references/`.
- **`plugin_b_experience.py`** — distils agent training-run logs into `wins.md`,
  `failures.md`, `hypotheses.md`, with a git branch per run and LLM-mediated conflict
  resolution.
- **`plugin_c_dreamer.py`** — "sleep-time" consolidation and forgetting over plugin B's
  output; entries age out at `dreamer_runs ≥ 10 + (seen − 1)`, at most 3 per file per run,
  and are deleted at `archived_runs = 5`.

### LLM plumbing (`scripts/_llm.py`)

A single Anthropic-protocol client against Zhipu GLM
(`https://open.bigmodel.cn/api/anthropic`, `glm-5.2`), 1200 s timeout, constructed per call.
Key resolution falls back `GLM_API_KEY` → `DEEPSEEK_API_KEY` → `OPENAI_API_KEY`. `.env` is
loaded from two places, one of which reaches outside the repo into `mlevolve/.env`.

---

## 2. How MLEvolve consumed it

`engine/coldstart/knowledge.py::build_guidance_description` → one boolean switch:

```yaml
methodology_kb_path: "../paper-skills/experience_kb"
methodology_dynamic: True   # True = LLM dynamic search, False = static methodology_map.json
```

The dynamic path is `methodology_agent.build_methodology_guidance`, and it works like this:

1. **`_scan_categories`** walks the KB and collects every directory containing an
   `insight.md`, as a list of **name strings**.
2. **`_match_categories_with_llm`** shows the LLM the **first 1500 characters** of the task
   description plus the full list of category names, and asks it to *"Select up to 5 most
   relevant categories"* (`temperature=0`, `max_tokens=256`). Replies are kept only on exact
   string equality with a known name, then truncated to 5.
3. **`_read_high_confidence_references`** opens each matched `insight.md`, parses the markdown
   table by hand, keeps only rows whose confidence column is `HIGH`, resolves the reference
   filename (falling back to a fuzzy slug-prefix match), and strips the
   `## Papers & Evidence` block, `**Delta**:` lines and frontmatter.
4. Everything is concatenated under `## Methodology Insights from Literature` and appended to
   the cold-start guidance. A side-channel `ref_ids` list is returned for adoption tracking.

Properties of this design:

| | |
|---|---|
| retrieval unit | a **category** (~50 papers) |
| what the LLM sees | category **names** only — no abstracts, no contents |
| task description used | first **1500 characters** |
| cap | **5 categories**, regardless of task |
| relevance score | none — no ranking, no threshold, no token budget |
| confidence | HIGH only; MEDIUM and LOW discarded |
| layer consumed | `insight.md` (plugin A2), **not** the per-paper `*_methodology.md` |

There are no embeddings anywhere in this path — no BM25, no FAISS, no vector similarity. The
category layer of steps 2–3 exists *because* selection is by name: without named categories
the LLM would have nothing to choose between.

### The read side for humans: `agents/*-search.md`

Eight Claude Code subagent definitions, one per venue, `model: haiku`,
`disallowedTools: Write, Edit`. Each scans `output/{venue}-*/`, reads `SKILL.md` indexes,
selects 2–5 categories and returns **extracted content — titles, TLDRs, methods — never file
paths**, on the principle that the agent replaces the caller's search work. This path is
independent of the MLEvolve runtime and was not used in any experiment.

---

## 3. State of the artifacts at handover

The code supports far more than had actually been produced.

| tree | contents |
|---|---|
| `output/` | `aaai-2024` (77 categories, 5,097 refs), `naacl-2024` (106, 1,818), `manual-2024` (1, 6) |
| `methodology_kb/` | 84 per-paper `*_methodology.md`, over `naacl-2024` and `manual-2024` |
| `methodology_kb/paperinsight/` | 3 `insight.md` files |
| `experience_kb/` | **3 hand-curated categories** in the plugin-A2 insight format: `ensemble-diversity-vs-validation-gap` (11 rows), `small-data-transformer-finetuning` (15), `winning-recipe-nlp-classification` (12) |
| `wins.md` / `failures.md` / `hypotheses.md` | **absent** — plugins B and C had never been run to completion |

The single most consequential fact here: **`methodology_kb_path` pointed at
`experience_kb/`**, so the knowledge base MLEvolve actually consumed at handover was those
**three hand-curated categories**, not the ~7,000-paper `output/` tree and not
`methodology_kb/`. The large corpus existed but was not connected to the agent.

Also note `aaai-2024` has **77 categories against `N_CLUSTERS = 80`** — direct evidence of the
cluster-name collision described below.

---

## 4. Defects present at handover

### Fixed as part of this work

1. **Cluster-name collision silently dropped papers.** Step 2 ended with
   `named[name] = indices` — a plain assignment. Two agglomerative clusters that received the
   same LLM-generated name meant the second **replaced** the first, and every paper in the
   first vanished from `clusters.json` with no warning. The final count is printed *after* the
   collapse, so the loss was invisible. `aaai-2024`'s 77-vs-80 confirms it fired.
   Fix: `setdefault(...).extend(...)`.
2. **Classification was aligned by position.** The prompt numbered the inputs `[1]`, `[2]`, …
   but the *requested output format contained no index*, and the parser matched the k-th
   non-blank output line to the k-th paper. One stray line — a preamble, a markdown fence, a
   wrapped TLDR — shifted every subsequent paper in the batch onto the previous paper's
   labels. Fix: require and parse an explicit `[n]` index, bounds-check it, and flag
   unmatched papers.
3. **`max_tokens=1024` for a 20-paper batch** silently truncated the tail; the pad loop then
   assigned `categories[0]` — an arbitrary cluster — to every unparsed paper, indistinguishable
   in the output from a real classification. Fix: `max(1024, 110 × batch_size)`.
4. **Filename collisions in step 4.** `open(ref_dir/fname, "w")` with no existence check, and
   a `slugify` that *deletes* rather than substitutes, so distinct IDs converge. The second
   paper overwrote the first while `SKILL.md` still listed two rows pointing at one file.
   Fix: uniqueness suffixes, index rows follow.
5. **Unbounded agent loop** in the A2 insighter. Fix: hard turn cap.
6. **Machine-specific paths.** `load_dotenv("/Users/haoming/Downloads/paper-skills/.env")` in
   `fetch/iclr.py` — a different user's home directory, so ICLR credentials silently resolved
   to `None` (consistent with `output/` containing no `iclr-*`). `run_all.sh` hardcoded
   `PYTHON=/opt/anaconda3/bin/python`. Fix: a single repo-relative LLM config module
   (`scripts/llm.py`) and `PYTHON="${PYTHON:-python}"`.
7. **Step 3 was fully sequential** — hundreds of blocking calls. Fix: a thread pool.

### Inherited, latent at handover, amplified by this work

**The two kinds of cold-start guidance were concatenated into one string.**
`build_guidance_description` ended with `text += methodology_text` — already present at
handover, and applied to *both* the dynamic (insight-based) and static paths. `draft_agent`
then interpolated the combined value into the middle of its **"Pretrained Model Strategy →
Option A [RECOMMENDED]"** block, under a "you MUST copy the Code template EXACTLY"
instruction. The inherited `draft_agent` in fact went further than the clean MLEvolve copy,
adding a rule the latter dropped:

> **🔴 MANDATORY — EXACT COPY BRANCH RULE:** … at least ONE branch MUST use the Code template
> VERBATIM — copy the ENTIRE code as-is, character for character, ZERO modifications.

So retrieved literature was presented as a recommended pretrained model, and one draft branch
was under a mandatory instruction to copy "the Code template" verbatim from text that
contained no code. The same defect also defeats the `"None model"` sentinel: `draft_agent`
skips the whole block when `coldstart_description == "None model"`, and appending any
technique text breaks that equality.

**This was near-harmless in the original configuration and became harmful here.** At handover
`methodology_kb_path` pointed at `experience_kb/` — three categories — and retrieval read only
HIGH-confidence rows from at most five LLM-matched categories, so the appended text was short
and frequently empty. Empty concatenation is a no-op, and the sentinel keeps working. Once the
full corpus was connected and injection moved to technique granularity, the appended block
became long, structurally intrusive (a `---` rule and an `##` heading inside a bulleted list),
and present on every run.

Attribution, stated plainly: **an inherited structural flaw whose blast radius this work
enlarged without noticing.** It was found and fixed on 2026-08-08; see `methodology.md` §2.3.
Every experiment reported before that date ran with it.

### Known and still open

- **Non-determinism by omission.** Steps 2–4 never pass a `temperature`, so `_llm.chat` omits
  the parameter and the endpoint default (1.0) applies. Cluster names, classifications and
  skill descriptions therefore differ run to run. Only the plugins pass `temperature=0`.
- **Plugin B never merges to master.** After `git checkout -b run-{name}`, HEAD *is* the
  branch, and the code runs `git merge {branch}` without first checking out master — always
  "Already up to date". The ~80-line LLM conflict-resolution subsystem is unreachable, and the
  closing `git checkout master` reverts the working tree, stranding each run's output on a
  branch nobody reads.
- **Plugin C's consolidation can destroy the file it consolidates.** It sends
  `content[:8000]` to the LLM and then rewrites the *whole* file from the returned entries, so
  anything past 8,000 characters is erased; and body text is recovered by exact-name lookup
  against the original, while the prompt explicitly asks the model to merge and rename
  entries, so a renamed entry keeps its heading and loses its content.
- **No contamination guard** anywhere: nothing prevents retrieving knowledge derived from the
  target competition.
- **README inaccuracies**: "Steps 2-4 resume automatically" is true only of step 3; the setup
  section documents `DEEPSEEK_*` while the client reads `GLM_*`; the usage loop omits `iccv`.
- **Unpinned dependencies**, with `requests` and `beautifulsoup4` missing from
  `requirements.txt` and `arxiv` / `marker-pdf` listed but never imported.

These last items are recorded for completeness; plugins B and C are outside the current scope
of this work.

---

## 5. What carried forward, and what did not

**Kept unchanged.** The four-stage corpus pipeline; the signed per-paper technique extraction
of plugin A, including its prompt and the `[POSITIVE]`/`[NEGATIVE]`/`[NEUTRAL]` rendering; the
cross-paper insight format with its ≥2-paper citation rule and confidence labels; the eight
per-venue search subagents.

**Replaced.** The retrieval path. Category-name selection by LLM gave way to two-stage
semantic retrieval — an abstract-level index over the whole corpus, then a technique-level
rerank over what that returns — together with on-demand extraction, query distillation and
mean-centring. `methodology.md` §2 documents the replacement; the original design is preserved
as the `llm` mode, and remains the fallback when no index is present.

**Consequence worth stating plainly.** Because selection is now semantic, the category layer
produced by steps 2 and 3 is no longer required *for retrieval*. It still determines the
on-disk layout, the `tldr` field that feeds the embedded text, and the `output/` product the
search subagents read — but a retrieval index could be built directly from step 1's output.
That is a testable simplification, not yet tested.
