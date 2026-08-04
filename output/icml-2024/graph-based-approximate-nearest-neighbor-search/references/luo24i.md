---
title: "Cluster-Aware Similarity Diffusion for Instance Retrieval"
source: "https://proceedings.mlr.press/v235/luo24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24i/luo24i.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'graph-based-approximate-nearest-neighbor-search']
tags: ['instance-retrieval', 'similarity-diffusion', 're-ranking', 'cluster-awareness']
venue: "ICML 2024"
tldr: "Cluster-Aware Similarity Diffusion improves instance retrieval by incorporating cluster structure into the affinity graph to reduce outlier propagation."
---

# Cluster-Aware Similarity Diffusion for Instance Retrieval

**Source**: [https://proceedings.mlr.press/v235/luo24i.html](https://proceedings.mlr.press/v235/luo24i.html)

**TLDR**: Cluster-Aware Similarity Diffusion improves instance retrieval by incorporating cluster structure into the affinity graph to reduce outlier propagation.

## Abstract

Diffusion-based re-ranking is a common method used for retrieving instances by performing similarity propagation in a nearest neighbor graph. However, existing techniques that construct the affinity graph based on pairwise instances can lead to the propagation of misinformation from outliers and other manifolds, resulting in inaccurate results. To overcome this issue, we propose a novel Cluster-Aware Similarity (CAS) diffusion for instance retrieval. The primary concept of CAS is to conduct similarity diffusion within local clusters, which can reduce the influence from other manifolds explicitly. To obtain a symmetrical and smooth similarity matrix, our Bidirectional Similarity Diffusion strategy introduces an inverse constraint term to the optimization objective of local cluster diffusion. Additionally, we have optimized a Neighbor-guided Similarity Smoothing approach to ensure similarity consistency among the local neighbors of each instance. Evaluations in instance retrieval and object re-identification validate the effectiveness of the proposed CAS, our code is publicly available.