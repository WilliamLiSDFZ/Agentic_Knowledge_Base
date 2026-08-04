---
title: "BiSHop: Bi-Directional Cellular Learning for Tabular Data with Generalized Sparse Modern Hopfield Model"
source: "https://proceedings.mlr.press/v235/xu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24l/xu24l.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['Hopfield-networks', 'tabular-learning', 'sparse-representation']
venue: "ICML 2024"
tldr: "BiSHop introduces a bi-directional sparse modern Hopfield network framework for deep learning on tabular data handling feature sparsity and non-rotational invariance."
---

# BiSHop: Bi-Directional Cellular Learning for Tabular Data with Generalized Sparse Modern Hopfield Model

**Source**: [https://proceedings.mlr.press/v235/xu24l.html](https://proceedings.mlr.press/v235/xu24l.html)

**TLDR**: BiSHop introduces a bi-directional sparse modern Hopfield network framework for deep learning on tabular data handling feature sparsity and non-rotational invariance.

## Abstract

We introduce the Bi-Directional Sparse Hopfield Network (BiSHop), a novel end-to-end framework for tabular learning. BiSHop handles the two major challenges of deep tabular learning: non-rotationally invariant data structure and feature sparsity in tabular data. Our key motivation comes from the recently established connection between associative memory and attention mechanisms. Consequently, BiSHop uses a dual-component approach, sequentially processing data both column-wise and row-wise through two interconnected directional learning modules. Computationally, these modules house layers of generalized sparse modern Hopfield layers, a sparse extension of the modern Hopfield model with learnable sparsity. Methodologically, BiSHop facilitates multi-scale representation learning, capturing both intra-feature and inter-feature interactions, with adaptive sparsity at each scale. Empirically, through experiments on diverse real-world datasets, BiSHop surpasses current SOTA methods with significantly fewer HPO runs, marking it a robust solution for deep tabular learning. The code is available on GitHub; future updates are on arXiv.