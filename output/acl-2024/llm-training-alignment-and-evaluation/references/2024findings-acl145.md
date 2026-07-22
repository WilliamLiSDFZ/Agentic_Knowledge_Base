---
title: "LM-Cocktail: Resilient Tuning of Language Models via Model Merging"
source: "https://aclanthology.org/2024.findings-acl.145/"
pdf_url: ""
categories: ['continual-learning-for-nlp-tasks', 'llm-training-alignment-and-evaluation']
tags: ['model-merging', 'fine-tuning', 'catastrophic-forgetting', 'language-models', 'resilience']
venue: "ACL 2024"
tldr: "Proposes LM-Cocktail, a model merging approach to preserve general task performance while fine-tuning language models for specific domains."
---

# LM-Cocktail: Resilient Tuning of Language Models via Model Merging

**Source**: [https://aclanthology.org/2024.findings-acl.145/](https://aclanthology.org/2024.findings-acl.145/)

**TLDR**: Proposes LM-Cocktail, a model merging approach to preserve general task performance while fine-tuning language models for specific domains.

## Abstract

AbstractThe pre-trained language models are continually fine-tuned to better support downstream applications. However, this operation may result in significant performance degeneration on general tasks beyond the targeted domain. To overcome this problem, we propose LM-Cocktail which enables the fine-tuned model to stay resilient in general perspectives. Our method is conducted in the form of model merging, where the fine-tuned language model is merged with the pre-trained base model or the peer models from other domains through weighted average. Despite simplicity, LM-Cocktail is surprisingly effective: the resulted model is able to achieve a strong empirical performance in the whole scope of general tasks while preserving a superior capacity in its targeted domain.