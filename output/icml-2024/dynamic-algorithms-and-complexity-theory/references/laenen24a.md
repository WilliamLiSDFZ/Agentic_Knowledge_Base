---
title: "Dynamic Spectral Clustering with Provable Approximation Guarantee"
source: "https://proceedings.mlr.press/v235/laenen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/laenen24a/laenen24a.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['dynamic-graphs', 'spectral-clustering', 'approximation-guarantee', 'evolving-graphs']
venue: "ICML 2024"
tldr: "A dynamic spectral clustering algorithm for evolving graphs with provable approximation guarantees as cluster structure gradually changes."
---

# Dynamic Spectral Clustering with Provable Approximation Guarantee

**Source**: [https://proceedings.mlr.press/v235/laenen24a.html](https://proceedings.mlr.press/v235/laenen24a.html)

**TLDR**: A dynamic spectral clustering algorithm for evolving graphs with provable approximation guarantees as cluster structure gradually changes.

## Abstract

This paper studies clustering algorithms for dynamically evolving graphs $\{G_t\}$, in which new edges (and potential new vertices) are added into a graph, and the underlying cluster structure of the graph can gradually change. The paper proves that, under some mild condition on the cluster-structure, the clusters of the final graph $G_T$ of $n_T$ vertices at time $T$ can be well approximated by a dynamic variant of the spectral clustering algorithm. The algorithm runs in amortised update time $O(1)$ and query time $o(n_T)$. Experimental studies on both synthetic and real-world datasets further confirm the practicality of our designed algorithm.