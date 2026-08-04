---
title: "Listening to the noise: Blind Denoising with Gibbs Diffusion"
source: "https://proceedings.mlr.press/v235/heurtel-depeiges24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/heurtel-depeiges24a/heurtel-depeiges24a.pdf"
categories: ['generative-models-and-variational-inference', 'audio-and-music-generation-diffusion-models']
tags: ['blind-denoising', 'diffusion-models', 'Gibbs-sampling', 'Bayesian']
venue: "ICML 2024"
tldr: "Proposes Gibbs Diffusion for blind denoising that simultaneously estimates noise parameters and denoises using diffusion-based priors."
---

# Listening to the noise: Blind Denoising with Gibbs Diffusion

**Source**: [https://proceedings.mlr.press/v235/heurtel-depeiges24a.html](https://proceedings.mlr.press/v235/heurtel-depeiges24a.html)

**TLDR**: Proposes Gibbs Diffusion for blind denoising that simultaneously estimates noise parameters and denoises using diffusion-based priors.

## Abstract

In recent years, denoising problems have become intertwined with the development of deep generative models. In particular, diffusion models are trained like denoisers, and the distribution they model coincide with denoising priors in the Bayesian picture. However, denoising through diffusion-based posterior sampling requires the noise level and covariance to be known, preventing blind denoising. We overcome this limitation by introducing Gibbs Diffusion (GDiff), a general methodology addressing posterior sampling of both the signal and the noise parameters. Assuming arbitrary parametric Gaussian noise, we develop a Gibbs algorithm that alternates sampling steps from a conditional diffusion model trained to map the signal prior to the class of noise distributions, and a Monte Carlo sampler to infer the noise parameters. Our theoretical analysis highlights potential pitfalls, guides diagnostic usage, and quantifies errors in the Gibbs stationary distribution caused by the diffusion model. We showcase our method for 1) blind denoising of natural images involving colored noises with unknown amplitude and exponent, and 2) a cosmology problem, namely the analysis of cosmic microwave background data, where Bayesian inference of "noise" parameters means constraining models of the evolution of the Universe.