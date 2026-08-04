---
title: "GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer"
source: "https://proceedings.mlr.press/v235/jia24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jia24b/jia24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'clustering-methods-and-multi-view-learning']
tags: ['multimodal-fusion', 'vision-transformer', 'cross-modal', 'pixel-wise']
venue: "ICML 2024"
tldr: "GeminiFusion proposes an efficient pixel-wise multimodal fusion method for vision transformers that outperforms prior token exchange approaches."
---

# GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

**Source**: [https://proceedings.mlr.press/v235/jia24b.html](https://proceedings.mlr.press/v235/jia24b.html)

**TLDR**: GeminiFusion proposes an efficient pixel-wise multimodal fusion method for vision transformers that outperforms prior token exchange approaches.

## Abstract

Cross-modal transformers have demonstrated superiority in various vision tasks by effectively integrating different modalities. This paper first critiques prior token exchange methods which replace less informative tokens with inter-modal features, and demonstrate exchange based methods underperform cross-attention mechanisms, while the computational demand of the latter inevitably restricts its use with longer sequences. To surmount the computational challenges, we propose GeminiFusion, a pixel-wise fusion approach that capitalizes on aligned cross-modal representations. GeminiFusion elegantly combines intra-modal and inter-modal attentions, dynamically integrating complementary information across modalities. We employ a layer-adaptive noise to adaptively control their interplay on a per-layer basis, thereby achieving a harmonized fusion process. Notably, GeminiFusion maintains linear complexity with respect to the number of input tokens, ensuring this multimodal framework operates with efficiency comparable to unimodal networks. Comprehensive evaluations across multimodal image-to-image translation, $3$D object detection and arbitrary-modal semantic segmentation tasks, including RGB, depth, LiDAR, event data, etc. demonstrate the superior performance of our GeminiFusion against leading-edge techniques. The PyTorch code is available here.