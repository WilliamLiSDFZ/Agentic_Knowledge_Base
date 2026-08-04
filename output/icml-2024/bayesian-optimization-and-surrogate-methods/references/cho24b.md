---
title: "Parameterized Physics-informed Neural Networks for Parameterized PDEs"
source: "https://proceedings.mlr.press/v235/cho24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24b/cho24b.pdf"
categories: ['neural-operators-for-pde-solving', 'bayesian-optimization-and-surrogate-methods']
tags: ['physics-informed-neural-networks', 'parameterized-PDEs', 'surrogate-models']
venue: "ICML 2024"
tldr: "Parameterized PINNs are proposed to efficiently solve families of PDEs with varying parameters without retraining from scratch."
---

# Parameterized Physics-informed Neural Networks for Parameterized PDEs

**Source**: [https://proceedings.mlr.press/v235/cho24b.html](https://proceedings.mlr.press/v235/cho24b.html)

**TLDR**: Parameterized PINNs are proposed to efficiently solve families of PDEs with varying parameters without retraining from scratch.

## Abstract

Complex physical systems are often described by partial differential equations (PDEs) that depend on parameters such as the Raynolds number in fluid mechanics. In applications such as design optimization or uncertainty quantification, solutions of those PDEs need to be evaluated at numerous points in the parameter space. While physics-informed neural networks (PINNs) have emerged as a new strong competitor as a surrogate, their usage in this scenario remains underexplored due to the inherent need for repetitive and time-consuming training. In this paper, we address this problem by proposing a novel extension, parameterized physics-informed neural networks (P$^2$INNs). P$^2$INNs enable modeling the solutions of parameterized PDEs via explicitly encoding a latent representation of PDE parameters. With the extensive empirical evaluation, we demonstrate that P$^2$INNs outperform the baselines both in accuracy and parameter efficiency on benchmark 1D and 2D parameterized PDEs and are also effective in overcoming the known “failure modes”.