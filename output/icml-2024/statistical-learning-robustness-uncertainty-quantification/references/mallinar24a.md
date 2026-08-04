---
title: "Minimum-Norm Interpolation Under Covariate Shift"
source: "https://proceedings.mlr.press/v235/mallinar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mallinar24a/mallinar24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'learning-with-imperfect-data-and-bias']
tags: ['covariate-shift', 'minimum-norm-interpolation', 'transfer-learning']
venue: "ICML 2024"
tldr: "A theoretical analysis of minimum-norm interpolation under covariate shift in linear regression, bridging the gap in transfer learning theory."
---

# Minimum-Norm Interpolation Under Covariate Shift

**Source**: [https://proceedings.mlr.press/v235/mallinar24a.html](https://proceedings.mlr.press/v235/mallinar24a.html)

**TLDR**: A theoretical analysis of minimum-norm interpolation under covariate shift in linear regression, bridging the gap in transfer learning theory.

## Abstract

Transfer learning is a critical part of real-world machine learning deployments and has been extensively studied in experimental works with overparameterized neural networks. However, even in the simplest setting of linear regression a notable gap still exists in the theoretical understanding of transfer learning. In-distribution research on high-dimensional linear regression has led to the identification of a phenomenon known as benign overfitting, in which linear interpolators overfit to noisy training labels and yet still generalize well. This behavior occurs under specific conditions on the source covariance matrix and input data dimension. Therefore, it is natural to wonder how such high-dimensional linear models behave under transfer learning. We prove the first non-asymptotic excess risk bounds for benignly-overfit linear interpolators in the transfer learning setting. From our analysis, we propose a taxonomy of beneficial and malignant covariate shifts based on the degree of overparameterization. We follow our analysis with empirical studies that show these beneficial and malignant covariate shifts for linear interpolators on real image data, and for fully-connected neural networks in settings where the input data dimension is larger than the training sample size.