---
title: "Degeneration-free Policy Optimization: RL Fine-Tuning for Language Models without Degeneration"
source: "https://proceedings.mlr.press/v235/jang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jang24b/jang24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['RL-fine-tuning', 'language-models', 'degeneration', 'policy-optimization', 'reward-maximization']
venue: "ICML 2024"
tldr: "A degeneration-free policy optimization method for RL fine-tuning of language models that maximizes task scores without reward hacking or output degeneration."
---

# Degeneration-free Policy Optimization: RL Fine-Tuning for Language Models without Degeneration

**Source**: [https://proceedings.mlr.press/v235/jang24b.html](https://proceedings.mlr.press/v235/jang24b.html)

**TLDR**: A degeneration-free policy optimization method for RL fine-tuning of language models that maximizes task scores without reward hacking or output degeneration.

## Abstract

As the pre-training objectives (e.g., next token prediction) of language models (LMs) are inherently not aligned with task scores, optimizing LMs to achieve higher downstream task scores is essential. One of the promising approaches is to fine-tune LMs through reinforcement learning (RL). However, conventional RL methods based on PPO and a penalty of KL divergence are vulnerable to text degeneration where LMs do not generate natural texts anymore after RL fine-tuning. To address this problem, we provide Degeneration-free Policy Optimization (DfPO) that can fine-tune LMs to generate texts that achieve improved downstream task scores, while preserving the ability to generate natural texts. To achieve this, we introduce KL-masking which masks out the actions that potentially cause deviation from the reference policy when its likelihood is increased or decreased. Then, we devise truncated advantage functions for separately performing likelihood maximization and minimization to improve the task performance. In the experiments, we provide the results of DfPO and baseline algorithms on various generative NLP tasks including text continuation, text detoxification, and commonsense generation. Our experiments demonstrate that DfPO successfully improves the downstream task scores while preserving the ability to generate natural texts, without requiring additional hyperparameter search.