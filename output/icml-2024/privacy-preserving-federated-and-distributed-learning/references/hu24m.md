---
title: "Provable Privacy with Non-Private Pre-Processing"
source: "https://proceedings.mlr.press/v235/hu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24m/hu24m.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'privacy-accounting', 'data-preprocessing']
venue: "ICML 2024"
tldr: "Proposes a framework to quantify the privacy cost of non-private data-dependent preprocessing steps in differentially private ML pipelines."
---

# Provable Privacy with Non-Private Pre-Processing

**Source**: [https://proceedings.mlr.press/v235/hu24m.html](https://proceedings.mlr.press/v235/hu24m.html)

**TLDR**: Proposes a framework to quantify the privacy cost of non-private data-dependent preprocessing steps in differentially private ML pipelines.

## Abstract

When analyzing Differentially Private (DP) machine learning pipelines, the potential privacy cost of data-dependent pre-processing is frequently overlooked in privacy accounting. In this work, we propose a general framework to evaluate the additional privacy cost incurred by non-private data-dependent pre-processing algorithms. Our framework establishes upper bounds on the overall privacy guarantees by utilising two new technical notions: a variant of DP termed Smooth DP and the bounded sensitivity of the pre-processing algorithms. In addition to the generic framework, we provide explicit overall privacy guarantees for multiple data-dependent pre-processing algorithms, such as data imputation, quantization, deduplication, standard scaling and PCA, when used in combination with several DP algorithms. Notably, this framework is also simple to implement, allowing direct integration into existing DP pipelines.