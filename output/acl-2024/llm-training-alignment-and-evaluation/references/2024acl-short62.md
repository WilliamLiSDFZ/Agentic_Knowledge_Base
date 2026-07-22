---
title: "Aligning Large Language Models via Fine-grained Supervision"
source: "https://aclanthology.org/2024.acl-short.62/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['alignment', 'fine-grained-supervision', 'RLHF']
venue: "ACL 2024"
tldr: "Introduces fine-grained token-level supervision to improve LLM alignment beyond standard RLHF approaches."
---

# Aligning Large Language Models via Fine-grained Supervision

**Source**: [https://aclanthology.org/2024.acl-short.62/](https://aclanthology.org/2024.acl-short.62/)

**TLDR**: Introduces fine-grained token-level supervision to improve LLM alignment beyond standard RLHF approaches.

## Abstract

AbstractPre-trained large-scale language models (LLMs) excel at producing coherent articles, yet their outputs may be untruthful, toxic, or fail to align with user expectations. Current approaches focus on using reinforcement learning with human feedback (RLHF) to improve model alignment, which works by transforming coarse human preferences of LLM outputs into a feedback signal that guides the model learning process. However, because this approach operates on sequence-level feedback, it lacks the precision to identify the exact parts of the output affecting user preferences. To address this gap, we propose a method to enhance LLM alignment through fine-grained token-level supervision. Specifically, we ask annotators to minimally edit less preferred responses within the standard reward modeling dataset to make them more favorable, ensuring changes are made only where necessary while retaining most of the original content. The refined dataset is used to train a token-level reward model, which is then used for training our fine-grained Proximal Policy Optimization (PPO) model. Our experiment results demonstrate that this approach can improve LLM performance by up to 5.1% in terms of win rate against the reference model, compared with the traditional PPO model.