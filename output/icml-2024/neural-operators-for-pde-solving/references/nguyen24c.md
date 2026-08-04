---
title: "PARCv2: Physics-aware Recurrent Convolutional Neural Networks for Spatiotemporal Dynamics Modeling"
source: "https://proceedings.mlr.press/v235/nguyen24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24c/nguyen24c.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['physics-aware-deep-learning', 'recurrent-convolutional', 'spatiotemporal-pde']
venue: "ICML 2024"
tldr: "PARCv2 extends physics-aware recurrent convolutional networks to model fast transient and advection-dominated spatiotemporal PDE dynamics."
---

# PARCv2: Physics-aware Recurrent Convolutional Neural Networks for Spatiotemporal Dynamics Modeling

**Source**: [https://proceedings.mlr.press/v235/nguyen24c.html](https://proceedings.mlr.press/v235/nguyen24c.html)

**TLDR**: PARCv2 extends physics-aware recurrent convolutional networks to model fast transient and advection-dominated spatiotemporal PDE dynamics.

## Abstract

Modeling unsteady, fast transient, and advection-dominated physics problems is a pressing challenge for physics-aware deep learning (PADL). The physics of complex systems is governed by large systems of partial differential equations (PDEs) and ancillary constitutive models with nonlinear structures, as well as evolving state fields exhibiting sharp gradients and rapidly deforming material interfaces. Here, we investigate an inductive bias approach that is versatile and generalizable to model generic nonlinear field evolution problems. Our study focuses on the recent physics-aware recurrent convolutions (PARC), which incorporates a differentiator-integrator architecture that inductively models the spatiotemporal dynamics of generic physical systems. We extend the capabilities of PARC to simulate unsteady, transient, and advection-dominant systems. The extended model, referred to as PARCv2, is equipped with differential operators to model advection-reaction-diffusion equations, as well as a hybrid integral solver for stable, long-time predictions. PARCv2 is tested on both standard benchmark problems in fluid dynamics, namely Burgers and Navier-Stokes equations, and then applied to more complex shock-induced reaction problems in energetic materials. We evaluate the behavior of PARCv2 in comparison to other physics-informed and learning bias models and demonstrate its potential to model unsteady and advection-dominant dynamics regimes.