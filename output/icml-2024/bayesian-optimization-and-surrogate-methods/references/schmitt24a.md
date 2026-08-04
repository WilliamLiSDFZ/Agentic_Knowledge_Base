---
title: "Leveraging Self-Consistency for Data-Efficient Amortized Bayesian Inference"
source: "https://proceedings.mlr.press/v235/schmitt24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schmitt24a/schmitt24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-optimization-and-surrogate-methods']
tags: ['amortized-inference', 'self-consistency', 'Bayes-theorem', 'marginal-likelihood', 'simulation-based-inference']
venue: "ICML 2024"
tldr: "Universal symmetries in joint probabilistic models are leveraged to improve data efficiency and accuracy of amortized Bayesian inference via self-consistency constraints."
---

# Leveraging Self-Consistency for Data-Efficient Amortized Bayesian Inference

**Source**: [https://proceedings.mlr.press/v235/schmitt24a.html](https://proceedings.mlr.press/v235/schmitt24a.html)

**TLDR**: Universal symmetries in joint probabilistic models are leveraged to improve data efficiency and accuracy of amortized Bayesian inference via self-consistency constraints.

## Abstract

We propose a method to improve the efficiency and accuracy of amortized Bayesian inference by leveraging universal symmetries in the joint probabilistic model of parameters and data. In a nutshell, we invert Bayes’ theorem and estimate the marginal likelihood based on approximate representations of the joint model. Upon perfect approximation, the marginal likelihood is constant across all parameter values by definition. However, errors in approximate inference lead to undesirable variance in the marginal likelihood estimates across different parameter values. We penalize violations of this symmetry with a self-consistency loss which significantly improves the quality of approximate inference in low data regimes and can be used to augment the training of popular neural density estimators. We apply our method to a number of synthetic problems and realistic scientific models, discovering notable advantages in the context of both neural posterior and likelihood approximation.