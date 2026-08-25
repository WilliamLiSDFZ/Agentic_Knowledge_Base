# Agentic Knowledge Base

Turns conference papers into knowledge that an ML-engineering agent can retrieve at run time, and
measures whether that knowledge actually helps.

This is the **offline half of a two-repo system**. The other half is **MLEvolve**, an agent that
solves Kaggle-style competitions by Monte Carlo Graph Search; at cold start it queries the indexes
built here. The research question is whether *research papers* — as opposed to Kaggle forum
write-ups, which is what prior work such as AutoMind uses — make the agent better.

Four tiers, in dependency order:

| tier | what it does | scripts |
|---|---|---|
| 1. Core pipeline | scrape abstracts → cluster into ~80 topics → LLM-classify → topic "skills" | `1_fetch` … `4_generate_skills` |
| 2. Methodology KB | per-paper technique extraction from full PDFs, plus cross-paper synthesis | `5_build_methodology`, `plugin_a*` |
| 3. Retrieval indexes | the cross-repo contract MLEvolve queries | `6_build_abstract_index`, `build_retrieval_index`, `probe_retrieval` |
| 4. Experiment analysis | decides what the MLEvolve runs actually support | `analyze_runs`, `plot_effects`, `measure_adoption`, `show_models` |

Tiers 1–3 are pipeline code. Tier 4 is measurement code and is held to a different standard —
see [Analysis](#analysis).

---

## Core pipeline

1. Fetch paper titles and abstracts from conference proceedings
2. Embed abstracts and cluster them into ~80 topic categories
3. Classify each paper into 1–3 categories with tags and a one-line summary
4. Write a `SKILL.md` index plus one reference file per paper

| Conference | Source |
|---|---|
| NeurIPS | papers.nips.cc |
| ICML | proceedings.mlr.press |
| CVPR / ICCV | openaccess.thecvf.com |
| ACL / NAACL | aclanthology.org |
| ICLR | OpenReview API |
| AAAI | Semantic Scholar API |

Note ICCV is biennial (odd years only).

```bash
bash run_all.sh neurips 2024          # one venue, resumes if interrupted at steps 2-4

python scripts/1_fetch.py           --venue icml --year 2024
python scripts/2_embed_cluster.py   --venue icml --year 2024
python scripts/3_classify.py        --venue icml --year 2024 --workers 8
python scripts/4_generate_skills.py --venue icml --year 2024
```

Cluster granularity is `N_CLUSTERS` in `scripts/2_embed_cluster.py` (default 80; higher = finer).

Output:

```
output/neurips-2024/
└── diffusion-models-image-generation/
    ├── SKILL.md          # description + index table (title, tags, file)
    └── references/*.md   # abstract, tags, TLDR, source URL
```

---

## Retrieval

This is where most of the recent work went, and where the measurable improvements are.

### Two problems that were fixed

**Query dilution.** Retrieval used to embed the whole competition description, which is mostly
rules, prize structure and submission-file formats. The resulting vector was diffuse. It is now
distilled by one cached LLM call into a 50–80 word statement of the ML problem.

**Embedding anisotropy.** Every paper in the corpus is an ML paper, so every vector shares a large
common component that swamps the topic signal. Subtracting the corpus mean before comparing fixes
this.

Measured together, on-topic papers in the top 10 went from **3 to 9**. Each fix was validated on a
second, structurally different task before being kept — an earlier rule-based query extractor
scored 10/10 on the task it was designed against and 0/10 on the next one.

### Two modes

- **Lazy (default).** Build a cheap abstract-level index (no LLM calls); at cold start MLEvolve
  retrieves with a low threshold, deep-extracts only the retrieved papers, and caches them.
  About 70M up-front tokens becomes ~0.3M per task, amortising toward zero.
- **Vector.** Pay everything up front: extract every paper, synthesise insights, index one record
  per insight.

```bash
python scripts/6_build_abstract_index.py --venues all              # cheap, zero LLM calls
python scripts/build_retrieval_index.py  --kb methodology_kb/paperinsight
python scripts/probe_retrieval.py --task path/to/description.md --all
```

`probe_retrieval.py` runs retrieval alone — no extraction, no agent — so a retrieval change can be
checked in seconds rather than a 12-hour run. Use it for every retrieval change.

### `manifest.json` is the contract

It records the embedding model, dimension, count and schema version. The consumer must instantiate
the *same* model and build FAISS from `embeddings.npy`. Changing `--model` on one side only
silently degrades retrieval. Default is `BAAI/bge-m3` — note this is a **different** model from the
core pipeline's `all-MiniLM-L6-v2`, which is only used for clustering.

---

## Methodology KB

Per-paper technique extraction from full PDFs, plus `methodology_kb/paperinsight/`, cross-paper
synthesis written by an LLM tool-use agent (`list_files` / `read_file` / `write_file` /
`git_commit`; insights must cite ≥2 papers).

```bash
python scripts/5_build_methodology.py --venue naacl --year 2024 \
    --paper-workers 8 --category-workers 3 --build-index

# or the individual plugins
python scripts/plugin_a_methodology.py --venue acl --year 2024 --category <cat-slug>
python scripts/plugin_a2_insighter.py  --venue acl --year 2024 --category <cat-slug>
```

PDF coverage is decided by `plugin_a_methodology.resolve_pdf_url()`: the captured `pdf_url` first,
else a source-URL rule (`aclanthology.org` → `+.pdf`, `openreview.net` `forum?id` → `pdf?id`). So
ACL/NAACL/EMNLP and ICLR are complete, NeurIPS/ICML/CVPR/ICCV work where the fetcher captured a
link, and AAAI is partial. `--allow-abstract-fallback` extracts from the abstract when no PDF
resolves — **off by default, it lowers KB quality**.

`methodology_kb/paperinsight/` is versioned by its own **nested git repo** that the plugin
`git init` / `git commit`s into automatically. `5_build_methodology.py` deliberately withholds the
`git_commit` tool from concurrent agents and makes one commit at the end; concurrent commits
corrupt that repo.

---

## Analysis

Tier 4 answers "do the MLEvolve runs support anything?" It is deliberately conservative, because
several runs are compromised in ways that leave no trace in the final number.

```bash
# 1. grade on the cluster (mle-bench private answers exist only there) — see MLEvolve/utils/grade_all.py
#    ../nautilus/fetch-run.sh does this automatically and brings back scores.csv

# 2. validity filtering + figures
python scripts/analyze_runs.py --runs ~/nautilus/results \
    --manual-exclusions results/8.17/manual_exclusions.yaml \
    --scores ~/nautilus/results/scores.csv --charts

# 3. are retrieved techniques actually implemented?
python scripts/measure_adoption.py --runs ~/nautilus/results \
    --inventory results/8.23/run_inventory.csv --out results/8.23

# 4. which models did each run actually use, across all nodes?
python scripts/show_models.py --runs ~/nautilus/results --task jigsaw
```

Vocabulary, all of it load-bearing:

- **Arms** — `A` = no KB, `B` = KB at draft, `C` = KB at draft + improve. Recovered from each run's
  `logs/config.yaml`, never from the directory name.
- **Draw** — one launch batch, clustered by start time. **`agent.seed` is not a draw id**: it seeds
  the generated code, not the agent's search, and the LLM is sampled, so two runs at the same seed
  are two independent draws — demonstrated when a same-seed pair flipped the sign of B−A.
- **Verdicts** — `ok` / `invalid` (the run is broken) / `superseded` (fine, but runs pre-2026-08-08
  injection code, so it cannot be pooled).
- **Matched K** — arms are compared only at the same ensemble size. Arms stop fusing at different
  sizes because they can afford different numbers of candidates; comparing across K measures fusion
  budget, not knowledge.

Every threshold lives in the `Thresholds` dataclass at the top of `analyze_runs.py`, each with a
comment justifying its value.

### Figures

| file | content |
|---|---|
| `<task>_paired.png` | one line per draw across arms at matched K |
| `<task>_effect.png` | per-contrast score differences, mean and 95% CI |
| `<task>_process.png` | valid-solution rate, buggy rate, custom-architecture rate |
| `<task>_vs_k.png` | score against ensemble size |

The process figures need no grading and are emitted without `--scores`.

### Measurement traps, documented in the code

Three bugs in this tier produced confidently wrong answers and are now guarded against explicitly:

- Matching rate limits with `\b429\b` also matches the millisecond field of a log timestamp.
- `re.compile(r"^\[...")` without `re.MULTILINE` makes every duration come out `0.00`.
- Reading `logs/best_solution.py` to characterise what a run explored — it is 1 of ~20 nodes, and
  doing this produced a published claim that an arm had "abandoned transformers" when 18 of its 19
  nodes contained one. Use `show_models.py`, which reads every node.

`results/<date>/` holds derived tables and figures. Raw run directories are local-only and large.

---

## Agents

`agents/` contains 8 subagent definitions (one per conference) for Claude Code. Each is scoped to
`output/{venue}-*/`, scans the `SKILL.md` indexes, reads matching `references/*.md`, and returns
**extracted content — titles, TLDRs, methods — never file paths**. They replace the caller's search
work rather than pointing at files. `model: haiku`, `Write`/`Edit` disallowed.

---

## Setup

```bash
pip install -r requirements.txt
```

Read the header comment in `requirements.txt` first: on an image that already ships torch,
`sentence-transformers` installs a second torch and torchvision then mismatches.

All chat completions go through `scripts/llm.py`, a single provider-agnostic client. Every script
does `from llm import client, MODEL` — never construct a client or hardcode a model id.

```
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=anthropic/claude-sonnet-4.6
LLM_API_KEY=...            # OpenRouter key (sk-or-...)
OPENREVIEW_USERNAME=...    # only needed for ICLR fetching
OPENREVIEW_PASSWORD=...
```

Switching providers is a one-`.env` change, e.g. `LLM_BASE_URL=https://api.deepseek.com` and
`LLM_MODEL=deepseek-chat`. Embeddings run locally, so only chat completions hit the API.

Two gotchas:

- **`temperature=0`** is passed by `plugin_a/a2`, `probe_retrieval` and `measure_adoption`. Fine for
  Sonnet; reasoning models (GPT-5 / o-series) reject it and also require `max_completion_tokens`
  instead of `max_tokens`. Only `probe_retrieval.py` and `measure_adoption.py` branch on this today.
- **`HF_ENDPOINT`** — set it when huggingface.co is blocked; every embedding step downloads its
  model from there and will otherwise hang.

There is no test suite. Verify pipeline changes by running one stage on one venue; verify
*retrieval* changes with `probe_retrieval.py` (seconds) rather than a 12-hour agent run.

---

## Docs

`docs/` carries the written record, several files in EN + ZH pairs:

- `methodology.md` / `.zh.md` — what the system does, parameter-exact
- `semantic_retrieval_design.md` / `.zh.md` — the retrieval design and its numbered post-mortems
- `related_work.md`, `comparison_automind.md`, `previous_work.md`

[`UPDATELOG.md`](UPDATELOG.md) at the repo root is the change record, newest first; each entry
states the symptom and the fix. Read the relevant entry before "fixing" something that looks odd —
several things that look wrong are deliberate, and several that look fine were bugs.

---

## Credits

The original implementation was written by **Haoming Wang**. Retrieval, the analysis tier and the
MLEvolve integration are by **Yuze Li (William)**.

Licensed under the Apache License 2.0 — see [`LICENSE`](LICENSE).
