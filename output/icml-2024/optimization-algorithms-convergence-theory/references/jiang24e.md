---
title: "Federated Optimization with Doubly Regularized Drift Correction"
source: "https://proceedings.mlr.press/v235/jiang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24e/jiang24e.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'client-drift', 'doubly-regularized', 'distributed-optimization']
venue: "ICML 2024"
tldr: "A doubly regularized drift correction method is proposed to mitigate client drift in federated optimization and improve convergence over FedAvg."
---

# Federated Optimization with Doubly Regularized Drift Correction

**Source**: [https://proceedings.mlr.press/v235/jiang24e.html](https://proceedings.mlr.press/v235/jiang24e.html)

**TLDR**: A doubly regularized drift correction method is proposed to mitigate client drift in federated optimization and improve convergence over FedAvg.

## Abstract

Federated learning is a distributed optimization paradigm that allows training machine learning models across decentralized devices while keeping the data localized. The standard method, FedAvg, suffers from client drift which can hamper performance and increase communication costs over centralized methods. Previous works proposed various strategies to mitigate drift, yet none have shown consistently improved communication-computation trade-offs over vanilla gradient descent across all standard function classes. In this work, we revisit DANE, an established method in distributed optimization. We show that (i) DANE can achieve the desired communication reduction under Hessian similarity constraints. Furthermore, (ii) we present an extension, DANE+, which supports arbitrary inexact local solvers and has more freedom to choose how to aggregate the local updates. We propose (iii) a novel method, FedRed, which has improved local computational complexity and retains the same communication complexity compared to DANE/DANE+. This is achieved by doubly regularized drift correction.