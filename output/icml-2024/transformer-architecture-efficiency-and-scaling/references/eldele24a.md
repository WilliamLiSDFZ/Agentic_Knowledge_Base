---
title: "TSLANet: Rethinking Transformers for Time Series Representation Learning"
source: "https://proceedings.mlr.press/v235/eldele24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/eldele24a/eldele24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['time-series', 'transformer', 'representation-learning', 'adaptive-spectral-block', 'lightweight-architecture']
venue: "ICML 2024"
tldr: "Proposes TSLANet, a hybrid architecture combining adaptive spectral blocks with lightweight attention for robust time series representation learning."
---

# TSLANet: Rethinking Transformers for Time Series Representation Learning

**Source**: [https://proceedings.mlr.press/v235/eldele24a.html](https://proceedings.mlr.press/v235/eldele24a.html)

**TLDR**: Proposes TSLANet, a hybrid architecture combining adaptive spectral blocks with lightweight attention for robust time series representation learning.

## Abstract

Time series data, characterized by its intrinsic long and short-range dependencies, poses a unique challenge across analytical applications. While Transformer-based models excel at capturing long-range dependencies, they face limitations in noise sensitivity, computational efficiency, and overfitting with smaller datasets. In response, we introduce a novel Time Series Lightweight Adaptive Network (TSLANet), as a universal convolutional model for diverse time series tasks. Specifically, we propose an Adaptive Spectral Block, harnessing Fourier analysis to enhance feature representation and to capture both long-term and short-term interactions while mitigating noise via adaptive thresholding. Additionally, we introduce an Interactive Convolution Block and leverage self-supervised learning to refine the capacity of TSLANet for decoding complex temporal patterns and improve its robustness on different datasets. Our comprehensive experiments demonstrate that TSLANet outperforms state-of-the-art models in various tasks spanning classification, forecasting, and anomaly detection, showcasing its resilience and adaptability across a spectrum of noise levels and data sizes. The code is available at https://github.com/emadeldeen24/TSLANet.