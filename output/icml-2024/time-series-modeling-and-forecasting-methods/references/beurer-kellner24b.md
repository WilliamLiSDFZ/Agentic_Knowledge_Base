---
title: "Prompt Sketching for Large Language Models"
source: "https://proceedings.mlr.press/v235/beurer-kellner24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/beurer-kellner24b/beurer-kellner24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'time-series-modeling-and-forecasting-methods']
tags: ['prompt-engineering', 'LLMs', 'constrained-generation', 'multi-step-prompting', 'decoding']
venue: "ICML 2024"
tldr: "Introduces prompt sketching for LLMs to jointly optimize multi-step prompting strategies by making the model aware of follow-up prompts during decoding."
---

# Prompt Sketching for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/beurer-kellner24b.html](https://proceedings.mlr.press/v235/beurer-kellner24b.html)

**TLDR**: Introduces prompt sketching for LLMs to jointly optimize multi-step prompting strategies by making the model aware of follow-up prompts during decoding.

## Abstract

Many recent prompting strategies for large language models (LLMs) query the model multiple times sequentially – first to produce intermediate results and then the final answer. However, using these methods, both decoder and model are unaware of potential follow-up prompts, leading to disconnected and undesirably wordy intermediate responses. In this work, we address this issue by proposing prompt sketching, a new prompting paradigm in which an LLM does not only respond by completing a prompt, but by predicting values for multiple variables in a template. This way, sketching grants users more control over the generation process, e.g., by providing a reasoning framework via intermediate instructions, leading to better overall results. The key idea enabling sketching with existing, autoregressive models is to adapt the decoding procedure to also score follow-up instructions during text generation, thus optimizing overall template likelihood in inference. Our experiments show that in a zero-shot setting, prompt sketching outperforms existing, sequential prompting schemes such as direct asking or chain-of-thought on 7 out of 8 LLM benchmarking tasks, including state tracking, arithmetic reasoning, and general question answering. To facilitate future use, we release a number of generic, yet effective sketches applicable to many tasks, and an open source library called dclib, powering our sketch-aware decoders as part of https://github.com/eth-sri/lmql.