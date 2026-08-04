---
title: "Accelerating Parallel Sampling of Diffusion Models"
source: "https://proceedings.mlr.press/v235/tang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24f/tang24f.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['diffusion-models', 'parallel-sampling', 'acceleration']
venue: "ICML 2024"
tldr: "A novel parallel sampling approach accelerates diffusion model inference by breaking the autoregressive sampling bottleneck."
---

# Accelerating Parallel Sampling of Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/tang24f.html](https://proceedings.mlr.press/v235/tang24f.html)

**TLDR**: A novel parallel sampling approach accelerates diffusion model inference by breaking the autoregressive sampling bottleneck.

## Abstract

Diffusion models have emerged as state-of-the-art generative models for image generation. However, sampling from diffusion models is usually time-consuming due to the inherent autoregressive nature of their sampling process. In this work, we propose a novel approach that accelerates the sampling of diffusion models by parallelizing the autoregressive process. Specifically, we reformulate the sampling process as solving a system of triangular nonlinear equations through fixed-point iteration. With this innovative formulation, we explore several systematic techniques to further reduce the iteration steps required by the solving process. Applying these techniques, we introduce ParaTAA, a universal and training-free parallel sampling algorithm that can leverage extra computational and memory resources to increase the sampling speed. Our experiments demonstrate that ParaTAA can decrease the inference steps required by common sequential sampling algorithms such as DDIM and DDPM by a factor of 4$\sim$14 times. Notably, when applying ParaTAA with 100 steps DDIM for Stable Diffusion, a widely-used text-to-image diffusion model, it can produce the same images as the sequential sampling in only 7 inference steps. The code is available at https://github.com/TZW1998/ParaTAA-Diffusion.