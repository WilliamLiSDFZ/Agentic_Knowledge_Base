---
title: "What Improves the Generalization of Graph Transformers? A Theoretical Dive into the Self-attention and Positional Encoding"
source: "https://proceedings.mlr.press/v235/li24bo.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bo/li24bo.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['graph-transformers', 'self-attention', 'positional-encoding', 'generalization']
venue: "ICML 2024"
tldr: "Provides theoretical analysis of how self-attention and positional encoding contribute to the generalization of graph transformers."
---

# What Improves the Generalization of Graph Transformers? A Theoretical Dive into the Self-attention and Positional Encoding

**Source**: [https://proceedings.mlr.press/v235/li24bo.html](https://proceedings.mlr.press/v235/li24bo.html)

**TLDR**: Provides theoretical analysis of how self-attention and positional encoding contribute to the generalization of graph transformers.

## Abstract

Graph Transformers, which incorporate self-attention and positional encoding, have recently emerged as a powerful architecture for various graph learning tasks. Despite their impressive performance, the complex non-convex interactions across layers and the recursive graph structure have made it challenging to establish a theoretical foundation for learning and generalization. This study introduces the first theoretical investigation of a shallow Graph Transformer for semi-supervised node classification, comprising a self-attention layer with relative positional encoding and a two-layer perception. Focusing on a graph data model with discriminative nodes that determine node labels and non-discriminative nodes that are class-irrelevant, we characterize the sample complexity required to achieve a desirable generalization error by training with stochastic gradient descent (SGD). This paper provides the quantitative characterization of the sample complexity and number of iterations for convergence dependent on the fraction of discriminative nodes, the dominant patterns, and the initial model errors. Furthermore, we demonstrate that self-attention and positional encoding enhance generalization by making the attention map sparse and promoting the core neighborhood during training, which explains the superior feature representation of Graph Transformers. Our theoretical results are supported by empirical experiments on synthetic and real-world benchmarks.