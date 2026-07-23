# Design: Technique-level semantic retrieval for methodology cold-start

**Status:** proposal · **Scope:** replaces the "LLM picks ≤5 categories by name" step in
mlevolve cold-start with embedding-based retrieval over individual insights.
**Cross-repo:** index is *built* in this repo (Agentic Knowledge Base), *queried* in
`mlevolve/engine/coldstart/methodology_agent.py`.

---

## 1. Problem

Today, when mlevolve cold-starts a task it selects literature knowledge like this
(`mlevolve/engine/coldstart/methodology_agent.py`):

1. `_scan_categories()` lists every `paperinsight/{venue}/{category}` that has an `insight.md`.
2. `_match_categories_with_llm()` sends `task_desc[:1500]` + the **list of category names** to
   an LLM and asks it to return **up to 5** category names.
3. `_read_high_confidence_references()` reads those categories' `insight.md`, keeps only
   `HIGH`-confidence rows, and reads their reference files.

Failure modes:

- **Recall is capped at the category name.** Selection happens on the *name* of a ~80-item
  cluster, not the content. A technique whose category name doesn't obviously match the task
  is invisible — even if its `Actionable Guidance` is a perfect fit.
- **Hard limit of 5 categories**, with no notion of *how* relevant each is.
- **Coarse unit.** The unit of selection is a whole category (dozens of papers), not a technique.
- **No score.** Nothing to rank, threshold, or trim by; it's all-or-nothing per category.
- **An extra LLM call** per run (latency + cost) that a vector lookup could replace.

## 2. Goal

Select at the **insight/technique granularity** using **hybrid semantic retrieval**
(dense vector + BM25), returning a ranked, score-thresholded set of insights for the task.
Keep `build_methodology_guidance()`'s signature and output format unchanged so nothing
downstream (`knowledge.py`, the draft prompt) needs to change.

