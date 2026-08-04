---
title: "Recurrent Early Exits for Federated Learning with Heterogeneous Clients"
source: "https://proceedings.mlr.press/v235/lee24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24h/lee24h.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['federated-learning', 'early-exit', 'heterogeneous-clients', 'recurrent-networks']
venue: "ICML 2024"
tldr: "Proposes recurrent early exit networks for federated learning to accommodate clients with heterogeneous hardware capacities."
---

# Recurrent Early Exits for Federated Learning with Heterogeneous Clients

**Source**: [https://proceedings.mlr.press/v235/lee24h.html](https://proceedings.mlr.press/v235/lee24h.html)

**TLDR**: Proposes recurrent early exit networks for federated learning to accommodate clients with heterogeneous hardware capacities.

## Abstract

Federated learning (FL) has enabled distributed learning of a model across multiple clients in a privacy-preserving manner. One of the main challenges of FL is to accommodate clients with varying hardware capacities; clients have differing compute and memory requirements. To tackle this challenge, recent state-of-the-art approaches leverage the use of early exits. Nonetheless, these approaches fall short of mitigating the challenges of joint learning multiple exit classifiers, often relying on hand-picked heuristic solutions for knowledge distillation among classifiers and/or utilizing additional layers for weaker classifiers. In this work, instead of utilizing multiple classifiers, we propose a recurrent early exit approach named ReeFL that fuses features from different sub-models into a single shared classifier. Specifically, we use a transformer-based early-exit module shared among sub-models to i) better exploit multi-layer feature representations for task-specific prediction and ii) modulate the feature representation of the backbone model for subsequent predictions. We additionally present a per-client self-distillation approach where the best sub-model is automatically selected as the teacher of the other sub-models at each client. Our experiments on standard image and speech classification benchmarks across various emerging federated fine-tuning baselines demonstrate ReeFL effectiveness over previous works.