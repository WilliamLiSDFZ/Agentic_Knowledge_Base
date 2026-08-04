---
title: "Scaling Laws for Fine-Grained Mixture of Experts"
source: "https://proceedings.mlr.press/v235/ludziejewski24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ludziejewski24a/ludziejewski24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['mixture-of-experts', 'scaling-laws', 'LLM', 'computational-efficiency']
venue: "ICML 2024"
tldr: "This work analyzes scaling properties of fine-grained Mixture of Experts models and introduces new hyperparameters to better characterize their behavior."
---

# Scaling Laws for Fine-Grained Mixture of Experts

**Source**: [https://proceedings.mlr.press/v235/ludziejewski24a.html](https://proceedings.mlr.press/v235/ludziejewski24a.html)

**TLDR**: This work analyzes scaling properties of fine-grained Mixture of Experts models and introduces new hyperparameters to better characterize their behavior.

## Abstract

Mixture of Experts (MoE) models have emerged as a primary solution for reducing the computational cost of Large Language Models. In this work, we analyze their scaling properties, highlighting certain arbitrary assumptions present in the existing literature. In particular, we introduce a new hyperparameter, granularity, the modification of which allows for the optimal adjustment of the size of experts. Subsequently, we present scaling laws for fine-grained MoE, taking into account the number of training tokens, model size, and granularity. Using these scaling laws, we derive the optimal training configuration for a given computational budget. Furthermore, in contrast with previous works, we demonstrate that the gap in efficiency between dense and MoE models grows as we scale up the model size and training budget.