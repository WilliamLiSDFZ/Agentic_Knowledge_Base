---
title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
source: "https://proceedings.mlr.press/v235/dohmatob24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dohmatob24b/dohmatob24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'neural-network-learning-dynamics-theory']
tags: ['model-collapse', 'scaling-laws', 'synthetic-data', 'distribution-shift', 'tail-behavior']
venue: "ICML 2024"
tldr: "Analyzes model collapse from iterative training on AI-generated data as a change in neural scaling laws, with particular focus on tail distribution degradation."
---

# A Tale of Tails: Model Collapse as a Change of Scaling Laws

**Source**: [https://proceedings.mlr.press/v235/dohmatob24b.html](https://proceedings.mlr.press/v235/dohmatob24b.html)

**TLDR**: Analyzes model collapse from iterative training on AI-generated data as a change in neural scaling laws, with particular focus on tail distribution degradation.

## Abstract

As AI model size grows, neural scaling laws have become a crucial tool to predict the improvements of large models when increasing capacity and the size of original (human or natural) training data. Yet, the widespread use of popular models means that the ecosystem of online data and text will co-evolve to progressively contain increased amounts of synthesized data. In this paper we ask: How will the scaling laws change in the inevitable regime where synthetic data makes its way into the training corpus? Will future models, still improve, or be doomed to degenerate up to total (model) collapse? We develop a theoretical framework of model collapse through the lens of scaling laws. We discover a wide range of decay phenomena, analyzing loss of scaling, shifted scaling with number of generations, the ”un-learning" of skills, and grokking when mixing human and synthesized data. Our theory is validated by large-scale experiments with a transformer on an arithmetic task and text generation using the large language model Llama2.