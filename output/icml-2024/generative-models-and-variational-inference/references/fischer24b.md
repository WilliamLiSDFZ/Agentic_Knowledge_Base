---
title: "Neuroexplicit Diffusion Models for Inpainting of Optical Flow Fields"
source: "https://proceedings.mlr.press/v235/fischer24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fischer24b/fischer24b.pdf"
categories: ['neural-operators-for-pde-solving', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'optical-flow', 'inpainting']
venue: "ICML 2024"
tldr: "Neuroexplicit diffusion models combine PDE-based priors with neural networks for interpretable and generalizable optical flow inpainting."
---

# Neuroexplicit Diffusion Models for Inpainting of Optical Flow Fields

**Source**: [https://proceedings.mlr.press/v235/fischer24b.html](https://proceedings.mlr.press/v235/fischer24b.html)

**TLDR**: Neuroexplicit diffusion models combine PDE-based priors with neural networks for interpretable and generalizable optical flow inpainting.

## Abstract

Deep learning has revolutionized the field of computer vision by introducing large scale neural networks with millions of parameters. Training these networks requires massive datasets and leads to intransparent models that can fail to generalize. At the other extreme, models designed from partial differential equations (PDEs) embed specialized domain knowledge into mathematical equations and usually rely on few manually chosen hyperparameters. This makes them transparent by construction and if designed and calibrated carefully, they can generalize well to unseen scenarios. In this paper, we show how to bring model- and data-driven approaches together by combining the explicit PDE-based approaches with convolutional neural networks to obtain the best of both worlds. We illustrate a joint architecture for the task of inpainting optical flow fields and show that the combination of model- and data-driven modeling leads to an effective architecture. Our model outperforms both fully explicit and fully data-driven baselines in terms of reconstruction quality, robustness and amount of required training data. Averaging the endpoint error across different mask densities, our method outperforms the explicit baselines by 11-27%, the GAN baseline by 47% and the Probabilisitic Diffusion baseline by 42%. With that, our method sets a new state of the art for inpainting of optical flow fields from random masks.