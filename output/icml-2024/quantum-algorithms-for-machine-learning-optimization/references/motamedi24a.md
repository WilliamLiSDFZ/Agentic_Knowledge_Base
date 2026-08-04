---
title: "Gibbs Sampling of Continuous Potentials on a Quantum Computer"
source: "https://proceedings.mlr.press/v235/motamedi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/motamedi24a/motamedi24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'sampling-and-optimization-on-manifolds']
tags: ['quantum-computing', 'Gibbs-sampling', 'quantum-Fourier-transform', 'continuous-potentials']
venue: "ICML 2024"
tldr: "A quantum algorithm leveraging quantum Fourier transforms and ODE solvers is proposed for Gibbs sampling from periodic continuous real-valued functions."
---

# Gibbs Sampling of Continuous Potentials on a Quantum Computer

**Source**: [https://proceedings.mlr.press/v235/motamedi24a.html](https://proceedings.mlr.press/v235/motamedi24a.html)

**TLDR**: A quantum algorithm leveraging quantum Fourier transforms and ODE solvers is proposed for Gibbs sampling from periodic continuous real-valued functions.

## Abstract

Gibbs sampling from continuous real-valued functions is a challenging problem of interest in machine learning. Here we leverage quantum Fourier transforms to build a quantum algorithm for this task when the function is periodic. We use the quantum algorithms for solving linear ordinary differential equations to solve the Fokker–Planck equation and prepare a quantum state encoding the Gibbs distribution. We show that the efficiency of interpolation and differentiation of these functions on a quantum computer depends on the rate of decay of the Fourier coefficients of the Fourier transform of the function. We view this property as a concentration of measure in the Fourier domain, and also provide functional analytic conditions for it. Our algorithm makes zeroeth order queries to a quantum oracle of the function and achieves polynomial quantum speedups in mean estimation in the Gibbs measure for generic non-convex periodic functions. At high temperatures the algorithm also allows for exponentially improved precision in sampling from Morse functions.