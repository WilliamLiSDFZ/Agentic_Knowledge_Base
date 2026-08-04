---
title: "Graph-based Forecasting with Missing Data through Spatiotemporal Downsampling"
source: "https://proceedings.mlr.press/v235/marisca24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/marisca24a/marisca24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['spatiotemporal-forecasting', 'graph-neural-networks', 'missing-data']
venue: "ICML 2024"
tldr: "A graph-based spatiotemporal forecasting method that handles missing sensor data through spatiotemporal downsampling."
---

# Graph-based Forecasting with Missing Data through Spatiotemporal Downsampling

**Source**: [https://proceedings.mlr.press/v235/marisca24a.html](https://proceedings.mlr.press/v235/marisca24a.html)

**TLDR**: A graph-based spatiotemporal forecasting method that handles missing sensor data through spatiotemporal downsampling.

## Abstract

Given a set of synchronous time series, each associated with a sensor-point in space and characterized by inter-series relationships, the problem of spatiotemporal forecasting consists of predicting future observations for each point. Spatiotemporal graph neural networks achieve striking results by representing the relationships across time series as a graph. Nonetheless, most existing methods rely on the often unrealistic assumption that inputs are always available and fail to capture hidden spatiotemporal dynamics when part of the data is missing. In this work, we tackle this problem through hierarchical spatiotemporal downsampling. The input time series are progressively coarsened over time and space, obtaining a pool of representations that capture heterogeneous temporal and spatial dynamics. Conditioned on observations and missing data patterns, such representations are combined by an interpretable attention mechanism to generate the forecasts. Our approach outperforms state-of-the-art methods on synthetic and real-world benchmarks under different missing data distributions, particularly in the presence of contiguous blocks of missing values.