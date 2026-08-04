---
title: "A Computational Framework for Solving Wasserstein Lagrangian Flows"
source: "https://proceedings.mlr.press/v235/neklyudov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/neklyudov24a/neklyudov24a.pdf"
categories: ['sampling-and-optimization-on-manifolds']
tags: ['optimal-transport', 'wasserstein-geometry', 'lagrangian-flows']
venue: "ICML 2024"
tldr: "A computational framework is introduced for solving Wasserstein Lagrangian flows under diverse geometry and regularization choices."
---

# A Computational Framework for Solving Wasserstein Lagrangian Flows

**Source**: [https://proceedings.mlr.press/v235/neklyudov24a.html](https://proceedings.mlr.press/v235/neklyudov24a.html)

**TLDR**: A computational framework is introduced for solving Wasserstein Lagrangian flows under diverse geometry and regularization choices.

## Abstract

The dynamical formulation of the optimal transport can be extended through various choices of the underlying geometry (kinetic energy), and the regularization of density paths (potential energy). These combinations yield different variational problems (Lagrangians), encompassing many variations of the optimal transport problem such as the Schrödinger bridge, unbalanced optimal transport, and optimal transport with physical constraints, among others. In general, the optimal density path is unknown, and solving these variational problems can be computationally challenging. We propose a novel deep learning based framework approaching all of these problems from a unified perspective. Leveraging the dual formulation of the Lagrangians, our method does not require simulating or backpropagating through the trajectories of the learned dynamics, and does not need access to optimal couplings. We showcase the versatility of the proposed framework by outperforming previous approaches for the single-cell trajectory inference, where incorporating prior knowledge into the dynamics is crucial for correct predictions.