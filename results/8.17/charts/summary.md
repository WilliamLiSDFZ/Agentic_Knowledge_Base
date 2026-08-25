# KB ablation — per-task effects

Scores are graded against mle-bench private answers (`MLEvolve/utils/grade_all.py`). The agent's own validation metric is not used anywhere here: arms hold out different data, so it is not comparable across arms.

## essay

2 usable draw(s), compared at K=1. 3 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 2 | +0.03502 | [-0.26815, +0.33819] | ++ | **CI contains zero — no detectable effect** |
| C-A | 2 | +0.03095 | [-0.23181, +0.29371] | ++ | **CI contains zero — no detectable effect** |
| C-B | 2 | -0.00407 | [-0.04448, +0.03634] | -- | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **364 draws** (8744 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
- `C-A`: to detect 0.005 at ~80% power needs **274 draws** (6569 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
- `C-B`: to detect 0.005 at ~80% power needs **6 draws** (155 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*

## jigsaw

3 usable draw(s), compared at K=2. 3 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 3 | -0.01090 | [-0.03704, +0.01525] | +-- | **CI contains zero — no detectable effect** (unpaired) |
| C-A | 3 | -0.00146 | [-0.01844, +0.01551] | +-- | **CI contains zero — no detectable effect** (unpaired) |
| C-B | 3 | +0.00943 | [-0.00331, +0.02217] | +++ | **CI contains zero — no detectable effect** |

- `B-A`: to detect 0.005 at ~80% power needs **35 draws** (851 GPU-hours at 12 h/run, 2 arms).
- `C-A`: to detect 0.005 at ~80% power needs **15 draws** (359 GPU-hours at 12 h/run, 2 arms).
- `C-B`: to detect 0.005 at ~80% power needs **8 draws** (202 GPU-hours at 12 h/run, 2 arms).

## lmsys

2 usable draw(s), compared at K=1. 2 run(s) excluded.

| contrast | n | mean | 95% CI | signs | verdict |
|---|---:|---:|---|---|---|
| B-A | 2 | -0.02612 | [-0.33685, +0.28460] | -- | **CI contains zero — no detectable effect** |
| C-A | 1 | -0.00963 | — | - | n=1, no interval |
| C-B | 1 | -0.00796 | — | - | n=1, no interval |

- `B-A`: to detect 0.005 at ~80% power needs **383 draws** (9186 GPU-hours at 12 h/run, 2 arms).  *(from n=2 — sd has 1 df, treat as a rough order of magnitude only)*
