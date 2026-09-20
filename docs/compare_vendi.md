# Comparing arm diversity with Vendi

`scripts/compare_vendi.py` compares **candidate mechanism diversity**, not scientific
novelty or task scores. It is a post-processing script; it never executes candidate
code, changes experiments, or accesses the cluster.

## MLEvolve runs

Start with a free, read-only inventory check (no API client/model download/output files):

```bash
.venv/bin/python scripts/compare_vendi.py \
  --runs /Users/william/nautilus/results \
  --inventory results/9.14/run_inventory.csv \
  --run-glob '20260914_*s6[12]' --arms A F \
  --out results/vendi_s61_s62 --dry-run
```

Remove `--dry-run` to extract summaries, embed, score and plot. This **calls the
configured LLM** and may download a SentenceTransformer model on first use. The
default embedding model is `sentence-transformers/all-MiniLM-L6-v2`, on CPU;
use `--embedding-model` and optionally `--embedding-revision` to select/pin another.
The resolved revision, preprocessing and library version are recorded. Treat the
choice of embedding as a measurement assumption, not an algorithm-equivalence oracle.

Summary calls reuse `scripts/llm.py` and its `.env` settings: `LLM_BASE_URL`,
`LLM_API_KEY` (or `OPENROUTER_API_KEY`) and `LLM_MODEL`. `--summary-model` overrides
the model. The default is the existing chat-completions path; endpoints/models
requiring the Responses API can use `--summary-api responses`. The chosen endpoint
must support that API. No sampling settings are forced. Live provider compatibility
is not established by the offline tests.

Defaults are `--views proposal implementation --stages draft improve`. Other node
stages can be selected explicitly. One node contributes one sample **per view**:

- `proposal`: same plan field for all arms; no analogy report is substituted for F.
- `implementation`: drafts describe the complete implementation. When parent code
  exists, assess the **raw parent-to-child diff** with related source context and
  static call/use locations. The reader uses MLEvolve's top-level
  `node2parent` map and supports older inline parent IDs. An improve implementation
  missing parent code is marked unavailable rather than treated as a whole-code
  summary. Coverage includes missing-parent counts.

Proposal/draft summaries use six neutral English fields: model, objective, data,
update, inference, change. Long inputs are chunked and merged without dropping source
characters. Parent-child assessments instead retain every diff hunk and select related
source context within a 160,000-character packet budget. If the full diff cannot fit,
the candidate is marked `insufficient_evidence`; omitted optional context is recorded.
Python AST parsing locates enclosing definitions, related uses and one-step aliases.
Short surrounding control-flow blocks and related module-level variable uses are
included to expose connections such as parameter grouping into an optimizer.
Parse failures fall back to nearby lines with an explicit limitation. Zero omitted
context means the helper's selected context fits; it does not guarantee every
dependency was selected. This is a
bounded source-context helper, not a complete call graph; candidate code is never run.

Parent-child assessments return one of three states:

- `changed`: typed changes (`new_mechanism`, `activation`, `parameter_change`,
  `bug_fix`, `removal`, `refactor`) with parent and child line references, matching
  source quotes, at least one changed code line and a child call/use reference.
  Only the neutral change descriptions are embedded.
- `no_change`: identical code or equivalent parsed ASTs. This is deliberately
  conservative; a model's no-change claim about a different AST becomes unresolved.
- `insufficient_evidence`: the available source or model assessment cannot support
  a connected change. An unused definition or an uncertain connection is not counted
  as an implemented mechanism. Unsupported claims get bounded correction attempts.

Arm labels, scores, paper names and analogy prose are excluded by the extraction
prompt. Evidence guards check source provenance and a static use/call, not semantic
correctness, whole-program reachability or successful runtime activation. The two
non-scoring states retain their rationale and contribute to coverage, never to the
embedding matrix. Assessment text is limited to 160 words across all change descriptions.
Embedding
token overflow produces an explicit error, not silent truncation. If it occurs,
use a suitable longer-context embedding model **for the whole comparison**.

