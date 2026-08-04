---
title: "Probabilistic Routing for Graph-Based Approximate Nearest Neighbor Search"
source: "https://proceedings.mlr.press/v235/lu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24l/lu24l.pdf"
categories: ['graph-based-approximate-nearest-neighbor-search']
tags: ['approximate-nearest-neighbor', 'graph-based-search', 'probabilistic-routing', 'high-dimensional']
venue: "ICML 2024"
tldr: "Introduces probabilistic routing strategies for graph-based approximate nearest neighbor search to improve efficiency and accuracy."
---

# Probabilistic Routing for Graph-Based Approximate Nearest Neighbor Search

**Source**: [https://proceedings.mlr.press/v235/lu24l.html](https://proceedings.mlr.press/v235/lu24l.html)

**TLDR**: Introduces probabilistic routing strategies for graph-based approximate nearest neighbor search to improve efficiency and accuracy.

## Abstract

Approximate nearest neighbor search (ANNS) in high-dimensional spaces is a pivotal challenge in the field of machine learning. In recent years graph-based methods have emerged as the superior approach to ANNS, establishing a new state of the art. Although various optimizations for graph-based ANNS have been introduced, they predominantly rely on heuristic methods that lack formal theoretical backing. This paper aims to enhance routing within graph-based ANNS by introducing a method that offers a probabilistic guarantee when exploring a node’s neighbors in the graph. We formulate the problem as probabilistic routing and develop two baseline strategies by incorporating locality-sensitive techniques. Subsequently, we introduce PEOs, a novel approach that efficiently identifies which neighbors in the graph should be considered for exact distance computation, thus significantly improving efficiency in practice. Our experiments demonstrate that equipping PEOs can increase throughput on a commonly utilized graph index (HNSW) by a factor of 1.6 to 2.5, and its efficiency consistently outperforms the leading-edge routing technique by 1.1 to 1.4 times. The code and datasets used for our evaluations are publicly accessible at https//github.com/ICML2024-code/PEOs .