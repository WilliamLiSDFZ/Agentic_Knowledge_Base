---
title: "Weisfeiler Leman for Euclidean Equivariant Machine Learning"
source: "https://proceedings.mlr.press/v235/hordan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hordan24a/hordan24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'graph-neural-networks-and-topology']
tags: ['weisfeiler-leman', 'gnn', 'equivariance', '3d-point-clouds', 'expressiveness']
venue: "ICML 2024"
tldr: "Connects the k-WL hierarchy to Euclidean equivariant GNNs and proves universality results for models operating on 3D geometric data."
---

# Weisfeiler Leman for Euclidean Equivariant Machine Learning

**Source**: [https://proceedings.mlr.press/v235/hordan24a.html](https://proceedings.mlr.press/v235/hordan24a.html)

**TLDR**: Connects the k-WL hierarchy to Euclidean equivariant GNNs and proves universality results for models operating on 3D geometric data.

## Abstract

The $k$-Weisfeiler-Leman ($k$-WL) graph isomorphism test hierarchy is a common method for assessing the expressive power of graph neural networks (GNNs). Recently, GNNs whose expressive power is equivalent to the $2$-WL test were proven to be universal on weighted graphs which encode $3\mathrm{D}$ point cloud data, yet this result is limited to invariant continuous functions on point clouds. In this paper, we extend this result in three ways: Firstly, we show that PPGN can simulate $2$-WL uniformly on all point clouds with low complexity. Secondly, we show that $2$-WL tests can be extended to point clouds which include both positions and velocities, a scenario often encountered in applications. Finally, we provide a general framework for proving equivariant universality and leverage it to prove that a simple modification of this invariant PPGN architecture can be used to obtain a universal equivariant architecture that can approximate all continuous equivariant functions uniformly. Building on our results, we develop our WeLNet architecture, which sets new state-of-the-art results on the N-Body dynamics task and the GEOM-QM9 molecular conformation generation task.