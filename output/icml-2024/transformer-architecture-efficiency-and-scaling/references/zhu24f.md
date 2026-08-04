---
title: "Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model"
source: "https://proceedings.mlr.press/v235/zhu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24f/zhu24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['state-space-models', 'vision-backbone', 'mamba', 'bidirectional', 'visual-representation']
venue: "ICML 2024"
tldr: "Vision Mamba proposes an efficient visual representation learning backbone using bidirectional state space models for long-range visual sequence modeling."
---

# Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model

**Source**: [https://proceedings.mlr.press/v235/zhu24f.html](https://proceedings.mlr.press/v235/zhu24f.html)

**TLDR**: Vision Mamba proposes an efficient visual representation learning backbone using bidirectional state space models for long-range visual sequence modeling.

## Abstract

Recently the state space models (SSMs) with efficient hardware-aware designs, i.e., the Mamba deep learning model, have shown great potential for long sequence modeling. Meanwhile building efficient and generic vision backbones purely upon SSMs is an appealing direction. However, representing visual data is challenging for SSMs due to the position-sensitivity of visual data and the requirement of global context for visual understanding. In this paper, we show that the reliance on self-attention for visual representation learning is not necessary and propose a new generic vision backbone with bidirectional Mamba blocks (Vim), which marks the image sequences with position embeddings and compresses the visual representation with bidirectional state space models. On ImageNet classification, COCO object detection, and ADE20k semantic segmentation tasks, Vim achieves higher performance compared to well-established vision transformers like DeiT, while also demonstrating significantly improved computation & memory efficiency. For example, Vim is 2.8x faster than DeiT and saves 86.8% GPU memory when performing batch inference to extract features on images with a resolution of 1248x1248. The results demonstrate that Vim is capable of overcoming the computation & memory constraints on performing Transformer-style understanding for high-resolution images and it has great potential to be the next-generation backbone for vision foundation models.