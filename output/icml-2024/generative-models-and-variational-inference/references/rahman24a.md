---
title: "Modular Learning of Deep Causal Generative Models for High-dimensional Causal Inference"
source: "https://proceedings.mlr.press/v235/rahman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rahman24a/rahman24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['causal-inference', 'generative-models', 'high-dimensional', 'identifiability', 'causal-structure']
venue: "ICML 2024"
tldr: "A modular deep causal generative model framework enabling causal inference on high-dimensional data like images."
---

# Modular Learning of Deep Causal Generative Models for High-dimensional Causal Inference

**Source**: [https://proceedings.mlr.press/v235/rahman24a.html](https://proceedings.mlr.press/v235/rahman24a.html)

**TLDR**: A modular deep causal generative model framework enabling causal inference on high-dimensional data like images.

## Abstract

Sound and complete algorithms have been proposed to compute identifiable causal queries using the causal structure and data. However, most of these algorithms assume accurate estimation of the data distribution, which is impractical for high-dimensional variables such as images. On the other hand, modern deep generative architectures can be trained to sample from high-dimensional distributions. However, training these networks are typically very costly. Thus, it is desirable to leverage pre-trained models to answer causal queries using such high-dimensional data. To address this, we propose modular training of deep causal generative models that not only makes learning more efficient, but also allows us to utilize large, pre-trained conditional generative models. To the best of our knowledge, our algorithm, Modular-DCM is the first algorithm that, given the causal structure, uses adversarial training to learn the network weights, and can make use of pre-trained models to provably sample from any identifiable causal query in the presence of latent confounders. With extensive experiments on the Colored-MNIST dataset, we demonstrate that our algorithm outperforms the baselines. We also show our algorithm’s convergence on the COVIDx dataset and its utility with a causal invariant prediction problem on CelebA-HQ.