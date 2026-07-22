---
title: "AFLoRA: Adaptive Freezing of Low Rank Adaptation in Parameter Efficient Fine-Tuning of Large Models"
source: "https://aclanthology.org/2024.acl-short.16/"
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['parameter-efficient-fine-tuning', 'LoRA', 'adaptive-freezing', 'low-rank-adaptation', 'LLM']
venue: "ACL 2024"
tldr: "Introduces AFLoRA, a parameter-efficient fine-tuning method that adaptively freezes low-rank adaptation matrices during training."
---

# AFLoRA: Adaptive Freezing of Low Rank Adaptation in Parameter Efficient Fine-Tuning of Large Models

**Source**: [https://aclanthology.org/2024.acl-short.16/](https://aclanthology.org/2024.acl-short.16/)

**TLDR**: Introduces AFLoRA, a parameter-efficient fine-tuning method that adaptively freezes low-rank adaptation matrices during training.

## Abstract

AbstractWe present a novel Parameter-Efficient Fine-Tuning (PEFT) method, dubbed as Adaptive Freezing of Low-Rank Adaptation (AFLoRA). Specifically, for each pre-trained frozen weight tensor, we add a parallel path of trainable low-rank matrices, namely a down-projection and an up-projection matrix, each of which is followed by a feature transformation vector. Based on a novel freezing score, we incrementally freeze these projection matrices during fine-tuning to reduce the computation and alleviate over-fitting. Our experimental results demonstrate that we can achieve state-of-the-art performance with an average improvement of up to 0.85% as evaluated on the GLUE benchmark while yielding up to 9.5× fewer average trainable parameters. While compared in terms of runtime, AFLoRA can yield up to 1.86× improvement as opposed to similar PEFT alternatives. Besides the practical utility of our approach, we provide insights on the trainability requirements of LoRA paths at different modules and the freezing schedule for the different projection matrices.