---
title: "PICLe: Eliciting Diverse Behaviors from Large Language Models with Persona In-Context Learning"
source: "https://proceedings.mlr.press/v235/choi24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24e/choi24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['persona', 'in-context-learning', 'llm-behavior']
venue: "ICML 2024"
tldr: "PICLe uses persona-based in-context learning to elicit diverse and targeted behavioral traits from large language models."
---

# PICLe: Eliciting Diverse Behaviors from Large Language Models with Persona In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/choi24e.html](https://proceedings.mlr.press/v235/choi24e.html)

**TLDR**: PICLe uses persona-based in-context learning to elicit diverse and targeted behavioral traits from large language models.

## Abstract

Large Language Models (LLMs) are trained on massive text corpora, which are encoded with diverse personality traits. This triggers an interesting goal of eliciting a desired personality trait from the LLM, and probing its behavioral preferences. Accordingly, we formalize the persona elicitation task, aiming to customize LLM behaviors to align with a target persona. We present Persona In-Context Learning (PICLe), a novel persona elicitation framework grounded in Bayesian inference. At the core, PICLe introduces a new ICL example selection criterion based on likelihood ratio, which is designed to optimally guide the model in eliciting a specific target persona. We demonstrate the effectiveness of PICLe through extensive comparisons against baseline methods across three contemporary LLMs. Code is available at https://github.com/deeplearning-wisc/picle.