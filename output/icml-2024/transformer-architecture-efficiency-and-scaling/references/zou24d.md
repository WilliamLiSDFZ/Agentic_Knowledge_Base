---
title: "BiE: Bi-Exponent Block Floating-Point for Large Language Models Quantization"
source: "https://proceedings.mlr.press/v235/zou24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zou24d/zou24d.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['quantization', 'LLMs', 'block-floating-point', 'bi-exponent', 'inference-optimization']
venue: "ICML 2024"
tldr: "BiE proposes a bi-exponent block floating-point quantization scheme to address the challenges of low-bit quantization for large language model inference."
---

# BiE: Bi-Exponent Block Floating-Point for Large Language Models Quantization

**Source**: [https://proceedings.mlr.press/v235/zou24d.html](https://proceedings.mlr.press/v235/zou24d.html)

**TLDR**: BiE proposes a bi-exponent block floating-point quantization scheme to address the challenges of low-bit quantization for large language model inference.

## Abstract

Nowadays, Large Language Models (LLMs) mostly possess billions of parameters, bringing significant challenges to hardware platforms. Although quantization is an efficient approach to reduce computation and memory overhead for inference optimization, we stress the challenge that mainstream low-bit quantization approaches still suffer from either various data distribution outliers or a lack of hardware efficiency. We also find that low-bit data format has further potential expressiveness to cover the atypical language data distribution. In this paper, we propose a novel numerical representation, Bi-Exponent Block Floating Point (BiE), and a new quantization flow. BiE quantization shows accuracy superiority and hardware friendliness on various models and benchmarks.