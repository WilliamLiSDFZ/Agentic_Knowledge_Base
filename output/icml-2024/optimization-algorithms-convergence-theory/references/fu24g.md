---
title: "Mean-field Underdamped Langevin Dynamics and its Spacetime Discretization"
source: "https://proceedings.mlr.press/v235/fu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24g/fu24g.pdf"
categories: ['optimization-algorithms-convergence-theory', 'sampling-and-optimization-on-manifolds']
tags: ['Langevin-dynamics', 'mean-field', 'probability-measure-optimization']
venue: "ICML 2024"
tldr: "An N-particle underdamped Langevin algorithm is proposed for optimizing nonlinear functionals over probability measures with convergence guarantees."
---

# Mean-field Underdamped Langevin Dynamics and its Spacetime Discretization

**Source**: [https://proceedings.mlr.press/v235/fu24g.html](https://proceedings.mlr.press/v235/fu24g.html)

**TLDR**: An N-particle underdamped Langevin algorithm is proposed for optimizing nonlinear functionals over probability measures with convergence guarantees.

## Abstract

We propose a new method called the N-particle underdamped Langevin algorithm for optimizing a special class of non-linear functionals defined over the space of probability measures. Examples of problems with this formulation include training mean-field neural networks, maximum mean discrepancy minimization and kernel Stein discrepancy minimization. Our algorithm is based on a novel spacetime discretization of the mean-field underdamped Langevin dynamics, for which we provide a new, fast mixing guarantee. In addition, we demonstrate that our algorithm converges globally in total variation distance, bridging the theoretical gap between the dynamics and its practical implementation.