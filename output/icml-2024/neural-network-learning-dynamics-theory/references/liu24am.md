---
title: "Characterizing ResNet’s Universal Approximation Capability"
source: "https://proceedings.mlr.press/v235/liu24am.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24am/liu24am.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['resnet', 'universal-approximation', 'neural-network-theory']
venue: "ICML 2024"
tldr: "A theoretical characterization of ResNet's universal approximation capability, providing formal understanding of its expressive power."
---

# Characterizing ResNet’s Universal Approximation Capability

**Source**: [https://proceedings.mlr.press/v235/liu24am.html](https://proceedings.mlr.press/v235/liu24am.html)

**TLDR**: A theoretical characterization of ResNet's universal approximation capability, providing formal understanding of its expressive power.

## Abstract

Since its debut in 2016, ResNet has become arguably the most favorable architecture in deep neural network (DNN) design. It effectively addresses the gradient vanishing/exploding issue in DNN training, allowing engineers to fully unleash DNN’s potential in tackling challenging problems in various domains. Despite its practical success, an essential theoretical question remains largely open: how well/best can ResNet approximate functions? In this paper, we answer this question for several important function classes, including polynomials and smooth functions. In particular, we show that ResNet with constant width can approximate Lipschitz continuous function with a Lipschitz constant $\mu$ using $\mathcal{O}(c(d)(\varepsilon/\mu)^{-d/2})$ tunable weights, where $c(d)$ is a constant depending on the input dimension $d$ and $\epsilon>0$ is the target approximation error. Further, we extend such a result to Lebesgue-integrable functions with the upper bound characterized by the modulus of continuity. These results indicate a factor of $d$ reduction in the number of tunable weights compared with the classical results for ReLU networks. Our results are also order-optimal in $\varepsilon$, thus achieving optimal approximation rate, as they match a generalized lower bound derived in this paper. This work adds to the theoretical justifications for ResNet’s stellar practical performance.