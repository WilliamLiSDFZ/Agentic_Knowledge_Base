---
title: "Bridging Model Heterogeneity in Federated Learning via Uncertainty-based Asymmetrical Reciprocity Learning"
source: "https://proceedings.mlr.press/v235/wang24cs.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cs/wang24cs.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'model-heterogeneity', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "FedType uses small proxy models with uncertainty-based asymmetrical reciprocity to bridge model heterogeneity in federated learning."
---

# Bridging Model Heterogeneity in Federated Learning via Uncertainty-based Asymmetrical Reciprocity Learning

**Source**: [https://proceedings.mlr.press/v235/wang24cs.html](https://proceedings.mlr.press/v235/wang24cs.html)

**TLDR**: FedType uses small proxy models with uncertainty-based asymmetrical reciprocity to bridge model heterogeneity in federated learning.

## Abstract

This paper presents FedType, a simple yet pioneering framework designed to fill research gaps in heterogeneous model aggregation within federated learning (FL). FedType introduces small identical proxy models for clients, serving as agents for information exchange, ensuring model security, and achieving efficient communication simultaneously. To transfer knowledge between large private and small proxy models on clients, we propose a novel uncertainty-based asymmetrical reciprocity learning method, eliminating the need for any public data. Comprehensive experiments conducted on benchmark datasets demonstrate the efficacy and generalization ability of FedType across diverse settings. Our approach redefines federated learning paradigms by bridging model heterogeneity, eliminating reliance on public data, prioritizing client privacy, and reducing communication costs (The codes are available in the supplementation materials).