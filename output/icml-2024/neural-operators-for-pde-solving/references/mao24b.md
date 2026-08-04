---
title: "Towards General Neural Surrogate Solvers with Specialized Neural Accelerators"
source: "https://proceedings.mlr.press/v235/mao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mao24b/mao24b.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['neural-surrogate', 'PDE-solver', 'domain-generalization']
venue: "ICML 2024"
tldr: "A specialized neural accelerator framework for solving PDEs across varying domains, geometries, and boundary conditions."
---

# Towards General Neural Surrogate Solvers with Specialized Neural Accelerators

**Source**: [https://proceedings.mlr.press/v235/mao24b.html](https://proceedings.mlr.press/v235/mao24b.html)

**TLDR**: A specialized neural accelerator framework for solving PDEs across varying domains, geometries, and boundary conditions.

## Abstract

Surrogate neural network-based partial differential equation (PDE) solvers have the potential to solve PDEs in an accelerated manner, but they are largely limited to systems featuring fixed domain sizes, geometric layouts, and boundary conditions. We propose Specialized Neural Accelerator-Powered Domain Decomposition Methods (SNAP-DDM), a DDM-based approach to PDE solving in which subdomain problems containing arbitrary boundary conditions and geometric parameters are accurately solved using an ensemble of specialized neural operators. We tailor SNAP-DDM to 2D electromagnetics and fluidic flow problems and show how innovations in network architecture and loss function engineering can produce specialized surrogate subdomain solvers with near unity accuracy. We utilize these solvers with standard DDM algorithms to accurately solve freeform electromagnetics and fluids problems featuring a wide range of domain sizes.