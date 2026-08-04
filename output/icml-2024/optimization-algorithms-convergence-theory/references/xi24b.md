---
title: "Jetfire: Efficient and Accurate Transformer Pretraining with INT8 Data Flow and Per-Block Quantization"
source: "https://proceedings.mlr.press/v235/xi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xi24b/xi24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['quantized-training', 'transformer-pretraining', 'INT8', 'per-block-quantization', 'efficiency']
venue: "ICML 2024"
tldr: "Introduces Jetfire, an efficient transformer pretraining method using INT8 data flow and per-block quantization to achieve significant speedup without performance degradation."
---

# Jetfire: Efficient and Accurate Transformer Pretraining with INT8 Data Flow and Per-Block Quantization

**Source**: [https://proceedings.mlr.press/v235/xi24b.html](https://proceedings.mlr.press/v235/xi24b.html)

**TLDR**: Introduces Jetfire, an efficient transformer pretraining method using INT8 data flow and per-block quantization to achieve significant speedup without performance degradation.

## Abstract

Pretraining transformers are generally time-consuming. Fully quantized training (FQT) is a promising approach to speed up pretraining. However, most FQT methods adopt a quantize-compute-dequantize procedure, which often leads to suboptimal speedup and significant performance degradation when used in transformers due to the high memory access overheads and low-precision computations. In this work, we propose Jetfire, an efficient and accurate INT8 training method specific to transformers. Our method features an INT8 data flow to optimize memory access and a per-block quantization method to maintain the accuracy of pretrained transformers. Extensive experiments demonstrate that our INT8 FQT method achieves comparable accuracy to the FP16 training baseline and outperforms the existing INT8 training works for transformers. Moreover, for a standard transformer block, our method offers an end-to-end training speedup of 1.42x and a 1.49x memory reduction compared to the FP16 baseline.