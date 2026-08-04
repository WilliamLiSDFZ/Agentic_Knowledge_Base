---
title: "Ai-sampler: Adversarial Learning of Markov kernels with involutive maps"
source: "https://proceedings.mlr.press/v235/egorov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/egorov24a/egorov24a.pdf"
categories: ['generative-models-and-variational-inference', 'probabilistic-generating-circuits-research']
tags: ['mcmc', 'adversarial-training', 'markov-kernels', 'involutive-maps', 'generative-modeling']
venue: "ICML 2024"
tldr: "Parameterizes and trains Markov chain transition kernels adversarially using involutive maps to achieve efficient sampling from complex distributions."
---

# Ai-sampler: Adversarial Learning of Markov kernels with involutive maps

**Source**: [https://proceedings.mlr.press/v235/egorov24a.html](https://proceedings.mlr.press/v235/egorov24a.html)

**TLDR**: Parameterizes and trains Markov chain transition kernels adversarially using involutive maps to achieve efficient sampling from complex distributions.

## Abstract

Markov chain Monte Carlo methods have become popular in statistics as versatile techniques to sample from complicated probability distributions. In this work, we propose a method to parameterize and train transition kernels of Markov chains to achieve efficient sampling and good mixing. This training procedure minimizes the total variation distance between the stationary distribution of the chain and the empirical distribution of the data. Our approach leverages involutive Metropolis-Hastings kernels constructed from reversible neural networks that ensure detailed balance by construction. We find that reversibility also implies $C_2$-equivariance of the discriminator function which can be used to restrict its function space.