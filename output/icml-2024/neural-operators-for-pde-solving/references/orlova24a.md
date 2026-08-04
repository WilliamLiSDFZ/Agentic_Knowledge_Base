---
title: "Deep Stochastic Mechanics"
source: "https://proceedings.mlr.press/v235/orlova24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/orlova24a/orlova24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['stochastic-mechanics', 'Schrödinger-equation', 'deep-learning', 'quantum-simulation']
venue: "ICML 2024"
tldr: "Introduces a deep learning approach for numerically simulating time-evolving Schrödinger equations inspired by stochastic mechanics."
---

# Deep Stochastic Mechanics

**Source**: [https://proceedings.mlr.press/v235/orlova24a.html](https://proceedings.mlr.press/v235/orlova24a.html)

**TLDR**: Introduces a deep learning approach for numerically simulating time-evolving Schrödinger equations inspired by stochastic mechanics.

## Abstract

This paper introduces a novel deep-learning-based approach for numerical simulation of a time-evolving Schrödinger equation inspired by stochastic mechanics and generative diffusion models. Unlike existing approaches, which exhibit computational complexity that scales exponentially in the problem dimension, our method allows us to adapt to the latent low-dimensional structure of the wave function by sampling from the Markovian diffusion. Depending on the latent dimension, our method may have far lower computational complexity in higher dimensions. Moreover, we propose novel equations for stochastic quantum mechanics, resulting in quadratic computational complexity with respect to the number of dimensions. Numerical simulations verify our theoretical findings and show a significant advantage of our method compared to other deep-learning-based approaches used for quantum mechanics.