---
title: "Sobolev Space Regularised Pre Density Models"
source: "https://proceedings.mlr.press/v235/kozdoba24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kozdoba24a/kozdoba24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['density-estimation', 'sobolev-regularization', 'kernel-methods']
venue: "ICML 2024"
tldr: "A non-parametric density estimation approach using Sobolev norm regularization that is statistically consistent with interpretable inductive bias."
---

# Sobolev Space Regularised Pre Density Models

**Source**: [https://proceedings.mlr.press/v235/kozdoba24a.html](https://proceedings.mlr.press/v235/kozdoba24a.html)

**TLDR**: A non-parametric density estimation approach using Sobolev norm regularization that is statistically consistent with interpretable inductive bias.

## Abstract

We propose a new approach to non-parametric density estimation that is based on regularizing a Sobolev norm of the density. This method is statistically consistent, and makes the inductive bias of the model clear and interpretable. While there is no closed analytic form for the associated kernel, we show that one can approximate it using sampling. The optimization problem needed to determine the density is non-convex, and standard gradient methods do not perform well. However, we show that with an appropriate initialization and using natural gradients, one can obtain well performing solutions. Finally, while the approach provides pre-densities (i.e. not necessarily integrating to 1), which prevents the use of log-likelihood for cross validation, we show that one can instead adapt Fisher divergence based score matching methods for this task. We evaluate the resulting method on the comprehensive recent anomaly detection benchmark suite, ADBench, and find that it ranks second best, among more than 15 algorithms.