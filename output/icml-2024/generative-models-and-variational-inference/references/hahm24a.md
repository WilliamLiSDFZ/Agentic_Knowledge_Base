---
title: "Isometric Representation Learning for Disentangled Latent Space of Diffusion Models"
source: "https://proceedings.mlr.press/v235/hahm24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hahm24a/hahm24a.pdf"
categories: ['generative-models-and-variational-inference', 'llm-geometry-and-interpretability-research']
tags: ['diffusion-models', 'latent-space', 'disentanglement', 'isometric-representation', 'generative-models']
venue: "ICML 2024"
tldr: "Proposes isometric representation learning to create a disentangled and geometry-preserving latent space for diffusion models."
---

# Isometric Representation Learning for Disentangled Latent Space of Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/hahm24a.html](https://proceedings.mlr.press/v235/hahm24a.html)

**TLDR**: Proposes isometric representation learning to create a disentangled and geometry-preserving latent space for diffusion models.

## Abstract

The latent space of diffusion model mostly still remains unexplored, despite its great success and potential in the field of generative modeling. In fact, the latent space of existing diffusion models are entangled, with a distorted mapping from its latent space to image space. To tackle this problem, we present Isometric Diffusion, equipping a diffusion model with a geometric regularizer to guide the model to learn a geometrically sound latent space of the training data manifold. This approach allows diffusion models to learn a more disentangled latent space, which enables smoother interpolation, more accurate inversion, and more precise control over attributes directly in the latent space. Our extensive experiments consisting of image interpolations, image inversions, and linear editing show the effectiveness of our method.