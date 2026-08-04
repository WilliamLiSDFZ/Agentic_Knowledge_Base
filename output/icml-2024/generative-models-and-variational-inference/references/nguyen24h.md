---
title: "Generative Conditional Distributions by Neural (Entropic) Optimal Transport"
source: "https://proceedings.mlr.press/v235/nguyen24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24h/nguyen24h.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['conditional-distributions', 'entropic-optimal-transport', 'generative-models']
venue: "ICML 2024"
tldr: "Introduces a neural entropic optimal transport method for learning generative models of conditional distributions across multiple covariate instances."
---

# Generative Conditional Distributions by Neural (Entropic) Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/nguyen24h.html](https://proceedings.mlr.press/v235/nguyen24h.html)

**TLDR**: Introduces a neural entropic optimal transport method for learning generative models of conditional distributions across multiple covariate instances.

## Abstract

Learning conditional distributions is challenging because the desired outcome is not a single distribution but multiple distributions that correspond to multiple instances of the covariates. We introduce a novel neural entropic optimal transport method designed to effectively learn generative models of conditional distributions, particularly in scenarios characterized by limited sample sizes. Our method relies on the minimax training of two neural networks: a generative network parametrizing the inverse cumulative distribution functions of the conditional distributions and another network parametrizing the conditional Kantorovich potential. To prevent overfitting, we regularize the objective function by penalizing the Lipschitz constant of the network output. Our experiments on real-world datasets show the effectiveness of our algorithm compared to state-of-the-art conditional distribution learning techniques. Our implementation can be found at https://github.com/nguyenngocbaocmt02/GENTLE.