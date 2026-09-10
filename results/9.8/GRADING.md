# Corrected scoring, 2026-09-09

The current charts use `scores-continuous-auc-v1.csv`. Jigsaw Unintended Bias keeps
continuous predictions when computing ROC-AUC; all other competition graders are
unchanged. The same 520 submission keys from 78 runs were processed: 37 corrected
jubias scores, 475 exactly unchanged scores for other tasks, and eight already
unscored Jigsaw submissions. Missing scores now have an explicit failure note.

The original scores, analogy summary and all charts are in
`legacy_before_auc_fix/`. Do not mix those jubias scores with the corrected metric.
`grading_audit.json` records the comparison; `deployment.json` records exact code
hashes and the cluster deployment. `regrade.log` retains the original batch output
and its correction: the first summary mistakenly counted `None` as success.
`none-score-regression.log` verifies the corrected accounting on that old run.

The updated main score figures were built from the existing `run_inventory.csv`
using `plot_analogy.load_inventory`, `analyze_runs.build_groups`,
`analyze_runs.load_scores`, and `analyze_runs.build_charts`. The inventory,
exclusions, grouping rules and process figures were preserved. Analogy plots use:

```bash
python scripts/plot_analogy.py --runs /path/to/downloaded/runs \
  --out results/9.8 --scores results/9.8/scores-continuous-auc-v1.csv
```

The fix itself is in the sibling MLEvolve repository's `patches/mlebench/`, with
application/checking in `utils/mlebench_patch.py`. No models were retrained and no
private labels were copied off the cluster.
