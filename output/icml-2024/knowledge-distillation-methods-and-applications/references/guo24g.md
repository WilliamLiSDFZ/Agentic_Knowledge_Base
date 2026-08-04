---
title: "Compressing Large Language Models by Joint Sparsification and Quantization"
source: "https://proceedings.mlr.press/v235/guo24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24g/guo24g.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['LLM-compression', 'sparsification', 'quantization', 'joint-optimization', 'model-efficiency']
venue: "ICML 2024"
tldr: "A joint sparsification and quantization compression technique tailored for large language models."
---

# Compressing Large Language Models by Joint Sparsification and Quantization

**Source**: [https://proceedings.mlr.press/v235/guo24g.html](https://proceedings.mlr.press/v235/guo24g.html)

**TLDR**: A joint sparsification and quantization compression technique tailored for large language models.

## Abstract

In this paper, we introduce a novel model compression technique named Joint Sparsification and Quantization (JSQ), explicitly tailored for large language models (LLMs). Traditional methods employ either sparsification or quantization individually to compress LLMs, leading to performance degradation at high compression ratios. In contrast, our JSQ approach integrates sparsification and quantization cohesively. As sparsification tend to preserve outliers that is harmful to quantization, we introduce a novel sparsity metric to serves as a bridge between the sparsification and quantization. Moreover, it is proven outliers in LLMs have significant impact but harmful to compression. Current solutions are highly coupled with quantization process, which is not helpful to sparsification. To this end, we also introduce a search-based activation editor to automatically eliminate relatively useless outliers. Comprehensive experiments across various datasets and architectures affirm the efficacy of our JSQ framework. Notably, our JSQ achieves 7.96$\times$ computation reduction without crashing for the representative model LLaMA. This accomplishment stands in stark contrast to the limitations of most state-of-the-art LLM compression methods, which typically fail under such extreme compression ratios. Our code is released at https://github.com/uanu2002/JSQ.