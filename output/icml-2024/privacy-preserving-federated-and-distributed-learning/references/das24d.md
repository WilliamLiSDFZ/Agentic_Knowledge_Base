---
title: "Disparate Impact on Group Accuracy of Linearization for Private Inference"
source: "https://proceedings.mlr.press/v235/das24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/das24d/das24d.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['private-inference', 'linearization', 'disparate-impact', 'fairness', 'cryptographic-inference']
venue: "ICML 2024"
tldr: "Reveals that linearizing neural network activations for private inference causes disparate accuracy impacts across demographic groups, raising fairness concerns."
---

# Disparate Impact on Group Accuracy of Linearization for Private Inference

**Source**: [https://proceedings.mlr.press/v235/das24d.html](https://proceedings.mlr.press/v235/das24d.html)

**TLDR**: Reveals that linearizing neural network activations for private inference causes disparate accuracy impacts across demographic groups, raising fairness concerns.

## Abstract

Ensuring privacy-preserving inference on cryptographically secure data is a well-known computational challenge. To alleviate the bottleneck of costly cryptographic computations in non-linear activations, recent methods have suggested linearizing a targeted portion of these activations in neural networks. This technique results in significantly reduced runtimes with often negligible impacts on accuracy. In this paper, we demonstrate that such computational benefits may lead to increased fairness costs. Specifically, we find that reducing the number of ReLU activations disproportionately decreases the accuracy for minority groups compared to majority groups. To explain these observations, we provide a mathematical interpretation under restricted assumptions about the nature of the decision boundary, while also showing the prevalence of this problem across widely used datasets and architectures. Finally, we show how a simple procedure altering the finetuning step for linearized models can serve as an effective mitigation strategy.