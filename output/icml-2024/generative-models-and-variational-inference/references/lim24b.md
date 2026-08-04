---
title: "Momentum Particle Maximum Likelihood"
source: "https://proceedings.mlr.press/v235/lim24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lim24b/lim24b.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['maximum-likelihood-estimation', 'particle-methods', 'optimal-transport']
venue: "ICML 2024"
tldr: "A momentum-based particle method for maximum likelihood estimation in latent variable models using optimal transport insights."
---

# Momentum Particle Maximum Likelihood

**Source**: [https://proceedings.mlr.press/v235/lim24b.html](https://proceedings.mlr.press/v235/lim24b.html)

**TLDR**: A momentum-based particle method for maximum likelihood estimation in latent variable models using optimal transport insights.

## Abstract

Maximum likelihood estimation (MLE) of latent variable models is often recast as the minimization of a free energy functional over an extended space of parameters and probability distributions. This perspective was recently combined with insights from optimal transport to obtain novel particle-based algorithms for fitting latent variable models to data. Drawing inspiration from prior works which interpret ‘momentum-enriched’ optimization algorithms as discretizations of ordinary differential equations, we propose an analogous dynamical-systems-inspired approach to minimizing the free energy functional. The result is a dynamical system that blends elements of Nesterov’s Accelerated Gradient method, the underdamped Langevin diffusion, and particle methods. Under suitable assumptions, we prove that the continuous-time system minimizes the functional. By discretizing the system, we obtain a practical algorithm for MLE in latent variable models. The algorithm outperforms existing particle methods in numerical experiments and compares favourably with other MLE algorithms.