---
title: "Premise Order Matters in Reasoning with Large Language Models"
source: "https://proceedings.mlr.press/v235/chen24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24i/chen24i.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['LLM-reasoning', 'premise-ordering', 'robustness', 'logical-reasoning']
venue: "ICML 2024"
tldr: "LLMs are shown to be brittle to the ordering of premises in reasoning tasks, degrading performance despite logically equivalent inputs."
---

# Premise Order Matters in Reasoning with Large Language Models

**Source**: [https://proceedings.mlr.press/v235/chen24i.html](https://proceedings.mlr.press/v235/chen24i.html)

**TLDR**: LLMs are shown to be brittle to the ordering of premises in reasoning tasks, degrading performance despite logically equivalent inputs.

## Abstract

Large language models (LLMs) have accomplished remarkable reasoning performance in various domains. However, in the domain of reasoning tasks, we discover a frailty: LLMs are surprisingly brittle to the ordering of the premises, despite the fact that such ordering does not alter the underlying task. In particular, we observe that LLMs achieve the best performance when the premise order aligns with the context required in intermediate reasoning steps. For example, in deductive reasoning tasks, presenting the premises in the same order as the ground truth proof in the prompt (as opposed to random ordering) drastically increases the model’s accuracy. We first examine the effect of premise ordering on deductive reasoning on a variety of LLMs, and our evaluation shows that even if the model performance is decent on the optimal order, permuting the premise order can cause a performance drop of over 30%. In addition, we release the benchmark R-GSM, based on GSM8K, to examine the ordering effect for mathematical problem-solving, and we again observe a significant drop in accuracy, relative to the original GSM8K benchmark.