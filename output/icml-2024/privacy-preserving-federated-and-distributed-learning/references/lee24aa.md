---
title: "Rethinking the Flat Minima Searching in Federated Learning"
source: "https://proceedings.mlr.press/v235/lee24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24aa/lee24aa.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'flat-minima', 'sharpness-aware-minimization', 'generalization']
venue: "ICML 2024"
tldr: "Rethinks and improves flat minima searching in federated learning to enhance generalization under client heterogeneity."
---

# Rethinking the Flat Minima Searching in Federated Learning

**Source**: [https://proceedings.mlr.press/v235/lee24aa.html](https://proceedings.mlr.press/v235/lee24aa.html)

**TLDR**: Rethinks and improves flat minima searching in federated learning to enhance generalization under client heterogeneity.

## Abstract

Albeit the success of federated learning (FL) in decentralized training, bolstering the generalization of models by overcoming heterogeneity across clients still remains a huge challenge. To aim at improved generalization of FL, a group of recent works pursues flatter minima of models by employing sharpness-aware minimization in the local training at the client side. However, we observe that the global model, i.e., the aggregated model, does not lie on flat minima of the global objective, even with the effort of flatness searching in local training, which we define as flatness discrepancy. By rethinking and theoretically analyzing flatness searching in FL through the lens of the discrepancy problem, we propose a method called Federated Learning for Global Flatness (FedGF) that explicitly pursues the flatter minima of the global models, leading to the relieved flatness discrepancy and remarkable performance gains in the heterogeneous FL benchmarks.