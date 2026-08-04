---
title: "Statistically Optimal Generative Modeling with Maximum Deviation from the Empirical Distribution"
source: "https://proceedings.mlr.press/v235/vardanyan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vardanyan24a/vardanyan24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['generative-modeling', 'statistical-optimality', 'empirical-distribution', 'diversity', 'sample-complexity']
venue: "ICML 2024"
tldr: "Provides a mathematical framework for evaluating generative models by measuring maximum deviation from the empirical distribution to ensure statistical optimality and diversity."
---

# Statistically Optimal Generative Modeling with Maximum Deviation from the Empirical Distribution

**Source**: [https://proceedings.mlr.press/v235/vardanyan24a.html](https://proceedings.mlr.press/v235/vardanyan24a.html)

**TLDR**: Provides a mathematical framework for evaluating generative models by measuring maximum deviation from the empirical distribution to ensure statistical optimality and diversity.

## Abstract

This paper explores the problem of generative modeling, aiming to simulate diverse examples from an unknown distribution based on observed examples. While recent studies have focused on quantifying the statistical precision of popular algorithms, there is a lack of mathematical evaluation regarding the non-replication of observed examples and the creativity of the generative model. We present theoretical insights into this aspect, demonstrating that the Wasserstein GAN, constrained to left-invertible push-forward maps, generates distributions that not only avoid replication but also significantly deviate from the empirical distribution. Importantly, we show that left-invertibility achieves this without compromising the statistical optimality of the resulting generator. Our most important contribution provides a finite-sample lower bound on the Wasserstein-1 distance between the generative distribution and the empirical one. We also establish a finite-sample upper bound on the distance between the generative distribution and the true data-generating one. Both bounds are explicit and show the impact of key parameters such as sample size, dimensions of the ambient and latent spaces, noise level, and smoothness measured by the Lipschitz constant.