Non-goals (tracked separately): iterative/per-step retrieval and memory-aware exclusion
(improvement #2); finer task typing (improvement #3). Hooks are left for these.

## 3. The retrieval unit

The natural unit already exists: each row of an `insight.md` maps to one
`paperinsight/{venue}/{category}/references/{slug}.md` — a **cross-paper insight** with a
title, confidence, cited papers, an explanation, and an `Actionable Guidance` block. That is
exactly "one technique conditioned on a situation." We index **one record per reference file.**

Two text fields per record, with different jobs:

| field | built from | used for |
|-------|-----------|----------|
| `embed_text` | `title` + `Actionable Guidance` + `Condition` | what we embed & match against the task (the "when/what") |
| `guidance_text` | cleaned reference body (`_strip_ref_noise` logic) | what we inject into the prompt on a hit |

Embedding the *guidance/condition* (not the whole paper dump) keeps the vector focused on
applicability to a task, which is what the query is about.

Optional finer layer (phase 2): also index each `## [POSITIVE]` section from the per-paper
`*_methodology.md` files. Same record schema, `source: "methodology_per_paper"`. Start with
insight-level only.

### Record schema (portable, one JSON object per line in `index/records.jsonl`)

```json
{
  "id": "naacl-2024/efficient-large-model-training-optimization/adaptive-rank-allocation",
  "venue": "naacl-2024",
  "category": "efficient-large-model-training-optimization",
  "title": "Adaptive Rank Allocation in Low-Rank Adaptation Outperforms Uniform Rank",
  "confidence": "HIGH",
  "papers": ["2024naacl-long.35", "2024naacl-long.13"],
  "source": "methodology_kb",
  "embed_text": "Adaptive Rank Allocation ... \nActionable Guidance: use ABLoRA importance ... \nCondition: fine-tuning LLMs with LoRA where layers differ in importance",
  "guidance_text": "# Adaptive Rank Allocation ...\n<cleaned body>"
}
```

## 4. Architecture

```
BUILD (this repo, offline, after plugin_a2)          QUERY (mlevolve, at cold-start)
────────────────────────────────────────            ─────────────────────────────────────
scripts/build_retrieval_index.py                     methodology_agent.build_methodology_guidance()
  walk paperinsight/ (+ experience_kb/)                 load index artifact (once, cached)
  parse each reference -> record                        query = task_desc (+ data_preview)
  embed embed_text  (sentence-transformers)             HybridRetriever.search(query, top_k)
  write index/ artifact:                                confidence-weight + threshold + trim
    - records.jsonl                                     assemble same guidance block as today
    - embeddings.npy                          ── artifact ──►   (fallback to LLM/static if absent)
    - manifest.json (model, dim, kb_hash)
```

Key reuse: **mlevolve already ships the retriever we need** —
`mlevolve/agents/memory/retriever.py::HybridRetriever` (BM25 + FAISS `IndexFlatL2` + RRF
fusion) and `mlevolve/agents/memory/embedding_models.py::EmbeddingModel`. The query side
reuses these verbatim; we only feed them insight records instead of memory records. No new
retrieval code in mlevolve.

The build side stays dependency-light: it needs only `sentence-transformers` + `numpy`
(already in this repo's `requirements.txt`). It writes `embeddings.npy`; mlevolve builds the
in-memory FAISS index from that array at load time (it already has `faiss`), so **this repo
gains no `faiss` dependency**.

## 5. Build side — `scripts/build_retrieval_index.py` (new, this repo)

Responsibilities:

1. Walk `methodology_kb/paperinsight/{venue}/{category}/`. For each `insight.md`, parse the
   table (`# | Insight | Papers | Confidence | File`) to get `confidence` + `papers` per row,
   then read the matching `references/{slug}.md` (reuse the existing row→file resolution incl.
   the slug-prefix fuzzy fallback from `_read_high_confidence_references`).
2. Build `embed_text` (title + Actionable Guidance + Condition — parse those sections out of
   the reference body) and `guidance_text` (the reference body with frontmatter / `Papers &
   Evidence` / `Delta` stripped — same as `_strip_ref_noise`).
3. Optionally include `experience_kb/*/references/*.md` the same way (`source: experience_kb`).
4. Embed all `embed_text` with the configured model; write:
   - `index/records.jsonl` — the records (without vectors)
   - `index/embeddings.npy` — `float32 [N, dim]`, row-aligned to records.jsonl
   - `index/manifest.json` — `{embedding_model, dim, count, built_at, kb_content_hash, schema_version}`

Sketch:

```python
# scripts/build_retrieval_index.py
import json, hashlib, numpy as np
from pathlib import Path
from datetime import datetime
from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-m3"          # must match the query side; see §8
KB = Path("methodology_kb")
OUT = KB / "index"

def iter_records():
    for insight_md in (KB / "paperinsight").glob("*/*/insight.md"):
        cat_dir = insight_md.parent
        venue, category = cat_dir.parts[-2], cat_dir.parts[-1]
        for row in parse_insight_table(insight_md):          # -> {title, confidence, papers, file}
            ref = resolve_reference(cat_dir, row)            # reuse slug/fuzzy resolution
            if not ref: continue
            body = ref.read_text(encoding="utf-8")
            yield {
                "id": f"{venue}/{category}/{ref.stem}",
                "venue": venue, "category": category,
                "title": row["title"], "confidence": row["confidence"].upper(),
                "papers": row["papers"], "source": "methodology_kb",
                "embed_text": build_embed_text(row["title"], body),   # title + guidance + condition
                "guidance_text": strip_ref_noise(body),
            }

def main():
    records = list(iter_records())
    model = SentenceTransformer(MODEL_NAME)
    vecs = model.encode([r["embed_text"] for r in records],
                        normalize_embeddings=True, show_progress_bar=True).astype("float32")
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "records.jsonl", "w") as f:
        for r in records: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    np.save(OUT / "embeddings.npy", vecs)
    json.dump({"embedding_model": MODEL_NAME, "dim": int(vecs.shape[1]),
               "count": len(records), "built_at": datetime.now().isoformat(),
               "kb_content_hash": hash_kb(KB), "schema_version": 1},
              open(OUT / "manifest.json", "w"), indent=2)
```

Wire it in as the last stage of the plugin layer (after `plugin_a2_insighter`), and/or a line
in `run_all.sh`. Rebuild whenever the KB changes; `kb_content_hash` lets the query side warn on
staleness.

## 6. Query side — rewrite `methodology_agent.py` (mlevolve)

Replace `_match_categories_with_llm` + `_read_high_confidence_references` with a retrieval path.
Keep `build_methodology_guidance(task_desc, methodology_kb_path, cfg)` and its returned block
identical in shape.

```python
# a tiny record object so HybridRetriever can hold our insights
class InsightRecord:
    def __init__(self, d): self.__dict__.update(d)

_INDEX_CACHE = {}   # methodology_kb_path -> (retriever, records)

def _load_index(methodology_kb_path, cfg):
    if methodology_kb_path in _INDEX_CACHE:
        return _INDEX_CACHE[methodology_kb_path]
    idx = Path(methodology_kb_path) / "index"
    manifest = json.load(open(idx / "manifest.json"))
    records = [InsightRecord(json.loads(l)) for l in open(idx / "records.jsonl")]
    texts = [r.embed_text for r in records]
    emb_model = EmbeddingModel(model_type="local",
                               model_name=manifest["embedding_model"],   # SAME as build
                               device=getattr(cfg, "embedding_device", "cpu"))
    retr = HybridRetriever(emb_model)
    vecs = np.load(idx / "embeddings.npy")
    retr.records, retr.texts = records, texts
    retr.vectors = vecs
    retr.vector_index = faiss.IndexFlatL2(retr.dimension); retr.vector_index.add(vecs)
    retr.bm25 = BM25Okapi([t.lower().split() for t in texts])          # cheap, rebuild here
    _INDEX_CACHE[methodology_kb_path] = (retr, records)
    return retr, records

def build_methodology_guidance(task_desc, methodology_kb_path, cfg):
    idx_dir = Path(methodology_kb_path) / "index"
    if not (idx_dir / "manifest.json").exists():
        return _legacy_llm_or_static(task_desc, methodology_kb_path, cfg)   # fallback, unchanged

    retr, _ = _load_index(methodology_kb_path, cfg)
    query = _build_query(task_desc, cfg)                 # §7
    hits = retr.search(query, top_k=cfg.retr_pool, alpha=cfg.retr_alpha)    # [(rec, score)]
    selected = _select(hits, cfg)                        # confidence-weight + threshold + trim
    if not selected:
        return ""
    blocks = [f"### [{r.category}] {r.title} (confidence: {r.confidence})\n\n{r.guidance_text}"
              for r, _ in selected]
    return ("\n\n---\n## Methodology Insights from Literature\n"
            "The following techniques were retrieved as most relevant to this task:\n\n"
            + "\n\n---\n\n".join(blocks))
```

`faiss`, `BM25Okapi`, `np`, `EmbeddingModel`, `HybridRetriever` are all already importable in
mlevolve. (Optionally add a `HybridRetriever.load_from_embeddings(records, texts, npy_path)`
helper so the FAISS-from-array wiring lives in one place instead of `methodology_agent`.)

## 7. Query construction

Start simple, leave room to grow:

- **v1:** `query = task_desc` (full, not truncated to 1500).
- **v1.1 (recommended):** append a compact data summary derived from `agent.data_preview`
  (modality, #samples, #features/#classes, image size). The data shape is a strong signal for
  which techniques apply and mlevolve already computes it. Keep it short (a few lines) so it
  doesn't dominate the embedding.
- **phase 3:** multi-query (task text + data summary embedded separately, union of hits) if a
  single blended vector under-recalls.

## 8. Embedding model

**Rule:** build side and query side **must** use the same model (same vector space + dim).
Enforced by `manifest.embedding_model`; the query side instantiates `EmbeddingModel` from it,
and `HybridRetriever` already asserts the loaded dim matches.

Recommendation (2026 landscape):

- **Target: `BAAI/bge-m3`** — the open production default in 2026 (MIT, multilingual,
  dense+sparse), a clear step up from `bge-base-en-v1.5`. ~1024-dim; a few thousand insights
  embed in seconds and each query is one short encode.
- **Zero-friction fallback: `BAAI/bge-base-en-v1.5`** — already loaded by mlevolve's memory
  layer, so reusing it means no extra model download. Slightly weaker but fine to ship first.

Both are configurable; the manifest is the source of truth. The retrieval unit texts are short
(a title + a guidance paragraph), so this is squarely in-distribution for general retrieval
embeddings — no domain fine-tuning needed.

**Optional reranker (phase 2):** add a cross-encoder second stage over the top ~30 hits for
precision. 2026 default is **`BAAI/bge-reranker-v2-m3`** (best quality/latency/license);
lighter options exist (FlashRank, mxbai-rerank) if latency matters. Skip in v1 — hybrid
retrieval alone already fixes the recall problem; the reranker is a precision refinement.

## 9. Selection policy (defaults, all config-driven)

- `retr_pool = 30` candidates from `HybridRetriever.search`, `retr_alpha = 0.5` (balanced
  BM25/vector — reuse the retriever default).
- **Confidence weighting:** multiply score by `{HIGH:1.0, MEDIUM:0.7, LOW:0.4}`; drop `LOW`
  unless nothing else clears the bar. (Preserves today's HIGH-first bias without hard-dropping
  everything else.)
- **Min-score threshold** on the (normalized) fused score so irrelevant tasks inject nothing,
  rather than always returning 5 categories.
- **Trim to `retr_top_n = 10`** insights and a **token budget** (~4–6k tokens) so the draft
  prompt doesn't bloat (this also mitigates the current "whole blob" dilution).
- **Dedup** near-identical titles (same technique surfacing across venues) — keep the highest
  score, note the extra venues.
- **Forward hook for improvement #2:** `search(..., exclude_ids=...)` to drop insights already
  tried/failed per the global memory. Not wired in v1; the signature leaves room.

## 10. Config & backward compatibility

Add to `config.yaml` under the existing knobs (with a mode switch so it's reversible):

```yaml
methodology_retrieval: vector      # vector | llm | static   (default vector; llm = today's behavior)
retr_alpha: 0.5
retr_pool: 30
retr_top_n: 10
retr_min_score: 0.15
embedding_device: cpu              # or cuda
# embedding model comes from index/manifest.json (build/query must match)
```

`build_methodology_guidance` dispatches on `methodology_retrieval`; `llm`/`static` keep the
current code paths verbatim as fallbacks. If the mode is `vector` but no `index/` artifact
exists, it logs a warning and falls back to `llm`. **No caller changes** — `knowledge.py:128`
and the draft prompt are untouched.

## 11. Evaluation (prove the recall win before switching the default)

Offline harness in this repo, `scripts/eval_retrieval.py`:

1. **Probe set:** ~15–20 representative tasks (pull names+descriptions from
   `competition_tag_classified.json` / dataset descriptions). For each, label the *relevant*
   insight ids in the KB (human pass, or a strong-LLM pass then spot-checked).
2. **Compare** three selectors on the same probes: (a) today's `_match_categories_with_llm`
   (mapped to its insights), (b) vector-only, (c) hybrid.
3. **Metrics:** recall@{5,10,20} and nDCG@10 per selector; plus **coverage** = fraction of
   tasks that get ≥1 relevant insight (the current method returns *nothing* when names don't
   match — coverage is where we expect the biggest jump). Report retrieval latency/cost too
   (one local encode + FAISS vs an LLM call).
4. **Gate:** only flip `methodology_retrieval` default to `vector` if hybrid ≥ LLM on recall and
   coverage across the probe set.

## 12. Rollout

- **Phase 1 (this proposal):** builder + `records.jsonl`/`embeddings.npy`/`manifest.json`
  artifact; mlevolve query rewrite reusing `HybridRetriever`; config toggle; LLM/static
  fallback; eval harness. Ship behind `methodology_retrieval: vector` once eval passes.
- **Phase 2:** cross-encoder reranker; index `experience_kb` too; wire `exclude_ids` for
  memory-aware retrieval (bridges to improvement #2).
- **Phase 3:** enrich query with `data_preview`; move from one-shot cold-start to per-step
  retrieval when the search stalls (improvement #2 proper).

## 13. Risks & mitigations

| risk | mitigation |
|------|-----------|
| build/query model mismatch → dim error | `manifest.embedding_model` drives the query model; `HybridRetriever` asserts dim |
| stale index after KB update | rebuild as last pipeline stage; `kb_content_hash` in manifest → warn on mismatch |
| cold-load latency (model + index) | load once per run, cache in `_INDEX_CACHE`; index is small |
| no `index/` present | fall back to existing LLM/static path; nothing breaks |
| over-retrieval bloats prompt | `retr_top_n` + token budget + dedup |
| parsing gaps in reference bodies | reuse the proven `insight.md` row resolution + `_strip_ref_noise`; skip unparseable, don't crash |

## 14. File-by-file change list

**This repo (Agentic Knowledge Base):**
- **new** `scripts/build_retrieval_index.py` — build the index artifact.
- **new** `scripts/eval_retrieval.py` — recall/coverage harness.
- **edit** `run_all.sh` (optional) — run the index build after the plugin layer.
- `requirements.txt` — already has `sentence-transformers`, `numpy`; no new deps for the build.
- `docs/semantic_retrieval_design.md` — this doc.

**mlevolve repo:**
- **edit** `engine/coldstart/methodology_agent.py` — add `InsightRecord`, `_load_index`,
  `_build_query`, `_select`; rewrite `build_methodology_guidance` to dispatch on
  `methodology_retrieval`; keep `_match_categories_with_llm` / `_read_high_confidence_references`
  as the `llm` fallback.
- **edit** `config/config.yaml` + `config/__init__.py` — the keys in §10.
- **optional** `agents/memory/retriever.py` — add `load_from_embeddings(records, texts, npy_path)`
  helper so the FAISS-from-array wiring is shared, not duplicated.

## 15. Open questions

- Index `experience_kb` in v1 or v2? (Its insights are battle-tested — arguably worth a
  confidence boost — but format/verification differ. Leaning v2.)
- Per-venue-year sub-indexes vs one global index? One global index is simpler and lets a task
  pull the best insight regardless of venue; revisit only if the KB grows large.
- Should the artifact live inside `methodology_kb/index/` (travels with the KB) or as a separate
  release asset? Inside the KB is simplest and matches how mlevolve already points at
  `methodology_kb_path`.

## 16. Lazy mode (v1.1, implemented): abstract-first index + on-demand deep extraction

**Motivation.** The batch pipeline (plugin A over every paper, then A2 per category) pays
the full extraction cost up front — ~70M+ input tokens for one NeurIPS year — while a
cold-start only ever consumes a handful of insights. Lazy mode moves the expensive step to
query time and caps it.

**Flow** (`methodology_retrieval: lazy`):

1. **Abstract index** (`scripts/6_build_abstract_index.py`, this repo): one record per
   paper (title/tldr/abstract + `pdf_url`/`source`), embedded locally — **zero LLM cost**.
   Built as the default final step of `run_all.sh` (the heavy batch step 5 is now opt-in
   via `FULL_METHODOLOGY=1`).
2. **Cold-start retrieval** (MLEvolve `engine/coldstart/ondemand.py`): query the abstract
   index with a **low relative threshold** (`lazy_min_score`, default 0.05; pool
   `lazy_pool` = 40) — recall over precision, because the next step caps cost anyway.
3. **On-demand extraction:** candidates without a cached `*_methodology.md` are extracted
   NOW (PDF download → pymupdf → one LLM call each; thread pool; at most
   `max_extractions_per_coldstart` = 20 per task — the **cost ceiling knob**). Results are
   written to the **standard** `methodology_kb/{venue}/{category}/` layout, so the cache is
   permanent, shared with the batch pipeline (which skips existing files), and can later be
   synthesized by plugin A2 offline.
4. **Assembly:** `[POSITIVE]` sections of all available candidates, ordered by abstract
   retrieval score, title-deduped, under `retr_token_budget`. Injected in the same
   guidance-block format as every other mode.

**Cost:** ~0.3M tokens per task at first (20 extractions × ~16k), amortizing toward zero as
the cache warms — vs 70M+ up front for the batch path.

**Trade-offs:** no cross-paper synthesis or confidence calibration (A2) in-loop — recover
it by periodically running A2 offline over the accumulated cache; cold-start needs network
for PDFs (degrades gracefully to cached-only); `pymupdf4llm` is a soft dependency in
MLEvolve (extraction is skipped if missing); cold-start latency +3–8 min, bounded by the
extraction cap.

**Config (MLEvolve):** `abstract_index_path`, `lazy_pool`, `lazy_min_score`,
`max_extractions_per_coldstart`, `lazy_extract_workers`; in lazy mode
`methodology_kb_path` points at the **methodology_kb root** (the extraction cache tree).

**Reserved (off):** `lazy_synthesize` — a single task-conditioned synthesis call over the
extracted techniques (cheaper than A2's agent loop; phase 2).

## References (2026 retrieval landscape)

- Best open embedding models 2026 (BGE-M3 as production default; Qwen3-Embedding tops MTEB):
  BentoML, KnowledgeSDK, CodeSOTA MTEB.
- Rerankers 2026 (BGE-reranker-v2-m3 default; lightweight alternatives): ZeroEntropy, BSWEN,
  Local AI Master.
