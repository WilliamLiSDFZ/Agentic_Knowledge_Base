---
title: "Auto-Regressive Next-Token Predictors are Universal Learners"
source: "https://proceedings.mlr.press/v235/malach24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/malach24a/malach24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['auto-regressive-models', 'next-token-prediction', 'universal-approximation']
venue: "ICML 2024"
tldr: "A theoretical framework showing that auto-regressive next-token predictors are universal learners capable of expressing complex reasoning abilities."
---

# Auto-Regressive Next-Token Predictors are Universal Learners

**Source**: [https://proceedings.mlr.press/v235/malach24a.html](https://proceedings.mlr.press/v235/malach24a.html)

**TLDR**: A theoretical framework showing that auto-regressive next-token predictors are universal learners capable of expressing complex reasoning abilities.

## Abstract

Large language models display remarkable capabilities in logical and mathematical reasoning, allowing them to solve complex tasks. Interestingly, these abilities emerge in networks trained on the simple task of next-token prediction. In this work, we present a theoretical framework for studying auto-regressive next-token predictors. We demonstrate that even simple models such as linear next-token predictors, trained on Chain-of-Thought (CoT) data, can approximate any function efficiently computed by a Turing machine. We introduce a new complexity measure—length complexity—which measures the number of intermediate tokens in a CoT sequence required to approximate some target function, and analyze the interplay between length complexity and other notions of complexity. Finally, we show experimentally that simple next-token predictors, such as linear networks and shallow Multi-Layer Perceptrons (MLPs), display non-trivial performance on text generation and arithmetic tasks. Our results demonstrate that the power of today’s LLMs can be attributed, to a great extent, to the auto-regressive next-token training scheme, and not necessarily to a particular choice of architecture.