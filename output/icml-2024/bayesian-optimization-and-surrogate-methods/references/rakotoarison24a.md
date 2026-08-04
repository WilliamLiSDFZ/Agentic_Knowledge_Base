---
title: "In-Context Freeze-Thaw Bayesian Optimization for Hyperparameter Optimization"
source: "https://proceedings.mlr.press/v235/rakotoarison24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rakotoarison24a/rakotoarison24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['Bayesian-optimization', 'freeze-thaw', 'hyperparameter-optimization', 'in-context-learning', 'grey-box']
venue: "ICML 2024"
tldr: "An in-context learning-based freeze-thaw Bayesian optimization method for efficient hyperparameter tuning of deep learning models."
---

# In-Context Freeze-Thaw Bayesian Optimization for Hyperparameter Optimization

**Source**: [https://proceedings.mlr.press/v235/rakotoarison24a.html](https://proceedings.mlr.press/v235/rakotoarison24a.html)

**TLDR**: An in-context learning-based freeze-thaw Bayesian optimization method for efficient hyperparameter tuning of deep learning models.

## Abstract

With the increasing computational costs associated with deep learning, automated hyperparameter optimization methods, strongly relying on black-box Bayesian optimization (BO), face limitations. Freeze-thaw BO offers a promising grey-box alternative, strategically allocating scarce resources incrementally to different configurations. However, the frequent surrogate model updates inherent to this approach pose challenges for existing methods, requiring retraining or fine-tuning their neural network surrogates online, introducing overhead, instability, and hyper-hyperparameters. In this work, we propose FT-PFN, a novel surrogate for Freeze-thaw style BO. FT-PFN is a prior-data fitted network (PFN) that leverages the transformers’ in-context learning ability to efficiently and reliably do Bayesian learning curve extrapolation in a single forward pass. Our empirical analysis across three benchmark suites shows that the predictions made by FT-PFN are more accurate and 10-100 times faster than those of the deep Gaussian process and deep ensemble surrogates used in previous work. Furthermore, we show that, when combined with our novel acquisition mechanism (MFPI-random), the resulting in-context freeze-thaw BO method (ifBO), yields new state-of-the-art performance in the same three families of deep learning HPO benchmarks considered in prior work.