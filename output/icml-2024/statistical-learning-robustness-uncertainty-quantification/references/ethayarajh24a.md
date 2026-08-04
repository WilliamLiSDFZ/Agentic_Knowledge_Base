---
title: "Model Alignment as Prospect Theoretic Optimization"
source: "https://proceedings.mlr.press/v235/ethayarajh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ethayarajh24a/ethayarajh24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['rlhf', 'prospect-theory', 'human-feedback', 'loss-aversion', 'llm-alignment']
venue: "ICML 2024"
tldr: "Demonstrates that LLM alignment objectives implicitly encode prospect-theoretic human biases and proposes optimization under explicit prospect theory framing."
---

# Model Alignment as Prospect Theoretic Optimization

**Source**: [https://proceedings.mlr.press/v235/ethayarajh24a.html](https://proceedings.mlr.press/v235/ethayarajh24a.html)

**TLDR**: Demonstrates that LLM alignment objectives implicitly encode prospect-theoretic human biases and proposes optimization under explicit prospect theory framing.

## Abstract

Kahneman & Tversky’s $\textit{prospect theory}$ tells us that humans perceive random variables in a biased but well-defined manner (1992); for example, humans are famously loss-averse. We show that objectives for aligning LLMs with human feedback implicitly incorporate many of these biases—the success of these objectives (e.g., DPO) over cross-entropy minimization can partly be ascribed to them belonging to a family of loss functions that we call $\textit{human-aware losses}$ (HALOs). However, the utility functions these methods attribute to humans still differ from those in the prospect theory literature. Using a Kahneman-Tversky model of human utility, we propose a HALO that directly maximizes the utility of generations instead of maximizing the log-likelihood of preferences, as current methods do. We call this approach KTO, and it matches or exceeds the performance of preference-based methods at scales from 1B to 30B, despite only learning from a binary signal of whether an output is desirable. More broadly, our work suggests that there is no one HALO that is universally superior; the best loss depends on the inductive biases most appropriate for a given setting, an oft-overlooked consideration.