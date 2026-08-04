---
title: "Subhomogeneous Deep Equilibrium Models"
source: "https://proceedings.mlr.press/v235/sittoni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sittoni24a/sittoni24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['implicit-depth-networks', 'deep-equilibrium-models', 'fixed-point-theory', 'stability']
venue: "ICML 2024"
tldr: "A new class of subhomogeneous deep equilibrium models is presented with provable existence and uniqueness guarantees for improved stability and reproducibility."
---

# Subhomogeneous Deep Equilibrium Models

**Source**: [https://proceedings.mlr.press/v235/sittoni24a.html](https://proceedings.mlr.press/v235/sittoni24a.html)

**TLDR**: A new class of subhomogeneous deep equilibrium models is presented with provable existence and uniqueness guarantees for improved stability and reproducibility.

## Abstract

Implicit-depth neural networks have grown as powerful alternatives to traditional networks in various applications in recent years. However, these models often lack guarantees of existence and uniqueness, raising stability, performance, and reproducibility issues. In this paper, we present a new analysis of the existence and uniqueness of fixed points for implicit-depth neural networks based on the concept of subhomogeneous operators and the nonlinear Perron-Frobenius theory. Compared to previous similar analyses, our theory allows for weaker assumptions on the parameter matrices, thus yielding a more flexible framework for well-defined implicit networks. We illustrate the performance of the resulting subhomogeneous networks on feedforward, convolutional, and graph neural network examples