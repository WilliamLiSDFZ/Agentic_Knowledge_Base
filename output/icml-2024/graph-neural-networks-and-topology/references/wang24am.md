---
title: "Graph As Point Set"
source: "https://proceedings.mlr.press/v235/wang24am.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24am/wang24am.pdf"
categories: ['graph-neural-networks-and-topology', 'sampling-compression-and-dimensionality-reduction']
tags: ['graph-neural-networks', 'point-set-representation', 'set-based-learning', 'graph-representation']
venue: "ICML 2024"
tldr: "Graphs are represented as point sets enabling the use of set-based neural architectures as an alternative to message-passing GNNs."
---

# Graph As Point Set

**Source**: [https://proceedings.mlr.press/v235/wang24am.html](https://proceedings.mlr.press/v235/wang24am.html)

**TLDR**: Graphs are represented as point sets enabling the use of set-based neural architectures as an alternative to message-passing GNNs.

## Abstract

Graph is a fundamental data structure to model interconnections between entities. Set, on the contrary, stores independent elements. To learn graph representations, current Graph Neural Networks (GNNs) primarily use message passing to encode the interconnections. In contrast, this paper introduces a novel graph-to-set conversion method that bijectively transforms interconnected nodes into a set of independent points and then uses a set encoder to learn the graph representation. This conversion method holds dual significance. Firstly, it enables using set encoders to learn from graphs, thereby significantly expanding the design space of GNNs. Secondly, for Transformer, a specific set encoder, we provide a novel and principled approach to inject graph information losslessly, different from all the heuristic structural/positional encoding methods adopted in previous graph transformers. To demonstrate the effectiveness of our approach, we introduce Point Set Transformer (PST), a transformer architecture that accepts a point set converted from a graph as input. Theoretically, PST exhibits superior expressivity for both short-range substructure counting and long-range shortest path distance tasks compared to existing GNNs. Extensive experiments further validate PST’s outstanding real-world performance. Besides Transformer, we also devise a Deepset-based set encoder, which achieves performance comparable to representative GNNs, affirming the versatility of our graph-to-set method.