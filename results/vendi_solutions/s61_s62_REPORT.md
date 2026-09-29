# Complete solution Vendi

Available representations: 38/38. Run-level issues: 1.

Each non-root candidate is one complete solution, including draft, improve, debug and fusion. Only its neutral source-grounded summary is embedded. Parent differences, analogy reports, arm labels and scores are not summary inputs. Identical solutions in different candidates retain their frequency; debug retries and related descendants are correlated observations.

Within each task, runs with at least two available candidates form a fixed cohort with shared m=2..minimum candidate count. Compare s61_s62_run_scores.csv and s61_s62_comparisons.csv at matched m. s61_s62_full_run_scores.csv uses all available candidates and unequal counts are descriptive only; a singleton scores 1 but cannot enter matched comparisons. Keep different experiment versions, models, draft counts and budgets in separate invocations; budget is not automatically matched.

Failed/pending training candidates are included unless --valid-only is used (is_valid must be true). Missing source and extraction/embedding failures are not zero scores. Check coverage before interpreting differences. Source references establish provenance, not successful execution.

Vendi measures diversity, not scientific novelty or task performance. Independent runs are the experimental repeats; candidate-subset bands are NOT effect confidence intervals. Pairing requires explicit inventory pair_id, never inferred seeds. The paper embeds solution titles; our complete code summaries follow autoresearch's adaptation and are not a numerical reproduction of the paper.

## Coverage

| Run | Arm | Candidates | Available | Missing | Errors | Excluded | Stages |
|---|---|---:|---:|---:|---:|---:|---|
| 20260914_062456_jubias-base-gpt56sol-s61 | A | 10 | 10 | 0 | 0 | 0 | {"debug": 3, "draft": 4, "improve": 3} |
| 20260914_070227_jubias-base-gpt56sol-s62 | A | 13 | 13 | 0 | 0 | 0 | {"debug": 2, "draft": 5, "fusion_draft": 1, "improve": 5} |
| 20260914_070253_jubias-anaf-gpt56sol-s62 | F | 8 | 8 | 0 | 0 | 0 | {"draft": 3, "improve": 5} |
| 20260914_070847_jubias-anaf-gpt56sol-s61 | F | 7 | 7 | 0 | 0 | 0 | {"debug": 1, "draft": 3, "improve": 3} |

See s61_s62_solution_cards.csv for titles, summaries and evidence; s61_s62_samples.jsonl for reusable vectors; s61_s62_coverage.csv for exclusions; s61_s62_manifest.json for measurement settings and code identities.
