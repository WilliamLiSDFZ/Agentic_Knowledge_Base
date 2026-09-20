# Vendi diversity comparison

Available representations: 61/62. Run-level issues: 1.

Each task/stage/view is separate. Candidate count is matched within a fixed cohort of runs with at least two available candidates. Missing/failed extraction can bias this cohort: inspect coverage.csv before interpreting comparisons. Failed training candidates are retained unless --valid-only was specified. Budget is not automatically matched.

Explicit pair_id is required for paired differences; matching seeds alone does not pair runs. All differences are descriptive, without significance claims. Subset bands are NOT effect confidence intervals. Vendi measures embedding diversity, not scientific novelty or runtime activation. No baseline is borrowed and no tasks are pooled.

Diff-based implementation Vendi is CONDITIONAL on evidenced static changes. No-change and insufficient-evidence candidates are counted separately, never embedded as refusal text or given Vendi=0. Read changed/no-change/insufficient rates in coverage.csv alongside scores: high conditional diversity alone does not imply high exploration productivity. Runs with no measurable changes remain in coverage even when no score can be computed. Validated quotes establish source provenance, not semantic correctness or observed runtime activation. Each change's full diff/context is saved under change_evidence/.

See samples.jsonl for source references and extraction evidence; manifest.json pins the settings/model identity. Reusing a changed input updates these tables; use a new output directory when comparing different settings.

## Coverage, including runs without a score

| Task / stage / view | Run | Arm | Candidates | Available | Changed | No change | Insufficient | Missing / errors |
|---|---|---|---:|---:|---:|---:|---:|---:|
| jigsaw-unintended-bias-in-toxicity-classification / draft / implementation | 20260914_062456_jubias-base-gpt56sol-s61 | A | 4 | 4 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / proposal | 20260914_062456_jubias-base-gpt56sol-s61 | A | 4 | 4 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / implementation | 20260914_062456_jubias-base-gpt56sol-s61 | A | 3 | 2 | 2 | 0 | 1 | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / proposal | 20260914_062456_jubias-base-gpt56sol-s61 | A | 3 | 3 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / implementation | 20260914_070227_jubias-base-gpt56sol-s62 | A | 5 | 5 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / proposal | 20260914_070227_jubias-base-gpt56sol-s62 | A | 5 | 5 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / implementation | 20260914_070227_jubias-base-gpt56sol-s62 | A | 5 | 5 | 5 | 0 | 0 | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / proposal | 20260914_070227_jubias-base-gpt56sol-s62 | A | 5 | 5 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / implementation | 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 3 | 3 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / proposal | 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 3 | 3 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / implementation | 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 5 | 5 | 5 | 0 | 0 | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / proposal | 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 5 | 5 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / implementation | 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 3 | 3 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / draft / proposal | 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 3 | 3 | — | — | — | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / implementation | 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 3 | 3 | 3 | 0 | 0 | 0 / 0 |
| jigsaw-unintended-bias-in-toxicity-classification / improve / proposal | 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 3 | 3 | — | — | — | 0 / 0 |
