---
title: "Neural Collapse meets Differential Privacy: Curious behaviors of NoisyGD with Near-Perfect Representation Learning"
source: "https://proceedings.mlr.press/v235/wang24cu.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cu/wang24cu.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['differential-privacy', 'neural-collapse', 'representation-learning']
venue: "ICML 2024"
tldr: "This paper analyzes curious behaviors of differentially private learning with near-perfect representations through the lens of neural collapse theory."
---

# Neural Collapse meets Differential Privacy: Curious behaviors of NoisyGD with Near-Perfect Representation Learning

**Source**: [https://proceedings.mlr.press/v235/wang24cu.html](https://proceedings.mlr.press/v235/wang24cu.html)

**TLDR**: This paper analyzes curious behaviors of differentially private learning with near-perfect representations through the lens of neural collapse theory.

## Abstract

A recent study by De et al. (2022) shows that large-scale representation learning through pre-training on a public dataset significantly enhances differentially private (DP) learning in downstream tasks. To explain this, we consider a layer-peeled model in representation learning, resulting in Neural Collapse (NC) phenomena. Within NC, we establish that the misclassification error is independent of dimension when the distance between actual and ideal features is below a threshold. We empirically evaluate feature quality in the last layer under different pre-trained models, showing that a more powerful pre-trained model improves feature representation. Moreover, we show that DP fine-tuning is less robust compared to non-DP fine-tuning, especially with perturbations. Supported by theoretical analyses and experiments, we suggest strategies like feature normalization and dimension reduction methods such as PCA to enhance DP fine-tuning robustness. Conducting PCA on last-layer features significantly improves testing accuracy.