---
title: "Understanding Diffusion Models by Feynman’s Path Integral"
source: "https://proceedings.mlr.press/v235/hirono24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hirono24a/hirono24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['diffusion-models', 'path-integral', 'stochastic-sampling', 'score-based']
venue: "ICML 2024"
tldr: "Applies Feynman's path integral framework to theoretically explain performance differences between stochastic and deterministic diffusion model samplers."
---

# Understanding Diffusion Models by Feynman’s Path Integral

**Source**: [https://proceedings.mlr.press/v235/hirono24a.html](https://proceedings.mlr.press/v235/hirono24a.html)

**TLDR**: Applies Feynman's path integral framework to theoretically explain performance differences between stochastic and deterministic diffusion model samplers.

## Abstract

Score-based diffusion models have proven effective in image generation and have gained widespread usage; however, the underlying factors contributing to the performance disparity between stochastic and deterministic (i.e., the probability flow ODEs) sampling schemes remain unclear. We introduce a novel formulation of diffusion models using Feynman’s path integral, which is a formulation originally developed for quantum physics. We find this formulation providing comprehensive descriptions of score-based generative models, and demonstrate the derivation of backward stochastic differential equations and loss functions. The formulation accommodates an interpolating parameter connecting stochastic and deterministic sampling schemes, and we identify this parameter as a counterpart of Planck’s constant in quantum physics. This analogy enables us to apply the Wentzel–Kramers–Brillouin (WKB) expansion, a well-established technique in quantum physics, for evaluating the negative log-likelihood to assess the performance disparity between stochastic and deterministic sampling schemes.