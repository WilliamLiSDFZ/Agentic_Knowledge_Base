---
title: "From Coarse to Fine: Enable Comprehensive Graph Self-supervised Learning with Multi-granular Semantic Ensemble"
source: "https://proceedings.mlr.press/v235/wen24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wen24e/wen24e.pdf"
categories: ['graph-neural-networks-and-topology', 'clustering-methods-and-multi-view-learning']
tags: ['graph-self-supervised-learning', 'multi-granular-semantics', 'pre-training', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "A multi-granular semantic ensemble framework enhances graph self-supervised learning by capturing structural information at multiple levels of granularity."
---

# From Coarse to Fine: Enable Comprehensive Graph Self-supervised Learning with Multi-granular Semantic Ensemble

**Source**: [https://proceedings.mlr.press/v235/wen24e.html](https://proceedings.mlr.press/v235/wen24e.html)

**TLDR**: A multi-granular semantic ensemble framework enhances graph self-supervised learning by capturing structural information at multiple levels of granularity.

## Abstract

Self-supervised learning (SSL) has gained increasing attention in the graph learning community, owing to its capability of enabling powerful models pre-trained on large unlabeled graphs for general purposes, facilitating quick adaptation to specific domains. Though promising, existing graph SSL frameworks often struggle to capture both high-level abstract features and fine-grained features simultaneously, leading to sub-optimal generalization abilities across different downstream tasks. To bridge this gap, we present Multi-granularity Graph Semantic Ensemble via Knowledge Distillation, namely MGSE, a plug-and-play graph knowledge distillation framework that can be applied to any existing graph SSL framework to enhance its performance by incorporating the concept of multi-granularity. Specifically, MGSE captures multi-granular knowledge by employing multiple student models to learn from a single teacher model, conditioned by probability distributions with different granularities. We apply it to six state-of-the-art graph SSL frameworks and evaluate their performances over multiple graph datasets across different domains, the experimental results show that MGSE can consistently boost the performance of these existing graph SSL frameworks with up to 9.2% improvement.