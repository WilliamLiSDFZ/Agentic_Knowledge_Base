---
title: "Transolver: A Fast Transformer Solver for PDEs on General Geometries"
source: "https://proceedings.mlr.press/v235/wu24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24r/wu24r.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['transformer', 'PDE-solving', 'neural-operators', 'mesh-based', 'geometry']
venue: "ICML 2024"
tldr: "Proposes Transolver, a fast transformer-based PDE solver that handles complex geometries by efficiently capturing intricate physical interactions on large-scale meshes."
---

# Transolver: A Fast Transformer Solver for PDEs on General Geometries

**Source**: [https://proceedings.mlr.press/v235/wu24r.html](https://proceedings.mlr.press/v235/wu24r.html)

**TLDR**: Proposes Transolver, a fast transformer-based PDE solver that handles complex geometries by efficiently capturing intricate physical interactions on large-scale meshes.

## Abstract

Transformers have empowered many milestones across various fields and have recently been applied to solve partial differential equations (PDEs). However, since PDEs are typically discretized into large-scale meshes with complex geometries, it is challenging for Transformers to capture intricate physical correlations directly from massive individual points. Going beyond superficial and unwieldy meshes, we present Transolver based on a more foundational idea, which is learning intrinsic physical states hidden behind discretized geometries. Specifically, we propose a new Physics-Attention to adaptively split the discretized domain into a series of learnable slices of flexible shapes, where mesh points under similar physical states will be ascribed to the same slice. By calculating attention to physics-aware tokens encoded from slices, Transovler can effectively capture intricate physical correlations under complex geometrics, which also empowers the solver with endogenetic geometry-general modeling capacity and can be efficiently computed in linear complexity. Transolver achieves consistent state-of-the-art with 22% relative gain across six standard benchmarks and also excels in large-scale industrial simulations, including car and airfoil designs. Code is available at https://github.com/thuml/Transolver.