---
title: "Align Your Steps: Optimizing Sampling Schedules in Diffusion Models"
source: "https://proceedings.mlr.press/v235/sabour24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sabour24a/sabour24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['diffusion-models', 'sampling-schedules', 'optimization', 'score-based-models', 'inference-speed']
venue: "ICML 2024"
tldr: "A method is proposed to optimize sampling schedules in diffusion models using stochastic optimization, improving sample quality at reduced function evaluations."
---

# Align Your Steps: Optimizing Sampling Schedules in Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/sabour24a.html](https://proceedings.mlr.press/v235/sabour24a.html)

**TLDR**: A method is proposed to optimize sampling schedules in diffusion models using stochastic optimization, improving sample quality at reduced function evaluations.

## Abstract

Diffusion models (DMs) have established themselves as the state-of-the-art generative modeling approach in the visual domain and beyond. A crucial drawback of DMs is their slow sampling speed, relying on many sequential function evaluations through large neural networks. Sampling from DMs can be seen as solving a differential equation through a discretized set of noise levels known as the sampling schedule. While past works primarily focused on deriving efficient solvers, little attention has been given to finding optimal sampling schedules, and the entire literature relies on hand-crafted heuristics. In this work, for the first time, we propose a general and principled approach to optimizing the sampling schedules of DMs for high-quality outputs, called Align Your Steps. We leverage methods from stochastic calculus and find optimal schedules specific to different solvers, trained DMs and datasets. We evaluate our novel approach on several image, video as well as 2D toy data synthesis benchmarks, using a variety of different samplers, and observe that our optimized schedules outperform previous hand-crafted schedules in almost all experiments. Our method demonstrates the untapped potential of sampling schedule optimization, especially in the few-step synthesis regime.