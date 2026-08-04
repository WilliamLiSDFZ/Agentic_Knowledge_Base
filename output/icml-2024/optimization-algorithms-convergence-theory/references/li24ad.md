---
title: "Accelerating Convergence of Score-Based Diffusion Models, Provably"
source: "https://proceedings.mlr.press/v235/li24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ad/li24ad.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['diffusion-models', 'score-based', 'convergence', 'sampling-speed', 'theory']
venue: "ICML 2024"
tldr: "Theoretical analysis and methods are proposed to provably accelerate the convergence and sampling speed of score-based diffusion models."
---

# Accelerating Convergence of Score-Based Diffusion Models, Provably

**Source**: [https://proceedings.mlr.press/v235/li24ad.html](https://proceedings.mlr.press/v235/li24ad.html)

**TLDR**: Theoretical analysis and methods are proposed to provably accelerate the convergence and sampling speed of score-based diffusion models.

## Abstract

Score-based diffusion models, while achieving remarkable empirical performance, often suffer from low sampling speed, due to extensive function evaluations needed during the sampling phase. Despite a flurry of recent activities towards speeding up diffusion generative modeling in practice, theoretical underpinnings for acceleration techniques remain severely limited. In this paper, we design novel training-free algorithms to accelerate popular deterministic (i.e., DDIM) and stochastic (i.e., DDPM) samplers. Our accelerated deterministic sampler converges at a rate $O(\frac{1}{{T}^2})$ with $T$ the number of steps, improving upon the $O(\frac{1}{T})$ rate for the DDIM sampler; and our accelerated stochastic sampler converges at a rate $O(\frac{1}{T})$, outperforming the rate $O(\frac{1}{\sqrt{T}})$ for the DDPM sampler. The design of our algorithms leverages insights from higher-order approximation, and shares similar intuitions as popular high-order ODE solvers like the DPM-Solver-2. Our theory accommodates $\ell_2$-accurate score estimates, and does not require log-concavity or smoothness on the target distribution.