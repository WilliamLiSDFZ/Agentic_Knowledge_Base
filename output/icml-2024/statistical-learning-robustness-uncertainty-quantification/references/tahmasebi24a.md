---
title: "Sample Complexity Bounds for Estimating Probability Divergences under Invariances"
source: "https://proceedings.mlr.press/v235/tahmasebi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tahmasebi24a/tahmasebi24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['group-invariance', 'divergence-estimation', 'sample-complexity']
venue: "ICML 2024"
tldr: "Sample complexity bounds for estimating probability divergences are derived under group-invariance structures common in graph and point cloud data."
---

# Sample Complexity Bounds for Estimating Probability Divergences under Invariances

**Source**: [https://proceedings.mlr.press/v235/tahmasebi24a.html](https://proceedings.mlr.press/v235/tahmasebi24a.html)

**TLDR**: Sample complexity bounds for estimating probability divergences are derived under group-invariance structures common in graph and point cloud data.

## Abstract

Group-invariant probability distributions appear in many data-generative models in machine learning, such as graphs, point clouds, and images. In practice, one often needs to estimate divergences between such distributions. In this work, we study how the inherent invariances, with respect to any smooth action of a Lie group on a manifold, improve sample complexity when estimating the 1-Wasserstein distance, the Sobolev Integral Probability Metrics (Sobolev IPMs), the Maximum Mean Discrepancy (MMD), and also the complexity of the density estimation problem (in the $L^2$ and $L^\infty$ distance). Our results indicate a two-fold gain: (1) reducing the sample complexity by a multiplicative factor corresponding to the group size (for finite groups) or the normalized volume of the quotient space (for groups of positive dimension); (2) improving the exponent in the convergence rate (for groups of positive dimension). These results are completely new for groups of positive dimension and extend recent bounds for finite group actions.