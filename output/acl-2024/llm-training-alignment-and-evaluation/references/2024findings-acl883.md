---
title: "Multi-Task Transfer Matters During Instruction-Tuning"
source: "https://aclanthology.org/2024.findings-acl.883/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['instruction-tuning', 'multi-task-learning', 'in-context-learning']
venue: "ACL 2024"
tldr: "This paper investigates how multi-task transfer during instruction tuning influences in-context learning generalization in language models."
---

# Multi-Task Transfer Matters During Instruction-Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.883/](https://aclanthology.org/2024.findings-acl.883/)

**TLDR**: This paper investigates how multi-task transfer during instruction tuning influences in-context learning generalization in language models.

## Abstract

AbstractInstruction-tuning trains a language model on hundreds of tasks jointly to improve a model’s ability to learn in-context;however, the mechanisms that drive in-context learning are poorly understood and, as a result, the role of instruction-tuning on in-context generalization is poorly understood as well.In this work, we study the impact of instruction-tuning on multi-task transfer: how well a model’s parameters adapt to an unseen task via fine-tuning.We find that instruction-tuning negatively impacts a model’s transfer to unseen tasks, and that model transfer and in-context generalization are highly correlated, suggesting that this catastrophic forgetting may impact in-context learning.We study methods to improve model transfer, finding that multi-task training—how well the training tasks are optimized—can significantly impact ICL generalization; additionally, we find that continual training on unsupervised pre-training data can mitigate forgetting and improve ICL generalization as well.Finally, we demonstrate that, early into training, the impact of instruction-tuning on model transfer to tasks impacts in-context generalization on that task.Overall, we provide significant evidence that multi-task transfer is deeply connected to a model’s ability to learn a task in-context.