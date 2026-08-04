---
title: "Diffusion Rejection Sampling"
source: "https://proceedings.mlr.press/v235/na24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/na24a/na24a.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['diffusion-models', 'rejection-sampling', 'score-based-generative-models']
venue: "ICML 2024"
tldr: "A rejection sampling scheme is introduced to align diffusion model sampling transitions with the true target distribution, improving generation quality."
---

# Diffusion Rejection Sampling

**Source**: [https://proceedings.mlr.press/v235/na24a.html](https://proceedings.mlr.press/v235/na24a.html)

**TLDR**: A rejection sampling scheme is introduced to align diffusion model sampling transitions with the true target distribution, improving generation quality.

## Abstract

Recent advances in powerful pre-trained diffusion models encourage the development of methods to improve the sampling performance under well-trained diffusion models. This paper introduces Diffusion Rejection Sampling (DiffRS), which uses a rejection sampling scheme that aligns the sampling transition kernels with the true ones at each timestep. The proposed method can be viewed as a mechanism that evaluates the quality of samples at each intermediate timestep and refines them with varying effort depending on the sample. Theoretical analysis shows that DiffRS can achieve a tighter bound on sampling error compared to pre-trained models. Empirical results demonstrate the state-of-the-art performance of DiffRS on the benchmark datasets and the effectiveness of DiffRS for fast diffusion samplers and large-scale text-to-image diffusion models. Our code is available at https://github.com/aailabkaist/DiffRS.