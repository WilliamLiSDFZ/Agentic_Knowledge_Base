---
title: "PolySketchFormer: Fast Transformers via Sketching Polynomial Kernels"
source: "https://proceedings.mlr.press/v235/kacham24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kacham24a/kacham24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['transformers', 'sketching', 'polynomial-kernels', 'efficient-attention']
venue: "ICML 2024"
tldr: "PolySketchFormer uses polynomial kernel sketching to reduce self-attention complexity, enabling fast transformer training and inference."
---

# PolySketchFormer: Fast Transformers via Sketching Polynomial Kernels

**Source**: [https://proceedings.mlr.press/v235/kacham24a.html](https://proceedings.mlr.press/v235/kacham24a.html)

**TLDR**: PolySketchFormer uses polynomial kernel sketching to reduce self-attention complexity, enabling fast transformer training and inference.

## Abstract

The quadratic time and memory complexity inherent to self-attention mechanisms, with respect to sequence length, presents a critical computational bottleneck in the training and deployment of large-scale Transformer-based language models. Recent theoretical results indicate the intractability of sub-quadratic softmax attention approximation under reasonable complexity assumptions. This paper addresses this challenge by first demonstrating that polynomial attention with high degree can effectively replace softmax without sacrificing model quality. Next, we develop polynomial sketching techniques from numerical linear algebra to achieve linear-time polynomial attention with approximation guarantees. Crucially, our approach achieves this speedup without requiring the sparsification of attention matrices. We also present a block-based algorithm to apply causal masking efficiently. Combining these techniques, we provide PolySketchFormer, a practical linear-time Transformer architecture for language modeling that offers provable guarantees. We validate PolySketchFormer empirically by training language models capable of handling long contexts. These experiments utilize both synthetic and real-world datasets (PG19, Wikipedia and C4) on Google Cloud TPUs. For context lengths of 32k and GPT-2 style models, our model achieves 2x speedup in training compared to FlashAttention of the fastest configuration, with no observed degradation in quality across our experiments.