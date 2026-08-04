---
title: "A Global Geometric Analysis of Maximal Coding Rate Reduction"
source: "https://proceedings.mlr.press/v235/wang24as.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24as/wang24as.pdf"
categories: ['neural-network-learning-dynamics-theory', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['maximal-coding-rate-reduction', 'representation-learning', 'global-geometry', 'deep-networks']
venue: "ICML 2024"
tldr: "A global geometric analysis of the MCR² objective provides theoretical guarantees for structured and compact deep representation learning."
---

# A Global Geometric Analysis of Maximal Coding Rate Reduction

**Source**: [https://proceedings.mlr.press/v235/wang24as.html](https://proceedings.mlr.press/v235/wang24as.html)

**TLDR**: A global geometric analysis of the MCR² objective provides theoretical guarantees for structured and compact deep representation learning.

## Abstract

The maximal coding rate reduction (MCR$^2$) objective for learning structured and compact deep representations is drawing increasing attention, especially after its recent usage in the derivation of fully explainable and highly effective deep network architectures. However, it lacks a complete theoretical justification: only the properties of its global optima are known, and its global landscape has not been studied. In this work, we give a complete characterization of the properties of all its local and global optima as well as other types of critical points. Specifically, we show that each (local or global) maximizer of the MCR$^2$ problem corresponds to a low-dimensional, discriminative, and diverse representation, and furthermore, each critical point of the objective is either a local maximizer or a strict saddle point. Such a favorable landscape makes MCR$^2$ a natural choice of objective for learning diverse and discriminative representations via first-order optimization. To further verify our theoretical findings, we illustrate these properties with extensive experiments on both synthetic and real data sets.