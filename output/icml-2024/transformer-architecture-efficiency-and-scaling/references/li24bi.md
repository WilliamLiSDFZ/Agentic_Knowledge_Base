---
title: "LoRAP: Transformer Sub-Layers Deserve Differentiated Structured Compression for Large Language Models"
source: "https://proceedings.mlr.press/v235/li24bi.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bi/li24bi.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['LoRA', 'structured-compression', 'large-language-models']
venue: "ICML 2024"
tldr: "Proposes LoRAP, a differentiated structured compression method for LLMs that treats transformer sub-layers differently based on their characteristics."
---

# LoRAP: Transformer Sub-Layers Deserve Differentiated Structured Compression for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/li24bi.html](https://proceedings.mlr.press/v235/li24bi.html)

**TLDR**: Proposes LoRAP, a differentiated structured compression method for LLMs that treats transformer sub-layers differently based on their characteristics.

## Abstract

Large language models (LLMs) show excellent performance in difficult tasks, but they often require massive memories and computational resources. How to reduce the parameter scale of LLMs has become research hotspots. In this study, we get an important observation that the multi-head self-attention (MHA) sub-layer of Transformer exhibits noticeable low-rank structure, while the feed-forward network (FFN) sub-layer does not. With this regard, we design a novel structured compression method LoRAP, which organically combines Low-Rank matrix approximation And structured Pruning. For the MHA sub-layer, we proposal an input activation weighted singular value decomposition method and allocate different parameter amounts for each weight matrix based on the differences in low-rank properties of matrices.For the FFN sub-layer, we propose a gradient-free structured channel pruning method and save the least important 1% of parameters which actually play a vital role in model performance. Extensive evaluations on zero-shot perplexity and zero-shot task classification indicate that our proposal is superior to previous structured compression rivals under multiple compression ratios. Our code will be released soon.