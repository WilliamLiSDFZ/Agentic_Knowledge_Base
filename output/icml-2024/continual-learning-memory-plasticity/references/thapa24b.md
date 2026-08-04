---
title: "Bayesian Adaptation of Network Depth and Width for Continual Learning"
source: "https://proceedings.mlr.press/v235/thapa24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/thapa24b/thapa24b.pdf"
categories: ['continual-learning-memory-plasticity', 'generative-models-and-variational-inference']
tags: ['continual-learning', 'Bayesian-nonparametrics', 'dynamic-architecture']
venue: "ICML 2024"
tldr: "A non-parametric Bayesian approach is proposed to adaptively infer both network depth and width for continual learning without forgetting."
---

# Bayesian Adaptation of Network Depth and Width for Continual Learning

**Source**: [https://proceedings.mlr.press/v235/thapa24b.html](https://proceedings.mlr.press/v235/thapa24b.html)

**TLDR**: A non-parametric Bayesian approach is proposed to adaptively infer both network depth and width for continual learning without forgetting.

## Abstract

While existing dynamic architecture-based continual learning methods adapt network width by growing new branches, they overlook the critical aspect of network depth. We propose a novel non-parametric Bayesian approach to infer network depth and adapt network width while maintaining model performance across tasks. Specifically, we model the growth of network depth with a beta process and apply drop-connect regularization to network width using a conjugate Bernoulli process. Our results show that our proposed method achieves superior or comparable performance with state-of-the-art methods across various continual learning benchmarks. Moreover, our approach can be readily extended to unsupervised continual learning, showcasing competitive performance compared to existing techniques.