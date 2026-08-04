---
title: "Preventing Model Collapse in Gaussian Process Latent Variable Models"
source: "https://proceedings.mlr.press/v235/li24as.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24as/li24as.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['Gaussian-process', 'latent-variable-models', 'dimensionality-reduction', 'model-collapse', 'kernel']
venue: "ICML 2024"
tldr: "A method prevents model collapse in Gaussian process latent variable models by addressing kernel flexibility and projection noise issues."
---

# Preventing Model Collapse in Gaussian Process Latent Variable Models

**Source**: [https://proceedings.mlr.press/v235/li24as.html](https://proceedings.mlr.press/v235/li24as.html)

**TLDR**: A method prevents model collapse in Gaussian process latent variable models by addressing kernel flexibility and projection noise issues.

## Abstract

Gaussian process latent variable models (GPLVMs) are a versatile family of unsupervised learning models commonly used for dimensionality reduction. However, common challenges in modeling data with GPLVMs include inadequate kernel flexibility and improper selection of the projection noise, leading to a type of model collapse characterized by vague latent representations that do not reflect the underlying data structure. This paper addresses these issues by, first, theoretically examining the impact of projection variance on model collapse through the lens of a linear GPLVM. Second, we tackle model collapse due to inadequate kernel flexibility by integrating the spectral mixture (SM) kernel and a differentiable random Fourier feature (RFF) kernel approximation, which ensures computational scalability and efficiency through off-the-shelf automatic differentiation tools for learning the kernel hyperparameters, projection variance, and latent representations within the variational inference framework. The proposed GPLVM, named advisedRFLVM, is evaluated across diverse datasets and consistently outperforms various salient competing models, including state-of-the-art variational autoencoders (VAEs) and other GPLVM variants, in terms of informative latent representations and missing data imputation.