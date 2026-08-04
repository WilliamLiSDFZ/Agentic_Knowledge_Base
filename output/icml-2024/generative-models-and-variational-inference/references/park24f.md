---
title: "Mean-field Chaos Diffusion Models"
source: "https://proceedings.mlr.press/v235/park24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24f/park24f.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['score-based-generative-models', 'mean-field-theory', 'diffusion-models', 'high-cardinality']
venue: "ICML 2024"
tldr: "Introduces mean-field chaos diffusion models that leverage mean-field theory to scale score-based generative models to high-cardinality data distributions."
---

# Mean-field Chaos Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/park24f.html](https://proceedings.mlr.press/v235/park24f.html)

**TLDR**: Introduces mean-field chaos diffusion models that leverage mean-field theory to scale score-based generative models to high-cardinality data distributions.

## Abstract

In this paper, we introduce a new class of score-based generative models (SGMs) designed to handle high-cardinality data distributions by leveraging concepts from mean-field theory. We present mean-field chaos diffusion models (MF-CDMs), which address the curse of dimensionality inherent in high-cardinality data by utilizing the propagation of chaos property of interacting particles. By treating high-cardinality data as a large stochastic system of interacting particles, we develop a novel score-matching method for infinite-dimensional chaotic particle systems and propose an approximation scheme that employs a subdivision strategy for efficient training. Our theoretical and empirical results demonstrate the scalability and effectiveness of MF-CDMs for managing large high-cardinality data structures, such as 3D point clouds.