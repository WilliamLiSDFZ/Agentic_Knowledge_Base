---
title: "Distributional Bellman Operators over Mean Embeddings"
source: "https://proceedings.mlr.press/v235/wenliang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wenliang24a/wenliang24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'sampling-compression-and-dimensionality-reduction']
tags: ['distributional-reinforcement-learning', 'mean-embeddings', 'temporal-difference', 'sketching']
venue: "ICML 2024"
tldr: "A new algorithmic framework for distributional RL uses finite-dimensional mean embeddings of return distributions to derive novel dynamic programming and TD algorithms."
---

# Distributional Bellman Operators over Mean Embeddings

**Source**: [https://proceedings.mlr.press/v235/wenliang24a.html](https://proceedings.mlr.press/v235/wenliang24a.html)

**TLDR**: A new algorithmic framework for distributional RL uses finite-dimensional mean embeddings of return distributions to derive novel dynamic programming and TD algorithms.

## Abstract

We propose a novel algorithmic framework for distributional reinforcement learning, based on learning finite-dimensional mean embeddings of return distributions. The framework reveals a wide variety of new algorithms for dynamic programming and temporal-difference algorithms that rely on the sketch Bellman operator, which updates mean embeddings with simple linear-algebraic computations. We provide asymptotic convergence theory, and examine the empirical performance of the algorithms on a suite of tabular tasks. Further, we show that this approach can be straightforwardly combined with deep reinforcement learning.