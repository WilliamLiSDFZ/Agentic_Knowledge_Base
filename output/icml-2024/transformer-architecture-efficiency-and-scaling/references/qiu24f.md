---
title: "Compute Better Spent: Replacing Dense Layers with Structured Matrices"
source: "https://proceedings.mlr.press/v235/qiu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24f/qiu24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['structured-matrices', 'dense-layers', 'efficiency', 'foundation-models', 'compute']
venue: "ICML 2024"
tldr: "Structured matrix replacements for dense linear layers are shown to improve compute efficiency in foundation models."
---

# Compute Better Spent: Replacing Dense Layers with Structured Matrices

**Source**: [https://proceedings.mlr.press/v235/qiu24f.html](https://proceedings.mlr.press/v235/qiu24f.html)

**TLDR**: Structured matrix replacements for dense linear layers are shown to improve compute efficiency in foundation models.

## Abstract

Dense linear layers are the dominant computational bottleneck in foundation models. Identifying more efficient alternatives to dense matrices has enormous potential for building more compute-efficient models, as exemplified by the success of convolutional networks in the image domain. In this work, we systematically explore structured matrices as replacements for dense matrices. We show that different structures often require drastically different initialization scales and learning rates, which are crucial to performance, especially as models scale. Using insights from the Maximal Update Parameterization, we determine the optimal scaling for initialization and learning rates of these unconventional layers. Finally, we measure the scaling laws of different structures to compare how quickly their performance improves with compute. We propose a novel matrix family containing Monarch matrices, the Block Tensor-Train (BTT), which we show performs better than dense matrices for the same compute on multiple tasks. On CIFAR-10/100 with augmentation, BTT achieves exponentially lower training loss than dense when training MLPs and ViTs. BTT matches dense ViT-S/32 performance on ImageNet-1k with 3.8 times less compute and is more efficient than dense for training small GPT-2 language models.