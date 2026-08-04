---
title: "Particle Denoising Diffusion Sampler"
source: "https://proceedings.mlr.press/v235/phillips24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/phillips24a/phillips24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['diffusion-models', 'particle-methods', 'score-matching']
venue: "ICML 2024"
tldr: "A particle-based denoising diffusion sampler that estimates the time-reversal of diffusion processes for approximate sampling."
---

# Particle Denoising Diffusion Sampler

**Source**: [https://proceedings.mlr.press/v235/phillips24a.html](https://proceedings.mlr.press/v235/phillips24a.html)

**TLDR**: A particle-based denoising diffusion sampler that estimates the time-reversal of diffusion processes for approximate sampling.

## Abstract

Denoising diffusion models have become ubiquitous for generative modeling. The core idea is to transport the data distribution to a Gaussian by using a diffusion. Approximate samples from the data distribution are then obtained by estimating the time-reversal of this diffusion using score matching ideas. We follow here a similar strategy to sample from unnormalized probability densities and compute their normalizing constants. However, the time-reversed diffusion is here simulated by using an original iterative particle scheme relying on a novel score matching loss. Contrary to standard denoising diffusion models, the resulting Particle Denoising Diffusion Sampler (PDDS) provides asymptotically consistent estimates under mild assumptions. We demonstrate PDDS on multimodal and high dimensional sampling tasks.