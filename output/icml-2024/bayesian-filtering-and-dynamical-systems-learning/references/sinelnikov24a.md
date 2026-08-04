---
title: "Latent variable model for high-dimensional point process with structured missingness"
source: "https://proceedings.mlr.press/v235/sinelnikov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sinelnikov24a/sinelnikov24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['point-processes', 'latent-variable-models', 'structured-missingness']
venue: "ICML 2024"
tldr: "Proposes a latent variable model for high-dimensional longitudinal point process data with structured missingness patterns."
---

# Latent variable model for high-dimensional point process with structured missingness

**Source**: [https://proceedings.mlr.press/v235/sinelnikov24a.html](https://proceedings.mlr.press/v235/sinelnikov24a.html)

**TLDR**: Proposes a latent variable model for high-dimensional longitudinal point process data with structured missingness patterns.

## Abstract

Longitudinal data are important in numerous fields, such as healthcare, sociology and seismology, but real-world datasets present notable challenges for practitioners because they can be high-dimensional, contain structured missingness patterns, and measurement time points can be governed by an unknown stochastic process. While various solutions have been suggested, the majority of them have been designed to account for only one of these challenges. In this work, we propose a flexible and efficient latent-variable model that is capable of addressing all these limitations. Our approach utilizes Gaussian processes to capture correlations between samples and their associated missingness masks as well as to model the underlying point process. We construct our model as a variational autoencoder together with deep neural network parameterised decoder and encoder models, and develop a scalable amortised variational inference approach for efficient model training. We demonstrate competitive performance using both simulated and real datasets.