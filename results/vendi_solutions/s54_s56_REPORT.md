# Complete solution Vendi

Available representations: 59/59. Run-level issues: 0.

Each non-root candidate is one complete solution, including draft, improve, debug and fusion. Only its neutral source-grounded summary is embedded. Parent differences, analogy reports, arm labels and scores are not summary inputs. Identical solutions in different candidates retain their frequency; debug retries and related descendants are correlated observations.

Within each task, runs with at least two available candidates form a fixed cohort with shared m=2..minimum candidate count. Compare s54_s56_run_scores.csv and s54_s56_comparisons.csv at matched m. s54_s56_full_run_scores.csv uses all available candidates and unequal counts are descriptive only; a singleton scores 1 but cannot enter matched comparisons. Keep different experiment versions, models, draft counts and budgets in separate invocations; budget is not automatically matched.

Failed/pending training candidates are included unless --valid-only is used (is_valid must be true). Missing source and extraction/embedding failures are not zero scores. Check coverage before interpreting differences. Source references establish provenance, not successful execution.

Vendi measures diversity, not scientific novelty or task performance. Independent runs are the experimental repeats; candidate-subset bands are NOT effect confidence intervals. Pairing requires explicit inventory pair_id, never inferred seeds. The paper embeds solution titles; our complete code summaries follow autoresearch's adaptation and are not a numerical reproduction of the paper.

## Coverage

| Run | Arm | Candidates | Available | Missing | Errors | Excluded | Stages |
|---|---|---:|---:|---:|---:|---:|---|
| 20260911_071931_jubias-base-s54 | A | 8 | 8 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 4} |
| 20260911_072108_jubias-base-s55 | A | 8 | 8 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 4} |
| 20260911_072344_jubias-base-s56 | A | 11 | 11 | 0 | 0 | 0 | {"debug": 3, "draft": 4, "improve": 4} |
| 20260911_072611_jubias-anaf-s55 | F | 14 | 14 | 0 | 0 | 0 | {"debug": 4, "draft": 4, "improve": 6} |
| 20260911_072611_jubias-anaf-s56 | F | 11 | 11 | 0 | 0 | 0 | {"debug": 1, "draft": 5, "improve": 5} |
| 20260911_072808_jubias-anaf-s54 | F | 7 | 7 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 3} |

See s54_s56_solution_cards.csv for titles, summaries and evidence; s54_s56_samples.jsonl for reusable vectors; s54_s56_coverage.csv for exclusions; s54_s56_manifest.json for measurement settings and code identities.
