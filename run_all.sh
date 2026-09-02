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

# Step 5 (heavy: per-paper PDF+LLM, per-category synthesis agent) is OPT-IN. It builds the
# methodology_kb product; MLEvolve no longer consumes it at run time.
# Run it with:  FULL_METHODOLOGY=1 bash run_all.sh ...
if [ -n "${FULL_METHODOLOGY:-}" ]; then
    echo "=== Step 5: Full batch methodology (plugin A + A2) ==="
    $PYTHON scripts/5_build_methodology.py --venue $VENUE --year $YEAR \
        --paper-workers "${PAPER_WORKERS:-8}" \
        --category-workers "${CATEGORY_WORKERS:-3}"
fi

# Step 6: the paper corpus MLEvolve's analogy agent searches with BM25 (title+tldr+abstract;
# zero LLM calls, zero GPU, seconds). Skip with SKIP_INDEX=1.
if [ -z "${SKIP_INDEX:-}" ]; then
    echo "=== Step 6: Build paper corpus (cheap, no LLM) ==="
    $PYTHON scripts/6_build_paper_corpus.py --venues all
fi

echo "=== Done: output/${VENUE}-${YEAR}/ (+ output/paper_corpus; methodology_kb via FULL_METHODOLOGY=1) ==="
