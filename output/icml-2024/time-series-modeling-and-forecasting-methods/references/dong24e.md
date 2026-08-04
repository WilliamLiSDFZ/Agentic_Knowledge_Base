---
title: "TimeSiam: A Pre-Training Framework for Siamese Time-Series Modeling"
source: "https://proceedings.mlr.press/v235/dong24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dong24e/dong24e.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['time-series', 'pre-training', 'siamese-networks', 'self-supervised-learning']
venue: "ICML 2024"
tldr: "TimeSiam is a Siamese-based pre-training framework for time series that captures temporal dependencies without relying on vision or language pre-training paradigms."
---

# TimeSiam: A Pre-Training Framework for Siamese Time-Series Modeling

**Source**: [https://proceedings.mlr.press/v235/dong24e.html](https://proceedings.mlr.press/v235/dong24e.html)

**TLDR**: TimeSiam is a Siamese-based pre-training framework for time series that captures temporal dependencies without relying on vision or language pre-training paradigms.

## Abstract

Time series pre-training has recently garnered wide attention for its potential to reduce labeling expenses and benefit various downstream tasks. Prior methods are mainly based on pre-training techniques well-acknowledged in vision or language, such as masked modeling and contrastive learning. However, randomly masking time series or calculating series-wise similarity will distort or neglect inherent temporal correlations crucial in time series data. To emphasize temporal correlation modeling, this paper proposes TimeSiam as a simple but effective self-supervised pre-training framework for Time series based on Siamese networks. Concretely, TimeSiam pre-trains Siamese encoders to capture intrinsic temporal correlations between randomly sampled past and current subseries. With a simple data augmentation method (e.g. masking), TimeSiam can benefit from diverse augmented subseries and learn internal time-dependent representations through a past-to-current reconstruction. Moreover, learnable lineage embeddings are also introduced to distinguish temporal distance between sampled series and further foster the learning of diverse temporal correlations. TimeSiam consistently outperforms extensive advanced pre-training baselines, demonstrating superior forecasting and classification capabilities across 13 standard benchmarks in both intra- and cross-domain scenarios.