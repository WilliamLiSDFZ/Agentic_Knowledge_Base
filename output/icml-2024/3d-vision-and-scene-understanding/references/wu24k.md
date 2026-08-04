---
title: "PointMC: Multi-instance Point Cloud Registration based on Maximal Cliques"
source: "https://proceedings.mlr.press/v235/wu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24k/wu24k.pdf"
categories: ['3d-vision-and-scene-understanding', 'graph-clustering-and-matching-algorithms']
tags: ['point-cloud-registration', 'maximal-cliques', 'rigid-transformations', 'multi-instance', '3d-vision']
venue: "ICML 2024"
tldr: "Proposes PointMC, a multi-instance point cloud registration method using maximal cliques to estimate multiple rigid transformations without costly high-dimensional feature clustering."
---

# PointMC: Multi-instance Point Cloud Registration based on Maximal Cliques

**Source**: [https://proceedings.mlr.press/v235/wu24k.html](https://proceedings.mlr.press/v235/wu24k.html)

**TLDR**: Proposes PointMC, a multi-instance point cloud registration method using maximal cliques to estimate multiple rigid transformations without costly high-dimensional feature clustering.

## Abstract

Multi-instance point cloud registration is the problem of estimating multiple rigid transformations between two point clouds. Existing solutions rely on global spatial consistency of ambiguity and the time-consuming clustering of highdimensional correspondence features, making it difficult to handle registration scenarios where multiple instances overlap. To address these problems, we propose a maximal clique based multiinstance point cloud registration framework called PointMC. The key idea is to search for maximal cliques on the correspondence compatibility graph to estimate multiple transformations, and cluster these transformations into clusters corresponding to different instances to efficiently and accurately estimate all poses. PointMC leverages a correspondence embedding module that relies on local spatial consistency to effectively eliminate outliers, and the extracted discriminative features empower the network to circumvent missed pose detection in scenarios involving multiple overlapping instances. We conduct comprehensive experiments on both synthetic and real-world datasets, and the results show that the proposed PointMC yields remarkable performance improvements.