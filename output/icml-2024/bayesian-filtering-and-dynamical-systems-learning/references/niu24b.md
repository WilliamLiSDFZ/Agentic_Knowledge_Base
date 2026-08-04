---
title: "Latent Optimal Paths by Gumbel Propagation for Variational Bayesian Dynamic Programming"
source: "https://proceedings.mlr.press/v235/niu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/niu24b/niu24b.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['dynamic-programming', 'Gumbel-distribution', 'variational-inference']
venue: "ICML 2024"
tldr: "Introduces stochastic optimal paths via Gumbel propagation to transform dynamic programming problems into differentiable variational Bayesian frameworks."
---

# Latent Optimal Paths by Gumbel Propagation for Variational Bayesian Dynamic Programming

**Source**: [https://proceedings.mlr.press/v235/niu24b.html](https://proceedings.mlr.press/v235/niu24b.html)

**TLDR**: Introduces stochastic optimal paths via Gumbel propagation to transform dynamic programming problems into differentiable variational Bayesian frameworks.

## Abstract

We propose the stochastic optimal path which solves the classical optimal path problem by a probability-softening solution. This unified approach transforms a wide range of DP problems into directed acyclic graphs in which all paths follow a Gibbs distribution. We show the equivalence of the Gibbs distribution to a message-passing algorithm by the properties of the Gumbel distribution and give all the ingredients required for variational Bayesian inference of a latent path, namely Bayesian dynamic programming (BDP). We demonstrate the usage of BDP in the latent space of variational autoencoders (VAEs) and propose the BDP-VAE which captures structured sparse optimal paths as latent variables. This enables end-to-end training for generative tasks in which models rely on unobserved structural information. At last, we validate the behavior of our approach and showcase its applicability in two real-world applications: text-to-speech and singing voice synthesis. Our implementation code is available at https://github.com/XinleiNIU/LatentOptimalPathsBayesianDP.