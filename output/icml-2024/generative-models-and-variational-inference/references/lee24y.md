---
title: "Behavior Generation with Latent Actions"
source: "https://proceedings.mlr.press/v235/lee24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24y/lee24y.pdf"
categories: ['generative-models-and-variational-inference', 'neural-operators-for-pde-solving']
tags: ['behavior-generation', 'latent-actions', 'decision-making', 'generative-models']
venue: "ICML 2024"
tldr: "Introduces a behavior generation framework using latent action spaces to model multimodal action distributions for decision-making."
---

# Behavior Generation with Latent Actions

**Source**: [https://proceedings.mlr.press/v235/lee24y.html](https://proceedings.mlr.press/v235/lee24y.html)

**TLDR**: Introduces a behavior generation framework using latent action spaces to model multimodal action distributions for decision-making.

## Abstract

Generative modeling of complex behaviors from labeled datasets has been a longstanding problem in decision-making. Unlike language or image generation, decision-making requires modeling actions – continuous-valued vectors that are multimodal in their distribution, potentially drawn from uncurated sources, where generation errors can compound in sequential prediction. A recent class of models called Behavior Transformers (BeT) addresses this by discretizing actions using k-means clustering to capture different modes. However, k-means struggles to scale for high-dimensional action spaces or long sequences, and lacks gradient information, and thus BeT suffers in modeling long-range actions. In this work, we present Vector-Quantized Behavior Transformer (VQ-BeT), a versatile model for behavior generation that handles multimodal action prediction, conditional generation, and partial observations. VQ-BeT augments BeT by tokenizing continuous actions with a hierarchical vector quantization module. Across seven environments including simulated manipulation, autonomous driving, and robotics, VQ-BeT improves on state-of-the-art models such as BeT and Diffusion Policies. Importantly, we demonstrate VQ-BeT’s improved ability to capture behavior modes while accelerating inference speed 5× over Diffusion Policies. Videos can be found https://sjlee.cc/vq-bet/