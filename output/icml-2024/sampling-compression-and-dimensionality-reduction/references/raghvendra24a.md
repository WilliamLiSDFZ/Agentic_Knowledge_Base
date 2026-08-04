---
title: "A New Robust Partial p-Wasserstein-Based Metric for Comparing Distributions"
source: "https://proceedings.mlr.press/v235/raghvendra24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/raghvendra24a/raghvendra24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['Wasserstein-distance', 'robust-metric', 'outliers', 'partial-transport', 'distribution-comparison']
venue: "ICML 2024"
tldr: "A robust partial p-Wasserstein metric that reduces sensitivity to outliers when comparing distributions."
---

# A New Robust Partial p-Wasserstein-Based Metric for Comparing Distributions

**Source**: [https://proceedings.mlr.press/v235/raghvendra24a.html](https://proceedings.mlr.press/v235/raghvendra24a.html)

**TLDR**: A robust partial p-Wasserstein metric that reduces sensitivity to outliers when comparing distributions.

## Abstract

The $2$-Wasserstein distance is sensitive to minor geometric differences between distributions, making it a very powerful dissimilarity metric. However, due to this sensitivity, a small outlier mass can also cause a significant increase in the $2$-Wasserstein distance between two similar distributions. Similarly, sampling discrepancy can cause the empirical $2$-Wasserstein distance on $n$ samples in $\mathbb{R}^2$ to converge to the true distance at a rate of $n^{-1/4}$, which is significantly slower than the rate of $n^{-1/2}$ for $1$-Wasserstein distance. We introduce a new family of distances parameterized by $k \ge 0$, called $k$-RPW that is based on computing the partial $2$-Wasserstein distance. We show that (1) $k$-RPW satisfies the metric properties, (2) $k$-RPW is robust to small outlier mass while retaining the sensitivity of $2$-Wasserstein distance to minor geometric differences, and (3) when $k$ is a constant, $k$-RPW distance between empirical distributions on $n$ samples in $\mathbb{R}^2$ converges to the true distance at a rate of $n^{-1/3}$, which is faster than the convergence rate of $n^{-1/4}$ for the $2$-Wasserstein distance. Using the partial $p$-Wasserstein distance, we extend our distance to any $p \in [1,\infty]$. By setting parameters $k$ or $p$ appropriately, we can reduce our distance to the total variation, $p$-Wasserstein, and the Lévy-Prokhorov distances. Experiments show that our distance function achieves higher accuracy in comparison to the $1$-Wasserstein, $2$-Wasserstein, and TV distances for image retrieval tasks on noisy real-world data sets.