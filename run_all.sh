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

# Step 5 is heavy (per-paper PDF download + LLM, per-category synthesis agent) and needs
# HF_ENDPOINT for the retrieval index. Skip it with:  SKIP_METHODOLOGY=1 bash run_all.sh ...
if [ -z "${SKIP_METHODOLOGY:-}" ]; then
    echo "=== Step 5: Build methodology (plugin A + A2) + retrieval index ==="
    $PYTHON scripts/5_build_methodology.py --venue $VENUE --year $YEAR \
        --paper-workers "${PAPER_WORKERS:-8}" \
        --category-workers "${CATEGORY_WORKERS:-3}" \
        --build-index
else
    echo "=== Step 5 skipped (SKIP_METHODOLOGY set) ==="
fi

echo "=== Done: output/${VENUE}-${YEAR}/ + methodology_kb/ ==="
