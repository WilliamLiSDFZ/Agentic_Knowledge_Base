---
title: "SIN: Selective and Interpretable Normalization for Long-Term Time Series Forecasting"
source: "https://proceedings.mlr.press/v235/han24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24e/han24e.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['normalization', 'non-stationarity', 'time-series-forecasting']
venue: "ICML 2024"
tldr: "A selective and interpretable normalization method is proposed to handle non-stationary statistics in long-term time series forecasting."
---

# SIN: Selective and Interpretable Normalization for Long-Term Time Series Forecasting

**Source**: [https://proceedings.mlr.press/v235/han24e.html](https://proceedings.mlr.press/v235/han24e.html)

**TLDR**: A selective and interpretable normalization method is proposed to handle non-stationary statistics in long-term time series forecasting.

## Abstract

In real-world applications, time series data frequently exhibit non-stationarity, with statistics changing over time. This variability undermines the forecasting accuracy of deep learning models that are trained on historical data but deployed for future prediction. A common approach to mitigate this issue involves normalizing the data to counteract statistical drift, followed by denormalization on the prediction. However, existing methods often employ heuristic normalization techniques that do not fully account for the unique characteristics of the series. Our paper addresses the critical question in this context: which statistics should be removed and restored? We argue that the statistics selected for normalization should exhibit both local invariance and global variability to ensure their correctness and helpfulness. To this end, we propose the Selective and Interpretable Normalization methodology, dubbed SIN. This approach maximizes the covariance between a given look-back window and its subsequent future values, thereby identifying key statistics for normalization and simultaneously learning the corresponding normalization transformations. The interpretable framework can be used to explain the success and limitations of some popular normalization methods. By integrating SIN, we demonstrate improvements in the performance of several prevalent forecasting models, thereby validating the utility of our approach.