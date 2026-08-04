---
title: "A Subquadratic Time Algorithm for Robust Sparse Mean Estimation"
source: "https://proceedings.mlr.press/v235/pensia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pensia24a/pensia24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['sparse-mean-estimation', 'robust-statistics', 'subquadratic-algorithm', 'adversarial-outliers', 'high-dimensional']
venue: "ICML 2024"
tldr: "Presents a subquadratic time algorithm for robust sparse mean estimation under adversarial corruptions, improving over prior work."
---

# A Subquadratic Time Algorithm for Robust Sparse Mean Estimation

**Source**: [https://proceedings.mlr.press/v235/pensia24a.html](https://proceedings.mlr.press/v235/pensia24a.html)

**TLDR**: Presents a subquadratic time algorithm for robust sparse mean estimation under adversarial corruptions, improving over prior work.

## Abstract

We study the algorithmic problem of sparse mean estimation in the presence of adversarial outliers. Specifically, the algorithm observes a corrupted set of samples from $\mathcal{N}(\mu,\mathbf{I}_d)$, where the unknown mean $\mu \in \mathbb{R}^d$ is constrained to be $k$-sparse. A series of prior works has developed efficient algorithms for robust sparse mean estimation with sample complexity $\mathrm{poly}(k,\log d, 1/\epsilon)$ and runtime $d^2 \mathrm{poly}(k,\log d,1/\epsilon)$, where $\epsilon$ is the fraction of contamination. In particular, the fastest runtime of existing algorithms is quadratic in the dimension, which can be prohibitive in high dimensions. This quadratic barrier in the runtime stems from the reliance of these algorithms on the sample covariance matrix, which is of size $d^2$. Our main contribution is an algorithm for robust sparse mean estimation which runs in subquadratic time using $\mathrm{poly}(k,\log d,1/\epsilon)$ samples. Our results build on algorithmic advances in detecting weak correlations, a generalized version of the light-bulb problem by Valiant (2015).