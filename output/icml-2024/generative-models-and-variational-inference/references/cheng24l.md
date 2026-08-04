---
title: "Kernel Semi-Implicit Variational Inference"
source: "https://proceedings.mlr.press/v235/cheng24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24l/cheng24l.pdf"
categories: ['generative-models-and-variational-inference', 'neural-operators-for-pde-solving']
tags: ['variational-inference', 'semi-implicit-distributions', 'kernel-methods']
venue: "ICML 2024"
tldr: "Kernel Semi-Implicit Variational Inference improves ELBO estimation for semi-implicit variational families using kernel-based techniques."
---

# Kernel Semi-Implicit Variational Inference

**Source**: [https://proceedings.mlr.press/v235/cheng24l.html](https://proceedings.mlr.press/v235/cheng24l.html)

**TLDR**: Kernel Semi-Implicit Variational Inference improves ELBO estimation for semi-implicit variational families using kernel-based techniques.

## Abstract

Semi-implicit variational inference (SIVI) extends traditional variational families with semi-implicit distributions defined in a hierarchical manner. Due to the intractable densities of semi-implicit distributions, classical SIVI often resorts to surrogates of evidence lower bound (ELBO) that would introduce biases for training. A recent advancement in SIVI, named SIVI-SM, utilizes an alternative score matching objective made tractable via a minimax formulation, albeit requiring an additional lower-level optimization. In this paper, we propose kernel SIVI (KSIVI), a variant of SIVI-SM that eliminates the need for the lower-level optimization through kernel tricks. Specifically, we show that when optimizing over a reproducing kernel Hilbert space (RKHS), the lower-level problem has an explicit solution. This way, the upper-level objective becomes the kernel Stein discrepancy (KSD), which is readily computable for stochastic gradient descent due to the hierarchical structure of semi-implicit variational distributions. An upper bound for the variance of the Monte Carlo gradient estimators of the KSD objective is derived, which allows us to establish novel convergence guarantees of KSIVI. We demonstrate the effectiveness and efficiency of KSIVI on both synthetic distributions and a variety of real data Bayesian inference tasks.