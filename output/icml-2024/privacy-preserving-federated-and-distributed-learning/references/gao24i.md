---
title: "Private Heterogeneous Federated Learning Without a Trusted Server Revisited: Error-Optimal and Communication-Efficient Algorithms for Convex Losses"
source: "https://proceedings.mlr.press/v235/gao24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24i/gao24i.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'differential-privacy', 'communication-efficiency', 'convex-optimization']
venue: "ICML 2024"
tldr: "This paper presents error-optimal and communication-efficient federated learning algorithms under local differential privacy without a trusted server."
---

# Private Heterogeneous Federated Learning Without a Trusted Server Revisited: Error-Optimal and Communication-Efficient Algorithms for Convex Losses

**Source**: [https://proceedings.mlr.press/v235/gao24i.html](https://proceedings.mlr.press/v235/gao24i.html)

**TLDR**: This paper presents error-optimal and communication-efficient federated learning algorithms under local differential privacy without a trusted server.

## Abstract

We revisit the problem of federated learning (FL) with private data from people who do not trust the server or other silos/clients. In this context, every silo (e.g. hospital) has data from several people (e.g. patients) and needs to protect the privacy of each person’s data (e.g. health records), even if the server and/or other silos try to uncover this data. Inter-Silo Record-Level Differential Privacy (ISRL-DP) prevents each silo’s data from being leaked, by requiring that silo $i$’s communications satisfy item-level differential privacy. Prior work (Lowy & Razaviyayn, 2023a) characterized the optimal excess risk bounds for ISRL-DP algorithms with homogeneous (i.i.d.) silo data and convex loss functions. However, two important questions were left open: 1) Can the same excess risk bounds be achieved with heterogeneous (non-i.i.d.) silo data? 2) Can the optimal risk bounds be achieved with fewer communication rounds? In this paper, we give positive answers to both questions. We provide novel ISRL-DP FL algorithms that achieve the optimal excess risk bounds in the presence of heterogeneous silo data. Moreover, our algorithms are more communication-efficient than the prior state-of-the-art. For smooth loss functions, our algorithm achieves the optimal excess risk bound and has communication complexity that matches the non-private lower bound. Additionally, our algorithms are more computationally efficient than the previous state-of-the-art.