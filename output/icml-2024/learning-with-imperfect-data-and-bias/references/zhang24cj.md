---
title: "Feature Contamination: Neural Networks Learn Uncorrelated Features and Fail to Generalize"
source: "https://proceedings.mlr.press/v235/zhang24cj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cj/zhang24cj.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'neural-network-learning-dynamics-theory']
tags: ['distribution-shift', 'feature-learning', 'generalization']
venue: "ICML 2024"
tldr: "Theoretically characterizes how neural networks learn uncorrelated features leading to failure under distribution shifts."
---

# Feature Contamination: Neural Networks Learn Uncorrelated Features and Fail to Generalize

**Source**: [https://proceedings.mlr.press/v235/zhang24cj.html](https://proceedings.mlr.press/v235/zhang24cj.html)

**TLDR**: Theoretically characterizes how neural networks learn uncorrelated features leading to failure under distribution shifts.

## Abstract

Learning representations that generalize under distribution shifts is critical for building robust machine learning models. However, despite significant efforts in recent years, algorithmic advances in this direction have been limited. In this work, we seek to understand the fundamental difficulty of out-of-distribution generalization with deep neural networks. We first empirically show that perhaps surprisingly, even allowing a neural network to explicitly fit the representations obtained from a teacher network that can generalize out-of-distribution is insufficient for the generalization of the student network. Then, by a theoretical study of two-layer ReLU networks optimized by stochastic gradient descent (SGD) under a structured feature model, we identify a fundamental yet unexplored feature learning proclivity of neural networks, feature contamination: neural networks can learn uncorrelated features together with predictive features, resulting in generalization failure under distribution shifts. Notably, this mechanism essentially differs from the prevailing narrative in the literature that attributes the generalization failure to spurious correlations. Overall, our results offer new insights into the non-linear feature learning dynamics of neural networks and highlight the necessity of considering inductive biases in out-of-distribution generalization.