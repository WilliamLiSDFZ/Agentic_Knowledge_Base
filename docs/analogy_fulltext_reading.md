# Analogy agent: reading original papers

Implementation: 2026-09-09. Runtime code lives in the sibling MLEvolve repository.

## Scope and activation

The existing BM25 corpus and ranking are unchanged. The analogy agent can open papers whose
IDs appeared in its current search results, inspect their paginated outlines, and request
original text chunks. Both the draft and improve entry points support this feature.

Enable it for a new run by adding `analogy.fulltext.enabled=True` to an existing D/E/F
configuration. `analogy.enabled=True` and the appropriate `analogy.draft` / `analogy.improve`
settings are still required. Defaults remain abstract-only so existing job definitions retain
their behavior. Do not pool full-text runs with earlier abstract-only runs merely because both
are labelled D, E, or F; preserve a separate experiment output directory and inspect config and
reading manifests. The KB snapshot's corpus digest deliberately remains a corpus identity.

Initial reading budgets, increased from the design proposal at the user's request:

| Setting under `analogy.fulltext` | Default | Meaning |
|---|---:|---|
| `enabled` | false | Expose the two reading tools and evidence-aware report schema |
| `cache_dir` | empty | Resolves to `MLEvolve/cache/paper_fulltext`, shared on the PVC |
| `offline` | false | When true, require an already parsed cache entry of the exact version |
| `max_papers` | 3 | Distinct opening attempts per invocation; failures count |
| `max_read_calls` | 12 | Calls to `read_paper` per invocation |
| `read_chars` | 8,000 | Maximum body characters returned by one reading call |
| `total_chars` | 40,000 | Cumulative returned body characters; repeated reads count again |
| `open_timeout_seconds` | 60 | Lock wait + download + parsing deadline for one paper |
| `total_open_seconds` | 150 | Cumulative paper opening time per invocation |

The existing assistant-turn limit (10), mechanism limit (3), and injected-report budget
(8,000 characters) are unchanged. Multiple tool calls can share an assistant turn. Character
budgets count source text, not tokens; actual input/output tokens and elapsed time are logged.
Only complete chunks that fit are returned, so some unused character budget is possible.

## Tool and evidence contract

1. `search_papers(query)` retrieves metadata using the existing BM25 index.
2. `read_abstract(ids)` screens candidates. In full-text mode, only complete abstracts fitting
   the response budget are returned; omitted IDs are listed explicitly.
3. `open_paper(paper_id, outline_offset=0)` downloads/parses on first access or loads the cache.
   It returns source URL, hashes, warnings, page count, and up to 30 outline entries. Each
   entry has a stable chunk ID, 1-based PDF page, inferred heading, and character count.
   `next_outline_offset` allows navigation through long papers, including appendices.
   Opening alone does not return citable body text.
4. `read_paper(paper_id, chunk_ids)` returns up to eight selected chunks, subject to reading
   budgets. The response lists chunks not returned and the remaining budget.
5. `submit_report` includes the original mechanism/mapping/intervention fields plus
   `assumptions`, `target_fit`, `limitations`, `validation_plan`, and `evidence_refs`.

Each evidence reference names a paper, `source=full_text|abstract`, and a 12-400 character
quote. Full-text references also require the chunk ID. The validator checks the quote against
text actually returned in this invocation, allowing whitespace normalization. It derives
page, section and file/text hashes from the reading ledger, not from the model's claims.
Unread chunks and invented quotes cannot support a mechanism; cited IDs without surviving
evidence are removed. Reports explicitly label `full_text`, `abstract_only`, or `mixed` evidence.
These are provenance checks, not a proof that the quoted passage logically supports a claim.

The prompt asks the agent to inspect methods, assumptions, experiments and limitations, and
revise or reject a proposed analogy if the full text contradicts it. Reports must distinguish
source findings from proposed adaptations and specify a minimal validation and rejection rule.
The downstream coding agent receives the concise report rather than the entire paper.
This change does not enforce faithful execution of the proposed intervention by the coder.

## Download, parsing and cache

The runtime modules are `engine/analogy/fulltext.py` and `fulltext_worker.py` in MLEvolve.
They adapt the KB's existing PDF-resolution approach without importing its LLM methodology
extraction pipeline. The KB corpus itself does not need rebuilding.

Resolution uses the captured `pdf_url`, deterministic ACL/OpenReview/arXiv links, or the
selected publisher/DOI page's `citation_pdf_url` metadata. gzip responses are decoded before
PDF/HTML detection. Redirects and download targets are restricted to the supported scholarly
hosts; the agent cannot supply an arbitrary URL. The mlresearch proceedings PDF repository is
supported. No arXiv search, title search, browser, or general web-search tool is added.

