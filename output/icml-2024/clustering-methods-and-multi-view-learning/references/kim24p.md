---
title: "Clustered Federated Learning via Gradient-based Partitioning"
source: "https://proceedings.mlr.press/v235/kim24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24p/kim24p.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['federated-learning', 'clustered-partitioning', 'data-heterogeneity']
venue: "ICML 2024"
tldr: "Introduces gradient-based client partitioning for clustered federated learning under privacy-preserving constraints."
---

# Clustered Federated Learning via Gradient-based Partitioning

**Source**: [https://proceedings.mlr.press/v235/kim24p.html](https://proceedings.mlr.press/v235/kim24p.html)

**TLDR**: Introduces gradient-based client partitioning for clustered federated learning under privacy-preserving constraints.

## Abstract

Clustered Federated Learning (CFL) is a promising distributed learning framework that addresses data heterogeneity issues across multiple clients by grouping clients and providing a shared generalized model for each group. However, under privacy-preserving federated learning protocols where there is no direct sharing of clients’ local datasets, existing approaches often fail to find optimal client groupings resulting in sub-optimal performance. In this paper, we propose a novel CFL algorithm that achieves robust clustering and learning performance. Conceptually, our algorithm groups clients that exhibit similarity in their model updates by periodically accumulating and clustering the gradients that clients compute for various models. The proposed algorithm is shown to achieve a near-optimal error rate for stochastic convergence to optimal models under mild conditions. We present a detailed analysis of the algorithm along with an evaluation on several CFL benchmarks demonstrating that it outperforms existing approaches in terms of convergence speed, clustering accuracy, and task performance.