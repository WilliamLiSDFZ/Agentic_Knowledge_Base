---
title: "A New Linear Scaling Rule for Private Adaptive Hyperparameter Optimization"
source: "https://proceedings.mlr.press/v235/panda24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/panda24a/panda24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'hyperparameter-optimization', 'DP-SGD', 'scaling-rules']
venue: "ICML 2024"
tldr: "Proposes a new linear scaling rule for hyperparameter optimization in differentially private deep learning to reduce the cost of tuning DP-SGD."
---

# A New Linear Scaling Rule for Private Adaptive Hyperparameter Optimization

**Source**: [https://proceedings.mlr.press/v235/panda24a.html](https://proceedings.mlr.press/v235/panda24a.html)

**TLDR**: Proposes a new linear scaling rule for hyperparameter optimization in differentially private deep learning to reduce the cost of tuning DP-SGD.

## Abstract

An open problem in differentially private deep learning is hyperparameter optimization (HPO). DP-SGD introduces new hyperparameters and complicates existing ones, forcing researchers to painstakingly tune hyperparameters with hundreds of trials, which in turn makes it impossible to account for the privacy cost of HPO without destroying the utility. We propose an adaptive HPO method that uses cheap trials (in terms of privacy cost and runtime) to estimate optimal hyperparameters and scales them up. We obtain state-of-the-art performance on 22 benchmark tasks, across computer vision and natural language processing, across pretraining and finetuning, across architectures and a wide range of $\varepsilon \in [0.01,8.0]$, all while accounting for the privacy cost of HPO.