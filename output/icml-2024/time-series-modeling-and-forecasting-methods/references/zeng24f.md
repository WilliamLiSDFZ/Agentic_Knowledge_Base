---
title: "Interacting Diffusion Processes for Event Sequence Forecasting"
source: "https://proceedings.mlr.press/v235/zeng24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24f/zeng24f.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'generative-models-and-variational-inference']
tags: ['temporal-point-processes', 'diffusion-models', 'event-forecasting']
venue: "ICML 2024"
tldr: "A novel framework incorporating interacting diffusion processes into temporal point processes for improved long-horizon event sequence forecasting."
---

# Interacting Diffusion Processes for Event Sequence Forecasting

**Source**: [https://proceedings.mlr.press/v235/zeng24f.html](https://proceedings.mlr.press/v235/zeng24f.html)

**TLDR**: A novel framework incorporating interacting diffusion processes into temporal point processes for improved long-horizon event sequence forecasting.

## Abstract

Neural Temporal Point Processes (TPPs) have emerged as the primary framework for predicting sequences of events that occur at irregular time intervals, but their sequential nature can hamper performance for long-horizon forecasts. To address this, we introduce a novel approach that incorporates a diffusion generative model. The model facilitates sequence-to-sequence prediction, allowing multi-step predictions based on historical event sequences. In contrast to previous approaches, our model directly learns the joint probability distribution of types and inter-arrival times for multiple events. The model is composed of two diffusion processes, one for the time intervals and one for the event types. These processes interact through their respective denoising functions, which can take as input intermediate representations from both processes, allowing the model to learn complex interactions. We demonstrate that our proposal outperforms state-of-the-art baselines for long-horizon forecasting of TPPs.