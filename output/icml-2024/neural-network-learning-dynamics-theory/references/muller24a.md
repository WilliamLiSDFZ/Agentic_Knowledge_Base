---
title: "Is Kernel Prediction More Powerful than Gating in Convolutional Neural Networks?"
source: "https://proceedings.mlr.press/v235/muller24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muller24a/muller24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['hypernetworks', 'kernel-prediction', 'gating', 'convolutional-networks']
venue: "ICML 2024"
tldr: "The theoretical relationship between kernel prediction and gating in ConvNets is analyzed, questioning the assumed hierarchy of multiplicative interactions."
---

# Is Kernel Prediction More Powerful than Gating in Convolutional Neural Networks?

**Source**: [https://proceedings.mlr.press/v235/muller24a.html](https://proceedings.mlr.press/v235/muller24a.html)

**TLDR**: The theoretical relationship between kernel prediction and gating in ConvNets is analyzed, questioning the assumed hierarchy of multiplicative interactions.

## Abstract

Neural networks whose weights are the output of a predictor (HyperNetworks) achieve excellent performance on many tasks. In ConvNets, kernel prediction layers are a popular type of HyperNetwork. Previous theoretical work has argued that a hierarchy of multiplicative interactions exists in which gating is at the bottom and full weight prediction, as in HyperNetworks, is at the top. In this paper, we constructively demonstrate an equivalence between gating combined with fixed weight layers and weight prediction, relativizing the notion of a hierarchy of multiplicative interactions. We further derive an equivalence between a restricted type of HyperNetwork and factorization machines. Finally, we find empirically that gating layers can learn to imitate weight prediction layers with an SGD variant and show a novel practical application in image denoising using kernel prediction networks. Our reformulation of predicted kernels, combining fixed layers and gating, reduces memory requirements.