---
title: "Accelerating Convergence in Bayesian Few-Shot Classification"
source: "https://proceedings.mlr.press/v235/ke24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ke24a/ke24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-optimization-and-surrogate-methods']
tags: ['Bayesian-few-shot', 'variational-inference', 'mirror-descent']
venue: "ICML 2024"
tldr: "Integrates mirror descent-based variational inference into Gaussian process few-shot classification to address non-conjugate inference challenges."
---

# Accelerating Convergence in Bayesian Few-Shot Classification

**Source**: [https://proceedings.mlr.press/v235/ke24a.html](https://proceedings.mlr.press/v235/ke24a.html)

**TLDR**: Integrates mirror descent-based variational inference into Gaussian process few-shot classification to address non-conjugate inference challenges.

## Abstract

Bayesian few-shot classification has been a focal point in the field of few-shot learning. This paper seamlessly integrates mirror descent-based variational inference into Gaussian process-based few-shot classification, addressing the challenge of non-conjugate inference. By leveraging non-Euclidean geometry, mirror descent achieves accelerated convergence by providing the steepest descent direction along the corresponding manifold. It also exhibits the parameterization invariance property concerning the variational distribution. Experimental results demonstrate competitive classification accuracy, improved uncertainty quantification, and faster convergence compared to baseline models. Additionally, we investigate the impact of hyperparameters and components. Code is publicly available at https://github.com/keanson/MD-BSFC.