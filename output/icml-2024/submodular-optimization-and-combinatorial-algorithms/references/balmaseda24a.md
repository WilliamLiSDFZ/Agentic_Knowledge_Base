---
title: "Combinatorial Approximations for Cluster Deletion: Simpler, Faster, and Better"
source: "https://proceedings.mlr.press/v235/balmaseda24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balmaseda24a/balmaseda24a.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['cluster-deletion', 'approximation-algorithms', 'graph-clustering']
venue: "ICML 2024"
tldr: "Simpler and faster approximation algorithms for the NP-hard cluster deletion problem are presented with tighter analysis."
---

# Combinatorial Approximations for Cluster Deletion: Simpler, Faster, and Better

**Source**: [https://proceedings.mlr.press/v235/balmaseda24a.html](https://proceedings.mlr.press/v235/balmaseda24a.html)

**TLDR**: Simpler and faster approximation algorithms for the NP-hard cluster deletion problem are presented with tighter analysis.

## Abstract

Cluster deletion is an NP-hard graph clustering objective with applications in computational biology and social network analysis, where the goal is to delete a minimum number of edges to partition a graph into cliques. We first provide a tighter analysis of two previous approximation algorithms, improving their approximation guarantees from 4 to 3. Moreover, we show that both algorithms can be derandomized in a surprisingly simple way, by greedily taking a vertex of maximum degree in an auxiliary graph and forming a cluster around it. One of these algorithms relies on solving a linear program. Our final contribution is to design a new and purely combinatorial approach for doing so that is far more scalable in theory and practice.