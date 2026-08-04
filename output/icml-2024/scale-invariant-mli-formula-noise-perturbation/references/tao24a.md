---
title: "MLI Formula: A Nearly Scale-Invariant Solution with Noise Perturbation"
source: "https://proceedings.mlr.press/v235/tao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tao24a/tao24a.pdf"
categories: ['scale-invariant-mli-formula-noise-perturbation', 'neural-network-learning-dynamics-theory']
tags: ['monotonic-linear-interpolation', 'loss-landscape', 'noise-perturbation']
venue: "ICML 2024"
tldr: "A nearly scale-invariant MLI formula with noise perturbation is derived to explain and generalize the monotonic linear interpolation phenomenon in neural network training."
---

# MLI Formula: A Nearly Scale-Invariant Solution with Noise Perturbation

**Source**: [https://proceedings.mlr.press/v235/tao24a.html](https://proceedings.mlr.press/v235/tao24a.html)

**TLDR**: A nearly scale-invariant MLI formula with noise perturbation is derived to explain and generalize the monotonic linear interpolation phenomenon in neural network training.

## Abstract

Monotonic Linear Interpolation (MLI) refers to the peculiar phenomenon that the error between the initial and converged model monotonically decreases along the linear interpolation, i.e., $(1-\alpha)\boldsymbol{\theta}_0 + \alpha \boldsymbol{\theta}_F$. Previous works focus on paired initial and converged points, relating MLI to the smoothness of the optimization trajectory. In this paper, we find a shocking fact that the error curves still exhibit a monotonic decrease when $\boldsymbol{\theta}_0$ is replaced with noise or even zero values, implying that the decreasing curve may be primarily related to the property of the converged model rather than the optimization trajectory. We further explore the relationship between $\alpha\boldsymbol{\theta}_F$ and $\boldsymbol{\theta}_F$ and propose scale invariance properties in various cases, including Generalized Scale Invariance (GSI), Rectified Scale Invariance (RSI), and Normalized Scale Invariance (NSI). From an inverse perspective, the MLI formula is essentially an equation that adds varying levels of noise (i.e., $(1-\alpha)\boldsymbol{\epsilon}$) to a nearly scale-invariant network (i.e., $\alpha \boldsymbol{\theta}_F$), resulting in a monotonically increasing error as the noise level rises. MLI is a special case where $\boldsymbol{\epsilon}$ is equal to $\boldsymbol{\theta}_0$.