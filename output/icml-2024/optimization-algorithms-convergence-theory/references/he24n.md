---
title: "Robust Multi-Task Learning with Excess Risks"
source: "https://proceedings.mlr.press/v235/he24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24n/he24n.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'optimization-algorithms-convergence-theory']
tags: ['multi-task-learning', 'robustness', 'excess-risk', 'adaptive-weights']
venue: "ICML 2024"
tldr: "Develops a robust multi-task learning framework with theoretical excess risk guarantees using adaptive task weight updates."
---

# Robust Multi-Task Learning with Excess Risks

**Source**: [https://proceedings.mlr.press/v235/he24n.html](https://proceedings.mlr.press/v235/he24n.html)

**TLDR**: Develops a robust multi-task learning framework with theoretical excess risk guarantees using adaptive task weight updates.

## Abstract

Multi-task learning (MTL) considers learning a joint model for multiple tasks by optimizing a convex combination of all task losses. To solve the optimization problem, existing methods use an adaptive weight updating scheme, where task weights are dynamically adjusted based on their respective losses to prioritize difficult tasks. However, these algorithms face a great challenge whenever label noise is present, in which case excessive weights tend to be assigned to noisy tasks that have relatively large Bayes optimal errors, thereby overshadowing other tasks and causing performance to drop across the board. To overcome this limitation, we propose Multi-Task Learning with Excess Risks (ExcessMTL), an excess risk-based task balancing method that updates the task weights by their distances to convergence instead. Intuitively, ExcessMTL assigns higher weights to worse-trained tasks that are further from convergence. To estimate the excess risks, we develop an efficient and accurate method with Taylor approximation. Theoretically, we show that our proposed algorithm achieves convergence guarantees and Pareto stationarity. Empirically, we evaluate our algorithm on various MTL benchmarks and demonstrate its superior performance over existing methods in the presence of label noise. Our code is available at https://github.com/yifei-he/ExcessMTL.