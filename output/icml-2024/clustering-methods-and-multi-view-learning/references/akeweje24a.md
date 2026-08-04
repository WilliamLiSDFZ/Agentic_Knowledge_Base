---
title: "Learning Mixtures of Gaussian Processes through Random Projection"
source: "https://proceedings.mlr.press/v235/akeweje24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/akeweje24a/akeweje24a.pdf"
categories: ['clustering-methods-and-multi-view-learning']
tags: ['gaussian-process-mixture', 'random-projection', 'functional-data', 'clustering', 'ensemble']
venue: "ICML 2024"
tldr: "Proposes an ensemble clustering framework using random projections to learn mixtures of Gaussian processes in functional data."
---

# Learning Mixtures of Gaussian Processes through Random Projection

**Source**: [https://proceedings.mlr.press/v235/akeweje24a.html](https://proceedings.mlr.press/v235/akeweje24a.html)

**TLDR**: Proposes an ensemble clustering framework using random projections to learn mixtures of Gaussian processes in functional data.

## Abstract

We propose an ensemble clustering framework to uncover latent cluster labels in functional data generated from a Gaussian process mixture. Our method exploits the fact that the projection coefficients of the functional data onto any given projection function follow a univariate Gaussian mixture model (GMM). By conducting multiple one-dimensional projections and learning a univariate GMM for each, we create an ensemble of GMMs. Each GMM serves as a base clustering, and applying ensemble clustering yields a consensus clustering. Our approach significantly reduces computational complexity compared to state-of-the-art methods, and we provide theoretical guarantees on the identifiability and learnability of Gaussian process mixtures. Extensive experiments on synthetic and real datasets confirm the superiority of our method over existing techniques.