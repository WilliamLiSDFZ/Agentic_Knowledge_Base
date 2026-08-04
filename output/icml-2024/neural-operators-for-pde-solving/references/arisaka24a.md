---
title: "Accelerating Legacy Numerical Solvers by Non-intrusive Gradient-based Meta-solving"
source: "https://proceedings.mlr.press/v235/arisaka24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/arisaka24a/arisaka24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['meta-learning', 'scientific-computing', 'hyperparameter-selection', 'gradient-based', 'solver-acceleration']
venue: "ICML 2024"
tldr: "Accelerates legacy numerical solvers non-intrusively using gradient-based meta-learning for hyperparameter optimization."
---

# Accelerating Legacy Numerical Solvers by Non-intrusive Gradient-based Meta-solving

**Source**: [https://proceedings.mlr.press/v235/arisaka24a.html](https://proceedings.mlr.press/v235/arisaka24a.html)

**TLDR**: Accelerates legacy numerical solvers non-intrusively using gradient-based meta-learning for hyperparameter optimization.

## Abstract

Scientific computing is an essential tool for scientific discovery and engineering design, and its computational cost is always a main concern in practice. To accelerate scientific computing, it is a promising approach to use machine learning (especially meta-learning) techniques for selecting hyperparameters of traditional numerical methods. There have been numerous proposals to this direction, but many of them require automatic-differentiable numerical methods. However, in reality, many practical applications still depend on well-established but non-automatic-differentiable legacy codes, which prevents practitioners from applying the state-of-the-art research to their own problems. To resolve this problem, we propose a non-intrusive methodology with a novel gradient estimation technique to combine machine learning and legacy numerical codes without any modification. We theoretically and numerically show the advantage of the proposed method over other baselines and present applications of accelerating established non-automatic-differentiable numerical solvers implemented in PETSc, a widely used open-source numerical software library.