---
title: "Differentiable Distributionally Robust Optimization Layers"
source: "https://proceedings.mlr.press/v235/ma24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24j/ma24j.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['distributionally-robust-optimization', 'decision-focused-learning', 'differentiable-optimization', 'uncertainty']
venue: "ICML 2024"
tldr: "Differentiable distributionally robust optimization layers are proposed to embed DRO into learning pipelines for decision-focused learning."
---

# Differentiable Distributionally Robust Optimization Layers

**Source**: [https://proceedings.mlr.press/v235/ma24j.html](https://proceedings.mlr.press/v235/ma24j.html)

**TLDR**: Differentiable distributionally robust optimization layers are proposed to embed DRO into learning pipelines for decision-focused learning.

## Abstract

In recent years, there has been a growing research interest in decision-focused learning, which embeds optimization problems as a layer in learning pipelines and demonstrates a superior performance than the prediction-focused approach. However, for distributionally robust optimization (DRO), a popular paradigm for decision-making under uncertainty, it is still unknown how to embed it as a layer, i.e., how to differentiate decisions with respect to an ambiguity set. In this paper, we develop such differentiable DRO layers for generic mixed-integer DRO problems with parameterized second-order conic ambiguity sets and discuss its extension to Wasserstein ambiguity sets. To differentiate the mixed-integer decisions, we propose a novel dual-view methodology by handling continuous and discrete parts of decisions via different principles. Specifically, we construct a differentiable energy-based surrogate to implement the dual-view methodology and use importance sampling to estimate its gradient. We further prove that such a surrogate enjoys the asymptotic convergency under regularization. As an application of the proposed differentiable DRO layers, we develop a novel decision-focused learning pipeline for contextual distributionally robust decision-making tasks and compare it with the prediction-focused approach in experiments