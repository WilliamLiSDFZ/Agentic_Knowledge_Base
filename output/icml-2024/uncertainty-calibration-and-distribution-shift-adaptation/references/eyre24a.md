---
title: "Out of the Ordinary: Spectrally Adapting Regression for Covariate Shift"
source: "https://proceedings.mlr.press/v235/eyre24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/eyre24a/eyre24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['covariate-shift', 'regression', 'spectral-adaptation', 'distribution-shift', 'out-of-distribution']
venue: "ICML 2024"
tldr: "Proposes a spectral adaptation method for regression under covariate shift that improves out-of-distribution generalization for continuous targets."
---

# Out of the Ordinary: Spectrally Adapting Regression for Covariate Shift

**Source**: [https://proceedings.mlr.press/v235/eyre24a.html](https://proceedings.mlr.press/v235/eyre24a.html)

**TLDR**: Proposes a spectral adaptation method for regression under covariate shift that improves out-of-distribution generalization for continuous targets.

## Abstract

Designing deep neural network classifiers that perform robustly on distributions differing from the available training data is an active area of machine learning research. However, out-of-distribution generalization for regression—the analogous problem for modeling continuous targets—remains relatively unexplored. To tackle this problem, we return to first principles and analyze how the closed-form solution for Ordinary Least Squares (OLS) regression is sensitive to covariate shift. We characterize the out-of-distribution risk of the OLS model in terms of the eigenspectrum decomposition of the source and target data. We then use this insight to propose a method called Spectral Adapted Regressor (SpAR) for adapting the weights of the last layer of a pre-trained neural regression model to perform better on input data originating from a different distribution. We demonstrate how this lightweight spectral adaptation procedure can improve out-of-distribution performance for synthetic and real-world datasets.