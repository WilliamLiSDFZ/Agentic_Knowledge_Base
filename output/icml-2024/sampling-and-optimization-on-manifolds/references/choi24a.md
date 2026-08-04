---
title: "Scalable Wasserstein Gradient Flow for Generative Modeling through Unbalanced Optimal Transport"
source: "https://proceedings.mlr.press/v235/choi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24a/choi24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['wasserstein-gradient-flow', 'generative-modeling', 'unbalanced-optimal-transport']
venue: "ICML 2024"
tldr: "A scalable Wasserstein gradient flow framework for generative modeling is developed using unbalanced optimal transport discretization."
---

# Scalable Wasserstein Gradient Flow for Generative Modeling through Unbalanced Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/choi24a.html](https://proceedings.mlr.press/v235/choi24a.html)

**TLDR**: A scalable Wasserstein gradient flow framework for generative modeling is developed using unbalanced optimal transport discretization.

## Abstract

Wasserstein gradient flow (WGF) describes the gradient dynamics of probability density within the Wasserstein space. WGF provides a promising approach for conducting optimization over the probability distributions. Numerically approximating the continuous WGF requires the time discretization method. The most well-known method for this is the JKO scheme. In this regard, previous WGF models employ the JKO scheme and parametrized transport map for each JKO step. However, this approach results in quadratic training complexity $O(K^2)$ with the number of JKO step $K$. This severely limits the scalability of WGF models. In this paper, we introduce a scalable WGF-based generative model, called Semi-dual JKO (S-JKO). Our model is based on the semi-dual form of the JKO step, derived from the equivalence between the JKO step and the Unbalanced Optimal Transport. Our approach reduces the training complexity to $O(K)$. We demonstrate that our model significantly outperforms existing WGF-based generative models, achieving FID scores of 2.62 on CIFAR-10 and 6.42 on CelebA-HQ-256, which are comparable to state-of-the-art image generative models.