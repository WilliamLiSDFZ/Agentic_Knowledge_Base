---
title: "TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks"
source: "https://proceedings.mlr.press/v235/wang24az.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24az/wang24az.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['language-models', 'tool-use', 'program-synthesis', 'verifiable-toolboxes']
venue: "ICML 2024"
tldr: "TroVE enables language models to automatically induce reusable and verifiable high-level toolboxes for programmatic task solving."
---

# TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks

**Source**: [https://proceedings.mlr.press/v235/wang24az.html](https://proceedings.mlr.press/v235/wang24az.html)

**TLDR**: TroVE enables language models to automatically induce reusable and verifiable high-level toolboxes for programmatic task solving.

## Abstract

Language models (LMs) can solve tasks such as answering questions about tables or images by writing programs. However, using primitive functions often leads to verbose and error-prone programs, and higher-level functions require expert design. To enable better solutions without human labor, we ask code LMs to curate reusable high-level functions, and use them to write solutions. We present TROVE, a training-free method of inducing a verifiable and efficient toolbox of functions, by generating via using, growing, and periodically trimming the toolbox. On 11 datasets from math, table question answering, and image reasoning tasks, TROVE consistently yields simpler solutions with higher accuracy than baselines using CodeLLaMa and previous methods using GPT, while using 79-98% smaller toolboxes. TROVE further enables 31% faster and 13% more accurate human verification than baselines. With the same pipeline, it creates diverse functions for varied tasks and datasets, providing insights into their individual characteristics.