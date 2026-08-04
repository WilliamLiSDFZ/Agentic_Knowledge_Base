---
title: "Rolling Diffusion Models"
source: "https://proceedings.mlr.press/v235/ruhe24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ruhe24a/ruhe24a.pdf"
categories: ['generative-models-and-variational-inference', 'time-series-modeling-and-forecasting-methods']
tags: ['diffusion-models', 'temporal-data', 'video-generation', 'rolling-diffusion', 'noise-scheduling']
venue: "ICML 2024"
tldr: "Rolling Diffusion introduces a sliding-window noise schedule for diffusion models that better handles temporal data such as video and climate simulations."
---

# Rolling Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/ruhe24a.html](https://proceedings.mlr.press/v235/ruhe24a.html)

**TLDR**: Rolling Diffusion introduces a sliding-window noise schedule for diffusion models that better handles temporal data such as video and climate simulations.

## Abstract

Diffusion models have recently been increasingly applied to temporal data such as video, fluid mechanics simulations, or climate data. These methods generally treat subsequent frames equally regarding the amount of noise in the diffusion process. This paper explores Rolling Diffusion: a new approach that uses a sliding window denoising process. It ensures that the diffusion process progressively corrupts through time by assigning more noise to frames that appear later in a sequence, reflecting greater uncertainty about the future as the generation process unfolds. Empirically, we show that when the temporal dynamics are complex, Rolling Diffusion is superior to standard diffusion. In particular, this result is demonstrated in a video prediction task using the Kinetics-600 video dataset and in a chaotic fluid dynamics forecasting experiment.