---
title: "On the Trajectory Regularity of ODE-based Diffusion Sampling"
source: "https://proceedings.mlr.press/v235/chen24bm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bm/chen24bm.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['ODE-based-diffusion', 'sampling-trajectories', 'generative-models']
venue: "ICML 2024"
tldr: "Intriguing trajectory regularity properties of ODE-based diffusion sampling are identified and exploited to improve generation efficiency."
---

# On the Trajectory Regularity of ODE-based Diffusion Sampling

**Source**: [https://proceedings.mlr.press/v235/chen24bm.html](https://proceedings.mlr.press/v235/chen24bm.html)

**TLDR**: Intriguing trajectory regularity properties of ODE-based diffusion sampling are identified and exploited to improve generation efficiency.

## Abstract

Diffusion-based generative models use stochastic differential equations (SDEs) and their equivalent ordinary differential equations (ODEs) to establish a smooth connection between a complex data distribution and a tractable prior distribution. In this paper, we identify several intriguing trajectory properties in the ODE-based sampling process of diffusion models. We characterize an implicit denoising trajectory and discuss its vital role in forming the coupled sampling trajectory with a strong shape regularity, regardless of the generated content. We also describe a dynamic programming-based scheme to make the time schedule in sampling better fit the underlying trajectory structure. This simple strategy requires minimal modification to any given ODE-based numerical solvers and incurs negligible computational cost, while delivering superior performance in image generation, especially in $5\sim 10$ function evaluations.