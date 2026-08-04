---
title: "Bifurcated Attention for Single-Context Large-Batch Sampling"
source: "https://proceedings.mlr.press/v235/athiwaratkun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/athiwaratkun24a/athiwaratkun24a.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'transformer-architecture-efficiency-and-scaling']
tags: ['LLM-inference', 'batch-sampling', 'KV-cache', 'memory-IO', 'attention-mechanism']
venue: "ICML 2024"
tldr: "Introduces bifurcated attention to reduce redundant memory IO costs in single-context large-batch language model inference."
---

# Bifurcated Attention for Single-Context Large-Batch Sampling

**Source**: [https://proceedings.mlr.press/v235/athiwaratkun24a.html](https://proceedings.mlr.press/v235/athiwaratkun24a.html)

**TLDR**: Introduces bifurcated attention to reduce redundant memory IO costs in single-context large-batch language model inference.

## Abstract

In our study, we present bifurcated attention, a method developed for language model inference in single-context batch sampling contexts. This approach aims to reduce redundant memory IO costs, a significant factor in latency for high batch sizes and long context lengths. Bifurcated attention achieves this by dividing the attention mechanism during incremental decoding into two distinct GEMM operations, focusing on the KV cache from prefill and the decoding process. This method ensures precise computation and maintains the usual computational load (FLOPs) of standard attention mechanisms, but with reduced memory IO. Bifurcated attention is also compatible with multi-query attention mechanism known for reduced memory IO for KV cache, further enabling higher batch size and context length. The resulting efficiency leads to lower latency, improving suitability for real-time applications, e.g., enabling massively-parallel answer generation without substantially increasing latency, enhancing performance when integrated with post-processing techniques such as reranking.