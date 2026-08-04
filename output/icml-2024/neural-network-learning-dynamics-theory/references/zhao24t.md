---
title: "When Will Gradient Regularization Be Harmful?"
source: "https://proceedings.mlr.press/v235/zhao24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24t/zhao24t.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['gradient-regularization', 'over-parameterized-networks', 'domain-adaptation', 'performance-degeneration']
venue: "ICML 2024"
tldr: "This paper reveals conditions under which gradient regularization can harm performance in deep neural network training, particularly in adaptation scenarios."
---

# When Will Gradient Regularization Be Harmful?

**Source**: [https://proceedings.mlr.press/v235/zhao24t.html](https://proceedings.mlr.press/v235/zhao24t.html)

**TLDR**: This paper reveals conditions under which gradient regularization can harm performance in deep neural network training, particularly in adaptation scenarios.

## Abstract

Gradient regularization (GR), which aims to penalize the gradient norm atop the loss function, has shown promising results in training modern over-parameterized deep neural networks. However, can we trust this powerful technique? This paper reveals that GR can cause performance degeneration in adaptive optimization scenarios, particularly with learning rate warmup. Our empirical and theoretical analyses suggest this is due to GR inducing instability and divergence in gradient statistics of adaptive optimizers at the initial training stage. Inspired by the warmup heuristic, we propose three GR warmup strategies, each relaxing the regularization effect to a certain extent during the warmup course to ensure the accurate and stable accumulation of gradients. With experiments on Vision Transformer family, we confirm the three GR warmup strategies can effectively circumvent these issues, thereby largely improving the model performance. Meanwhile, we note that scalable models tend to rely more on the GR warmup, where the performance can be improved by up to 3% on Cifar10 compared to baseline GR. Code is available at https://github.com/zhaoyang-0204/gnp.