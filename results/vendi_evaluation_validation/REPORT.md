# Vendi evaluation validation — 2026-09-20

Follow-up: the user subsequently ran the live extraction and produced 59/62
representations. Review and local fixes are recorded in
[DIFF_REVIEW.md](../vendi_s61_s62_fixed/DIFF_REVIEW.md). The follow-up suite has
85 passing tests; [context_v2_validation.json](context_v2_validation.json) records
the new optimizer-context regression. The original pre-rerun record below is
retained for provenance.

Local implementation and offline checks are complete. Live model extraction and
new Vendi scores have not been validated or produced.

- 81 tests pass with `.venv/bin/python -m unittest discover -s tests -p 'test_*vendi*.py' -v`.
- All 16 S61/S62 improve candidates contain the full diff and all context selected
  by the bounded source helper within 160,000 characters. This does not establish
  that every semantic dependency is present.
- Actual-source regression fixtures cover A61 `732bfac846334d4cb83cf12810f26fe9`
  (sampler connected to DataLoader) and F61 `0a060fbe2cb3481b929422d70e302fc9`
  (ranking-loss microbatch gate and accumulation scaling). The manually authored
  assessments pass exact source-reference and static-use checks; this is not a
  measurement of LLM extraction accuracy.
- Synthetic CLI checks confirm that refusal text/vectors are excluded, complete
  no-change runs remain visible in coverage and the report, and unknown evidence
  produces incomplete coverage rather than a fabricated score.

Detailed actual-source references: [offline_validation.json](offline_validation.json).

Automatic approval review rejected the live test because sending source diff/context
to the configured LLM proxy did not have explicit destination authorization. No
successful API call occurred. The next step is to obtain that authorization, run the
two real model regressions, inspect their assessments, then recompute into a new
`results/vendi_s61_s62_diff` directory using the command in `docs/compare_vendi.md`.
Existing scores and caches are preserved.
