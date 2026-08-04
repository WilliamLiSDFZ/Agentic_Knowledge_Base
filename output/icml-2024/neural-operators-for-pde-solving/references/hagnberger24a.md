---
title: "Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations"
source: "https://proceedings.mlr.press/v235/hagnberger24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hagnberger24a/hagnberger24a.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-operators', 'PDE-solving', 'transformers', 'conditional-neural-fields', 'time-dependent']
venue: "ICML 2024"
tldr: "A vectorized conditional neural field framework for efficiently solving time-dependent parametric PDEs with transformers."
---

# Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations

**Source**: [https://proceedings.mlr.press/v235/hagnberger24a.html](https://proceedings.mlr.press/v235/hagnberger24a.html)

**TLDR**: A vectorized conditional neural field framework for efficiently solving time-dependent parametric PDEs with transformers.

## Abstract

Transformer models are increasingly used for solving Partial Differential Equations (PDEs). Several adaptations have been proposed, all of which suffer from the typical problems of Transformers, such as quadratic memory and time complexity. Furthermore, all prevalent architectures for PDE solving lack at least one of several desirable properties of an ideal surrogate model, such as (i) generalization to PDE parameters not seen during training, (ii) spatial and temporal zero-shot super-resolution, (iii) continuous temporal extrapolation, (iv) support for 1D, 2D, and 3D PDEs, and (v) efficient inference for longer temporal rollouts. To address these limitations, we propose Vectorized Conditional Neural Fields (VCNeFs), which represent the solution of time-dependent PDEs as neural fields. Contrary to prior methods, however, VCNeFs compute, for a set of multiple spatio-temporal query points, their solutions in parallel and model their dependencies through attention mechanisms. Moreover, VCNeF can condition the neural field on both the initial conditions and the parameters of the PDEs. An extensive set of experiments demonstrates that VCNeFs are competitive with and often outperform existing ML-based surrogate models.