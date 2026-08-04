---
title: "MEMORYLLM: Towards Self-Updatable Large Language Models"
source: "https://proceedings.mlr.press/v235/wang24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24s/wang24s.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'continual-learning-memory-plasticity']
tags: ['LLM', 'self-updatable', 'continual-learning', 'knowledge-injection', 'memory-augmented']
venue: "ICML 2024"
tldr: "MEMORYLLM builds self-updatable large language models with a large memory pool enabling efficient continual knowledge integration after deployment."
---

# MEMORYLLM: Towards Self-Updatable Large Language Models

**Source**: [https://proceedings.mlr.press/v235/wang24s.html](https://proceedings.mlr.press/v235/wang24s.html)

**TLDR**: MEMORYLLM builds self-updatable large language models with a large memory pool enabling efficient continual knowledge integration after deployment.

## Abstract

Existing Large Language Models (LLMs) usually remain static after deployment, which might make it hard to inject new knowledge into the model. We aim to build models containing a considerable portion of self-updatable parameters, enabling the model to integrate new knowledge effectively and efficiently. To this end, we introduce MEMORYLLM, a model that comprises a transformer and a fixed-size memory pool within the latent space of the transformer. MEMORYLLM can self-update with text knowledge and memorize the knowledge injected earlier. Our evaluations demonstrate the ability of MEMORYLLM to effectively incorporate new knowledge, as evidenced by its performance on model editing benchmarks. Meanwhile, the model exhibits long-term information retention capacity, which is validated through our custom-designed evaluations and long-context benchmarks. MEMORYLLM also shows operational integrity without any sign of performance degradation even after nearly a million memory updates. Our code and model are open-sourced at https://github.com/wangyu-ustc/MemoryLLM.