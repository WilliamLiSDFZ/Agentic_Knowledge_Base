---
title: "3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3dbcadb7beedc2afe32bb23f75dd30ec-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'self-distillation-knowledge-transfer-gains']
tags: ['parameter-efficient-finetuning', 'rotary-adaptation', 'lora']
venue: "NeurIPS 2024"
tldr: "Introduces a 2D rotary adaptation method for LLMs that enables efficient finetuning, batching, and compositional composability simultaneously."
---

# 3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3dbcadb7beedc2afe32bb23f75dd30ec-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/3dbcadb7beedc2afe32bb23f75dd30ec-Abstract-Conference.html)

**TLDR**: Introduces a 2D rotary adaptation method for LLMs that enables efficient finetuning, batching, and compositional composability simultaneously.

## Abstract

Parameter-efficient finetuning (PEFT) methods effectively adapt large language models (LLMs) to diverse downstream tasks, reducing storage and GPU memory demands. Despite these advantages, several applications pose new challenges to PEFT beyond mere parameter efficiency. One notable challenge involves the efficient deployment of LLMs equipped with multiple task- or user-specific adapters, particularly when different adapters are needed for distinct requests within the same batch. Another challenge is the interpretability of LLMs, which is crucial for understanding how LLMs function. Previous studies introduced various approaches to address different challenges. In this paper, we introduce a novel method, RoAd, which employs a straightforward 2D rotation to adapt LLMs and addresses all the above challenges: (1) RoAd is remarkably parameter-efficient, delivering optimal performance on GLUE, eight commonsense reasoning tasks and four arithmetic reasoning tasks with <0.1% trainable parameters; (2) RoAd facilitates the efficient serving of requests requiring different adapters within a batch, with an overhead comparable to element-wise multiplication instead of batch matrix multiplication; (3) RoAd enhances LLM's interpretability through integration within a framework of distributed interchange intervention, demonstrated via composition experiments.