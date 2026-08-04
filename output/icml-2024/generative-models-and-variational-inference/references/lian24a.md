---
title: "Kepler codebook"
source: "https://proceedings.mlr.press/v235/lian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lian24a/lian24a.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['codebook', 'discrete-representation', 'sphere-packing']
venue: "ICML 2024"
tldr: "Kepler codebook frames codebook training as a sphere-packing problem to learn better discrete distributions for generative models."
---

# Kepler codebook

**Source**: [https://proceedings.mlr.press/v235/lian24a.html](https://proceedings.mlr.press/v235/lian24a.html)

**TLDR**: Kepler codebook frames codebook training as a sphere-packing problem to learn better discrete distributions for generative models.

## Abstract

A codebook designed for learning discrete distributions in latent space has demonstrated state-of-the-art results on generation tasks. This inspires us to explore what distribution of codebook is better. Following the spirit of Kepler’s Conjecture, we cast the codebook training as solving the sphere packing problem and derive a Kepler codebook with a compact and structured distribution to obtain a codebook for image representations. Furthermore, we implement the Kepler codebook training by simply employing this derived distribution as regularization and using the codebook partition method. We conduct extensive experiments to evaluate our trained codebook for image reconstruction and generation on natural and human face datasets, respectively, achieving significant performance improvement. Besides, our Kepler codebook has demonstrated superior performance when evaluated across datasets and even for reconstructing images with different resolutions. Our trained models and source codes will be publicly released.