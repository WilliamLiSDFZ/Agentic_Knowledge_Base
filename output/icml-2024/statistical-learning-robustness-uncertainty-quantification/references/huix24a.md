---
title: "Theoretical Guarantees for Variational Inference with Fixed-Variance Mixture of Gaussians"
source: "https://proceedings.mlr.press/v235/huix24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huix24a/huix24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['variational-inference', 'mixture-of-gaussians', 'theoretical-guarantees', 'KL-divergence', 'posterior-approximation']
venue: "ICML 2024"
tldr: "Provides theoretical guarantees for variational inference using fixed-variance Gaussian mixture approximations of posterior distributions."
---

# Theoretical Guarantees for Variational Inference with Fixed-Variance Mixture of Gaussians

**Source**: [https://proceedings.mlr.press/v235/huix24a.html](https://proceedings.mlr.press/v235/huix24a.html)

**TLDR**: Provides theoretical guarantees for variational inference using fixed-variance Gaussian mixture approximations of posterior distributions.

## Abstract

Variational inference (VI) is a popular approach in Bayesian inference, that looks for the best approximation of the posterior distribution within a parametric family, minimizing a loss that is (typically) the reverse Kullback-Leibler (KL) divergence. Despite its empirical success, the theoretical properties of VI have only recently received attention, and is restricted to the Gaussian case. This research paper aims to contribute to the theoretical study of VI in the non-Gaussian case by investigating the setting of Mixture of Gaussians with fixed covariance. In this view, VI over this specific family can be casted as the minimization of a Mollified relative entropy, i.e. the KL between the convolution (with respect to a Gaussian kernel) of an atomic measure supported on Diracs, where the support of the atomic measure correspond to the localization of the Gaussian components, and the target distribution. Hence, solving variational inference is equivalent to optimizing the positions of the Diracs (the particles), which can be done through gradient descent and takes the form of an interacting particle system. We study two sources of error in variational inference in this context. The first is an optimization result that is a descent lemma establishing that the algorithm decreases the objective at each iteration. The second is an approximation error that upper bounds the mollified relative entropy between an optimal finite mixture and the target distribution.