---
title: "High-Performance Temporal Reversible Spiking Neural Networks with $\mathcalO(L)$ Training Memory and $\mathcalO(1)$ Inference Cost"
source: "https://proceedings.mlr.press/v235/hu24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24q/hu24q.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'neural-network-learning-dynamics-theory']
tags: ['spiking-neural-networks', 'temporal-reversibility', 'training-efficiency']
venue: "ICML 2024"
tldr: "Introduces a temporal reversible SNN architecture that achieves O(L) training memory and O(1) inference cost simultaneously."
---

# High-Performance Temporal Reversible Spiking Neural Networks with $\mathcalO(L)$ Training Memory and $\mathcalO(1)$ Inference Cost

**Source**: [https://proceedings.mlr.press/v235/hu24q.html](https://proceedings.mlr.press/v235/hu24q.html)

**TLDR**: Introduces a temporal reversible SNN architecture that achieves O(L) training memory and O(1) inference cost simultaneously.

## Abstract

Multi-timestep simulation of brain-inspired Spiking Neural Networks (SNNs) boost memory requirements during training and increase inference energy cost. Current training methods cannot simultaneously solve both training and inference dilemmas. This work proposes a novel Temporal Reversible architecture for SNNs (T-RevSNN) to jointly address the training and inference challenges by altering the forward propagation of SNNs. We turn off the temporal dynamics of most spiking neurons and design multi-level temporal reversible interactions at temporal turn-on spiking neurons, resulting in a $\mathcal{O}(L)$ training memory. Combined with the temporal reversible nature, we redesign the input encoding and network organization of SNNs to achieve $\mathcal{O}(1)$ inference energy cost. Then, we finely adjust the internal units and residual connections of the basic SNN block to ensure the effectiveness of sparse temporal information interaction. T-RevSNN achieves excellent accuracy on ImageNet, while the memory efficiency, training time acceleration and inference energy efficiency can be significantly improved by $8.6 \times$, $2.0 \times$ and $1.6 \times$, respectively. This work is expected to break the technical bottleneck of significantly increasing memory cost and training time for large-scale SNNs while maintaining both high performance and low inference energy cost.