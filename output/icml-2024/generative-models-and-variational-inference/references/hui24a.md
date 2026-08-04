---
title: "Make-A-Shape: a Ten-Million-scale 3D Shape Model"
source: "https://proceedings.mlr.press/v235/hui24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hui24a/hui24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['3d-generative-model', 'shape-generation', 'large-scale', 'wavelet', 'implicit-representation']
venue: "ICML 2024"
tldr: "Presents Make-A-Shape, a large-scale 3D generative model trained on 10 million shapes using efficient wavelet-based representations."
---

# Make-A-Shape: a Ten-Million-scale 3D Shape Model

**Source**: [https://proceedings.mlr.press/v235/hui24a.html](https://proceedings.mlr.press/v235/hui24a.html)

**TLDR**: Presents Make-A-Shape, a large-scale 3D generative model trained on 10 million shapes using efficient wavelet-based representations.

## Abstract

The progression in large-scale 3D generative models has been impeded by significant resource requirements for training and challenges like inefficient representations. This paper introduces Make-A-Shape, a novel 3D generative model trained on a vast scale, using 10 million publicly-available shapes. We first innovate the wavelet-tree representation to encode high-resolution SDF shapes with minimal loss, leveraging our newly-proposed subband coefficient filtering scheme. We then design a subband coefficient packing scheme to facilitate diffusion-based generation and a subband adaptive training strategy for effective training on the large-scale dataset. Our generative framework is versatile, capable of conditioning on various input modalities such as images, point clouds, and voxels, enabling a variety of downstream applications, e.g., unconditional generation, completion, and conditional generation. Our approach clearly surpasses the existing baselines in delivering high-quality results and can efficiently generate shapes within two seconds for most conditions.