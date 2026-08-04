---
title: "InfoNet: Neural Estimation of Mutual Information without Test-Time Optimization"
source: "https://proceedings.mlr.press/v235/hu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24h/hu24h.pdf"
categories: ['sufficient-dimension-reduction-correlation-methods', 'time-series-modeling-and-forecasting-methods']
tags: ['mutual-information', 'neural-estimation', 'amortized', 'information-theory', 'correlation']
venue: "ICML 2024"
tldr: "Proposes InfoNet, an amortized neural estimator for mutual information that avoids test-time optimization and generalizes across variable pairs."
---

# InfoNet: Neural Estimation of Mutual Information without Test-Time Optimization

**Source**: [https://proceedings.mlr.press/v235/hu24h.html](https://proceedings.mlr.press/v235/hu24h.html)

**TLDR**: Proposes InfoNet, an amortized neural estimator for mutual information that avoids test-time optimization and generalizes across variable pairs.

## Abstract

Estimating mutual correlations between random variables or data streams is essential for intelligent behavior and decision-making. As a fundamental quantity for measuring statistical relationships, mutual information has been extensively studied and utilized for its generality and equitability. However, existing methods often lack the efficiency needed for real-time applications, such as test-time optimization of a neural network, or the differentiability required for end-to-end learning, like histograms. We introduce a neural network called InfoNet, which directly outputs mutual information estimations of data streams by leveraging the attention mechanism and the computational efficiency of deep learning infrastructures. By maximizing a dual formulation of mutual information through large-scale simulated training, our approach circumvents time-consuming test-time optimization and offers generalization ability. We evaluate the effectiveness and generalization of our proposed mutual information estimation scheme on various families of distributions and applications. Our results demonstrate that InfoNet and its training process provide a graceful efficiency-accuracy trade-off and order-preserving properties. We will make the code and models available as a comprehensive toolbox to facilitate studies in different fields requiring real-time mutual information estimation.