---
title: "Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products"
source: "https://proceedings.mlr.press/v235/bar-shalom24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bar-shalom24a/bar-shalom24a.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['subgraph-GNNs', 'graph-transformers', 'graph-products']
venue: "ICML 2024"
tldr: "Subgraphormer unifies subgraph GNNs and graph transformers via graph products to combine expressiveness and attention mechanisms."
---

# Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products

**Source**: [https://proceedings.mlr.press/v235/bar-shalom24a.html](https://proceedings.mlr.press/v235/bar-shalom24a.html)

**TLDR**: Subgraphormer unifies subgraph GNNs and graph transformers via graph products to combine expressiveness and attention mechanisms.

## Abstract

In the realm of Graph Neural Networks (GNNs), two exciting research directions have recently emerged: Subgraph GNNs and Graph Transformers. In this paper, we propose an architecture that integrates both approaches, dubbed Subgraphormer, which combines the enhanced expressive power, message-passing mechanisms, and aggregation schemes from Subgraph GNNs with attention and positional encodings, arguably the most important components in Graph Transformers. Our method is based on an intriguing new connection we reveal between Subgraph GNNs and product graphs, suggesting that Subgraph GNNs can be formulated as Message Passing Neural Networks (MPNNs) operating on a product of the graph with itself. We use this formulation to design our architecture: first, we devise an attention mechanism based on the connectivity of the product graph. Following this, we propose a novel and efficient positional encoding scheme for Subgraph GNNs, which we derive as a positional encoding for the product graph. Our experimental results demonstrate significant performance improvements over both Subgraph GNNs and Graph Transformers on a wide range of datasets.