---
title: "Fast Randomized Low-Rank Adaptation of Pre-trained Language Models with PAC Regularization"
source: "https://aclanthology.org/2024.findings-acl.310/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['lora', 'parameter-efficient-fine-tuning', 'randomized-methods']
venue: "ACL 2024"
tldr: "Proposes Randomized LoRA with PAC regularization for memory-efficient fine-tuning of large language models."
---

# Fast Randomized Low-Rank Adaptation of Pre-trained Language Models with PAC Regularization

**Source**: [https://aclanthology.org/2024.findings-acl.310/](https://aclanthology.org/2024.findings-acl.310/)

**TLDR**: Proposes Randomized LoRA with PAC regularization for memory-efficient fine-tuning of large language models.

## Abstract

AbstractLow-rank adaptation (LoRA) achieves parameter efficient fine-tuning for large language models (LLMs) by decomposing the model weight update into a pair of low-rank projection matrices. Yet, the memory overhead restricts it to scale up when the model size increases. We propose Randomized LoRA (RLoRA) which adopts Randomized Walsh-Hadamard Transform to achieve significant reduction in the size of trainable parameters compared to LoRA. At the same time, it allows a PAC-Bayes regularizer to be efficiently incorporated to improve generalization. We evaluate the effectiveness of RLoRA on LLMs RoBERTa, GPT-2 and LLaMA-7B using GLUE, E2E and math reasoning benchmarks. With a much lower memory requirement, RLoRA can give similar performance as the SOTA low-rank adaptation methods for these three tasks and significantly better performance under few-shot settings.