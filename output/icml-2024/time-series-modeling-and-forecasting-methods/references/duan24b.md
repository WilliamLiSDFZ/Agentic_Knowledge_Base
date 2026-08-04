---
title: "MF-CLR: Multi-Frequency Contrastive Learning Representation for Time Series"
source: "https://proceedings.mlr.press/v235/duan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/duan24b/duan24b.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['time-series', 'contrastive-learning', 'multi-frequency', 'representation-learning']
venue: "ICML 2024"
tldr: "MF-CLR learns time series representations by exploiting multi-frequency contrastive learning across channels with different sampling rates."
---

# MF-CLR: Multi-Frequency Contrastive Learning Representation for Time Series

**Source**: [https://proceedings.mlr.press/v235/duan24b.html](https://proceedings.mlr.press/v235/duan24b.html)

**TLDR**: MF-CLR learns time series representations by exploiting multi-frequency contrastive learning across channels with different sampling rates.

## Abstract

Learning a decent representation from unlabeled time series is a challenging task, especially when the time series data is derived from diverse channels at different sampling rates. Our motivation stems from the financial domain, where sparsely labeled covariates are commonly collected at different frequencies, e.g., daily stock market index, monthly unemployment rate and quarterly net revenue of a certain listed corporation. This paper presents Multi-Frequency Contrastive Learning Representation (MF-CLR), aimed at learning a good representation of multi-frequency time series in a self-supervised paradigm by leveraging the ability of contrastive learning. MF-CLR introduces a hierarchical mechanism that spans across different frequencies along the feature dimension. Within each contrastive block, two groups of subseries with adjacent frequencies are embedded based on our proposed cross-frequency consistency. To validate the effectiveness of MF-CLR, we conduct extensive experiments on five downstream tasks, including long-term and short-term forecasting, classification, anomaly detection and imputation. Experimental evidence shows that MF-CLR delivers a leading performance in all the downstream tasks and keeps consistent performance across different target dataset scales in the transfer learning scenario.