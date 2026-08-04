---
title: "Benign Overfitting in Adversarial Training of Neural Networks"
source: "https://proceedings.mlr.press/v235/wang24cn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cn/wang24cn.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['benign-overfitting', 'adversarial-training', 'neural-networks']
venue: "ICML 2024"
tldr: "This paper studies benign overfitting in adversarial training, showing interpolating models can generalize well even under adversarial conditions."
---

# Benign Overfitting in Adversarial Training of Neural Networks

**Source**: [https://proceedings.mlr.press/v235/wang24cn.html](https://proceedings.mlr.press/v235/wang24cn.html)

**TLDR**: This paper studies benign overfitting in adversarial training, showing interpolating models can generalize well even under adversarial conditions.

## Abstract

Benign overfitting is the phenomenon wherein none of the predictors in the hypothesis class can achieve perfect accuracy (i.e., non-realizable or noisy setting), but a model that interpolates the training data still achieves good generalization. A series of recent works aim to understand this phenomenon for regression and classification tasks using linear predictors as well as two-layer neural networks. In this paper, we study such a benign overfitting phenomenon in an adversarial setting. We show that under a distributional assumption, interpolating neural networks found using adversarial training generalize well despite inference-time attacks. Specifically, we provide convergence and generalization guarantees for adversarial training of two-layer networks (with smooth as well as non-smooth activation functions) showing that under moderate $\ell_2$ norm perturbation budget, the trained model has near-zero robust training loss and near-optimal robust generalization error. We support our theoretical findings with an empirical study on synthetic and real-world data.