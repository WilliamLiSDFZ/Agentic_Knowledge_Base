# Update Log

A running record of notable changes to this project. Newest entries on top.
Each entry notes the symptom (what was wrong) and the fix (what changed), with the
affected files.

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
