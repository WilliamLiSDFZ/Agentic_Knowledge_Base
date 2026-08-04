---
title: "Liouville Flow Importance Sampler"
source: "https://proceedings.mlr.press/v235/tian24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tian24c/tian24c.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['importance-sampling', 'flow-based-models', 'unnormalized-densities']
venue: "ICML 2024"
tldr: "The Liouville Flow Importance Sampler uses a learned time-dependent velocity field to transport samples from simple to complex distributions for efficient unnormalized density sampling."
---

# Liouville Flow Importance Sampler

**Source**: [https://proceedings.mlr.press/v235/tian24c.html](https://proceedings.mlr.press/v235/tian24c.html)

**TLDR**: The Liouville Flow Importance Sampler uses a learned time-dependent velocity field to transport samples from simple to complex distributions for efficient unnormalized density sampling.

## Abstract

We present the Liouville Flow Importance Sampler (LFIS), an innovative flow-based model for generating samples from unnormalized density functions. LFIS learns a time-dependent velocity field that deterministically transports samples from a simple initial distribution to a complex target distribution, guided by a prescribed path of annealed distributions. The training of LFIS utilizes a unique method that enforces the structure of a derived partial differential equation to neural networks modeling velocity fields. By considering the neural velocity field as an importance sampler, sample weights can be computed through accumulating errors along the sample trajectories driven by neural velocity fields, ensuring unbiased and consistent estimation of statistical quantities. We demonstrate the effectiveness of LFIS through its application to a range of benchmark problems, on many of which LFIS achieved state-of-the-art performance.