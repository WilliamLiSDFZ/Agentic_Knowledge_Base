---
title: "Understanding Heterophily for Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/wang24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24u/wang24u.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['graph-neural-networks', 'heterophily', 'graph-convolution', 'theoretical-analysis', 'node-classification']
venue: "ICML 2024"
tldr: "This paper provides theoretical understanding of heterophily in GNNs by analyzing graph convolution under various heterophily patterns."
---

# Understanding Heterophily for Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/wang24u.html](https://proceedings.mlr.press/v235/wang24u.html)

**TLDR**: This paper provides theoretical understanding of heterophily in GNNs by analyzing graph convolution under various heterophily patterns.

## Abstract

Graphs with heterophily have been regarded as challenging scenarios for Graph Neural Networks (GNNs), where nodes are connected with dissimilar neighbors through various patterns. In this paper, we present theoretical understandings of heterophily for GNNs by incorporating the graph convolution (GC) operations into fully connected networks via the proposed Heterophilous Stochastic Block Models (HSBM), a general random graph model that can accommodate diverse heterophily patterns. Our theoretical investigation comprehensively analyze the impact of heterophily from three critical aspects. Firstly, for the impact of different heterophily patterns, we show that the separability gains are determined by two factors, i.e., the Euclidean distance of the neighborhood distributions and $\sqrt{\mathbb{E}\left[\operatorname{deg}\right]}$, where $\mathbb{E}\left[\operatorname{deg}\right]$ is the averaged node degree. Secondly, we show that the neighborhood inconsistency has a detrimental impact on separability, which is similar to degrading $\mathbb{E}\left[\operatorname{deg}\right]$ by a specific factor. Finally, for the impact of stacking multiple layers, we show that the separability gains are determined by the normalized distance of the $l$-powered neighborhood distributions, indicating that nodes still possess separability in various regimes, even when over-smoothing occurs. Extensive experiments on both synthetic and real-world data verify the effectiveness of our theory.