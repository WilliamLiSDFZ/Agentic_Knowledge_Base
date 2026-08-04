---
title: "Overcoming Saturation in Density Ratio Estimation by Iterated Regularization"
source: "https://proceedings.mlr.press/v235/gruber24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gruber24b/gruber24b.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['density-ratio-estimation', 'kernel-methods', 'regularization']
venue: "ICML 2024"
tldr: "This paper identifies error saturation in kernel-based density ratio estimation and proposes iterated regularization to overcome it and achieve faster convergence."
---

# Overcoming Saturation in Density Ratio Estimation by Iterated Regularization

**Source**: [https://proceedings.mlr.press/v235/gruber24b.html](https://proceedings.mlr.press/v235/gruber24b.html)

**TLDR**: This paper identifies error saturation in kernel-based density ratio estimation and proposes iterated regularization to overcome it and achieve faster convergence.

## Abstract

Estimating the ratio of two probability densities from finitely many samples, is a central task in machine learning and statistics. In this work, we show that a large class of kernel methods for density ratio estimation suffers from error saturation, which prevents algorithms from achieving fast error convergence rates on highly regular learning problems. To resolve saturation, we introduce iterated regularization in density ratio estimation to achieve fast error rates. Our methods outperform its non-iteratively regularized versions on benchmarks for density ratio estimation as well as on large-scale evaluations for importance-weighted ensembling of deep unsupervised domain adaptation models.