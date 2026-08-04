---
title: "Faster Streaming and Scalable Algorithms for Finding Directed Dense Subgraphs in Large Graphs"
source: "https://proceedings.mlr.press/v235/mitrovic24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mitrovic24a/mitrovic24a.pdf"
categories: ['graph-based-community-structure-detection', 'dynamic-algorithms-and-complexity-theory']
tags: ['dense-subgraph', 'streaming-algorithms', 'approximation']
venue: "ICML 2024"
tldr: "Presents faster streaming and scalable algorithms achieving (2+ε)-approximation for finding directed densest subgraphs in large graphs."
---

# Faster Streaming and Scalable Algorithms for Finding Directed Dense Subgraphs in Large Graphs

**Source**: [https://proceedings.mlr.press/v235/mitrovic24a.html](https://proceedings.mlr.press/v235/mitrovic24a.html)

**TLDR**: Presents faster streaming and scalable algorithms achieving (2+ε)-approximation for finding directed densest subgraphs in large graphs.

## Abstract

Finding dense subgraphs is a fundamental algorithmic tool in data mining, community detection, and clustering. In this problem, the aim is to find an induced subgraph whose edge-to-vertex ratio is maximized. We show how to find a $(2+\epsilon)$ approximation of the directed densest subgraph on randomized streams in a single pass while using $O(n \cdot {\rm poly} \log n)$ memory on $n$-vertex graphs. In contrast, the approach by Bahmani et al. (VLDB 2012) uses $O(\log n)$ passes and by Esfandiari et al. (2015) makes one pass but uses $O(n^{3/2})$ memory; both algorithms also apply to arbitrary-ordered streams. Our techniques extend to Massively Parallel Computation (MPC), yielding quadratic improvement over state-of-the-art by Bahmani et al. (VLDB 2012 and WAW 2014). We empirically show that the quality of our output is essentially the same as that of Bahmani et al. (VLDB 2012) while being $2$ times faster on large graphs, even on non-randomly ordered streams.