---
title: "Self-Supervised Coarsening of Unstructured Grid with Automatic Differentiation"
source: "https://proceedings.mlr.press/v235/shumilin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shumilin24a/shumilin24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['mesh-coarsening', 'automatic-differentiation', 'numerical-simulation']
venue: "ICML 2024"
tldr: "Presents a self-supervised algorithm for coarsening unstructured grids using automatic differentiation to reduce computational load in numerical simulations."
---

# Self-Supervised Coarsening of Unstructured Grid with Automatic Differentiation

**Source**: [https://proceedings.mlr.press/v235/shumilin24a.html](https://proceedings.mlr.press/v235/shumilin24a.html)

**TLDR**: Presents a self-supervised algorithm for coarsening unstructured grids using automatic differentiation to reduce computational load in numerical simulations.

## Abstract

Due to the high computational load of modern numerical simulation, there is a demand for approaches that would reduce the size of discrete problems while keeping the accuracy reasonable. In this work, we present an original algorithm to coarsen an unstructured grid based on the concepts of differentiable physics. We achieve this by employing $k$-means clustering, autodifferentiation and stochastic minimization algorithms. We demonstrate performance of the designed algorithm on two PDEs: a linear parabolic equation which governs slightly compressible fluid flow in porous media and the wave equation. Our results show that in the considered scenarios, we reduced the number of grid points up to 10 times while preserving the modeled variable dynamics in the points of interest. The proposed approach can be applied to the simulation of an arbitrary system described by evolutionary partial differential equations.