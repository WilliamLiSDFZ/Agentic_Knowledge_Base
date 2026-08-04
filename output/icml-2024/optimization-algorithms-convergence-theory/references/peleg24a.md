---
title: "Bias of Stochastic Gradient Descent or the Architecture: Disentangling the Effects of Overparameterization of Neural Networks"
source: "https://proceedings.mlr.press/v235/peleg24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peleg24a/peleg24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['overparameterization', 'implicit-bias', 'SGD', 'neural-networks', 'generalization']
venue: "ICML 2024"
tldr: "Disentangles the effects of SGD implicit bias and architecture simplicity bias on generalization in overparameterized neural networks."
---

# Bias of Stochastic Gradient Descent or the Architecture: Disentangling the Effects of Overparameterization of Neural Networks

**Source**: [https://proceedings.mlr.press/v235/peleg24a.html](https://proceedings.mlr.press/v235/peleg24a.html)

**TLDR**: Disentangles the effects of SGD implicit bias and architecture simplicity bias on generalization in overparameterized neural networks.

## Abstract

Neural networks typically generalize well when fitting the data perfectly, even though they are heavily overparameterized. Many factors have been pointed out as the reason for this phenomenon, including an implicit bias of stochastic gradient descent (SGD) and a possible simplicity bias arising from the neural network architecture. The goal of this paper is to disentangle the factors that influence generalization stemming from optimization and architectural choices by studying random and SGD-optimized networks that achieve zero training error. We experimentally show, in the low sample regime, that overparameterization in terms of increasing width is beneficial for generalization, and this benefit is due to the bias of SGD and not due to an architectural bias. In contrast, for increasing depth, overparameterization is detrimental for generalization, but random and SGD-optimized networks behave similarly, so this can be attributed to an architectural bias.