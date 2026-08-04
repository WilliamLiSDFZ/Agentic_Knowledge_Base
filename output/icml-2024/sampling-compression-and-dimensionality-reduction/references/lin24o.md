---
title: "Fast and Sample Efficient Multi-Task Representation Learning in Stochastic Contextual Bandits"
source: "https://proceedings.mlr.press/v235/lin24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24o/lin24o.pdf"
categories: ['online-learning-and-sequential-decision-making', 'sampling-compression-and-dimensionality-reduction']
tags: ['contextual-bandits', 'representation-learning', 'multi-task']
venue: "ICML 2024"
tldr: "A fast and sample-efficient algorithm for multi-task representation learning in stochastic linear contextual bandits."
---

# Fast and Sample Efficient Multi-Task Representation Learning in Stochastic Contextual Bandits

**Source**: [https://proceedings.mlr.press/v235/lin24o.html](https://proceedings.mlr.press/v235/lin24o.html)

**TLDR**: A fast and sample-efficient algorithm for multi-task representation learning in stochastic linear contextual bandits.

## Abstract

We study how representation learning can improve the learning efficiency of contextual bandit problems. We study the setting where we play T linear contextual bandits with dimension simultaneously, and these T bandit tasks collectively share a common linear representation with a dimensionality of r ≪ d. We present a new algorithm based on alternating projected gradient descent (GD) and minimization estimator to recover a low-rank feature matrix. We obtain constructive provable guarantees for our estimator that provide a lower bound on the required sample complexity and an upper bound on the iteration complexity (total number of iterations needed to achieve a certain error level). Using the proposed estimator, we present a multi-task learning algorithm for linear contextual bandits and prove the regret bound of our algorithm. We presented experiments and compared the performance of our algorithm against benchmark algorithms.