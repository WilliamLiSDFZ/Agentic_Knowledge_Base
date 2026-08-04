---
title: "Larimar: Large Language Models with Episodic Memory Control"
source: "https://proceedings.mlr.press/v235/das24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/das24a/das24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'continual-learning-memory-plasticity']
tags: ['large-language-models', 'episodic-memory', 'knowledge-editing', 'brain-inspired', 'memory-control']
venue: "ICML 2024"
tldr: "Introduces Larimar, a brain-inspired LLM architecture with a distributed episodic memory module enabling efficient dynamic knowledge updates."
---

# Larimar: Large Language Models with Episodic Memory Control

**Source**: [https://proceedings.mlr.press/v235/das24a.html](https://proceedings.mlr.press/v235/das24a.html)

**TLDR**: Introduces Larimar, a brain-inspired LLM architecture with a distributed episodic memory module enabling efficient dynamic knowledge updates.

## Abstract

Efficient and accurate updating of knowledge stored in Large Language Models (LLMs) is one of the most pressing research challenges today. This paper presents Larimar - a novel, brain-inspired architecture for enhancing LLMs with a distributed episodic memory. Larimar’s memory allows for dynamic, one-shot updates of knowledge without the need for computationally expensive re-training or fine-tuning. Experimental results on multiple fact editing benchmarks demonstrate that Larimar attains accuracy comparable to most competitive baselines, even in the challenging sequential editing setup, but also excels in speed—yielding speed-ups of 8-10x depending on the base LLM —as well as flexibility due to the proposed architecture being simple, LLM-agnostic, and hence general. We further provide mechanisms for selective fact forgetting, information leakage prevention, and input context length generalization with Larimar and show their effectiveness. Our code is available at https://github.com/IBM/larimar.