---
title: "Diffusion Tempering Improves Parameter Estimation with Probabilistic Integrators for Ordinary Differential Equations"
source: "https://proceedings.mlr.press/v235/beck24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/beck24a/beck24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'neural-operators-for-pde-solving']
tags: ['ODEs', 'parameter-estimation', 'probabilistic-integrators', 'diffusion-tempering', 'dynamical-systems']
venue: "ICML 2024"
tldr: "Introduces diffusion tempering with probabilistic integrators to improve parameter estimation for ordinary differential equations."
---

# Diffusion Tempering Improves Parameter Estimation with Probabilistic Integrators for Ordinary Differential Equations

**Source**: [https://proceedings.mlr.press/v235/beck24a.html](https://proceedings.mlr.press/v235/beck24a.html)

**TLDR**: Introduces diffusion tempering with probabilistic integrators to improve parameter estimation for ordinary differential equations.

## Abstract

Ordinary differential equations (ODEs) are widely used to describe dynamical systems in science, but identifying parameters that explain experimental measurements is challenging. In particular, although ODEs are differentiable and would allow for gradient-based parameter optimization, the nonlinear dynamics of ODEs often lead to many local minima and extreme sensitivity to initial conditions. We therefore propose diffusion tempering, a novel regularization technique for probabilistic numerical methods which improves convergence of gradient-based parameter optimization in ODEs. By iteratively reducing a noise parameter of the probabilistic integrator, the proposed method converges more reliably to the true parameters. We demonstrate that our method is effective for dynamical systems of different complexity and show that it obtains reliable parameter estimates for a Hodgkin–Huxley model with a practically relevant number of parameters.