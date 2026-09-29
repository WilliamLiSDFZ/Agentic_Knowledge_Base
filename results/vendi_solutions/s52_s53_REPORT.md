# Complete solution Vendi

Available representations: 27/27. Run-level issues: 0.

Each non-root candidate is one complete solution, including draft, improve, debug and fusion. Only its neutral source-grounded summary is embedded. Parent differences, analogy reports, arm labels and scores are not summary inputs. Identical solutions in different candidates retain their frequency; debug retries and related descendants are correlated observations.

Within each task, runs with at least two available candidates form a fixed cohort with shared m=2..minimum candidate count. Compare s52_s53_run_scores.csv and s52_s53_comparisons.csv at matched m. s52_s53_full_run_scores.csv uses all available candidates and unequal counts are descriptive only; a singleton scores 1 but cannot enter matched comparisons. Keep different experiment versions, models, draft counts and budgets in separate invocations; budget is not automatically matched.

Failed/pending training candidates are included unless --valid-only is used (is_valid must be true). Missing source and extraction/embedding failures are not zero scores. Check coverage before interpreting differences. Source references establish provenance, not successful execution.

Vendi measures diversity, not scientific novelty or task performance. Independent runs are the experimental repeats; candidate-subset bands are NOT effect confidence intervals. Pairing requires explicit inventory pair_id, never inferred seeds. The paper embeds solution titles; our complete code summaries follow autoresearch's adaptation and are not a numerical reproduction of the paper.

## Coverage

| Run | Arm | Candidates | Available | Missing | Errors | Excluded | Stages |
|---|---|---:|---:|---:|---:|---:|---|
| 20260910_022413_jubias-base-s53 | A | 7 | 7 | 0 | 0 | 0 | {"debug": 4, "draft": 3} |
| 20260910_022912_jubias-anaf-s53 | F | 7 | 7 | 0 | 0 | 0 | {"debug": 4, "draft": 3} |
| 20260910_022943_jubias-anaf-s52 | F | 6 | 6 | 0 | 0 | 0 | {"debug": 3, "draft": 3} |
| 20260910_022953_jubias-base-s52 | A | 7 | 7 | 0 | 0 | 0 | {"debug": 4, "draft": 3} |

See s52_s53_solution_cards.csv for titles, summaries and evidence; s52_s53_samples.jsonl for reusable vectors; s52_s53_coverage.csv for exclusions; s52_s53_manifest.json for measurement settings and code identities.
