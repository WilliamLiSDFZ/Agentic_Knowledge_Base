---
title: "Provable Benefits of Local Steps in Heterogeneous Federated Learning for Neural Networks: A Feature Learning Perspective"
source: "https://proceedings.mlr.press/v235/bao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bao24a/bao24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'neural-network-learning-dynamics-theory']
tags: ['federated-learning', 'local-steps', 'feature-learning']
venue: "ICML 2024"
tldr: "This paper theoretically justifies the benefits of local steps in heterogeneous federated learning through a feature learning perspective."
---

# Provable Benefits of Local Steps in Heterogeneous Federated Learning for Neural Networks: A Feature Learning Perspective

**Source**: [https://proceedings.mlr.press/v235/bao24a.html](https://proceedings.mlr.press/v235/bao24a.html)

**TLDR**: This paper theoretically justifies the benefits of local steps in heterogeneous federated learning through a feature learning perspective.

## Abstract

Local steps are crucial for Federated Learning (FL) algorithms and have witnessed great empirical success in reducing communication costs and improving the generalization performance of deep neural networks. However, there are limited studies on the effect of local steps on heterogeneous FL. A few works investigate this problem from the optimization perspective. Woodworth et al. (2020a) showed that the iteration complexity of Local SGD, the most popular FL algorithm, is dominated by the baseline mini-batch SGD, which does not show the benefits of local steps. In addition, Levy (2023) proposed a new local update method that provably benefits over mini-batch SGD. However, in the same setting, there is still no work analyzing the effects of local steps to generalization in a heterogeneous FL setting. Motivated by our experimental findings where Local SGD learns more distinguishing features than parallel SGD, this paper studies the generalization benefits of local steps from a feature learning perspective. We propose a novel federated data model that exhibits a new form of data heterogeneity, under which we show that a convolutional neural network (CNN) trained by GD with global updates will miss some pattern-related features, while the network trained by GD with local updates can learn all features in polynomial time. Consequently, local steps help CNN generalize better in our data model. In a different parameter setting, we also prove that Local GD with one-shot model averaging can learn all features and generalize well in all clients. Our experimental results also confirm the benefits of local steps in improving test accuracy on real-world data.