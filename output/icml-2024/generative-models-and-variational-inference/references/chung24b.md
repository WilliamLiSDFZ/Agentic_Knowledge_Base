---
title: "Prompt-tuning Latent Diffusion Models for Inverse Problems"
source: "https://proceedings.mlr.press/v235/chung24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chung24b/chung24b.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['inverse-problems', 'latent-diffusion', 'prompt-tuning']
venue: "ICML 2024"
tldr: "Prompt-tuning of text-to-image latent diffusion models is proposed as an improved prior for solving imaging inverse problems."
---

# Prompt-tuning Latent Diffusion Models for Inverse Problems

**Source**: [https://proceedings.mlr.press/v235/chung24b.html](https://proceedings.mlr.press/v235/chung24b.html)

**TLDR**: Prompt-tuning of text-to-image latent diffusion models is proposed as an improved prior for solving imaging inverse problems.

## Abstract

We propose a new method for solving imaging inverse problems using text-to-image latent diffusion models as general priors. Existing methods using latent diffusion models for inverse problems typically rely on simple null text prompts, which can lead to suboptimal performance. To improve upon this, we introduce a method for prompt tuning, which jointly optimizes the text embedding on-the-fly while running the reverse diffusion. This allows us to generate images that are more faithful to the diffusion prior. Specifically, our approach involves a unified optimization framework that simultaneously considers the prompt, latent, and pixel values through alternating minimization. This significantly diminishes image artifacts - a major problem when using latent diffusion models instead of pixel-based diffusion ones. Our method, called P2L, outperforms both pixel- and latent-diffusion model-based inverse problem solvers on a variety of tasks, such as super-resolution, deblurring, and inpainting. Furthermore, P2L demonstrates remarkable scalability to higher resolutions without artifacts.