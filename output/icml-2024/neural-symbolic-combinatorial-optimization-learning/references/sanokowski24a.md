---
title: "A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization"
source: "https://proceedings.mlr.press/v235/sanokowski24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sanokowski24a/sanokowski24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'combinatorial-optimization', 'discrete-generation', 'unsupervised', 'energy-based']
venue: "ICML 2024"
tldr: "A diffusion model framework is proposed for unsupervised neural combinatorial optimization by learning to sample from intractable discrete distributions."
---

# A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization

**Source**: [https://proceedings.mlr.press/v235/sanokowski24a.html](https://proceedings.mlr.press/v235/sanokowski24a.html)

**TLDR**: A diffusion model framework is proposed for unsupervised neural combinatorial optimization by learning to sample from intractable discrete distributions.

## Abstract

Learning to sample from intractable distributions over discrete sets without relying on corresponding training data is a central problem in a wide range of fields, including Combinatorial Optimization. Currently, popular deep learning-based approaches rely primarily on generative models that yield exact sample likelihoods. This work introduces a method that lifts this restriction and opens the possibility to employ highly expressive latent variable models like diffusion models. Our approach is conceptually based on a loss that upper bounds the reverse Kullback-Leibler divergence and evades the requirement of exact sample likelihoods. We experimentally validate our approach in data-free Combinatorial Optimization and demonstrate that our method achieves a new state-of-the-art on a wide range of benchmark problems.