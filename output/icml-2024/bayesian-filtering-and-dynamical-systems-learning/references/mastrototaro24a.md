---
title: "Online Variational Sequential Monte Carlo"
source: "https://proceedings.mlr.press/v235/mastrototaro24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mastrototaro24a/mastrototaro24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning']
tags: ['sequential-Monte-Carlo', 'state-space-models', 'online-variational-inference']
venue: "ICML 2024"
tldr: "An online variational sequential Monte Carlo method for efficient parameter learning and latent state inference in state-space models."
---

# Online Variational Sequential Monte Carlo

**Source**: [https://proceedings.mlr.press/v235/mastrototaro24a.html](https://proceedings.mlr.press/v235/mastrototaro24a.html)

**TLDR**: An online variational sequential Monte Carlo method for efficient parameter learning and latent state inference in state-space models.

## Abstract

Being the most classical generative model for serial data, state-space models (SSM) are fundamental in AI and statistical machine learning. In SSM, any form of parameter learning or latent state inference typically involves the computation of complex latent-state posteriors. In this work, we build upon the variational sequential Monte Carlo (VSMC) method, which provides computationally efficient and accurate model parameter estimation and Bayesian latent-state inference by combining particle methods and variational inference. While standard VSMC operates in the offline mode, by re-processing repeatedly a given batch of data, we distribute the approximation of the gradient of the VSMC surrogate ELBO in time using stochastic approximation, allowing for online learning in the presence of streams of data. This results in an algorithm, online VSMC, that is capable of performing efficiently, entirely on-the-fly, both parameter estimation and particle proposal adaptation. In addition, we provide rigorous theoretical results describing the algorithm’s convergence properties as the number of data tends to infinity as well as numerical illustrations of its excellent convergence properties and usefulness also in batch-processing settings.