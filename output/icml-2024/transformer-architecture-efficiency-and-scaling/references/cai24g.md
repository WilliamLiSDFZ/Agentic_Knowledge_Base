---
title: "LoCoCo: Dropping In Convolutions for Long Context Compression"
source: "https://proceedings.mlr.press/v235/cai24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24g/cai24g.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['long-context', 'KV-cache', 'convolution', 'context-compression', 'LLM']
venue: "ICML 2024"
tldr: "LoCoCo compresses long contexts in LLMs by integrating convolutions with a fixed-size KV cache to reduce memory overhead during inference and fine-tuning."
---

# LoCoCo: Dropping In Convolutions for Long Context Compression

**Source**: [https://proceedings.mlr.press/v235/cai24g.html](https://proceedings.mlr.press/v235/cai24g.html)

**TLDR**: LoCoCo compresses long contexts in LLMs by integrating convolutions with a fixed-size KV cache to reduce memory overhead during inference and fine-tuning.

## Abstract

This paper tackles the memory hurdle of of processing long context sequences in Large Language Models (LLMs), by presenting a novel approach, Dropping In Convolutions for Long Context Compression (LoCoCo). LoCoCo employs only a fixed-size Key-Value (KV) cache, and can enhance efficiency in both inference and fine-tuning stages. Diverging from prior methods that selectively drop KV pairs based on heuristics, LoCoCo leverages a data-driven adaptive fusion technique, blending previous KV pairs with incoming tokens to minimize the loss of contextual information and ensure accurate attention modeling. This token integration is achieved through injecting one-dimensional convolutional kernels that dynamically calculate mixing weights for each KV cache slot. Designed for broad compatibility with existing LLM frameworks, LoCoCo allows for straightforward "drop-in" integration without needing architectural modifications, while incurring minimal tuning overhead. Experiments demonstrate that LoCoCo maintains consistently outstanding performance across various context lengths and can achieve a high context compression rate during both inference and fine-tuning phases. During inference, we successfully compressed up to $3482$ tokens into a $128$-size KV cache, while retaining comparable performance to the full sequence - an accuracy improvement of up to $0.2791$ compared to baselines at the same cache size. During post-training tuning, we also effectively extended the context length from 4K to 32K using a KV cache of fixed size 512, achieving performance similar to fine-tuning with entire sequences.