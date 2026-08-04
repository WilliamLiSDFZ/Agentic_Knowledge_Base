---
title: "How Deep Networks Learn Sparse and Hierarchical Data: the Sparse Random Hierarchy Model"
source: "https://proceedings.mlr.press/v235/tomasini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tomasini24a/tomasini24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'time-series-modeling-and-forecasting-methods']
tags: ['deep-learning-theory', 'hierarchical-representations', 'sparse-data']
venue: "ICML 2024"
tldr: "The Sparse Random Hierarchy Model is introduced to theoretically analyze how deep networks learn hierarchical and sparse data structures more efficiently than shallow models."
---

# How Deep Networks Learn Sparse and Hierarchical Data: the Sparse Random Hierarchy Model

**Source**: [https://proceedings.mlr.press/v235/tomasini24a.html](https://proceedings.mlr.press/v235/tomasini24a.html)

**TLDR**: The Sparse Random Hierarchy Model is introduced to theoretically analyze how deep networks learn hierarchical and sparse data structures more efficiently than shallow models.

## Abstract

Understanding what makes high-dimensional data learnable is a fundamental question in machine learning. On the one hand, it is believed that the success of deep learning lies in its ability to build a hierarchy of representations that become increasingly more abstract with depth, going from simple features like edges to more complex concepts. On the other hand, learning to be insensitive to invariances of the task, such as smooth transformations for image datasets, has been argued to be important for deep networks and it strongly correlates with their performance. In this work, we aim to explain this correlation and unify these two viewpoints. We show that by introducing sparsity to generative hierarchical models of data, the task acquires insensitivity to spatial transformations that are discrete versions of smooth transformations. In particular, we introduce the Sparse Random Hierarchy Model (SRHM), where we observe and rationalize that a hierarchical representation mirroring the hierarchical model is learnt precisely when such insensitivity is learnt, thereby explaining the strong correlation between the latter and performance. Moreover, we quantify how the sample complexity of CNNs learning the SRHM depends on both the sparsity and hierarchical structure of the task.