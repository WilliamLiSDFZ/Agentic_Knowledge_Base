---
title: "DUPLEX: Dual GAT for Complex Embedding of Directed Graphs"
source: "https://proceedings.mlr.press/v235/ke24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ke24c/ke24c.pdf"
categories: ['graph-neural-networks-and-topology', 'graph-clustering-and-matching-algorithms']
tags: ['directed-graph-embedding', 'dual-GAT', 'complex-valued-representations']
venue: "ICML 2024"
tldr: "Proposes DUPLEX, a dual graph attention network using complex embeddings to better capture directed edge information in graph representation learning."
---

# DUPLEX: Dual GAT for Complex Embedding of Directed Graphs

**Source**: [https://proceedings.mlr.press/v235/ke24c.html](https://proceedings.mlr.press/v235/ke24c.html)

**TLDR**: Proposes DUPLEX, a dual graph attention network using complex embeddings to better capture directed edge information in graph representation learning.

## Abstract

Current directed graph embedding methods build upon undirected techniques but often inadequately capture directed edge information, leading to challenges such as: (1) Suboptimal representations for nodes with low in/out-degrees, due to the insufficient neighbor interactions; (2) Limited inductive ability for representing new nodes post-training; (3) Narrow generalizability, as training is overly coupled with specific tasks. In response, we propose DUPLEX, an inductive framework for complex embeddings of directed graphs. It (1) leverages Hermitian adjacency matrix decomposition for comprehensive neighbor integration, (2) employs a dual GAT encoder for directional neighbor modeling, and (3) features two parameter-free decoders to decouple training from particular tasks. DUPLEX outperforms state-of-the-art models, especially for nodes with sparse connectivity, and demonstrates robust inductive capability and adaptability across various tasks. The code will be available upon publication.