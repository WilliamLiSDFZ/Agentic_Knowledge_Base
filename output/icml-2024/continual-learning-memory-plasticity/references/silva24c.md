---
title: "Learning from Memory: Non-Parametric Memory Augmented Self-Supervised Learning of Visual Features"
source: "https://proceedings.mlr.press/v235/silva24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/silva24c/silva24c.pdf"
categories: ['continual-learning-memory-plasticity', 'clustering-methods-and-multi-view-learning']
tags: ['self-supervised-learning', 'non-parametric-memory', 'visual-representation']
venue: "ICML 2024"
tldr: "Augments self-supervised visual learning with a non-parametric memory of seen concepts to improve training stability."
---

# Learning from Memory: Non-Parametric Memory Augmented Self-Supervised Learning of Visual Features

**Source**: [https://proceedings.mlr.press/v235/silva24c.html](https://proceedings.mlr.press/v235/silva24c.html)

**TLDR**: Augments self-supervised visual learning with a non-parametric memory of seen concepts to improve training stability.

## Abstract

This paper introduces a novel approach to improving the training stability of self-supervised learning (SSL) methods by leveraging a non-parametric memory of seen concepts. The proposed method involves augmenting a neural network with a memory component to stochastically compare current image views with previously encountered concepts. Additionally, we introduce stochastic memory blocks to regularize training and enforce consistency between image views. We extensively benchmark our method on many vision tasks, such as linear probing, transfer learning, few-shot classification, and image retrieval on many datasets. The experimental results consolidate the effectiveness of the proposed approach in achieving stable SSL training without additional regularizers while learning highly transferable representations and requiring less computing time and resources.