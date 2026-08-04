---
title: "Simultaneous identification of models and parameters of scientific simulators"
source: "https://proceedings.mlr.press/v235/schroder24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schroder24b/schroder24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['model-selection', 'Bayesian-inference', 'scientific-simulators', 'simulation-based-inference', 'model-components']
venue: "ICML 2024"
tldr: "A Bayesian framework simultaneously identifies model structure and parameters of scientific simulators composed of multiple discrete components."
---

# Simultaneous identification of models and parameters of scientific simulators

**Source**: [https://proceedings.mlr.press/v235/schroder24b.html](https://proceedings.mlr.press/v235/schroder24b.html)

**TLDR**: A Bayesian framework simultaneously identifies model structure and parameters of scientific simulators composed of multiple discrete components.

## Abstract

Many scientific models are composed of multiple discrete components, and scientists often make heuristic decisions about which components to include. Bayesian inference provides a mathematical framework for systematically selecting model components, but defining prior distributions over model components and developing associated inference schemes has been challenging. We approach this problem in a simulation-based inference framework: We define model priors over candidate components and, from model simulations, train neural networks to infer joint probability distributions over both model components and associated parameters. Our method, simulation-based model inference (SBMI), represents distributions over model components as a conditional mixture of multivariate binary distributions in the Grassmann formalism. SBMI can be applied to any compositional stochastic simulator without requiring likelihood evaluations. We evaluate SBMI on a simple time series model and on two scientific models from neuroscience, and show that it can discover multiple data-consistent model configurations, and that it reveals non-identifiable model components and parameters. SBMI provides a powerful tool for data-driven scientific inquiry which will allow scientists to identify essential model components and make uncertainty-informed modelling decisions.