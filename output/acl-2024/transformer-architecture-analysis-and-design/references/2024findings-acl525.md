---
title: "ResLoRA: Identity Residual Mapping in Low-Rank Adaption"
source: "https://aclanthology.org/2024.findings-acl.525/"
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['parameter-efficient-fine-tuning', 'LoRA', 'residual-mapping']
venue: "ACL 2024"
tldr: "ResLoRA adds identity residual mappings to LoRA to accelerate and improve LLM fine-tuning convergence."
---

# ResLoRA: Identity Residual Mapping in Low-Rank Adaption

**Source**: [https://aclanthology.org/2024.findings-acl.525/](https://aclanthology.org/2024.findings-acl.525/)

**TLDR**: ResLoRA adds identity residual mappings to LoRA to accelerate and improve LLM fine-tuning convergence.

## Abstract

AbstractAs one of the most popular parameter-efficient fine-tuning (PEFT) methods, low-rank adaptation (LoRA) is commonly applied to fine-tune large language models (LLMs). However, updating the weights of LoRA blocks effectively and expeditiously is challenging due to the long calculation path in the original model. To address this, we propose ResLoRA, an improved framework of LoRA. By adding residual paths during training and using merging approaches to eliminate these extra paths during inference, our method can achieve better results in fewer training steps without any extra trainable parameters or inference cost compared to LoRA. The experiments on NLG, NLU, and text-to-image tasks demonstrate the effectiveness of our method. To the best of our knowledge, ResLoRA is the first work that combines the residual path with LoRA. The code of our method is available at [this url](https://github.com/microsoft/LMOps/tree/main/reslora).