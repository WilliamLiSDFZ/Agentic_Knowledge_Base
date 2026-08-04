---
title: "High-Dimensional Geometric Streaming for Nearly Low Rank Data"
source: "https://proceedings.mlr.press/v235/esfandiari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/esfandiari24a/esfandiari24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['streaming-algorithms', 'subspace-approximation', 'lp-regression', 'dimensionality-reduction', 'sketching']
venue: "ICML 2024"
tldr: "Presents streaming algorithms for ℓp subspace approximation exploiting nearly low-rank structure in high-dimensional geometric data."
---

# High-Dimensional Geometric Streaming for Nearly Low Rank Data

**Source**: [https://proceedings.mlr.press/v235/esfandiari24a.html](https://proceedings.mlr.press/v235/esfandiari24a.html)

**TLDR**: Presents streaming algorithms for ℓp subspace approximation exploiting nearly low-rank structure in high-dimensional geometric data.

## Abstract

We study streaming algorithms for the $\ell_p$ subspace approximation problem. Given points $a_1, \ldots, a_n$ as an insertion-only stream and a rank parameter $k$, the $\ell_p$ subspace approximation problem is to find a $k$-dimensional subspace $V$ such that $(\sum_{i=1}^n d(a_i, V)^p)^{1/p}$ is minimized, where $d(a, V)$ denotes the Euclidean distance between $a$ and $V$ defined as $\min_{v \in V} ||a - v||$. When $p = \infty$, we need to find a subspace $V$ that minimizes $\max_i d(a_i, V)$. For $\ell_{\infty}$ subspace approximation, we give a deterministic strong coreset construction algorithm and show that it can be used to compute a $\mathrm{poly}(k, \log n)$ approximate solution. We show that the distortion obtained by our coreset is nearly tight for any sublinear space algorithm. For $\ell_p$ subspace approximation, we show that suitably scaling the points and then using our $\ell_{\infty}$ coreset construction, we can compute a $\mathrm{poly}(k, \log n)$ approximation. Our algorithms are easy to implement and run very fast on large datasets. We also use our strong coreset construction to improve the results in a recent work of Woodruff and Yasuda (FOCS 2022) which gives streaming algorithms for high-dimensional geometric problems such as width estimation, convex hull estimation, and volume estimation.