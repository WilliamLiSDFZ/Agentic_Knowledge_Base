---
title: "Bespoke Non-Stationary Solvers for Fast Sampling of Diffusion and Flow Models"
source: "https://proceedings.mlr.press/v235/shaul24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shaul24a/shaul24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['diffusion-models', 'ODE-solvers', 'solver-distillation']
venue: "ICML 2024"
tldr: "Bespoke Non-Stationary Solvers improve sampling efficiency of diffusion and flow models through a solver distillation approach that subsumes existing numerical ODE solvers."
---

# Bespoke Non-Stationary Solvers for Fast Sampling of Diffusion and Flow Models

**Source**: [https://proceedings.mlr.press/v235/shaul24a.html](https://proceedings.mlr.press/v235/shaul24a.html)

**TLDR**: Bespoke Non-Stationary Solvers improve sampling efficiency of diffusion and flow models through a solver distillation approach that subsumes existing numerical ODE solvers.

## Abstract

This paper introduces Bespoke Non-Stationary (BNS) Solvers, a solver distillation approach to improve sample efficiency of Diffusion and Flow models. BNS solvers are based on a family of non-stationary solvers that provably subsumes existing numerical ODE solvers and consequently demonstrate considerable improvement in sample approximation (PSNR) over these baselines. Compared to model distillation, BNS solvers benefit from a tiny parameter space ($<$200 parameters), fast optimization (two orders of magnitude faster), maintain diversity of samples, and in contrast to previous solver distillation approaches nearly close the gap from standard distillation methods such as Progressive Distillation in the low-medium NFE regime. For example, BNS solver achieves 45 PSNR / 1.76 FID using 16 NFE in class-conditional ImageNet-64. We experimented with BNS solvers for conditional image generation, text-to-image generation, and text-2-audio generation showing significant improvement in sample approximation (PSNR) in all.