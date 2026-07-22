---
title: "Language Model Adaption for Reinforcement Learning with Natural Language Action Space"
source: "https://aclanthology.org/2024.acl-long.89/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'financial-reasoning-llm-benchmarks-and-datasets']
tags: ['reinforcement-learning', 'natural-language-action-space', 'language-model-adaptation']
venue: "ACL 2024"
tldr: "Adapts language models for reinforcement learning with natural language action spaces to address the curse of dimensionality."
---

# Language Model Adaption for Reinforcement Learning with Natural Language Action Space

**Source**: [https://aclanthology.org/2024.acl-long.89/](https://aclanthology.org/2024.acl-long.89/)

**TLDR**: Adapts language models for reinforcement learning with natural language action spaces to address the curse of dimensionality.

## Abstract

AbstractReinforcement learning with natural language action space often suffers from the curse of dimensionality due to the combinatorial nature of the natural language. Previous research leverages pretrained language models to capture action semantics and reduce the size of the action space. However, since pretrained models are typically trained on general corpora, there can be an unpredictable mismatch between the priors encoded in pretrained models and the characteristics of the specific RL environment. To address this issue, we propose Mutual-Information Regularized Policy Optimization, MIPO. MIPO enables implicit and dynamic reduction of the action space. Starting from the prior provided by the pretrained language model, our method dynamically adjusts the prior during the learning process based on the guidance of mutual information regularization. Theoretically, we demonstrate that this policy optimization process leads to the monotonic improvement on the mutual-information regularized RL objective. Empirically, we conduct experiments in various environments and demonstrate the effectiveness of MIPO.