---
title: "Random Exploration in Bayesian Optimization: Order-Optimal Regret and Computational Efficiency"
source: "https://proceedings.mlr.press/v235/salgia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/salgia24a/salgia24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'online-learning-and-sequential-decision-making']
tags: ['Bayesian-optimization', 'Gaussian-processes', 'random-exploration', 'regret-bounds', 'kernel-bandits']
venue: "ICML 2024"
tldr: "Random exploration in Bayesian optimization with Gaussian processes is shown to achieve order-optimal regret with improved computational efficiency."
---

# Random Exploration in Bayesian Optimization: Order-Optimal Regret and Computational Efficiency

**Source**: [https://proceedings.mlr.press/v235/salgia24a.html](https://proceedings.mlr.press/v235/salgia24a.html)

**TLDR**: Random exploration in Bayesian optimization with Gaussian processes is shown to achieve order-optimal regret with improved computational efficiency.

## Abstract

We consider Bayesian optimization using Gaussian Process models, also referred to as kernel-based bandit optimization. We study the methodology of exploring the domain using random samples drawn from a distribution. We show that this random exploration approach achieves the optimal error rates. Our analysis is based on novel concentration bounds in an infinite dimensional Hilbert space established in this work, which may be of independent interest. We further develop an algorithm based on random exploration with domain shrinking and establish its order-optimal regret guarantees under both noise-free and noisy settings. In the noise-free setting, our analysis closes the existing gap in regret performance under a mild assumption on the underlying function and thereby partially resolves a COLT open problem. The proposed algorithm also enjoys a computational advantage over prevailing methods due to the random exploration that obviates the expensive optimization of a non-convex acquisition function for choosing the query points at each iteration.