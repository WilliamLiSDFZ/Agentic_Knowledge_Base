---
title: "A Comprehensive Evaluation of Quantization Strategies for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.726/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['quantization', 'model-compression', 'evaluation', 'deployment-efficiency']
venue: "ACL 2024"
tldr: "Provides a comprehensive evaluation of quantization strategies for large language models across diverse tasks and settings."
---

# A Comprehensive Evaluation of Quantization Strategies for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.726/](https://aclanthology.org/2024.findings-acl.726/)

**TLDR**: Provides a comprehensive evaluation of quantization strategies for large language models across diverse tasks and settings.

## Abstract

AbstractIncreasing the number of parameters in large language models (LLMs) usually improves performance in downstream tasks but raises compute and memory costs, making deployment difficult in resource-limited settings. Quantization techniques, which reduce the bits needed for model weights or activations with minimal performance loss, have become popular due to the rise of LLMs. However, most quantization studies use pre-trained LLMs, and the impact of quantization on instruction-tuned LLMs and the relationship between perplexity and benchmark performance of quantized LLMs are not well understood. Evaluation of quantized LLMs is often limited to language modeling and a few classification tasks, leaving their performance on other benchmarks unclear. To address these gaps, we propose a structured evaluation framework consisting of three critical dimensions: (1) knowledge & capacity, (2) alignment, and (3) efficiency, and conduct extensive experiments across ten diverse benchmarks. Our experimental results indicate that LLMs with 4-bit quantization can retain performance comparable to their non-quantized counterparts, and perplexity can serve as a proxy metric for quantized LLMs on most benchmarks. Furthermore, quantized LLMs with larger parameter scales can outperform smaller LLMs. Despite the memory savings achieved through quantization, it can also slow down the inference speed of LLMs. Consequently, substantial engineering efforts and hardware support are imperative to achieve a balanced optimization of decoding speed and memory consumption in the context of quantized LLMs.