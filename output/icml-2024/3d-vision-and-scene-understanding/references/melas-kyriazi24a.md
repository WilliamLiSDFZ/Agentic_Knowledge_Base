---
title: "IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation"
source: "https://proceedings.mlr.press/v235/melas-kyriazi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/melas-kyriazi24a/melas-kyriazi24a.pdf"
categories: ['3d-vision-and-scene-understanding']
tags: ['text-to-3D', 'multiview-diffusion', '3D-generation']
venue: "ICML 2024"
tldr: "An iterative multiview diffusion and reconstruction pipeline for high-quality 3D generation from text prompts."
---

# IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation

**Source**: [https://proceedings.mlr.press/v235/melas-kyriazi24a.html](https://proceedings.mlr.press/v235/melas-kyriazi24a.html)

**TLDR**: An iterative multiview diffusion and reconstruction pipeline for high-quality 3D generation from text prompts.

## Abstract

Most text-to-3D generators build upon off-the-shelf text-to-image models trained on billions of images. They use variants of Score Distillation Sampling (SDS), which is slow, somewhat unstable, and prone to artifacts. A mitigation is to fine-tune the 2D generator to be multi-view aware, which can help distillation or can be combined with reconstruction networks to output 3D objects directly. In this paper, we further explore the design space of text-to-3D models. We significantly improve multi-view generation by considering video instead of image generators. Combined with a 3D reconstruction algorithm which, by using Gaussian splatting, can optimize a robust image-based loss, we directly produce high-quality 3D outputs from the generated views. Our new method, IM-3D, reduces the number of evaluations of the 2D generator network 10-100$\times$, resulting in a much more efficient pipeline, better quality, fewer geometric inconsistencies, and higher yield of usable 3D assets.