---
title: "Correcting Diffusion-Based Perceptual Image Compression with Privileged End-to-End Decoder"
source: "https://proceedings.mlr.press/v235/ma24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24s/ma24s.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['diffusion-models', 'perceptual-image-compression', 'end-to-end-decoder']
venue: "ICML 2024"
tldr: "A diffusion-based perceptual image compression framework with a privileged end-to-end decoder to correct distortion while maintaining perceptual quality."
---

# Correcting Diffusion-Based Perceptual Image Compression with Privileged End-to-End Decoder

**Source**: [https://proceedings.mlr.press/v235/ma24s.html](https://proceedings.mlr.press/v235/ma24s.html)

**TLDR**: A diffusion-based perceptual image compression framework with a privileged end-to-end decoder to correct distortion while maintaining perceptual quality.

## Abstract

The images produced by diffusion models can attain excellent perceptual quality. However, it is challenging for diffusion models to guarantee distortion, hence the integration of diffusion models and image compression models still needs more comprehensive explorations. This paper presents a diffusion-based image compression method that employs a privileged end-to-end decoder model as correction, which achieves better perceptual quality while guaranteeing the distortion to an extent. We build a diffusion model and design a novel paradigm that combines the diffusion model and an end-to-end decoder, and the latter is responsible for transmitting the privileged information extracted at the encoder side. Specifically, we theoretically analyze the reconstruction process of the diffusion models at the encoder side with the original images being visible. Based on the analysis, we introduce an end-to-end convolutional decoder to provide a better approximation of the score function $\nabla_{\mathbf{x}_t}\log p(\mathbf{x}_t)$ at the encoder side and effectively transmit the combination. Experiments demonstrate the superiority of our method in both distortion and perception compared with previous perceptual compression methods.