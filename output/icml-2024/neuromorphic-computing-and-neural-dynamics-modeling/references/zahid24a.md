---
title: "Sample as you Infer: Predictive Coding with Langevin Dynamics"
source: "https://proceedings.mlr.press/v235/zahid24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zahid24a/zahid24a.pdf"
categories: ['generative-models-and-variational-inference', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['predictive-coding', 'Langevin-dynamics', 'generative-model', 'computational-neuroscience']
venue: "ICML 2024"
tldr: "Langevin Predictive Coding injects noise into predictive coding inference to enable principled sampling for deep generative model learning."
---

# Sample as you Infer: Predictive Coding with Langevin Dynamics

**Source**: [https://proceedings.mlr.press/v235/zahid24a.html](https://proceedings.mlr.press/v235/zahid24a.html)

**TLDR**: Langevin Predictive Coding injects noise into predictive coding inference to enable principled sampling for deep generative model learning.

## Abstract

We present Langevin Predictive Coding (LPC), a novel algorithm for deep generative model learning that builds upon the predictive coding framework of computational neuroscience. By injecting Gaussian noise into the predictive coding inference procedure and incorporating an encoder network initialization, we reframe the approach as an amortized Langevin sampling method for optimizing a tight variational lower bound. To increase robustness to sampling step size, we present a lightweight preconditioning technique inspired by Riemannian Langevin methods and adaptive SGD. We compare LPC against VAEs by training generative models on benchmark datasets; our experiments demonstrate superior sample quality and faster convergence for LPC in a fraction of SGD training iterations, while matching or exceeding VAE performance across key metrics like FID, diversity and coverage.