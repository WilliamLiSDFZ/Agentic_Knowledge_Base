---
title: "Characterizing Overfitting in Kernel Ridgeless Regression Through the Eigenspectrum"
source: "https://proceedings.mlr.press/v235/cheng24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24g/cheng24g.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['kernel-regression', 'overfitting', 'eigenspectrum']
venue: "ICML 2024"
tldr: "New eigenspectrum-based bounds for kernel matrices are derived to characterize overfitting in kernel ridgeless regression in the over-parameterized regime."
---

# Characterizing Overfitting in Kernel Ridgeless Regression Through the Eigenspectrum

**Source**: [https://proceedings.mlr.press/v235/cheng24g.html](https://proceedings.mlr.press/v235/cheng24g.html)

**TLDR**: New eigenspectrum-based bounds for kernel matrices are derived to characterize overfitting in kernel ridgeless regression in the over-parameterized regime.

## Abstract

We derive new bounds for the condition number of kernel matrices, which we then use to enhance existing non-asymptotic test error bounds for kernel ridgeless regression in the over-parameterized regime for a fixed input dimension. For kernels with polynomial spectral decay, we recover the bound from previous work; for exponential decay, our bound is non-trivial and novel. Our conclusion is two-fold: (i) kernel regressors whose eigenspectrum decays polynomially must generalize well, even in the presence of noisy labeled training data; these models exhibit so-called tempered overfitting; (ii) if the eigenspectrum of any kernel ridge regressor decays exponentially, then it generalizes poorly, i.e., it exhibits catastrophic overfitting. This adds to the available characterization of kernel ridge regressors exhibiting benign overfitting as the extremal case where the eigenspectrum of the kernel decays sub-polynomially. Our analysis combines new random matrix theory (RMT) techniques with recent tools in the kernel ridge regression (KRR) literature.