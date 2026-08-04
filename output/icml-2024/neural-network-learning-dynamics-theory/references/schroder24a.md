---
title: "Asymptotics of Learning with Deep Structured (Random) Features"
source: "https://proceedings.mlr.press/v235/schroder24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schroder24a/schroder24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['random-features', 'deep-networks', 'asymptotic-analysis', 'generalization', 'high-dimensional']
venue: "ICML 2024"
tldr: "A tight asymptotic characterization of test error for learning with deep structured random features is derived in the proportional high-dimensional limit."
---

# Asymptotics of Learning with Deep Structured (Random) Features

**Source**: [https://proceedings.mlr.press/v235/schroder24a.html](https://proceedings.mlr.press/v235/schroder24a.html)

**TLDR**: A tight asymptotic characterization of test error for learning with deep structured random features is derived in the proportional high-dimensional limit.

## Abstract

For a large class of feature maps we provide a tight asymptotic characterisation of the test error associated with learning the readout layer, in the high-dimensional limit where the input dimension, hidden layer widths, and number of training samples are proportionally large. This characterization is formulated in terms of the population covariance of the features. Our work is partially motivated by the problem of learning with Gaussian rainbow neural networks, namely deep non-linear fully-connected networks with random but structured weights, whose row-wise covariances are further allowed to depend on the weights of previous layers. For such networks we also derive a closed-form formula for the feature covariance in terms of the weight matrices. We further find that in some cases our results can capture feature maps learned by deep, finite-width neural networks trained under gradient descent.