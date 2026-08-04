---
title: "Diffusion Posterior Sampling is Computationally Intractable"
source: "https://proceedings.mlr.press/v235/gupta24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gupta24a/gupta24a.pdf"
categories: ['generative-models-and-variational-inference', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['diffusion-models', 'posterior-sampling', 'computational-intractability', 'generative-models', 'hardness']
venue: "ICML 2024"
tldr: "Proves that posterior sampling with diffusion models is computationally intractable in general."
---

# Diffusion Posterior Sampling is Computationally Intractable

**Source**: [https://proceedings.mlr.press/v235/gupta24a.html](https://proceedings.mlr.press/v235/gupta24a.html)

**TLDR**: Proves that posterior sampling with diffusion models is computationally intractable in general.

## Abstract

Diffusion models are a remarkably effective way of learning and sampling from a distribution $p(x)$. In posterior sampling, one is also given a measurement model $p(y \mid x)$ and a measurement $y$, and would like to sample from $p(x \mid y)$. Posterior sampling is useful for tasks such as inpainting, super-resolution, and MRI reconstruction, so a number of recent works have given algorithms to heuristically approximate it; but none are known to converge to the correct distribution in polynomial time. In this paper we show that posterior sampling is computationally intractable: under the most basic assumption in cryptography—that one-way functions exist—there are instances for which every algorithm takes superpolynomial time, even though unconditional sampling is provably fast. We also show that the exponential-time rejection sampling algorithm is essentially optimal under the stronger plausible assumption that there are one-way functions that take exponential time to invert.