# KB ablation — per-task effects

Scores are graded against mle-bench private answers (`MLEvolve/utils/grade_all.py`). The agent's own validation metric is not used anywhere here: arms hold out different data, so it is not comparable across arms.

## essay

4 usable draw(s), compared at K=1. 3 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 4 | +0.00617 | [-0.05827, +0.07061] | ++-- | **CI contains zero — no detectable effect** |
| C-A | 4 | +0.01225 | [-0.03421, +0.05871] | +++- | **CI contains zero — no detectable effect** |
| C-B | 4 | +0.00608 | [-0.01334, +0.02550] | --++ | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **525 draws** (12599 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **273 draws** (6549 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **48 draws** (1145 GPU-hours at 12 h/run, 2 arms).

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

## lmsys

5 usable draw(s), compared at K=1. 4 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 4 | -0.00940 | [-0.05408, +0.03528] | --++ | **CI contains zero — no detectable effect** |
| C-A | 3 | +0.00462 | [-0.04318, +0.05243] | -+- | **CI contains zero — no detectable effect** (unpaired) |
| C-B | 2 | +0.00308 | [-0.13725, +0.14342] | -+ | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **252 draws** (6057 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **118 draws** (2843 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **78 draws** (1874 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
