---
title: "Equivariant Diffusion for Crystal Structure Prediction"
source: "https://proceedings.mlr.press/v235/lin24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24b/lin24b.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'generative-models-and-variational-inference']
tags: ['crystal-structure-prediction', 'diffusion-models', 'equivariance']
venue: "ICML 2024"
tldr: "An equivariant diffusion model for crystal structure prediction that enforces permutation, rotation, and periodic translation symmetries."
---

# Equivariant Diffusion for Crystal Structure Prediction

**Source**: [https://proceedings.mlr.press/v235/lin24b.html](https://proceedings.mlr.press/v235/lin24b.html)

**TLDR**: An equivariant diffusion model for crystal structure prediction that enforces permutation, rotation, and periodic translation symmetries.

## Abstract

In addressing the challenge of Crystal Structure Prediction (CSP), symmetry-aware deep learning models, particularly diffusion models, have been extensively studied, which treat CSP as a conditional generation task. However, ensuring permutation, rotation, and periodic translation equivariance during diffusion process remains incompletely addressed. In this work, we propose EquiCSP, a novel equivariant diffusion-based generative model. We not only address the overlooked issue of lattice permutation equivariance in existing models, but also develop a unique noising algorithm that rigorously maintains periodic translation equivariance throughout both training and inference processes. Our experiments indicate that EquiCSP significantly surpasses existing models in terms of generating accurate structures and demonstrates faster convergence during the training process.