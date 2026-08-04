---
title: "What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation"
source: "https://proceedings.mlr.press/v235/singh24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singh24c/singh24c.pdf"
categories: ['llm-geometry-and-interpretability-research', 'neural-network-learning-dynamics-theory']
tags: ['induction-heads', 'mechanistic-interpretability', 'in-context-learning']
venue: "ICML 2024"
tldr: "Mechanistically studies the formation and operation of induction head circuits critical to in-context learning in transformers."
---

# What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation

**Source**: [https://proceedings.mlr.press/v235/singh24c.html](https://proceedings.mlr.press/v235/singh24c.html)

**TLDR**: Mechanistically studies the formation and operation of induction head circuits critical to in-context learning in transformers.

## Abstract

In-context learning is a powerful emergent ability in transformer models. Prior work in mechanistic interpretability has identified a circuit element that may be critical for in-context learning – the induction head (IH), which performs a match-and-copy operation. During training of large transformers on natural language data, IHs emerge around the same time as a notable phase change in the loss. Despite the robust evidence for IHs and this interesting coincidence with the phase change, relatively little is known about the diversity and emergence dynamics of IHs. Why is there more than one IH, and how are they dependent on each other? Why do IHs appear all of a sudden, and what are the subcircuits that enable them to emerge? We answer these questions by studying IH emergence dynamics in a controlled setting by training on synthetic data. In doing so, we develop and share a novel optogenetics-inspired causal framework for modifying activations throughout training. Using this framework, we delineate the diverse and additive nature of IHs. By "clamping" subsets of activations throughout training, we then identify three underlying subcircuits that interact to drive IH formation, yielding the phase change. Furthermore, these subcircuits shed light on data-dependent properties of formation, such as phase change timing, already showing the promise of this more in-depth understanding of subcircuits that need to "go right" for an induction head.