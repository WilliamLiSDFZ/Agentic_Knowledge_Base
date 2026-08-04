---
title: "Mitigating Catastrophic Forgetting in Online Continual Learning by Modeling Previous Task Interrelations via Pareto Optimization"
source: "https://proceedings.mlr.press/v235/wu24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ab/wu24ab.pdf"
categories: ['continual-learning-memory-plasticity', 'optimization-algorithms-convergence-theory']
tags: ['continual-learning', 'catastrophic-forgetting', 'pareto-optimization', 'replay-buffer', 'task-interrelations']
venue: "ICML 2024"
tldr: "Mitigates catastrophic forgetting in online continual learning by modeling previous task interrelations through Pareto optimization with replay-based methods."
---

# Mitigating Catastrophic Forgetting in Online Continual Learning by Modeling Previous Task Interrelations via Pareto Optimization

**Source**: [https://proceedings.mlr.press/v235/wu24ab.html](https://proceedings.mlr.press/v235/wu24ab.html)

**TLDR**: Mitigates catastrophic forgetting in online continual learning by modeling previous task interrelations through Pareto optimization with replay-based methods.

## Abstract

Catastrophic forgetting remains a core challenge in continual learning (CL), where the models struggle to retain previous knowledge when learning new tasks. While existing replay-based CL methods have been proposed to tackle this challenge by utilizing a memory buffer to store data from previous tasks, they generally overlook the interdependence between previously learned tasks and fail to encapsulate the optimally integrated knowledge in previous tasks, leading to sub-optimal performance of the previous tasks. Against this issue, we first reformulate replay-based CL methods as a unified hierarchical gradient aggregation framework. We then incorporate the Pareto optimization to capture the interrelationship among previously learned tasks and design a Pareto-Optimized CL algorithm (POCL), which effectively enhances the overall performance of past tasks while ensuring the performance of the current task. Comprehensive empirical results demonstrate that the proposed POCL outperforms current state-of-the-art CL methods across multiple datasets and different settings.