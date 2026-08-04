---
title: "SLOG: An Inductive Spectral Graph Neural Network Beyond Polynomial Filter"
source: "https://proceedings.mlr.press/v235/xu24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24aa/xu24aa.pdf"
categories: ['graph-neural-networks-and-topology', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['spectral-GNN', 'inductive-learning', 'graph-filters']
venue: "ICML 2024"
tldr: "Proposes SLOG, an inductive spectral GNN that goes beyond polynomial filters to capture both local and global graph frequency signals."
---

# SLOG: An Inductive Spectral Graph Neural Network Beyond Polynomial Filter

**Source**: [https://proceedings.mlr.press/v235/xu24aa.html](https://proceedings.mlr.press/v235/xu24aa.html)

**TLDR**: Proposes SLOG, an inductive spectral GNN that goes beyond polynomial filters to capture both local and global graph frequency signals.

## Abstract

Graph neural networks (GNNs) have exhibited superb power in many graph related tasks. Existing GNNs can be categorized into spatial GNNs and spectral GNNs. The spatial GNNs primarily capture the local information around each node, while the spectral GNNs are able to operate on the frequency signals of the entire graph. However, most, if not all, existing spectral GNNs are faced with two limitations: (1) the polynomial limitation that for most spectral GNNs, the expressive power in the spectral domain is limited to polynomial filters; and (2) the transductive limitation that most spectral GNNs can only be applied to the transductive setting on relatively small-scale graphs. In this paper, we propose a novel spectral graph neural network named SLOG to solve the above two limitations. For the polynomial limitation, SLOG proposes a novel real-valued filter with geometric interpretability, mathematical feasibility and adaptive filtering ability to go beyond polynomial. For the transductive limitation, SLOG combines the subgraph sampling technique in spatial GNNs and the signal processing technique in spectral GNNs together to make itself tailored to the inductive setting on large-scale graphs. Extensive experimental results on 16 datasets demonstrate the superiority of SLOG in inductive homophilic and heterophilic node classification task.