---
title: "EDISON: Enhanced Dictionary-Induced Tensorized Incomplete Multi-View Clustering with Gaussian Error Rank Minimization"
source: "https://proceedings.mlr.press/v235/gu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gu24b/gu24b.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'learning-with-imperfect-data-and-bias']
tags: ['incomplete-multi-view-clustering', 'tensor-decomposition', 'dictionary-learning']
venue: "ICML 2024"
tldr: "EDISON proposes an efficient incomplete multi-view clustering method using enhanced dictionary representation and Gaussian error rank minimization."
---

# EDISON: Enhanced Dictionary-Induced Tensorized Incomplete Multi-View Clustering with Gaussian Error Rank Minimization

**Source**: [https://proceedings.mlr.press/v235/gu24b.html](https://proceedings.mlr.press/v235/gu24b.html)

**TLDR**: EDISON proposes an efficient incomplete multi-view clustering method using enhanced dictionary representation and Gaussian error rank minimization.

## Abstract

This paper presents an efficient and scalable incomplete multi-view clustering method, referred to as Enhanced Dictionary-Induced tenSorized incomplete multi-view clustering with Gaussian errOr raNk minimization (EDISON). Specifically, EDISON employs an enhanced dictionary representation strategy as the foundation for inferring missing data and constructing anchor graphs, ensuring robustness to less-than-ideal data and maintaining high computational efficiency. Additionally, we introduce Gaussian error rank as a concise approximation of the true tensor rank, facilitating a comprehensive exploration of the diverse information encapsulated by various singular values in tensor data. Additionally, we integrate a hyper-anchor graph Laplacian manifold regularization into the tensor representation, allowing for the simultaneous utilization of inter-view high-order correlations and intra-view local correlations. Extensive experiments demonstrate the superiority of the EDISON model in both effectiveness and efficiency compared to SOTA methods.