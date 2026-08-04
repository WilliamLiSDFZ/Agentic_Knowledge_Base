---
title: "Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks"
source: "https://proceedings.mlr.press/v235/ramesh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ramesh24a/ramesh24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-geometry-and-interpretability-research']
tags: ['transformers', 'compositionality', 'interpretability', 'synthetic-tasks', 'in-context-learning']
venue: "ICML 2024"
tldr: "This paper studies how autoregressive transformers compose learned capabilities on synthetic interpretable tasks to understand their compositional generalization."
---

# Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks

**Source**: [https://proceedings.mlr.press/v235/ramesh24a.html](https://proceedings.mlr.press/v235/ramesh24a.html)

**TLDR**: This paper studies how autoregressive transformers compose learned capabilities on synthetic interpretable tasks to understand their compositional generalization.

## Abstract

Transformers trained on huge text corpora exhibit a remarkable set of capabilities, e.g., performing simple logical operations. Given the inherent compositional nature of language, one can expect the model to learn to compose these capabilities, potentially yielding a combinatorial explosion of what operations it can perform on an input. Motivated by the above, we aim to assess in this paper “how capable can a transformer become?”. Specifically, we train autoregressive Transformer models on a data-generating process that involves compositions of a set of well-defined monolithic capabilities. Through a series of extensive and systematic experiments on this data-generating process, we show that: (1) autoregressive Transformers can learn compositional structures from small amounts of training data and generalize to exponentially or even combinatorially many functions; (2) composing functions by generating intermediate outputs is more effective at generalizing to unseen compositions, compared to generating no intermediate outputs; (3) biases in the order of the compositions in the training data, results in Transformers that fail to compose some combinations of functions; and (4) the attention layers seem to select the capability to apply while the feed-forward layers execute the capability.