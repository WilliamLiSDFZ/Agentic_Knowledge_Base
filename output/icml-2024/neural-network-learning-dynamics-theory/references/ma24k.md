---
title: "CKGConv: General Graph Convolution with Continuous Kernels"
source: "https://proceedings.mlr.press/v235/ma24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24k/ma24k.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['graph-convolution', 'continuous-kernels', 'spectral-methods', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "CKGConv defines a general and unified graph convolution operator using continuous kernels that is flexible across spatial and spectral perspectives."
---

# CKGConv: General Graph Convolution with Continuous Kernels

**Source**: [https://proceedings.mlr.press/v235/ma24k.html](https://proceedings.mlr.press/v235/ma24k.html)

**TLDR**: CKGConv defines a general and unified graph convolution operator using continuous kernels that is flexible across spatial and spectral perspectives.

## Abstract

The existing definitions of graph convolution, either from spatial or spectral perspectives, are inflexible and not unified. Defining a general convolution operator in the graph domain is challenging due to the lack of canonical coordinates, the presence of irregular structures, and the properties of graph symmetries. In this work, we propose a novel and general graph convolution framework by parameterizing the kernels as continuous functions of pseudo-coordinates derived via graph positional encoding. We name this Continuous Kernel Graph Convolution (CKGConv). Theoretically, we demonstrate that CKGConv is flexible and expressive. CKGConv encompasses many existing graph convolutions, and exhibits a stronger expressiveness, as powerful as graph transformers in terms of distinguishing non-isomorphic graphs. Empirically, we show that CKGConv-based Networks outperform existing graph convolutional networks and perform comparably to the best graph transformers across a variety of graph datasets. The code and models are publicly available at https://github.com/networkslab/CKGConv.