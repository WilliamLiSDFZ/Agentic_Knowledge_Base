---
title: "DsDm: Model-Aware Dataset Selection with Datamodels"
source: "https://proceedings.mlr.press/v235/engstrom24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/engstrom24a/engstrom24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['dataset-selection', 'datamodels', 'training-data', 'data-quality', 'large-scale-training']
venue: "ICML 2024"
tldr: "Shows that model-aware dataset selection using datamodels outperforms quality-heuristic filtering for training large-scale models."
---

# DsDm: Model-Aware Dataset Selection with Datamodels

**Source**: [https://proceedings.mlr.press/v235/engstrom24a.html](https://proceedings.mlr.press/v235/engstrom24a.html)

**TLDR**: Shows that model-aware dataset selection using datamodels outperforms quality-heuristic filtering for training large-scale models.

## Abstract

When selecting data for training large-scale models, standard practice is to filter for examples that match human notions of data quality. Such filtering yields qualitatively clean datapoints that intuitively should improve model behavior. However, in practice the opposite can often happen: we find that selecting according to similarity with "high quality" data sources may not increase (and can even hurt) performance compared to randomly selecting data. To develop better methods for selecting data, we start by framing dataset selection as an optimization problem that we can directly solve for: given target tasks, a learning algorithm, and candidate data, select the subset that maximizes model performance. This framework thus avoids handpicked notions of data quality, and instead models explicitly how the learning process uses train datapoints to predict on the target tasks. Our resulting method greatly improves language model (LM) performance on both pre-specified tasks and previously unseen tasks. Specifically, choosing target tasks representative of standard LM problems and evaluating on diverse held-out benchmarks, our selected datasets provide a 2x compute multiplier over baseline methods.