---
title: "Scaling Beyond the GPU Memory Limit for Large Mixture-of-Experts Model Training"
source: "https://proceedings.mlr.press/v235/kim24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24w/kim24w.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'privacy-preserving-federated-and-distributed-learning']
tags: ['mixture-of-experts', 'GPU-memory', 'large-scale-training']
venue: "ICML 2024"
tldr: "Proposes a method to scale Mixture-of-Experts model training beyond GPU memory limits while addressing load imbalance."
---

# Scaling Beyond the GPU Memory Limit for Large Mixture-of-Experts Model Training

**Source**: [https://proceedings.mlr.press/v235/kim24w.html](https://proceedings.mlr.press/v235/kim24w.html)

**TLDR**: Proposes a method to scale Mixture-of-Experts model training beyond GPU memory limits while addressing load imbalance.

## Abstract

Mixture-of-Experts (MoE) is a powerful technique for enhancing the performance of neural networks while decoupling computational complexity from the number of parameters. However, despite this, scaling the number of experts requires adding more GPUs. In addition, the load imbalance in token load across experts causes unnecessary computation or straggler problems. We present ES-MoE, a novel method for efficient scaling MoE training. It offloads expert parameters to host memory and leverages pipelined expert processing to overlap GPU-CPU communication with GPU computation. It dynamically balances token loads across GPUs, improving computational efficiency. ES-MoE accelerates MoE training on a limited number of GPUs without degradation in model performance. We validate our approach on GPT-based MoE models, demonstrating 67$\times$ better scalability and up to 17.5$\times$ better throughput over existing frameworks.