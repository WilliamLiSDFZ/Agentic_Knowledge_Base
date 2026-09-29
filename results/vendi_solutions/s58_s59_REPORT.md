# Complete solution Vendi

Available representations: 42/42. Run-level issues: 0.

Each non-root candidate is one complete solution, including draft, improve, debug and fusion. Only its neutral source-grounded summary is embedded. Parent differences, analogy reports, arm labels and scores are not summary inputs. Identical solutions in different candidates retain their frequency; debug retries and related descendants are correlated observations.

Within each task, runs with at least two available candidates form a fixed cohort with shared m=2..minimum candidate count. Compare s58_s59_run_scores.csv and s58_s59_comparisons.csv at matched m. s58_s59_full_run_scores.csv uses all available candidates and unequal counts are descriptive only; a singleton scores 1 but cannot enter matched comparisons. Keep different experiment versions, models, draft counts and budgets in separate invocations; budget is not automatically matched.

Failed/pending training candidates are included unless --valid-only is used (is_valid must be true). Missing source and extraction/embedding failures are not zero scores. Check coverage before interpreting differences. Source references establish provenance, not successful execution.

Vendi measures diversity, not scientific novelty or task performance. Independent runs are the experimental repeats; candidate-subset bands are NOT effect confidence intervals. Pairing requires explicit inventory pair_id, never inferred seeds. The paper embeds solution titles; our complete code summaries follow autoresearch's adaptation and are not a numerical reproduction of the paper.

## Coverage

| Run | Arm | Candidates | Available | Missing | Errors | Excluded | Stages |
|---|---|---:|---:|---:|---:|---:|---|
| 20260912_081346_jubias-anaf-gpt56sol-s58 | F | 11 | 11 | 0 | 0 | 0 | {"debug": 1, "draft": 4, "improve": 6} |
| 20260912_082030_jubias-base-gpt56sol-s59 | A | 10 | 10 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 6} |
| 20260912_082058_jubias-base-gpt56sol-s58 | A | 9 | 9 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 5} |
| 20260912_082449_jubias-anaf-gpt56sol-s59 | F | 12 | 12 | 0 | 0 | 0 | {"debug": 3, "draft": 4, "improve": 5} |

See s58_s59_solution_cards.csv for titles, summaries and evidence; s58_s59_samples.jsonl for reusable vectors; s58_s59_coverage.csv for exclusions; s58_s59_manifest.json for measurement settings and code identities.
