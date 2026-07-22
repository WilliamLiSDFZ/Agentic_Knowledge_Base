---
title: "Distilling Robustness into Natural Language Inference Models with Domain-Targeted Augmentation"
source: "https://aclanthology.org/2024.findings-acl.132/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['knowledge-distillation', 'natural-language-inference', 'domain-robustness']
venue: "ACL 2024"
tldr: "Improves out-of-distribution robustness of NLI models by combining knowledge distillation with domain-targeted data augmentation."
---

# Distilling Robustness into Natural Language Inference Models with Domain-Targeted Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.132/](https://aclanthology.org/2024.findings-acl.132/)

**TLDR**: Improves out-of-distribution robustness of NLI models by combining knowledge distillation with domain-targeted data augmentation.

## Abstract

AbstractKnowledge distillation optimises a smaller student model to behave similarly to a larger teacher model, retaining some of the performance benefits. While this method can improve results on in-distribution examples, it does not necessarily generalise to out-of-distribution (OOD) settings. We investigate two complementary methods for improving the robustness of the resulting student models on OOD domains. The first approach augments the distillation with generated unlabeled examples that match the target distribution. The second method upsamples data points among the training set that are similar to the target distribution. When applied on the task of natural language inference (NLI), our experiments on MNLI show that distillation with these modifications outperforms previous robustness solutions. We also find that these methods improve performance on OOD domains even beyond the target domain.