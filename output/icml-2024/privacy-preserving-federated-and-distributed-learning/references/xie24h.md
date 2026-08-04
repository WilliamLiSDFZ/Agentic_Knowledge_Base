---
title: "MH-pFLID: Model Heterogeneous personalized Federated Learning via Injection and Distillation for Medical Data Analysis"
source: "https://proceedings.mlr.press/v235/xie24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24h/xie24h.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'knowledge-distillation-methods-and-applications']
tags: ['federated-learning', 'model-heterogeneity', 'knowledge-distillation']
venue: "ICML 2024"
tldr: "MH-pFLID addresses model heterogeneity in personalized federated learning for medical data via injection and distillation techniques."
---

# MH-pFLID: Model Heterogeneous personalized Federated Learning via Injection and Distillation for Medical Data Analysis

**Source**: [https://proceedings.mlr.press/v235/xie24h.html](https://proceedings.mlr.press/v235/xie24h.html)

**TLDR**: MH-pFLID addresses model heterogeneity in personalized federated learning for medical data via injection and distillation techniques.

## Abstract

Federated learning is widely used in medical applications for training global models without needing local data access, but varying computational capabilities and network architectures (system heterogeneity) across clients pose significant challenges in effectively aggregating information from non-independently and identically distributed (non-IID) data (statistic heterogeneity). Current federated learning methods using knowledge distillation require public datasets, raising privacy and data collection issues. Additionally, these datasets require additional local computing and storage resources, which is a burden for medical institutions with limited hardware conditions. In this paper, we introduce a novel federated learning paradigm, named Model Heterogeneous personalized Federated Learning via Injection and Distillation (MH-pFLID). Our framework leverages a lightweight messenger model, eliminating the need for public datasets and reducing the training cost for each client. We also develops receiver and transmitter modules for each client to separate local biases from generalizable information, reducing biased data collection and mitigating client drift. Our experiments on various medical tasks including image classification, image segmentation, and time-series classification, show MH-pFLID outperforms state-of-the-art methods in all these areas and has good generalizability.