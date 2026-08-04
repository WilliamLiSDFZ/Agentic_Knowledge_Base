---
title: "LSEnet: Lorentz Structural Entropy Neural Network for Deep Graph Clustering"
source: "https://proceedings.mlr.press/v235/sun24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24g/sun24g.pdf"
categories: ['graph-based-community-structure-detection', 'topological-deep-learning-persistent-homology']
tags: ['graph-clustering', 'hyperbolic-geometry', 'structural-entropy', 'deep-learning', 'unknown-cluster-number']
venue: "ICML 2024"
tldr: "LSEnet uses Lorentz structural entropy in a neural network framework to perform deep graph clustering without requiring a predefined number of clusters."
---

# LSEnet: Lorentz Structural Entropy Neural Network for Deep Graph Clustering

**Source**: [https://proceedings.mlr.press/v235/sun24g.html](https://proceedings.mlr.press/v235/sun24g.html)

**TLDR**: LSEnet uses Lorentz structural entropy in a neural network framework to perform deep graph clustering without requiring a predefined number of clusters.

## Abstract

Graph clustering is a fundamental problem in machine learning. Deep learning methods achieve the state-of-the-art results in recent years, but they still cannot work without predefined cluster numbers. Such limitation motivates us to pose a more challenging problem of graph clustering with unknown cluster number. We propose to address this problem from a fresh perspective of graph information theory (i.e., structural information). In the literature, structural information has not yet been introduced to deep clustering, and its classic definition falls short of discrete formulation and modeling node features. In this work, we first formulate a differentiable structural information (DSI) in the continuous realm, accompanied by several theoretical results. By minimizing DSI, we construct the optimal partitioning tree where densely connected nodes in the graph tend to have the same assignment, revealing the cluster struc- ture. DSI is also theoretically presented as a new graph clustering objective, not requiring the pre-defined cluster number. Furthermore, we design a neural LSEnet in the Lorentz model of hyperbolic space, where we integrate node features to structural information via manifold-valued graph convolution. Extensive empirical results on real graphs show the superiority of our approach.