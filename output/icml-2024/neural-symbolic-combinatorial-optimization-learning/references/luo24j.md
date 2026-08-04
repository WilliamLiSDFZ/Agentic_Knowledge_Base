---
title: "End-to-End Neuro-Symbolic Reinforcement Learning with Textual Explanations"
source: "https://proceedings.mlr.press/v235/luo24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24j/luo24j.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'ai-explainability-uncertainty-human-decision-making']
tags: ['neuro-symbolic', 'reinforcement-learning', 'explainability', 'textual-explanations']
venue: "ICML 2024"
tldr: "An end-to-end neuro-symbolic RL framework that uses textual explanations to refine structured state representations for interpretable decision-making."
---

# End-to-End Neuro-Symbolic Reinforcement Learning with Textual Explanations

**Source**: [https://proceedings.mlr.press/v235/luo24j.html](https://proceedings.mlr.press/v235/luo24j.html)

**TLDR**: An end-to-end neuro-symbolic RL framework that uses textual explanations to refine structured state representations for interpretable decision-making.

## Abstract

Neuro-symbolic reinforcement learning (NS-RL) has emerged as a promising paradigm for explainable decision-making, characterized by the interpretability of symbolic policies. NS-RL entails structured state representations for tasks with visual observations, but previous methods cannot refine the structured states with rewards due to a lack of efficiency. Accessibility also remains an issue, as extensive domain knowledge is required to interpret symbolic policies. In this paper, we present a neuro-symbolic framework for jointly learning structured states and symbolic policies, whose key idea is to distill the vision foundation model into an efficient perception module and refine it during policy learning. Moreover, we design a pipeline to prompt GPT-4 to generate textual explanations for the learned policies and decisions, significantly reducing users’ cognitive load to understand the symbolic policies. We verify the efficacy of our approach on nine Atari tasks and present GPT-generated explanations for policies and decisions.