---
title: "Break the Sequential Dependency of LLM Inference Using Lookahead Decoding"
source: "https://proceedings.mlr.press/v235/fu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24a/fu24a.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'transformer-architecture-efficiency-and-scaling']
tags: ['LLM-inference', 'lookahead-decoding', 'parallel-decoding']
venue: "ICML 2024"
tldr: "Lookahead decoding breaks the sequential dependency in autoregressive LLM inference to achieve speedup without requiring a draft model."
---

# Break the Sequential Dependency of LLM Inference Using Lookahead Decoding

**Source**: [https://proceedings.mlr.press/v235/fu24a.html](https://proceedings.mlr.press/v235/fu24a.html)

**TLDR**: Lookahead decoding breaks the sequential dependency in autoregressive LLM inference to achieve speedup without requiring a draft model.

## Abstract

Autoregressive decoding of large language models (LLMs) is memory bandwidth bounded, resulting in high latency and significant wastes of the parallel processing power of modern accelerators. Existing methods for accelerating LLM decoding often require a draft model (e.g., speculative decoding), which is nontrivial to obtain and unable to generalize. In this paper, we introduce Lookahead decoding, an exact, parallel decoding algorithm that accelerates LLM decoding without needing auxiliary models or data stores. It allows trading per-step log(FLOPs) to reduce the number of total decoding steps, is more parallelizable on single or multiple modern accelerators, and is compatible with concurrent memory-efficient attention (e.g., FlashAttention). Our implementation of Lookahead decoding can speed up autoregressive decoding by up to 1.8x on MT-bench and 4x with strong scaling on multiple GPUs in code completion tasks. Our code is avialable at https://github.com/hao-ai-lab/LookaheadDecoding