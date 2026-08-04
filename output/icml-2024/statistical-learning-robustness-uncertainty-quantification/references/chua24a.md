---
title: "How Private are DP-SGD Implementations?"
source: "https://proceedings.mlr.press/v235/chua24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chua24a/chua24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'dp-sgd', 'batch-sampling']
venue: "ICML 2024"
tldr: "A significant privacy gap is demonstrated between shuffling and Poisson subsampling in practical DP-SGD implementations."
---

# How Private are DP-SGD Implementations?

**Source**: [https://proceedings.mlr.press/v235/chua24a.html](https://proceedings.mlr.press/v235/chua24a.html)

**TLDR**: A significant privacy gap is demonstrated between shuffling and Poisson subsampling in practical DP-SGD implementations.

## Abstract

We demonstrate a substantial gap between the privacy guarantees of the Adaptive Batch Linear Queries (ABLQ) mechanism under different types of batch sampling: (i) Shuffling, and (ii) Poisson subsampling; the typical analysis of Differentially Private Stochastic Gradient Descent (DP-SGD) follows by interpreting it as a post-processing of ABLQ. While shuffling-based DP-SGD is more commonly used in practical implementations, it has not been amenable to easy privacy analysis, either analytically or even numerically. On the other hand, Poisson subsampling-based DP-SGD is challenging to scalably implement, but has a well-understood privacy analysis, with multiple open-source numerically tight privacy accountants available. This has led to a common practice of using shuffling-based DP-SGD in practice, but using the privacy analysis for the corresponding Poisson subsampling version. Our result shows that there can be a substantial gap between the privacy analysis when using the two types of batch sampling, and thus advises caution in reporting privacy parameters for DP-SGD.