# KB ablation — per-task effects

Scores are graded against mle-bench private answers (`MLEvolve/utils/grade_all.py`). The agent's own validation metric is not used anywhere here: arms hold out different data, so it is not comparable across arms.

Jigsaw Unintended Bias uses the corrected `jubias-continuous-auc-v1` metric (continuous predictions). Legacy scores that thresholded predictions at 0.5 must not be compared with these results.

## jigsaw-unintended-bias-in-toxicity-classification

1 usable draw(s), compared at K=1. 2 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| G-A | 1 | -0.09056 | — | - | n=1, no interval |

