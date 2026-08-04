---
title: "Understanding Stochastic Natural Gradient Variational Inference"
source: "https://proceedings.mlr.press/v235/wu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24f/wu24f.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['variational-inference', 'natural-gradient', 'stochastic-optimization', 'convergence']
venue: "ICML 2024"
tldr: "Provides the first non-asymptotic convergence analysis of stochastic natural gradient variational inference in practical settings."
---

# Understanding Stochastic Natural Gradient Variational Inference

**Source**: [https://proceedings.mlr.press/v235/wu24f.html](https://proceedings.mlr.press/v235/wu24f.html)

**TLDR**: Provides the first non-asymptotic convergence analysis of stochastic natural gradient variational inference in practical settings.

## Abstract

Stochastic natural gradient variational inference (NGVI) is a popular posterior inference method with applications in various probabilistic models. Despite its wide usage, little is known about the non-asymptotic convergence rate in the stochastic setting. We aim to lessen this gap and provide a better understanding. For conjugate likelihoods, we prove the first $\mathcal{O}(\frac{1}{T})$ non-asymptotic convergence rate of stochastic NGVI. The complexity is no worse than stochastic gradient descent (a.k.a. black-box variational inference) and the rate likely has better constant dependency that leads to faster convergence in practice. For non-conjugate likelihoods, we show that stochastic NGVI with the canonical parameterization implicitly optimizes a non-convex objective. Thus, a global convergence rate of $\mathcal{O}(\frac{1}{T})$ is unlikely without some significant new understanding of optimizing the ELBO using natural gradients.