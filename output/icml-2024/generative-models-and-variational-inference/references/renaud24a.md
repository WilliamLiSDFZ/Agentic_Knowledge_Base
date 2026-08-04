---
title: "Plug-and-Play image restoration with Stochastic deNOising REgularization"
source: "https://proceedings.mlr.press/v235/renaud24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/renaud24a/renaud24a.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['plug-and-play', 'image-restoration', 'stochastic-denoising', 'regularization', 'inverse-problems']
venue: "ICML 2024"
tldr: "A stochastic denoising regularization framework is proposed for Plug-and-Play image restoration that provides a principled probabilistic interpretation of denoiser-based algorithms."
---

# Plug-and-Play image restoration with Stochastic deNOising REgularization

**Source**: [https://proceedings.mlr.press/v235/renaud24a.html](https://proceedings.mlr.press/v235/renaud24a.html)

**TLDR**: A stochastic denoising regularization framework is proposed for Plug-and-Play image restoration that provides a principled probabilistic interpretation of denoiser-based algorithms.

## Abstract

Plug-and-Play (PnP) algorithms are a class of iterative algorithms that address image inverse problems by combining a physical model and a deep neural network for regularization. Even if they produce impressive image restoration results, these algorithms rely on a non-standard use of a denoiser on images that are less and less noisy along the iterations, which contrasts with recent algorithms based on Diffusion Models (DM), where the denoiser is applied only on re-noised images. We propose a new PnP framework, called Stochastic deNOising REgularization (SNORE), which applies the denoiser only on images with noise of the adequate level. It is based on an explicit stochastic regularization, which leads to a stochastic gradient descent algorithm to solve ill-posed inverse problems. A convergence analysis of this algorithm and its annealing extension is provided. Experimentally, we prove that SNORE is competitive with respect to state-of-the-art methods on deblurring and inpainting tasks, both quantitatively and qualitatively.