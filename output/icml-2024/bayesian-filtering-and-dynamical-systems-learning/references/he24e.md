---
title: "ReDiffuser: Reliable Decision-Making Using a Diffuser with Confidence Estimation"
source: "https://proceedings.mlr.press/v235/he24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24e/he24e.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['diffusion-models', 'offline-rl', 'confidence-estimation']
venue: "ICML 2024"
tldr: "ReDiffuser improves reliability of diffusion-based offline reinforcement learning by incorporating confidence estimation to stabilize non-deterministic sampling."
---

# ReDiffuser: Reliable Decision-Making Using a Diffuser with Confidence Estimation

**Source**: [https://proceedings.mlr.press/v235/he24e.html](https://proceedings.mlr.press/v235/he24e.html)

**TLDR**: ReDiffuser improves reliability of diffusion-based offline reinforcement learning by incorporating confidence estimation to stabilize non-deterministic sampling.

## Abstract

The diffusion model has demonstrated impressive performance in offline reinforcement learning. However, non-deterministic sampling in diffusion models can lead to unstable performance. Furthermore, the lack of confidence measurements makes it difficult to evaluate the reliability and trustworthiness of the sampled decisions. To address these issues, we present ReDiffuser, which utilizes confidence estimation to ensure reliable decision-making. We achieve this by learning a confidence function based on Random Network Distillation. The confidence function measures the reliability of sampled decisions and contributes to quantitative recognition of reliable decisions. Additionally, we integrate the confidence function into task-specific sampling procedures to realize adaptive-horizon planning and value-embedded planning. Experiments show that the proposed ReDiffuser achieves state-of-the-art performance on standard offline RL datasets.