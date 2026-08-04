---
title: "Provably Better Explanations with Optimized Aggregation of Feature Attributions"
source: "https://proceedings.mlr.press/v235/decker24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/decker24a/decker24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['feature-attribution', 'explainability', 'aggregation', 'post-hoc-explanation', 'optimization']
venue: "ICML 2024"
tldr: "Proposes an optimized aggregation of multiple feature attribution methods that provably yields better and more stable explanations than individual methods."
---

# Provably Better Explanations with Optimized Aggregation of Feature Attributions

**Source**: [https://proceedings.mlr.press/v235/decker24a.html](https://proceedings.mlr.press/v235/decker24a.html)

**TLDR**: Proposes an optimized aggregation of multiple feature attribution methods that provably yields better and more stable explanations than individual methods.

## Abstract

Using feature attributions for post-hoc explanations is a common practice to understand and verify the predictions of opaque machine learning models. Despite the numerous techniques available, individual methods often produce inconsistent and unstable results, putting their overall reliability into question. In this work, we aim to systematically improve the quality of feature attributions by combining multiple explanations across distinct methods or their variations. For this purpose, we propose a novel approach to derive optimal convex combinations of feature attributions that yield provable improvements of desired quality criteria such as robustness or faithfulness to the model behavior. Through extensive experiments involving various model architectures and popular feature attribution techniques, we demonstrate that our combination strategy consistently outperforms individual methods and existing baselines.