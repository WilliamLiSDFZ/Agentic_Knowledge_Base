---
title: "Neural Jump-Diffusion Temporal Point Processes"
source: "https://proceedings.mlr.press/v235/zhang24cm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cm/zhang24cm.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'time-series-modeling-and-forecasting-methods']
tags: ['temporal-point-processes', 'stochastic-differential-equations', 'jump-diffusion']
venue: "ICML 2024"
tldr: "Reformulates temporal point processes as solutions to SDEs, introducing neural jump-diffusion TPPs."
---

# Neural Jump-Diffusion Temporal Point Processes

**Source**: [https://proceedings.mlr.press/v235/zhang24cm.html](https://proceedings.mlr.press/v235/zhang24cm.html)

**TLDR**: Reformulates temporal point processes as solutions to SDEs, introducing neural jump-diffusion TPPs.

## Abstract

We present a novel perspective on temporal point processes (TPPs) by reformulating their intensity processes as solutions to stochastic differential equations (SDEs). In particular, we first prove the equivalent SDE formulations of several classical TPPs, including Poisson processes, Hawkes processes, and self-correcting processes. Based on these proofs, we introduce a unified TPP framework called Neural Jump-Diffusion Temporal Point Process (NJDTPP), whose intensity process is governed by a neural jump-diffusion SDE (NJDSDE) where the drift, diffusion, and jump coefficient functions are parameterized by neural networks. Compared to previous works, NJDTPP exhibits model flexibility in capturing intensity dynamics without relying on any specific functional form, and provides theoretical guarantees regarding the existence and uniqueness of the solution to the proposed NJDSDE. Experiments on both synthetic and real-world datasets demonstrate that NJDTPP is capable of capturing the dynamics of intensity processes in different scenarios and significantly outperforms the state-of-the-art TPP models in prediction tasks.