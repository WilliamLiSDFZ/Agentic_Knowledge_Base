---
title: "IntactKV: Improving Large Language Model Quantization by Keeping Pivot Tokens Intact"
source: "https://aclanthology.org/2024.findings-acl.460/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'transformer-architecture-analysis-and-design']
tags: ['LLM-quantization', 'KV-cache', 'pivot-tokens', 'outliers', 'efficiency']
venue: "ACL 2024"
tldr: "IntactKV improves LLM quantization by identifying and preserving pivot tokens that act as outliers critical to model performance."
---

# IntactKV: Improving Large Language Model Quantization by Keeping Pivot Tokens Intact

**Source**: [https://aclanthology.org/2024.findings-acl.460/](https://aclanthology.org/2024.findings-acl.460/)

**TLDR**: IntactKV improves LLM quantization by identifying and preserving pivot tokens that act as outliers critical to model performance.

## Abstract

AbstractLarge language models (LLMs) excel in natural language processing but demand intensive computation. To mitigate this, various quantization methods have been explored, yet they compromise LLM performance. This paper unveils a previously overlooked type of outliers in LLMs. Such outliers are found to allocate most of the attention scores on initial tokens of input, termed as pivot tokens, which are crucial to the performance of quantized LLMs. Given that, we propose IntactKV to generate the KV cache of pivot tokens losslessly from the full-precision model. The approach is simple and easy to combine with existing quantization solutions with no extra inference overhead. Besides, IntactKV can be calibrated as additional LLM parameters to boost the quantized LLMs further with minimal training costs. Mathematical analysis also proves that IntactKV effectively reduces the upper bound of quantization error. Empirical results show that IntactKV brings consistent improvement over various quantization methods across different LLMs and downstream tasks, leading to the new state-of-the-art for LLM quantization. The codes are available at https://github.com/ruikangliu/IntactKV.