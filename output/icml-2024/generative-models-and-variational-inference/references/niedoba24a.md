---
title: "Nearest Neighbour Score Estimators for Diffusion Generative Models"
source: "https://proceedings.mlr.press/v235/niedoba24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/niedoba24a/niedoba24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['score-estimation', 'diffusion-models', 'nearest-neighbor']
venue: "ICML 2024"
tldr: "Proposes a nearest-neighbor based score function estimator for diffusion models that reduces bias and variance compared to existing methods."
---

# Nearest Neighbour Score Estimators for Diffusion Generative Models

**Source**: [https://proceedings.mlr.press/v235/niedoba24a.html](https://proceedings.mlr.press/v235/niedoba24a.html)

**TLDR**: Proposes a nearest-neighbor based score function estimator for diffusion models that reduces bias and variance compared to existing methods.

## Abstract

Score function estimation is the cornerstone of both training and sampling from diffusion generative models. Despite this fact, the most commonly used estimators are either biased neural network approximations or high variance Monte Carlo estimators based on the conditional score. We introduce a novel nearest neighbour score function estimator which utilizes multiple samples from the training set to dramatically decrease estimator variance. We leverage our low variance estimator in two compelling applications. Training consistency models with our estimator, we report a significant increase in both convergence speed and sample quality. In diffusion models, we show that our estimator can replace a learned network for probability-flow ODE integration, opening promising new avenues of future research. Code will be released upon paper acceptance.