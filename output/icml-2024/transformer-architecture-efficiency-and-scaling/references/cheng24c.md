---
title: "Reference Neural Operators: Learning the Smooth Dependence of Solutions of PDEs on Geometric Deformations"
source: "https://proceedings.mlr.press/v235/cheng24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24c/cheng24c.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-operators', 'PDE-solving', 'geometric-deformations']
venue: "ICML 2024"
tldr: "Reference Neural Operators learn the smooth dependence of PDE solutions on geometric deformations to reduce data requirements for arbitrary-shape domains."
---

# Reference Neural Operators: Learning the Smooth Dependence of Solutions of PDEs on Geometric Deformations

**Source**: [https://proceedings.mlr.press/v235/cheng24c.html](https://proceedings.mlr.press/v235/cheng24c.html)

**TLDR**: Reference Neural Operators learn the smooth dependence of PDE solutions on geometric deformations to reduce data requirements for arbitrary-shape domains.

## Abstract

For partial differential equations on domains of arbitrary shapes, existing works of neural operators attempt to learn a mapping from geometries to solutions. It often requires a large dataset of geometry-solution pairs in order to obtain a sufficiently accurate neural operator. However, for many industrial applications, e.g., engineering design optimization, it can be prohibitive to satisfy the requirement since even a single simulation may take hours or days of computation. To address this issue, we propose reference neural operators (RNO), a novel way of implementing neural operators, i.e., to learn the smooth dependence of solutions on geometric deformations. Specifically, given a reference solution, RNO can predict solutions corresponding to arbitrary deformations of the referred geometry. This approach turns out to be much more data efficient. Through extensive experiments, we show that RNO can learn the dependence across various types and different numbers of geometry objects with relatively small datasets. RNO outperforms baseline models in accuracy by a large lead and achieves up to 80% error reduction.