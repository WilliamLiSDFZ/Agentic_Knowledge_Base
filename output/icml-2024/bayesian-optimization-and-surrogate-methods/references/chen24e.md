---
title: "InstructZero: Efficient Instruction Optimization for Black-Box Large Language Models"
source: "https://proceedings.mlr.press/v235/chen24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24e/chen24e.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'large-language-model-alignment-and-capabilities']
tags: ['instruction-optimization', 'black-box-LLMs', 'Bayesian-optimization', 'prompt-tuning']
venue: "ICML 2024"
tldr: "InstructZero optimizes instructions for black-box LLMs by using a soft prompt in an open-source LLM with Bayesian optimization in the intrinsic space."
---

# InstructZero: Efficient Instruction Optimization for Black-Box Large Language Models

**Source**: [https://proceedings.mlr.press/v235/chen24e.html](https://proceedings.mlr.press/v235/chen24e.html)

**TLDR**: InstructZero optimizes instructions for black-box LLMs by using a soft prompt in an open-source LLM with Bayesian optimization in the intrinsic space.

## Abstract

Large language models (LLMs) are instruction followers but the performance varies under different instructions. It is challenging to create the best instruction, especially for black-box LLMs on which backpropagation is forbidden. Instead of directly optimizing the discrete instruction, we optimize a low-dimensional soft prompt applied to an open-source LLM to generate the instruction for the black-box LLM. In each optimization step of the proposed method InstructZero, a soft prompt is converted into an instruction by the open-source LLM, which is then submitted to the black-box LLM for zero-shot evaluation, whose result is sent to Bayesian optimization to produce new soft prompts improving the zero-shot performance. We evaluate InstructZero on different combinations of open-source LLMs and APIs including Vicuna and ChatGPT. InstructZero outperforms SOTA auto-instruction methods across a variety of downstream tasks.