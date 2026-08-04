---
title: "MagicPose: Realistic Human Poses and Facial Expressions Retargeting with Identity-aware Diffusion"
source: "https://proceedings.mlr.press/v235/chang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chang24d/chang24d.pdf"
categories: ['generative-models-and-variational-inference', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['diffusion-models', 'pose-retargeting', 'identity-preservation', 'facial-expression']
venue: "ICML 2024"
tldr: "MagicPose uses identity-aware diffusion to retarget human poses and facial expressions while preserving subject identity."
---

# MagicPose: Realistic Human Poses and Facial Expressions Retargeting with Identity-aware Diffusion

**Source**: [https://proceedings.mlr.press/v235/chang24d.html](https://proceedings.mlr.press/v235/chang24d.html)

**TLDR**: MagicPose uses identity-aware diffusion to retarget human poses and facial expressions while preserving subject identity.

## Abstract

In this work, we propose MagicPose, a diffusion-based model for 2D human pose and facial expression retargeting. Specifically, given a reference image, we aim to generate a person’s new images by controlling the poses and facial expressions while keeping the identity unchanged. To this end, we propose a two-stage training strategy to disentangle human motions and appearance (e.g., facial expressions, skin tone, and dressing), consisting of (1) the pre-training of an appearance-control block and (2) learning appearance-disentangled pose control. Our novel design enables robust appearance control over generated human images, including body, facial attributes, and even background. By leveraging the prior knowledge of image diffusion models, MagicPose generalizes well to unseen human identities and complex poses without the need for additional fine-tuning. Moreover, the proposed model is easy to use and can be considered as a plug-in module/extension to Stable Diffusion. The project website is here. The code is available here.