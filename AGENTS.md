# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Overview

Two-stage system for turning conference papers into agent-consumable knowledge bases:

1. **Core pipeline** (`scripts/1-4_*.py`): scrape conference abstracts → embed/cluster into ~80 topics → LLM-classify → emit topic "skills" under `output/{venue}-{year}/`. This is what the README documents.
2. **Plugin layer** (`scripts/plugin_*.py`): a deeper extraction/synthesis tier that builds two further knowledge bases (`methodology_kb/`, `experience_kb/`) from paper PDFs and from ML training-run logs. **Not in the README** — read the per-plugin notes below.

All chat-completions calls go through **`scripts/llm.py`**, a single provider-agnostic client built on the **`openai` SDK**. It reads `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY` from `.env` and **defaults to OpenRouter + Codex Sonnet** (`anthropic/Codex-sonnet-4.6`). Every script does `from llm import client, MODEL` and calls `client.chat.completions.create(model=MODEL, ...)` — never construct a client or hardcode a model id. Switching providers (e.g. DeepSeek-direct) is a one-`.env`-change: `LLM_BASE_URL=https://api.deepseek.com`, `LLM_MODEL=deepseek-chat`. Embeddings are local (`sentence-transformers`), so only chat completions hit the API.

## Environment & gotchas

These will bite a fresh checkout — check them before debugging "missing key" / "module not found" errors:

- **Install deps**: `pip install -r requirements.txt` (now includes `openai`).
- **`.env` keys**: `LLM_API_KEY` (+ optional `LLM_BASE_URL`/`LLM_MODEL`) for all LLM steps; `OPENREVIEW_USERNAME`/`OPENREVIEW_PASSWORD` (only for `iclr` fetching). `scripts/llm.py` loads `.env` for every script, so no shell-export step is needed. (`DEEPSEEK_*`/`ANTHROPIC_*` keys are legacy/unused unless you point `LLM_*` at them.)
- **`temperature=0`** is passed in `plugin_a/b/c` and `a2`. Fine for Sonnet 4.6; would 400 if `LLM_MODEL` is pointed at Opus 4.7/4.8 or Fable 5 (sampling params removed there).
- **Interpreter**: `run_all.sh` uses `PYTHON="${PYTHON:-python}"` (whatever `python` is on PATH); override with `PYTHON=/path/to/python bash run_all.sh …`. The plugin scripts anchor their `output/` `methodology_kb/` `experience_kb/` `cache/` paths to the repo root (`REPO_ROOT = Path(__file__).resolve().parent.parent`), so they can be run from any directory.
- There is **no test suite**; verify changes by running the relevant pipeline stage on one venue.

## Commands

```bash
# Core pipeline, one venue (resumes if interrupted on steps 2-4)
bash run_all.sh <venue> <year>            # e.g. neurips 2024

# Core pipeline, run a single stage
python scripts/1_fetch.py          --venue icml --year 2024
python scripts/2_embed_cluster.py  --venue icml --year 2024
python scripts/3_classify.py       --venue icml --year 2024
python scripts/4_generate_skills.py --venue icml --year 2024
```

Valid `--venue`: `neurips icml cvpr iccv acl naacl iclr aaai` (or `all` for fetch). `cvpr`/`iccv` share `CVFFetcher`; `acl`/`naacl` share `ACLFetcher`.

```bash
# Plugin layer (run per category folder; depends on core output existing)
python scripts/plugin_a_methodology.py --venue acl --year 2024 --category <cat-slug>   # PDFs -> techniques
python scripts/plugin_a2_insighter.py  --venue acl --year 2024 --category <cat-slug>   # methodology files -> cross-paper insights
python scripts/plugin_b_experience.py  --run_dir <path/to/run>                          # training-run logs -> wins/failures/hypotheses
python scripts/plugin_c_dreamer.py     --output_dir experience_kb                       # consolidate + forget over experience_kb
```

## Data flow

The pipeline stages communicate **only through JSON files in `cache/`**, keyed by `{venue}_{year}_*`. Each stage skips work that already exists, which is how resume works:

```
1_fetch          -> cache/{venue}_{year}_papers.json      (title, abstract, url, id, venue, year — see fetch/base.py)
2_embed_cluster  -> cache/{venue}_{year}_clusters.json    (AgglomerativeClustering, N_CLUSTERS=80 in the script; LLM names each cluster)
3_classify       -> cache/{venue}_{year}_classified.json  (LLM assigns 1-3 categories + tags + tldr, batched, append-on-resume)
4_generate_skills-> output/{venue}-{year}/{category}/{SKILL.md, references/*.md}
```

`output/` is committed as the product (the `agents/` read it); `cache/` is gitignored scratch.

## Architecture

### Conference fetchers (`scripts/fetch/`)
One module per source, all subclassing `ConferenceFetcher` (`base.py`) and returning the same paper dict shape. `1_fetch.py` is the dispatcher (`FETCHERS` map). Sources differ per venue: NeurIPS/ICML/CVF scrape HTML, ACL/NAACL parse Anthology, ICLR uses the OpenReview API (needs creds), AAAI uses Semantic Scholar.

### The three knowledge bases
- **`output/`** — topic-clustered paper index (abstracts only). Built by the core pipeline. Consumed by the search agents.
- **`methodology_kb/`** — per-paper technique extraction from full PDFs (`plugin_a`, currently ACL-only since it derives PDF URLs from `aclanthology.org`), plus **`methodology_kb/paperinsight/`** cross-paper synthesis written by `plugin_a2` (an LLM **tool-use agent** with `list_files`/`read_file`/`write_file`/`git_commit` tools; insights must cite ≥2 papers).
- **`experience_kb/`** — `wins.md`/`failures.md`/`hypotheses.md` distilled from agent training-run logs. `plugin_b` ingests a run, `plugin_c` ("dreamer") periodically consolidates duplicates, extracts meta-insights, and ages entries out via `Seen`/`Dreamer runs`/`Archived runs` counters → `archive/` → deletion.

### Nested git repos (important)
`plugin_b`, `plugin_c`, and `plugin_a2` run `git init`/`git commit` **inside their output dirs** to version the KB independently. `plugin_b` even branches per run and uses the LLM to resolve merge conflicts between parallel runs. This is why the top-level `.gitignore` excludes `methodology_kb/paperinsight/.git/` and `experience_kb/archive/`. When working in those trees, expect a separate git history.

### Search agents (`agents/*.md`)
8 Codex subagent definitions (one per conference, `model: haiku`, `Write`/`Edit` disallowed). Each is scoped to `output/{venue}-*/`, scans `SKILL.md` indexes, reads matching `references/*.md`, and returns **extracted content (titles/TLDRs/methods), never file paths** — they replace the caller's search work rather than pointing at files.
