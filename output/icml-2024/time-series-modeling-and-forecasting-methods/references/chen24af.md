---
title: "TimeMIL: Advancing Multivariate Time Series Classification via a Time-aware Multiple Instance Learning"
source: "https://proceedings.mlr.press/v235/chen24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24af/chen24af.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['time-series-classification', 'multiple-instance-learning', 'multivariate', 'transformers']
venue: "ICML 2024"
tldr: "Proposes TimeMIL, a time-aware multiple instance learning framework for multivariate time series classification capturing sparse and local patterns."
---

# TimeMIL: Advancing Multivariate Time Series Classification via a Time-aware Multiple Instance Learning

**Source**: [https://proceedings.mlr.press/v235/chen24af.html](https://proceedings.mlr.press/v235/chen24af.html)

**TLDR**: Proposes TimeMIL, a time-aware multiple instance learning framework for multivariate time series classification capturing sparse and local patterns.

## Abstract

Deep neural networks, including transformers and convolutional neural networks (CNNs), have significantly improved multivariate time series classification (MTSC). However, these methods often rely on supervised learning, which does not fully account for the sparsity and locality of patterns in time series data (e.g., quantification of diseases-related anomalous points in ECG and abnormal detection in signal). To address this challenge, we formally discuss and reformulate MTSC as a weakly supervised problem, introducing a novel multiple-instance learning (MIL) framework for better localization of patterns of interest and modeling time dependencies within time series. Our novel approach, TimeMIL, formulates the temporal correlation and ordering within a time-aware MIL pooling, leveraging a tokenized transformer with a specialized learnable wavelet positional token. The proposed method surpassed 26 recent state-of-the-art MTSC methods, underscoring the effectiveness of the weakly supervised TimeMIL in MTSC. The code is available https://github.com/xiwenc1/TimeMIL.