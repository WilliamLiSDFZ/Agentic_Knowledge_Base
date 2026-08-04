---
title: "DFlow: A Generative Model Combining Denoising AutoEncoder and Normalizing Flow for High Fidelity Waveform Generation"
source: "https://proceedings.mlr.press/v235/miao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/miao24d/miao24d.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['normalizing-flow', 'denoising-autoencoder', 'waveform-generation']
venue: "ICML 2024"
tldr: "Presents DFlow, a generative framework combining normalizing flows and denoising autoencoders for high-fidelity audio waveform generation."
---

# DFlow: A Generative Model Combining Denoising AutoEncoder and Normalizing Flow for High Fidelity Waveform Generation

**Source**: [https://proceedings.mlr.press/v235/miao24d.html](https://proceedings.mlr.press/v235/miao24d.html)

**TLDR**: Presents DFlow, a generative framework combining normalizing flows and denoising autoencoders for high-fidelity audio waveform generation.

## Abstract

In this work, we present DFlow, a novel generative framework that combines Normalizing Flow (NF) with a Denoising AutoEncoder (DAE), for high-fidelity waveform generation. With a tactfully designed structure, DFlow seamlessly integrates the capabilities of both NF and DAE, resulting in a significantly improved performance compared to the standard NF models. Experimental results showcase DFlow’s superiority, achieving the highest MOS score among the existing methods on commonly used datasets and the fastest synthesis speed among all likelihood models. We further demonstrate the generalization ability of DFlow by generating high-quality out-of-distribution audio samples, such as singing and music audio. Additionally, we extend the model capacity of DFlow by scaling up both the model size and training set size. Our large-scale universal vocoder, DFlow-XL, achieves highly competitive performance against the best universal vocoder, BigVGAN.