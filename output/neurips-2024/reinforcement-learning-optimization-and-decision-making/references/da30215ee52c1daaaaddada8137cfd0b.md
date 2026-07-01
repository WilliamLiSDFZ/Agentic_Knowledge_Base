---
title: "Scalable Bayesian Optimization via Focalized Sparse Gaussian Processes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/da30215ee52c1daaaaddada8137cfd0b-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'stochastic-optimization-convergence-and-variance-reduction']
tags: ['bayesian-optimization', 'sparse-gaussian-processes', 'scalability']
venue: "NeurIPS 2024"
tldr: "A scalable Bayesian optimization method using focalized sparse Gaussian processes to handle high-dimensional and large-budget problems."
---

# Scalable Bayesian Optimization via Focalized Sparse Gaussian Processes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/da30215ee52c1daaaaddada8137cfd0b-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/da30215ee52c1daaaaddada8137cfd0b-Abstract-Conference.html)

**TLDR**: A scalable Bayesian optimization method using focalized sparse Gaussian processes to handle high-dimensional and large-budget problems.

## Abstract

Bayesian optimization is an effective technique for black-box optimization, but its applicability is typically limited to low-dimensional and small-budget problems due to the cubic complexity of computing the Gaussian process (GP) surrogate. While various approximate GP models have been employed to scale Bayesian optimization to larger sample sizes, most suffer from overly-smooth estimation and focus primarily on problems that allow for large online samples.  In this work, we argue that Bayesian optimization algorithms with sparse GPs can more efficiently allocate their representational power to relevant regions of the search space. To achieve this, we propose focalized GP, which leverages a novel variational loss function to achieve stronger local prediction, as well as FocalBO, which hierarchically optimizes the focalized GP acquisition function over progressively smaller search spaces. Experimental results demonstrate that FocalBO can efficiently leverage large amounts of offline and online data to achieve state-of-the-art performance on robot morphology design and to control a 585-dimensional musculoskeletal system.