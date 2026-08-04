---
title: "MC-GTA: Metric-Constrained Model-Based Clustering using Goodness-of-fit Tests with Autocorrelations"
source: "https://proceedings.mlr.press/v235/wang24av.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24av/wang24av.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'clustering-methods-and-multi-view-learning']
tags: ['metric-constrained-clustering', 'autocorrelation', 'goodness-of-fit', 'temporal-spatial-data']
venue: "ICML 2024"
tldr: "A metric-constrained clustering method leveraging autocorrelation-based goodness-of-fit tests is proposed for temporal and spatial data."
---

# MC-GTA: Metric-Constrained Model-Based Clustering using Goodness-of-fit Tests with Autocorrelations

**Source**: [https://proceedings.mlr.press/v235/wang24av.html](https://proceedings.mlr.press/v235/wang24av.html)

**TLDR**: A metric-constrained clustering method leveraging autocorrelation-based goodness-of-fit tests is proposed for temporal and spatial data.

## Abstract

A wide range of (multivariate) temporal (1D) and spatial (2D) data analysis tasks, such as grouping vehicle sensor trajectories, can be formulated as clustering with given metric constraints. Existing metric-constrained clustering algorithms overlook the rich correlation between feature similarity and metric distance, i.e., metric autocorrelation. The model-based variations of these clustering algorithms (e.g. TICC and STICC) achieve SOTA performance, yet suffer from computational instability and complexity by using a metric-constrained Expectation-Maximization procedure. In order to address these two problems, we propose a novel clustering algorithm, MC-GTA (Model-based Clustering via Goodness-of-fit Tests with Autocorrelations). Its objective is only composed of pairwise weighted sums of feature similarity terms (square Wasserstein-2 distance) and metric autocorrelation terms (a novel multivariate generalization of classic semivariogram). We show that MC-GTA is effectively minimizing the total hinge loss for intra-cluster observation pairs not passing goodness-of-fit tests, i.e., statistically not originating from the same distribution. Experiments on 1D/2D synthetic and real-world datasets demonstrate that MC-GTA successfully incorporates metric autocorrelation. It outperforms strong baselines by large margins (up to 14.3% in ARI and 32.1% in NMI) with faster and stabler optimization ($>$10x speedup).