---
title: "Sliding Down the Stairs: How Correlated Latent Variables Accelerate Learning with Neural Networks"
source: "https://proceedings.mlr.press/v235/bardone24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bardone24a/bardone24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['neural-networks', 'higher-order-cumulants', 'SGD', 'feature-learning', 'latent-variables']
venue: "ICML 2024"
tldr: "Shows that correlated latent variables enable neural networks to efficiently extract higher-order input cumulants, accelerating learning via SGD."
---

# Sliding Down the Stairs: How Correlated Latent Variables Accelerate Learning with Neural Networks

**Source**: [https://proceedings.mlr.press/v235/bardone24a.html](https://proceedings.mlr.press/v235/bardone24a.html)

**TLDR**: Shows that correlated latent variables enable neural networks to efficiently extract higher-order input cumulants, accelerating learning via SGD.

## Abstract

Neural networks extract features from data using stochastic gradient descent (SGD). In particular, higher-order input cumulants (HOCs) are crucial for their performance. However, extracting information from the $p$th cumulant of $d$-dimensional inputs is computationally hard: the number of samples required to recover a single direction from an order-$p$ tensor (tensor PCA) using SGD grows as $d^{p−1}$, which is prohibitive for high-dimensional inputs. This result raises the question of how neural networks extract relevant directions from the HOCs of their inputs efficiently. Here, we show that correlations between latent variables along the directions encoded in different input cumulants speed up learning from higher-order correlations. We show this effect analytically by deriving nearly sharp thresholds for the number of samples required by a single neuron to recover these directions using online SGD from a random start in high dimensions. Our analytical results are confirmed in simulations of two-layer neural networks and unveil a new mechanism for hierarchical learning in neural networks