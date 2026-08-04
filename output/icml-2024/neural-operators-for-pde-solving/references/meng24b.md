---
title: "Physics-Informed Neural Network Policy Iteration: Algorithms, Convergence, and Verification"
source: "https://proceedings.mlr.press/v235/meng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/meng24b/meng24b.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-operators-for-pde-solving']
tags: ['policy-iteration', 'optimal-control', 'convergence-guarantees']
venue: "ICML 2024"
tldr: "Proposes physics-informed neural network policy iteration algorithms with convergence guarantees for solving high-dimensional nonlinear optimal control problems."
---

# Physics-Informed Neural Network Policy Iteration: Algorithms, Convergence, and Verification

**Source**: [https://proceedings.mlr.press/v235/meng24b.html](https://proceedings.mlr.press/v235/meng24b.html)

**TLDR**: Proposes physics-informed neural network policy iteration algorithms with convergence guarantees for solving high-dimensional nonlinear optimal control problems.

## Abstract

Solving nonlinear optimal control problems is a challenging task, particularly for high-dimensional problems. We propose algorithms for model-based policy iterations to solve nonlinear optimal control problems with convergence guarantees. The main component of our approach is an iterative procedure that utilizes neural approximations to solve linear partial differential equations (PDEs), ensuring convergence. We present two variants of the algorithms. The first variant formulates the optimization problem as a linear least square problem, drawing inspiration from extreme learning machine (ELM) for solving PDEs. This variant efficiently handles low-dimensional problems with high accuracy. The second variant is based on a physics-informed neural network (PINN) for solving PDEs and has the potential to address high-dimensional problems. We demonstrate that both algorithms outperform traditional approaches, such as Galerkin methods, by a significant margin. We provide a theoretical analysis of both algorithms in terms of convergence of neural approximations towards the true optimal solutions in a general setting. Furthermore, we employ formal verification techniques to demonstrate the verifiable stability of the resulting controllers.