---
title: "3D Geometric Shape Assembly via Efficient Point Cloud Matching"
source: "https://proceedings.mlr.press/v235/lee24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24s/lee24s.pdf"
categories: ['3d-vision-and-scene-understanding', 'graph-clustering-and-matching-algorithms']
tags: ['3D-assembly', 'point-cloud-matching', 'shape-correspondence', 'geometric-learning']
venue: "ICML 2024"
tldr: "Introduces Proxy Matching for efficient coarse-to-fine point cloud correspondence to assemble 3D geometric shapes."
---

# 3D Geometric Shape Assembly via Efficient Point Cloud Matching

**Source**: [https://proceedings.mlr.press/v235/lee24s.html](https://proceedings.mlr.press/v235/lee24s.html)

**TLDR**: Introduces Proxy Matching for efficient coarse-to-fine point cloud correspondence to assemble 3D geometric shapes.

## Abstract

Learning to assemble geometric shapes into a larger target structure is a pivotal task in various practical applications. In this work, we tackle this problem by establishing local correspondences between point clouds of part shapes in both coarse- and fine-levels. To this end, we introduce Proxy Match Transform (PMT), an approximate high-order feature transform layer that enables reliable matching between mating surfaces of parts while incurring low costs in memory and compute. Building upon PMT, we introduce a new framework, dubbed Proxy Match TransformeR (PMTR), for the geometric assembly task. We evaluate the proposed PMTR on the large-scale 3D geometric shape assembly benchmark dataset of Breaking Bad and demonstrate its superior performance and efficiency compared to state-of-the-art methods. Project page: https://nahyuklee.github.io/pmtr