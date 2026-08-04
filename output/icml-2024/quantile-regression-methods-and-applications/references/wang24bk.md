---
title: "Distributed High-Dimensional Quantile Regression: Estimation Efficiency and Support Recovery"
source: "https://proceedings.mlr.press/v235/wang24bk.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bk/wang24bk.pdf"
categories: ['quantile-regression-methods-and-applications', 'privacy-preserving-federated-and-distributed-learning']
tags: ['quantile-regression', 'distributed-estimation', 'high-dimensional-statistics', 'support-recovery']
venue: "ICML 2024"
tldr: "Studies distributed estimation and support recovery for high-dimensional linear quantile regression, establishing estimation efficiency and sparsity guarantees."
---

# Distributed High-Dimensional Quantile Regression: Estimation Efficiency and Support Recovery

**Source**: [https://proceedings.mlr.press/v235/wang24bk.html](https://proceedings.mlr.press/v235/wang24bk.html)

**TLDR**: Studies distributed estimation and support recovery for high-dimensional linear quantile regression, establishing estimation efficiency and sparsity guarantees.

## Abstract

In this paper, we focus on distributed estimation and support recovery for high-dimensional linear quantile regression. Quantile regression is a popular alternative tool to the least squares regression for robustness against outliers and data heterogeneity. However, the non-smoothness of the check loss function poses big challenges to both computation and theory in the distributed setting. To tackle these problems, we transform the original quantile regression into the least-squares optimization. By applying a double-smoothing approach, we extend a previous Newton-type distributed approach without the restrictive independent assumption between the error term and covariates. An efficient algorithm is developed, which enjoys high computation and communication efficiency. Theoretically, the proposed distributed estimator achieves a near-oracle convergence rate and high support recovery accuracy after a constant number of iterations. Extensive experiments on synthetic examples and a real data application further demonstrate the effectiveness of the proposed method.