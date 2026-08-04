---
title: "Reparameterized Importance Sampling for Robust Variational Bayesian Neural Networks"
source: "https://proceedings.mlr.press/v235/long24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/long24a/long24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['variational-inference', 'Bayesian-neural-networks', 'importance-sampling', 'mean-field']
venue: "ICML 2024"
tldr: "Introduces reparameterized importance sampling to address Monte Carlo sampling limitations in mean-field variational inference for BNNs."
---

# Reparameterized Importance Sampling for Robust Variational Bayesian Neural Networks

**Source**: [https://proceedings.mlr.press/v235/long24a.html](https://proceedings.mlr.press/v235/long24a.html)

**TLDR**: Introduces reparameterized importance sampling to address Monte Carlo sampling limitations in mean-field variational inference for BNNs.

## Abstract

Mean-field variational inference (MFVI) methods provide computationally cheap approximations to the posterior of Bayesian Neural Networks (BNNs) when compared to alternatives like MCMC. However, applying MFVI to BNNs encounters limitations due to the Monte Carlo sampling problem. This problem stems from two main issues. First, most samples do not accurately represent the most probable weights. Second, random sampling from variational distributions introduces high variance in gradient estimates, which can hinder the optimization process, leading to slow convergence or even failure. In this paper, we introduce a novel sampling method called Reparameterized Importance Sampling (RIS) to estimate the first moment in neural networks, reducing variance during feed-forward propagation. We begin by analyzing the generalized form of the optimal proposal distribution and presenting an inexpensive approximation. Next, we describe the sampling process from the proposal distribution as a transformation that combines exogenous randomness with the variational parameters. Our experimental results demonstrate the effectiveness of the proposed RIS method in three critical aspects: improved convergence, enhanced predictive performance, and successful uncertainty estimation for out-of-distribution data.