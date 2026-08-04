---
title: "Sampling-based Multi-dimensional Recalibration"
source: "https://proceedings.mlr.press/v235/chung24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chung24a/chung24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['calibration', 'multivariate-forecasting', 'probabilistic-prediction']
venue: "ICML 2024"
tldr: "A sampling-based approach for multi-dimensional recalibration of probabilistic forecasts that handles dependencies across output dimensions."
---

# Sampling-based Multi-dimensional Recalibration

**Source**: [https://proceedings.mlr.press/v235/chung24a.html](https://proceedings.mlr.press/v235/chung24a.html)

**TLDR**: A sampling-based approach for multi-dimensional recalibration of probabilistic forecasts that handles dependencies across output dimensions.

## Abstract

Calibration of probabilistic forecasts in the regression setting has been widely studied in the single dimensional case, where the output variables are assumed to be univariate. In many problem settings, however, the output variables are multi-dimensional, and in the presence of dependence across the output dimensions, measuring calibration and performing recalibration for each dimension separately can be both misleading and detrimental. In this work, we focus on representing predictive uncertainties via samples, and propose a recalibration method which accounts for the joint distribution across output dimensions to produce calibrated samples. Based on the concept of highest density regions (HDR), we define the notion of HDR calibration, and show that our recalibration method produces samples which are HDR calibrated. We demonstrate the performance of our method and the quality of the recalibrated samples on a suite of benchmark datasets in multi-dimensional regression, a real-world dataset in modeling plasma dynamics during nuclear fusion reactions, and on a decision-making application in forecasting demand.