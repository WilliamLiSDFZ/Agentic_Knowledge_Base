---
title: "Bounding the Excess Risk for Linear Models Trained on Marginal-Preserving, Differentially-Private, Synthetic Data"
source: "https://proceedings.mlr.press/v235/zhou24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24k/zhou24k.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'synthetic-data', 'excess-risk-bounds']
venue: "ICML 2024"
tldr: "Derives excess risk bounds for linear models trained on marginal-preserving differentially private synthetic data, quantifying the privacy-utility tradeoff."
---

# Bounding the Excess Risk for Linear Models Trained on Marginal-Preserving, Differentially-Private, Synthetic Data

**Source**: [https://proceedings.mlr.press/v235/zhou24k.html](https://proceedings.mlr.press/v235/zhou24k.html)

**TLDR**: Derives excess risk bounds for linear models trained on marginal-preserving differentially private synthetic data, quantifying the privacy-utility tradeoff.

## Abstract

The growing use of machine learning (ML) has raised concerns that an ML model may reveal private information about an individual who has contributed to the training dataset. To prevent leakage of sensitive data, we consider using differentially- private (DP), synthetic training data instead of real training data to train an ML model. A key desirable property of synthetic data is its ability to preserve the low-order marginals of the original distribution. Our main contribution comprises novel upper and lower bounds on the excess empirical risk of linear models trained on such synthetic data, for continuous and Lipschitz loss functions. We perform extensive experimentation alongside our theoretical results.