Each download/parse runs in a separate subprocess with a hard timeout, a 30 MiB download limit
and a 100-page parse limit. PyMuPDF4LLM's deterministic text/table mode is selected explicitly:
the default layout-model backend exceeded the dev pod's budget during real-paper validation.
PDF bytes are read once into memory to avoid repeated random reads on the network PVC.
The first two pages must pass a conservative title-token check against the corpus record.

All extractable pages are split into chunks of at most 2,000 characters. Text is not truncated
to the first N characters; methods, experiments, references and appendices remain addressable.
PDF page numbers are physical page positions, not necessarily the printed page labels.
Heading recognition is heuristic; page/chunk navigation still works when a heading is missed.
OCR, figures and visual understanding of complex equations are outside this first version.
The tool reports that limitation and identifies pages with no extracted text.

Cache entries are keyed by paper ID, title, source candidates, parser versions and a SHA-256
of both reader source files. They preserve the downloaded PDF, download receipt and parsed
document. File and text hashes are verified before reuse. A downloaded PDF can be reused after
a parse timeout; incomplete parsed documents are never published as successes. An OS file lock
serializes writers sharing a cache; lock waiting is bounded. Failed worker results have a
five-minute retry delay. Within one invocation a failed paper is not repeatedly downloaded.

Full-text errors return a structured status and leave `read_abstract` usable. Failed fetching
is never presented as successful full-text evidence. `offline=True` requires a complete parsed
cache entry; it does not parse an uncached version or make a network request.

## Provenance and reproduction

`logs/analogy/<invocation>.fulltext.json` stores reading configuration, reader/library versions,
source URLs, PDF/text hashes, download/parse timestamps, open attempts, exact tool responses,
the original chunks returned to the agent, abstracts read, character counts and timings.
The normal Markdown trace and JSONL index point to the same invocation. A later model API
failure still preserves earlier reading activity. `logs/kb_snapshot.json` records the enabled
reading configuration and parser identity in addition to the existing corpus snapshot.

To reproduce the available text, keep the reader source and dependency versions, corpus, and
cache. To audit what an earlier agent actually saw, use the saved tool responses in its reading
manifest; downloading a newer version of a paper is not an exact replay.

## Installation and verification

The optional MLEvolve `requirements_fulltext.txt` pins PyMuPDF, PyMuPDF4LLM and
PyMuPDF Layout to 1.28.0, with tabulate 0.9.0. Install this layer separately with
`python -m pip install --no-deps -r requirements_fulltext.txt`, or use `FULLTEXT=1` with
`k8s/setup-venv.sh` when preparing a new environment. These versions were already present in
the shared dev-pod environment; installing/upgrading the ML stack is not needed.

From MLEvolve, the deterministic tests and the live publisher/cache smoke test are:

```bash
python utils/verify_analogy_injection.py
python utils/verify_analogy_fulltext.py
python utils/verify_analogy_fulltext.py \
  --corpus /workspace/Agentic_Knowledge_Base/output/paper_corpus \
  --paper-id aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6 \
  --paper-id neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6 \
  --cache /workspace/MLEvolve/cache/paper_fulltext \
  --out /workspace/fulltext-validation/s48.json
```

The tests and publisher smoke test do not call an LLM or train a model. Repeating the smoke
test with `--offline` validates reuse of the exact cached documents. For a model-driven replay,
`utils/replay_analogy.py` accepts `--fulltext`, `--fulltext-cache`, `--fulltext-offline`,
`--fulltext-max-papers`, `--fulltext-read-chars`, and `--fulltext-total-chars`; use `--out` to
save the reading manifest alongside the report. Model credentials come from the existing
`LLM_MODEL`, `LLM_BASE_URL`, and `LLM_API_KEY` environment variables.

Before training comparisons, evaluate fixed task packets and fixed candidate papers with a
common report template and a common model budget. Measure source fidelity, stated assumptions,
intervention specificity, and extra token/time cost. This implementation alone does not
establish that full-text reading improves benchmark performance.

## Validation on the dev pod (2026-09-09)

Fifteen new regressions and all existing analogy injection/configuration checks pass. Four
real papers parse successfully and are readable offline with identical hashes: the S48 AAAI
paper (9 pages) and NeurIPS paper (32 pages), plus ACL (19 pages) and ICML (18 pages). Five
representative rendered pages were checked against extracted text, including a two-column
method section and an appendix table. Their combined source text exceeds the per-invocation
budget; the reader exposes it through navigation instead of silently discarding the tail.

The OpenReview sample `iclr-2024/09xfexjhqe` returned HTTP 403 from the cluster. This exercises
the unavailable/fallback path and is not counted as a successful full-text extraction. The
five-source online smoke test reports a nonzero exit status for that failed source; the
four-source offline smoke test passes. The final online sample spent 28.6 seconds in total
opening the five sources; this is one small sample, not a general performance guarantee.

Evidence and deployment backups are under `/workspace/fulltext-validation/2026-09-09/`.
The verification uses scripted model responses and real downloads/parsing; it does not test
model-driven reading quality or benchmark gains, and does not launch training or paid API calls.
