---
title: "Infinite-Horizon Distributionally Robust Regret-Optimal Control"
source: "https://proceedings.mlr.press/v235/kargin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kargin24a/kargin24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['distributionally-robust-control', 'Wasserstein-ambiguity', 'regret-minimization']
venue: "ICML 2024"
tldr: "Studies infinite-horizon distributionally robust control minimizing worst-case regret over time-correlated disturbances within a Wasserstein-2 ambiguity set."
---

# Infinite-Horizon Distributionally Robust Regret-Optimal Control

**Source**: [https://proceedings.mlr.press/v235/kargin24a.html](https://proceedings.mlr.press/v235/kargin24a.html)

**TLDR**: Studies infinite-horizon distributionally robust control minimizing worst-case regret over time-correlated disturbances within a Wasserstein-2 ambiguity set.

## Abstract

We study the infinite-horizon distributionally robust (DR) control of linear systems with quadratic costs, where disturbances have unknown, possibly time-correlated distribution within a Wasserstein-2 ambiguity set. We aim to minimize the worst-case expected regret—the excess cost of a causal policy compared to a non-causal one with access to future disturbance. Though the optimal policy lacks a finite-order state-space realization (i.e., it is non-rational), it can be characterized by a finite-dimensional parameter. Leveraging this, we develop an efficient frequency-domain algorithm to compute this optimal control policy and present a convex optimization method to construct a near-optimal state-space controller that approximates the optimal non-rational controller in the $\mathit{H}_\infty$-norm. This approach avoids solving a computationally expensive semi-definite program (SDP) that scales with the time horizon in the finite-horizon setting.