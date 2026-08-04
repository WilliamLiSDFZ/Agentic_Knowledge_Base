---
title: "Learning to Explore for Stochastic Gradient MCMC"
source: "https://proceedings.mlr.press/v235/kim24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24k/kim24k.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['bayesian-neural-networks', 'SGMCMC', 'posterior-inference']
venue: "ICML 2024"
tldr: "Proposes a learned exploration strategy for stochastic gradient MCMC to better handle multimodal posteriors in Bayesian neural networks."
---

# Learning to Explore for Stochastic Gradient MCMC

**Source**: [https://proceedings.mlr.press/v235/kim24k.html](https://proceedings.mlr.press/v235/kim24k.html)

**TLDR**: Proposes a learned exploration strategy for stochastic gradient MCMC to better handle multimodal posteriors in Bayesian neural networks.

## Abstract

Bayesian Neural Networks(BNNs) with high-dimensional parameters pose a challenge for posterior inference due to the multi-modality of the posterior distributions. Stochastic Gradient Markov Chain Monte Carlo(SGMCMC) with cyclical learning rate scheduling is a promising solution, but it requires a large number of sampling steps to explore high-dimensional multi-modal posteriors, making it computationally expensive. In this paper, we propose a meta-learning strategy to build SGMCMC which can efficiently explore the multi-modal target distributions. Our algorithm allows the learned SGMCMC to quickly explore the high-density region of the posterior landscape. Also, we show that this exploration property is transferrable to various tasks, even for the ones unseen during a meta-training stage. Using popular image classification benchmarks and a variety of downstream tasks, we demonstrate that our method significantly improves the sampling efficiency, achieving better performance than vanilla SGMCMC without incurring significant computational overhead.