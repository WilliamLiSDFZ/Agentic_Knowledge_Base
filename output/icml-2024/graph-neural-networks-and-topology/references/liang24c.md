---
title: "Sign is Not a Remedy: Multiset-to-Multiset Message Passing for Learning on Heterophilic Graphs"
source: "https://proceedings.mlr.press/v235/liang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liang24c/liang24c.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['heterophilic-graphs', 'message-passing', 'GNN']
venue: "ICML 2024"
tldr: "Multiset-to-multiset message passing is proposed as a better alternative to signed message passing for heterophilic graph learning."
---

# Sign is Not a Remedy: Multiset-to-Multiset Message Passing for Learning on Heterophilic Graphs

**Source**: [https://proceedings.mlr.press/v235/liang24c.html](https://proceedings.mlr.press/v235/liang24c.html)

**TLDR**: Multiset-to-multiset message passing is proposed as a better alternative to signed message passing for heterophilic graph learning.

## Abstract

Graph Neural Networks (GNNs) have gained significant attention as a powerful modeling and inference method, especially for homophilic graph-structured data. To empower GNNs in heterophilic graphs, where adjacent nodes exhibit dissimilar labels or features, Signed Message Passing (SMP) has been widely adopted. However, there is a lack of theoretical and empirical analysis regarding the limitations of SMP. In this work, we unveil the potential pitfalls of SMP and their remedies. We first identify two limitations of SMP: undesirable representation update for multi-hop neighbors and vulnerability against oversmoothing issues. To overcome these challenges, we propose a novel message-passing function called Multiset to Multiset GNN (M2M-GNN). Our theoretical analyses and extensive experiments demonstrate that M2M-GNN effectively alleviates the limitations of SMP, yielding superior performance in comparison.