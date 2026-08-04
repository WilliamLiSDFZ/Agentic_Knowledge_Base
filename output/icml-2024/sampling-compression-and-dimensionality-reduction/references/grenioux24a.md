---
title: "Stochastic Localization via Iterative Posterior Sampling"
source: "https://proceedings.mlr.press/v235/grenioux24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/grenioux24a/grenioux24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['stochastic-localization', 'score-based-generative-models', 'posterior-sampling']
venue: "ICML 2024"
tldr: "This paper connects stochastic localization with iterative posterior sampling to develop improved score-based generative modeling techniques."
---

# Stochastic Localization via Iterative Posterior Sampling

**Source**: [https://proceedings.mlr.press/v235/grenioux24a.html](https://proceedings.mlr.press/v235/grenioux24a.html)

**TLDR**: This paper connects stochastic localization with iterative posterior sampling to develop improved score-based generative modeling techniques.

## Abstract

Building upon score-based learning, new interest in stochastic localization techniques has recently emerged. In these models, one seeks to noise a sample from the data distribution through a stochastic process, called observation process, and progressively learns a denoiser associated to this dynamics. Apart from specific applications, the use of stochastic localization for the problem of sampling from an unnormalized target density has not been explored extensively. This work contributes to fill this gap. We consider a general stochastic localization framework and introduce an explicit class of observation processes, associated with flexible denoising schedules. We provide a complete methodology, Stochastic Localization via Iterative Posterior Sampling (SLIPS), to obtain approximate samples of these dynamics, and as a by-product, samples from the target distribution. Our scheme is based on a Markov chain Monte Carlo estimation of the denoiser and comes with detailed practical guidelines. We illustrate the benefits and applicability of SLIPS on several benchmarks of multi-modal distributions, including Gaussian mixtures in increasing dimensions, Bayesian logistic regression and a high-dimensional field system from statistical-mechanics.