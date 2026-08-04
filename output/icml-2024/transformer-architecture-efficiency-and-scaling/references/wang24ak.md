---
title: "Visual Transformer with Differentiable Channel Selection: An Information Bottleneck Inspired Approach"
source: "https://proceedings.mlr.press/v235/wang24ak.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ak/wang24ak.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'ai-explainability-uncertainty-human-decision-making']
tags: ['visual-transformers', 'information-bottleneck', 'channel-selection', 'attention']
venue: "ICML 2024"
tldr: "A differentiable channel selection module inspired by the information bottleneck is proposed for visual transformers to improve efficiency and performance."
---

# Visual Transformer with Differentiable Channel Selection: An Information Bottleneck Inspired Approach

**Source**: [https://proceedings.mlr.press/v235/wang24ak.html](https://proceedings.mlr.press/v235/wang24ak.html)

**TLDR**: A differentiable channel selection module inspired by the information bottleneck is proposed for visual transformers to improve efficiency and performance.

## Abstract

Self-attention and transformers have been widely used in deep learning. Recent efforts have been devoted to incorporating transformer blocks into different types of neural architectures, including those with convolutions, leading to various visual transformers for computer vision tasks. In this paper, we propose a novel and compact transformer block, Transformer with Differentiable Channel Selection, or DCS-Transformer. DCS-Transformer features channel selection in the computation of the attention weights and the input/output features of the MLP in the transformer block. Our DCS-Transformer is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs of the visual transformers while maintaining or even improving the prediction accuracy. In the experiments, we replace all the transformer blocks in MobileViT and EfficientViT with DCS-Transformer blocks, leading to DCS-Transformer networks with different backbones. The DCS-Transformer is motivated by reduction of Information Bottleneck, and a novel variational upper bound for the IB loss which can be optimized by SGD is derived and incorporated into the training loss of the network with DCS-Transformer. Extensive results on image classification and object detection evidence that DCS-Transformer renders compact and efficient visual transformers with comparable or much better prediction accuracy than the original visual transformers. The code of DCS-Transformer is available at https://github.com/Statistical-Deep-Learning/DCS-Transformer.