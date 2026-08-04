---
title: "Coarse-To-Fine Tensor Trains for Compact Visual Representations"
source: "https://proceedings.mlr.press/v235/loeschcke24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/loeschcke24a/loeschcke24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'sampling-compression-and-dimensionality-reduction']
tags: ['tensor-networks', 'tensor-train', 'visual-representations', 'novel-view-synthesis', '3D-reconstruction']
venue: "ICML 2024"
tldr: "Introduces coarse-to-fine tensor train decompositions for compact, high-quality visual representations in 3D tasks."
---

# Coarse-To-Fine Tensor Trains for Compact Visual Representations

**Source**: [https://proceedings.mlr.press/v235/loeschcke24a.html](https://proceedings.mlr.press/v235/loeschcke24a.html)

**TLDR**: Introduces coarse-to-fine tensor train decompositions for compact, high-quality visual representations in 3D tasks.

## Abstract

The ability to learn compact, high-quality, and easy-to-optimize representations for visual data is paramount to many applications such as novel view synthesis and 3D reconstruction. Recent work has shown substantial success in using tensor networks to design such compact and high-quality representations. However, the ability to optimize tensor-based representations, and in particular, the highly compact tensor train representation, is still lacking. This has prevented practitioners from deploying the full potential of tensor networks for visual data. To this end, we propose ’Prolongation Upsampling Tensor Train (PuTT)’, a novel method for learning tensor train representations in a coarse-to-fine manner. Our method involves the prolonging or ‘upsampling’ of a learned tensor train representation, creating a sequence of ’coarse-to-fine’ tensor trains that are incrementally refined. We evaluate our representation along three axes: (1). compression, (2). denoising capability, and (3). image completion capability. To assess these axes, we consider the tasks of image fitting, 3D fitting, and novel view synthesis, where our method shows an improved performance compared to state-of-the-art tensor-based methods.