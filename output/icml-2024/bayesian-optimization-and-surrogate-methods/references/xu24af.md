---
title: "Sparse Inducing Points in Deep Gaussian Processes: Enhancing Modeling with Denoising Diffusion Variational Inference"
source: "https://proceedings.mlr.press/v235/xu24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24af/xu24af.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-optimization-and-surrogate-methods']
tags: ['deep-Gaussian-processes', 'inducing-points', 'denoising-diffusion']
venue: "ICML 2024"
tldr: "Enhances deep Gaussian processes by using denoising diffusion variational inference to improve inducing point approximations for posterior estimation."
---

# Sparse Inducing Points in Deep Gaussian Processes: Enhancing Modeling with Denoising Diffusion Variational Inference

**Source**: [https://proceedings.mlr.press/v235/xu24af.html](https://proceedings.mlr.press/v235/xu24af.html)

**TLDR**: Enhances deep Gaussian processes by using denoising diffusion variational inference to improve inducing point approximations for posterior estimation.

## Abstract

Deep Gaussian processes (DGPs) provide a robust paradigm in Bayesian deep learning. In DGPs, a set of sparse integration locations called inducing points are selected to approximate the posterior distribution of the model. This is done to reduce computational complexity and improve model efficiency. However, inferring the posterior distribution of inducing points is not straightforward. Traditional variational inference techniques methods to approximate the posterior often leads to significant bias. To address this issue, we propose an alternative named Denoising Diffusion Variational Inference (DDVI) that utilizes a denoising diffusion stochastic differential equation (SDE) for generating posterior samples of inducing variables. We refer to the score matching method in the denoising diffusion model to approximate challenging score functions using a neural network. Furthermore, by combining classical mathematical theory of SDE with the minimization of KL divergence between the approximate and true processes, we propose a novel explicit variational lower bound for the marginal likelihood function of DGP. Through extensive experiments on various datasets and comparisons with baseline methods, we empirically demonstrate the effectiveness of the DDVI method in posterior inference of inducing points for DGP models.