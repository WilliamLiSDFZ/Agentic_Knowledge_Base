---
title: "Understanding Forgetting in Continual Learning with Linear Regression"
source: "https://proceedings.mlr.press/v235/ding24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24c/ding24c.pdf"
categories: ['continual-learning-memory-plasticity', 'neural-network-learning-dynamics-theory']
tags: ['continual-learning', 'catastrophic-forgetting', 'linear-regression', 'theory', 'sequential-tasks']
venue: "ICML 2024"
tldr: "Theoretically analyzes catastrophic forgetting in continual learning through linear regression, identifying key factors that drive forgetting across sequential tasks."
---

# Understanding Forgetting in Continual Learning with Linear Regression

**Source**: [https://proceedings.mlr.press/v235/ding24c.html](https://proceedings.mlr.press/v235/ding24c.html)

**TLDR**: Theoretically analyzes catastrophic forgetting in continual learning through linear regression, identifying key factors that drive forgetting across sequential tasks.

## Abstract

Continual learning, focused on sequentially learning multiple tasks, has gained significant attention recently. Despite the tremendous progress made in the past, the theoretical understanding, especially factors contributing to $\textit{catastrophic forgetting}$, remains relatively unexplored. In this paper, we provide a general theoretical analysis of forgetting in the linear regression model via Stochastic Gradient Descent (SGD) applicable to both under-parameterized and overparameterized regimes. Our theoretical framework reveals some interesting insights into the intricate relationship between task sequence and algorithmic parameters, an aspect not fully captured in previous studies due to their restrictive assumptions. Specifically, we demonstrate that, given a sufficiently large data size, the arrangement of tasks in a sequence—where tasks with larger eigenvalues in their population data covariance matrices are trained later—tends to result in increased forgetting. Additionally, our findings highlight that an appropriate choice of step size will help mitigate forgetting in both under-parameterized and overparameterized settings. To validate our theoretical analysis, we conducted simulation experiments on both linear regression models and Deep Neural Networks (DNNs). Results from these simulations substantiate our theoretical findings.