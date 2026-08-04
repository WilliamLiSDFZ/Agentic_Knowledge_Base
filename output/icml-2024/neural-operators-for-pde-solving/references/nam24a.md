---
title: "Solving Poisson Equations using Neural Walk-on-Spheres"
source: "https://proceedings.mlr.press/v235/nam24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nam24a/nam24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['neural-pde-solver', 'walk-on-spheres', 'poisson-equation']
venue: "ICML 2024"
tldr: "Neural Walk-on-Spheres combines stochastic representations with neural networks for efficient high-dimensional Poisson equation solving."
---

# Solving Poisson Equations using Neural Walk-on-Spheres

**Source**: [https://proceedings.mlr.press/v235/nam24a.html](https://proceedings.mlr.press/v235/nam24a.html)

**TLDR**: Neural Walk-on-Spheres combines stochastic representations with neural networks for efficient high-dimensional Poisson equation solving.

## Abstract

We propose Neural Walk-on-Spheres (NWoS), a novel neural PDE solver for the efficient solution of high-dimensional Poisson equations. Leveraging stochastic representations and Walk-on-Spheres methods, we develop novel losses for neural networks based on the recursive solution of Poisson equations on spheres inside the domain. The resulting method is highly parallelizable and does not require spatial gradients for the loss. We provide a comprehensive comparison against competing methods based on PINNs, the Deep Ritz method, and (backward) stochastic differential equations. In several challenging, high-dimensional numerical examples, we demonstrate the superiority of NWoS in accuracy, speed, and computational costs. Compared to commonly used PINNs, our approach can reduce memory usage and errors by orders of magnitude. Furthermore, we apply NWoS to problems in PDE-constrained optimization and molecular dynamics to show its efficiency in practical applications.