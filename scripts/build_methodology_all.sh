#!/usr/bin/env bash
# Build methodology_kb for ALL categories of a venue/year, then the retrieval index.
#
# Usage:
#   bash scripts/build_methodology_all.sh <venue> <year>
#   e.g. bash scripts/build_methodology_all.sh naacl 2024
#   PYTHON=/path/to/python bash scripts/build_methodology_all.sh acl 2024
#
# Prereq: run `bash run_all.sh <venue> <year>` first (produces output/<venue>-<year>/).
# Note:  plugin_a currently only handles aclanthology.org PDFs, so use acl/naacl for now.
set -euo pipefail
cd "$(dirname "$0")/.."

VENUE="${1:-naacl}"
YEAR="${2:-2024}"
PY="${PYTHON:-python}"
OUT_DIR="output/${VENUE}-${YEAR}"

[ -d "$OUT_DIR" ] || { echo "No $OUT_DIR — run: bash run_all.sh $VENUE $YEAR first"; exit 1; }

n=0
for dir in "$OUT_DIR"/*/; do
    [ -d "$dir" ] || continue
    cat="$(basename "$dir")"
    n=$((n + 1))
    echo "===== [$VENUE-$YEAR] ($n) $cat ====="

    # plugin_a is resumable: it skips *_methodology.md files that already exist.
    "$PY" scripts/plugin_a_methodology.py --venue "$VENUE" --year "$YEAR" --category "$cat"

    # plugin_a2 is an expensive agent loop — skip a category whose insight.md already exists.
    insight="methodology_kb/paperinsight/${VENUE}-${YEAR}/${cat}/insight.md"
    if [ -f "$insight" ]; then
        echo "  insight.md exists — skipping a2"
    else
        "$PY" scripts/plugin_a2_insighter.py --venue "$VENUE" --year "$YEAR" --category "$cat"
    fi
done

echo "Done ($n categories)."
