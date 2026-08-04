---
title: "Image Restoration Through Generalized Ornstein-Uhlenbeck Bridge"
source: "https://proceedings.mlr.press/v235/yue24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yue24d/yue24d.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['diffusion-model', 'image-restoration', 'Ornstein-Uhlenbeck-bridge', 'stochastic-differential-equations']
venue: "ICML 2024"
tldr: "Introduces a Generalized Ornstein-Uhlenbeck Bridge diffusion model for direct low-quality to high-quality image restoration mapping."
---

# Image Restoration Through Generalized Ornstein-Uhlenbeck Bridge

**Source**: [https://proceedings.mlr.press/v235/yue24d.html](https://proceedings.mlr.press/v235/yue24d.html)

**TLDR**: Introduces a Generalized Ornstein-Uhlenbeck Bridge diffusion model for direct low-quality to high-quality image restoration mapping.

## Abstract

Diffusion models exhibit powerful generative capabilities enabling noise mapping to data via reverse stochastic differential equations. However, in image restoration, the focus is on the mapping relationship from low-quality to high-quality images. Regarding this issue, we introduce the Generalized Ornstein-Uhlenbeck Bridge (GOUB) model. By leveraging the natural mean-reverting property of the generalized OU process and further eliminating the variance of its steady-state distribution through the Doob’s h–transform, we achieve diffusion mappings from point to point enabling the recovery of high-quality images from low-quality ones. Moreover, we unravel the fundamental mathematical essence shared by various bridge models, all of which are special instances of GOUB and empirically demonstrate the optimality of our proposed models. Additionally, we present the corresponding Mean-ODE model adept at capturing both pixel-level details and structural perceptions. Experimental outcomes showcase the state-of-the-art performance achieved by both models across diverse tasks, including inpainting, deraining, and super-resolution. Code is available at https://github.com/Hammour-steak/GOUB.