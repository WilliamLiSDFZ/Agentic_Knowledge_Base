---
title: "Latent Space Symmetry Discovery"
source: "https://proceedings.mlr.press/v235/yang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24g/yang24g.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'algebraic-structures-in-machine-learning']
tags: ['symmetry-discovery', 'equivariant-networks', 'latent-space']
venue: "ICML 2024"
tldr: "A method to automatically discover complex nonlinear symmetries in latent spaces without requiring prior knowledge of the symmetry group."
---

# Latent Space Symmetry Discovery

**Source**: [https://proceedings.mlr.press/v235/yang24g.html](https://proceedings.mlr.press/v235/yang24g.html)

**TLDR**: A method to automatically discover complex nonlinear symmetries in latent spaces without requiring prior knowledge of the symmetry group.

## Abstract

Equivariant neural networks require explicit knowledge of the symmetry group. Automatic symmetry discovery methods aim to relax this constraint and learn invariance and equivariance from data. However, existing symmetry discovery methods are limited to simple linear symmetries and cannot handle the complexity of real-world data. We propose a novel generative model, Latent LieGAN (LaLiGAN), which can discover symmetries of nonlinear group actions. It learns a mapping from the data space to a latent space where the symmetries become linear and simultaneously discovers symmetries in the latent space. Theoretically, we show that our model can express nonlinear symmetries under some conditions about the group action. Experimentally, we demonstrate that our method can accurately discover the intrinsic symmetry in high-dimensional dynamical systems. LaLiGAN also results in a well-structured latent space that is useful for downstream tasks including equation discovery and long-term forecasting.