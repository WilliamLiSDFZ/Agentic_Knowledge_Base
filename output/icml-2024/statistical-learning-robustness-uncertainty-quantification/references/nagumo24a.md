---
title: "Density Ratio Estimation with Doubly Strong Robustness"
source: "https://proceedings.mlr.press/v235/nagumo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nagumo24a/nagumo24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['density-ratio-estimation', 'outlier-robustness', 'divergence-minimization']
venue: "ICML 2024"
tldr: "Two density ratio estimation methods with doubly strong robustness to outliers are proposed using weighted divergence formulations."
---

# Density Ratio Estimation with Doubly Strong Robustness

**Source**: [https://proceedings.mlr.press/v235/nagumo24a.html](https://proceedings.mlr.press/v235/nagumo24a.html)

**TLDR**: Two density ratio estimation methods with doubly strong robustness to outliers are proposed using weighted divergence formulations.

## Abstract

We develop two density ratio estimation (DRE) methods with robustness to outliers. These are based on the divergence with a weight function to weaken the adverse effects of outliers. One is based on the Unnormalized Kullback-Leibler divergence, called Weighted DRE, and its optimization is a convex problem. The other is based on the γ-divergence, called γ-DRE, which improves a normalizing term problem of Weighted DRE. Its optimization is a DC (Difference of Convex functions) problem and needs more computation than a convex problem. These methods have doubly strong robustness, which means robustness to the heavy contamination of both the reference and target distributions. Numerical experiments show that our proposals are more robust than the previous methods.