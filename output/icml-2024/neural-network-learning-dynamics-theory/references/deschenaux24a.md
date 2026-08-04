---
title: "Going beyond Compositions, DDPMs Can Produce Zero-Shot Interpolations"
source: "https://proceedings.mlr.press/v235/deschenaux24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deschenaux24a/deschenaux24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['diffusion-models', 'zero-shot-generalization', 'interpolation', 'latent-factors', 'image-generation']
venue: "ICML 2024"
tldr: "DDPMs trained on disjoint data subsets can perform zero-shot interpolation between unseen combinations of latent factors, going beyond mere composition."
---

# Going beyond Compositions, DDPMs Can Produce Zero-Shot Interpolations

**Source**: [https://proceedings.mlr.press/v235/deschenaux24a.html](https://proceedings.mlr.press/v235/deschenaux24a.html)

**TLDR**: DDPMs trained on disjoint data subsets can perform zero-shot interpolation between unseen combinations of latent factors, going beyond mere composition.

## Abstract

Denoising Diffusion Probabilistic Models (DDPMs) exhibit remarkable capabilities in image generation, with studies suggesting that they can generalize by composing latent factors learned from the training data. In this work, we go further and study DDPMs trained on strictly separate subsets of the data distribution with large gaps on the support of the latent factors. We show that such a model can effectively generate images in the unexplored, intermediate regions of the distribution. For instance, when trained on clearly smiling and non-smiling faces, we demonstrate a sampling procedure which can generate slightly smiling faces without reference images (zero-shot interpolation). We replicate these findings for other attributes as well as other datasets. Our code is available on GitHub.