---
title: "All-in-one simulation-based inference"
source: "https://proceedings.mlr.press/v235/gloeckler24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gloeckler24a/gloeckler24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['simulation-based-inference', 'amortized-Bayesian-inference', 'neural-posterior-estimation']
venue: "ICML 2024"
tldr: "Introduces an all-in-one simulation-based inference framework that is more simulation-efficient and flexible across varied inference tasks."
---

# All-in-one simulation-based inference

**Source**: [https://proceedings.mlr.press/v235/gloeckler24a.html](https://proceedings.mlr.press/v235/gloeckler24a.html)

**TLDR**: Introduces an all-in-one simulation-based inference framework that is more simulation-efficient and flexible across varied inference tasks.

## Abstract

Amortized Bayesian inference trains neural networks to solve stochastic inference problems using model simulations, thereby making it possible to rapidly perform Bayesian inference for any newly observed data. However, current simulation-based amortized inference methods are simulation-hungry and inflexible: They require the specification of a fixed parametric prior, simulator, and inference tasks ahead of time. Here, we present a new amortized inference method—the Simformer—which overcomes these limitations. By training a probabilistic diffusion model with transformer architectures, the Simformer outperforms current state-of-the-art amortized inference approaches on benchmark tasks and is substantially more flexible: It can be applied to models with function-valued parameters, it can handle inference scenarios with missing or unstructured data, and it can sample arbitrary conditionals of the joint distribution of parameters and data, including both posterior and likelihood. We showcase the performance and flexibility of the Simformer on simulators from ecology, epidemiology, and neuroscience, and demonstrate that it opens up new possibilities and application domains for amortized Bayesian inference on simulation-based models.