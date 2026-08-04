---
title: "A Simple Early Exiting Framework for Accelerated Sampling in Diffusion Models"
source: "https://proceedings.mlr.press/v235/moon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/moon24a/moon24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'early-exiting', 'accelerated-sampling', 'inference-efficiency']
venue: "ICML 2024"
tldr: "An early exiting framework is introduced for diffusion models that skips score network evaluations at certain timesteps to significantly accelerate sampling without retraining."
---

# A Simple Early Exiting Framework for Accelerated Sampling in Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/moon24a.html](https://proceedings.mlr.press/v235/moon24a.html)

**TLDR**: An early exiting framework is introduced for diffusion models that skips score network evaluations at certain timesteps to significantly accelerate sampling without retraining.

## Abstract

Diffusion models have shown remarkable performance in generation problems over various domains including images, videos, text, and audio. A practical bottleneck of diffusion models is their sampling speed, due to the repeated evaluation of score estimation networks during the inference. In this work, we propose a novel framework capable of adaptively allocating compute required for the score estimation, thereby reducing the overall sampling time of diffusion models. We observe that the amount of computation required for the score estimation may vary along the time step for which the score is estimated. Based on this observation, we propose an early-exiting scheme, where we skip the subset of parameters in the score estimation network during the inference, based on a time-dependent exit schedule. Using the diffusion models for image synthesis, we show that our method could significantly improve the sampling throughput of the diffusion models without compromising image quality. Furthermore, we also demonstrate that our method seamlessly integrates with various types of solvers for faster sampling, capitalizing on their compatibility to enhance overall efficiency.