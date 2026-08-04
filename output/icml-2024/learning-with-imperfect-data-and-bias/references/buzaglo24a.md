---
title: "How Uniform Random Weights Induce Non-uniform Bias: Typical Interpolating Neural Networks Generalize with Narrow Teachers"
source: "https://proceedings.mlr.press/v235/buzaglo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/buzaglo24a/buzaglo24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['neural-network-generalization', 'interpolation', 'implicit-bias', 'random-weights']
venue: "ICML 2024"
tldr: "Shows that uniform random weights induce a non-uniform bias favoring narrow teacher networks, explaining generalization of interpolating neural networks."
---

# How Uniform Random Weights Induce Non-uniform Bias: Typical Interpolating Neural Networks Generalize with Narrow Teachers

**Source**: [https://proceedings.mlr.press/v235/buzaglo24a.html](https://proceedings.mlr.press/v235/buzaglo24a.html)

**TLDR**: Shows that uniform random weights induce a non-uniform bias favoring narrow teacher networks, explaining generalization of interpolating neural networks.

## Abstract

A main theoretical puzzle is why over-parameterized Neural Networks (NNs) generalize well when trained to zero loss (i.e., so they interpolate the data). Usually, the NN is trained with Stochastic Gradient Descent (SGD) or one of its variants. However, recent empirical work examined the generalization of a random NN that interpolates the data: the NN was sampled from a seemingly uniform prior over the parameters, conditioned on that the NN perfectly classifying the training set. Interestingly, such a NN sample typically generalized as well as SGD-trained NNs. We prove that such a random NN interpolator typically generalizes well if there exists an underlying narrow “teacher NN" that agrees with the labels. Specifically, we show that such a ‘flat’ prior over the NN parametrization induces a rich prior over the NN functions, due to the redundancy in the NN structure. In particular, this creates a bias towards simpler functions, which require less relevant parameters to represent — enabling learning with a sample complexity approximately proportional to the complexity of the teacher (roughly, the number of non-redundant parameters), rather than the student’s.