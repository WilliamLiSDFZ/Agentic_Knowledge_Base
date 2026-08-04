---
title: "Initial Guessing Bias: How Untrained Networks Favor Some Classes"
source: "https://proceedings.mlr.press/v235/francazi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/francazi24a/francazi24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'fairness-aware-algorithmic-decision-making']
tags: ['initialization-bias', 'neural-network-fairness', 'classification']
venue: "ICML 2024"
tldr: "Deep neural network architecture inherently biases class predictions before training, with implications for fairness and accuracy."
---

# Initial Guessing Bias: How Untrained Networks Favor Some Classes

**Source**: [https://proceedings.mlr.press/v235/francazi24a.html](https://proceedings.mlr.press/v235/francazi24a.html)

**TLDR**: Deep neural network architecture inherently biases class predictions before training, with implications for fairness and accuracy.

## Abstract

Understanding and controlling biasing effects in neural networks is crucial for ensuring accurate and fair model performance. In the context of classification problems, we provide a theoretical analysis demonstrating that the structure of a deep neural network (DNN) can condition the model to assign all predictions to the same class, even before the beginning of training, and in the absence of explicit biases. We prove that, besides dataset properties, the presence of this phenomenon, which we call Initial Guessing Bias (IGB), is influenced by model choices including dataset preprocessing methods, and architectural decisions, such as activation functions, max-pooling layers, and network depth. Our analysis of IGB provides information for architecture selection and model initialization. We also highlight theoretical consequences, such as the breakdown of node-permutation symmetry, the violation of self-averaging and the non-trivial effects that depth has on the phenomenon.