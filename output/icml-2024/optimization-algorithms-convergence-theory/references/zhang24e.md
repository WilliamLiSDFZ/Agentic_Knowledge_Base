---
title: "Discounted Adaptive Online Learning: Towards Better Regularization"
source: "https://proceedings.mlr.press/v235/zhang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24e/zhang24e.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-learning', 'discounted-regret', 'nonstationarity']
venue: "ICML 2024"
tldr: "A study of discounted regret in online convex optimization proposing better regularization strategies for nonstationary adversarial environments."
---

# Discounted Adaptive Online Learning: Towards Better Regularization

**Source**: [https://proceedings.mlr.press/v235/zhang24e.html](https://proceedings.mlr.press/v235/zhang24e.html)

**TLDR**: A study of discounted regret in online convex optimization proposing better regularization strategies for nonstationary adversarial environments.

## Abstract

We study online learning in adversarial nonstationary environments. Since the future can be very different from the past, a critical challenge is to gracefully forget the history while new data comes in. To formalize this intuition, we revisit the discounted regret in online convex optimization, and propose an adaptive (i.e., instance optimal), FTRL-based algorithm that improves the widespread non-adaptive baseline – gradient descent with a constant learning rate. From a practical perspective, this refines the classical idea of regularization in lifelong learning: we show that designing better regularizers can be guided by the principled theory of adaptive online optimization. Complementing this result, we also consider the (Gibbs & Candes, 2021)-style online conformal prediction problem, where the goal is to sequentially predict the uncertainty sets of a black-box machine learning model. We show that the FTRL nature of our algorithm can simplify the conventional gradient-descent-based analysis, leading to instance-dependent performance guarantees.