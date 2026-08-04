---
title: "Near-Linear Time Approximation Algorithms for k-means with Outliers"
source: "https://proceedings.mlr.press/v235/huang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24e/huang24e.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['k-means-clustering', 'outlier-detection', 'near-linear-time']
venue: "ICML 2024"
tldr: "Proposes near-linear time approximation algorithms for the k-means with outliers clustering problem."
---

# Near-Linear Time Approximation Algorithms for k-means with Outliers

**Source**: [https://proceedings.mlr.press/v235/huang24e.html](https://proceedings.mlr.press/v235/huang24e.html)

**TLDR**: Proposes near-linear time approximation algorithms for the k-means with outliers clustering problem.

## Abstract

The k-means with outliers problem is one of the most extensively studied clustering problems in the field of machine learning, where the goal is to discard up to z outliers and identify a minimum k-means clustering on the remaining data points. Most previous results for this problem have running time dependent on the aspect ratio Δ (the ratio between the maximum and the minimum pairwise distances) to achieve fast approximations. To address the issue of aspect ratio dependency on the running time, we propose sampling-based algorithms with almost linear running time in the data size, where a crucial component of our approach is an algorithm called Fast-Sampling. Fast-Sampling algorithm can find inliers that well approximate the optimal clustering centers without relying on a guess for the optimal clustering costs, where a 4-approximate solution can be obtained in time $O(\frac{ndk\log\log n}{\epsilon^2})$ with O(k/ϵ) centers opened and (1+ϵ)z outliers discarded. To reduce the number of centers opened, we propose a center reduction algorithm, where an O(1/ϵ)-approximate solution can be obtained in time $O(\frac{ndk\log \log n}{\epsilon^2} + dpoly(k, \frac{1}{\epsilon})\log(n\Delta))$ with (1+ϵ)z outliers discarded and exactly k centers opened. Empirical experiments suggest that our proposed sampling-based algorithms outperform state-of-the-art algorithms for the k-means with outliers problem.