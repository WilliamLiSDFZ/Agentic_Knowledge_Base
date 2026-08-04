---
title: "Differentially Private Representation Learning via Image Captioning"
source: "https://proceedings.mlr.press/v235/sander24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sander24b/sander24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['differential-privacy', 'representation-learning', 'image-captioning', 'privacy-accuracy-tradeoff', 'synthetic-data']
venue: "ICML 2024"
tldr: "Differentially private representation learning is improved by leveraging image captioning to generate privacy-preserving synthetic pretraining data."
---

# Differentially Private Representation Learning via Image Captioning

**Source**: [https://proceedings.mlr.press/v235/sander24b.html](https://proceedings.mlr.press/v235/sander24b.html)

**TLDR**: Differentially private representation learning is improved by leveraging image captioning to generate privacy-preserving synthetic pretraining data.

## Abstract

Differentially private (DP) machine learning is considered the gold-standard solution for training a model from sensitive data while still preserving privacy. However, a major barrier to achieving this ideal is its sub-optimal privacy-accuracy trade-off, which is particularly visible in DP representation learning. Specifically, it has been shown that under modest privacy budgets, most models learn representations that are not significantly better than hand-crafted features. In this work, we show that effective DP representation learning can be done via image captioning and scaling up to internet-scale multimodal datasets. Through a series of engineering tricks, we successfully train a DP image captioner (DP-Cap) on a 233M subset of LAION-2B from scratch using a reasonable amount of computation, and obtaining unprecedented high-quality image features that can be used in a variety of downstream vision and vision-language tasks. For example, under a privacy budget of $\varepsilon=8$ for the LAION dataset, a linear classifier trained on top of learned DP-Cap features attains $65.8%$ accuracy on ImageNet-1K, considerably improving the previous SOTA of $56.5%$. Our work challenges the prevailing sentiment that high-utility DP representation learning cannot be achieved by training from scratch.