For the default MiniLM, the sentence-embedding window is 256 tokens while its BERT
config supports 512 positions. `--embedding-max-length 512` explicitly selects that
window, including special tokens. The override is part of the embedding cache
identity, so all vectors use the same configuration. Raising the window beyond a
model's default is allowed only when its BERT config verifies the position capacity;
other architectures require a model with a sufficient default window. This changes
the measurement configuration; it is not a claim about accuracy beyond the model's
default training window.

To recover just a length failure without new LLM calls:

```bash
.venv/bin/python scripts/compare_vendi.py \
  --input results/vendi_s61_s62/samples.jsonl --reembed \
  --embedding-max-length 512 --out results/vendi_reembedded
```

`--reembed` requires text for every selected scoring sample and removes **all** old
scoring vectors and embedding errors, retaining summaries and source provenance.
Saved `no_change`/`insufficient_evidence` states remain non-scoring with empty text
and no vector. It prevents mixing
the surviving old vectors with newly generated ones. The final console output lists
failure reasons whenever coverage is incomplete.

**Earlier S61/S62 improve implementation outputs need re-extraction.** Before the
2026-09-19 reader fix, top-level `node2parent` was missed. The subsequent separate
parent/child summary comparison also missed small but consequential changes. The
2026-09-20 `diff-v1` assessment replaces that comparison with raw diff evidence.
`--input --reembed` cannot repair either representation problem. Rerun the original
sources into a new directory:

```bash
.venv/bin/python scripts/compare_vendi.py \
  --runs /Users/william/nautilus/results \
  --inventory results/9.14/run_inventory.csv \
  --run-glob '20260914_*s6[12]' --arms A F \
  --embedding-max-length 512 --out results/vendi_s61_s62_diff
```

Keep the same cache, summary model and endpoint to reuse existing proposal/draft
summaries and vectors. Diff assessments use a separate versioned `cache/vendi/changes`
namespace; old change summaries are never reused. Mixed representation versions
within one task/stage/view are rejected. Live diff assessment sends the displayed
source diff/context to the configured LLM endpoint.

The optional inventory is an allow-list, keyed by `name` (or `run_id`); it can be
the existing `run_inventory.csv` or a small CSV with `name,task,arm,pair_id`.
Task/arm can otherwise be inferred from saved config; arbitrary arm names may be
specified in the inventory. `invalid`/`superseded` inventory runs are listed in
coverage and excluded unless `--include-invalid` is supplied. Without an inventory,
run health has not been reviewed. `--runs` is authoritative for run locations;
old absolute `path` columns are not followed.

## Explicit pairing

Unpaired descriptive arm means are always available when data permit. Paired
differences require an explicit `pair_id`, for example:

```csv
name,task,arm,pair_id
my-baseline-run,competition-name,A,batch1-replicate1
my-treatment-run,competition-name,F,batch1-replicate1
```

There must be at most one run per task/pair/arm. The script never derives pairing
from seed or launch date and never borrows a baseline. Pair IDs assert matched
experimental conditions; they do not establish identical parent states or causality.
Select a comparable model/code/budget cohort in the inventory before running.

## Generic JSONL / fully offline scoring

Each line is one candidate with a **pre-normalized mechanism summary** in `text`:

```json
{"task":"my-task","run_id":"run-a","arm":"A","pair_id":"p1","candidate_id":"c1","parent_id":"","stage":"improve","view":"implementation","text":"objective: pairwise ranking; update: FIFO negative bank","status":"completed","is_valid":true}
```

Required: string `task,run_id,arm,candidate_id,stage`. Optional `view` defaults to
`implementation`; `pair_id` defaults empty. `source_refs` can hold an array of
paths/line references. `text` is already a mechanism card: the JSONL path **does not
call an LLM or normalize arbitrary prose/code**. Prepare summaries consistently
across arms. Distinct candidates with identical text remain distinct observations;
duplicate exports of the same candidate/view are merged, conflicting duplicates fail.

To avoid both LLM and embedding model calls, supply `embedding` (a numeric vector)
and `embedding_model` (one identical model/version identifier across all rows).
Either all available records have vectors or none do; vectors cannot be mixed with
text-only records. For example, replace `text` with:

```json
"embedding": [0.1, 0.3, 0.8], "embedding_model": "my-encoder@revision123"
```

```bash
.venv/bin/python scripts/compare_vendi.py \
  --input candidates.jsonl --baseline A --out results/vendi_generic
```

