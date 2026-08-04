---
title: "Neural Diffusion Models"
source: "https://proceedings.mlr.press/v235/bartosh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bartosh24a/bartosh24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-operators-for-pde-solving']
tags: ['diffusion-models', 'generative-models', 'nonlinear-transformations', 'score-matching', 'neural-ODEs']
venue: "ICML 2024"
tldr: "Extends diffusion models beyond linear data transformations to a broader family of nonlinear transformations for improved generative modeling."
---

# Neural Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/bartosh24a.html](https://proceedings.mlr.press/v235/bartosh24a.html)

**TLDR**: Extends diffusion models beyond linear data transformations to a broader family of nonlinear transformations for improved generative modeling.

## Abstract

Diffusion models have shown remarkable performance on many generative tasks. Despite recent success, most diffusion models are restricted in that they only allow linear transformation of the data distribution. In contrast, broader family of transformations can help train generative distributions more efficiently, simplifying the reverse process and closing the gap between the true negative log-likelihood and the variational approximation. In this paper, we present Neural Diffusion Models (NDMs), a generalization of conventional diffusion models that enables defining and learning time-dependent non-linear transformations of data. We show how to optimise NDMs using a variational bound in a simulation-free setting. Moreover, we derive a time-continuous formulation of NDMs, which allows fast and reliable inference using off-the-shelf numerical ODE and SDE solvers. Finally, we demonstrate the utility of NDMs through experiments on many image generation benchmarks, including MNIST, CIFAR-10, downsampled versions of ImageNet and CelebA-HQ. NDMs outperform conventional diffusion models in terms of likelihood, achieving state-of-the-art results on ImageNet and CelebA-HQ, and produces high-quality samples.