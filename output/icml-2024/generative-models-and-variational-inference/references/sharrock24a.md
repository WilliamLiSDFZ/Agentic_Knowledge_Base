---
title: "Sequential Neural Score Estimation: Likelihood-Free Inference with Conditional Score Based Diffusion Models"
source: "https://proceedings.mlr.press/v235/sharrock24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sharrock24a/sharrock24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'generative-models-and-variational-inference']
tags: ['simulation-based-inference', 'score-based-diffusion', 'Bayesian-posterior-estimation']
venue: "ICML 2024"
tldr: "SNPSE introduces sequential score-based diffusion models for likelihood-free Bayesian inference in simulator-based models."
---

# Sequential Neural Score Estimation: Likelihood-Free Inference with Conditional Score Based Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/sharrock24a.html](https://proceedings.mlr.press/v235/sharrock24a.html)

**TLDR**: SNPSE introduces sequential score-based diffusion models for likelihood-free Bayesian inference in simulator-based models.

## Abstract

We introduce Sequential Neural Posterior Score Estimation (SNPSE), a score-based method for Bayesian inference in simulator-based models. Our method, inspired by the remarkable success of score-based methods in generative modelling, leverages conditional score-based diffusion models to generate samples from the posterior distribution of interest. The model is trained using an objective function which directly estimates the score of the posterior. We embed the model into a sequential training procedure, which guides simulations using the current approximation of the posterior at the observation of interest, thereby reducing the simulation cost. We also introduce several alternative sequential approaches, and discuss their relative merits. We then validate our method, as well as its amortised, non-sequential, variant on several numerical examples, demonstrating comparable or superior performance to existing state-of-the-art methods such as Sequential Neural Posterior Estimation (SNPE).