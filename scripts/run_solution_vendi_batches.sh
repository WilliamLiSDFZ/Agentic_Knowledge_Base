#!/usr/bin/env bash
# Run the four downloaded A/F cohorts; all outputs share one flat directory.
# Usage: bash scripts/run_solution_vendi_batches.sh [--dry-run]
# On the CPU pod: VENDI_RUNS=/workspace/MLEvolve/runs bash scripts/run_solution_vendi_batches.sh
set -euo pipefail
cd "$(dirname "$0")/.."

VENDI_RUNS="${VENDI_RUNS:-$HOME/nautilus/results}"
VENDI_OUT="${VENDI_OUT:-results/vendi_solutions}"
VENDI_PYTHON="${VENDI_PYTHON:-python}"
batch_status=0

run_batch() {
    local label="$1" pattern="$2"
    shift 2
    if "$VENDI_PYTHON" scripts/compare_solution_vendi.py \
        --runs "$VENDI_RUNS" --inventory results/9.14/run_inventory.csv \
        --run-glob "$pattern" --arms A F --summary-model gpt-5.6-terra \
        --out "$VENDI_OUT" --prefix "$label" "$@"; then
        return 0
    else
        local status=$?
        # Incomplete coverage is saved; continue so the other batches still run.
        if [ "$status" -ne 2 ]; then return "$status"; fi
        batch_status=2
    fi
}

run_batch s52_s53 '20260910_*s5[23]' "$@"
run_batch s54_s56 '20260911_07*s5[456]' "$@"
run_batch s58_s59 '20260912_08*jubias-*-gpt56sol-s5[89]' "$@"
run_batch s61_s62 '20260914_*s6[12]' "$@"
exit "$batch_status"
