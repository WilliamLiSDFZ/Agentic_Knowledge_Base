---
title: "Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale"
source: "https://proceedings.mlr.press/v235/zheng24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24f/zheng24f.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['diffusion-models', 'guidance', 'nonlinear-correction', 'score-based-generative-models']
venue: "ICML 2024"
tldr: "This paper proposes characteristic guidance, a nonlinear correction to classifier-free guidance in diffusion models that becomes important at large guidance scales."
---

# Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale

**Source**: [https://proceedings.mlr.press/v235/zheng24f.html](https://proceedings.mlr.press/v235/zheng24f.html)

**TLDR**: This paper proposes characteristic guidance, a nonlinear correction to classifier-free guidance in diffusion models that becomes important at large guidance scales.

## Abstract

Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples. However, this approach overlooks nonlinear effects that become significant when guidance scale is large. To address this issue, we propose characteristic guidance, a guidance method that provides first-principle non-linear correction for classifier-free guidance. Such correction forces the guided DDPMs to respect the Fokker-Planck (FP) equation of diffusion process, in a way that is training-free and compatible with existing sampling methods. Experiments show that characteristic guidance enhances semantic characteristics of prompts and mitigate irregularities in image generation, proving effective in diverse applications ranging from simulating magnet phase transitions to latent space sampling.