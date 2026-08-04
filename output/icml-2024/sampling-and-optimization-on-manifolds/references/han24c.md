---
title: "Riemannian coordinate descent algorithms on matrix manifolds"
source: "https://proceedings.mlr.press/v235/han24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24c/han24c.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning', 'sampling-and-optimization-on-manifolds']
tags: ['riemannian-optimization', 'coordinate-descent', 'matrix-manifolds']
venue: "ICML 2024"
tldr: "Coordinate descent algorithms are developed for optimization on Riemannian matrix manifolds, updating variables block-by-block while maintaining manifold feasibility."
---

# Riemannian coordinate descent algorithms on matrix manifolds

**Source**: [https://proceedings.mlr.press/v235/han24c.html](https://proceedings.mlr.press/v235/han24c.html)

**TLDR**: Coordinate descent algorithms are developed for optimization on Riemannian matrix manifolds, updating variables block-by-block while maintaining manifold feasibility.

## Abstract

Many machine learning applications are naturally formulated as optimization problems on Riemannian manifolds. The main idea behind Riemannian optimization is to maintain the feasibility of the variables while moving along a descent direction on the manifold. This results in updating all the variables at every iteration. In this work, we provide a general framework for developing computationally efficient coordinate descent (CD) algorithms on matrix manifolds that allows updating only a few variables at every iteration while adhering to the manifold constraint. In particular, we propose CD algorithms for various manifolds such as Stiefel, Grassmann, (generalized) hyperbolic, symplectic, and symmetric positive (semi)definite. While the cost per iteration of the proposed CD algorithms is low, we further develop a more efficient variant via a first-order approximation of the objective function. We analyze their convergence and complexity, and empirically illustrate their efficacy in several applications.