---
title: "Learning-Rate-Free Stochastic Optimization over Riemannian Manifolds"
source: "https://proceedings.mlr.press/v235/dodd24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dodd24a/dodd24a.pdf"
categories: ['sampling-and-optimization-on-manifolds', 'optimization-algorithms-convergence-theory']
tags: ['Riemannian-optimization', 'learning-rate-free', 'stochastic-optimization', 'manifold', 'hyperparameter-free']
venue: "ICML 2024"
tldr: "Proposes a learning-rate-free stochastic optimization algorithm for Riemannian manifolds, eliminating the need for costly hyperparameter tuning."
---

# Learning-Rate-Free Stochastic Optimization over Riemannian Manifolds

**Source**: [https://proceedings.mlr.press/v235/dodd24a.html](https://proceedings.mlr.press/v235/dodd24a.html)

**TLDR**: Proposes a learning-rate-free stochastic optimization algorithm for Riemannian manifolds, eliminating the need for costly hyperparameter tuning.

## Abstract

In recent years, interest in gradient-based optimization over Riemannian manifolds has surged. However, a significant challenge lies in the reliance on hyperparameters, especially the learning rate, which requires meticulous tuning by practitioners to ensure convergence at a suitable rate. In this work, we introduce innovative learning-rate-free algorithms for stochastic optimization over Riemannian manifolds, eliminating the need for hand-tuning and providing a more robust and user-friendly approach. We establish high probability convergence guarantees that are optimal, up to logarithmic factors, compared to the best-known optimally tuned rate in the deterministic setting. Our approach is validated through numerical experiments, demonstrating competitive performance against learning-rate-dependent algorithms.