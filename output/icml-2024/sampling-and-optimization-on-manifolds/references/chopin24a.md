---
title: "A connection between Tempering and Entropic Mirror Descent"
source: "https://proceedings.mlr.press/v235/chopin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chopin24a/chopin24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['sequential-monte-carlo', 'tempering', 'mirror-descent']
venue: "ICML 2024"
tldr: "A theoretical connection is established between tempering in SMC and entropic mirror descent for sampling from unnormalized densities."
---

# A connection between Tempering and Entropic Mirror Descent

**Source**: [https://proceedings.mlr.press/v235/chopin24a.html](https://proceedings.mlr.press/v235/chopin24a.html)

**TLDR**: A theoretical connection is established between tempering in SMC and entropic mirror descent for sampling from unnormalized densities.

## Abstract

This paper explores the connections between tempering (for Sequential Monte Carlo; SMC) and entropic mirror descent to sample from a target probability distribution whose unnormalized density is known. We establish that tempering SMC corresponds to entropic mirror descent applied to the reverse Kullback-Leibler (KL) divergence and obtain convergence rates for the tempering iterates. Our result motivates the tempering iterates from an optimization point of view, showing that tempering can be seen as a descent scheme of the KL divergence with respect to the Fisher-Rao geometry, in contrast to Langevin dynamics that perform descent of the KL with respect to the Wasserstein-2 geometry. We exploit the connection between tempering and mirror descent iterates to justify common practices in SMC and derive adaptive tempering rules that improve over other alternative benchmarks in the literature.