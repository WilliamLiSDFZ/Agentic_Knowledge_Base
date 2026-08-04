---
title: "SparseTSF: Modeling Long-term Time Series Forecasting with *1k* Parameters"
source: "https://proceedings.mlr.press/v235/lin24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24n/lin24n.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['time-series-forecasting', 'lightweight-model', 'sparse-periodicity']
venue: "ICML 2024"
tldr: "SparseTSF is an extremely lightweight model for long-term time series forecasting using cross-period sparse sampling."
---

# SparseTSF: Modeling Long-term Time Series Forecasting with *1k* Parameters

**Source**: [https://proceedings.mlr.press/v235/lin24n.html](https://proceedings.mlr.press/v235/lin24n.html)

**TLDR**: SparseTSF is an extremely lightweight model for long-term time series forecasting using cross-period sparse sampling.

## Abstract

This paper introduces SparseTSF, a novel, extremely lightweight model for Long-term Time Series Forecasting (LTSF), designed to address the challenges of modeling complex temporal dependencies over extended horizons with minimal computational resources. At the heart of SparseTSF lies the Cross-Period Sparse Forecasting technique, which simplifies the forecasting task by decoupling the periodicity and trend in time series data. This technique involves downsampling the original sequences to focus on cross-period trend prediction, effectively extracting periodic features while minimizing the model’s complexity and parameter count. Based on this technique, the SparseTSF model uses fewer than 1k parameters to achieve competitive or superior performance compared to state-of-the-art models. Furthermore, SparseTSF showcases remarkable generalization capabilities, making it well-suited for scenarios with limited computational resources, small samples, or low-quality data. The code is publicly available at this repository: https://github.com/lss-1138/SparseTSF.