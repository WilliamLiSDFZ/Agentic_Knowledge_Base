---
title: "Bridging Data Gaps in Diffusion Models with Adversarial Noise-Based Transfer Learning"
source: "https://proceedings.mlr.press/v235/wang24ap.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ap/wang24ap.pdf"
categories: ['generative-models-and-variational-inference', 'learning-with-imperfect-data-and-bias']
tags: ['diffusion-models', 'transfer-learning', 'adversarial-noise', 'limited-data']
venue: "ICML 2024"
tldr: "Adversarial noise-based transfer learning is proposed to bridge data gaps in diffusion models for image generation."
---

# Bridging Data Gaps in Diffusion Models with Adversarial Noise-Based Transfer Learning

**Source**: [https://proceedings.mlr.press/v235/wang24ap.html](https://proceedings.mlr.press/v235/wang24ap.html)

**TLDR**: Adversarial noise-based transfer learning is proposed to bridge data gaps in diffusion models for image generation.

## Abstract

Diffusion Probabilistic Models (DPMs) show significant potential in image generation, yet their performance hinges on having access to large datasets. Previous works, like Generative Adversarial Networks (GANs), have tackled the limited data problem by transferring pre-trained models learned with sufficient data. However, those methods are hard to be utilized in DPMs since the distinct differences between DPM-based and GAN-based methods, showing in the unique iterative denoising process integral and the need for many timesteps with no-targeted noise in DPMs. In this paper, we propose a novel DPMs-based transfer learning method, ANT, to address the limited data problem. It includes two strategies: similarity-guided training, which boosts transfer with a classifier, and adversarial noise selection which adaptively chooses targeted noise based on the input image. Extensive experiments in the context of few-shot image generation tasks demonstrate that our method is not only efficient but also excels in terms of image quality and diversity when compared to existing GAN-based and DDPM-based methods.