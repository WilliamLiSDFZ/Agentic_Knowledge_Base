---
title: "Superpoint Gaussian Splatting for Real-Time High-Fidelity Dynamic Scene Reconstruction"
source: "https://proceedings.mlr.press/v235/wan24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24f/wan24f.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['gaussian-splatting', 'dynamic-scene-reconstruction', 'novel-view-synthesis', 'real-time-rendering', 'deformation-modeling']
venue: "ICML 2024"
tldr: "Superpoint Gaussian Splatting enables real-time high-fidelity dynamic scene reconstruction by grouping Gaussians into superpoints with learned deformations."
---

# Superpoint Gaussian Splatting for Real-Time High-Fidelity Dynamic Scene Reconstruction

**Source**: [https://proceedings.mlr.press/v235/wan24f.html](https://proceedings.mlr.press/v235/wan24f.html)

**TLDR**: Superpoint Gaussian Splatting enables real-time high-fidelity dynamic scene reconstruction by grouping Gaussians into superpoints with learned deformations.

## Abstract

Rendering novel view images in dynamic scenes is a crucial yet challenging task. Current methods mainly utilize NeRF-based methods to represent the static scene and an additional time-variant MLP to model scene deformations, resulting in relatively low rendering quality as well as slow inference speed. To tackle these challenges, we propose a novel framework named Superpoint Gaussian Splatting (SP-GS). Specifically, our framework first employs explicit 3D Gaussians to reconstruct the scene and then clusters Gaussians with similar properties (e.g., rotation, translation, and location) into superpoints. Empowered by these superpoints, our method manages to extend 3D Gaussian splatting to dynamic scenes with only a slight increase in computational expense. Apart from achieving state-of-the-art visual quality and real-time rendering under high resolutions, the superpoint representation provides a stronger manipulation capability. Extensive experiments demonstrate the practicality and effectiveness of our approach on both synthetic and real-world datasets. Please see our project page at https://dnvtmf.github.io/SP_GS.github.io.