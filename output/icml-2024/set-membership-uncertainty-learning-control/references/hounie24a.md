---
title: "Loss Shaping Constraints for Long-Term Time Series Forecasting"
source: "https://proceedings.mlr.press/v235/hounie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hounie24a/hounie24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'set-membership-uncertainty-learning-control']
tags: ['time-series', 'long-horizon-forecasting', 'loss-shaping', 'constraints', 'deep-learning']
venue: "ICML 2024"
tldr: "Introduces loss shaping constraints for long-term time series forecasting to control per-step prediction error distribution beyond average performance."
---

# Loss Shaping Constraints for Long-Term Time Series Forecasting

**Source**: [https://proceedings.mlr.press/v235/hounie24a.html](https://proceedings.mlr.press/v235/hounie24a.html)

**TLDR**: Introduces loss shaping constraints for long-term time series forecasting to control per-step prediction error distribution beyond average performance.

## Abstract

Several applications in time series forecasting require predicting multiple steps ahead. Despite the vast amount of literature in the topic, both classical and recent deep learning based approaches have mostly focused on minimising performance averaged over the predicted window. We observe that this can lead to disparate distributions of errors across forecasting steps, especially for recent transformer architectures trained on popular forecasting benchmarks. That is, optimising performance on average can lead to undesirably large errors at specific time-steps. In this work, we present a Constrained Learning approach for long-term time series forecasting that aims to find the best model in terms of average performance that respects a user-defined upper bound on the loss at each time-step. We call our approach loss shaping constraints because it imposes constraints on the loss at each time step, and leverage recent duality results to show that despite its non-convexity, the resulting problem has a bounded duality gap. We propose a practical primal-dual algorithm to tackle it, and demonstrate that the proposed approach exhibits competitive average performance in time series forecasting benchmarks, while shaping the distribution of errors across the predicted window.