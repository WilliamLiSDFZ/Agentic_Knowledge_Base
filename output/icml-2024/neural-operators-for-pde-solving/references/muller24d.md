---
title: "Position: Optimization in SciML Should Employ the Function Space Geometry"
source: "https://proceedings.mlr.press/v235/muller24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muller24d/muller24d.pdf"
categories: ['position-papers-on-ml-research-directions', 'neural-operators-for-pde-solving']
tags: ['function-space-optimization', 'scientific-machine-learning', 'infinite-dimensional', 'discretization']
venue: "ICML 2024"
tldr: "A position paper advocating for first optimizing in function space then discretizing as the principled paradigm for optimization in scientific machine learning."
---

# Position: Optimization in SciML Should Employ the Function Space Geometry

**Source**: [https://proceedings.mlr.press/v235/muller24d.html](https://proceedings.mlr.press/v235/muller24d.html)

**TLDR**: A position paper advocating for first optimizing in function space then discretizing as the principled paradigm for optimization in scientific machine learning.

## Abstract

We provide an infinite-dimensional view on optimization problems encountered in scientific machine learning (SciML) and advocate for the paradigm first optimize, then discretize for their solution. This amounts to first choosing an appropriate infinite-dimensional algorithm which is then discretized in a second step. To illustrate this point, we discuss recently proposed state-of-the-art algorithms for SciML applications and see that they can be derived within this framework. Hence, this perspective allows for a principled guide for the design of optimization algorithms for SciML. As the infinite-dimensional viewpoint is presently underdeveloped we formalize it here to foster the development of novel optimization algorithms.