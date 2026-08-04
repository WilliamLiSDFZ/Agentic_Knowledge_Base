---
title: "Learning Optimal Projection for Forecast Reconciliation of Hierarchical Time Series"
source: "https://proceedings.mlr.press/v235/tsiourvas24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tsiourvas24b/tsiourvas24b.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'optimization-algorithms-convergence-theory']
tags: ['hierarchical-forecasting', 'forecast-reconciliation', 'optimal-projection']
venue: "ICML 2024"
tldr: "Learns optimal projection matrices for hierarchical time series forecast reconciliation to ensure coherency and accuracy."
---

# Learning Optimal Projection for Forecast Reconciliation of Hierarchical Time Series

**Source**: [https://proceedings.mlr.press/v235/tsiourvas24b.html](https://proceedings.mlr.press/v235/tsiourvas24b.html)

**TLDR**: Learns optimal projection matrices for hierarchical time series forecast reconciliation to ensure coherency and accuracy.

## Abstract

Hierarchical time series forecasting requires not only prediction accuracy but also coherency, i.e., forecasts add up appropriately across the hierarchy. Recent literature has shown that reconciliation via projection outperforms prior methods such as top-down or bottom-up approaches. Unlike existing work that pre-specifies a projection matrix (e.g., orthogonal), we study the problem of learning the optimal oblique projection from data for coherent forecasting of hierarchical time series. In addition to the unbiasedness-preserving property, oblique projection implicitly accounts for the hierarchy structure and assigns different weights to individual time series, providing significant adaptability over orthogonal projection which treats base forecast errors equally. We examine two broad classes of projections, namely Euclidean projection and general oblique projections. We propose to model the reconciliation step as a learnable, structured, projection layer in the neural forecaster architecture. The proposed approach allows for the efficient learning of the optimal projection in an end-to-end framework where both the neural forecaster and the projection layer are learned simultaneously. An empirical evaluation of real-world hierarchical time series datasets demonstrates the superior performance of the proposed method over existing state-of-the-art approaches.