---
title: "Preemptive Answer “Attacks” on Chain-of-Thought Reasoning"
source: "https://aclanthology.org/2024.findings-acl.876/"
categories: ['llm-security-robustness-and-detection', 'llm-agents-reasoning-and-planning']
tags: ['chain-of-thought', 'robustness', 'adversarial-prompting']
venue: "ACL 2024"
tldr: "Reveals that preemptive answer injection into prompts can significantly disrupt LLM chain-of-thought reasoning robustness."
---

# Preemptive Answer “Attacks” on Chain-of-Thought Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.876/](https://aclanthology.org/2024.findings-acl.876/)

**TLDR**: Reveals that preemptive answer injection into prompts can significantly disrupt LLM chain-of-thought reasoning robustness.

## Abstract

AbstractLarge language models (LLMs) showcase impressive reasoning capabilities when coupled with Chain-of-Thought (CoT) prompting. However, the robustness of this approach warrants further investigation. In this paper, we introduce a novel scenario termed preemptive answers, where the LLM obtains an answer before engaging in reasoning. This situation can arise inadvertently or induced by malicious users by prompt injection attacks. Experiments reveal that preemptive answers significantly impair the model’s reasoning capability across various CoT methods and a broad spectrum of datasets. To bolster the robustness of reasoning, we propose two measures aimed at mitigating this issue to some extent.