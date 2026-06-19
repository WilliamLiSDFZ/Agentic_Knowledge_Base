# Agentic Knowledge Base

Builds structured knowledge bases for AI agents in two stages:

- **Core pipeline** — scrapes papers from 8 major ML/AI conferences, clusters them by topic, and generates clustered topic "skills" under `output/`.
- **Plugin layer** — a deeper tier that turns paper PDFs and ML training-run logs into `methodology_kb/` (per-paper techniques + cross-paper insights) and `experience_kb/` (wins / failures / hypotheses).

## What it does

The core pipeline:

1. Fetches paper titles and abstracts from conference proceedings
2. Embeds abstracts and clusters them into ~80 topic categories
3. Classifies each paper into 1-3 categories with tags and a one-line summary
4. Writes a `SKILL.md` index + individual reference files per category

Output lives in `output/{venue}-{year}/`.

## Supported conferences

| Conference | Source |
|------------|--------|
| NeurIPS | papers.nips.cc |
| ICML | proceedings.mlr.press |
| CVPR / ICCV | openaccess.thecvf.com |
| ACL / NAACL | aclanthology.org |
| ICLR | OpenReview API |
| AAAI | Semantic Scholar API |

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env` and fill in your keys. LLM calls go through `scripts/llm.py`, which is provider-agnostic and defaults to **OpenRouter + Claude Sonnet**:

```
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=anthropic/claude-sonnet-4.6
LLM_API_KEY=...            # your OpenRouter key (sk-or-...)
OPENREVIEW_USERNAME=...    # only needed for ICLR fetching
OPENREVIEW_PASSWORD=...
```

To use a different provider, change those three lines — e.g. DeepSeek-direct:

```
LLM_BASE_URL=https://api.deepseek.com
LLM_MODEL=deepseek-chat
LLM_API_KEY=...            # your DeepSeek key
```

Embeddings run locally (`sentence-transformers`), so only chat completions hit the API.

## Usage

```bash
# Single conference
bash run_all.sh neurips 2024

# All conferences
for venue in neurips icml cvpr acl naacl iclr aaai; do
  bash run_all.sh $venue 2024
done
```

Or run steps individually:

```bash
python scripts/1_fetch.py --venue icml --year 2024
python scripts/2_embed_cluster.py --venue icml --year 2024
python scripts/3_classify.py --venue icml --year 2024
python scripts/4_generate_skills.py --venue icml --year 2024
```

Steps 2-4 resume automatically if interrupted.

To adjust the number of topic clusters, edit `N_CLUSTERS` in `scripts/2_embed_cluster.py` (default: 80). Higher = finer granularity.

## Output structure

```
output/
└── neurips-2024/
    ├── diffusion-models-image-generation/
    │   ├── SKILL.md
    │   └── references/
    │       ├── abc123.md
    │       └── ...
    └── ...
```

Each `SKILL.md` contains a description and an index table (title, tags, file).
Each `references/*.md` contains the abstract, tags, TLDR, and source URL.

## Plugin layer

A deeper tier that builds two further knowledge bases on top of the core pipeline's `output/`. Each plugin runs independently.

### `methodology_kb/` — what techniques papers used and how well they worked

```bash
# Download PDFs for a category and extract per-paper techniques + their positive/negative effects
# (currently ACL / Anthology sources only)
python scripts/plugin_a_methodology.py --venue acl --year 2024 --category <cat-slug>

# Read those methodology files and synthesize cross-paper insights -> methodology_kb/paperinsight/
# (an LLM tool-use agent: it lists, reads, writes, and commits on its own)
python scripts/plugin_a2_insighter.py --venue acl --year 2024 --category <cat-slug>
```

`<cat-slug>` is a category folder name produced by the core pipeline (e.g. a directory under `output/acl-2024/`).

### `experience_kb/` — lessons learned from ML training runs

```bash
# Ingest a training-run log dir (steps/judge_*/output.json, designer*/output.json)
# and distill wins.md / failures.md / hypotheses.md
python scripts/plugin_b_experience.py --run_dir <path/to/run>

# "Dreamer": sleep-time consolidation — merge duplicate entries, extract meta-insights,
# and age out low-value entries via archive/ then deletion
python scripts/plugin_c_dreamer.py --output_dir experience_kb
```

`experience_kb/` and `methodology_kb/paperinsight/` are each versioned by their own **nested git repos** that the plugins `git init` / `git commit` into automatically.

See `CLAUDE.md` for the full architecture and known gotchas.

## Agents

`agents/` contains 8 subagent definitions (one per conference) for use with Claude Code. Each agent scans the relevant `output/{venue}-*/` directory and returns extracted paper content for a given research query.

## Credits

The original implementation of this project was written by **Haoming Wang**. It is now maintained and developed further by **Yuze Li (William)**.

Licensed under the Apache License 2.0 — see [`LICENSE`](LICENSE).
