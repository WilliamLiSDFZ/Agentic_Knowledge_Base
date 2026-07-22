---
title: "PEMT: Multi-Task Correlation Guided Mixture-of-Experts Enables Parameter-Efficient Transfer Learning"
source: "https://aclanthology.org/2024.findings-acl.410/"
categories: ['transformer-architecture-analysis-and-design', 'continual-learning-for-nlp-tasks']
tags: ['parameter-efficient', 'mixture-of-experts', 'multi-task']
venue: "ACL 2024"
tldr: "PEMT uses multi-task correlation-guided mixture-of-experts to enable parameter-efficient transfer learning across NLP tasks."
---

# PEMT: Multi-Task Correlation Guided Mixture-of-Experts Enables Parameter-Efficient Transfer Learning

**Source**: [https://aclanthology.org/2024.findings-acl.410/](https://aclanthology.org/2024.findings-acl.410/)

**TLDR**: PEMT uses multi-task correlation-guided mixture-of-experts to enable parameter-efficient transfer learning across NLP tasks.

## Abstract

AbstractParameter-efficient fine-tuning (PEFT) has emerged as an effective method for adapting pre-trained language models to various tasks efficiently. Recently, there has been a growing interest in transferring knowledge from one or multiple tasks to the downstream target task to achieve performance improvements. However, current approaches typically either train adapters on individual tasks or distill shared knowledge from source tasks, failing to fully exploit task-specific knowledge and the correlation between source and target tasks. To overcome these limitations, we propose PEMT, a novel parameter-efficient fine-tuning framework based on multi-task transfer learning. PEMT extends the mixture-of-experts (MoE) framework to capture the transferable knowledge as a weighted combination of adapters trained on source tasks. These weights are determined by a gated unit, measuring the correlation between the target and each source task using task description prompt vectors. To fully exploit the task-specific knowledge, we also propose the Task Sparsity Loss to improve the sparsity of the gated unit. We conduct experiments on a broad range of tasks over 17 datasets. The experimental results demonstrate our PEMT yields stable improvements over full fine-tuning, and state-of-the-art PEFT and knowledge transferring methods on various tasks. The results highlight the effectiveness of our method which is capable of sufficiently exploiting the knowledge and correlation features across multiple tasks.