---
title: "Exploring the Low-Pass Filtering Behavior in Image Super-Resolution"
source: "https://proceedings.mlr.press/v235/deng24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deng24e/deng24e.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'neural-network-learning-dynamics-theory']
tags: ['image-super-resolution', 'low-pass-filtering', 'deep-neural-networks', 'frequency-analysis', 'interpretability']
venue: "ICML 2024"
tldr: "Interprets deep image super-resolution networks through the lens of low-pass filtering behavior to provide a mathematical understanding of their operation."
---

# Exploring the Low-Pass Filtering Behavior in Image Super-Resolution

**Source**: [https://proceedings.mlr.press/v235/deng24e.html](https://proceedings.mlr.press/v235/deng24e.html)

**TLDR**: Interprets deep image super-resolution networks through the lens of low-pass filtering behavior to provide a mathematical understanding of their operation.

## Abstract

Deep neural networks for image super-resolution (ISR) have shown significant advantages over traditional approaches like the interpolation. However, they are often criticized as ’black boxes’ compared to traditional approaches with solid mathematical foundations. In this paper, we attempt to interpret the behavior of deep neural networks in ISR using theories from the field of signal processing. First, we report an intriguing phenomenon, referred to as ‘the sinc phenomenon.’ It occurs when an impulse input is fed to a neural network. Then, building on this observation, we propose a method named Hybrid Response Analysis (HyRA) to analyze the behavior of neural networks in ISR tasks. Specifically, HyRA decomposes a neural network into a parallel connection of a linear system and a non-linear system and demonstrates that the linear system functions as a low-pass filter while the non-linear system injects high-frequency information. Finally, to quantify the injected high-frequency information, we introduce a metric for image-to-image tasks called Frequency Spectrum Distribution Similarity (FSDS). FSDS reflects the distribution similarity of different frequency components and can capture nuances that traditional metrics may overlook. Code, videos and raw experimental results for this paper can be found in: https://github.com/RisingEntropy/LPFInISR.