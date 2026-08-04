---
title: "FADAS: Towards Federated Adaptive Asynchronous Optimization"
source: "https://proceedings.mlr.press/v235/wang24bv.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bv/wang24bv.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'asynchronous-optimization', 'adaptive-methods', 'privacy-preserving']
venue: "ICML 2024"
tldr: "Introduces FADAS, a federated adaptive asynchronous optimization algorithm with convergence guarantees for privacy-preserving machine learning."
---

# FADAS: Towards Federated Adaptive Asynchronous Optimization

**Source**: [https://proceedings.mlr.press/v235/wang24bv.html](https://proceedings.mlr.press/v235/wang24bv.html)

**TLDR**: Introduces FADAS, a federated adaptive asynchronous optimization algorithm with convergence guarantees for privacy-preserving machine learning.

## Abstract

Federated learning (FL) has emerged as a widely adopted training paradigm for privacy-preserving machine learning. While the SGD-based FL algorithms have demonstrated considerable success in the past, there is a growing trend towards adopting adaptive federated optimization methods, particularly for the training of large-scale models. However, the conventional synchronous aggregation design poses a significant challenge to the practical deployment of those adaptive federated optimization methods, particularly in the presence of straggler clients. To fill this research gap, this paper introduces federated adaptive asynchronous optimization, named FADAS, a novel method that incorporates asynchronous updates into adaptive federated optimization with provable guarantees. To further enhance the efficiency and resilience of our proposed method in scenarios with significant asynchronous delays, we also extend FADAS with a delay-adaptive learning adjustment strategy. We rigorously establish the convergence rate of the proposed algorithms and empirical results demonstrate the superior performance of FADAS over other asynchronous FL baselines.