---
title: "LLM Maybe LongLM: SelfExtend LLM Context Window Without Tuning"
source: "https://proceedings.mlr.press/v235/jin24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24b/jin24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['long-context', 'llm', 'context-window-extension', 'self-extend']
venue: "ICML 2024"
tldr: "SelfExtend enables LLMs to handle longer contexts than their training length without fine-tuning by exploiting their inherent positional generalization capabilities."
---

# LLM Maybe LongLM: SelfExtend LLM Context Window Without Tuning

**Source**: [https://proceedings.mlr.press/v235/jin24b.html](https://proceedings.mlr.press/v235/jin24b.html)

**TLDR**: SelfExtend enables LLMs to handle longer contexts than their training length without fine-tuning by exploiting their inherent positional generalization capabilities.

## Abstract

It is well known that LLMs cannot generalize well to long contexts whose lengths are larger than the training sequence length. This poses challenges when employing LLMs for processing long input sequences during inference. In this work, we argue that LLMs themselves have inherent capabilities to handles s long contexts without fine-tuning. To achieve this goal, we propose SelfExtend to extend the context window of LLMs by constructing bi-level attention information: the grouped attention and the neighbor attention. The grouped attention captures the dependencies among tokens that are far apart, while neighbor attention captures dependencies among adjacent tokens within a specified range. The two-level attentions are computed based on the original model’s self-attention mechanism during inference. With minor code modification, our SelfExtend can effortlessly extend existing LLMs’ context window without any fine-tuning. We conduct comprehensive experiments on multiple benchmarks and the results show that our SelfExtend can effectively extend existing LLMs’ context window length.