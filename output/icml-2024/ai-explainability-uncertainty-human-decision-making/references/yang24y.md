---
title: "Explain Temporal Black-Box Models via Functional Decomposition"
source: "https://proceedings.mlr.press/v235/yang24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24y/yang24y.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'time-series-modeling-and-forecasting-methods']
tags: ['temporal-explanation', 'functional-decomposition', 'time-series']
venue: "ICML 2024"
tldr: "A method to explain temporal black-box models via functional decomposition that accounts for strong temporal dependencies in time series data."
---

# Explain Temporal Black-Box Models via Functional Decomposition

**Source**: [https://proceedings.mlr.press/v235/yang24y.html](https://proceedings.mlr.press/v235/yang24y.html)

**TLDR**: A method to explain temporal black-box models via functional decomposition that accounts for strong temporal dependencies in time series data.

## Abstract

How to explain temporal models is a significant challenge due to the inherent characteristics of time series data, notably the strong temporal dependencies and interactions between observations. Unlike ordinary tabular data, data at different time steps in time series usually interact dynamically, forming influential patterns that shape the model’s predictions, rather than only acting in isolation. Existing explanatory approaches for time series often overlook these crucial temporal interactions by treating time steps as separate entities, leading to a superficial understanding of model behavior. To address this challenge, we introduce FDTempExplainer, an innovative model-agnostic explanation method based on functional decomposition, tailored to unravel the complex interplay within black-box time series models. Our approach disentangles the individual contributions from each time step, as well as the aggregated influence of their interactions, in a rigorous framework. FDTempExplainer accurately measures the strength of interactions, yielding insights that surpass those from baseline models. We demonstrate the effectiveness of our approach in a wide range of time series applications, including anomaly detection, classification, and forecasting, showing its superior performance to the state-of-the-art algorithms.