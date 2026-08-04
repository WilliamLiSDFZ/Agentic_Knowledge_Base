---
title: "Efficient Denoising Diffusion via Probabilistic Masking"
source: "https://proceedings.mlr.press/v235/zhang24cf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cf/zhang24cf.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['diffusion-models', 'efficient-inference', 'probabilistic-masking']
venue: "ICML 2024"
tldr: "Proposes probabilistic masking to accelerate diffusion model inference by reducing required denoising timesteps."
---

# Efficient Denoising Diffusion via Probabilistic Masking

**Source**: [https://proceedings.mlr.press/v235/zhang24cf.html](https://proceedings.mlr.press/v235/zhang24cf.html)

**TLDR**: Proposes probabilistic masking to accelerate diffusion model inference by reducing required denoising timesteps.

## Abstract

Diffusion models have exhibited remarkable advancements in generating high-quality data. However, a critical drawback is their computationally intensive inference process, which requires a large number of timesteps to generate a single sample. Existing methods address this challenge by decoupling the forward and reverse processes, and they rely on handcrafted rules for sampling acceleration, leading to the risk of discarding important steps. In this paper, we propose an Efficient Denoising Diffusion method via Probabilistic Masking (EDDPM) that can identify and skip the redundant steps during training. To determine whether a timestep should be skipped or not, we employ probabilistic reparameterization to continualize the binary determination mask. The mask distribution parameters are learned jointly with model weights. By incorporating a real-time sparse constraint, our method can effectively identify and eliminate unnecessary steps during the training iterations, thereby improving inference efficiency. Notably, as the model becomes fully trained, the random masks converge to a sparse and deterministic one, retaining only a small number of essential steps. Empirical results demonstrate the superiority of our proposed EDDPM over the state-of-the-art sampling acceleration methods across various domains. EDDPM can generate high-quality samples with only 20% of the steps for time series imputation and achieve 4.89 FID with 5 steps for CIFAR-10. Moreover, when starting from a pretrained model, our method efficiently identifies the most informative timesteps within a single epoch, which demonstrates the potential of EDDPM to be a practical tool to explore large diffusion models with limited resources.