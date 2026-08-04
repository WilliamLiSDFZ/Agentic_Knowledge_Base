---
title: "Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics"
source: "https://proceedings.mlr.press/v235/toshev24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/toshev24a/toshev24a.pdf"
categories: ['neural-operators-for-pde-solving', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['smoothed-particle-hydrodynamics', 'neural-simulation', 'Lagrangian-fluid']
venue: "ICML 2024"
tldr: "Neural SPH improves neural network-based modeling of Lagrangian fluid dynamics by incorporating SPH inductive biases to correct simulation errors efficiently."
---

# Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics

**Source**: [https://proceedings.mlr.press/v235/toshev24a.html](https://proceedings.mlr.press/v235/toshev24a.html)

**TLDR**: Neural SPH improves neural network-based modeling of Lagrangian fluid dynamics by incorporating SPH inductive biases to correct simulation errors efficiently.

## Abstract

Smoothed particle hydrodynamics (SPH) is omnipresent in modern engineering and scientific disciplines. SPH is a class of Lagrangian schemes that discretize fluid dynamics via finite material points that are tracked through the evolving velocity field. Due to the particle-like nature of the simulation, graph neural networks (GNNs) have emerged as appealing and successful surrogates. However, the practical utility of such GNN-based simulators relies on their ability to faithfully model physics, providing accurate and stable predictions over long time horizons - which is a notoriously hard problem. In this work, we identify particle clustering originating from tensile instabilities as one of the primary pitfalls. Based on these insights, we enhance both training and rollout inference of state-of-the-art GNN-based simulators with varying components from standard SPH solvers, including pressure, viscous, and external force components. All Neural SPH-enhanced simulators achieve better performance than the baseline GNNs, often by orders of magnitude in terms of rollout error, allowing for significantly longer rollouts and significantly better physics modeling. Code available under https://github.com/tumaer/neuralsph.