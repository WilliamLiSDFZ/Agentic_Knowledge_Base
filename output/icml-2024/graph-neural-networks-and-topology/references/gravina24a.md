---
title: "Long Range Propagation on Continuous-Time Dynamic Graphs"
source: "https://proceedings.mlr.press/v235/gravina24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gravina24a/gravina24a.pdf"
categories: ['graph-neural-networks-and-topology', 'time-series-modeling-and-forecasting-methods']
tags: ['continuous-time-dynamic-graphs', 'long-range-propagation', 'temporal-graph-learning']
venue: "ICML 2024"
tldr: "This paper addresses long-range dependency limitations in continuous-time dynamic graph learning by proposing improved propagation mechanisms."
---

# Long Range Propagation on Continuous-Time Dynamic Graphs

**Source**: [https://proceedings.mlr.press/v235/gravina24a.html](https://proceedings.mlr.press/v235/gravina24a.html)

**TLDR**: This paper addresses long-range dependency limitations in continuous-time dynamic graph learning by proposing improved propagation mechanisms.

## Abstract

Learning Continuous-Time Dynamic Graphs (C-TDGs) requires accurately modeling spatio-temporal information on streams of irregularly sampled events. While many methods have been proposed recently, we find that most message passing-, recurrent- or self-attention-based methods perform poorly on long-range tasks. These tasks require correlating information that occurred "far" away from the current event, either spatially (higher-order node information) or along the time dimension (events occurred in the past). To address long-range dependencies, we introduce Continuous-Time Graph Anti-Symmetric Network (CTAN). Grounded within the ordinary differential equations framework, our method is designed for efficient propagation of information. In this paper, we show how CTAN’s (i) long-range modeling capabilities are substantiated by theoretical findings and how (ii) its empirical performance on synthetic long-range benchmarks and real-world benchmarks is superior to other methods. Our results motivate CTAN’s ability to propagate long-range information in C-TDGs as well as the inclusion of long-range tasks as part of temporal graph models evaluation.