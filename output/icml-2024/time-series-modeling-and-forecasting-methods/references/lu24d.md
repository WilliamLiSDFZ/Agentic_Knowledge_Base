---
title: "CATS: Enhancing Multivariate Time Series Forecasting by Constructing Auxiliary Time Series as Exogenous Variables"
source: "https://proceedings.mlr.press/v235/lu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24d/lu24d.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['multivariate-time-series', 'forecasting', 'auxiliary-variables', 'exogenous-variables', 'deep-learning']
venue: "ICML 2024"
tldr: "Improves multivariate time series forecasting by constructing auxiliary time series as exogenous variables to capture inter-variable dependencies."
---

# CATS: Enhancing Multivariate Time Series Forecasting by Constructing Auxiliary Time Series as Exogenous Variables

**Source**: [https://proceedings.mlr.press/v235/lu24d.html](https://proceedings.mlr.press/v235/lu24d.html)

**TLDR**: Improves multivariate time series forecasting by constructing auxiliary time series as exogenous variables to capture inter-variable dependencies.

## Abstract

For Multivariate Time Series Forecasting (MTSF), recent deep learning applications show that univariate models frequently outperform multivariate ones. To address the deficiency in multivariate models, we introduce a method to Construct Auxiliary Time Series (CATS) that functions like a 2D temporal-contextual attention mechanism, which generates Auxiliary Time Series (ATS) from Original Time Series (OTS) to effectively represent and incorporate inter-series relationships for forecasting. Key principles of ATS—continuity, sparsity, and variability—are identified and implemented through different modules. Even with a basic 2-layer MLP as the core predictor, CATS achieves state-of-the-art, significantly reducing complexity and parameters compared to previous multivariate models, marking it as an efficient and transferable MTSF solution.