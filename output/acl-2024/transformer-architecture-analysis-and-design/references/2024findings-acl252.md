---
title: "E2-LLM: Efficient and Extreme Length Extension of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.252/"
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['long-context', 'LLM-extension', 'efficient-training']
venue: "ACL 2024"
tldr: "E2-LLM efficiently extends LLM context length to extreme lengths with minimal additional training cost and no long-context data requirement."
---

# E2-LLM: Efficient and Extreme Length Extension of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.252/](https://aclanthology.org/2024.findings-acl.252/)

**TLDR**: E2-LLM efficiently extends LLM context length to extreme lengths with minimal additional training cost and no long-context data requirement.

## Abstract

AbstractTraining Large Language Models (LLMs) to process extensive context lengths incurs prohibitive computational costs. Prevailing techniques for extending context capabilities in LLMs typically require not only additional training procedures but also access to datasets with long context (e.g., sequences of 32K tokens), presupposing substantial GPU expenditures. To address the aforementioned issues, we introduce a novel solution named Efficient and Extreme length extension for Large Language Models (E2-LLM). E2-LLM entails a singular training process over considerably short sequences (e.g., 4K tokens), which greatly mitigates the cost of continual-pretraining or fine-tuning. Within the training phase, we incorporate a dual augmentation strategy with Rotary Position Embeddings (RoPE) that adjusts the scale and position indices across distinct training samples. E 2 -LLM is meticulously designed to enhance the model’s robustness to diverse relative positions. The experimental results on multiple benchmark datasets demonstrate the superior performance of E 2 -LLM on demanding tasks of processing long contexts.