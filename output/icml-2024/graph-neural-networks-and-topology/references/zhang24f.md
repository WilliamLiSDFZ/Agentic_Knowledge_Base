---
title: "Improving Equivariant Graph Neural Networks on Large Geometric Graphs via Virtual Nodes Learning"
source: "https://proceedings.mlr.press/v235/zhang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24f/zhang24f.pdf"
categories: ['graph-neural-networks-and-topology', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['equivariant-GNN', 'large-graphs', 'virtual-nodes']
venue: "ICML 2024"
tldr: "Virtual node learning improves equivariant GNN efficiency and performance on large sparse geometric graphs."
---

# Improving Equivariant Graph Neural Networks on Large Geometric Graphs via Virtual Nodes Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24f.html](https://proceedings.mlr.press/v235/zhang24f.html)

**TLDR**: Virtual node learning improves equivariant GNN efficiency and performance on large sparse geometric graphs.

## Abstract

Equivariant Graph Neural Networks (GNNs) have made remarkable success in a variety of scientific applications. However, existing equivariant GNNs encounter the efficiency issue for large geometric graphs and perform poorly if the input is reduced to sparse local graph for speed acceleration. In this paper, we propose FastEGNN, an enhanced model of equivariant GNNs on large geometric graphs. The central idea is leveraging a small ordered set of virtual nodes to approximate the large unordered graph of real nodes. In particular, we distinguish the message passing and aggregation for different virtual node to encourage the mutual distinctiveness, and minimize the Maximum Mean Discrepancy (MMD) between virtual and real coordinates to realize the global distributedness. FastEGNN meets all necessary E(3) symmetries, with certain universal expressivity assurance as well. Our experiments on N-body systems (100 nodes), proteins (800 nodes) and water-3D (8000 nodes), demonstrate that FastEGNN achieves a promising balance between accuracy and efficiency, and outperforms EGNN in accuracy even after dropping all edges in real systems like proteins and water-3D.