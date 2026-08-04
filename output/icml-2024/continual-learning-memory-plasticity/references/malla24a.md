---
title: "COPAL: Continual Pruning in Large Language Generative Models"
source: "https://proceedings.mlr.press/v235/malla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/malla24a/malla24a.pdf"
categories: ['continual-learning-memory-plasticity', 'transformer-architecture-efficiency-and-scaling']
tags: ['continual-pruning', 'large-language-models', 'domain-adaptation']
venue: "ICML 2024"
tldr: "COPAL enables continual pruning of large language models for efficient and adaptive domain-specific deployment without catastrophic forgetting."
---

# COPAL: Continual Pruning in Large Language Generative Models

**Source**: [https://proceedings.mlr.press/v235/malla24a.html](https://proceedings.mlr.press/v235/malla24a.html)

**TLDR**: COPAL enables continual pruning of large language models for efficient and adaptive domain-specific deployment without catastrophic forgetting.

## Abstract

Adapting pre-trained large language models to different domains in natural language processing requires two key considerations: high computational demands and model’s inability to continual adaptation. To simultaneously address both issues, this paper presents COPAL (COntinual Pruning in Adaptive Language settings), an algorithm developed for pruning large language generative models under a continual model adaptation setting. While avoiding resource-heavy finetuning or retraining, our pruning process is guided by the proposed sensitivity analysis. The sensitivity effectively measures model’s ability to withstand perturbations introduced by the new dataset and finds model’s weights that are relevant for all encountered datasets. As a result, COPAL allows seamless model adaptation to new domains while enhancing the resource efficiency. Our empirical evaluation on a various size of LLMs show that COPAL outperforms baseline models, demonstrating its efficacy in efficiency and adaptability.