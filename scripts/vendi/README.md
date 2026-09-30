# Complete solution Vendi

Run `scripts/compare_solution_vendi.py` from the repository root with the project
Python environment activated. This package contains input handling (`reader.py`),
summary extraction and embeddings (`runtime.py`), scoring (`metrics.py`), and
figures (`reporting.py`).

## Run the analysis

To regenerate the unified analysis from saved summaries and vectors:

```bash
python scripts/compare_solution_vendi.py \
  --input result/vendi_solutions/samples.jsonl
```

With existing vectors this is offline: no LLM calls or embedding-model download.
Add `--reembed` to encode saved summaries again on CPU; this needs the embedding
model locally or a model download, but makes no LLM calls.

To extract complete solutions from fetched experiments:

```bash
python scripts/compare_solution_vendi.py \
  --runs ~/nautilus/results \
  --manifest scripts/vendi/jigsaw_runs.csv \
  --summary-model gpt-5.6-terra
```

On the CPU dev pod, use `--runs /workspace/MLEvolve/runs`. The bundled manifest
selects 18 runs forming nine A/F pairs: S52–53, S54–56, S58–59, and S61–62.
Its `paired_job` column references the paired YAML in MLEvolve. The pairs were
checked against saved run configurations and the 9.14 inventory; resource
requests match, but actual GPU assignments are not controlled.
Append `--dry-run` to check selection without model calls, downloads, or writes.
Uncached summaries use the provider configured through `scripts/llm.py` and `.env`.
Successful summaries and embeddings reuse `cache/vendi_solutions`, including caches
created before the package move. CPU is sufficient.

For older batch exports without batch metadata, combine them with the manifest:

```bash
python scripts/compare_solution_vendi.py \
  --input results/vendi_solutions/*_samples.jsonl \
  --manifest scripts/vendi/jigsaw_runs.csv
```

Only complete `solution-v1` representations are accepted.

## Outputs

Everything goes into `result/vendi_solutions/` by default:

- `vendi.png/.pdf/.csv`: all run curves on one coordinate system per task;
  pair colors and arm line styles distinguish experiments.
- `effect.png/.pdf/.csv`: all pair differences on one coordinate system per task,
  retaining batch labels and the same pair colors as the Vendi figure.
- `paired.png/.pdf/.csv`: explicit paired endpoints at the shared candidate count.
- `coverage.csv`, `solution_cards.csv`, `samples.jsonl`, `manifest.json`, and
  `REPORT.md`: coverage, evidence, reusable representations, and provenance.
- `run_scores.csv`, `comparisons.csv`, `full_run_scores.csv`: detailed scores.

Check coverage before interpreting results; missing representations never become
zero scores. Repeating the raw-run command retries failed extraction using caches.

## Add experiments and interpret scores

Supply your own CSV through `--manifest`, with `name` (run-directory name), `task`,
`arm`, `batch`, and optional `pair_id`. Saved inputs require batch metadata unless
a manifest supplies it. Assign different experiment versions to different batches.
Set matching pair IDs only for explicitly paired Jobs; seeds alone do not establish
pairing. Paired Jobs can still run on different hardware.

All batches of one task share the candidate-count range, but effects stay within
their batches. Candidates are never pooled across runs. Each non-root candidate
contributes its complete implementation, including debug/fusion and failed attempts;
repeated solutions retain their frequency. Vendi measures diversity, not quality or
scientific novelty. Candidate-subset variability is not an effect confidence interval.
