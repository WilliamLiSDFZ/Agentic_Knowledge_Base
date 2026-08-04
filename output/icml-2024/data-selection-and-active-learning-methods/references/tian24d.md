---
title: "Ranking-based Client Imitation Selection for Efficient Federated Learning"
source: "https://proceedings.mlr.press/v235/tian24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tian24d/tian24d.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'data-selection-and-active-learning-methods']
tags: ['federated-learning', 'client-selection', 'heterogeneous-devices']
venue: "ICML 2024"
tldr: "A ranking-based client imitation selection strategy improves federated learning efficiency by selecting representative participating devices under data and system heterogeneity."
---

# Ranking-based Client Imitation Selection for Efficient Federated Learning

**Source**: [https://proceedings.mlr.press/v235/tian24d.html](https://proceedings.mlr.press/v235/tian24d.html)

**TLDR**: A ranking-based client imitation selection strategy improves federated learning efficiency by selecting representative participating devices under data and system heterogeneity.

## Abstract

Federated Learning (FL) enables multiple devices to collaboratively train a shared model while ensuring data privacy. The selection of participating devices in each training round critically affects both the model performance and training efficiency, especially given the vast heterogeneity in training capabilities and data distribution across devices. To deal with these challenges, we introduce a novel device selection solution called FedRank, which is based on an end-to-end, ranking-based model that is pre-trained by imitation learning against state-of-the-art analytical approaches. It not only considers data and system heterogeneity at runtime but also adaptively and efficiently chooses the most suitable clients for model training. Specifically, FedRank views client selection in FL as a ranking problem and employs a pairwise training strategy for the smart selection process. Additionally, an imitation learning-based approach is designed to counteract the cold-start issues often seen in state-of-the-art learning-based approaches. Experimental results reveal that FedRank boosts model accuracy by 5.2% to 56.9%, accelerates the training convergence up to $2.01 \times$ and saves the energy consumption up to 40.1%.