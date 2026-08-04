---
title: "PANDA: Expanded Width-Aware Message Passing Beyond Rewiring"
source: "https://proceedings.mlr.press/v235/choi24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24f/choi24f.pdf"
categories: ['graph-neural-networks-and-topology', 'topological-deep-learning-persistent-homology']
tags: ['graph-neural-networks', 'over-squashing', 'message-passing']
venue: "ICML 2024"
tldr: "PANDA addresses over-squashing in GNNs by expanding node width in message passing without requiring graph rewiring."
---

# PANDA: Expanded Width-Aware Message Passing Beyond Rewiring

**Source**: [https://proceedings.mlr.press/v235/choi24f.html](https://proceedings.mlr.press/v235/choi24f.html)

**TLDR**: PANDA addresses over-squashing in GNNs by expanding node width in message passing without requiring graph rewiring.

## Abstract

Recent research in the field of graph neural network (GNN) has identified a critical issue known as "over-squashing," resulting from the bottleneck phenomenon in graph structures, which impedes the propagation of long-range information. Prior works have proposed a variety of graph rewiring concepts that aim at optimizing the spatial or spectral properties of graphs to promote the signal propagation. However, such approaches inevitably deteriorate the original graph topology, which may lead to a distortion of information flow. To address this, we introduce an expanded width-aware (PANDA) message passing, a new message passing paradigm where nodes with high centrality, a potential source of over-squashing, are selectively expanded in width to encapsulate the growing influx of signals from distant nodes. Experimental results show that our method outperforms existing rewiring methods, suggesting that selectively expanding the hidden state of nodes can be a compelling alternative to graph rewiring for addressing the over-squashing.