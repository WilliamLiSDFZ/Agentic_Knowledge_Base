---
title: "Unifying Bayesian Flow Networks and Diffusion Models through Stochastic Differential Equations"
source: "https://proceedings.mlr.press/v235/xue24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xue24d/xue24d.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['Bayesian-flow-networks', 'diffusion-models', 'stochastic-differential-equations']
venue: "ICML 2024"
tldr: "Unifies Bayesian flow networks and diffusion models under a common stochastic differential equation framework for both continuous and discrete data."
---

# Unifying Bayesian Flow Networks and Diffusion Models through Stochastic Differential Equations

**Source**: [https://proceedings.mlr.press/v235/xue24d.html](https://proceedings.mlr.press/v235/xue24d.html)

**TLDR**: Unifies Bayesian flow networks and diffusion models under a common stochastic differential equation framework for both continuous and discrete data.

## Abstract

Bayesian flow networks (BFNs) iteratively refine the parameters, instead of the samples in diffusion models (DMs), of distributions at various noise levels through Bayesian inference. Owing to its differentiable nature, BFNs are promising in modeling both continuous and discrete data, while simultaneously maintaining fast sampling capabilities. This paper aims to understand and enhance BFNs by connecting them with DMs through stochastic differential equations (SDEs). We identify the linear SDEs corresponding to the noise-addition processes in BFNs, demonstrate that BFN’s regression losses are aligned with denoise score matching, and validate the sampler in BFN as a first-order solver for the respective reverse-time SDE. Based on these findings and existing recipes of fast sampling in DMs, we propose specialized solvers for BFNs that markedly surpass the original BFN sampler in terms of sample quality with a limited number of function evaluations (e.g., 10) on both image and text datasets. Notably, our best sampler achieves an increase in speed of $5\sim20$ times for free.