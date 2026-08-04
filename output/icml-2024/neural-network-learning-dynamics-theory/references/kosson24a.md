---
title: "Rotational Equilibrium: How Weight Decay Balances Learning Across Neural Networks"
source: "https://proceedings.mlr.press/v235/kosson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kosson24a/kosson24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['weight-decay', 'neural-networks', 'learning-dynamics', 'rotational-equilibrium', 'regularization']
venue: "ICML 2024"
tldr: "Demonstrates that weight decay drives neuron weight vectors to a rotational equilibrium balancing magnitude and angular updates across deep networks."
---

# Rotational Equilibrium: How Weight Decay Balances Learning Across Neural Networks

**Source**: [https://proceedings.mlr.press/v235/kosson24a.html](https://proceedings.mlr.press/v235/kosson24a.html)

**TLDR**: Demonstrates that weight decay drives neuron weight vectors to a rotational equilibrium balancing magnitude and angular updates across deep networks.

## Abstract

This study investigates how weight decay affects the update behavior of individual neurons in deep neural networks through a combination of applied analysis and experimentation. Weight decay can cause the expected magnitude and angular updates of a neuron’s weight vector to converge to a steady state we call rotational equilibrium. These states can be highly homogeneous, effectively balancing the average rotation—a proxy for the effective learning rate—across different layers and neurons. Our work analyzes these dynamics across optimizers like Adam, Lion, and SGD with momentum, offering a new simple perspective on training that elucidates the efficacy of widely used but poorly understood methods in deep learning. We demonstrate how balanced rotation plays a key role in the effectiveness of normalization like Weight Standardization, as well as that of AdamW over Adam with L2-regularization. Finally, we show that explicitly controlling the rotation provides the benefits of weight decay while substantially reducing the need for learning rate warmup.