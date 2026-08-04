---
title: "On the Convergence of Projected Bures-Wasserstein Gradient Descent under Euclidean Strong Convexity"
source: "https://proceedings.mlr.press/v235/fan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fan24b/fan24b.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning']
tags: ['bures-wasserstein', 'gradient-descent', 'convergence-theory']
venue: "ICML 2024"
tldr: "Establishes convergence guarantees for projected Bures-Wasserstein gradient descent under Euclidean strong convexity assumptions."
---

# On the Convergence of Projected Bures-Wasserstein Gradient Descent under Euclidean Strong Convexity

**Source**: [https://proceedings.mlr.press/v235/fan24b.html](https://proceedings.mlr.press/v235/fan24b.html)

**TLDR**: Establishes convergence guarantees for projected Bures-Wasserstein gradient descent under Euclidean strong convexity assumptions.

## Abstract

The Bures-Wasserstein (BW) gradient descent method has gained considerable attention in various domains, including Gaussian barycenter, matrix recovery and variational inference problems, due to its alignment with the Wasserstein geometry of normal distributions. Despite its popularity, existing convergence analysis are often contingent upon specific loss functions, and the exploration of constrained settings within this framework remains limited. In this work, we make an attempt to bridge this gap by providing a general convergence rate guarantee for BW gradient descent when the Euclidean strong convexity of the loss and the constraints is assumed. In an effort to advance practical implementations, we also derive a closed-form solution for the projection onto BW distance-constrained sets, which enables the fast implementation of projected BW gradient descent for problems that arise in the constrained barycenter and distributionally robust optimization literature. Experimental results demonstrate significant improvements in computational efficiency and convergence speed, underscoring the efficacy of our method in practical scenarios.