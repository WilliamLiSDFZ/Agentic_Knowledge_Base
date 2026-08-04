---
title: "FedLMT: Tackling System Heterogeneity of Federated Learning via Low-Rank Model Training with Theoretical Guarantees"
source: "https://proceedings.mlr.press/v235/liu24ch.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ch/liu24ch.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['federated-learning', 'system-heterogeneity', 'low-rank-training', 'model-compression', 'theoretical-guarantees']
venue: "ICML 2024"
tldr: "FedLMT addresses system heterogeneity in federated learning via low-rank model training that enables resource-constrained clients to participate with theoretical convergence guarantees."
---

# FedLMT: Tackling System Heterogeneity of Federated Learning via Low-Rank Model Training with Theoretical Guarantees

**Source**: [https://proceedings.mlr.press/v235/liu24ch.html](https://proceedings.mlr.press/v235/liu24ch.html)

**TLDR**: FedLMT addresses system heterogeneity in federated learning via low-rank model training that enables resource-constrained clients to participate with theoretical convergence guarantees.

## Abstract

Federated learning (FL) is an emerging machine learning paradigm for preserving data privacy. However, diverse client hardware often has varying computation resources. Such system heterogeneity limits the participation of resource-constrained clients in FL, and hence degrades the global model accuracy. To enable heterogeneous clients to participate in and contribute to FL training, previous works tackle this problem by assigning customized sub-models to individual clients with model pruning, distillation, or low-rank based techniques. Unfortunately, the global model trained by these methods still encounters performance degradation due to heterogeneous sub-model aggregation. Besides, most methods are heuristic-based and lack convergence analysis. In this work, we propose the FedLMT framework to bridge the performance gap, by assigning clients with a homogeneous pre-factorized low-rank model to substantially reduce resource consumption without conducting heterogeneous aggregation. We theoretically prove that the convergence of the low-rank model can guarantee the convergence of the original full model. To further meet clients’ personalized resource needs, we extend FedLMT to pFedLMT, by separating model parameters into common and custom ones. Finally, extensive experiments are conducted to verify our theoretical analysis and show that FedLMT and pFedLMT outperform other baselines with much less communication and computation costs.