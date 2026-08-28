---
license: apache-2.0
language: [en]
tags:
  - machine-learning-engineering
  - retrieval-augmented-generation
  - mle-bench
  - agents
pretty_name: MLEvolve external knowledge base — corpus, index and experiment runs
size_categories: [10K<n<100K]
---

# MLEvolve external knowledge base — corpus, retrieval index and experiment runs

Companion data for two repositories:

- [`Agentic_Knowledge_Base`](https://github.com/WilliamLiSDFZ/Agentic_Knowledge_Base) — builds the
  knowledge base and analyses the experiments
- [`MLEvolve-externalKB`](https://github.com/WilliamLiSDFZ/MLEvolve-externalKB) — the agent that
  consumes it

**The question this data is trying to answer:** does knowledge extracted from *research papers*
make an ML-engineering agent better? Prior work such as AutoMind draws mainly on Kaggle forum
write-ups; this system uses papers only, which is the difference it is trying to isolate.

**Current answer: no effect is detectable yet, and the most useful evidence is diagnostic rather
than a score.** See [Results](#what-the-data-currently-shows) before drawing conclusions from the
raw files — a majority of the runs are not usable, and the reasons are recorded.

---

## Contents

| path | size | what it is |
|---|---|---|
| `output/{venue}-{year}/` | 96 MB | topic-clustered paper corpus: `SKILL.md` index + one `references/*.md` per paper (abstract, tags, TLDR, source URL) |
| `output/abstract_index/` | ~110 MB | **the retrieval index the agent actually queries** — `records.jsonl`, `embeddings.npy`, `manifest.json` |
| `methodology_kb/{venue}-{year}/` | 2.7 MB | per-paper technique extraction from full PDFs, with `[POSITIVE]` / `[NEGATIVE]` labels, `Delta`, `Condition` and an evidence quote |
| `runs/` | 1.4 GB | 70 MLEvolve run directories + `scores.csv` |
| `analysis/` | ~7 MB | derived tables and figures, left unpacked so they render in the web UI |

### Corpus composition

| venue | categories | papers |
|---|---:|---:|
| neurips-2024 | 80 | 7,886 |
| aaai-2024 | 77 | 5,097 |
| icml-2024 | 160 | 4,839 |
| acl-2024 | 160 | 3,526 |
| naacl-2024 | 106 | 1,818 |
| **total** | | **23,166** |

Only these five venues are built. The pipeline supports eight (CVPR, ICCV and ICLR are
implemented but were never run), so anything describing this corpus as covering eight conferences
is out of date. 223 papers have full-PDF technique extraction; the rest are abstract-level only.

---

## The index is the important file

`output/abstract_index/` is the only artifact here that is in neither git repository, and it is
the one that determines what retrieval returns.

**`manifest.json` is a contract.** It records the embedding model, dimension, record count and
schema version. A consumer must instantiate the *same* model and build its FAISS index from
`embeddings.npy`. Using a different model on one side does not fail — it silently degrades
retrieval, which is much worse.

Two non-obvious properties of this index, both of which were measured rather than assumed:

- **Vectors are mean-centred at query time.** Every paper in the corpus is an ML paper, so every
  embedding shares a large common component that swamps topic signal. Subtracting the corpus mean
  is what makes the scores discriminate.
- **The query is an LLM-distilled task summary, not the raw competition description.** The raw
  description is mostly rules, prizes and submission formats. Distilling first, and centring,
  together took on-topic papers in the top 10 from 3 to 9.

---

## `runs/` — read `run_inventory.csv` first

70 run directories. **Only 40 are usable.**

| verdict | count | meaning |
|---|---:|---|
| `ok` | 40 | usable |
| `invalid` | 23 | the run itself is broken — rate-limited mid-run, pod preempted, or no submission produced |
| `superseded` | 7 | the run is fine, but it exercises pre-2026-08-08 prompt-injection code and cannot be pooled with the rest |

`analysis/*/run_inventory.csv` carries the verdict and the reason for every run. Starting from the
raw directories instead will produce wrong conclusions — the `invalid` runs look normal from the
outside.

Each run directory contains:

```
logs/
  journal.json            every search node: plan, code, metric, is_valid, is_buggy, stage
  config.yaml             the full resolved config — this is where the ARM comes from
  MLEvolve.log            the run log
  best_solution.py        the single best solution (see the warning below)
  injected_knowledge.md   the exact techniques this run received  (27 runs)
  kb_snapshot.json        which venues/years the corpus held at run start  (future runs only)
workspace/
  ensembles_csv/          fused submissions, named top{K}ens-total_run_time{H}h.csv
```

### Vocabulary

- **Arms** — `A` = no knowledge base, `B` = knowledge at drafting, `C` = knowledge at drafting and
  improvement. Recovered from `logs/config.yaml`, never from the directory name.
- **Draw** — one launch batch: a cluster of start times **and** a single `agent.seed`. Neither key
  works alone. `agent.seed` does not reproduce a run — it seeds the generated candidate code, not
  the agent's search, and the LLM is sampled — so two batches a week apart at the same seed are
  two independent draws. Conversely two batches launched 30 minutes apart at different seeds are
  also two draws.
- **Matched K** — arms are compared only at the same ensemble size. Arms stop fusing at different
  sizes because they can afford different numbers of candidates, so comparing across K measures
  fusion budget rather than knowledge.

### `scores.csv`

459 rows, graded against MLE-bench private answers. Columns: `run, competition, variant, k,
cum_hours, score, medal, lower_better, file, note`.

`variant` is `capped` (the original 9-hour cumulative-training-time fusion budget) or `uncapped`
(a replay with that budget lifted). **Never compare arms across variants.** Lifting the cap turned
out not to change the ranking of the arms, which is a useful negative result about the evaluation
protocol rather than about the knowledge base.

---

## What the data currently shows

**No score contrast has a confidence interval that excludes zero**, on any task, at n = 4–5 draws.

| task | usable draws | best contrast | mean | 95% CI |
|---|---:|---|---:|---|
| jigsaw | 4 | C − B | +0.0062 AUC | [−0.0045, +0.0170] |
| essay | 5 | C − A | +0.0123 QWK | [−0.034, +0.059] |
| lmsys | 5 | B − A | −0.0094 log loss | [−0.054, +0.035] |

The reason is not only sample size. The baseline's own run-to-run variance is larger than the
effect being measured — on essay the paired sd is 0.038 QWK, which puts a 0.005 effect several
hundred draws away. A Meta study of this benchmark ([arXiv:2507.02554](https://arxiv.org/abs/2507.02554))
reaches the same conclusion independently and recommends 10–20 seeds per competition rather than
the usual 3.

### The informative result is about adoption, not score

Judging every generated solution against every injected technique (`adoption.csv`, 4,488
judgements over 15 runs) shows that whether the knowledge is used at all depends almost entirely
on the task:

| task | nodes adopting ≥1 technique | fully implemented | weakened proxy |
|---|---:|---:|---:|
| jigsaw | **3 / 89 (3%)** | 0 | 3 |
| essay | 92 / 105 (88%) | **1** | 114 |
| lmsys | **178 / 180 (99%)** | 209 | 141 |

Three different failure modes:

- **jigsaw — the knowledge is never used.** Half the retrieved techniques are multimodal
  meme-detection methods (`Fine-tuned CLIP multimodal encoder`, `Image captions for
  targeted-harmful memes`). Retrieval matched on "toxicity" and returned things a text-only
  competition cannot execute.
- **essay — used, but degraded.** Techniques requiring annotated argument structure, which the
  competition does not provide, were reimplemented as keyword regexes. 114 proxies, 1 full.
- **lmsys — fully implemented, and still no score effect.** This rules out "the model ignores the
  prompt" as an explanation and points at the techniques themselves.

An LLM judged these labels; they have not been human-validated, so treat the exact numbers as
indicative.

---

## Reproducing

```bash
git clone https://github.com/WilliamLiSDFZ/Agentic_Knowledge_Base
cd Agentic_Knowledge_Base && pip install -r requirements.txt

# retrieval, without running an agent (seconds)
python scripts/probe_retrieval.py --task <competition description>.md --all

# validity filtering, effect sizes and figures
python scripts/analyze_runs.py --runs <path to runs/> \
    --scores <path to runs/scores.csv> --charts

# which models each run actually used, across all nodes
python scripts/show_models.py --runs <path to runs/> --task jigsaw
```

### One warning worth repeating

Do **not** characterise a run from `logs/best_solution.py`. It is one solution out of roughly
twenty. Doing exactly that produced a confident and wrong conclusion here — that a knowledge-base
arm had "abandoned transformers for TF-IDF" — when 18 of that run's 19 nodes contained a
transformer and only its single best-scoring node happened not to. Use `journal.json`, which has
every node.

---

## Citation and licence

Corpus built from publicly available conference proceedings (NeurIPS, ICML, ACL, NAACL, AAAI);
individual papers remain under their original licences. Pipeline code and derived artifacts are
Apache 2.0. Original pipeline by **Haoming Wang**; retrieval, analysis and MLEvolve integration by
**Yuze Li**.
