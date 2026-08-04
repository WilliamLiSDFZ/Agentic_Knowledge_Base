---
title: "Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications"
source: "https://proceedings.mlr.press/v235/wei24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wei24f/wei24f.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['llm-safety', 'pruning', 'low-rank-modification']
venue: "ICML 2024"
tldr: "This paper reveals the brittleness of LLM safety alignment by showing pruning and low-rank modifications can easily bypass safety mechanisms."
---

# Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications

**Source**: [https://proceedings.mlr.press/v235/wei24f.html](https://proceedings.mlr.press/v235/wei24f.html)

**TLDR**: This paper reveals the brittleness of LLM safety alignment by showing pruning and low-rank modifications can easily bypass safety mechanisms.

## Abstract

Large language models (LLMs) show inherent brittleness in their safety mechanisms, as evidenced by their susceptibility to jailbreaking and even non-malicious fine-tuning. This study explores this brittleness of safety alignment by leveraging pruning and low-rank modifications. We develop methods to identify critical regions that are vital for safety guardrails, and that are disentangled from utility-relevant regions at both the neuron and rank levels. Surprisingly, the isolated regions we find are sparse, comprising about $3$ % at the parameter level and $2.5$ % at the rank level. Removing these regions compromises safety without significantly impacting utility, corroborating the inherent brittleness of the model’s safety mechanisms. Moreover, we show that LLMs remain vulnerable to low-cost fine-tuning attacks even when modifications to the safety-critical regions are restricted. These findings underscore the urgent need for more robust safety strategies in LLMs.