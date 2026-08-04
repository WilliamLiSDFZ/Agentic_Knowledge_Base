---
title: "Learning to Continually Learn with the Bayesian Principle"
source: "https://proceedings.mlr.press/v235/lee24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24j/lee24j.pdf"
categories: ['continual-learning-memory-plasticity', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['continual-learning', 'Bayesian-inference', 'meta-learning', 'forgetting']
venue: "ICML 2024"
tldr: "Applies Bayesian principles to continual learning to mitigate catastrophic forgetting via online meta-learning of a learning algorithm."
---

# Learning to Continually Learn with the Bayesian Principle

**Source**: [https://proceedings.mlr.press/v235/lee24j.html](https://proceedings.mlr.press/v235/lee24j.html)

**TLDR**: Applies Bayesian principles to continual learning to mitigate catastrophic forgetting via online meta-learning of a learning algorithm.

## Abstract

In the present era of deep learning, continual learning research is mainly focused on mitigating forgetting when training a neural network with stochastic gradient descent on a non-stationary stream of data. On the other hand, in the more classical literature of statistical machine learning, many models have sequential Bayesian update rules that yield the same learning outcome as the batch training, i.e., they are completely immune to catastrophic forgetting. However, they are often overly simple to model complex real-world data. In this work, we adopt the meta-learning paradigm to combine the strong representational power of neural networks and simple statistical models’ robustness to forgetting. In our novel meta-continual learning framework, continual learning takes place only in statistical models via ideal sequential Bayesian update rules, while neural networks are meta-learned to bridge the raw data and the statistical models. Since the neural networks remain fixed during continual learning, they are protected from catastrophic forgetting. This approach not only achieves significantly improved performance but also exhibits excellent scalability. Since our approach is domain-agnostic and model-agnostic, it can be applied to a wide range of problems and easily integrated with existing model architectures.