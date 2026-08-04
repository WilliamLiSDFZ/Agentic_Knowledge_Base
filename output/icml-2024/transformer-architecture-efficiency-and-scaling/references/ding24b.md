---
title: "AMPA: Adaptive Mixed Precision Allocation for Low-Bit Integer Training"
source: "https://proceedings.mlr.press/v235/ding24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24b/ding24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['mixed-precision', 'quantization', 'low-bit-training', 'integer-arithmetic', 'adaptive-allocation']
venue: "ICML 2024"
tldr: "Proposes AMPA, an adaptive mixed precision allocation method enabling effective low-bit integer training beyond fixed INT8 precision for neural networks."
---

# AMPA: Adaptive Mixed Precision Allocation for Low-Bit Integer Training

**Source**: [https://proceedings.mlr.press/v235/ding24b.html](https://proceedings.mlr.press/v235/ding24b.html)

**TLDR**: Proposes AMPA, an adaptive mixed precision allocation method enabling effective low-bit integer training beyond fixed INT8 precision for neural networks.

## Abstract

Low-bit integer training emerges as a promising approach to mitigate the heavy burden during network training by quantizing the weights, activations, and gradients. However, existing methods cannot well achieve mixed-precision quantization for low-bit training and are commonly limited to INT8 precision. In this paper, we propose a novel low-bit integer training framework that, for the first time, achieves adaptive mixed-precision allocation (AMPA) for weights, activations, and gradients, and pushes the boundaries to a precision level below INT8. We develop a novel magnitude-based sensitivity measurement with regard to the quantization losses of weight, activation, and gradient quantization and the average gradient magnitudes, which is demonstrated as an upper bound of quantization influence in theory. We further design a layer-wise precision update strategy under observations on the quantization losses and their effects on model performance in low-bit training. Extensive experiments on different backbones and datasets show that, compared to INT8 quantization, the proposed method can achieve more than 38% BitOPs reduction with a tolerable loss below 2% in image classification, image segmentation, and language modeling.