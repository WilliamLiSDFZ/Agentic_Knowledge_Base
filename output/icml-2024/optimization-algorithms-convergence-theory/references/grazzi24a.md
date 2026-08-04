---
title: "Nonsmooth Implicit Differentiation: Deterministic and Stochastic Convergence Rates"
source: "https://proceedings.mlr.press/v235/grazzi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/grazzi24a/grazzi24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['implicit-differentiation', 'nonsmooth-optimization', 'hyperparameter-optimization']
venue: "ICML 2024"
tldr: "This paper analyzes deterministic and stochastic convergence rates for computing derivatives of fixed points of nondifferentiable contraction maps."
---

# Nonsmooth Implicit Differentiation: Deterministic and Stochastic Convergence Rates

**Source**: [https://proceedings.mlr.press/v235/grazzi24a.html](https://proceedings.mlr.press/v235/grazzi24a.html)

**TLDR**: This paper analyzes deterministic and stochastic convergence rates for computing derivatives of fixed points of nondifferentiable contraction maps.

## Abstract

We study the problem of efficiently computing the derivative of the fixed-point of a parametric nondifferentiable contraction map. This problem has wide applications in machine learning, including hyperparameter optimization, meta-learning and data poisoning attacks. We analyze two popular approaches: iterative differentiation (ITD) and approximate implicit differentiation (AID). A key challenge behind the nonsmooth setting is that the chain rule does not hold anymore. We build upon the work by Bolte et al. (2022), who prove linear convergence of nonsmooth ITD under a piecewise Lipschitz smooth assumption. In the deterministic case, we provide a linear rate for AID and an improved linear rate for ITD which closely match the ones for the smooth setting. We further introduce NSID, a new stochastic method to compute the implicit derivative when the contraction map is defined as the composition of an outer map and an inner map which is accessible only through a stochastic unbiased estimator. We establish rates for the convergence of NSID, encompassing the best available rates in the smooth setting. We also present illustrative experiments confirming our analysis.