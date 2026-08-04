---
title: "Differentially Private Post-Processing for Fair Regression"
source: "https://proceedings.mlr.press/v235/xian24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xian24b/xian24b.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['differential-privacy', 'fairness', 'regression']
venue: "ICML 2024"
tldr: "A differentially private post-processing algorithm for fair regression satisfying statistical parity while preserving privacy."
---

# Differentially Private Post-Processing for Fair Regression

**Source**: [https://proceedings.mlr.press/v235/xian24b.html](https://proceedings.mlr.press/v235/xian24b.html)

**TLDR**: A differentially private post-processing algorithm for fair regression satisfying statistical parity while preserving privacy.

## Abstract

This paper describes a differentially private post-processing algorithm for learning fair regressors satisfying statistical parity, addressing privacy concerns of machine learning models trained on sensitive data, as well as fairness concerns of their potential to propagate historical biases. Our algorithm can be applied to post-process any given regressor to improve fairness by remapping its outputs. It consists of three steps: first, the output distributions are estimated privately via histogram density estimation and the Laplace mechanism, then their Wasserstein barycenter is computed, and the optimal transports to the barycenter are used for post-processing to satisfy fairness. We analyze the sample complexity of our algorithm and provide fairness guarantee, revealing a trade-off between the statistical bias and variance induced from the choice of the number of bins in the histogram, in which using less bins always favors fairness at the expense of error.