---
title: "FedMBridge: Bridgeable Multimodal Federated Learning"
source: "https://proceedings.mlr.press/v235/chen24ba.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ba/chen24ba.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['multimodal-federated-learning', 'heterogeneous-modalities', 'bridgeable-architecture', 'personalization']
venue: "ICML 2024"
tldr: "Proposes FedMBridge, a flexible multimodal federated learning framework supporting diverse client modality types via bridgeable neural architectures."
---

# FedMBridge: Bridgeable Multimodal Federated Learning

**Source**: [https://proceedings.mlr.press/v235/chen24ba.html](https://proceedings.mlr.press/v235/chen24ba.html)

**TLDR**: Proposes FedMBridge, a flexible multimodal federated learning framework supporting diverse client modality types via bridgeable neural architectures.

## Abstract

Multimodal Federated Learning (MFL) addresses the setup of multiple clients with diversified modality types (e.g. image, text, video, and audio) working together to improve their local personal models in a data-privacy manner. Prior MFL works rely on restrictive compositional neural architecture designs to ensure inter-client information sharing via blockwise model aggregation, limiting their applicability in the real-world Architecture-personalized MFL (AMFL) scenarios, where clients may have distinguished multimodal interaction strategies and there is no restriction on local architecture design. The key challenge in AMFL is how to automatically and efficiently tackle the two heterogeneity patterns–statistical and architecture heterogeneity–while maximizing the beneficial information sharing among clients. To solve this challenge, we propose FedMBridge, which leverages a topology-aware hypernetwork to act as a bridge that can automatically balance and digest the two heterogeneity patterns in a communication-efficient manner. Our experiments on four AMFL simulations demonstrate the efficiency and effectiveness of our proposed approach.