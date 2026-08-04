---
title: "Achieving Margin Maximization Exponentially Fast via Progressive Norm Rescaling"
source: "https://proceedings.mlr.press/v235/wang24ax.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ax/wang24ax.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['margin-maximization', 'gradient-descent', 'norm-rescaling', 'linear-classification']
venue: "ICML 2024"
tldr: "Progressive norm rescaling is shown to achieve margin maximization exponentially faster in gradient-based classification algorithms."
---

# Achieving Margin Maximization Exponentially Fast via Progressive Norm Rescaling

**Source**: [https://proceedings.mlr.press/v235/wang24ax.html](https://proceedings.mlr.press/v235/wang24ax.html)

**TLDR**: Progressive norm rescaling is shown to achieve margin maximization exponentially faster in gradient-based classification algorithms.

## Abstract

In this work, we investigate the margin-maximization bias exhibited by gradient-based algorithms in classifying linearly separable data. We present an in-depth analysis of the specific properties of the velocity field associated with (normalized) gradients, focusing on their role in margin maximization. Inspired by this analysis, we propose a novel algorithm called Progressive Rescaling Gradient Descent (PRGD) and show that PRGD can maximize the margin at an exponential rate. This stands in stark contrast to all existing algorithms, which maximize the margin at a slow polynomial rate. Specifically, we identify mild conditions on data distribution under which existing algorithms such as gradient descent (GD) and normalized gradient descent (NGD) provably fail in maximizing the margin efficiently. To validate our theoretical findings, we present both synthetic and real-world experiments. Notably, PRGD also shows promise in enhancing the generalization performance when applied to linearly non-separable datasets and deep neural networks.