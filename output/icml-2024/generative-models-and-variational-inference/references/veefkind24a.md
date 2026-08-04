---
title: "A Probabilistic Approach to Learning the Degree of Equivariance in Steerable CNNs"
source: "https://proceedings.mlr.press/v235/veefkind24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/veefkind24a/veefkind24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'generative-models-and-variational-inference']
tags: ['steerable-CNNs', 'equivariance', 'symmetry-learning', 'probabilistic', 'geometric-deep-learning']
venue: "ICML 2024"
tldr: "Introduces a probabilistic approach to learning the degree of equivariance in steerable CNNs to handle unknown or varying geometric symmetries."
---

# A Probabilistic Approach to Learning the Degree of Equivariance in Steerable CNNs

**Source**: [https://proceedings.mlr.press/v235/veefkind24a.html](https://proceedings.mlr.press/v235/veefkind24a.html)

**TLDR**: Introduces a probabilistic approach to learning the degree of equivariance in steerable CNNs to handle unknown or varying geometric symmetries.

## Abstract

Steerable convolutional neural networks (SCNNs) enhance task performance by modelling geometric symmetries through equivariance constraints on weights. Yet, unknown or varying symmetries can lead to overconstrained weights and decreased performance. To address this, this paper introduces a probabilistic method to learn the degree of equivariance in SCNNs. We parameterise the degree of equivariance as a likelihood distribution over the transformation group using Fourier coefficients, offering the option to model layer-wise and shared equivariance. These likelihood distributions are regularised to ensure an interpretable degree of equivariance across the network. Advantages include the applicability to many types of equivariant networks through the flexible framework of SCNNs and the ability to learn equivariance with respect to any subgroup of any compact group without requiring additional layers. Our experiments reveal competitive performance on datasets with mixed symmetries, with learnt likelihood distributions that are representative of the underlying degree of equivariance.