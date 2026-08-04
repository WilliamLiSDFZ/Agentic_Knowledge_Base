---
title: "Topological Neural Networks go Persistent, Equivariant, and Continuous"
source: "https://proceedings.mlr.press/v235/verma24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/verma24a/verma24a.pdf"
categories: ['topological-deep-learning-persistent-homology', 'graph-neural-networks-and-topology']
tags: ['topological-neural-networks', 'persistent-homology', 'equivariance', 'higher-order-interactions', 'continuous']
venue: "ICML 2024"
tldr: "Extends topological neural networks to incorporate persistent homology, equivariance, and continuous settings for richer higher-order relational representations."
---

# Topological Neural Networks go Persistent, Equivariant, and Continuous

**Source**: [https://proceedings.mlr.press/v235/verma24a.html](https://proceedings.mlr.press/v235/verma24a.html)

**TLDR**: Extends topological neural networks to incorporate persistent homology, equivariance, and continuous settings for richer higher-order relational representations.

## Abstract

Topological Neural Networks (TNNs) incorporate higher-order relational information beyond pairwise interactions, enabling richer representations than Graph Neural Networks (GNNs). Concurrently, topological descriptors based on persistent homology (PH) are being increasingly employed to augment the GNNs. We investigate the benefits of integrating these two paradigms. Specifically, we introduce TopNets as a broad framework that subsumes and unifies various methods in the intersection of GNNs/TNNs and PH such as (generalizations of) RePHINE and TOGL. TopNets can also be readily adapted to handle (symmetries in) geometric complexes, extending the scope of TNNs and PH to spatial settings. Theoretically, we show that PH descriptors can provably enhance the expressivity of simplicial message-passing networks. Empirically, (continuous and $E(n)$-equivariant extensions of) TopNets achieve strong performance across diverse tasks, including antibody design, molecular dynamics simulation, and drug property prediction.