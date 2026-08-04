---
title: "Translating Subgraphs to Nodes Makes Simple GNNs Strong and Efficient for Subgraph Representation Learning"
source: "https://proceedings.mlr.press/v235/kim24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24aa/kim24aa.pdf"
categories: ['graph-neural-networks-and-topology', 'sampling-compression-and-dimensionality-reduction']
tags: ['subgraph-representation-learning', 'GNN', 'node-compression']
venue: "ICML 2024"
tldr: "Translates subgraph structures into node representations to enable simple GNNs to efficiently perform subgraph representation learning."
---

# Translating Subgraphs to Nodes Makes Simple GNNs Strong and Efficient for Subgraph Representation Learning

**Source**: [https://proceedings.mlr.press/v235/kim24aa.html](https://proceedings.mlr.press/v235/kim24aa.html)

**TLDR**: Translates subgraph structures into node representations to enable simple GNNs to efficiently perform subgraph representation learning.

## Abstract

Subgraph representation learning has emerged as an important problem, but it is by default approached with specialized graph neural networks on a large global graph. These models demand extensive memory and computational resources but challenge modeling hierarchical structures of subgraphs. In this paper, we propose Subgraph-To-Node (S2N) translation, a novel formulation for learning representations of subgraphs. Specifically, given a set of subgraphs in the global graph, we construct a new graph by coarsely transforming subgraphs into nodes. Demonstrating both theoretical and empirical evidence, S2N not only significantly reduces memory and computational costs compared to state-of-the-art models but also outperforms them by capturing both local and global structures of the subgraph. By leveraging graph coarsening methods, our method outperforms baselines even in a data-scarce setting with insufficient subgraphs. Our experiments on eight benchmarks demonstrate that fined-tuned models with S2N translation can process 183 – 711 times more subgraph samples than state-of-the-art models at a better or similar performance level.