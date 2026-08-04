---
title: "Delaunay Graph: Addressing Over-Squashing and Over-Smoothing Using Delaunay Triangulation"
source: "https://proceedings.mlr.press/v235/attali24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/attali24a/attali24a.pdf"
categories: ['graph-neural-networks-and-topology', 'topological-deep-learning-persistent-homology']
tags: ['graph-neural-networks', 'over-squashing', 'over-smoothing', 'Delaunay-triangulation', 'message-passing']
venue: "ICML 2024"
tldr: "Proposes using Delaunay triangulation to construct graph topologies that alleviate over-squashing and over-smoothing in GNNs."
---

# Delaunay Graph: Addressing Over-Squashing and Over-Smoothing Using Delaunay Triangulation

**Source**: [https://proceedings.mlr.press/v235/attali24a.html](https://proceedings.mlr.press/v235/attali24a.html)

**TLDR**: Proposes using Delaunay triangulation to construct graph topologies that alleviate over-squashing and over-smoothing in GNNs.

## Abstract

GNNs rely on the exchange of messages to distribute information along the edges of the graph. This approach makes the efficiency of architectures highly dependent on the specific structure of the input graph. Certain graph topologies lead to inefficient information propagation, resulting in a phenomenon known as over-squashing. While the majority of existing methods address over-squashing by rewiring the input graph, our novel approach involves constructing a graph directly from features using Delaunay Triangulation. We posit that the topological properties of the resulting graph prove advantageous for mitigate oversmoothing and over-squashing. Our extensive experimentation demonstrates that our method consistently outperforms established graph rewiring methods.