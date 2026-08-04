---
title: "Differentially Private Bias-Term Fine-tuning of Foundation Models"
source: "https://proceedings.mlr.press/v235/bu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bu24c/bu24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['differential-privacy', 'fine-tuning', 'foundation-models', 'bias-term']
venue: "ICML 2024"
tldr: "Studies differentially private bias-term-only fine-tuning of large pretrained models, achieving high accuracy under strong privacy constraints with low computational cost."
---

# Differentially Private Bias-Term Fine-tuning of Foundation Models

**Source**: [https://proceedings.mlr.press/v235/bu24c.html](https://proceedings.mlr.press/v235/bu24c.html)

**TLDR**: Studies differentially private bias-term-only fine-tuning of large pretrained models, achieving high accuracy under strong privacy constraints with low computational cost.

## Abstract

We study the problem of differentially private (DP) fine-tuning of large pre-trained models — a recent privacy-preserving approach suitable for solving downstream tasks with sensitive data. Existing work has demonstrated that high accuracy is possible under strong privacy constraint, yet requires significant computational overhead or modifications to the network architecture. We propose differentially private bias-term fine-tuning (DP-BiTFiT), which matches the state-of-the-art accuracy for DP algorithms and the efficiency of the standard BiTFiT. DP-BiTFiT is model agnostic (not modifying the network architecture), parameter efficient (only training about 0.1% of the parameters), and computation efficient (almost removing the overhead caused by DP, in both the time and space complexity). On a wide range of tasks, DP-BiTFiT is 2 - 30X faster and uses 2 - 8X less memory than DP full fine-tuning, even faster than the standard full fine-tuning. This amazing efficiency enables us to conduct DP fine-tuning on language and vision tasks with long-sequence texts and high-resolution images, which were computationally difficult using existing methods.