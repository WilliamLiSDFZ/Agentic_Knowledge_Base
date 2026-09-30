# Complete solution Vendi

Available representations: 166/166; scored runs: 18; complete explicit pairs: 9.

Each non-root candidate contributes its complete code's neutral summary, including draft, improve, debug and fusion. Identical implementations in distinct candidates retain their frequency. Summary text alone is embedded; titles, arm labels, analogy reports, parents and scores are excluded.

Runs with at least two available candidates use a shared m=2..minimum count across ALL batches within each task. Vendi is calculated inside each run, never by pooling candidates across runs. Batch identities remain separate: there is no cross-version overall effect. Explicit pairs come from the run manifest, not inferred seeds. Job pairing does not match realized hardware or search paths.

vendi.csv contains every run curve; effect.csv contains within-batch pair differences (or descriptive unpaired means when no complete pair exists); paired.csv contains explicit A/F endpoints at the task's largest shared m. Each has a PNG/PDF figure unless --no-plots is used. comparisons.csv also retains unmatched pairs and batch means. full_run_scores.csv uses all available candidates and is descriptive when counts differ.

Vendi measures diversity, not novelty or task performance. Runs are experimental repeats; related candidates are correlated. Candidate-subset bands in run_scores.csv are NOT confidence intervals for an arm effect. Failed training candidates remain included unless --valid-only is used. Missing sources, failed representations and excluded records are visible in coverage.csv, never zero scores.

## Coverage

| Batch | Run | Arm | Candidates | Available | Missing | Errors | Excluded | Issue |
|---|---|---|---:|---:|---:|---:|---:|---|
| s52_s53 | 20260910_022413_jubias-base-s53 | A | 7 | 7 | 0 | 0 | 0 |  |
| s52_s53 | 20260910_022912_jubias-anaf-s53 | F | 7 | 7 | 0 | 0 | 0 |  |
| s52_s53 | 20260910_022943_jubias-anaf-s52 | F | 6 | 6 | 0 | 0 | 0 |  |
| s52_s53 | 20260910_022953_jubias-base-s52 | A | 7 | 7 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_071931_jubias-base-s54 | A | 8 | 8 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_072108_jubias-base-s55 | A | 8 | 8 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_072344_jubias-base-s56 | A | 11 | 11 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_072611_jubias-anaf-s55 | F | 14 | 14 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_072611_jubias-anaf-s56 | F | 11 | 11 | 0 | 0 | 0 |  |
| s54_s56 | 20260911_072808_jubias-anaf-s54 | F | 7 | 7 | 0 | 0 | 0 |  |
| s58_s59 | 20260912_081346_jubias-anaf-gpt56sol-s58 | F | 11 | 11 | 0 | 0 | 0 |  |
| s58_s59 | 20260912_082030_jubias-base-gpt56sol-s59 | A | 10 | 10 | 0 | 0 | 0 |  |
| s58_s59 | 20260912_082058_jubias-base-gpt56sol-s58 | A | 9 | 9 | 0 | 0 | 0 |  |
| s58_s59 | 20260912_082449_jubias-anaf-gpt56sol-s59 | F | 12 | 12 | 0 | 0 | 0 |  |
| s61_s62 | 20260914_062456_jubias-base-gpt56sol-s61 | A | 10 | 10 | 0 | 0 | 0 |  |
| s61_s62 | 20260914_070227_jubias-base-gpt56sol-s62 | A | 13 | 13 | 0 | 0 | 0 |  |
| s61_s62 | 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 8 | 8 | 0 | 0 | 0 |  |
| s61_s62 | 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 7 | 7 | 0 | 0 | 0 |  |

See solution_cards.csv for summaries and evidence, samples.jsonl for reusable vectors, and manifest.json for measurement settings, input/code hashes and pairing metadata.
