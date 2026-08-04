---
title: "Unveiling and Harnessing Hidden Attention Sinks: Enhancing Large Language Models without Training through Attention Calibration"
source: "https://proceedings.mlr.press/v235/yu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24l/yu24l.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-geometry-and-interpretability-research']
tags: ['attention-sinks', 'attention-calibration', 'large-language-models']
venue: "ICML 2024"
tldr: "Reveals hidden attention sinks in LLMs and proposes attention calibration to enhance model performance without additional training."
---

# Unveiling and Harnessing Hidden Attention Sinks: Enhancing Large Language Models without Training through Attention Calibration

**Source**: [https://proceedings.mlr.press/v235/yu24l.html](https://proceedings.mlr.press/v235/yu24l.html)

**TLDR**: Reveals hidden attention sinks in LLMs and proposes attention calibration to enhance model performance without additional training.

## Abstract

Attention is a fundamental component behind the remarkable achievements of large language models (LLMs). However, our current understanding of the attention mechanism, especially regarding how attention distributions are established, remains limited. Inspired by recent studies that explore the presence of attention sink in the initial token, which receives disproportionately large attention scores despite their lack of semantic importance, this work delves deeper into this phenomenon. We aim to provide a more profound understanding of the existence of attention sinks within LLMs and to uncover ways to enhance the achievable accuracy of LLMs by directly optimizing the attention distributions, without the need for weight finetuning. Specifically, this work begins with comprehensive visualizations of the attention distributions in LLMs during inference across various inputs and tasks. Based on these visualizations, to the best of our knowledge, we are the first to discover that (1) attention sinks occur not only at the start of sequences but also within later tokens of the input, and (2) not all attention sinks have a positive impact on the achievable accuracy of LLMs. Building upon our findings, we propose a training-free Attention Calibration Technique (ACT) that automatically optimizes the attention distributions on the fly during inference in an input-adaptive manner. Extensive experiments validate that ACT consistently enhances the accuracy of various LLMs across different applications. Specifically, ACT achieves an average improvement of up to $7.30%$ in accuracy across different datasets when applied to Llama-30B.