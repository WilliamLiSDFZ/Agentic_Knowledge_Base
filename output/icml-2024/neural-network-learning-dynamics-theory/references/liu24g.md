---
title: "ReLU Network with Width $d+\mathcalO(1)$ Can Achieve Optimal Approximation Rate"
source: "https://proceedings.mlr.press/v235/liu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24g/liu24g.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['ReLU-networks', 'narrow-networks', 'approximation-theory']
venue: "ICML 2024"
tldr: "This paper proves that ReLU networks of width d+O(1) are sufficient to achieve optimal function approximation rates."
---

# ReLU Network with Width $d+\mathcalO(1)$ Can Achieve Optimal Approximation Rate

**Source**: [https://proceedings.mlr.press/v235/liu24g.html](https://proceedings.mlr.press/v235/liu24g.html)

**TLDR**: This paper proves that ReLU networks of width d+O(1) are sufficient to achieve optimal function approximation rates.

## Abstract

The prevalent employment of narrow neural networks, characterized by their minimal parameter count per layer, has led to a surge in research exploring their potential as universal function approximators. A notable result in this field states that networks with just a width of $d+1$ can approximate any continuous function for input dimension $d$ arbitrarily well. However, the optimal approximation rate for these narrowest networks, i.e., the optimal relation between the count of tunable parameters and the approximation error, remained unclear. In this paper, we address this gap by proving that ReLU networks with width $d+1$ can achieve the optimal approximation rate for continuous functions over the domain $[0,1]^d$ under $L^p$ norm for $p\in[1,\infty)$. We further show that for the uniform norm, a width of $d+11$ is sufficient. We also extend the results to narrow feed-forward networks with various activations, confirming their capability to approximate at the optimal rate. This work adds to the understanding of universal approximation of narrow networks.