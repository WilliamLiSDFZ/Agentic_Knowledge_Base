---
title: "Revitalizing Multivariate Time Series Forecasting: Learnable Decomposition with Inter-Series Dependencies and Intra-Series Variations Modeling"
source: "https://proceedings.mlr.press/v235/yu24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24s/yu24s.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'neural-network-learning-dynamics-theory']
tags: ['multivariate-time-series', 'learnable-decomposition', 'inter-series-dependencies']
venue: "ICML 2024"
tldr: "A time series forecasting model with learnable trend decomposition and joint modeling of inter-series dependencies and intra-series variations."
---

# Revitalizing Multivariate Time Series Forecasting: Learnable Decomposition with Inter-Series Dependencies and Intra-Series Variations Modeling

**Source**: [https://proceedings.mlr.press/v235/yu24s.html](https://proceedings.mlr.press/v235/yu24s.html)

**TLDR**: A time series forecasting model with learnable trend decomposition and joint modeling of inter-series dependencies and intra-series variations.

## Abstract

Predicting multivariate time series is crucial, demanding precise modeling of intricate patterns, including inter-series dependencies and intra-series variations. Distinctive trend characteristics in each time series pose challenges, and existing methods, relying on basic moving average kernels, may struggle with the non-linear structure and complex trends in real-world data. Given that, we introduce a learnable decomposition strategy to capture dynamic trend information more reasonably. Additionally, we propose a dual attention module tailored to capture inter-series dependencies and intra-series variations simultaneously for better time series forecasting, which is implemented by channel-wise self-attention and autoregressive self-attention. To evaluate the effectiveness of our method, we conducted experiments across eight open-source datasets and compared it with the state-of-the-art methods. Through the comparison results, our $\textbf{Leddam}$ ($\textbf{LE}arnable$ $\textbf{D}ecomposition$ and $\textbf{D}ual $ $\textbf{A}ttention$ $\textbf{M}odule$) not only demonstrates significant advancements in predictive performance but also the proposed decomposition strategy can be plugged into other methods with a large performance-boosting, from 11.87% to 48.56% MSE error degradation. Code is available at this link: https://github.com/Levi-Ackman/Leddam.