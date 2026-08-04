---
title: "Federated Self-Explaining GNNs with Anti-shortcut Augmentations"
source: "https://proceedings.mlr.press/v235/yue24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yue24b/yue24b.pdf"
categories: ['graph-neural-networks-and-topology', 'privacy-preserving-federated-and-distributed-learning']
tags: ['graph-neural-networks', 'federated-learning', 'explainability', 'shortcut-mitigation']
venue: "ICML 2024"
tldr: "A federated self-explaining GNN framework with anti-shortcut augmentations for privacy-preserving graph rationalization."
---

# Federated Self-Explaining GNNs with Anti-shortcut Augmentations

**Source**: [https://proceedings.mlr.press/v235/yue24b.html](https://proceedings.mlr.press/v235/yue24b.html)

**TLDR**: A federated self-explaining GNN framework with anti-shortcut augmentations for privacy-preserving graph rationalization.

## Abstract

Graph Neural Networks (GNNs) have demonstrated remarkable performance in graph classification tasks. However, ensuring the explainability of their predictions remains a challenge. To address this, graph rationalization methods have been introduced to generate concise subsets of the original graph, known as rationales, which serve to explain the predictions made by GNNs. Existing rationalizations often rely on shortcuts in data for prediction and rationale composition. In response, de-shortcut rationalization methods have been proposed, which commonly leverage counterfactual augmentation to enhance data diversity for mitigating the shortcut problem. Nevertheless, these methods have predominantly focused on centralized datasets and have not been extensively explored in the Federated Learning (FL) scenarios. To this end, in this paper, we propose a Federated Graph Rationalization (FedGR) with anti-shortcut augmentations to achieve self-explaining GNNs, which involves two data augmenters. These augmenters are employed to produce client-specific shortcut conflicted samples at each client, which contributes to mitigating the shortcut problem under the FL scenarios. Experiments on real-world benchmarks and synthetic datasets validate the effectiveness of FedGR under the FL scenarios.