---
title: "Asymptotics of feature learning in two-layer networks after one gradient-step"
source: "https://proceedings.mlr.press/v235/cui24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cui24d/cui24d.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['feature-learning', 'two-layer-networks', 'gradient-descent']
venue: "ICML 2024"
tldr: "Analyzes asymptotically how two-layer neural networks learn features beyond the kernel regime after a single gradient descent step."
---

# Asymptotics of feature learning in two-layer networks after one gradient-step

**Source**: [https://proceedings.mlr.press/v235/cui24d.html](https://proceedings.mlr.press/v235/cui24d.html)

**TLDR**: Analyzes asymptotically how two-layer neural networks learn features beyond the kernel regime after a single gradient descent step.

## Abstract

In this manuscript, we investigate the problem of how two-layer neural networks learn features from data, and improve over the kernel regime, after being trained with a single gradient descent step. Leveraging the insight from (Ba et al., 2022), we model the trained network by a spiked Random Features (sRF) model. Further building on recent progress on Gaussian universality (Dandi et al., 2023), we provide an exact asymptotic description of the generalization error of the sRF in the high-dimensional limit where the number of samples, the width, and the input dimension grow at a proportional rate. The resulting characterization for sRFs also captures closely the learning curves of the original network model. This enables us to understand how adapting to the data is crucial for the network to efficiently learn non-linear functions in the direction of the gradient - where at initialization it can only express linear functions in this regime.