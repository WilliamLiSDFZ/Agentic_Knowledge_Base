---
title: "Privacy-Preserving Instructions for Aligning Large Language Models"
source: "https://proceedings.mlr.press/v235/yu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24e/yu24e.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'large-language-model-alignment-and-capabilities']
tags: ['differential-privacy', 'llm-alignment', 'instruction-tuning']
venue: "ICML 2024"
tldr: "A privacy-preserving framework for aligning LLMs using differentially private user instructions annotated by human workers."
---

# Privacy-Preserving Instructions for Aligning Large Language Models

**Source**: [https://proceedings.mlr.press/v235/yu24e.html](https://proceedings.mlr.press/v235/yu24e.html)

**TLDR**: A privacy-preserving framework for aligning LLMs using differentially private user instructions annotated by human workers.

## Abstract

Service providers of large language model (LLM) applications collect user instructions in the wild and use them in further aligning LLMs with users’ intentions. These instructions, which potentially contain sensitive information, are annotated by human workers in the process. This poses a new privacy risk not addressed by the typical private optimization. To this end, we propose using synthetic instructions to replace real instructions in data annotation and model fine-tuning. Formal differential privacy is guaranteed by generating those synthetic instructions using privately fine-tuned generators. Crucial in achieving the desired utility is our novel filtering algorithm that matches the distribution of the synthetic instructions to that of the real ones. In both supervised fine-tuning and reinforcement learning from human feedback, our extensive experiments demonstrate the high utility of the final set of synthetic instructions by showing comparable results to real instructions. In supervised fine-tuning, models trained with private synthetic instructions outperform leading open-source models such as Vicuna.