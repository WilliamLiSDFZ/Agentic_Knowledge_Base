---
title: "Generative Marginalization Models"
source: "https://proceedings.mlr.press/v235/liu24az.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24az/liu24az.pdf"
categories: ['probabilistic-generating-circuits-research', 'generative-models-and-variational-inference']
tags: ['generative-models', 'marginal-distributions', 'discrete-data']
venue: "ICML 2024"
tldr: "Marginalization models, a new family of generative models for discrete data that explicitly model all induced marginal distributions for scalable and flexible generation."
---

# Generative Marginalization Models

**Source**: [https://proceedings.mlr.press/v235/liu24az.html](https://proceedings.mlr.press/v235/liu24az.html)

**TLDR**: Marginalization models, a new family of generative models for discrete data that explicitly model all induced marginal distributions for scalable and flexible generation.

## Abstract

We introduce marginalization models (MAMs), a new family of generative models for high-dimensional discrete data. They offer scalable and flexible generative modeling by explicitly modeling all induced marginal distributions. Marginalization models enable fast approximation of arbitrary marginal probabilities with a single forward pass of the neural network, which overcomes a major limitation of arbitrary marginal inference models, such as any-order autoregressive models. MAMs also address the scalability bottleneck encountered in training any-order generative models for high-dimensional problems under the context of energy-based training, where the goal is to match the learned distribution to a given desired probability (specified by an unnormalized log-probability function such as energy or reward function). We propose scalable methods for learning the marginals, grounded in the concept of "marginalization self-consistency". We demonstrate the effectiveness of the proposed model on a variety of discrete data distributions, including images, text, physical systems, and molecules, for maximum likelihood and energy-based training settings. MAMs achieve orders of magnitude speedup in evaluating the marginal probabilities on both settings. For energy-based training tasks, MAMs enable any-order generative modeling of high-dimensional problems beyond the scale of previous methods. Code is available at github.com/PrincetonLIPS/MaM.