---
title: "HelmFluid: Learning Helmholtz Dynamics for Interpretable Fluid Prediction"
source: "https://proceedings.mlr.press/v235/xing24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xing24c/xing24c.pdf"
categories: ['neural-operators-for-pde-solving', 'time-series-modeling-and-forecasting-methods']
tags: ['fluid-dynamics', 'Helmholtz-decomposition', 'neural-operators']
venue: "ICML 2024"
tldr: "HelmFluid incorporates Helmholtz decomposition into deep learning for interpretable and physically grounded fluid dynamics prediction."
---

# HelmFluid: Learning Helmholtz Dynamics for Interpretable Fluid Prediction

**Source**: [https://proceedings.mlr.press/v235/xing24c.html](https://proceedings.mlr.press/v235/xing24c.html)

**TLDR**: HelmFluid incorporates Helmholtz decomposition into deep learning for interpretable and physically grounded fluid dynamics prediction.

## Abstract

Fluid prediction is a long-standing challenge due to the intrinsic high-dimensional non-linear dynamics. Previous methods usually utilize the non-linear modeling capability of deep models to directly estimate velocity fields for future prediction. However, skipping over inherent physical properties but directly learning superficial velocity fields will overwhelm the model from generating precise or physics-reliable results. In this paper, we propose the HelmFluid toward an accurate and interpretable predictor for fluid. Inspired by the Helmholtz theorem, we design a HelmDynamics block to learn Helmholtz dynamics, which decomposes fluid dynamics into more solvable curl-free and divergence-free parts, physically corresponding to potential and stream functions of fluid. By embedding the HelmDynamics block into a Multiscale Multihead Integral Architecture, HelmFluid can integrate learned Helmholtz dynamics along temporal dimension in multiple spatial scales to yield future fluid. Compared with previous velocity estimating methods, HelmFluid is faithfully derived from Helmholtz theorem and ravels out complex fluid dynamics with physically interpretable evidence. Experimentally, HelmFluid achieves consistent state-of-the-art in both numerical simulated and real-world observed benchmarks, even for scenarios with complex boundaries.