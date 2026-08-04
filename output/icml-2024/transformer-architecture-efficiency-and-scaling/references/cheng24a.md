---
title: "Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context"
source: "https://proceedings.mlr.press/v235/cheng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24a/cheng24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['in-context-learning', 'functional-gradient-descent', 'transformer-theory']
venue: "ICML 2024"
tldr: "Transformers are shown theoretically and empirically to implement functional gradient descent for in-context learning of non-linear functions."
---

# Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context

**Source**: [https://proceedings.mlr.press/v235/cheng24a.html](https://proceedings.mlr.press/v235/cheng24a.html)

**TLDR**: Transformers are shown theoretically and empirically to implement functional gradient descent for in-context learning of non-linear functions.

## Abstract

Many neural network architectures are known to be Turing Complete, and can thus, in principle implement arbitrary algorithms. However, Transformers are unique in that they can implement gradient-based learning algorithms under simple parameter configurations. This paper provides theoretical and empirical evidence that (non-linear) Transformers naturally learn to implement gradient descent in function space, which in turn enable them to learn non-linear functions in context. Our results apply to a broad class of combinations of non-linear architectures and non-linear in-context learning tasks. Additionally, we show that the optimal choice of non-linear activation depends in a natural way on the class of functions that need to be learned.