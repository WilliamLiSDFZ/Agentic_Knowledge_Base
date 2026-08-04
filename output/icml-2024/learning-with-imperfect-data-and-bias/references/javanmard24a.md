---
title: "PriorBoost: An Adaptive Algorithm for Learning from Aggregate Responses"
source: "https://proceedings.mlr.press/v235/javanmard24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/javanmard24a/javanmard24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['aggregate-responses', 'learning-from-bags', 'adaptive-algorithm', 'linear-regression', 'GLM']
venue: "ICML 2024"
tldr: "PriorBoost is an adaptive algorithm for learning from aggregate responses that reduces optimal bagging to one-dimensional optimization for linear and generalized linear models."
---

# PriorBoost: An Adaptive Algorithm for Learning from Aggregate Responses

**Source**: [https://proceedings.mlr.press/v235/javanmard24a.html](https://proceedings.mlr.press/v235/javanmard24a.html)

**TLDR**: PriorBoost is an adaptive algorithm for learning from aggregate responses that reduces optimal bagging to one-dimensional optimization for linear and generalized linear models.

## Abstract

This work studies algorithms for learning from aggregate responses. We focus on the construction of aggregation sets (called bags in the literature) for event-level loss functions. We prove for linear regression and generalized linear models (GLMs) that the optimal bagging problem reduces to one-dimensional size-constrained $k$-means clustering. Further, we theoretically quantify the advantage of using curated bags over random bags. We then propose the $\texttt{PriorBoost}$ algorithm, which adaptively forms bags of samples that are increasingly homogeneous with respect to (unobserved) individual responses to improve model quality. We study label differential privacy for aggregate learning, and we also provide extensive experiments showing that $\texttt{PriorBoost}$ regularly achieves optimal model quality for event-level predictions, in stark contrast to non-adaptive algorithms.