---
title: "PRISE: LLM-Style Sequence Compression for Learning Temporal Action Abstractions in Control"
source: "https://proceedings.mlr.press/v235/zheng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24b/zheng24b.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['temporal-action-abstractions', 'sequence-compression', 'LLM', 'sequential-decision-making']
venue: "ICML 2024"
tldr: "PRISE frames temporal action abstraction learning as a sequence compression problem, drawing on LLM-style tokenization techniques for control tasks."
---

# PRISE: LLM-Style Sequence Compression for Learning Temporal Action Abstractions in Control

**Source**: [https://proceedings.mlr.press/v235/zheng24b.html](https://proceedings.mlr.press/v235/zheng24b.html)

**TLDR**: PRISE frames temporal action abstraction learning as a sequence compression problem, drawing on LLM-style tokenization techniques for control tasks.

## Abstract

Temporal action abstractions, along with belief state representations, are a powerful knowledge sharing mechanism for sequential decision making. In this work, we propose a novel view that treats inducing temporal action abstractions as a sequence compression problem. To do so, we bring a subtle but critical component of LLM training pipelines – input tokenization via byte pair encoding (BPE) – to bear on the seemingly distant task of learning skills of variable time span in continuous control domains. We introduce an approach called Primitive Sequence Encoding (PRISE) that combines continuous action quantization with BPE to learn powerful action abstractions. We empirically show that high-level skills discovered by PRISE from a multitask set of robotic manipulation demonstrations significantly boost the learning performance of behavior cloning on downstream tasks.