---
title: "Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models"
source: "https://proceedings.mlr.press/v235/dong24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dong24b/dong24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['LLM-pruning', 'symbolic-regression', 'evolutionary-search', 'post-training-pruning', 'neural-architecture']
venue: "ICML 2024"
tldr: "Proposes Pruner-Zero, which evolves symbolic pruning metrics from scratch using genetic programming to enable efficient post-training pruning of LLMs without retraining."
---

# Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/dong24b.html](https://proceedings.mlr.press/v235/dong24b.html)

**TLDR**: Proposes Pruner-Zero, which evolves symbolic pruning metrics from scratch using genetic programming to enable efficient post-training pruning of LLMs without retraining.

## Abstract

Despite the remarkable capabilities, Large Language Models (LLMs) face deployment challenges due to their extensive size. Pruning methods drop a subset of weights to accelerate, but many of them require retraining, which is prohibitively expensive and computationally demanding. Recently, post-training pruning approaches introduced novel metrics, enabling the pruning of LLMs without retraining. However, these metrics require the involvement of human experts and tedious trial and error. To efficiently identify superior pruning metrics, we develop an automatic framework for searching symbolic pruning metrics using genetic programming. In particular, we devise an elaborate search space encompassing the existing pruning metrics to discover the potential symbolic pruning metric. We propose an opposing operation simplification strategy to increase the diversity of the population. In this way, Pruner-Zero allows auto-generation of symbolic pruning metrics. Based on the searched results, we explore the correlation between pruning metrics and performance after pruning and summarize some principles. Extensive experiments on LLaMA and LLaMA-2 on language modeling and zero-shot tasks demonstrate that our Pruner-Zero obtains superior performance than SOTA post-training pruning methods. Code at: https://github.com/pprp/Pruner-Zero.