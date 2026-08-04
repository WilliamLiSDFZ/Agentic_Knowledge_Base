---
title: "DataFreeShield: Defending Adversarial Attacks without Training Data"
source: "https://proceedings.mlr.press/v235/lee24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24f/lee24f.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['adversarial-robustness', 'data-free-defense', 'knowledge-distillation', 'pretrained-models']
venue: "ICML 2024"
tldr: "Proposes DataFreeShield, a method to defend against adversarial attacks without requiring access to original training data."
---

# DataFreeShield: Defending Adversarial Attacks without Training Data

**Source**: [https://proceedings.mlr.press/v235/lee24f.html](https://proceedings.mlr.press/v235/lee24f.html)

**TLDR**: Proposes DataFreeShield, a method to defend against adversarial attacks without requiring access to original training data.

## Abstract

Recent advances in adversarial robustness rely on an abundant set of training data, where using external or additional datasets has become a common setting. However, in real life, the training data is often kept private for security and privacy issues, while only the pretrained weight is available to the public. In such scenarios, existing methods that assume accessibility to the original data become inapplicable. Thus we investigate the pivotal problem of data-free adversarial robustness, where we try to achieve adversarial robustness without accessing any real data. Through a preliminary study, we highlight the severity of the problem by showing that robustness without the original dataset is difficult to achieve, even with similar domain datasets. To address this issue, we propose DataFreeShield, which tackles the problem from two perspectives: surrogate dataset generation and adversarial training using the generated data. Through extensive validation, we show that DataFreeShield outperforms baselines, demonstrating that the proposed method sets the first entirely data-free solution for the adversarial robustness problem.