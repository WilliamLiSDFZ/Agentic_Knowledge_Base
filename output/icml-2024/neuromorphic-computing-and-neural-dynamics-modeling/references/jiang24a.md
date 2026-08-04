---
title: "NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks"
source: "https://proceedings.mlr.press/v235/jiang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24a/jiang24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'optimization-algorithms-convergence-theory']
tags: ['spiking-neural-networks', 'neuromorphic-computing', 'online-training', 'neuronal-dynamics']
venue: "ICML 2024"
tldr: "NDOT leverages neuronal dynamics to enable efficient online training of spiking neural networks without relying on backpropagation through time."
---

# NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks

**Source**: [https://proceedings.mlr.press/v235/jiang24a.html](https://proceedings.mlr.press/v235/jiang24a.html)

**TLDR**: NDOT leverages neuronal dynamics to enable efficient online training of spiking neural networks without relying on backpropagation through time.

## Abstract

Spiking Neural Networks (SNNs) are attracting great attention for their energy-efficient and fast-inference properties in neuromorphic computing. However, the efficient training of deep SNNs poses challenges in gradient calculation due to the non-differentiability of their binary spike-generating activation functions. The widely used surrogate gradient (SG) method, combined with the back-propagation through time (BPTT), has shown considerable effectiveness. Yet, BPTT’s process of unfolding and back-propagating along the computation graph requires storing intermediate information at all time-steps, resulting in huge memory consumption and failing to meet online requirements. In this work, we propose Neuronal Dynamics-based Online Training (NDOT) for SNNs, which uses the neuronal dynamics-based temporal dependency/sensitivity in gradient computation. NDOT enables forward-in-time learning by decomposing the full gradient into temporal and spatial gradients. To illustrate the intuition behind NDOT, we employ the Follow-the-Regularized-Leader (FTRL) algorithm. FTRL explicitly utilizes historical information and addresses limitations in instantaneous loss. Our proposed NDOT method accurately captures temporal dependencies through neuronal dynamics, functioning similarly to FTRL’s explicit utilizing historical information. Experiments on CIFAR-10, CIFAR-100, and CIFAR10-DVS demonstrate the superior performance of our NDOT method on large-scale static and neuromorphic datasets within a small number of time steps. The codes are available at https://github.com/HaiyanJiang/SNN-NDOT.