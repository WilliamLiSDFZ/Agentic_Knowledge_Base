---
title: "An Online Optimization Perspective on First-Order and Zero-Order Decentralized Nonsmooth Nonconvex Stochastic Optimization"
source: "https://proceedings.mlr.press/v235/sahinoglu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sahinoglu24a/sahinoglu24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'privacy-preserving-federated-and-distributed-learning']
tags: ['decentralized-optimization', 'nonsmooth-nonconvex', 'stochastic-optimization', 'online-optimization', 'multi-agent']
venue: "ICML 2024"
tldr: "An online optimization perspective yields novel finite-time guarantees for finding stationary points in decentralized nonsmooth nonconvex stochastic optimization."
---

# An Online Optimization Perspective on First-Order and Zero-Order Decentralized Nonsmooth Nonconvex Stochastic Optimization

**Source**: [https://proceedings.mlr.press/v235/sahinoglu24a.html](https://proceedings.mlr.press/v235/sahinoglu24a.html)

**TLDR**: An online optimization perspective yields novel finite-time guarantees for finding stationary points in decentralized nonsmooth nonconvex stochastic optimization.

## Abstract

We investigate the finite-time analysis of finding ($\delta, \epsilon$)-stationary points for nonsmooth nonconvex objectives in decentralized stochastic optimization. A set of agents aim at minimizing a global function using only their local information by interacting over a network. We present a novel algorithm, called Multi Epoch Decentralized Online Learning (ME-DOL), for which we establish the sample complexity in various settings. First, using a recently proposed online-to-nonconvex technique, we show that our algorithm recovers the optimal convergence rate of smooth nonconvex objectives. We then extend our analysis to the nonsmooth setting, building on properties of randomized smoothing and Goldstein-subdifferential sets. We establish the sample complexity of $O(\delta^{-1}\epsilon^{-3})$, which to the best of our knowledge is the first finite-time guarantee for decentralized nonsmooth nonconvex stochastic optimization in the first-order setting (without weak-convexity), matching its optimal centralized counterpart. We further prove the same rate for the zero-order oracle setting without using variance reduction.