---
title: "Subsampling is not Magic: Why Large Batch Sizes Work for Differentially Private Stochastic Optimisation"
source: "https://proceedings.mlr.press/v235/raisa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/raisa24a/raisa24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'DP-SGD', 'batch-size', 'gradient-variance', 'privacy-amplification']
venue: "ICML 2024"
tldr: "Theoretically explains why large batch sizes benefit differentially private SGD by analyzing total gradient variance."
---

# Subsampling is not Magic: Why Large Batch Sizes Work for Differentially Private Stochastic Optimisation

**Source**: [https://proceedings.mlr.press/v235/raisa24a.html](https://proceedings.mlr.press/v235/raisa24a.html)

**TLDR**: Theoretically explains why large batch sizes benefit differentially private SGD by analyzing total gradient variance.

## Abstract

We study how the batch size affects the total gradient variance in differentially private stochastic gradient descent (DP-SGD), seeking a theoretical explanation for the usefulness of large batch sizes. As DP-SGD is the basis of modern DP deep learning, its properties have been widely studied, and recent works have empirically found large batch sizes to be beneficial. However, theoretical explanations of this benefit are currently heuristic at best. We first observe that the total gradient variance in DP-SGD can be decomposed into subsampling-induced and noise-induced variances. We then prove that in the limit of an infinite number of iterations, the effective noise-induced variance is invariant to the batch size. The remaining subsampling-induced variance decreases with larger batch sizes, so large batches reduce the effective total gradient variance. We confirm numerically that the asymptotic regime is relevant in practical settings when the batch size is not small, and find that outside the asymptotic regime, the total gradient variance decreases even more with large batch sizes. We also find a sufficient condition that implies that large batch sizes similarly reduce effective DP noise variance for one iteration of DP-SGD.