---
title: "SAMformer: Unlocking the Potential of Transformers in Time Series Forecasting with Sharpness-Aware Minimization and Channel-Wise Attention"
source: "https://proceedings.mlr.press/v235/ilbert24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ilbert24a/ilbert24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'time-series-modeling-and-forecasting-methods']
tags: ['transformer', 'time-series-forecasting', 'sharpness-aware-minimization', 'channel-wise-attention', 'linear-baselines']
venue: "ICML 2024"
tldr: "SAMformer applies sharpness-aware minimization and channel-wise attention to close the gap between transformers and linear baselines in multivariate long-term forecasting."
---

# SAMformer: Unlocking the Potential of Transformers in Time Series Forecasting with Sharpness-Aware Minimization and Channel-Wise Attention

**Source**: [https://proceedings.mlr.press/v235/ilbert24a.html](https://proceedings.mlr.press/v235/ilbert24a.html)

**TLDR**: SAMformer applies sharpness-aware minimization and channel-wise attention to close the gap between transformers and linear baselines in multivariate long-term forecasting.

## Abstract

Transformer-based architectures achieved breakthrough performance in natural language processing and computer vision, yet they remain inferior to simpler linear baselines in multivariate long-term forecasting. To better understand this phenomenon, we start by studying a toy linear forecasting problem for which we show that transformers are incapable of converging to their true solution despite their high expressive power. We further identify the attention of transformers as being responsible for this low generalization capacity. Building upon this insight, we propose a shallow lightweight transformer model that successfully escapes bad local minima when optimized with sharpness-aware optimization. We empirically demonstrate that this result extends to all commonly used real-world multivariate time series datasets. In particular, SAMformer surpasses current state-of-the-art methods and is on par with the biggest foundation model MOIRAI while having significantly fewer parameters. The code is available at https://github.com/romilbert/samformer.