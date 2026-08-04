---
title: "An Iterative Min-Min Optimization Method for Sparse Bayesian Learning"
source: "https://proceedings.mlr.press/v235/wang24al.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24al/wang24al.pdf"
categories: ['optimization-algorithms-convergence-theory', 'sparse-phase-retrieval-with-priors']
tags: ['sparse-Bayesian-learning', 'convergence', 'iterative-optimization', 'sparsity']
venue: "ICML 2024"
tldr: "An iterative min-min optimization method with global convergence guarantees is developed for sparse Bayesian learning."
---

# An Iterative Min-Min Optimization Method for Sparse Bayesian Learning

**Source**: [https://proceedings.mlr.press/v235/wang24al.html](https://proceedings.mlr.press/v235/wang24al.html)

**TLDR**: An iterative min-min optimization method with global convergence guarantees is developed for sparse Bayesian learning.

## Abstract

As a well-known machine learning algorithm, sparse Bayesian learning (SBL) can find sparse representations in linearly probabilistic models by imposing a sparsity-promoting prior on model coefficients. However, classical SBL algorithms lack the essential theoretical guarantees of global convergence. To address this issue, we propose an iterative Min-Min optimization method to solve the marginal likelihood function (MLF) of SBL based on the concave-convex procedure. The method can optimize the hyperparameters related to both the prior and noise level analytically at each iteration by re-expressing MLF using auxiliary functions. Particularly, we demonstrate that the method globally converges to a local minimum or saddle point of MLF. With rigorous theoretical guarantees, the proposed novel SBL algorithm outperforms classical ones in finding sparse representations on simulation and real-world examples, ranging from sparse signal recovery to system identification and kernel regression.