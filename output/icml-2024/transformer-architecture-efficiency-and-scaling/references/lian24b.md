---
title: "Receptive Fields As Experts in Convolutional Neural Architectures"
source: "https://proceedings.mlr.press/v235/lian24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lian24b/lian24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['receptive-fields', 'mixture-of-experts', 'convolutional-networks']
venue: "ICML 2024"
tldr: "Mixture of Receptive Fields (MoRF) dynamically combines multiple receptive field sizes as experts in CNN architectures."
---

# Receptive Fields As Experts in Convolutional Neural Architectures

**Source**: [https://proceedings.mlr.press/v235/lian24b.html](https://proceedings.mlr.press/v235/lian24b.html)

**TLDR**: Mixture of Receptive Fields (MoRF) dynamically combines multiple receptive field sizes as experts in CNN architectures.

## Abstract

The size of spatial receptive fields, from the early 3$\times$3 convolutions in VGGNet to the recent 7$\times$7 convolutions in ConvNeXt, has always played a critical role in architecture design. In this paper, we propose a Mixture of Receptive Fields (MoRF) instead of using a single receptive field. MoRF contains the combinations of multiple receptive fields with different sizes, e.g., convolutions with different kernel sizes, which can be regarded as experts. Such an approach serves two functions: one is to select the appropriate receptive field according to the input, and the other is to expand the network capacity. Furthermore, we also introduce two types of routing mechanisms, hard routing and soft routing to automatically select the appropriate receptive field experts. In the inference stage, the selected receptive field experts are merged via re-parameterization to maintain a similar inference speed compared to the single receptive field. To demonstrate the effectiveness of MoRF, we integrate the MoRF concept into multiple architectures, e.g., ResNet and ConvNeXt. Extensive experiments show that our approach outperforms the baselines in image classification, object detection, and segmentation tasks without significantly increasing the inference time.