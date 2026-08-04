---
title: "$\bfΦ_\textrmFlow$: Differentiable Simulations for PyTorch, TensorFlow and Jax"
source: "https://proceedings.mlr.press/v235/holl24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/holl24a/holl24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['differentiable-simulation', 'PDE-solving', 'PyTorch', 'scientific-ML']
venue: "ICML 2024"
tldr: "Presents PhiFlow, a differentiable simulation toolkit integrating with PyTorch, TensorFlow, and Jax for physics-based machine learning."
---

# $\bfΦ_\textrmFlow$: Differentiable Simulations for PyTorch, TensorFlow and Jax

**Source**: [https://proceedings.mlr.press/v235/holl24a.html](https://proceedings.mlr.press/v235/holl24a.html)

**TLDR**: Presents PhiFlow, a differentiable simulation toolkit integrating with PyTorch, TensorFlow, and Jax for physics-based machine learning.

## Abstract

Differentiable processes have proven an invaluable tool for machine learning (ML) in scientific and engineering settings, but most ML libraries are not primarily designed for such applications. We present $\Phi_\textrm{Flow}$, a Python toolkit that seamlessly integrates with PyTorch, TensorFlow, Jax and NumPy, simplifying the process of writing differentiable simulation code at every step. $\Phi_\textrm{Flow}$ provides many essential features that go beyond the capabilities of the base libraries, such as differential operators, boundary conditions, the ability to write dimensionality-agnostic code, floating-point precision management, fully differentiable preconditioned (sparse) linear solves, automatic matrix generation via function tracing, integration of SciPy optimizers, simulation vectorization, and visualization tools. At the same time, $\Phi_\textrm{Flow}$ inherits all important traits of the base ML libraries, such as GPU / TPU support, just-in-time compilation, and automatic differentiation. Put together, these features drastically simplify scientific code like PDE or ODE solvers on grids or unstructured meshes, and $\Phi_\textrm{Flow}$ even includes out-of-the-box support for fluid simulations. $\Phi_\textrm{Flow}$ has been used in various publications and as a ground-truth solver in multiple scientific data sets.