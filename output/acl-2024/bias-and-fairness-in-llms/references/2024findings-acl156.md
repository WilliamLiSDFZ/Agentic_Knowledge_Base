---
title: "The Language Barrier: Dissecting Safety Challenges of LLMs in Multilingual Contexts"
source: "https://aclanthology.org/2024.findings-acl.156/"
categories: ['llm-security-robustness-and-detection', 'bias-and-fairness-in-llms']
tags: ['multilingual-safety', 'llm-alignment', 'jailbreak']
venue: "ACL 2024"
tldr: "This paper analyzes how LLM safety challenges vary across languages and proposes approaches to address multilingual alignment gaps."
---

# The Language Barrier: Dissecting Safety Challenges of LLMs in Multilingual Contexts

**Source**: [https://aclanthology.org/2024.findings-acl.156/](https://aclanthology.org/2024.findings-acl.156/)

**TLDR**: This paper analyzes how LLM safety challenges vary across languages and proposes approaches to address multilingual alignment gaps.

## Abstract

AbstractAs the influence of large language models (LLMs) spans across global communities, their safety challenges in multilingual settings become paramount for alignment research. This paper examines the variations in safety challenges faced by LLMs across different languages and discusses approaches to alleviating such concerns. By comparing how state-of-the-art LLMs respond to the same set of malicious prompts written in higher- vs. lower-resource languages,we observe that (1) LLMs tend to generate unsafe responses much more often when a malicious prompt is written in a lower-resource language, and (2) LLMs tend to generate more irrelevant responses to malicious prompts in lower-resource languages. To understand where the discrepancy can be attributed, we study the effect of instruction tuning with reinforcement learning from human feedback (RLHF) or supervised finetuning (SFT) on the HH-RLHF dataset. Surprisingly, while training with high-resource languages improves model alignment, training in lower-resource languages yields minimal improvement. This suggests that the bottleneck of cross-lingual alignment is rooted in the pretraining stage. Our findings highlight the challenges in cross-lingual LLM safety, and we hope they inform future research in this direction.