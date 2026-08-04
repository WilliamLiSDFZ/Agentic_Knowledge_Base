---
title: "Minimizing $f$-Divergences by Interpolating Velocity Fields"
source: "https://proceedings.mlr.press/v235/liu24by.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24by/liu24by.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['f-divergence', 'wasserstein-gradient-flow', 'particle-methods', 'velocity-field-interpolation', 'distribution-approximation']
venue: "ICML 2024"
tldr: "A method to minimize f-divergences by interpolating velocity fields along Wasserstein gradient flow paths to efficiently move particles toward target distributions."
---

# Minimizing $f$-Divergences by Interpolating Velocity Fields

**Source**: [https://proceedings.mlr.press/v235/liu24by.html](https://proceedings.mlr.press/v235/liu24by.html)

**TLDR**: A method to minimize f-divergences by interpolating velocity fields along Wasserstein gradient flow paths to efficiently move particles toward target distributions.

## Abstract

Many machine learning problems can be seen as approximating a target distribution using a particle distribution by minimizing their statistical discrepancy. Wasserstein Gradient Flow can move particles along a path that minimizes the $f$-divergence between the target and particle distributions. To move particles, we need to calculate the corresponding velocity fields derived from a density ratio function between these two distributions. Previous works estimated such density ratio functions and then differentiated the estimated ratios. These approaches may suffer from overfitting, leading to a less accurate estimate of the velocity fields. Inspired by non-parametric curve fitting, we directly estimate these velocity fields using interpolation techniques. We prove that our estimators are consistent under mild conditions. We validate their effectiveness using novel applications on domain adaptation and missing data imputation. The code for reproducing our results can be found at https://github.com/anewgithubname/gradest2.