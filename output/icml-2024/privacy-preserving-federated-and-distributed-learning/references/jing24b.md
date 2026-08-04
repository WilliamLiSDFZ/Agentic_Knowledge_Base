---
title: "FedSC: Provable Federated Self-supervised Learning with Spectral Contrastive Objective over Non-i.i.d. Data"
source: "https://proceedings.mlr.press/v235/jing24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jing24b/jing24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['federated-learning', 'self-supervised-learning', 'spectral-contrastive', 'non-iid']
venue: "ICML 2024"
tldr: "FedSC provides provable convergence guarantees for federated self-supervised learning with a spectral contrastive objective under non-i.i.d. data distributions."
---

# FedSC: Provable Federated Self-supervised Learning with Spectral Contrastive Objective over Non-i.i.d. Data

**Source**: [https://proceedings.mlr.press/v235/jing24b.html](https://proceedings.mlr.press/v235/jing24b.html)

**TLDR**: FedSC provides provable convergence guarantees for federated self-supervised learning with a spectral contrastive objective under non-i.i.d. data distributions.

## Abstract

Recent efforts have been made to integrate self-supervised learning (SSL) with the framework of federated learning (FL). One unique challenge of federated self-supervised learning (FedSSL) is that the global objective of FedSSL usually does not equal the weighted sum of local SSL objectives. Consequently, conventional approaches, such as federated averaging (FedAvg), fail to precisely minimize the FedSSL global objective, often resulting in suboptimal performance, especially when data is non-i.i.d.. To fill this gap, we propose a provable FedSSL algorithm, named FedSC, based on the spectral contrastive objective. In FedSC, clients share correlation matrices of data representations in addition to model weights periodically, which enables inter-client contrast of data samples in addition to intra-client contrast and contraction, resulting in improved quality of data representations. Differential privacy (DP) protection is deployed to control the additional privacy leakage on local datasets when correlation matrices are shared. We provide theoretical analysis on convergence and extra privacy leakage, and conduct numerical experiments to justify the effectiveness of our proposed algorithm.