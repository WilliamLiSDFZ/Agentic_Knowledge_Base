---
title: "Adaptive Group Personalization for Federated Mutual Transfer Learning"
source: "https://proceedings.mlr.press/v235/xu24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24u/xu24u.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'personalization', 'mutual-transfer-learning']
venue: "ICML 2024"
tldr: "An adaptive group personalization method for federated mutual transfer learning is proposed with theoretical guarantees on learnability across heterogeneous clients."
---

# Adaptive Group Personalization for Federated Mutual Transfer Learning

**Source**: [https://proceedings.mlr.press/v235/xu24u.html](https://proceedings.mlr.press/v235/xu24u.html)

**TLDR**: An adaptive group personalization method for federated mutual transfer learning is proposed with theoretical guarantees on learnability across heterogeneous clients.

## Abstract

Mutual transfer learning aims to improve prediction with knowledge from related domains. Recently, federated learning is applied in this field to address the communication and privacy concerns. However, previous clustered federated learning (CFL) solutions lack theoretical guarantee of learnability recovery and require time-consuming hyper-parameter tuning, while centralized mutual transfer learning methods lack adaptability to concept drifts. In this paper, we propose the Adaptive Group Personalization method (AdaGrP) to overcome these challenges. We adaptively decide the recovery threshold with a nonparametric method, adaptive threshold correction, for tuning-free solution with relaxed condition. Theoretical results guarantee the perfect learnability recovery with the corrected threshold. Empirical results show AdaGrP achieves 16.9% average improvement in learnability structure recovery compared with state-of-the-art CFL baselines.