---
title: "Improving Gradient-Guided Nested Sampling for Posterior Inference"
source: "https://proceedings.mlr.press/v235/lemos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lemos24a/lemos24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['nested-sampling', 'posterior-inference', 'Hamiltonian-slice-sampling', 'differentiable-programming', 'Bayesian-inference']
venue: "ICML 2024"
tldr: "Presents an improved gradient-guided nested sampling algorithm combining Hamiltonian slice sampling, dynamic nested sampling, and parallelization for scalable posterior inference."
---

# Improving Gradient-Guided Nested Sampling for Posterior Inference

**Source**: [https://proceedings.mlr.press/v235/lemos24a.html](https://proceedings.mlr.press/v235/lemos24a.html)

**TLDR**: Presents an improved gradient-guided nested sampling algorithm combining Hamiltonian slice sampling, dynamic nested sampling, and parallelization for scalable posterior inference.

## Abstract

We present a performant, general-purpose gradient-guided nested sampling (GGNS) algorithm, combining the state of the art in differentiable programming, Hamiltonian slice sampling, clustering, mode separation, dynamic nested sampling, and parallelization. This unique combination allows GGNS to scale well with dimensionality and perform competitively on a variety of synthetic and real-world problems. We also show the potential of combining nested sampling with generative flow networks to obtain large amounts of high-quality samples from the posterior distribution. This combination leads to faster mode discovery and more accurate estimates of the partition function.