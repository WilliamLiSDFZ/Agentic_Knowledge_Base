---
title: "Why Do You Grok? A Theoretical Analysis on Grokking Modular Addition"
source: "https://proceedings.mlr.press/v235/mohamadi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mohamadi24a/mohamadi24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['grokking', 'modular-addition', 'generalization-theory']
venue: "ICML 2024"
tldr: "Provides a theoretical explanation for the grokking phenomenon in modular addition tasks, linking delayed generalization to gradient descent dynamics."
---

# Why Do You Grok? A Theoretical Analysis on Grokking Modular Addition

**Source**: [https://proceedings.mlr.press/v235/mohamadi24a.html](https://proceedings.mlr.press/v235/mohamadi24a.html)

**TLDR**: Provides a theoretical explanation for the grokking phenomenon in modular addition tasks, linking delayed generalization to gradient descent dynamics.

## Abstract

We present a theoretical explanation of the “grokking” phenomenon (Power et al., 2022), where a model generalizes long after overfitting, for the originally-studied problem of modular addition. First, we show that early in gradient descent, so that the “kernel regime” approximately holds, no permutation-equivariant model can achieve small population error on modular addition unless it sees at least a constant fraction of all possible data points. Eventually, however, models escape the kernel regime. We show that one-hidden-layer quadratic networks that achieve zero training loss with bounded $\ell_\infty$ norm generalize well with substantially fewer training points, and further show such networks exist and can be found by gradient descent with small $\ell_\infty$ regularization. We further provide empirical evidence that these networks leave the kernel regime only after initially overfitting. Taken together, our results strongly support the case for grokking as a consequence of the transition from kernel-like behavior to limiting behavior of gradient descent on deep networks.