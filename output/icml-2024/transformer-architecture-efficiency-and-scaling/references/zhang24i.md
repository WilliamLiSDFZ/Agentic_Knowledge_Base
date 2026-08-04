---
title: "Reshape and Adapt for Output Quantization (RAOQ): Quantization-aware Training for In-memory Computing Systems"
source: "https://proceedings.mlr.press/v235/zhang24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24i/zhang24i.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['quantization', 'in-memory-computing', 'quantization-aware-training']
venue: "ICML 2024"
tldr: "A quantization-aware training method that reshapes and adapts weights to minimize output quantization error for in-memory computing systems."
---

# Reshape and Adapt for Output Quantization (RAOQ): Quantization-aware Training for In-memory Computing Systems

**Source**: [https://proceedings.mlr.press/v235/zhang24i.html](https://proceedings.mlr.press/v235/zhang24i.html)

**TLDR**: A quantization-aware training method that reshapes and adapts weights to minimize output quantization error for in-memory computing systems.

## Abstract

In-memory computing (IMC) has emerged as a promising solution to address both computation and data-movement challenges, by performing computation on data in-place directly in the memory array. IMC typically relies on analog operation, which makes analog-to-digital converters (ADCs) necessary, for converting results back to the digital domain. However, ADCs maintain computational efficiency by having limited precision, leading to substantial quantization errors in compute outputs. This work proposes RAOQ (Reshape and Adapt for Output Quantization) to overcome this issue, which comprises two classes of mechanisms including: 1) mitigating ADC quantization error by adjusting the statistics of activations and weights, through an activation-shifting approach (A-shift) and a weight reshaping technique (W-reshape); 2) adapting AI models to better tolerate ADC quantization through a bit augmentation method (BitAug), complemented by the introduction of ADC-LoRA, a low-rank approximation technique, to reduce the training overhead. RAOQ demonstrates consistently high performance across different scales and domains of neural network models for computer vision and natural language processing (NLP) tasks at various bit precisions, achieving state-of-the-art results with practical IMC implementations.