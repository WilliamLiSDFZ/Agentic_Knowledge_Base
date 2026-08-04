---
title: "Compositional Curvature Bounds for Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/entesari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/entesari24a/entesari24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'neural-network-learning-dynamics-theory']
tags: ['adversarial-robustness', 'curvature-bounds', 'second-order-analysis', 'deep-neural-networks', 'compositional-bounds']
venue: "ICML 2024"
tldr: "Derives tight compositional upper bounds on the curvature of deep neural networks to certify robustness against adversarial perturbations."
---

# Compositional Curvature Bounds for Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/entesari24a.html](https://proceedings.mlr.press/v235/entesari24a.html)

**TLDR**: Derives tight compositional upper bounds on the curvature of deep neural networks to certify robustness against adversarial perturbations.

## Abstract

A key challenge that threatens the widespread use of neural networks in safety-critical applications is their vulnerability to adversarial attacks. In this paper, we study the second-order behavior of continuously differentiable deep neural networks, focusing on robustness against adversarial perturbations. First, we provide a theoretical analysis of robustness and attack certificates for deep classifiers by leveraging local gradients and upper bounds on the second derivative (curvature constant). Next, we introduce a novel algorithm to analytically compute provable upper bounds on the second derivative of neural networks. This algorithm leverages the compositional structure of the model to propagate the curvature bound layer-by-layer, giving rise to a scalable and modular approach. The proposed bound can serve as a differentiable regularizer to control the curvature of neural networks during training, thereby enhancing robustness. Finally, we demonstrate the efficacy of our method on classification tasks using the MNIST and CIFAR-10 datasets.