Previously exported `samples.jsonl` containing successful embeddings can also be
used as input. Keep the same `--stages`/`--views`, or specify the desired subset.
For assessed changes, carry `representation_version`, `assessment_status` and
`mechanism_card` forward. Non-scoring states survive import and re-embedding;
conflicting row/card states are rejected. Generic input is treated as prepared
data, not revalidated against source or certified as evidence-checked extraction.

## Statistics and outputs

Standard q=1 Vendi uses L2-normalized vectors, their cosine Gram matrix, and the
exponential entropy of its normalized eigenvalues. Negative cosine entries are
preserved. See the [official implementation](https://github.com/vertaix/Vendi-Score).

Each task/stage/view is separate. Runs with at least two available candidates form
a fixed cohort; all share `m=2..min(candidate counts)`. At each m the script enumerates
all subsets if there are at most `--repeats` (default 1,000), otherwise samples that
many subsets without replacement *within each draw*. `--seed` makes this repeatable.
Repeated draws may select the same subset. The cohort does not change along a curve.
Vendi=1 for a single vector is mathematically valid but excluded from comparisons.

The script does **not** automatically equalize time/token budgets. It retains failed
training candidates when their plan/code is available. `--valid-only` is a separate
sensitivity analysis, requiring `is_valid: true`; save it to a different output
directory. Missing summaries, missing runs and extraction failures are never zero
scores. Inspect coverage: selective failures can bias even an equal-count comparison.

Diff-based implementation Vendi measures diversity **conditional on evidenced static
changes**. Always read it together with each run's changed/no-change/insufficient
counts and fractions of all selected candidates. High conditional diversity does
not establish that an arm produces more useful changes. Entire runs with no
measurable changes remain in coverage even when they cannot produce a Vendi curve.
Parameter changes and bug fixes count as computational changes, not scientific novelty.

Outputs:

- `samples.jsonl`: canonical text, vectors, source hashes/references, extraction
  evidence and errors; no complete source code or run credentials.
- `change_evidence/*.json`: raw diff, selected context, original line references,
  source hashes and packet limitations for each assessed implementation; contains
  source excerpts and supports manual audit.
- `run_scores.csv`: matched-count Vendi per run, with candidate-subset percentiles.
- `comparisons.csv`: unpaired means, explicit paired differences and paired means.
- `coverage.csv`: candidate counts, valid/failed counts when known, missing sources,
  extraction failures, changed/no-change/insufficient counts and fractions,
  excluded runs and available inventory runtime.
- `vendi_*.png`, optionally `paired_deltas.png`: wide plots; `--no-plots` skips them.
- `manifest.json`, `REPORT.md`: settings, model identity and interpretation limits.

All comparisons are descriptive. Subset bands are **not arm-effect confidence
intervals**. There is no bootstrap significance testing or pooling across tasks.
There is no quality weighting, literature search, or claim that more diversity is
necessarily more useful. A statistically causal test still requires more independent,
well-matched experiments.

Successful LLM fragment/merge calls and embeddings are cached by content, prompt
and model identity under `cache/vendi` (override with `--cache`). Partial success
survives interruption; failed calls are retried at most three times and are not
cached as valid results. A rerun retries failures and reuses successes. Output tables
are replaced; script-generated plots are refreshed. Use separate output directories
for different comparison settings. Exit code 2 means missing representations,
extraction/embedding errors or no scoreable cohort; inspect the saved coverage/report.
`no_change` is not an extraction error; an entirely verified no-change input exits
successfully while producing coverage rather than fabricated zero scores.
Diff extraction shares its three-attempt budget between transport retries and
evidence corrections. A timeout retries the same prompt; malformed evidence gets
validation feedback. Accepted `insufficient_evidence` decisions are cached and do
not disappear merely by rerunning. Source-context packet versions are included in
cache keys, so updating context extraction consistently reassesses parent-child
implementations while retaining proposal/draft caches.

Dependencies are the existing NumPy, matplotlib, sentence-transformers, OpenAI SDK,
python-dotenv, plus PyYAML for config fallback. Pure precomputed-vector scoring with
`--no-plots` only needs NumPy. Offline checks:

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*vendi*.py' -v
```
