---
title: "Scalable High-Resolution Pixel-Space Image Synthesis with Hourglass Diffusion Transformers"
source: "https://proceedings.mlr.press/v235/crowson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/crowson24a/crowson24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['diffusion-transformers', 'high-resolution', 'image-synthesis']
venue: "ICML 2024"
tldr: "Presents Hourglass Diffusion Transformer (HDiT), a pixel-space image generative model with linear scaling in pixel count enabling efficient high-resolution synthesis."
---

# Scalable High-Resolution Pixel-Space Image Synthesis with Hourglass Diffusion Transformers

**Source**: [https://proceedings.mlr.press/v235/crowson24a.html](https://proceedings.mlr.press/v235/crowson24a.html)

**TLDR**: Presents Hourglass Diffusion Transformer (HDiT), a pixel-space image generative model with linear scaling in pixel count enabling efficient high-resolution synthesis.

## Abstract

We present the Hourglass Diffusion Transformer (HDiT), an image-generative model that exhibits linear scaling with pixel count, supporting training at high resolution (e.g. $1024 \times 1024$) directly in pixel-space. Building on the Transformer architecture, which is known to scale to billions of parameters, it bridges the gap between the efficiency of convolutional U-Nets and the scalability of Transformers. HDiT trains successfully without typical high-resolution training techniques such as multiscale architectures, latent autoencoders or self-conditioning. We demonstrate that HDiT performs competitively with existing models on ImageNet $256^2$, and sets a new state-of-the-art for diffusion models on FFHQ-$1024^2$. Code is available at https://github.com/crowsonkb/k-diffusion.