---
title: "Data-free Neural Representation Compression with Riemannian Neural Dynamics"
source: "https://proceedings.mlr.press/v235/pei24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pei24d/pei24d.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'sampling-compression-and-dimensionality-reduction']
tags: ['neural-compression', 'Riemannian-dynamics', 'data-free', 'neuromorphic', 'representation-compression']
venue: "ICML 2024"
tldr: "Presents a data-free neural representation compression method using Riemannian neural dynamics inspired by physical neural interaction models."
---

# Data-free Neural Representation Compression with Riemannian Neural Dynamics

**Source**: [https://proceedings.mlr.press/v235/pei24d.html](https://proceedings.mlr.press/v235/pei24d.html)

**TLDR**: Presents a data-free neural representation compression method using Riemannian neural dynamics inspired by physical neural interaction models.

## Abstract

Neural models are equivalent to dynamic systems from a physics-inspired view, implying that computation on neural networks can be interpreted as the dynamical interactions between neurons. However, existing work models neuronal interaction as a weight-based linear transformation, and the nonlinearity comes from the nonlinear activation functions, which leads to limited nonlinearity and data-fitting ability of the whole neural model. Inspired by Riemannian geometry, we interpret neural structures by projecting neurons onto the Riemannian neuronal state space and model neuronal interaction with Riemannian metric (${\it RieM}$), which provides a more efficient neural representation with higher parameter efficiency. With ${\it RieM}$, we further design a novel data-free neural compression mechanism that does not require additional fine-tuning with real data. Using backbones like ResNet and Vision Transformer, we conduct extensive experiments on datasets such as MNIST, CIFAR-100, ImageNet-1k, and COCO object detection. Empirical results show that, under equal compression rates and computational complexity, models compressed with ${\it RieM}$ achieve superior inference accuracy compared to existing data-free compression methods.