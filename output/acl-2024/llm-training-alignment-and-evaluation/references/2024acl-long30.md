---
title: "GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis"
source: "https://aclanthology.org/2024.acl-long.30/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['jailbreak-detection', 'gradient-analysis', 'safety']
venue: "ACL 2024"
tldr: "GradSafe detects jailbreak prompts by analyzing safety-critical gradient patterns without requiring extensive fine-tuning or labeled data."
---

# GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis

**Source**: [https://aclanthology.org/2024.acl-long.30/](https://aclanthology.org/2024.acl-long.30/)

**TLDR**: GradSafe detects jailbreak prompts by analyzing safety-critical gradient patterns without requiring extensive fine-tuning or labeled data.

## Abstract

AbstractLarge Language Models (LLMs) face threats from jailbreak prompts. Existing methods for detecting jailbreak prompts are primarily online moderation APIs or finetuned LLMs. These strategies, however, often require extensive and resource-intensive data collection and training processes. In this study, we propose GradSafe, which effectively detects jailbreak prompts by scrutinizing the gradients of safety-critical parameters in LLMs. Our method is grounded in a pivotal observation: the gradients of an LLM’s loss for jailbreak prompts paired with compliance response exhibit similar patterns on certain safety-critical parameters. In contrast, safe prompts lead to different gradient patterns. Building on this observation, GradSafe analyzes the gradients from prompts (paired with compliance responses) to accurately detect jailbreak prompts. We show that GradSafe, applied to Llama-2 without further training, outperforms Llama Guard—despite its extensive finetuning with a large dataset—in detecting jailbreak prompts. This superior performance is consistent across both zero-shot and adaptation scenarios, as evidenced by our evaluations on ToxicChat and XSTest. The source code is available at https://github.com/xyq7/GradSafe.