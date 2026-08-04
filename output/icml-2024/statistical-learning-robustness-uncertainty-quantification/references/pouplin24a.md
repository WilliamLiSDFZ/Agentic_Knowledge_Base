---
title: "Relaxed Quantile Regression: Prediction Intervals for Asymmetric Noise"
source: "https://proceedings.mlr.press/v235/pouplin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pouplin24a/pouplin24a.pdf"
categories: ['quantile-regression-methods-and-applications', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['quantile-regression', 'prediction-intervals', 'asymmetric-noise']
venue: "ICML 2024"
tldr: "A relaxed quantile regression approach for constructing valid prediction intervals under asymmetric noise distributions."
---

# Relaxed Quantile Regression: Prediction Intervals for Asymmetric Noise

**Source**: [https://proceedings.mlr.press/v235/pouplin24a.html](https://proceedings.mlr.press/v235/pouplin24a.html)

**TLDR**: A relaxed quantile regression approach for constructing valid prediction intervals under asymmetric noise distributions.

## Abstract

Constructing valid prediction intervals rather than point estimates is a well-established approach for uncertainty quantification in the regression setting. Models equipped with this capacity output an interval of values in which the ground truth target will fall with some prespecified probability. This is an essential requirement in many real-world applications where simple point predictions’ inability to convey the magnitude and frequency of errors renders them insufficient for high-stakes decisions. Quantile regression is a leading approach for obtaining such intervals via the empirical estimation of quantiles in the (non-parametric) distribution of outputs. This method is simple, computationally inexpensive, interpretable, assumption-free, and effective. However, it does require that the specific quantiles being learned are chosen a priori. This results in (a) intervals that are arbitrarily symmetric around the median which is sub-optimal for realistic skewed distributions, or (b) learning an excessive number of intervals. In this work, we propose Relaxed Quantile Regression (RQR), a direct alternative to quantile regression based interval construction that removes this arbitrary constraint whilst maintaining its strengths. We demonstrate that this added flexibility results in intervals with an improvement in desirable qualities (e.g. mean width) whilst retaining the essential coverage guarantees of quantile regression.