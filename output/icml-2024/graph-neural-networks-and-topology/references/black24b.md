---
title: "Comparing Graph Transformers via Positional Encodings"
source: "https://proceedings.mlr.press/v235/black24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/black24b/black24b.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['graph-transformers', 'positional-encodings', 'expressivity', 'WL-test']
venue: "ICML 2024"
tldr: "This paper compares the distinguishing power of graph transformers by analyzing the role of absolute versus relative positional encodings."
---

# Comparing Graph Transformers via Positional Encodings

**Source**: [https://proceedings.mlr.press/v235/black24b.html](https://proceedings.mlr.press/v235/black24b.html)

**TLDR**: This paper compares the distinguishing power of graph transformers by analyzing the role of absolute versus relative positional encodings.

## Abstract

The distinguishing power of graph transformers is tied to the choice of positional encoding: features used to augment the base transformer with information about the graph. There are two primary types of positional encoding: absolute positional encodings (APEs) and relative positional encodings (RPEs). APEs assign features to each node and are given as input to the transformer. RPEs instead assign a feature to each pair of nodes, e.g., shortest-path distance, and are used to augment the attention block. A priori, it is unclear which method is better for maximizing the power of the resulting graph transformer. In this paper, we aim to understand the relationship between these different types of positional encodings. Interestingly, we show that graph transformers using APEs and RPEs are equivalent in their ability to distinguish non-isomorphic graphs. In particular, we demonstrate how to interchange APEs and RPEs while maintaining their distinguishing power in terms of graph transformers. However, in the case of graphs with node features, we show that RPEs may have an advantage over APEs. Based on our theoretical results, we provide a study of different APEs and RPEs—including the shortest-path and resistance distance and the recently introduced stable and expressive positional encoding (SPE)—and compare their distinguishing power in terms of transformers. We believe our work will help navigate the vast number of positional encoding choices and provide guidance on the future design of positional encodings for graph transformers.