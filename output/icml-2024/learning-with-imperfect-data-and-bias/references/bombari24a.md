---
title: "How Spurious Features are Memorized: Precise Analysis for Random and NTK Features"
source: "https://proceedings.mlr.press/v235/bombari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bombari24a/bombari24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['spurious-features', 'memorization', 'random-features', 'NTK']
venue: "ICML 2024"
tldr: "This paper provides a precise theoretical analysis of how spurious features are memorized in random feature and NTK models during training."
---

# How Spurious Features are Memorized: Precise Analysis for Random and NTK Features

**Source**: [https://proceedings.mlr.press/v235/bombari24a.html](https://proceedings.mlr.press/v235/bombari24a.html)

**TLDR**: This paper provides a precise theoretical analysis of how spurious features are memorized in random feature and NTK models during training.

## Abstract

Deep learning models are known to overfit and memorize spurious features in the training dataset. While numerous empirical studies have aimed at understanding this phenomenon, a rigorous theoretical framework to quantify it is still missing. In this paper, we consider spurious features that are uncorrelated with the learning task, and we provide a precise characterization of how they are memorized via two separate terms: (i) the stability of the model with respect to individual training samples, and (ii) the feature alignment between the spurious pattern and the full sample. While the first term is well established in learning theory and it is connected to the generalization error in classical work, the second one is, to the best of our knowledge, novel. Our key technical result gives a precise characterization of the feature alignment for the two prototypical settings of random features (RF) and neural tangent kernel (NTK) regression. We prove that the memorization of spurious features weakens as the generalization capability increases and, through the analysis of the feature alignment, we unveil the role of the model and of its activation function. Numerical experiments show the predictive power of our theory on standard datasets (MNIST, CIFAR-10).