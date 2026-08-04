---
title: "Towards Neural Architecture Search through Hierarchical Generative Modeling"
source: "https://proceedings.mlr.press/v235/xiang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiang24a/xiang24a.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-architecture-search', 'generative-modeling', 'hierarchical']
venue: "ICML 2024"
tldr: "Proposes a hierarchical generative modeling approach to neural architecture search that balances search space breadth and computational cost."
---

# Towards Neural Architecture Search through Hierarchical Generative Modeling

**Source**: [https://proceedings.mlr.press/v235/xiang24a.html](https://proceedings.mlr.press/v235/xiang24a.html)

**TLDR**: Proposes a hierarchical generative modeling approach to neural architecture search that balances search space breadth and computational cost.

## Abstract

Neural Architecture Search (NAS) aims to automate deep neural network design across various applications, while a good search space design is core to NAS performance. A too-narrow search space may fail to cover diverse task requirements, whereas a too-broad one can escalate computational expenses and reduce efficiency. %We propose automatically generating the search space to tailor it to specific task conditions, optimizing search costs and producing viable architectures. In this work, we aim to address this challenge by leaning on the recent advances in generative modelling – we propose a novel method that can navigate through an extremely large, general-purpose initial search space efficiently by training a two-level generative model hierarchy. The first level uses Conditional Continuous Normalizing Flow (CCNF) for micro-cell design, while the second employs a transformer-based sequence generator to craft macro architectures aligned with task needs and architectural constraints. To ensure computational feasibility, we pretrain the generative models in a task-agnostic manner using a metric space of graph and zero-cost (ZC) similarities between architectures. We show our approach can achieve state-of-the-art performance among other low-cost NAS methods across different tasks on CIFAR-10/100, ImageNet and NAS-Bench-360.