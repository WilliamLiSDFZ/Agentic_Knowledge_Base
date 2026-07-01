---
title: "Neural network learns low-dimensional polynomials with SGD near the information-theoretic limit"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6bd5fca2074dcd9ede9de50f71f7ec28-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'statistical-computational-tradeoffs-high-dimensional-learning']
tags: ['SGD', 'single-index-model', 'information-theoretic-limits']
venue: "NeurIPS 2024"
tldr: "Proves that neural networks trained with SGD can learn single-index target functions near the information-theoretic sample complexity limit."
---

# Neural network learns low-dimensional polynomials with SGD near the information-theoretic limit

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6bd5fca2074dcd9ede9de50f71f7ec28-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/6bd5fca2074dcd9ede9de50f71f7ec28-Abstract-Conference.html)

**TLDR**: Proves that neural networks trained with SGD can learn single-index target functions near the information-theoretic sample complexity limit.

## Abstract

We study the problem of gradient descent learning of a single-index target function $f_*(\boldsymbol{x}) = \textstyle\sigma_*\left(\langle\boldsymbol{x},\boldsymbol{\theta}\rangle\right)$ under isotropic Gaussian data in $\mathbb{R}^d$, where the unknown link function $\sigma_*:\mathbb{R}\to\mathbb{R}$ has information exponent $p$ (defined as the lowest degree in the Hermite expansion). Prior works showed that gradient-based training of neural networks can learn this target with $n\gtrsim d^{\Theta(p)}$ samples, and such complexity is predicted to be necessary by the correlational statistical query lower bound. Surprisingly, we prove that a two-layer neural network optimized by an SGD-based algorithm (on the squared loss) learns $f_*$ with a complexity that is not governed by the information exponent. Specifically, for arbitrary polynomial single-index models, we establish a sample and runtime complexity of $n \simeq T = \Theta(d\cdot\mathrm{polylog} d)$, where $\Theta(\cdot)$ hides a constant only depending on the degree of $\sigma_*$; this dimension dependence matches the information theoretic limit up to polylogarithmic factors. More generally, we show that $n\gtrsim d^{(p_*-1)\vee 1}$ samples are sufficient to achieve low generalization error, where $p_* \le p$ is the \textit{generative exponent} of the link function. Core to our analysis is the reuse of minibatch in the gradient computation, which gives rise to higher-order information beyond correlational queries.