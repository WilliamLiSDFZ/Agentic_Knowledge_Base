---
title: "Nonlinear Filtering with Brenier Optimal Transport Maps"
source: "https://proceedings.mlr.press/v235/al-jarrah24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/al-jarrah24a/al-jarrah24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['nonlinear-filtering', 'optimal-transport', 'particle-filters']
venue: "ICML 2024"
tldr: "This paper proposes using Brenier optimal transport maps to improve nonlinear filtering, overcoming limitations of standard sequential importance resampling particle filters."
---

# Nonlinear Filtering with Brenier Optimal Transport Maps

**Source**: [https://proceedings.mlr.press/v235/al-jarrah24a.html](https://proceedings.mlr.press/v235/al-jarrah24a.html)

**TLDR**: This paper proposes using Brenier optimal transport maps to improve nonlinear filtering, overcoming limitations of standard sequential importance resampling particle filters.

## Abstract

This paper is concerned with the problem of nonlinear filtering, i.e., computing the conditional distribution of the state of a stochastic dynamical system given a history of noisy partial observations. Conventional sequential importance resampling (SIR) particle filters suffer from fundamental limitations, in scenarios involving degenerate likelihoods or high-dimensional states, due to the weight degeneracy issue. In this paper, we explore an alternative method, which is based on estimating the Brenier optimal transport (OT) map from the current prior distribution of the state to the posterior distribution at the next time step. Unlike SIR particle filters, the OT formulation does not require the analytical form of the likelihood. Moreover, it allows us to harness the approximation power of neural networks to model complex and multi-modal distributions and employ stochastic optimization algorithms to enhance scalability. Extensive numerical experiments are presented that compare the OT method to the SIR particle filter and the ensemble Kalman filter, evaluating the performance in terms of sample efficiency, high-dimensional scalability, and the ability to capture complex and multi-modal distributions.