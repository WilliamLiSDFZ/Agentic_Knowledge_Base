---
title: "UNIWIZ: A Unified Large Language Model Orchestrated Wizard for Safe Knowledge Grounded Conversations"
source: "https://aclanthology.org/2024.findings-acl.102/"
categories: ['llm-security-robustness-and-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['safe-knowledge-grounded-conversation', 'llm-safety', 'hallucination-mitigation']
venue: "ACL 2024"
tldr: "Introduces UNIWIZ, a unified LLM orchestration framework balancing safety alignment and knowledge grounding to reduce unsafe and hallucinated responses."
---

# UNIWIZ: A Unified Large Language Model Orchestrated Wizard for Safe Knowledge Grounded Conversations

**Source**: [https://aclanthology.org/2024.findings-acl.102/](https://aclanthology.org/2024.findings-acl.102/)

**TLDR**: Introduces UNIWIZ, a unified LLM orchestration framework balancing safety alignment and knowledge grounding to reduce unsafe and hallucinated responses.

## Abstract

AbstractLarge Language Models (LLMs) have made significant progress in integrating safety and knowledge alignment. However, adversarial actors can manipulate these models into generating unsafe responses, and excessive safety alignment can lead to unintended hallucinations. To address these challenges, we introduce UniWiz, a novel 2-step data orchestration framework that unifies safety and knowledge data generation. We propose a “safety-priming” method to generate synthetic safety data and overcome safety bottlenecks. We also inject relevant knowledge into conversations by retrieving factual information from curated sources. UniWiz dataset consists of 17,638 quality-controlled conversations and 10,000 augmented preference data. Pretrained models fine-tuned on UniWiz show improvements across various metrics and outperform state-of-the-art instruction-tuned models trained on much larger datasets.