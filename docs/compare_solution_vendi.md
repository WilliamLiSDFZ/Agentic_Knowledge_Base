# Complete solution Vendi for MLEvolve

`scripts/compare_solution_vendi.py` measures the diversity of complete candidate
implementations, following autoresearch's solution-summary convention. It reads
existing journals without running candidate code or changing experiments.

## Run

From the AKB repository root, using the existing analysis Python environment:

```bash
# Local fetched runs. On the CPU dev pod use /workspace/MLEvolve/runs instead.
VENDI_RUNS=/Users/william/nautilus/results

python scripts/compare_solution_vendi.py \
  --runs "$VENDI_RUNS" \
  --inventory results/9.14/run_inventory.csv \
  --run-glob '20260914_*s6[12]' --arms A F \
  --summary-model gpt-5.6-terra \
  --out results/vendi_solutions --prefix s61_s62 --dry-run
```

Remove `--dry-run` to extract summaries, embed, score and plot. Dry-run reads inputs
only: no API clients, downloads, output directories or cache writes. The inventory
is an allow-list; non-`ok` verdicts are excluded unless `--include-invalid` is used.
Its old absolute path column is ignored: `--runs` supplies the current root.

To run all four downloaded cohorts sequentially into one flat folder:

```bash
bash scripts/run_solution_vendi_batches.sh --dry-run
bash scripts/run_solution_vendi_batches.sh
```

The batch script defaults to local `~/nautilus/results` and `results/vendi_solutions`.
On the CPU pod set `VENDI_RUNS=/workspace/MLEvolve/runs`; `VENDI_OUT` and
`VENDI_PYTHON` optionally select another output folder and Python interpreter.
Incomplete coverage is saved and the script continues to subsequent cohorts.

All results are in the same directory. `--prefix s61_s62` produces filenames such
as `s61_s62_REPORT.md`, `s61_s62_run_scores.csv` and `s61_s62_vendi_01.png`.
Use a different prefix for each cohort so tables and plots cannot overwrite each
other. Prefixes accept only ASCII letters, digits, underscores and hyphens;
omitting the option retains the original unprefixed filenames. Existing result
folders are not moved; reruns reuse successful cached summaries and embeddings.

Individual complete A/F cohorts can use the same inventory and output directory:

| Cohort | `--run-glob` | `--prefix` |
|---|---|---|
| S52/53 | `20260910_*s5[23]` | `s52_s53` |
| S54–56 | `20260911_07*s5[456]` | `s54_s56` |
| S58/59 | `20260912_08*jubias-*-gpt56sol-s5[89]` | `s58_s59` |

Keep different code versions, models, budgets and draft configurations in separate
invocations. The script separates tasks but does not infer experiment batches.

## Representation and models

- Each non-root journal node is one solution, including debug and fusion nodes.
  All share `stage=solution`; `original_stage` and coverage retain the stage mix.
- Complete `code` is summarized independently, with no parent/diff requirement.
  Missing code is unavailable; plans and analogy reports are never substituted.
- The neutral card has a short `title`, at most 160 English words of `summary`, and
  `SOURCE:line` evidence. Only the summary is embedded. Long code is fully read in
  32,000-character fragments, then merged in groups of at most four cards.
- Prompts exclude arm labels, scores, paper names and novelty claims. Evidence
  validates source locations, not semantic correctness or successful execution.
- Different candidates with identical code retain their frequency and reuse cached
  summaries. Only duplicate exports of the same candidate are deduplicated.

Summary requests reuse `scripts/llm.py` and its `.env` settings: `LLM_BASE_URL`,
`LLM_API_KEY` (or `OPENROUTER_API_KEY`) and `LLM_MODEL`. The example explicitly uses
`gpt-5.6-terra`. `--summary-api` defaults to `chat`; `responses` is also available.
Uncached extraction sends source fragments and intermediate cards to that endpoint.

Embedding runs on CPU with `sentence-transformers/all-MiniLM-L6-v2`, pinned to
revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, using a 512-token window.
First use may download the model. Token overflow is reported, never silently
truncated. A different model can be selected explicitly; do not mix embedding
configurations within a comparison. No GPU or separate embedding API is required.

## Comparison and interpretation

Standard q=1 cosine Vendi is computed within each run. Runs with at least two
available candidates form a fixed cohort per task and share
`m=2..minimum available candidate count`. At each m, subsets are enumerated when
there are at most `--repeats` combinations (default 1000); otherwise fixed-seed
sampling is used. Identical solutions retain their frequency.

`full_run_scores.csv` also describes all available candidates per run. Unequal-count
scores are not matched effects. A singleton has Vendi 1 but no matched comparison.
Single-draft experiments can still compare their initial and subsequent solutions
together. Debug retries and descendant versions are correlated; they are not
independent experimental repeats.

Main analysis includes failed/pending training candidates with available code.
Use `--valid-only` in a separate output directory for sensitivity analysis; it
requires the journal's `is_valid` to be exactly true. Exclusions and missing data
stay visible in coverage and never become zero scores. `is_valid` is not a new
independent verification of successful training or scoreability.

Explicit inventory `pair_id` enables descriptive paired differences. Seeds do not
create pairs automatically. Candidate-subset bands are not effect confidence
intervals. Read coverage alongside scores, especially when extraction differs by arm.
Vendi measures diversity, not scientific novelty or performance. The original AR
paper embeds solution titles with `text-embedding-3-small`; this full-code-summary
plus MiniLM adaptation does not reproduce the paper's absolute values.

## Outputs and recovery

Outputs include `solution_cards.csv`, `samples.jsonl`, `coverage.csv`,
`full_run_scores.csv`, matched `run_scores.csv`, `comparisons.csv`, wide PNG plots,
`REPORT.md` and `manifest.json`. The manifest records model settings and code hashes.
Cards retain source hashes, original stages and source-line evidence.

Caches default to `cache/vendi_solutions`. Rerun the same `--runs` command after a
timeout to reuse successful extraction. Saved complete vectors can be rescored
offline; saved summaries can be re-embedded without calling the summary LLM:

```bash
python scripts/compare_solution_vendi.py \
  --input results/vendi_solutions/s61_s62_samples.jsonl \
  --out results/vendi_solutions --prefix s61_s62_recomputed

python scripts/compare_solution_vendi.py \
  --input results/vendi_solutions/s61_s62_samples.jsonl --reembed \
  --out results/vendi_solutions --prefix s61_s62_reembedded
```

Only `solution-v1` inputs are accepted. Old proposal/diff summaries and vectors
cannot be reused; regenerate from raw journals. Use a new output directory rather
than overwriting old change-based results. Missing summaries require a `--runs`
rerun, since `samples.jsonl` intentionally omits full source. Partly embedded input
requires `--reembed` so all surviving summaries use one configuration.

Exit 0 means scoring completed; exit 2 indicates missing/extraction failures or
insufficient candidates for matched scoring. Inspect coverage in either case.

```bash
python -m unittest discover -s tests -p 'test_*vendi*.py' -v
```
