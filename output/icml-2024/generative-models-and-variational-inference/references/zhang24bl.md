---
title: "Directly Denoising Diffusion Models"
source: "https://proceedings.mlr.press/v235/zhang24bl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bl/zhang24bl.pdf"
categories: ['generative-models-and-variational-inference', 'audio-and-music-generation-diffusion-models']
tags: ['diffusion-models', 'few-step-sampling', 'image-generation', 'denoising', 'generative-models']
venue: "ICML 2024"
tldr: "Presents Directly Denoising Diffusion Models (DDDMs) for high-quality image generation with few-step sampling without distillation or custom samplers."
---

# Directly Denoising Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/zhang24bl.html](https://proceedings.mlr.press/v235/zhang24bl.html)

**TLDR**: Presents Directly Denoising Diffusion Models (DDDMs) for high-quality image generation with few-step sampling without distillation or custom samplers.

## Abstract

In this paper, we present Directly Denoising Diffusion Models (DDDMs): a simple and generic approach for generating realistic images with few-step sampling, while multistep sampling is still preserved for better performance. DDDMs require no delicately designed samplers nor distillation on pre-trained distillation models. DDDMs train the diffusion model conditioned on an estimated target that was generated from previous training iterations of its own. To generate images, samples generated from previous timestep are also taken into consideration, guiding the generation process iteratively. We further propose Pseudo-LPIPS, a novel metric loss that is more robust to various values of hyperparameter. Despite its simplicity, the proposed approach can achieve strong performance in benchmark datasets. Our model achieves FID scores of 2.57 and 2.33 on CIFAR-10 in one-step and two-step sampling respectively, surpassing those obtained from GANs and distillation-based models. By extending the sampling to 1000 steps, we further reduce FID score to 1.79, aligning with state-of-the-art methods in the literature. For ImageNet 64x64, our approach stands as a competitive contender against leading models.