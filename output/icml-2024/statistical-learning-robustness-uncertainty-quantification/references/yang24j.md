---
title: "Deeper or Wider: A Perspective from Optimal Generalization Error with Sobolev Loss"
source: "https://proceedings.mlr.press/v235/yang24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24j/yang24j.pdf"
categories: ['neural-network-learning-dynamics-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['neural-network-depth', 'generalization-error', 'sobolev-loss']
venue: "ICML 2024"
tldr: "A theoretical comparison of deeper versus wider neural networks through the lens of optimal generalization error using Sobolev loss functions."
---

# Deeper or Wider: A Perspective from Optimal Generalization Error with Sobolev Loss

**Source**: [https://proceedings.mlr.press/v235/yang24j.html](https://proceedings.mlr.press/v235/yang24j.html)

**TLDR**: A theoretical comparison of deeper versus wider neural networks through the lens of optimal generalization error using Sobolev loss functions.

## Abstract

Constructing the architecture of a neural network is a challenging pursuit for the machine learning community, and the dilemma of whether to go deeper or wider remains a persistent question. This paper explores a comparison between deeper neural networks (DeNNs) with a flexible number of layers and wider neural networks (WeNNs) with limited hidden layers, focusing on their optimal generalization error in Sobolev losses. Analytical investigations reveal that the architecture of a neural network can be significantly influenced by various factors, including the number of sample points, parameters within the neural networks, and the regularity of the loss function. Specifically, a higher number of parameters tends to favor WeNNs, while an increased number of sample points and greater regularity in the loss function lean towards the adoption of DeNNs. We ultimately apply this theory to address partial differential equations using deep Ritz and physics-informed neural network (PINN) methods, guiding the design of neural networks.