---
title: "A Neural-Preconditioned Poisson Solver for Mixed Dirichlet and Neumann Boundary Conditions"
source: "https://proceedings.mlr.press/v235/lan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lan24a/lan24a.pdf"
categories: ['neural-operators-for-pde-solving', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['neural-preconditioner', 'Poisson-solver', 'mixed-boundary-conditions', 'iterative-solver']
venue: "ICML 2024"
tldr: "A neural network preconditioner for iterative Poisson solvers that handles mixed Dirichlet and Neumann boundary conditions efficiently."
---

# A Neural-Preconditioned Poisson Solver for Mixed Dirichlet and Neumann Boundary Conditions

**Source**: [https://proceedings.mlr.press/v235/lan24a.html](https://proceedings.mlr.press/v235/lan24a.html)

**TLDR**: A neural network preconditioner for iterative Poisson solvers that handles mixed Dirichlet and Neumann boundary conditions efficiently.

## Abstract

We introduce a neural-preconditioned iterative solver for Poisson equations with mixed boundary conditions. Typical Poisson discretizations yield large, ill-conditioned linear systems. Iterative solvers can be effective for these problems, but only when equipped with powerful preconditioners. Unfortunately, effective preconditioners like multigrid require costly setup phases that must be re-executed every time domain shapes or boundary conditions change, forming a severe bottleneck for problems with evolving boundaries. In contrast, we present a neural preconditioner trained to efficiently approximate the inverse of the discrete Laplacian in the presence of such changes. Our approach generalizes to domain shapes, boundary conditions, and grid sizes outside the training set. The key to our preconditioner’s success is a novel, lightweight neural network architecture featuring spatially varying convolution kernels and supporting fast inference. We demonstrate that our solver outperforms state-of-the-art methods like algebraic multigrid as well as recently proposed neural preconditioners on challenging test cases arising from incompressible fluid simulations.