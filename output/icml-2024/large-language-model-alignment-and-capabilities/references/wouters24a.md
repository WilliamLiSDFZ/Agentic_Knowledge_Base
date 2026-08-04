---
title: "Optimizing Watermarks for Large Language Models"
source: "https://proceedings.mlr.press/v235/wouters24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wouters24a/wouters24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-watermarking', 'text-quality', 'identifiability', 'optimization']
venue: "ICML 2024"
tldr: "Formulates and solves an optimization problem to find watermarks for LLMs that best balance detectability and minimal impact on generated text quality."
---

# Optimizing Watermarks for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/wouters24a.html](https://proceedings.mlr.press/v235/wouters24a.html)

**TLDR**: Formulates and solves an optimization problem to find watermarks for LLMs that best balance detectability and minimal impact on generated text quality.

## Abstract

With the rise of large language models (LLMs) and concerns about potential misuse, watermarks for generative LLMs have recently attracted much attention. An important aspect of such watermarks is the trade-off between their identifiability and their impact on the quality of the generated text. This paper introduces a systematic approach to this trade-off in terms of a multi-objective optimization problem. For a large class of robust, efficient watermarks, the associated Pareto optimal solutions are identified and shown to outperform existing robust, efficient watermarks.