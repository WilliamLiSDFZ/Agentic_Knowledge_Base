---
title: "UGrid: An Efficient-And-Rigorous Neural Multigrid Solver for Linear PDEs"
source: "https://proceedings.mlr.press/v235/han24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24a/han24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['multigrid-solver', 'neural-PDE-solver', 'linear-PDEs', 'efficiency', 'rigorous-guarantees']
venue: "ICML 2024"
tldr: "A neural multigrid solver combining deep learning with rigorous numerical guarantees for efficient linear PDE solving."
---

# UGrid: An Efficient-And-Rigorous Neural Multigrid Solver for Linear PDEs

**Source**: [https://proceedings.mlr.press/v235/han24a.html](https://proceedings.mlr.press/v235/han24a.html)

**TLDR**: A neural multigrid solver combining deep learning with rigorous numerical guarantees for efficient linear PDE solving.

## Abstract

Numerical solvers of Partial Differential Equations (PDEs) are of fundamental significance to science and engineering. To date, the historical reliance on legacy techniques has circumscribed possible integration of big data knowledge and exhibits sub-optimal efficiency for certain PDE formulations, while data-driven neural methods typically lack mathematical guarantee of convergence and correctness. This paper articulates a mathematically rigorous neural solver for linear PDEs. The proposed UGrid solver, built upon the principled integration of U-Net and MultiGrid, manifests a mathematically rigorous proof of both convergence and correctness, and showcases high numerical accuracy, as well as strong generalization power to various input geometry/values and multiple PDE formulations. In addition, we devise a new residual loss metric, which enables unsupervised training and affords more stability and a larger solution space over the legacy losses.