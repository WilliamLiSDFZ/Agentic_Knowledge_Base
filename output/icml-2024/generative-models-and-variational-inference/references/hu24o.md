---
title: "Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications"
source: "https://proceedings.mlr.press/v235/hu24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24o/hu24o.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['model-inversion', 'vision-transformers', 'data-free-learning']
venue: "ICML 2024"
tldr: "Proposes a sparse model inversion method for vision transformers that efficiently reconstructs training data for data-free applications."
---

# Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications

**Source**: [https://proceedings.mlr.press/v235/hu24o.html](https://proceedings.mlr.press/v235/hu24o.html)

**TLDR**: Proposes a sparse model inversion method for vision transformers that efficiently reconstructs training data for data-free applications.

## Abstract

Model inversion, which aims to reconstruct the original training data from pre-trained discriminative models, is especially useful when the original training data is unavailable due to privacy, usage rights, or size constraints. However, existing dense inversion methods attempt to reconstruct the entire image area, making them extremely inefficient when inverting high-resolution images from large-scale Vision Transformers (ViTs). We further identify two underlying causes of this inefficiency: the redundant inversion of noisy backgrounds and the unintended inversion of spurious correlations—a phenomenon we term “hallucination” in model inversion. To address these limitations, we propose a novel sparse model inversion strategy, as a plug-and-play extension to speed up existing dense inversion methods with no need for modifying their original loss functions. Specifically, we selectively invert semantic foregrounds while stopping the inversion of noisy backgrounds and potential spurious correlations. Through both theoretical and empirical studies, we validate the efficacy of our approach in achieving significant inversion acceleration (up to $\times$3.79) while maintaining comparable or even enhanced downstream performance in data-free model quantization and data-free knowledge transfer. Code is available at https://github.com/Egg-Hu/SMI.