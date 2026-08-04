---
title: "Learning Low-dimensional Latent Dynamics from High-dimensional Observations: Non-asymptotics and Lower Bounds"
source: "https://proceedings.mlr.press/v235/zhang24bh.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bh/zhang24bh.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'neural-network-learning-dynamics-theory']
tags: ['linear-dynamical-systems', 'latent-variable-models', 'high-dimensional-observations', 'non-asymptotic-analysis', 'system-identification']
venue: "ICML 2024"
tldr: "Provides non-asymptotic guarantees and lower bounds for learning low-dimensional latent linear dynamics from high-dimensional observations."
---

# Learning Low-dimensional Latent Dynamics from High-dimensional Observations: Non-asymptotics and Lower Bounds

**Source**: [https://proceedings.mlr.press/v235/zhang24bh.html](https://proceedings.mlr.press/v235/zhang24bh.html)

**TLDR**: Provides non-asymptotic guarantees and lower bounds for learning low-dimensional latent linear dynamics from high-dimensional observations.

## Abstract

In this paper, we focus on learning a linear time-invariant (LTI) model with low-dimensional latent variables but high-dimensional observations. We provide an algorithm that recovers the high-dimensional features, i.e. column space of the observer, embeds the data into low dimensions and learns the low-dimensional model parameters. Our algorithm enjoys a sample complexity guarantee of order $\tilde{\mathcal{O}}(n/\epsilon^2)$, where $n$ is the observation dimension. We further establish a fundamental lower bound indicating this complexity bound is optimal up to logarithmic factors and dimension-independent constants. We show that this inevitable linear factor of $n$ is due to the learning error of the observer’s column space in the presence of high-dimensional noises. Extending our results, we consider a meta-learning problem inspired by various real-world applications, where the observer column space can be collectively learned from datasets of multiple LTI systems. An end-to-end algorithm is then proposed, facilitating learning LTI systems from a meta-dataset which breaks the sample complexity lower bound in certain scenarios.