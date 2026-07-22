---
title: "Small Models are Valuable Plug-ins for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.18/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'llm-training-alignment-and-evaluation']
tags: ['small-models', 'llm-plugin', 'knowledge-transfer']
venue: "ACL 2024"
tldr: "This work proposes using small fine-tuned models as plug-ins to inject task-specific knowledge into large, inaccessible language models without modifying their weights."
---

# Small Models are Valuable Plug-ins for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.18/](https://aclanthology.org/2024.findings-acl.18/)

**TLDR**: This work proposes using small fine-tuned models as plug-ins to inject task-specific knowledge into large, inaccessible language models without modifying their weights.

## Abstract

AbstractLarge language models (LLMs) such as GPT-3 and GPT-4 are powerful but their weights are often publicly unavailable and their immense sizes make the models difficult to be tuned with common hardware. As a result, effectively tuning these models with large-scale supervised data can be challenging. As an alternative, In-Context Learning (ICL) can only use a small number of supervised examples due to context length limits. In this paper, we propose Super In-Context Learning (SuperICL) which allows black-box LLMs to work with locally fine-tuned smaller models, resulting in superior performance on supervised tasks. Our experiments demonstrate that SuperICL can improve performance beyond state-of-the-art fine-tuned models while addressing the instability problem of in-context learning.