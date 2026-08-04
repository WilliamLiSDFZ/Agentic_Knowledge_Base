---
title: "FiT: Flexible Vision Transformer for Diffusion Model"
source: "https://proceedings.mlr.press/v235/lu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24k/lu24k.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['vision-transformer', 'diffusion-model', 'flexible-resolution', 'image-generation']
venue: "ICML 2024"
tldr: "Proposes FiT, a flexible vision transformer for diffusion models capable of handling arbitrary image resolutions beyond training domain."
---

# FiT: Flexible Vision Transformer for Diffusion Model

**Source**: [https://proceedings.mlr.press/v235/lu24k.html](https://proceedings.mlr.press/v235/lu24k.html)

**TLDR**: Proposes FiT, a flexible vision transformer for diffusion models capable of handling arbitrary image resolutions beyond training domain.

## Abstract

In the context of this reality, existing diffusion models, such as Diffusion Transformers, often face challenges when processing image resolutions outside of their trained domain. To overcome this limitation, we present the Flexible Vision Transformer (FiT), a transformer architecture specifically designed for generating images with unrestricted resolutions and aspect ratios. Unlike traditional methods that perceive images as static-resolution grids, FiT conceptualizes images as sequences of dynamically-sized tokens. This perspective enables a flexible training strategy that effortlessly adapts to diverse aspect ratios during both training and inference phases, thus promoting resolution generalization and eliminating biases induced by image cropping. Enhanced by a meticulously adjusted network structure and the integration of training-free extrapolation techniques, FiT exhibits remarkable flexibility in resolution extrapolation generation. Comprehensive experiments demonstrate the exceptional performance of FiT across a broad range of resolutions. Repository available at https://github.com/whlzy/FiT.