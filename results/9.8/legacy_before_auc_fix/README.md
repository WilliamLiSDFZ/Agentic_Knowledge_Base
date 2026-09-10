# Archived results before the 2026-09-09 AUC fix

These files preserve the original 9/8 analysis inputs and outputs:

- `scores.csv`: original downloaded scores across tasks.
- `analogy_summary.csv`: original derived analogy table.
- `charts.tar.gz`: complete original `charts/` directory.

Jigsaw Unintended Bias scores in this archive were calculated after incorrectly
thresholding predictions at 0.5. They are retained for audit only and must not be
pooled with corrected `jubias-continuous-auc-v1` scores. The updated score loader
intentionally rejects these jubias rows. Other tasks' graders were not modified.
