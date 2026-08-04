---
title: "Vision Transformers as Probabilistic Expansion from Learngene"
source: "https://proceedings.mlr.press/v235/wang24cf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cf/wang24cf.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'continual-learning-memory-plasticity']
tags: ['vision-transformers', 'learngene', 'model-initialization', 'elastic-scaling']
venue: "ICML 2024"
tldr: "Proposes viewing Vision Transformers as probabilistic expansions from a compact learngene, enabling flexible model initialization across varying resource constraints."
---

# Vision Transformers as Probabilistic Expansion from Learngene

**Source**: [https://proceedings.mlr.press/v235/wang24cf.html](https://proceedings.mlr.press/v235/wang24cf.html)

**TLDR**: Proposes viewing Vision Transformers as probabilistic expansions from a compact learngene, enabling flexible model initialization across varying resource constraints.

## Abstract

Deep learning has advanced through the combination of large datasets and computational power, leading to the development of extensive pre-trained models like Vision Transformers (ViTs). However, these models often assume a one-size-fits-all utility, lacking the ability to initialize models with elastic scales tailored to the resource constraints of specific downstream tasks. To address these issues, we propose Probabilistic Expansion from LearnGene (PEG) for mixture sampling and elastic initialization of Vision Transformers. Specifically, PEG utilizes a probabilistic mixture approach to sample Multi-Head Self-Attention layers and Feed-Forward Networks from a large ancestry model into a more compact part termed as learngene. Theoretically, we demonstrate that these learngene can approximate the parameter distribution of the original ancestry model, thereby preserving its significant knowledge. Next, PEG expands the sampled learngene through non-linear mapping, enabling the initialization of descendant models with elastic scales to suit various resource constraints. Our extensive experiments demonstrate the effectiveness of PEG and outperforming traditional initialization strategies.