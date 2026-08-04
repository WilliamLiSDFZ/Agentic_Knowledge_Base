---
title: "The Surprising Effectiveness of Skip-Tuning in Diffusion Sampling"
source: "https://proceedings.mlr.press/v235/ma24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24r/ma24r.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['diffusion-models', 'skip-connections', 'image-generation']
venue: "ICML 2024"
tldr: "An investigation into the surprising effectiveness of tuning skip connections in UNet-based diffusion models to improve image generation quality."
---

# The Surprising Effectiveness of Skip-Tuning in Diffusion Sampling

**Source**: [https://proceedings.mlr.press/v235/ma24r.html](https://proceedings.mlr.press/v235/ma24r.html)

**TLDR**: An investigation into the surprising effectiveness of tuning skip connections in UNet-based diffusion models to improve image generation quality.

## Abstract

With the incorporation of the UNet architecture, diffusion probabilistic models have become a dominant force in image generation tasks. One key design in UNet is the skip connections between the encoder and decoder blocks. Although skip connections have been shown to improve training stability and model performance, we point out that such shortcuts can be a limiting factor for the complexity of the transformation. As the sampling steps decrease, the generation process and the role of the UNet get closer to the push-forward transformations from Gaussian distribution to the target, posing a challenge for the network’s complexity. To address this challenge, we propose Skip-Tuning, a simple yet surprisingly effective training-free tuning method on the skip connections. For instance, our method can achieve 100% FID improvement for pretrained EDM on ImageNet 64 with only 19 NFEs (1.75), breaking the limit of ODE samplers regardless of sampling steps. Surprisingly, the improvement persists when we increase the number of sampling steps and can even surpass the best result from EDM-2 (1.58) with only 39 NFEs (1.57). Comprehensive exploratory experiments are conducted to shed light on the surprising effectiveness of our Skip-Tuning. We observe that while Skip-Tuning increases the score-matching losses in the pixel space, the losses in the feature space are reduced, particularly at intermediate noise levels, which coincide with the most effective range accounting for image quality improvement.