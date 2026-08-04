---
title: "Diffusive Gibbs Sampling"
source: "https://proceedings.mlr.press/v235/chen24be.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24be/chen24be.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['MCMC', 'multi-modal-distributions', 'diffusion-sampling']
venue: "ICML 2024"
tldr: "Diffusive Gibbs Sampling combines diffusion models with Gibbs sampling to improve mixing in multi-modal distributions."
---

# Diffusive Gibbs Sampling

**Source**: [https://proceedings.mlr.press/v235/chen24be.html](https://proceedings.mlr.press/v235/chen24be.html)

**TLDR**: Diffusive Gibbs Sampling combines diffusion models with Gibbs sampling to improve mixing in multi-modal distributions.

## Abstract

The inadequate mixing of conventional Markov Chain Monte Carlo (MCMC) methods for multi-modal distributions presents a significant challenge in practical applications such as Bayesian inference and molecular dynamics. Addressing this, we propose Diffusive Gibbs Sampling (DiGS), an innovative family of sampling methods designed for effective sampling from distributions characterized by distant and disconnected modes. DiGS integrates recent developments in diffusion models, leveraging Gaussian convolution to create an auxiliary noisy distribution that bridges isolated modes in the original space and applying Gibbs sampling to alternately draw samples from both spaces. A novel Metropolis-within-Gibbs scheme is proposed to enhance mixing in the denoising sampling step. DiGS exhibits a better mixing property for sampling multi-modal distributions than state-of-the-art methods such as parallel tempering, attaining substantially improved performance across various tasks, including mixtures of Gaussians, Bayesian neural networks and molecular dynamics.