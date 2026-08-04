---
title: "Dynamic Metric Embedding into lp Space"
source: "https://proceedings.mlr.press/v235/banihashem24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/banihashem24b/banihashem24b.pdf"
categories: ['dynamic-algorithms-and-complexity-theory', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['dynamic-embedding', 'metric-spaces', 'graph-algorithms']
venue: "ICML 2024"
tldr: "The first non-trivial decremental dynamic graph embedding into lp space is presented with maintained distortion guarantees."
---

# Dynamic Metric Embedding into lp Space

**Source**: [https://proceedings.mlr.press/v235/banihashem24b.html](https://proceedings.mlr.press/v235/banihashem24b.html)

**TLDR**: The first non-trivial decremental dynamic graph embedding into lp space is presented with maintained distortion guarantees.

## Abstract

We give the first non-trivial decremental dynamic embedding of a weighted, undirected graph $G$ into $\ell_p$ space. Given a weighted graph $G$ undergoing a sequence of edge weight increases, the goal of this problem is to maintain a (randomized) mapping $\phi: (G,d) \to (X,\ell_p)$ from the set of vertices of the graph to the $\ell_p$ space such that for every pair of vertices $u$ and $v$, the expected distance between $\phi(u)$ and $\phi(v)$ in the $\ell_p$ metric is within a small multiplicative factor, referred to as the distortion, of their distance in $G$. Our main result is a dynamic algorithm with expected distortion $O(\log^2 n)$ and total update time $O\left((m^{1+o(1)} \log^2 W + Q)\log(nW) \right)$, where $W$ is the maximum weight of the edges, $Q$ is the total number of updates and $n, m$ denote the number of vertices and edges in $G$ respectively. This is the first result of its kind, extending the seminal result of Bourgain ’85 to the expanding field of dynamic algorithms. Moreover, we demonstrate that in the fully dynamic regime, where we tolerate edge insertions as well as deletions, no algorithm can explicitly maintain an embedding into $\ell_p$ space that has a low distortion with high probability.