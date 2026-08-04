---
title: "CaM: Cache Merging for Memory-efficient LLMs Inference"
source: "https://proceedings.mlr.press/v235/zhang24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24n/zhang24n.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['KV-cache', 'LLM-inference', 'memory-efficiency']
venue: "ICML 2024"
tldr: "CaM reduces LLM inference memory by merging rather than evicting KV caches, preserving information from less-attended tokens."
---

# CaM: Cache Merging for Memory-efficient LLMs Inference

**Source**: [https://proceedings.mlr.press/v235/zhang24n.html](https://proceedings.mlr.press/v235/zhang24n.html)

**TLDR**: CaM reduces LLM inference memory by merging rather than evicting KV caches, preserving information from less-attended tokens.

## Abstract

Despite the exceptional performance of Large Language Models (LLMs), the substantial volume of key-value (KV) pairs cached during inference presents a barrier to their efficient deployment. To ameliorate this, recent works have aimed to selectively eliminate these caches, informed by the attention scores of associated tokens. However, such cache eviction invariably leads to output perturbation, regardless of the token choice. This perturbation escalates with the compression ratio, which can precipitate a marked deterioration in LLM inference performance. This paper introduces Cache Merging (CaM) as a solution to mitigate this challenge. CaM adaptively merges to-be-evicted caches into the remaining ones, employing a novel sampling strategy governed by the prominence of attention scores within discarded locations. In this manner, CaM enables memory-efficient LLMs to preserve critical token information, even obviating the need to maintain their corresponding caches. Extensive experiments utilizing LLaMA, OPT, and GPT-NeoX across various benchmarks corroborate CaM’s proficiency in bolstering the performance of memory-efficient LLMs. Code is released at https://github.com/zyxxmu/cam.