---
title: "Resfusion: Denoising Diffusion Probabilistic Models for Image Restoration Based on Prior Residual Noise"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference']
tags: ['diffusion-models', 'image-restoration', 'residual-noise-prior']
venue: "NeurIPS 2024"
tldr: "Introduces Resfusion, a diffusion-based image restoration model that incorporates prior residual noise to guide the reverse generation process."
---

# Resfusion: Denoising Diffusion Probabilistic Models for Image Restoration Based on Prior Residual Noise

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html)

**TLDR**: Introduces Resfusion, a diffusion-based image restoration model that incorporates prior residual noise to guide the reverse generation process.

## Abstract

Recently, research on denoising diffusion models has expanded its application to the field of image restoration. Traditional diffusion-based image restoration methods utilize degraded images as conditional input to effectively guide the reverse generation process, without modifying the original denoising diffusion process. However, since the degraded images already include low-frequency information, starting from Gaussian white noise will result in increased sampling steps. We propose Resfusion, a general framework that incorporates the residual term into the diffusion forward process, starting the reverse process directly from the noisy degraded images. The form of our inference process is consistent with the DDPM. We introduced a weighted residual noise, named resnoise, as the prediction target and explicitly provide the quantitative relationship between the residual term and the noise term in resnoise. By leveraging a smooth equivalence transformation, Resfusion determine the optimal acceleration step and maintains the integrity of existing noise schedules, unifying the training and inference processes. The experimental results demonstrate that Resfusion exhibits competitive performance on ISTD dataset, LOL dataset and Raindrop dataset with only five sampling steps. Furthermore, Resfusion can be easily applied to image generation and emerges with strong versatility. Our code and model are available at https://github.com/nkicsl/Resfusion.