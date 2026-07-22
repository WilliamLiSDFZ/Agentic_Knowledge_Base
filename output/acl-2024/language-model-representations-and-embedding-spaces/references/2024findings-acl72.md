---
title: "SIBO: A Simple Booster for Parameter-Efficient Fine-Tuning"
source: "https://aclanthology.org/2024.findings-acl.72/"
categories: ['llm-training-alignment-and-evaluation', 'language-model-representations-and-embedding-spaces']
tags: ['parameter-efficient', 'fine-tuning', 'LoRA']
venue: "ACL 2024"
tldr: "Proposes SIBO, a simple booster for parameter-efficient fine-tuning methods like LoRA and Adapter tuning to improve performance."
---

# SIBO: A Simple Booster for Parameter-Efficient Fine-Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.72/](https://aclanthology.org/2024.findings-acl.72/)

**TLDR**: Proposes SIBO, a simple booster for parameter-efficient fine-tuning methods like LoRA and Adapter tuning to improve performance.

## Abstract

AbstractFine-tuning all parameters of large language models (LLMs) necessitates substantial computational power and extended time. Latest advancements in parameter-efficient fine-tuning (PEFT) techniques, such as Adapter tuning and LoRA, allow for adjustments to only a minor fraction of the parameters of these LLMs. Concurrently, it has been noted that the issue of over-smoothing diminishes the effectiveness of these Transformer-based LLMs, resulting in suboptimal performances in downstream tasks. In this paper, we present SIBO, which is a SImple BOoster to enhance PEFT, by injecting an initial residual. SIBO is straightforward and readily extensible to a range of state-of-the-art PEFT techniques to alleviate over-smoothing and enhance performance. Extensive experiments on 22 benchmark datasets demonstrate that SIBO significantly enhances the performance of various strong baselines, achieving up to 15.7% and 23.5% improvement over existing PEFT methods on the arithmetic and commonsense reasoning tasks, respectively.