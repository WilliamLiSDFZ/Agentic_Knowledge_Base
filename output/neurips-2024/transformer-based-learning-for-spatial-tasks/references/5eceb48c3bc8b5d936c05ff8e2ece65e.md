---
title: "Graph Convolutions Enrich the Self-Attention in Transformers!"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5eceb48c3bc8b5d936c05ff8e2ece65e-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'transformer-based-learning-for-spatial-tasks']
tags: ['graph-convolution', 'transformer', 'oversmoothing']
venue: "NeurIPS 2024"
tldr: "Proposes enriching transformer self-attention with graph convolutions to mitigate oversmoothing and improve representation expressiveness in deep models."
---

# Graph Convolutions Enrich the Self-Attention in Transformers!

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5eceb48c3bc8b5d936c05ff8e2ece65e-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5eceb48c3bc8b5d936c05ff8e2ece65e-Abstract-Conference.html)

**TLDR**: Proposes enriching transformer self-attention with graph convolutions to mitigate oversmoothing and improve representation expressiveness in deep models.

## Abstract

Transformers, renowned for their self-attention mechanism, have achieved state-of-the-art performance across various tasks in natural language processing, computer vision, time-series modeling, etc. However, one of the challenges with deep Transformer models is the oversmoothing problem, where representations across layers converge to indistinguishable values, leading to significant performance degradation. We interpret the original self-attention as a simple graph filter and redesign it from a graph signal processing (GSP) perspective. We propose a graph-filter-based self-attention (GFSA) to learn a general yet effective one, whose complexity, however, is slightly larger than that of the original self-attention mechanism. We demonstrate that GFSA improves the performance of Transformers in various fields, including computer vision, natural language processing, graph-level tasks, speech recognition, and code classification.