---
title: "An Improved Finite-time Analysis of Temporal Difference Learning with Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/ke24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ke24b/ke24b.pdf"
categories: ['neural-network-learning-dynamics-theory', 'online-learning-and-sequential-decision-making']
tags: ['temporal-difference-learning', 'neural-network-approximation', 'finite-time-analysis']
venue: "ICML 2024"
tldr: "Provides an improved finite-time convergence analysis of temporal difference learning with deep neural network function approximation."
---

# An Improved Finite-time Analysis of Temporal Difference Learning with Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/ke24b.html](https://proceedings.mlr.press/v235/ke24b.html)

**TLDR**: Provides an improved finite-time convergence analysis of temporal difference learning with deep neural network function approximation.

## Abstract

Temporal difference (TD) learning algorithms with neural network function parameterization have well-established empirical success in many practical large-scale reinforcement learning tasks. However, theoretical understanding of these algorithms remains challenging due to the nonlinearity of the action-value approximation. In this paper, we develop an improved non-asymptotic analysis of the neural TD method with a general $L$-layer neural network. New proof techniques are developed and an improved new $\tilde{\mathcal{O}}(\epsilon^{-1})$ sample complexity is derived. To our best knowledge, this is the first finite-time analysis of neural TD that achieves an $\tilde{\mathcal{O}}(\epsilon^{-1})$ complexity under the Markovian sampling, as opposed to the best known $\tilde{\mathcal{O}}(\epsilon^{-2})$ complexity in the existing literature.