---
title: "Linear Alignment: A Closed-form Solution for Aligning Human Preferences without Tuning and Feedback"
source: "https://proceedings.mlr.press/v235/gao24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24f/gao24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['LLM-alignment', 'RLHF', 'closed-form-solution', 'human-preferences']
venue: "ICML 2024"
tldr: "Linear Alignment provides a closed-form solution to align LLMs with human preferences without requiring iterative fine-tuning or human feedback during training."
---

# Linear Alignment: A Closed-form Solution for Aligning Human Preferences without Tuning and Feedback

**Source**: [https://proceedings.mlr.press/v235/gao24f.html](https://proceedings.mlr.press/v235/gao24f.html)

**TLDR**: Linear Alignment provides a closed-form solution to align LLMs with human preferences without requiring iterative fine-tuning or human feedback during training.

## Abstract

The success of AI assistants based on Language Models (LLMs) hinges on Reinforcement Learning from Human Feedback (RLHF) to comprehend and align with user intentions. However, traditional alignment algorithms, such as PPO, are hampered by complex annotation and training requirements. This reliance limits the applicability of RLHF and hinders the development of professional assistants tailored to diverse human preferences. In this work, we introduce Linear Alignment, a novel algorithm that aligns language models with human preferences in one single inference step, eliminating the reliance on data annotation and model training. Linear alignment incorporates a new parameterization for policy optimization under divergence constraints, which enables the extraction of optimal policy in a closed-form manner and facilitates the direct estimation of the aligned response. Extensive experiments on both general and personalized preference datasets demonstrate that linear alignment significantly enhances the performance and efficiency of LLM alignment across diverse scenarios.