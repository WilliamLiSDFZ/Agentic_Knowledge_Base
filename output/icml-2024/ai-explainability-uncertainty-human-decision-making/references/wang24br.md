---
title: "Benchmarking Deletion Metrics with the Principled Explanations"
source: "https://proceedings.mlr.press/v235/wang24br.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24br/wang24br.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'position-papers-on-ml-research-directions']
tags: ['attribution-methods', 'deletion-metrics', 'explainability-evaluation', 'feature-importance']
venue: "ICML 2024"
tldr: "Benchmarks insertion/deletion evaluation metrics for attribution-based explanations using principled ground-truth explanations."
---

# Benchmarking Deletion Metrics with the Principled Explanations

**Source**: [https://proceedings.mlr.press/v235/wang24br.html](https://proceedings.mlr.press/v235/wang24br.html)

**TLDR**: Benchmarks insertion/deletion evaluation metrics for attribution-based explanations using principled ground-truth explanations.

## Abstract

Insertion/deletion metrics and their variants have been extensively applied to evaluate attribution-based explanation methods. Such metrics measure the significance of features by observing changes in model predictions as features are incrementally inserted or deleted. Given the direct connection between the attribution values and model predictions that insertion/deletion metrics enable, they are commonly used as the decisive metrics for novel attribution methods. Such influential metrics for explanation methods should be handled with great scrutiny. However, contemporary research on insertion/deletion metrics falls short of a comprehensive analysis. To address this, we propose the TRAjectory importanCE (TRACE) framework, which achieves the best scores of the insertion/deletion metric. Our contribution includes two aspects: 1) TRACE stands as the principled explanation for explaining the influence of feature deletion on model predictions. We demonstrate that TRACE is guaranteed to achieve almost optimal results both theoretically and empirically. 2) Using TRACE, we benchmark insertion/deletion metrics across all possible settings and study critical problems such as the out-of-distribution (OOD) issue, and provide practical guidance on applying these metrics in practice.