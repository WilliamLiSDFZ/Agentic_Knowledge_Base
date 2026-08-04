---
title: "Stochastic Weakly Convex Optimization beyond Lipschitz Continuity"
source: "https://proceedings.mlr.press/v235/gao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24d/gao24d.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['weakly-convex-optimization', 'non-Lipschitz', 'stochastic-subgradient', 'adaptive-regularization']
venue: "ICML 2024"
tldr: "This paper extends stochastic weakly convex optimization to settings without Lipschitz continuity via adaptive regularization strategies."
---

# Stochastic Weakly Convex Optimization beyond Lipschitz Continuity

**Source**: [https://proceedings.mlr.press/v235/gao24d.html](https://proceedings.mlr.press/v235/gao24d.html)

**TLDR**: This paper extends stochastic weakly convex optimization to settings without Lipschitz continuity via adaptive regularization strategies.

## Abstract

This paper considers stochastic weakly convex optimization without the standard Lipschitz continuity assumption. Based on new adaptive regularization (stepsize) strategies, we show that a wide class of stochastic algorithms, including the stochastic subgradient method, preserve the $\mathcal{O} ( 1 / \sqrt{K})$ convergence rate with constant failure rate. Our analyses rest on rather weak assumptions: the Lipschitz parameter can be either bounded by a general growth function of $\\|x\\|$ or locally estimated through independent random samples. Numerical experiments demonstrate the efficiency and robustness of our proposed stepsize policies.