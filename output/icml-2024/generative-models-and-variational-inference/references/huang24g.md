---
title: "Symbolic Music Generation with Non-Differentiable Rule Guided Diffusion"
source: "https://proceedings.mlr.press/v235/huang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24g/huang24g.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['music-generation', 'diffusion-models', 'non-differentiable-guidance']
venue: "ICML 2024"
tldr: "Proposes a method for symbolic music generation using diffusion models guided by non-differentiable musical rules."
---

# Symbolic Music Generation with Non-Differentiable Rule Guided Diffusion

**Source**: [https://proceedings.mlr.press/v235/huang24g.html](https://proceedings.mlr.press/v235/huang24g.html)

**TLDR**: Proposes a method for symbolic music generation using diffusion models guided by non-differentiable musical rules.

## Abstract

We study the problem of symbolic music generation (e.g., generating piano rolls), with a technical focus on non-differentiable rule guidance. Musical rules are often expressed in symbolic form on note characteristics, such as note density or chord progression, many of which are non-differentiable which pose a challenge when using them for guided diffusion. We propose Stochastic Control Guidance (SCG), a novel guidance method that only requires forward evaluation of rule functions that can work with pre-trained diffusion models in a plug-and-play way, thus achieving training-free guidance for non-differentiable rules for the first time. Additionally, we introduce a latent diffusion architecture for symbolic music generation with high time resolution, which can be composed with SCG in a plug-and-play fashion. Compared to standard strong baselines in symbolic music generation, this framework demonstrates marked advancements in music quality and rule-based controllability, outperforming current state-of-the-art generators in a variety of settings. For detailed demonstrations, code and model checkpoints, please visit our project website.