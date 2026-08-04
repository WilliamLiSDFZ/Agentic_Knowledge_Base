---
title: "Convergence Guarantees for the DeepWalk Embedding on Block Models"
source: "https://proceedings.mlr.press/v235/harker24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/harker24a/harker24a.pdf"
categories: ['graph-neural-networks-and-topology', 'graph-clustering-and-matching-algorithms']
tags: ['graph-embeddings', 'deepwalk', 'block-models']
venue: "ICML 2024"
tldr: "Convergence guarantees are established for the DeepWalk embedding algorithm on stochastic block models, analyzing its nonlinear optimization on graph structure."
---

# Convergence Guarantees for the DeepWalk Embedding on Block Models

**Source**: [https://proceedings.mlr.press/v235/harker24a.html](https://proceedings.mlr.press/v235/harker24a.html)

**TLDR**: Convergence guarantees are established for the DeepWalk embedding algorithm on stochastic block models, analyzing its nonlinear optimization on graph structure.

## Abstract

Graph embeddings have emerged as a powerful tool for understanding the structure of graphs. Unlike classical spectral methods, recent methods such as DeepWalk, Node2Vec, etc. are based on solving nonlinear optimization problems on the graph, using local information obtained by performing random walks. These techniques have empirically been shown to produce “better” embeddings than their classical counterparts. However, due to their reliance on solving a nonconvex optimization problem, obtaining theoretical guarantees on the properties of the solution has remained a challenge, even for simple classes of graphs. In this work, we show convergence properties for the DeepWalk algorithm on graphs obtained from the Stochastic Block Model (SBM). Despite being simplistic, the SBM has proved to be a classic model for analyzing the behavior of algorithms on large graphs. Our results mirror the existing ones for spectral embeddings on SBMs, showing that even in the case of one-dimensional embeddings, the output of the DeepWalk algorithm provably recovers the cluster structure with high probability.