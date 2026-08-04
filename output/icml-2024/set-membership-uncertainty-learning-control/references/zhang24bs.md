---
title: "FESSNC: Fast Exponentially Stable and Safe Neural Controller"
source: "https://proceedings.mlr.press/v235/zhang24bs.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bs/zhang24bs.pdf"
categories: ['set-membership-uncertainty-learning-control', 'optimization-algorithms-convergence-theory']
tags: ['neural-controller', 'stochastic-differential-equations', 'exponential-stability', 'safety', 'nonlinear-control']
venue: "ICML 2024"
tldr: "Designs a fast exponentially stable and safe neural controller for nonlinear stochastic systems with rigorous guarantees."
---

# FESSNC: Fast Exponentially Stable and Safe Neural Controller

**Source**: [https://proceedings.mlr.press/v235/zhang24bs.html](https://proceedings.mlr.press/v235/zhang24bs.html)

**TLDR**: Designs a fast exponentially stable and safe neural controller for nonlinear stochastic systems with rigorous guarantees.

## Abstract

In order to stabilize nonlinear systems modeled by stochastic differential equations, we design a Fast Exponentially Stable and Safe Neural Controller (FESSNC) for fast learning controllers. Our framework is parameterized by neural networks, and realizing both rigorous exponential stability and safety guarantees. Concretely, we design heuristic methods to learn the exponentially stable and the safe controllers, respectively, in light of the classical theory of stochastic exponential stability and our established theorem on guaranteeing the almost-sure safety for stochastic dynamics. More significantly, to rigorously ensure the stability and the safety guarantees for the learned controllers, we develop a projection operator, projecting to the space of exponentially-stable and safe controllers. To reduce the highly computational cost for solving the projection operation, approximate projection operators are delicately proposed with closed forms that map the learned controllers to the target controller space. Furthermore, we employ Hutchinson’s trace estimator for a scalable unbiased estimate of the Hessian matrix that is used in the projection operator, which thus allows for reducing computational cost and, therefore, can accelerate the training and testing processes. More importantly, our approximate projection operations are applicable to the nonparametric control methods, improving their stability and safety performance. We empirically demonstrate the superiority of the FESSNC over the existing methods.