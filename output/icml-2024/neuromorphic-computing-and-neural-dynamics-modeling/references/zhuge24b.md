---
title: "Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration"
source: "https://proceedings.mlr.press/v235/zhuge24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuge24b/zhuge24b.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'transformer-architecture-efficiency-and-scaling']
tags: ['spiking-neural-networks', 'transformers', 'token-sparsification', 'energy-efficiency', 'training-acceleration']
venue: "ICML 2024"
tldr: "This paper proposes a token sparsification framework to accelerate training and inference of spiking transformers while preserving performance."
---

# Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration

**Source**: [https://proceedings.mlr.press/v235/zhuge24b.html](https://proceedings.mlr.press/v235/zhuge24b.html)

**TLDR**: This paper proposes a token sparsification framework to accelerate training and inference of spiking transformers while preserving performance.

## Abstract

Nowadays Spiking Transformers have exhibited remarkable performance close to Artificial Neural Networks (ANNs), while enjoying the inherent energy-efficiency of Spiking Neural Networks (SNNs). However, training Spiking Transformers on GPUs is considerably more time-consuming compared to the ANN counterparts, despite the energy-efficient inference through neuromorphic computation. In this paper, we investigate the token sparsification technique for efficient training of Spiking Transformer and find conventional methods suffer from noticeable performance degradation. We analyze the issue and propose our Sparsification with Timestep-wise Anchor Token and dual Alignments (STATA). Timestep-wise Anchor Token enables precise identification of important tokens across timesteps based on standardized criteria. Additionally, dual Alignments incorporate both Intra and Inter Alignment of the attention maps, fostering the learning of inferior attention. Extensive experiments show the effectiveness of STATA thoroughly, which demonstrates up to $\sim$1.53$\times$ training speedup and $\sim$48% energy reduction with comparable performance on various datasets and architectures.