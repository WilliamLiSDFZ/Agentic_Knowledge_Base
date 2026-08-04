---
title: "Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?"
source: "https://proceedings.mlr.press/v235/gatmiry24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gatmiry24b/gatmiry24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['looped-transformers', 'in-context-learning', 'gradient-descent']
venue: "ICML 2024"
tldr: "Analyzes whether looped transformers can implement multi-step gradient descent for in-context learning tasks."
---

# Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?

**Source**: [https://proceedings.mlr.press/v235/gatmiry24b.html](https://proceedings.mlr.press/v235/gatmiry24b.html)

**TLDR**: Analyzes whether looped transformers can implement multi-step gradient descent for in-context learning tasks.

## Abstract

Transformers to do reasoning and few-shot learning, without any fine-tuning, is widely conjectured to stem from their ability to implicitly simulate a multi-step algorithms – such as gradient descent – with their weights in a single forward pass. Recently, there has been progress in understanding this complex phenomenon from an expressivity point of view, by demonstrating that Transformers can express such multi-step algorithms. However, our knowledge about the more fundamental aspect of its learnability, beyond single layer models, is very limited. In particular, can training Transformers enable convergence to algorithmic solutions? In this work we resolve this for in context linear regression with linear looped Transformers – a multi-layer model with weight sharing that is conjectured to have an inductive bias to learn fix-point iterative algorithms. More specifically, for this setting we show that the global minimizer of the population training loss implements multi-step preconditioned gradient descent, with a preconditioner that adapts to the data distribution. Furthermore, we show a fast convergence for gradient flow on the regression loss, despite the non-convexity of the landscape, by proving a novel gradient dominance condition. To our knowledge, this is the first theoretical analysis for multi-layer Transformer in this setting. We further validate our theoretical findings through synthetic experiments.