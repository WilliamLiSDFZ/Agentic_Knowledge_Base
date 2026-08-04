---
title: "A Near-Linear Time Approximation Algorithm for Beyond-Worst-Case Graph Clustering"
source: "https://proceedings.mlr.press/v235/cohen-addad24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen-addad24c/cohen-addad24c.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['graph-clustering', 'semi-random-model', 'approximation-algorithms']
venue: "ICML 2024"
tldr: "Presents a near-linear time approximation algorithm for graph clustering under a semi-random adversarial model beyond worst-case analysis."
---

# A Near-Linear Time Approximation Algorithm for Beyond-Worst-Case Graph Clustering

**Source**: [https://proceedings.mlr.press/v235/cohen-addad24c.html](https://proceedings.mlr.press/v235/cohen-addad24c.html)

**TLDR**: Presents a near-linear time approximation algorithm for graph clustering under a semi-random adversarial model beyond worst-case analysis.

## Abstract

We consider the semi-random graph model of [Makarychev, Makarychev and Vijayaraghavan, STOC’12], where, given a random bipartite graph with $\alpha$ edges and an unknown bipartition $(A, B)$ of the vertex set, an adversary can add arbitrary edges inside each community and remove arbitrary edges from the cut $(A, B)$ (i.e. all adversarial changes are monotone with respect to the bipartition). For this model, a polynomial time algorithm [MMV’12] is known to approximate the Balanced Cut problem up to value $O(\alpha)$ as long as the cut $(A, B)$ has size $\Omega(\alpha)$. However, it consists of slow subroutines requiring optimal solutions for logarithmically many semidefinite programs. We study the fine-grained complexity of the problem and present the first near-linear time algorithm that achieves similar performances to that of [MMV’12]. Our algorithm runs in time $O(|V(G)|^{1+o(1)} + |E(G)|^{1+o(1)})$ and finds a balanced cut of value $O(\alpha).$ Our approach appears easily extendible to related problem, such as Sparsest Cut, and also yields an near-linear time $O(1)$-approximation to Dagupta’s objective function for hierarchical clustering [Dasgupta, STOC’16] for the semi-random hierarchical stochastic block model inputs of [Cohen-Addad, Kanade, Mallmann-Trenn, Mathieu, JACM’19].