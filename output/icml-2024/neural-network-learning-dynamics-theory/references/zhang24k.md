---
title: "Random Scaling and Momentum for Non-smooth Non-convex Optimization"
source: "https://proceedings.mlr.press/v235/zhang24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24k/zhang24k.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['SGD-momentum', 'non-smooth-optimization', 'random-scaling']
venue: "ICML 2024"
tldr: "Random scaling combined with momentum enables provable convergence for stochastic gradient descent on non-smooth non-convex neural network loss functions."
---

# Random Scaling and Momentum for Non-smooth Non-convex Optimization

**Source**: [https://proceedings.mlr.press/v235/zhang24k.html](https://proceedings.mlr.press/v235/zhang24k.html)

**TLDR**: Random scaling combined with momentum enables provable convergence for stochastic gradient descent on non-smooth non-convex neural network loss functions.

## Abstract

Training neural networks requires optimizing a loss function that may be highly irregular, and in particular neither convex nor smooth. Popular training algorithms are based on stochastic gradient descent with momentum (SGDM), for which classical analysis applies only if the loss is either convex or smooth. We show that a very small modification to SGDM closes this gap: simply scale the update at each time point by an exponentially distributed random scalar. The resulting algorithm achieves optimal convergence guarantees. Intriguingly, this result is not derived by a specific analysis of SGDM: instead, it falls naturally out of a more general framework for converting online convex optimization algorithms to non-convex optimization algorithms.