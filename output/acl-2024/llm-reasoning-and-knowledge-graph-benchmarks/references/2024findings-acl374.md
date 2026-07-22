---
title: "Towards Robust Temporal Reasoning of Large Language Models via a Multi-Hop QA Dataset and Pseudo-Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.374/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['temporal-reasoning', 'multi-hop-qa', 'knowledge-updating']
venue: "ACL 2024"
tldr: "Constructs a multi-hop temporal QA dataset and applies pseudo-instruction tuning to improve LLMs' robustness in reasoning about evolving temporal knowledge."
---

# Towards Robust Temporal Reasoning of Large Language Models via a Multi-Hop QA Dataset and Pseudo-Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.374/](https://aclanthology.org/2024.findings-acl.374/)

**TLDR**: Constructs a multi-hop temporal QA dataset and applies pseudo-instruction tuning to improve LLMs' robustness in reasoning about evolving temporal knowledge.

## Abstract

AbstractKnowledge in the real world is being updated constantly. However, it is costly to frequently update large language models (LLMs). Therefore, it is crucial for LLMs to understand the concept of temporal knowledge. However, prior works on temporal question answering (TQA) did not emphasize multi-answer and multi-hop types of temporal reasoning. In this paper, we propose a complex temporal question-answering dataset Complex-TR that focuses on multi-answer and multi-hop temporal reasoning. Besides, we also propose a novel data augmentation strategy to improve the complex temporal reasoning capability and robustness of LLMs. We conducted experiments on multiple temporal QA datasets. Experimental results show that our method is able to improve LLMs’ performance on temporal QA benchmarks by significant margins.