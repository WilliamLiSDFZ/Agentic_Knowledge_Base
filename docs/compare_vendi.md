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
- `implementation`: complete child code. When parent code exists, parent and child
  are independently summarized, then compared to emphasize the child's mechanism
  changes. The two sources remain separate through chunking and merging. Drafts
  describe the complete implementation. Missing parent context is not invented.

Summaries use six neutral English fields: model, objective, data, update, inference,
change. Arm labels, scores, paper names and analogy prose are excluded by the
extraction prompt. Code/plan references and model-produced evidence are retained
for manual audit; they are not a proof of semantic accuracy or runtime activation.
Every source character is processed: long inputs are chunked and merged. Embedding
token overflow produces an explicit error, not silent truncation. If it occurs,
use a suitable longer-context embedding model **for the whole comparison**.

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

Outputs:

- `samples.jsonl`: canonical text, vectors, source hashes/references, extraction
  evidence and errors; no complete source code or run credentials.
- `run_scores.csv`: matched-count Vendi per run, with candidate-subset percentiles.
- `comparisons.csv`: unpaired means, explicit paired differences and paired means.
- `coverage.csv`: candidate counts, valid/failed counts when known, missing sources,
  extraction failures, excluded runs and available inventory runtime.
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
for different comparison settings. Exit code 2 means extraction/embedding errors or
no scoreable cohort; inspect the saved coverage/report.

Dependencies are the existing NumPy, matplotlib, sentence-transformers, OpenAI SDK,
python-dotenv, plus PyYAML for config fallback. Pure precomputed-vector scoring with
`--no-plots` only needs NumPy. Offline checks:

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*vendi*.py' -v
```
