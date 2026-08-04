---
title: "REMEDI: Corrective Transformations for Improved Neural Entropy Estimation"
source: "https://proceedings.mlr.press/v235/nilsson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nilsson24a/nilsson24a.pdf"
categories: ['generative-models-and-variational-inference', 'llm-geometry-and-interpretability-research']
tags: ['entropy-estimation', 'mutual-information', 'neural-estimators']
venue: "ICML 2024"
tldr: "Introduces corrective transformations to improve neural entropy and mutual information estimation in high-dimensional settings."
---

# REMEDI: Corrective Transformations for Improved Neural Entropy Estimation

**Source**: [https://proceedings.mlr.press/v235/nilsson24a.html](https://proceedings.mlr.press/v235/nilsson24a.html)

**TLDR**: Introduces corrective transformations to improve neural entropy and mutual information estimation in high-dimensional settings.

## Abstract

Information theoretic quantities play a central role in machine learning. The recent surge in the complexity of data and models has increased the demand for accurate estimation of these quantities. However, as the dimension grows the estimation presents significant challenges, with existing methods struggling already in relatively low dimensions. To address this issue, in this work, we introduce REMEDI for efficient and accurate estimation of differential entropy, a fundamental information theoretic quantity. The approach combines the minimization of the cross-entropy for simple, adaptive base models and the estimation of their deviation, in terms of the relative entropy, from the data density. Our approach demonstrates improvement across a broad spectrum of estimation tasks, encompassing entropy estimation on both synthetic and natural data. Further, we extend important theoretical consistency results to a more generalized setting required by our approach. We illustrate how the framework can be naturally extended to information theoretic supervised learning models, with a specific focus on the Information Bottleneck approach. It is demonstrated that the method delivers better accuracy compared to the existing methods in Information Bottleneck. In addition, we explore a natural connection between REMEDI and generative modeling using rejection sampling and Langevin dynamics.