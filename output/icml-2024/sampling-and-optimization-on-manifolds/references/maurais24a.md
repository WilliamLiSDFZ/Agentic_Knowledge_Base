---
title: "Sampling in Unit Time with Kernel Fisher-Rao Flow"
source: "https://proceedings.mlr.press/v235/maurais24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/maurais24a/maurais24a.pdf"
categories: ['sampling-and-optimization-on-manifolds']
tags: ['sampling', 'kernel-Fisher-Rao', 'interacting-particle-systems']
venue: "ICML 2024"
tldr: "A gradient-free mean-field ODE and interacting particle system for efficient sampling from unnormalized target densities."
---

# Sampling in Unit Time with Kernel Fisher-Rao Flow

**Source**: [https://proceedings.mlr.press/v235/maurais24a.html](https://proceedings.mlr.press/v235/maurais24a.html)

**TLDR**: A gradient-free mean-field ODE and interacting particle system for efficient sampling from unnormalized target densities.

## Abstract

We introduce a new mean-field ODE and corresponding interacting particle systems (IPS) for sampling from an unnormalized target density. The IPS are gradient-free, available in closed form, and only require the ability to sample from a reference density and compute the (unnormalized) target-to-reference density ratio. The mean-field ODE is obtained by solving a Poisson equation for a velocity field that transports samples along the geometric mixture of the two densities, $\pi_0^{1-t} \pi_1^t$, which is the path of a particular Fisher-Rao gradient flow. We employ a RKHS ansatz for the velocity field, which makes the Poisson equation tractable and enables discretization of the resulting mean-field ODE over finite samples. The mean-field ODE can be additionally be derived from a discrete-time perspective as the limit of successive linearizations of the Monge-Ampère equations within a framework known as sample-driven optimal transport. We introduce a stochastic variant of our approach and demonstrate empirically that our IPS can produce high-quality samples from varied target distributions, outperforming comparable gradient-free particle systems and competitive with gradient-based alternatives.