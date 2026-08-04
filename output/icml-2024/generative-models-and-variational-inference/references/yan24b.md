---
title: "Probabilistic Time Series Modeling with Decomposable Denoising Diffusion Model"
source: "https://proceedings.mlr.press/v235/yan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24b/yan24b.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'generative-models-and-variational-inference']
tags: ['probabilistic-forecasting', 'denoising-diffusion', 'time-series-decomposition']
venue: "ICML 2024"
tldr: "Introduces a decomposable denoising diffusion model for probabilistic time series modeling that separates trend and seasonal components."
---

# Probabilistic Time Series Modeling with Decomposable Denoising Diffusion Model

**Source**: [https://proceedings.mlr.press/v235/yan24b.html](https://proceedings.mlr.press/v235/yan24b.html)

**TLDR**: Introduces a decomposable denoising diffusion model for probabilistic time series modeling that separates trend and seasonal components.

## Abstract

Probabilistic time series modeling based on generative models has attracted lots of attention because of its wide applications and excellent performance. However, existing state-of-the-art models, based on stochastic differential equation, not only struggle to determine the drift and diffusion coefficients during the design process but also have slow generation speed. To tackle this challenge, we firstly propose decomposable denoising diffusion model ($\text{D}^3\text{M}$) and prove it is a general framework unifying denoising diffusion models and continuous flow models. Based on the new framework, we propose some simple but efficient probability paths with high generation speed. Furthermore, we design a module that combines a special state space model with linear gated attention modules for sequence modeling. It preserves inductive bias and simultaneously models both local and global dependencies. Experimental results on 8 real-world datasets show that $\text{D}^3\text{M}$ reduces RMSE and CRPS by up to 4.6% and 4.3% compared with state-of-the-arts on imputation tasks, and achieves comparable results with state-of-the-arts on forecasting tasks with only 10 steps.