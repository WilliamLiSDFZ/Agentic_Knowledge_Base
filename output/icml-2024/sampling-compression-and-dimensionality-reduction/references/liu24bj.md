---
title: "Symmetric Matrix Completion with ReLU Sampling"
source: "https://proceedings.mlr.press/v235/liu24bj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bj/liu24bj.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['matrix-completion', 'ReLU-sampling', 'positive-semidefinite', 'low-rank', 'deterministic-sampling']
venue: "ICML 2024"
tldr: "This paper studies symmetric positive semi-definite low-rank matrix completion under ReLU and threshold-based deterministic entry-dependent sampling schemes."
---

# Symmetric Matrix Completion with ReLU Sampling

**Source**: [https://proceedings.mlr.press/v235/liu24bj.html](https://proceedings.mlr.press/v235/liu24bj.html)

**TLDR**: This paper studies symmetric positive semi-definite low-rank matrix completion under ReLU and threshold-based deterministic entry-dependent sampling schemes.

## Abstract

We study the problem of symmetric positive semi-definite low-rank matrix completion (MC) with deterministic entry-dependent sampling. In particular, we consider rectified linear unit (ReLU) sampling, where only positive entries are observed, as well as a generalization to threshold-based sampling. We first empirically demonstrate that the landscape of this MC problem is not globally benign: Gradient descent (GD) with random initialization will generally converge to stationary points that are not globally optimal. Nevertheless, we prove that when the matrix factor with a small rank satisfies mild assumptions, the nonconvex objective function is geodesically strongly convex on the quotient manifold in a neighborhood of a planted low-rank matrix. Moreover, we show that our assumptions are satisfied by a matrix factor with i.i.d. Gaussian entries. Finally, we develop a tailor-designed initialization for GD to solve our studied formulation, which empirically always achieves convergence to the global minima. We also conduct extensive experiments and compare MC methods, investigating convergence and completion performance with respect to initialization, noise level, dimension, and rank.