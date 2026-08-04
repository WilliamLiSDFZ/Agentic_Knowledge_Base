---
title: "DITTO: Diffusion Inference-Time T-Optimization for Music Generation"
source: "https://proceedings.mlr.press/v235/novack24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/novack24a/novack24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'bayesian-optimization-and-surrogate-methods']
tags: ['music-generation', 'diffusion-models', 'inference-time-optimization']
venue: "ICML 2024"
tldr: "Proposes DITTO, a framework for controlling text-to-music diffusion models at inference time by optimizing initial noise latents."
---

# DITTO: Diffusion Inference-Time T-Optimization for Music Generation

**Source**: [https://proceedings.mlr.press/v235/novack24a.html](https://proceedings.mlr.press/v235/novack24a.html)

**TLDR**: Proposes DITTO, a framework for controlling text-to-music diffusion models at inference time by optimizing initial noise latents.

## Abstract

We propose Diffusion Inference-Time T-Optimization (DITTO), a general-purpose framework for controlling pre-trained text-to-music diffusion models at inference-time via optimizing initial noise latents. Our method can be used to optimize through any differentiable feature matching loss to achieve a target (stylized) output and leverages gradient checkpointing for memory efficiency. We demonstrate a surprisingly wide-range of applications for music generation including inpainting, outpainting, and looping as well as intensity, melody, and musical structure control – all without ever fine-tuning the underlying model. When we compare our approach against related training, guidance, and optimization-based methods, we find DITTO achieves state-of-the-art performance on nearly all tasks, including outperforming comparable approaches on controllability, audio quality, and computational efficiency, thus opening the door for high-quality, flexible, training-free control of diffusion models. Sound examples can be found at https://ditto-music.github.io/web/.