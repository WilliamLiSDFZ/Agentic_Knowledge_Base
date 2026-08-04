---
title: "Time Series Diffusion in the Frequency Domain"
source: "https://proceedings.mlr.press/v235/crabbe24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/crabbe24a/crabbe24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'generative-models-and-variational-inference']
tags: ['time-series', 'diffusion-models', 'frequency-domain']
venue: "ICML 2024"
tldr: "Explores time series diffusion modeling in the frequency domain using Fourier analysis to improve generative performance."
---

# Time Series Diffusion in the Frequency Domain

**Source**: [https://proceedings.mlr.press/v235/crabbe24a.html](https://proceedings.mlr.press/v235/crabbe24a.html)

**TLDR**: Explores time series diffusion modeling in the frequency domain using Fourier analysis to improve generative performance.

## Abstract

Fourier analysis has been an instrumental tool in the development of signal processing. This leads us to wonder whether this framework could similarly benefit generative modelling. In this paper, we explore this question through the scope of time series diffusion models. More specifically, we analyze whether representing time series in the frequency domain is a useful inductive bias for score-based diffusion models. By starting from the canonical SDE formulation of diffusion in the time domain, we show that a dual diffusion process occurs in the frequency domain with an important nuance: Brownian motions are replaced by what we call mirrored Brownian motions, characterized by mirror symmetries among their components. Building on this insight, we show how to adapt the denoising score matching approach to implement diffusion models in the frequency domain. This results in frequency diffusion models, which we compare to canonical time diffusion models. Our empirical evaluation on real-world datasets, covering various domains like healthcare and finance, shows that frequency diffusion models better capture the training distribution than time diffusion models. We explain this observation by showing that time series from these datasets tend to be more localized in the frequency domain than in the time domain, which makes them easier to model in the former case. All our observations point towards impactful synergies between Fourier analysis and diffusion models.