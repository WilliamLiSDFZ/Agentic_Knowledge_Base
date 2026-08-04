---
title: "Amortized Variational Deep Kernel Learning"
source: "https://proceedings.mlr.press/v235/matias24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/matias24a/matias24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['deep-kernel-learning', 'Gaussian-processes', 'amortized-variational-inference']
venue: "ICML 2024"
tldr: "Amortized variational inference for deep kernel learning that mitigates overfitting and spurious non-local kernel correlations."
---

# Amortized Variational Deep Kernel Learning

**Source**: [https://proceedings.mlr.press/v235/matias24a.html](https://proceedings.mlr.press/v235/matias24a.html)

**TLDR**: Amortized variational inference for deep kernel learning that mitigates overfitting and spurious non-local kernel correlations.

## Abstract

Deep kernel learning (DKL) marries the uncertainty quantification of Gaussian processes (GPs) and the representational power of deep neural networks. However, training DKL is challenging and often leads to overfitting. Most notably, DKL often learns “non-local” kernels — incurring spurious correlations. To remedy this issue, we propose using amortized inducing points and a parameter-sharing scheme, which ties together the amortization and DKL networks. This design imposes an explicit dependency between the ELBO’s model fit and capacity terms. In turn, this prevents the former from dominating the optimization procedure and incurring the aforementioned spurious correlations. Extensive experiments show that our resulting method, amortized varitional DKL (AVDKL), i) consistently outperforms DKL and standard GPs for tabular data; ii) achieves significantly higher accuracy than DKL in node classification tasks; and iii) leads to substantially better accuracy and negative log-likelihood than DKL on CIFAR100.