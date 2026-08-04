---
title: "Improving Adversarial Energy-Based Model via Diffusion Process"
source: "https://proceedings.mlr.press/v235/geng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/geng24a/geng24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-optimization-and-surrogate-methods']
tags: ['energy-based-models', 'diffusion-process', 'adversarial-training']
venue: "ICML 2024"
tldr: "Improves adversarial energy-based model training by incorporating a diffusion process for better likelihood estimation."
---

# Improving Adversarial Energy-Based Model via Diffusion Process

**Source**: [https://proceedings.mlr.press/v235/geng24a.html](https://proceedings.mlr.press/v235/geng24a.html)

**TLDR**: Improves adversarial energy-based model training by incorporating a diffusion process for better likelihood estimation.

## Abstract

Generative models have shown strong generation ability while efficient likelihood estimation is less explored. Energy-based models (EBMs) define a flexible energy function to parameterize unnormalized densities efficiently but are notorious for being difficult to train. Adversarial EBMs introduce a generator to form a minimax training game to avoid expensive MCMC sampling used in traditional EBMs, but a noticeable gap between adversarial EBMs and other strong generative models still exists. Inspired by diffusion-based models, we embedded EBMs into each denoising step to split a long-generated process into several smaller steps. Besides, we employ a symmetric Jeffrey divergence and introduce a variational posterior distribution for the generator’s training to address the main challenges that exist in adversarial EBMs. Our experiments show significant improvement in generation compared to existing adversarial EBMs, while also providing a useful energy function for efficient density estimation.