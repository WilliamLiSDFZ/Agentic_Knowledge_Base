---
title: "GaussianPro: 3D Gaussian Splatting with Progressive Propagation"
source: "https://proceedings.mlr.press/v235/cheng24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24f/cheng24f.pdf"
categories: ['3d-vision-and-scene-understanding', 'transformer-architecture-efficiency-and-scaling']
tags: ['3D-Gaussian-splatting', 'progressive-propagation', 'neural-rendering']
venue: "ICML 2024"
tldr: "GaussianPro enhances 3D Gaussian Splatting with progressive propagation to improve rendering quality in large-scale textureless scenes."
---

# GaussianPro: 3D Gaussian Splatting with Progressive Propagation

**Source**: [https://proceedings.mlr.press/v235/cheng24f.html](https://proceedings.mlr.press/v235/cheng24f.html)

**TLDR**: GaussianPro enhances 3D Gaussian Splatting with progressive propagation to improve rendering quality in large-scale textureless scenes.

## Abstract

3D Gaussian Splatting (3DGS) has recently revolutionized the field of neural rendering with its high fidelity and efficiency. However, 3DGS heavily depends on the initialized point cloud produced by Structure-from-Motion (SfM) techniques. When tackling large-scale scenes that unavoidably contain texture-less surfaces, SfM techniques fail to produce enough points in these surfaces and cannot provide good initialization for 3DGS. As a result, 3DGS suffers from difficult optimization and low-quality renderings. In this paper, inspired by classic multi-view stereo (MVS) techniques, we propose GaussianPro, a novel method that applies a progressive propagation strategy to guide the densification of the 3D Gaussians. Compared to the simple split and clone strategies used in 3DGS, our method leverages the priors of the existing reconstructed geometries of the scene and utilizes patch matching to produce new Gaussians with accurate positions and orientations. Experiments on both large-scale and small-scale scenes validate the effectiveness of our method. Our method significantly surpasses 3DGS on the Waymo dataset, exhibiting an improvement of 1.15dB in terms of PSNR. Codes and data are available at https://github.com/kcheng1021/GaussianPro.