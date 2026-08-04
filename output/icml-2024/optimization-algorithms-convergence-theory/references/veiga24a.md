---
title: "Stochastic Gradient Flow Dynamics of Test Risk and its Exact Solution for Weak Features"
source: "https://proceedings.mlr.press/v235/veiga24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/veiga24a/veiga24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['stochastic-gradient-flow', 'test-risk', 'path-integral', 'learning-dynamics', 'weak-features']
venue: "ICML 2024"
tldr: "Derives an exact analytical solution for the test risk of stochastic gradient flow dynamics using a path integral formulation in the weak feature regime."
---

# Stochastic Gradient Flow Dynamics of Test Risk and its Exact Solution for Weak Features

**Source**: [https://proceedings.mlr.press/v235/veiga24a.html](https://proceedings.mlr.press/v235/veiga24a.html)

**TLDR**: Derives an exact analytical solution for the test risk of stochastic gradient flow dynamics using a path integral formulation in the weak feature regime.

## Abstract

We investigate the test risk of a continuous time stochastic gradient flow dynamics in learning theory. Using a path integral formulation we provide, in the regime of small learning rate, a general formula for computing the difference between test risk curves of pure gradient and stochastic gradient flows. We apply the general theory to a simple model of weak features, which displays the double descent phenomenon, and explicitly compute the corrections brought about by the added stochastic term in the dynamics, as a function of time and model parameters. The analytical results are compared to simulations of discrete time stochastic gradient descent and show good agreement.