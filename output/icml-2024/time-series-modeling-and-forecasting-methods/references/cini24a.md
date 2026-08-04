---
title: "Graph-based Time Series Clustering for End-to-End Hierarchical Forecasting"
source: "https://proceedings.mlr.press/v235/cini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cini24a/cini24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'graph-neural-networks-and-topology']
tags: ['hierarchical-forecasting', 'time-series-clustering', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "A graph-based time series clustering method is proposed to learn hierarchical structures end-to-end for improved hierarchical forecasting."
---

# Graph-based Time Series Clustering for End-to-End Hierarchical Forecasting

**Source**: [https://proceedings.mlr.press/v235/cini24a.html](https://proceedings.mlr.press/v235/cini24a.html)

**TLDR**: A graph-based time series clustering method is proposed to learn hierarchical structures end-to-end for improved hierarchical forecasting.

## Abstract

Relationships among time series can be exploited as inductive biases in learning effective forecasting models. In hierarchical time series, relationships among subsets of sequences induce hard constraints (hierarchical inductive biases) on the predicted values. In this paper, we propose a graph-based methodology to unify relational and hierarchical inductive biases in the context of deep learning for time series forecasting. In particular, we model both types of relationships as dependencies in a pyramidal graph structure, with each pyramidal layer corresponding to a level of the hierarchy. By exploiting modern - trainable - graph pooling operators we show that the hierarchical structure, if not available as a prior, can be learned directly from data, thus obtaining cluster assignments aligned with the forecasting objective. A differentiable reconciliation stage is incorporated into the processing architecture, allowing hierarchical constraints to act both as an architectural bias as well as a regularization element for predictions. Simulation results on representative datasets show that the proposed method compares favorably against the state of the art.