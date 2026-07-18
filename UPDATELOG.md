# Update Log

A running record of notable changes to this project. Newest entries on top.
Each entry notes the symptom (what was wrong) and the fix (what changed), with the
affected files.

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
