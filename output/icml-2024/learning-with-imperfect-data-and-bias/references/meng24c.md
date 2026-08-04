---
title: "Benign Overfitting in Two-Layer ReLU Convolutional Neural Networks for XOR Data"
source: "https://proceedings.mlr.press/v235/meng24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/meng24c/meng24c.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['benign-overfitting', 'overparameterization', 'generalization']
venue: "ICML 2024"
tldr: "Theoretically analyzes the benign overfitting phenomenon in two-layer ReLU convolutional neural networks trained on XOR-structured data."
---

# Benign Overfitting in Two-Layer ReLU Convolutional Neural Networks for XOR Data

**Source**: [https://proceedings.mlr.press/v235/meng24c.html](https://proceedings.mlr.press/v235/meng24c.html)

**TLDR**: Theoretically analyzes the benign overfitting phenomenon in two-layer ReLU convolutional neural networks trained on XOR-structured data.

## Abstract

Modern deep learning models are usually highly over-parameterized so that they can overfit the training data. Surprisingly, such overfitting neural networks can usually still achieve high prediction accuracy. To study this “benign overfitting” phenomenon, a line of recent works has theoretically studied the learning of linear models and two-layer neural networks. However, most of these analyses are still limited to the very simple learning problems where the Bayes-optimal classifier is linear. In this work, we investigate a class of XOR-type classification tasks with label-flipping noises. We show that, under a certain condition on the sample complexity and signal-to-noise ratio, an over-parameterized ReLU CNN trained by gradient descent can achieve near Bayes-optimal accuracy. Moreover, we also establish a matching lower bound result showing that when the previous condition is not satisfied, the prediction accuracy of the obtained CNN is an absolute constant away from the Bayes-optimal rate. Our result demonstrates that CNNs have a remarkable capacity to efficiently learn XOR problems, even in the presence of highly correlated features.