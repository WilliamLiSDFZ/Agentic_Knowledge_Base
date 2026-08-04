---
title: "Get More with LESS: Synthesizing Recurrence with KV Cache Compression for Efficient LLM Inference"
source: "https://proceedings.mlr.press/v235/dong24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dong24f/dong24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['KV-cache', 'LLM-inference', 'memory-efficiency', 'recurrence']
venue: "ICML 2024"
tldr: "LESS combines KV cache compression with recurrence mechanisms to reduce memory bottlenecks during LLM inference while maintaining performance."
---

# Get More with LESS: Synthesizing Recurrence with KV Cache Compression for Efficient LLM Inference

**Source**: [https://proceedings.mlr.press/v235/dong24f.html](https://proceedings.mlr.press/v235/dong24f.html)

**TLDR**: LESS combines KV cache compression with recurrence mechanisms to reduce memory bottlenecks during LLM inference while maintaining performance.

## Abstract

Many computational factors limit broader deployment of large language models. In this paper, we focus on a memory bottleneck imposed by the key-value (KV) cache, a computational shortcut that requires storing previous KV pairs during decoding. While existing KV cache methods approach this problem by pruning or evicting large swaths of relatively less important KV pairs to dramatically reduce the memory footprint of the cache, they can have limited success in tasks that require recollecting a majority of previous tokens. To alleviate this issue, we propose LESS, a simple integration of a (nearly free) constant sized cache with eviction-based cache methods, such that all tokens can be queried at later decoding steps. Its ability to retain information throughout time shows merit on a variety of tasks where we demonstrate LESS can help reduce the performance gap from caching everything, sometimes even matching it, all while being efficient. Relevant code can be found at https://github.com/hdong920/LESS.