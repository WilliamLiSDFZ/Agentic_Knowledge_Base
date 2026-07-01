---
title: "Base of RoPE Bounds Context Length"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9f12dd32d552f3ad9eaa0e9dfec291be-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'deep-learning-optimization-and-generalization-theory']
tags: ['RoPE', 'context-length', 'position-embedding']
venue: "NeurIPS 2024"
tldr: "Theoretically analyzes how the base of Rotary Position Embedding bounds the effective context length of large language models."
---

# Base of RoPE Bounds Context Length

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9f12dd32d552f3ad9eaa0e9dfec291be-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/9f12dd32d552f3ad9eaa0e9dfec291be-Abstract-Conference.html)

**TLDR**: Theoretically analyzes how the base of Rotary Position Embedding bounds the effective context length of large language models.

## Abstract

Position embedding is a core component of current Large Language Models (LLMs). Rotary position embedding (RoPE), a technique that encodes the position information with a rotation matrix, has been the de facto choice for position embedding in many LLMs, such as the Llama series. RoPE has been further utilized to extend long context capability, which is roughly based on adjusting the \textit{base} parameter of RoPE to mitigate out-of-distribution (OOD) problems in position embedding. However, in this paper, we find that LLMs may obtain a superficial long-context ability based on the OOD theory. We revisit the role of RoPE in LLMs and propose a novel property of long-term decay, we derive that the \textit{base of RoPE bounds context length}: there is an absolute lower bound for the base value to obtain certain context length capability. Our work reveals the relationship between context length and RoPE base both theoretically and empirically, which may shed light on future long context training.