---
title: "Auto-Linear Phenomenon in Subsurface Imaging"
source: "https://proceedings.mlr.press/v235/feng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24a/feng24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['full-waveform-inversion', 'subsurface-imaging', 'encoder-decoder']
venue: "ICML 2024"
tldr: "Discovers an auto-linear phenomenon in subsurface imaging neural networks that simplifies the image-to-image translation for geophysical inversion."
---

# Auto-Linear Phenomenon in Subsurface Imaging

**Source**: [https://proceedings.mlr.press/v235/feng24a.html](https://proceedings.mlr.press/v235/feng24a.html)

**TLDR**: Discovers an auto-linear phenomenon in subsurface imaging neural networks that simplifies the image-to-image translation for geophysical inversion.

## Abstract

Subsurface imaging involves solving full waveform inversion (FWI) to predict geophysical properties from measurements. This problem can be reframed as an image-to-image translation, with the usual approach being to train an encoder-decoder network using paired data from two domains: geophysical property and measurement. A recent seminal work (InvLINT) demonstrates there is only a linear mapping between the latent spaces of the two domains, and the decoder requires paired data for training. This paper extends this direction by demonstrating that only linear mapping necessitates paired data, while both the encoder and decoder can be learned from their respective domains through self-supervised learning. This unveils an intriguing phenomenon (named Auto-Linear) where the self-learned features of two separate domains are automatically linearly correlated. Compared with existing methods, our Auto-Linear has four advantages: (a) solving both forward and inverse modeling simultaneously, (b) reducing model size, (c) enhanced performance, especially when the paired data is limited, and (d) strong generalization ability of the trained encoder and decoder.