---
title: "Improving Robustness to Multiple Spurious Correlations by Multi-Objective Optimization"
source: "https://proceedings.mlr.press/v235/kim24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24l/kim24l.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'fairness-aware-algorithmic-decision-making']
tags: ['spurious-correlations', 'multi-objective-optimization', 'bias-mitigation']
venue: "ICML 2024"
tldr: "Proposes a multi-objective optimization approach to simultaneously mitigate multiple spurious correlations during model training."
---

# Improving Robustness to Multiple Spurious Correlations by Multi-Objective Optimization

**Source**: [https://proceedings.mlr.press/v235/kim24l.html](https://proceedings.mlr.press/v235/kim24l.html)

**TLDR**: Proposes a multi-objective optimization approach to simultaneously mitigate multiple spurious correlations during model training.

## Abstract

We study the problem of training an unbiased and accurate model given a dataset with multiple biases. This problem is challenging since the multiple biases cause multiple undesirable shortcuts during training, and even worse, mitigating one may exacerbate the other. We propose a novel training method to tackle this challenge. Our method first groups training data so that different groups induce different shortcuts, and then optimizes a linear combination of group-wise losses while adjusting their weights dynamically to alleviate conflicts between the groups in performance; this approach, rooted in the multi-objective optimization theory, encourages to achieve the minimax Pareto solution. We also present a new benchmark with multiple biases, dubbed MultiCelebA, for evaluating debiased training methods under realistic and challenging scenarios. Our method achieved the best on three datasets with multiple biases, and also showed superior performance on conventional single-bias datasets.