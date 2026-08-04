---
title: "Community-Invariant Graph Contrastive Learning"
source: "https://proceedings.mlr.press/v235/tan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24b/tan24b.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-contrastive-learning', 'community-structure', 'augmentation']
venue: "ICML 2024"
tldr: "Community-Invariant Graph Contrastive Learning uses community-preserving augmentation to improve generalization of graph representations."
---

# Community-Invariant Graph Contrastive Learning

**Source**: [https://proceedings.mlr.press/v235/tan24b.html](https://proceedings.mlr.press/v235/tan24b.html)

**TLDR**: Community-Invariant Graph Contrastive Learning uses community-preserving augmentation to improve generalization of graph representations.

## Abstract

Graph augmentation has received great attention in recent years for graph contrastive learning (GCL) to learn well-generalized node/graph representations. However, mainstream GCL methods often favor randomly disrupting graphs for augmentation, which shows limited generalization and inevitably leads to the corruption of high-level graph information, i.e., the graph community. Moreover, current knowledge-based graph augmentation methods can only focus on either topology or node features, causing the model to lack robustness against various types of noise. To address these limitations, this research investigated the role of the graph community in graph augmentation and figured out its crucial advantage for learnable graph augmentation. Based on our observations, we propose a community-invariant GCL framework to maintain graph community structure during learnable graph augmentation. By maximizing the spectral changes, this framework unifies the constraints of both topology and feature augmentation, enhancing the model’s robustness. Empirical evidence on 21 benchmark datasets demonstrates the exclusive merits of our framework. Code is released on Github (https://github.com/ShiyinTan/CI-GCL.git).