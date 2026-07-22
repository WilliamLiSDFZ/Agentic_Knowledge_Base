---
title: "RA-LoRA: Rank-Adaptive Parameter-Efficient Fine-Tuning for Accurate 2-bit Quantized Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.933/"
categories: ['llm-training-alignment-and-evaluation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['quantization', 'lora', 'rank-adaptive']
venue: "ACL 2024"
tldr: "RA-LoRA introduces rank-adaptive parameter-efficient fine-tuning to improve accuracy of heavily quantized 2-bit LLMs."
---

# RA-LoRA: Rank-Adaptive Parameter-Efficient Fine-Tuning for Accurate 2-bit Quantized Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.933/](https://aclanthology.org/2024.findings-acl.933/)

**TLDR**: RA-LoRA introduces rank-adaptive parameter-efficient fine-tuning to improve accuracy of heavily quantized 2-bit LLMs.

## Abstract

AbstractDeploying large language models (LLMs) with their extensive parameters and high memory demands challenges computational efficiency, particularly in fine-tuning for specific applications with limited resources. Techniques like Low-Rank Adaptation (LoRA) help by training a smaller, modifiable extension of the base model to reduce memory usage. However, combining quantization with LoRA, especially in low-bit scenarios, can lead to performance losses due to quantization errors. Our innovative Rank-Adaptive LoRA (RA-LoRA) addresses this by dynamically adjusting the adapter’s rank using rank-subspace analysis, optimizing performance with fewer parameters. We tested RA-LoRA on state-of-the-art LLMs for 2-bit efficient fine-tuning, showing it can improve model accuracy with minimal trainable parameters, marking a leap forward in quantization-aware fine-tuning methods and highlighting the significance of rank dynamics in optimizing quantized LLMs.