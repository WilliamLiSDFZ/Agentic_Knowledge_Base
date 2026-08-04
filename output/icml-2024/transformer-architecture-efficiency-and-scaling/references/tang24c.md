---
title: "Rethinking Optimization and Architecture for Tiny Language Models"
source: "https://proceedings.mlr.press/v235/tang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24c/tang24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['tiny-language-models', 'architecture', 'mobile-deployment']
venue: "ICML 2024"
tldr: "Optimized architectures and training strategies are proposed for tiny language models targeting high performance under mobile device constraints."
---

# Rethinking Optimization and Architecture for Tiny Language Models

**Source**: [https://proceedings.mlr.press/v235/tang24c.html](https://proceedings.mlr.press/v235/tang24c.html)

**TLDR**: Optimized architectures and training strategies are proposed for tiny language models targeting high performance under mobile device constraints.

## Abstract

The power of large language models (LLMs) has been demonstrated through numerous data and computing resources. However, the application of language models on mobile devices is facing huge challenge on the computation and memory costs, that is, tiny language models with high performance are urgently required. Limited by the highly complex training process, there are many details for optimizing language models that are seldom studied carefully. In this study, based on a tiny language model with 1B parameters, we carefully design a series of empirical study to analyze the effect of each component. Three perspectives are mainly discussed, i.e., neural architecture, parameter initialization, and optimization strategy. Several design formulas are empirically proved especially effective for tiny language models, including tokenizer compression, architecture tweaking, parameter inheritance and multiple-round training. Then we train PanGu-$\pi$-1B Pro and PanGu-$\pi$-1.5B Pro on 1.6T multilingual corpora, following the established formulas. Experimental results demonstrate the improved optimization and architecture yield a notable average improvement of 8.87 on benchmark evaluation sets for PanGu-$\pi$-1B Pro. Besides, PanGu-$\pi$-1.5B Pro surpasses a range of SOTA models with larger model sizes, validating its superior performance. The code will be released soon. The code is available at https://github.com/YuchuanTian/RethinkTinyLM.