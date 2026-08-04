---
title: "Light and Optimal Schrödinger Bridge Matching"
source: "https://proceedings.mlr.press/v235/gushchin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gushchin24a/gushchin24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['Schrödinger-bridge', 'optimal-transport', 'diffusion-models', 'bridge-matching', 'generative-models']
venue: "ICML 2024"
tldr: "A lightweight and optimal Schrödinger bridge matching solver connecting entropic optimal transport and diffusion models."
---

# Light and Optimal Schrödinger Bridge Matching

**Source**: [https://proceedings.mlr.press/v235/gushchin24a.html](https://proceedings.mlr.press/v235/gushchin24a.html)

**TLDR**: A lightweight and optimal Schrödinger bridge matching solver connecting entropic optimal transport and diffusion models.

## Abstract

Schrödinger Bridges (SB) have recently gained the attention of the ML community as a promising extension of classic diffusion models which is also interconnected to the Entropic Optimal Transport (EOT). Recent solvers for SB exploit the pervasive bridge matching procedures. Such procedures aim to recover a stochastic process transporting the mass between distributions given only a transport plan between them. In particular, given the EOT plan, these procedures can be adapted to solve SB. This fact is heavily exploited by recent works giving rives to matching-based SB solvers. The cornerstone here is recovering the EOT plan: recent works either use heuristical approximations (e.g., the minibatch OT) or establish iterative matching procedures which by the design accumulate the error during the training. We address these limitations and propose a novel procedure to learn SB which we call the optimal Schrödinger bridge matching. It exploits the optimal parameterization of the diffusion process and provably recovers the SB process (a) with a single bridge matching step and (b) with arbitrary transport plan as the input. Furthermore, we show that the optimal bridge matching objective coincides with the recently discovered energy-based modeling (EBM) objectives to learn EOT/SB. Inspired by this observation, we develop a light solver (which we call LightSB-M) to implement optimal matching in practice using the Gaussian mixture parameterization of the adjusted Schrödinger potential. We experimentally showcase the performance of our solver in a range of practical tasks.