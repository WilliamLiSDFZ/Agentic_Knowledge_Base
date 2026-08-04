---
title: "Simulation-Based Inference with Quantile Regression"
source: "https://proceedings.mlr.press/v235/jia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jia24a/jia24a.pdf"
categories: ['quantile-regression-methods-and-applications', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['simulation-based-inference', 'quantile-regression', 'posterior-estimation', 'autoregressive']
venue: "ICML 2024"
tldr: "Neural Quantile Estimation autoregressively learns one-dimensional conditional quantiles for each posterior dimension to perform simulation-based inference."
---

# Simulation-Based Inference with Quantile Regression

**Source**: [https://proceedings.mlr.press/v235/jia24a.html](https://proceedings.mlr.press/v235/jia24a.html)

**TLDR**: Neural Quantile Estimation autoregressively learns one-dimensional conditional quantiles for each posterior dimension to perform simulation-based inference.

## Abstract

We present Neural Quantile Estimation (NQE), a novel Simulation-Based Inference (SBI) method based on conditional quantile regression. NQE autoregressively learns individual one dimensional quantiles for each posterior dimension, conditioned on the data and previous posterior dimensions. Posterior samples are obtained by interpolating the predicted quantiles using monotonic cubic Hermite spline, with specific treatment for the tail behavior and multi-modal distributions. We introduce an alternative definition for the Bayesian credible region using the local Cumulative Density Function (CDF), offering substantially faster evaluation than the traditional Highest Posterior Density Region (HPDR). In case of limited simulation budget and/or known model misspecification, a post-processing calibration step can be integrated into NQE to ensure the unbiasedness of the posterior estimation with negligible additional computational cost. We demonstrate that NQE achieves state-of-the-art performance on a variety of benchmark problems.