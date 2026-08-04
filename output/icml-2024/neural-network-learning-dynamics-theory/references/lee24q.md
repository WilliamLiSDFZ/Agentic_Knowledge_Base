---
title: "Defining Neural Network Architecture through Polytope Structures of Datasets"
source: "https://proceedings.mlr.press/v235/lee24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24q/lee24q.pdf"
categories: ['neural-network-learning-dynamics-theory', 'causal-ml-for-clinical-decision-making']
tags: ['neural-architecture', 'polytope', 'dataset-complexity', 'classification-bounds']
venue: "ICML 2024"
tldr: "Defines upper and lower bounds for neural network architecture size based on the polytope structure of datasets."
---

# Defining Neural Network Architecture through Polytope Structures of Datasets

**Source**: [https://proceedings.mlr.press/v235/lee24q.html](https://proceedings.mlr.press/v235/lee24q.html)

**TLDR**: Defines upper and lower bounds for neural network architecture size based on the polytope structure of datasets.

## Abstract

Current theoretical and empirical research in neural networks suggests that complex datasets require large network architectures for thorough classification, yet the precise nature of this relationship remains unclear. This paper tackles this issue by defining upper and lower bounds for neural network widths, which are informed by the polytope structure of the dataset in question. We also delve into the application of these principles to simplicial complexes and specific manifold shapes, explaining how the requirement for network width varies in accordance with the geometric complexity of the dataset. Moreover, we develop an algorithm to investigate a converse situation where the polytope structure of a dataset can be inferred from its corresponding trained neural networks. Through our algorithm, it is established that popular datasets such as MNIST, Fashion-MNIST, and CIFAR10 can be efficiently encapsulated using no more than two polytopes with a small number of faces.