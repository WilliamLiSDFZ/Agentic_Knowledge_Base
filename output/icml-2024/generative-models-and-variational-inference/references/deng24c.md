---
title: "Variational Schrödinger Diffusion Models"
source: "https://proceedings.mlr.press/v235/deng24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deng24c/deng24c.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['Schrödinger-bridge', 'diffusion-models', 'variational-inference', 'score-matching', 'optimal-transport']
venue: "ICML 2024"
tldr: "Introduces variational Schrödinger diffusion models that avoid costly simulated trajectory training by efficiently approximating the forward score in Schrödinger bridges."
---

# Variational Schrödinger Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/deng24c.html](https://proceedings.mlr.press/v235/deng24c.html)

**TLDR**: Introduces variational Schrödinger diffusion models that avoid costly simulated trajectory training by efficiently approximating the forward score in Schrödinger bridges.

## Abstract

Schrödinger bridge (SB) has emerged as the go-to method for optimizing transportation plans in diffusion models. However, SB requires estimating the intractable forward score functions, inevitably resulting in the (costly) implicit training loss based on simulated trajectories. To improve the scalability while preserving efficient transportation plans, we leverage variational inference to linearize the forward score functions (variational scores) of SB and restore simulation-free properties in training backward scores. We propose the variational Schrödinger diffusion model (VSDM), where the forward process is a multivariate diffusion and the variational scores are adaptively optimized for efficient transport. Theoretically, we use stochastic approximation to prove the convergence of the variational scores and show the convergence of the adaptively generated samples based on the optimal variational scores. Empirically, we test the algorithm in simulated examples and observe that VSDM is efficient in generations of anisotropic shapes and yields straighter sample trajectories compared to the single-variate diffusion. We also verify the scalability of the algorithm in real-world data and achieve competitive unconditional generation performance in CIFAR10 and conditional generation in time series modeling. Notably, VSDM no longer depends on warm-up initializations required by SB.