---
title: "What’s the score? Automated Denoising Score Matching for Nonlinear Diffusions"
source: "https://proceedings.mlr.press/v235/singhal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singhal24a/singhal24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['score-matching', 'diffusion-models', 'nonlinear-diffusions']
venue: "ICML 2024"
tldr: "Develops automated denoising score matching for nonlinear diffusion processes beyond the standard linear Gaussian setting."
---

# What’s the score? Automated Denoising Score Matching for Nonlinear Diffusions

**Source**: [https://proceedings.mlr.press/v235/singhal24a.html](https://proceedings.mlr.press/v235/singhal24a.html)

**TLDR**: Develops automated denoising score matching for nonlinear diffusion processes beyond the standard linear Gaussian setting.

## Abstract

Reversing a diffusion process by learning its score forms the heart of diffusion-based generative modeling and for estimating properties of scientific systems. The diffusion processes that are tractable center on linear processes with a Gaussian stationary distribution, limiting the kinds of models that can be built to those that target a Gaussian prior or more generally limits the kinds of problems that can be generically solved to those that have conditionally linear score functions. In this work, we introduce a family of tractable denoising score matching objectives, called local-DSM, built using local increments of the diffusion process. We show how local-DSM melded with Taylor expansions enables automated training and score estimation with nonlinear diffusion processes. To demonstrate these ideas, we use automated-DSM to train generative models using non-Gaussian priors on challenging low dimensional distributions and the CIFAR10 image dataset. Additionally, we use the automated-DSM to learn the scores for nonlinear processes studied in statistical physics.