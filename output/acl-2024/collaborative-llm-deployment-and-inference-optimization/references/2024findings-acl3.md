---
title: "AFPQ: Asymmetric Floating Point Quantization for LLMs"
source: "https://aclanthology.org/2024.findings-acl.3/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'transformer-architecture-analysis-and-design']
tags: ['quantization', 'floating-point', 'llm-inference']
venue: "ACL 2024"
tldr: "AFPQ proposes asymmetric floating-point quantization for LLMs to reduce memory and bandwidth requirements while maintaining performance."
---

# AFPQ: Asymmetric Floating Point Quantization for LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.3/](https://aclanthology.org/2024.findings-acl.3/)

**TLDR**: AFPQ proposes asymmetric floating-point quantization for LLMs to reduce memory and bandwidth requirements while maintaining performance.

## Abstract

AbstractLarge language models (LLMs) show great performance in various tasks, but face deployment challenges from limited memory capacity and bandwidth.Low-bit weight quantization can save memory and accelerate inference.Although floating-point (FP) formats show good performance in LLM quantization, they tend to perform poorly with small group sizes or sub-4 bits.We find the reason is that the absence of asymmetry in previous FP quantization makes it unsuitable for handling asymmetric value distribution of LLM weight tensors.In this work, we propose asymmetric FP quantization (AFPQ), which sets separate scales for positive and negative values.Our method leads to large accuracy improvements and can be easily plugged into other quantization methods, including GPTQ and AWQ, for better performance.Besides, no additional storage is needed compared with asymmetric integer (INT) quantization.The code is available at https://github.com/zhangsichengsjtu/AFPQ.