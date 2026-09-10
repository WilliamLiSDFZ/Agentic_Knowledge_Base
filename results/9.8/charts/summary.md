# KB ablation — per-task effects

Scores are graded against mle-bench private answers (`MLEvolve/utils/grade_all.py`). The agent's own validation metric is not used anywhere here: arms hold out different data, so it is not comparable across arms.

Jigsaw Unintended Bias uses the corrected `jubias-continuous-auc-v1` metric (continuous predictions). Legacy scores that thresholded predictions at 0.5 must not be compared with these results.

## essay

8 usable draw(s), compared at K=1. 14 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 7 | +0.00212 | [-0.02269, +0.02692] | ++----- | **CI contains zero — no detectable effect** |
| C-A | 7 | +0.00258 | [-0.02062, +0.02578] | +++---- | **CI contains zero — no detectable effect** |
| C-B | 7 | +0.00046 | [-0.01182, +0.01275] | --+-++- | **CI contains zero — no detectable effect** |
| D-A | 1 | -0.00238 | — | - | n=1, no interval |

- `B-A`: to detect 0.005 at ~80% power needs **230 draws** (5525 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **201 draws** (4834 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **56 draws** (1355 GPU-hours at 12 h/run, 2 arms).

## jigsaw

4 usable draw(s), compared at K=1. 3 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 4 | -0.00518 | [-0.02714, +0.01679] | +--+ | **CI contains zero — no detectable effect** (unpaired) |
| C-A | 4 | +0.00105 | [-0.01260, +0.01470] | +--+ | **CI contains zero — no detectable effect** (unpaired) |
| C-B | 4 | +0.00623 | [-0.00450, +0.01695] | +++- | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **61 draws** (1464 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **24 draws** (565 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **15 draws** (349 GPU-hours at 12 h/run, 2 arms).

## jigsaw-unintended-bias-in-toxicity-classification

9 usable draw(s), compared at K=1. 18 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 2 | +0.11351 | [-0.48926, +0.71628] | ++ | **CI contains zero — no detectable effect** |
| C-A | 1 | +0.10583 | — | + | n=1, no interval |
| C-B | 1 | -0.05512 | — | - | n=1, no interval |
| D-A | 4 | -0.00234 | [-0.27100, +0.26633] | +--+ | **CI contains zero — no detectable effect** (unpaired) |
| E-A | 3 | -0.00711 | [-0.03091, +0.01670] | +-- | **CI contains zero — no detectable effect** (unpaired) |

- `B-A`: to detect 0.005 at ~80% power needs **1440 draws** (34569 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
- `D-A`: to detect 0.005 at ~80% power needs **9125 draws** (218995 GPU-hours at 12 h/run, 2 arms).
- `E-A`: to detect 0.005 at ~80% power needs **29 draws** (705 GPU-hours at 12 h/run, 2 arms).

## lmsys

6 usable draw(s), compared at K=1. 5 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 5 | -0.00954 | [-0.03973, +0.02065] | --++- | **CI contains zero — no detectable effect** |
| C-A | 3 | +0.00113 | [-0.05370, +0.05595] | -+- | **CI contains zero — no detectable effect** (unpaired) |
| C-B | 2 | +0.00308 | [-0.13725, +0.14342] | -+ | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **189 draws** (4543 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **156 draws** (3740 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **78 draws** (1874 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
