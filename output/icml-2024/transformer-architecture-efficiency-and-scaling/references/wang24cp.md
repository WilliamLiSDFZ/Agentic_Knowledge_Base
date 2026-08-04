---
title: "Exploring Intrinsic Dimension for Vision-Language Model Pruning"
source: "https://proceedings.mlr.press/v235/wang24cp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cp/wang24cp.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['intrinsic-dimension', 'vision-language-models', 'network-pruning']
venue: "ICML 2024"
tldr: "This paper leverages intrinsic dimensionality to guide structured pruning of vision-language models with minimal performance loss."
---

# Exploring Intrinsic Dimension for Vision-Language Model Pruning

**Source**: [https://proceedings.mlr.press/v235/wang24cp.html](https://proceedings.mlr.press/v235/wang24cp.html)

**TLDR**: This paper leverages intrinsic dimensionality to guide structured pruning of vision-language models with minimal performance loss.

## Abstract

The intrinsic dimension (ID) represents the minimum dimension needed to describe data on a lower-dimensional manifold within high-dimensional spaces. Network pruning aims to reduce the complexity of high-dimensional networks while minimizing performance trade-offs. This symmetry motivates the exploration of ID as a metric for effective pruning. For vision-language models, we investigate whether different modalities exist on separate manifolds, indicating varying complexity and prunability. We empirically study ID variations in large-scale vision-language pre-trained models and examine the contributions of different modalities to model prunability. We propose a layer importance metric based on ID, which can conveniently integrate with current metrics and enhance performance in vision-language model pruning. The experimental results show a high correlation between ID and modality prunability. Visual representations are more sensitive and crucial to model performance, while language representations are more robust and offer greater prunability. Our findings suggest an asymmetric pruning strategy for vision and language modalities, guided by the ID metric. The code is available at https://github.com/Nofear18/ID_VL_Pruning