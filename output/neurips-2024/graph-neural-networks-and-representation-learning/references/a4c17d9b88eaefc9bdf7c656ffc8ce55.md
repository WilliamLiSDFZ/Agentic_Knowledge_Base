---
title: "GRANOLA: Adaptive Normalization for Graph Neural Networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a4c17d9b88eaefc9bdf7c656ffc8ce55-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'deep-learning-optimization-and-generalization-theory']
tags: ['graph-neural-networks', 'normalization', 'adaptive-normalization', 'batch-normalization', 'graph-statistics']
venue: "NeurIPS 2024"
tldr: "GRANOLA introduces an adaptive normalization layer specifically designed for GNNs that captures graph-specific structural characteristics."
---

# GRANOLA: Adaptive Normalization for Graph Neural Networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a4c17d9b88eaefc9bdf7c656ffc8ce55-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a4c17d9b88eaefc9bdf7c656ffc8ce55-Abstract-Conference.html)

**TLDR**: GRANOLA introduces an adaptive normalization layer specifically designed for GNNs that captures graph-specific structural characteristics.

## Abstract

Despite the widespread adoption of Graph Neural Networks (GNNs), these models often incorporate off-the-shelf normalization layers like BatchNorm or InstanceNorm, which were not originally designed for GNNs. Consequently, these normalization layers may not effectively capture the unique characteristics of graph-structured data, potentially even weakening the expressive power of the overall architecture. While existing graph-specific normalization layers have been proposed, they often struggle to offer substantial and consistent benefits. In this paper, we propose GRANOLA, a novel graph-adaptive normalization layer. Unlike existing normalization layers, GRANOLA normalizes node features by adapting to the specific characteristics of the graph, particularly by generating expressive representations of its nodes, obtained by leveraging the propagation of Random Node Features (RNF) in the graph. We provide theoretical results that support our design choices as well as an extensive empirical evaluation demonstrating the superior performance of GRANOLA over existing normalization techniques. Furthermore, GRANOLA emerges as the top-performing method among all baselines in the same time complexity class of Message Passing Neural Networks (MPNNs).