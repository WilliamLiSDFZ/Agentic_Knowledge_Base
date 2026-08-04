---
title: "GLoRe: When, Where, and How to Improve LLM Reasoning via Global and Local Refinements"
source: "https://proceedings.mlr.press/v235/havrilla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/havrilla24a/havrilla24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['llm-reasoning', 'refinement', 'outcome-reward-model']
venue: "ICML 2024"
tldr: "GLoRe proposes Stepwise Outcome Reward Models to help LLMs identify when and where to refine reasoning steps using global and local feedback."
---

# GLoRe: When, Where, and How to Improve LLM Reasoning via Global and Local Refinements

**Source**: [https://proceedings.mlr.press/v235/havrilla24a.html](https://proceedings.mlr.press/v235/havrilla24a.html)

**TLDR**: GLoRe proposes Stepwise Outcome Reward Models to help LLMs identify when and where to refine reasoning steps using global and local feedback.

## Abstract

State-of-the-art language models can exhibit reasoning refinement capabilities on math, science or coding tasks. However, recent work demonstrates that even the best models struggle to identify when and where to refine without access to external feedback. In this paper, we propose Stepwise ORMs (SORMs) which are trained, only on synthetic data, to approximate the expected future reward of the optimal policy or $V^{\star}$ as a form of Process-based reward modeling. Our experiments show that SORMs can more accurately detect incorrect reasoning steps compared to ORMs, thus enabling them to give precise step-level feedback to refinement models. We then train global refinement models, which take only the question and a draft solution as input and predict a corrected solution, and local refinement models which also take as input a critique indicating the location of the first reasoning error. We generate training data for both models synthetically by reusing data used to train the SORM. We find combining global and local refinements, using the ORM as a reranker, significantly outperforms either one individually, as well as a best of three sample baseline. With this strategy we can improve the accuracy of a LLaMA-2 13B model (already fine-tuned with RL) on GSM8K from 53% to 65% when greedily sampled.