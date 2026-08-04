---
title: "CaRiNG: Learning Temporal Causal Representation under Non-Invertible Generation Process"
source: "https://proceedings.mlr.press/v235/chen24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ai/chen24ai.pdf"
categories: ['causal-inference-and-discovery-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['temporal-causal-representation', 'non-invertible-generation', 'latent-variables', 'identifiability']
venue: "ICML 2024"
tldr: "Proposes CaRiNG to identify temporal latent causal variables in sequential data under non-invertible generation processes."
---

# CaRiNG: Learning Temporal Causal Representation under Non-Invertible Generation Process

**Source**: [https://proceedings.mlr.press/v235/chen24ai.html](https://proceedings.mlr.press/v235/chen24ai.html)

**TLDR**: Proposes CaRiNG to identify temporal latent causal variables in sequential data under non-invertible generation processes.

## Abstract

Identifying the underlying time-delayed latent causal processes in sequential data is vital for grasping temporal dynamics and making downstream reasoning. While some recent methods can robustly identify these latent causal variables, they rely on strict assumptions about the invertible generation process from latent variables to observed data. However, these assumptions are often hard to satisfy in real-world applications containing information loss. For instance, the visual perception process translates a 3D space into 2D images, or the phenomenon of persistence of vision incorporates historical data into current perceptions. To address this challenge, we establish an identifiability theory that allows for the recovery of independent latent components even when they come from a nonlinear and non-invertible mix. Using this theory as a foundation, we propose a principled approach, CaRiNG, to learn the Causal Representation of Non-invertible Generative temporal data with identifiability guarantees. Specifically, we utilize temporal context to recover lost latent information and apply the conditions in our theory to guide the training process. Through experiments conducted on synthetic datasets, we validate that our CaRiNG method reliably identifies the causal process, even when the generation process is non-invertible. Moreover, we demonstrate that our approach considerably improves temporal understanding and reasoning in practical applications.