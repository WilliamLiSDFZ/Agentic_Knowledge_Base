---
title: "High-Dimensional Kernel Methods under Covariate Shift: Data-Dependent Implicit Regularization"
source: "https://proceedings.mlr.press/v235/chen24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24aa/chen24aa.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'learning-with-imperfect-data-and-bias']
tags: ['kernel-ridge-regression', 'covariate-shift', 'importance-weighting', 'high-dimensional']
venue: "ICML 2024"
tldr: "Analyzes kernel ridge regression under covariate shift in high dimensions, showing importance re-weighting induces implicit regularization via bias-variance tradeoff."
---

# High-Dimensional Kernel Methods under Covariate Shift: Data-Dependent Implicit Regularization

**Source**: [https://proceedings.mlr.press/v235/chen24aa.html](https://proceedings.mlr.press/v235/chen24aa.html)

**TLDR**: Analyzes kernel ridge regression under covariate shift in high dimensions, showing importance re-weighting induces implicit regularization via bias-variance tradeoff.

## Abstract

This paper studies kernel ridge regression in high dimensions under covariate shifts and analyzes the role of importance re-weighting. We first derive the asymptotic expansion of high dimensional kernels under covariate shifts. By a bias-variance decomposition, we theoretically demonstrate that the re-weighting strategy allows for decreasing the variance. For bias, we analyze the regularization of the arbitrary or well-chosen scale, showing that the bias can behave very differently under different regularization scales. In our analysis, the bias and variance can be characterized by the spectral decay of a data-dependent regularized kernel: the original kernel matrix associated with an additional re-weighting matrix, and thus the re-weighting strategy can be regarded as a data-dependent regularization for better understanding. Besides, our analysis provides asymptotic expansion of kernel functions/vectors under covariate shift, which has its own interest.