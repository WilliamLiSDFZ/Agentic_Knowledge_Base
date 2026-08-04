---
title: "Optimal Eye Surgeon: Finding image priors through sparse generators at initialization"
source: "https://proceedings.mlr.press/v235/ghosh24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghosh24c/ghosh24c.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'generative-models-and-variational-inference']
tags: ['image-prior', 'sparse-generators', 'pruning-at-initialization']
venue: "ICML 2024"
tldr: "Introduces Optimal Eye Surgeon, a framework for finding image priors by pruning deep generators at initialization to prevent noise overfitting."
---

# Optimal Eye Surgeon: Finding image priors through sparse generators at initialization

**Source**: [https://proceedings.mlr.press/v235/ghosh24c.html](https://proceedings.mlr.press/v235/ghosh24c.html)

**TLDR**: Introduces Optimal Eye Surgeon, a framework for finding image priors by pruning deep generators at initialization to prevent noise overfitting.

## Abstract

We introduce Optimal Eye Surgeon (OES), a framework for pruning and training deep image generator networks. Typically, untrained deep convolutional networks, which include image sampling operations, serve as effective image priors. However, they tend to overfit to noise in image restoration tasks due to being overparameterized. OES addresses this by adaptively pruning networks at random initialization to a level of underparameterization. This process effectively captures low-frequency image components even without training, by just masking. When trained to fit noisy image, these pruned subnetworks, which we term Sparse-DIP, resist overfitting to noise. This benefit arises from underparameterization and the regularization effect of masking, constraining them in the manifold of image priors. We demonstrate that subnetworks pruned through OES surpass other leading pruning methods, such as the Lottery Ticket Hypothesis, which is known to be suboptimal for image recovery tasks. Our extensive experiments demonstrate the transferability of OES-masks and the characteristics of sparse-subnetworks for image generation. Code is available at https://github.com/Avra98/Optimal-Eye-Surgeon.