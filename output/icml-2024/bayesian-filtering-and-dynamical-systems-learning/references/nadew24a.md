---
title: "Conditionally-Conjugate Gaussian Process Factor Analysis for Spike Count Data via Data Augmentation"
source: "https://proceedings.mlr.press/v235/nadew24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nadew24a/nadew24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning']
tags: ['gaussian-process-factor-analysis', 'neural-spike-data', 'data-augmentation']
venue: "ICML 2024"
tldr: "Data augmentation enables conditionally conjugate GPFA for spike count data, yielding tractable and accurate inference over neural recordings."
---

# Conditionally-Conjugate Gaussian Process Factor Analysis for Spike Count Data via Data Augmentation

**Source**: [https://proceedings.mlr.press/v235/nadew24a.html](https://proceedings.mlr.press/v235/nadew24a.html)

**TLDR**: Data augmentation enables conditionally conjugate GPFA for spike count data, yielding tractable and accurate inference over neural recordings.

## Abstract

Gaussian process factor analysis (GPFA) is a latent variable modeling technique commonly used to identify smooth, low-dimensional latent trajectories underlying high-dimensional neural recordings. Specifically, researchers model spiking rates as Gaussian observations, resulting in tractable inference. Recently, GPFA has been extended to model spike count data. However, due to the non-conjugacy of the likelihood, the inference becomes intractable. Prior works rely on either black-box inference techniques, numerical integration or polynomial approximations of the likelihood to handle intractability. To overcome this challenge, we propose a conditionally-conjugate Gaussian process factor analysis (ccGPFA) resulting in both analytically and computationally tractable inference for modeling neural activity from spike count data. In particular, we develop a novel data augmentation based method that renders the model conditionally conjugate. Consequently, our model enjoys the advantage of simple closed-form updates using a variational EM algorithm. Furthermore, due to its conditional conjugacy, we show our model can be readily scaled using sparse Gaussian Processes and accelerated inference via natural gradients. To validate our method, we empirically demonstrate its efficacy through experiments.