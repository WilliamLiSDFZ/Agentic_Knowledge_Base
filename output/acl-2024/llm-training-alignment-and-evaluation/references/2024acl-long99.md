---
title: "Dissecting Human and LLM Preferences"
source: "https://aclanthology.org/2024.acl-long.99/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['human-preference', 'LLM-evaluation', 'alignment', 'fine-tuning', 'preference-analysis']
venue: "ACL 2024"
tldr: "Dissects and compares human and LLM preferences in model response evaluation to improve explainability and controllability of alignment."
---

# Dissecting Human and LLM Preferences

**Source**: [https://aclanthology.org/2024.acl-long.99/](https://aclanthology.org/2024.acl-long.99/)

**TLDR**: Dissects and compares human and LLM preferences in model response evaluation to improve explainability and controllability of alignment.

## Abstract

AbstractAs a relative quality comparison of model responses, human and Large Language Model (LLM) preferences serve as common alignment goals in model fine-tuning and criteria in evaluation. Yet, these preferences merely reflect broad tendencies, resulting in less explainable and controllable models with potential safety risks. In this work, we dissect the preferences of human and 32 different LLMs to understand their quantitative composition, using annotations from real-world user-model conversations for a fine-grained, scenario-wise analysis. We find that humans are less sensitive to errors, favor responses that support their stances, and show clear dislike when models admit their limits. On the contrary, advanced LLMs like GPT-4-Turbo emphasize correctness, clarity, and harmlessness more. Additionally, LLMs of similar sizes tend to exhibit similar preferences, regardless of their training methods, and fine-tuning for alignment does not significantly alter the preferences of pretrained-only LLMs. Finally, we show that preference-based evaluation can be intentionally manipulated. In both training-free and training-based settings, aligning a model with the preferences of judges boosts scores, while injecting the least preferred properties lowers them. This results in notable score shifts: up to 0.59 on MT-Bench (1-10 scale) and 31.94 on AlpacaEval 2.0 (0-100 scale), highlighting the significant impact of this strategic adaptation. We have made all resources of this project publicly available.