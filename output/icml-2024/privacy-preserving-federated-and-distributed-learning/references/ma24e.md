---
title: "Beyond the Federation: Topology-aware Federated Learning for Generalization to Unseen Clients"
source: "https://proceedings.mlr.press/v235/ma24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24e/ma24e.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['federated-learning', 'topology-awareness', 'out-of-federation-generalization', 'data-heterogeneity']
venue: "ICML 2024"
tldr: "A topology-aware federated learning method improves generalization to unseen out-of-federation clients beyond in-federation data heterogeneity."
---

# Beyond the Federation: Topology-aware Federated Learning for Generalization to Unseen Clients

**Source**: [https://proceedings.mlr.press/v235/ma24e.html](https://proceedings.mlr.press/v235/ma24e.html)

**TLDR**: A topology-aware federated learning method improves generalization to unseen out-of-federation clients beyond in-federation data heterogeneity.

## Abstract

Federated Learning is widely employed to tackle distributed sensitive data. Existing methods primarily focus on addressing in-federation data heterogeneity. However, we observed that they suffer from significant performance degradation when applied to unseen clients for out-of-federation (OOF) generalization. The recent attempts to address generalization to unseen clients generally struggle to scale up to large-scale distributed settings due to high communication or computation costs. Moreover, methods that scale well often demonstrate poor generalization capability. To achieve OOF-resiliency in a scalable manner, we propose Topology-aware Federated Learning (TFL) that leverages client topology - a graph representing client relationships - to effectively train robust models against OOF data. We formulate a novel optimization problem for TFL, consisting of two key modules: Client Topology Learning, which infers the client relationships in a privacy-preserving manner, and Learning on Client Topology, which leverages the learned topology to identify influential clients and harness this information into the FL optimization process to efficiently build robust models. Empirical evaluation on a variety of real-world datasets verifies TFL’s superior OOF robustness and scalability.