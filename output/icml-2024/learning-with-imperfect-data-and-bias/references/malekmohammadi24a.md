---
title: "Noise-Aware Algorithm for Heterogeneous Differentially Private Federated Learning"
source: "https://proceedings.mlr.press/v235/malekmohammadi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/malekmohammadi24a/malekmohammadi24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['federated-learning', 'differential-privacy', 'heterogeneous-clients']
venue: "ICML 2024"
tldr: "A noise-aware algorithm for federated learning that handles heterogeneous differential privacy requirements across clients while maintaining high utility."
---

# Noise-Aware Algorithm for Heterogeneous Differentially Private Federated Learning

**Source**: [https://proceedings.mlr.press/v235/malekmohammadi24a.html](https://proceedings.mlr.press/v235/malekmohammadi24a.html)

**TLDR**: A noise-aware algorithm for federated learning that handles heterogeneous differential privacy requirements across clients while maintaining high utility.

## Abstract

High utility and rigorous data privacy are of the main goals of a federated learning (FL) system, which learns a model from the data distributed among some clients. The latter has been tried to achieve by using differential privacy in FL (DPFL). There is often heterogeneity in clients’ privacy requirements, and existing DPFL works either assume uniform privacy requirements for clients or are not applicable when server is not fully trusted (our setting). Furthermore, there is often heterogeneity in batch and/or dataset size of clients, which as shown, results in extra variation in the DP noise level across clients’ model updates. With these sources of heterogeneity, straightforward aggregation strategies, e.g., assigning clients’ aggregation weights proportional to their privacy parameters ($\epsilon$) will lead to lower utility. We propose Robust-HDP, which efficiently estimates the true noise level in clients’ model updates and reduces the noise-level in the aggregated model updates considerably. Robust-HDP improves utility and convergence speed, while being safe to the clients that may maliciously send falsified privacy parameter $\epsilon$ to server. Extensive experimental results on multiple datasets and our theoretical analysis confirm the effectiveness of Robust-HDP. Our code can be found here: https://github.com/Saber-mm/HDPFL.git