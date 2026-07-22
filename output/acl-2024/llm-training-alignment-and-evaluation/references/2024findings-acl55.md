---
title: "Exploring Mathematical Extrapolation of Large Language Models with Synthetic Data"
source: "https://aclanthology.org/2024.findings-acl.55/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['mathematical-reasoning', 'synthetic-data', 'extrapolation']
venue: "ACL 2024"
tldr: "Investigates LLMs' mathematical extrapolation ability using synthetic arithmetical puzzle problems and structured reasoning."
---

# Exploring Mathematical Extrapolation of Large Language Models with Synthetic Data

**Source**: [https://aclanthology.org/2024.findings-acl.55/](https://aclanthology.org/2024.findings-acl.55/)

**TLDR**: Investigates LLMs' mathematical extrapolation ability using synthetic arithmetical puzzle problems and structured reasoning.

## Abstract

AbstractWhile large language models (LLMs) have shown excellent capabilities in language understanding, text generation and many other tasks, they still struggle in complex multi-step reasoning problems such as mathematical reasoning. In this paper, through a newly proposed arithmetical puzzle problem, we show that the model can perform well on multi-step reasoning tasks via fine tuning on high-quality synthetic data. Experiments with the open-llama-3B model on three different test datasets show that not only the model can reach a zero-shot pass@1 at 0.44 on the in-domain dataset, it also demonstrates certain generalization capabilities on the out-of-domain datasets. Specifically, this paper has designed two out-of-domain datasets in the form of extending the numerical range and the composing components of the arithmetical puzzle problem separately. The fine-tuned model have shown encouraging performance on these two far more difficult tasks with the zero-shot pass@1 at 0.33 and 0.35 correspondingly.