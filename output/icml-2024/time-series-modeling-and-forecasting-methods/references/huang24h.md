---
title: "DiffDA: a Diffusion model for weather-scale Data Assimilation"
source: "https://proceedings.mlr.press/v235/huang24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24h/huang24h.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'time-series-modeling-and-forecasting-methods']
tags: ['data-assimilation', 'diffusion-models', 'weather-forecasting']
venue: "ICML 2024"
tldr: "Presents DiffDA, a denoising diffusion model for weather-scale data assimilation using predicted states and sparse observations."
---

# DiffDA: a Diffusion model for weather-scale Data Assimilation

**Source**: [https://proceedings.mlr.press/v235/huang24h.html](https://proceedings.mlr.press/v235/huang24h.html)

**TLDR**: Presents DiffDA, a denoising diffusion model for weather-scale data assimilation using predicted states and sparse observations.

## Abstract

The generation of initial conditions via accurate data assimilation is crucial for weather forecasting and climate modeling. We propose DiffDA as a denoising diffusion model capable of assimilating atmospheric variables using predicted states and sparse observations. Acknowledging the similarity between a weather forecast model and a denoising diffusion model dedicated to weather applications, we adapt the pretrained GraphCast neural network as the backbone of the diffusion model. Through experiments based on simulated observations from the ERA5 reanalysis dataset, our method can produce assimilated global atmospheric data consistent with observations at 0.25$^\circ$ ($\approx$30km) resolution globally. This marks the highest resolution achieved by ML data assimilation models. The experiments also show that the initial conditions assimilated from sparse observations (less than 0.96% of gridded data) and 48-hour forecast can be used for forecast models with a loss of lead time of at most 24 hours compared to initial conditions from state-of-the-art data assimilation in ERA5. This enables the application of the method to real-world applications, such as creating reanalysis datasets with autoregressive data assimilation.