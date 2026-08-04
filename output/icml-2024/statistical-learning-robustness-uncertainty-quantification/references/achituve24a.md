---
title: "Bayesian Uncertainty for Gradient Aggregation in Multi-Task Learning"
source: "https://proceedings.mlr.press/v235/achituve24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/achituve24a/achituve24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['multi-task-learning', 'gradient-aggregation', 'bayesian-uncertainty', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "Introduces Bayesian uncertainty estimates to weight gradient aggregation in multi-task learning optimization."
---

# Bayesian Uncertainty for Gradient Aggregation in Multi-Task Learning

**Source**: [https://proceedings.mlr.press/v235/achituve24a.html](https://proceedings.mlr.press/v235/achituve24a.html)

**TLDR**: Introduces Bayesian uncertainty estimates to weight gradient aggregation in multi-task learning optimization.

## Abstract

As machine learning becomes more prominent there is a growing demand to perform several inference tasks in parallel. Multi-task learning (MTL) addresses this challenge by learning a single model that solves several tasks simultaneously and efficiently. Often optimizing MTL models entails first computing the gradient of the loss for each task, and then aggregating all the gradients to obtain a combined update direction. However, common methods following this approach do not consider an important aspect, the sensitivity in the dimensions of the gradients. Some dimensions may be more lenient for changes while others may be more restrictive. Here, we introduce a novel gradient aggregation procedure using Bayesian inference. We place a probability distribution over the task-specific parameters, which in turn induce a distribution over the gradients of the tasks. This valuable information allows us to quantify the uncertainty associated with each of the gradients’ dimensions which is factored in when aggregating them. We empirically demonstrate the benefits of our approach in a variety of datasets, achieving state-of-the-art performance.