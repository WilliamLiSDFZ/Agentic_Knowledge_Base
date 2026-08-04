---
title: "An Infinite-Width Analysis on the Jacobian-Regularised Training of a Neural Network"
source: "https://proceedings.mlr.press/v235/kim24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ah/kim24ah.pdf"
categories: ['neural-network-learning-dynamics-theory', 'neural-operators-for-pde-solving']
tags: ['infinite-width-networks', 'Jacobian-regularization', 'neural-tangent-kernel']
venue: "ICML 2024"
tldr: "Analyzes Jacobian-regularized neural network training in the infinite-width limit to understand feature learning and generalization."
---

# An Infinite-Width Analysis on the Jacobian-Regularised Training of a Neural Network

**Source**: [https://proceedings.mlr.press/v235/kim24ah.html](https://proceedings.mlr.press/v235/kim24ah.html)

**TLDR**: Analyzes Jacobian-regularized neural network training in the infinite-width limit to understand feature learning and generalization.

## Abstract

The recent theoretical analysis of deep neural networks in their infinite-width limits has deepened our understanding of initialisation, feature learning, and training of those networks, and brought new practical techniques for finding appropriate hyperparameters, learning network weights, and performing inference. In this paper, we broaden this line of research by showing that this infinite-width analysis can be extended to the Jacobian of a deep neural network. We show that a multilayer perceptron (MLP) and its Jacobian at initialisation jointly converge to a Gaussian process (GP) as the widths of the MLP’s hidden layers go to infinity and characterise this GP. We also prove that in the infinite-width limit, the evolution of the MLP under the so-called robust training (i.e., training with a regulariser on the Jacobian) is described by a linear first-order ordinary differential equation that is determined by a variant of the Neural Tangent Kernel. We experimentally show the relevance of our theoretical claims to wide finite networks, and empirically analyse the properties of kernel regression solution to obtain an insight into Jacobian regularisation.