---
title: "Iterative Data Smoothing: Mitigating Reward Overfitting and Overoptimization in RLHF"
source: "https://proceedings.mlr.press/v235/zhu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24e/zhu24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['RLHF', 'reward-model', 'overfitting', 'overoptimization', 'data-smoothing']
venue: "ICML 2024"
tldr: "This paper proposes iterative data smoothing to mitigate reward model overfitting and overoptimization in reinforcement learning from human feedback."
---

# Iterative Data Smoothing: Mitigating Reward Overfitting and Overoptimization in RLHF

**Source**: [https://proceedings.mlr.press/v235/zhu24e.html](https://proceedings.mlr.press/v235/zhu24e.html)

**TLDR**: This paper proposes iterative data smoothing to mitigate reward model overfitting and overoptimization in reinforcement learning from human feedback.

## Abstract

Reinforcement Learning from Human Feedback (RLHF) is a pivotal technique that aligns language models closely with human-centric values. The initial phase of RLHF involves learning human values using a reward model from ranking data. It is observed that the performance of the reward model degrades after one epoch of training, and optimizing too much against the learned reward model eventually hinders the true objective. This paper analyzes potential reasons behind the issues, and designs improved reward learning algorithm termed ’Iterative Data Smoothing’ (IDS). The core idea is that during each training epoch, we not only update the model with the data, but also update the date using the model, replacing hard labels with soft labels. Our empirical findings highlight the superior performance of this approach over the traditional methods.