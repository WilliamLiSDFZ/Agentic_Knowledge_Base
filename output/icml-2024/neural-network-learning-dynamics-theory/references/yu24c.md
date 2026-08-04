---
title: "Activation-Descent Regularization for Input Optimization of ReLU Networks"
source: "https://proceedings.mlr.press/v235/yu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24c/yu24c.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['ReLU-networks', 'input-optimization', 'activation-patterns', 'descent-regularization']
venue: "ICML 2024"
tldr: "Activation-descent regularization is proposed for input optimization of ReLU networks by explicitly accounting for activation pattern changes."
---

# Activation-Descent Regularization for Input Optimization of ReLU Networks

**Source**: [https://proceedings.mlr.press/v235/yu24c.html](https://proceedings.mlr.press/v235/yu24c.html)

**TLDR**: Activation-descent regularization is proposed for input optimization of ReLU networks by explicitly accounting for activation pattern changes.

## Abstract

We present a new approach for input optimization of ReLU networks that explicitly takes into account the effect of changes in activation patterns. We analyze local optimization steps in both the input space and the space of activation patterns to propose methods with superior local descent properties. To accomplish this, we convert the discrete space of activation patterns into differentiable representations and propose regularization terms that improve each descent step. Our experiments demonstrate the effectiveness of the proposed input-optimization methods for improving the state-of-the-art in various areas, such as adversarial learning, generative modeling, and reinforcement learning.