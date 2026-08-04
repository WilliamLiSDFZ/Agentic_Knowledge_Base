---
title: "Sampling is as easy as keeping the consistency: convergence guarantee for Consistency Models"
source: "https://proceedings.mlr.press/v235/lyu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lyu24b/lyu24b.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['consistency-models', 'diffusion-models', 'convergence-guarantee', 'generative-models']
venue: "ICML 2024"
tldr: "The first convergence guarantee for consistency models is provided, showing they can generate high-quality samples comparable to diffusion models."
---

# Sampling is as easy as keeping the consistency: convergence guarantee for Consistency Models

**Source**: [https://proceedings.mlr.press/v235/lyu24b.html](https://proceedings.mlr.press/v235/lyu24b.html)

**TLDR**: The first convergence guarantee for consistency models is provided, showing they can generate high-quality samples comparable to diffusion models.

## Abstract

We provide the first convergence guarantee for the Consistency Models (CMs), a newly emerging type of one-step generative models that is capable of generating comparable samples to those sampled from state-of-the-art Diffusion Models. Our main result is that, under the basic assumptions on score-matching errors, consistency errors, and smoothness of the data distribution, CMs can efficiently generate samples in one step with small $W_2$ error to any real data distribution. Our results (1) hold for $L^2$-accurate assumptions on both score and consistency functions (rather than $L^\infty$-accurate assumptions); (2) do not require strong assumptions on the data distribution such as log-Sobelev conditions; (3) scale polynomially in all parameters; and (4) match the state-of-the-art convergence guarantee for score-based generative models. We also show that the Multi-step Consistency Sampling procedure can further reduce the error comparing to one step sampling, which supports the original statement from Song Yang’s work. Our result can be generalized to arbitrary bounded data distributions that may be supported on some low-dimensional sub-manifolds. Our results further imply TV error guarantees when making some Langevin-based modifications to the output distributions.