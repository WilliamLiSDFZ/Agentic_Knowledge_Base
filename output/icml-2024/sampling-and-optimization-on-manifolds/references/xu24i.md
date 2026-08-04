---
title: "Practical Hamiltonian Monte Carlo on Riemannian Manifolds via Relativity Theory"
source: "https://proceedings.mlr.press/v235/xu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24i/xu24i.pdf"
categories: ['sampling-and-optimization-on-manifolds']
tags: ['Hamiltonian-Monte-Carlo', 'Riemannian-manifolds', 'relativity-theory']
venue: "ICML 2024"
tldr: "This paper proposes a practical Riemannian HMC method inspired by special relativity to address integration instability on curved manifolds."
---

# Practical Hamiltonian Monte Carlo on Riemannian Manifolds via Relativity Theory

**Source**: [https://proceedings.mlr.press/v235/xu24i.html](https://proceedings.mlr.press/v235/xu24i.html)

**TLDR**: This paper proposes a practical Riemannian HMC method inspired by special relativity to address integration instability on curved manifolds.

## Abstract

Hamiltonian Monte Carlo (HMC) samples from an unnormalized density by numerically integrating Hamiltonian dynamics. Girolami & Calderhead (2011) extend HMC to Riemannian manifolds, but the resulting method faces integration instability issues for practical usage. While previous works have tackled this challenge by using more robust metric tensors than Fisher’s information metric, our work focuses on designing numerically stable Hamiltonian dynamics. To do so, we start with the idea from Lu et al. (2017), which designs momentum distributions to upper-bound the particle speed. Then, we generalize this Lu et al. (2017) method to Riemannian manifolds. In our generalization, the upper bounds of velocity norm become position-dependent, which intrinsically limits step sizes used in high curvature regions and, therefore, significantly reduces numerical errors. We also derive a more tractable algorithm to sample from relativistic momentum distributions without relying on the mean-field assumption.