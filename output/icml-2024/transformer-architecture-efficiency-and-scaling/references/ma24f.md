---
title: "Outlier-aware Slicing for Post-Training Quantization in Vision Transformer"
source: "https://proceedings.mlr.press/v235/ma24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24f/ma24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'learning-with-imperfect-data-and-bias']
tags: ['post-training-quantization', 'outliers', 'vision-transformer', 'model-compression']
venue: "ICML 2024"
tldr: "An outlier-aware slicing method for post-training quantization mitigates outlier-induced accuracy degradation in quantized vision transformers."
---

# Outlier-aware Slicing for Post-Training Quantization in Vision Transformer

**Source**: [https://proceedings.mlr.press/v235/ma24f.html](https://proceedings.mlr.press/v235/ma24f.html)

**TLDR**: An outlier-aware slicing method for post-training quantization mitigates outlier-induced accuracy degradation in quantized vision transformers.

## Abstract

Post-Training Quantization (PTQ) is a vital technique for network compression and acceleration, gaining prominence as model sizes increase. This paper addresses a critical challenge in PTQ: the severe impact of outliers on the accuracy of quantized transformer architectures. Specifically, we introduce the concept of ‘reconstruction granularity’ as a novel solution to this issue, which has been overlooked in previous works. Our work provides theoretical insights into the role of reconstruction granularity in mitigating the outlier problem in transformer models. This theoretical framework is supported by empirical analysis, demonstrating that varying reconstruction granularities significantly influence quantization performance. Our findings indicate that different architectural designs necessitate distinct optimal reconstruction granularities. For instance, the multi-stage Swin Transformer architecture benefits from finer granularity, a deviation from the trends observed in ViT and DeiT models. We further develop an algorithm for determining the optimal reconstruction granularity for various ViT models, achieving state-of-the-art (SOTA) performance in PTQ. For example, applying our method to $4$-bit quantization, the Swin-Base model achieves a Top-1 accuracy of $82.24%$ on the ImageNet classification task. This result surpasses the RepQ-ViT by $3.92%$ ($82.24%$ VS $78.32%$). Similarly, our approach elevates the ViT-Small to a Top-1 accuracy of $80.50%$, outperforming NoisyQuant by $3.64%$ ($80.50%$ VS $76.86%$). Codes are available in Supplementary Materials.