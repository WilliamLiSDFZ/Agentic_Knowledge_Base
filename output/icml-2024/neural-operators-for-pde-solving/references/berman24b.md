---
title: "CoLoRA: Continuous low-rank adaptation for reduced implicit neural modeling of parameterized partial differential equations"
source: "https://proceedings.mlr.press/v235/berman24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/berman24b/berman24b.pdf"
categories: ['neural-operators-for-pde-solving', 'continual-learning-memory-plasticity']
tags: ['neural-operators', 'PDEs', 'low-rank-adaptation', 'reduced-order-models', 'continual-learning']
venue: "ICML 2024"
tldr: "Introduces CoLoRA, a continuous low-rank adaptation framework for rapidly predicting PDE solution fields at new parameters using pre-trained neural networks."
---

# CoLoRA: Continuous low-rank adaptation for reduced implicit neural modeling of parameterized partial differential equations

**Source**: [https://proceedings.mlr.press/v235/berman24b.html](https://proceedings.mlr.press/v235/berman24b.html)

**TLDR**: Introduces CoLoRA, a continuous low-rank adaptation framework for rapidly predicting PDE solution fields at new parameters using pre-trained neural networks.

## Abstract

This work introduces reduced models based on Continuous Low Rank Adaptation (CoLoRA) that pre-train neural networks for a given partial differential equation and then continuously adapt low-rank weights in time to rapidly predict the evolution of solution fields at new physics parameters and new initial conditions. The adaptation can be either purely data-driven or via an equation-driven variational approach that provides Galerkin-optimal approximations. Because CoLoRA approximates solution fields locally in time, the rank of the weights can be kept small, which means that only few training trajectories are required offline so that CoLoRA is well suited for data-scarce regimes. Predictions with CoLoRA are orders of magnitude faster than with classical methods and their accuracy and parameter efficiency is higher compared to other neural network approaches.