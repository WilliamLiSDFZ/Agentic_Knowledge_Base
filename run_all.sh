#!/bin/bash
set -e

cd "$(dirname "$0")"

PYTHON="${PYTHON:-python}"
VENUE=${1:-neurips}
YEAR=${2:-2024}

echo "=== Step 1: Fetch ${VENUE} ${YEAR} papers ==="
$PYTHON scripts/1_fetch.py --venue $VENUE --year $YEAR

echo "=== Step 2: Embed + cluster ==="
$PYTHON scripts/2_embed_cluster.py --venue $VENUE --year $YEAR

echo "=== Step 3: Classify papers with LLM ==="
$PYTHON scripts/3_classify.py --venue $VENUE --year $YEAR

echo "=== Step 4: Generate skills ==="
$PYTHON scripts/4_generate_skills.py --venue $VENUE --year $YEAR

# Step 5 (heavy: per-paper PDF+LLM, per-category synthesis agent) is now OPT-IN — the
# default is the lazy path: build a cheap abstract index; MLEvolve extracts on demand.
# Run the full batch methodology with:  FULL_METHODOLOGY=1 bash run_all.sh ...
if [ -n "${FULL_METHODOLOGY:-}" ]; then
    echo "=== Step 5: Full batch methodology (plugin A + A2) + insight index ==="
    $PYTHON scripts/5_build_methodology.py --venue $VENUE --year $YEAR \
        --paper-workers "${PAPER_WORKERS:-8}" \
        --category-workers "${CATEGORY_WORKERS:-3}" \
        --build-index
fi

# Step 6: abstract index (no LLM calls; needs sentence-transformers + HF model — set
# HF_ENDPOINT if huggingface.co is blocked). Skip with SKIP_INDEX=1. Non-fatal on failure.
if [ -z "${SKIP_INDEX:-}" ]; then
    echo "=== Step 6: Build abstract retrieval index (cheap, no LLM) ==="
    if ! $PYTHON scripts/6_build_abstract_index.py --venues all; then
        echo "WARN: abstract index build failed (missing sentence-transformers or HF unreachable?) — continuing"
    fi
fi

echo "=== Done: output/${VENUE}-${YEAR}/ (+ abstract_index; methodology_kb fills lazily or via FULL_METHODOLOGY=1) ==="
