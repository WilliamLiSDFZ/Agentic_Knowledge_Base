---
title: "Tripod: Three Complementary Inductive Biases for Disentangled Representation Learning"
source: "https://proceedings.mlr.press/v235/hsu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hsu24a/hsu24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['disentangled-representation', 'inductive-biases', 'quantization', 'autoencoder', 'variational']
venue: "ICML 2024"
tldr: "Combines three complementary inductive biases—quantization, sparsity, and modular structure—in an autoencoder for improved disentangled representation learning."
---

# Tripod: Three Complementary Inductive Biases for Disentangled Representation Learning

**Source**: [https://proceedings.mlr.press/v235/hsu24a.html](https://proceedings.mlr.press/v235/hsu24a.html)

**TLDR**: Combines three complementary inductive biases—quantization, sparsity, and modular structure—in an autoencoder for improved disentangled representation learning.

## Abstract

Inductive biases are crucial in disentangled representation learning for narrowing down an underspecified solution set. In this work, we consider endowing a neural network autoencoder with three select inductive biases from the literature: data compression into a grid-like latent space via quantization, collective independence amongst latents, and minimal functional influence of any latent on how other latents determine data generation. In principle, these inductive biases are deeply complementary: they most directly specify properties of the latent space, encoder, and decoder, respectively. In practice, however, naively combining existing techniques instantiating these inductive biases fails to yield significant benefits. To address this, we propose adaptations to the three techniques that simplify the learning problem, equip key regularization terms with stabilizing invariances, and quash degenerate incentives. The resulting model, Tripod, achieves state-of-the-art results on a suite of four image disentanglement benchmarks. We also verify that Tripod significantly improves upon its naive incarnation and that all three of its "legs" are necessary for best performance.