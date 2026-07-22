---
title: "Towards Safer Large Language Models through Machine Unlearning"
source: "https://aclanthology.org/2024.findings-acl.107/"
categories: ['llm-security-robustness-and-detection', 'state-memory-replay-sequence-modeling']
tags: ['machine-unlearning', 'LLM-safety', 'harmful-content', 'knowledge-removal', 'alignment']
venue: "ACL 2024"
tldr: "Applies machine unlearning techniques to large language models to reduce generation of harmful content and improve safety."
---

# Towards Safer Large Language Models through Machine Unlearning

**Source**: [https://aclanthology.org/2024.findings-acl.107/](https://aclanthology.org/2024.findings-acl.107/)

**TLDR**: Applies machine unlearning techniques to large language models to reduce generation of harmful content and improve safety.

## Abstract

AbstractThe rapid advancement of Large Language Models (LLMs) has demonstrated their vast potential across various domains, attributed to their extensive pretraining knowledge and exceptional generalizability. However, LLMs often encounter challenges in generating harmful content when faced with problematic prompts. To address this problem, existing work attempted to implement a gradient ascent based approach to prevent LLMs from producing harmful output. While these methods can be effective, they frequently impact the model utility in responding to normal prompts. To address this gap, we introduce Selective Knowledge negation Unlearning (SKU), a novel unlearning framework for LLMs, designed to eliminate harmful knowledge while preserving utility on normal prompts. Specifically, SKU is consisted of two stages: harmful knowledge acquisition stage and knowledge negation stage. The first stage aims to identify and acquire harmful knowledge within the model, whereas the second is dedicated to remove this knowledge. SKU selectively isolates and removes harmful knowledge in model parameters, ensuring the model’s performance remains robust on normal prompts. Our experiments conducted across various LLM architectures demonstrate that SKU identifies a good balance point between removing harmful information and preserving utility.