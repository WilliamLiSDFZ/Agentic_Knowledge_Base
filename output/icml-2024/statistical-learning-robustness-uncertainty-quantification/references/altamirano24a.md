---
title: "Robust and Conjugate Gaussian Process Regression"
source: "https://proceedings.mlr.press/v235/altamirano24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/altamirano24a/altamirano24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'bayesian-optimization-and-surrogate-methods']
tags: ['Gaussian-processes', 'robust-regression', 'conjugate-likelihoods']
venue: "ICML 2024"
tldr: "This paper introduces robust and conjugate GP regression methods that maintain closed-form conditioning while relaxing the Gaussian noise assumption."
---

# Robust and Conjugate Gaussian Process Regression

**Source**: [https://proceedings.mlr.press/v235/altamirano24a.html](https://proceedings.mlr.press/v235/altamirano24a.html)

**TLDR**: This paper introduces robust and conjugate GP regression methods that maintain closed-form conditioning while relaxing the Gaussian noise assumption.

## Abstract

To enable closed form conditioning, a common assumption in Gaussian process (GP) regression is independent and identically distributed Gaussian observation noise. This strong and simplistic assumption is often violated in practice, which leads to unreliable inferences and uncertainty quantification. Unfortunately, existing methods for robustifying GPs break closed-form conditioning, which makes them less attractive to practitioners and significantly more computationally expensive. In this paper, we demonstrate how to perform provably robust and conjugate Gaussian process (RCGP) regression at virtually no additional cost using generalised Bayesian inference. RCGP is particularly versatile as it enables exact conjugate closed form updates in all settings where standard GPs admit them. To demonstrate its strong empirical performance, we deploy RCGP for problems ranging from Bayesian optimisation to sparse variational Gaussian processes.