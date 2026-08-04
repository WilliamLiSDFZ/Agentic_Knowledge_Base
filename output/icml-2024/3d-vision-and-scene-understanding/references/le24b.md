---
title: "Robust Inverse Graphics via Probabilistic Inference"
source: "https://proceedings.mlr.press/v235/le24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/le24b/le24b.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', '3d-vision-and-scene-understanding']
tags: ['3D-scene-inference', 'probabilistic-inference', 'domain-corruption', 'robust-inverse-graphics']
venue: "ICML 2024"
tldr: "A Bayesian framework for robust 3D scene inference from single corrupted images using strong scene priors without needing corruption-specific training."
---

# Robust Inverse Graphics via Probabilistic Inference

**Source**: [https://proceedings.mlr.press/v235/le24b.html](https://proceedings.mlr.press/v235/le24b.html)

**TLDR**: A Bayesian framework for robust 3D scene inference from single corrupted images using strong scene priors without needing corruption-specific training.

## Abstract

How do we infer a 3D scene from a single image in the presence of corruptions like rain, snow or fog? Straightforward domain randomization relies on knowing the family of corruptions ahead of time. Here, we propose a Bayesian approach—dubbed robust inverse graphics (RIG)—that relies on a strong scene prior and an uninformative uniform corruption prior, making it applicable to a wide range of corruptions. Given a single image, RIG performs posterior inference jointly over the scene and the corruption. We demonstrate this idea by training a neural radiance field (NeRF) scene prior and using a secondary NeRF to represent the corruptions over which we place an uninformative prior. RIG, trained only on clean data, outperforms depth estimators and alternative NeRF approaches that perform point estimation instead of full inference. The results hold for a number of scene prior architectures based on normalizing flows and diffusion models. For the latter, we develop reconstruction-guidance with auxiliary latents (ReGAL)—a diffusion conditioning algorithm that is applicable in the presence of auxiliary latent variables such as the corruption. RIG demonstrates how scene priors can be used beyond generation tasks.