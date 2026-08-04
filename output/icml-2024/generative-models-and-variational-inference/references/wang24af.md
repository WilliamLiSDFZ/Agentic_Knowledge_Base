---
title: "MS$^3$D: A RG Flow-Based Regularization for GAN Training with Limited Data"
source: "https://proceedings.mlr.press/v235/wang24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24af/wang24af.pdf"
categories: ['generative-models-and-variational-inference', 'learning-with-imperfect-data-and-bias']
tags: ['GANs', 'limited-data', 'renormalization-group', 'regularization']
venue: "ICML 2024"
tldr: "A renormalization group flow-based regularization method is proposed to stabilize GAN training under limited data conditions."
---

# MS$^3$D: A RG Flow-Based Regularization for GAN Training with Limited Data

**Source**: [https://proceedings.mlr.press/v235/wang24af.html](https://proceedings.mlr.press/v235/wang24af.html)

**TLDR**: A renormalization group flow-based regularization method is proposed to stabilize GAN training under limited data conditions.

## Abstract

Generative adversarial networks (GANs) have made impressive advances in image generation, but they often require large-scale training data to avoid degradation caused by discriminator overfitting. To tackle this issue, we investigate the challenge of training GANs with limited data, and propose a novel regularization method based on the idea of renormalization group (RG) in physics.We observe that in the limited data setting, the gradient pattern that the generator obtains from the discriminator becomes more aggregated over time. In RG context, this aggregated pattern exhibits a high discrepancy from its coarse-grained versions, which implies a high-capacity and sensitive system, prone to overfitting and collapse. To address this problem, we introduce a multi-scale structural self-dissimilarity (MS$^3$D) regularization, which constrains the gradient field to have a consistent pattern across different scales, thereby fostering a more redundant and robust system. We show that our method can effectively enhance the performance and stability of GANs under limited data scenarios, and even allow them to generate high-quality images with very few data.