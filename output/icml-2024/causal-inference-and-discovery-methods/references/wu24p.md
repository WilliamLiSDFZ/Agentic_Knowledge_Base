---
title: "Learning Causal Relations from Subsampled Time Series with Two Time-Slices"
source: "https://proceedings.mlr.press/v235/wu24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24p/wu24p.pdf"
categories: ['causal-inference-and-discovery-methods', 'time-series-modeling-and-forecasting-methods']
tags: ['causal-discovery', 'subsampled-time-series', 'missing-data', 'temporal-causality', 'time-slices']
venue: "ICML 2024"
tldr: "Studies causal relation discovery from subsampled time series where measurements are sparser than the underlying causal timescale using two time-slice observations."
---

# Learning Causal Relations from Subsampled Time Series with Two Time-Slices

**Source**: [https://proceedings.mlr.press/v235/wu24p.html](https://proceedings.mlr.press/v235/wu24p.html)

**TLDR**: Studies causal relation discovery from subsampled time series where measurements are sparser than the underlying causal timescale using two time-slice observations.

## Abstract

This paper studies the causal relations from subsampled time series, in which measurements are sparse and sampled at a coarser timescale than the causal timescale of the underlying system. In such data, because there are numerous missing time-slices (i.e., cross-sections at each time point) between two consecutive measurements, conventional causal discovery methods designed for standard time series data would produce significant errors. To learn causal relations from subsampled time series, a typical solution is to conduct different interventions and then make a comparison. However, full interventions are often expensive, unethical, or even infeasible, particularly in fields such as health and social science. In this paper, we first explore how readily available two-time-slices data can replace intervention data to improve causal ordering, and propose a novel Descendant Hierarchical Topology algorithm with Conditional Independence Test (DHT-CIT) to learn causal relations from subsampled time series using only two time-slices. Specifically, we develop a conditional independence criterion that can be applied iteratively to test each node from time series and identify all of its descendant nodes. Empirical results on both synthetic and real-world datasets demonstrate the superiority of our DHT-CIT algorithm.