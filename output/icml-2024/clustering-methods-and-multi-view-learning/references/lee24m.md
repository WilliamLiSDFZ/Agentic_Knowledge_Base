---
title: "Feature Distribution on Graph Topology Mediates the Effect of Graph Convolution: Homophily Perspective"
source: "https://proceedings.mlr.press/v235/lee24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24m/lee24m.pdf"
categories: ['graph-neural-networks-and-topology', 'clustering-methods-and-multi-view-learning']
tags: ['graph-neural-networks', 'homophily', 'feature-distribution', 'graph-convolution']
venue: "ICML 2024"
tldr: "Analyzes how the alignment between feature distribution and graph topology mediates the effect of graph convolution from a homophily perspective."
---

# Feature Distribution on Graph Topology Mediates the Effect of Graph Convolution: Homophily Perspective

**Source**: [https://proceedings.mlr.press/v235/lee24m.html](https://proceedings.mlr.press/v235/lee24m.html)

**TLDR**: Analyzes how the alignment between feature distribution and graph topology mediates the effect of graph convolution from a homophily perspective.

## Abstract

How would randomly shuffling feature vectors among nodes from the same class affect graph neural networks (GNNs)? The feature shuffle, intuitively, perturbs the dependence between graph topology and features (A-X dependence) for GNNs to learn from. Surprisingly, we observe a consistent and significant improvement in GNN performance following the feature shuffle. Having overlooked the impact of A-X dependence on GNNs, the prior literature does not provide a satisfactory understanding of the phenomenon. Thus, we raise two research questions. First, how should A-X dependence be measured, while controlling for potential confounds? Second, how does A-X dependence affect GNNs? In response, we (i) propose a principled measure for A-X dependence, (ii) design a random graph model that controls A-X dependence, (iii) establish a theory on how A-X dependence relates to graph convolution, and (iv) present empirical analysis on real-world graphs that align with the theory. We conclude that A-X dependence mediates the effect of graph convolution, such that smaller dependence improves GNN-based node classification.