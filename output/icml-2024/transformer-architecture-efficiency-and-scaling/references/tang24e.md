---
title: "Merging Multi-Task Models via Weight-Ensembling Mixture of Experts"
source: "https://proceedings.mlr.press/v235/tang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24e/tang24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['model-merging', 'mixture-of-experts', 'multi-task-learning']
venue: "ICML 2024"
tldr: "Weight-Ensembling Mixture of Experts merges multiple task-specific Transformer models into a unified model for concurrent multi-task execution."
---

# Merging Multi-Task Models via Weight-Ensembling Mixture of Experts

**Source**: [https://proceedings.mlr.press/v235/tang24e.html](https://proceedings.mlr.press/v235/tang24e.html)

**TLDR**: Weight-Ensembling Mixture of Experts merges multiple task-specific Transformer models into a unified model for concurrent multi-task execution.

## Abstract

Merging various task-specific Transformer-based vision models trained on different tasks into a single unified model can execute all the tasks concurrently. Previous methods, exemplified by task arithmetic, have been proven to be both effective and scalable. Existing methods have primarily focused on seeking a static optimal solution within the original model parameter space. A notable challenge is mitigating the interference between parameters of different models, which can substantially deteriorate performance. In this paper, we propose to merge most of the parameters while upscaling the MLP of the Transformer layers to a weight-ensembling mixture of experts (MoE) module, which can dynamically integrate shared and task-specific knowledge based on the input, thereby providing a more flexible solution that can adapt to the specific needs of each instance. Our key insight is that by identifying and separating shared knowledge and task-specific knowledge, and then dynamically integrating them, we can mitigate the parameter interference problem to a great extent. We conduct the conventional multi-task model merging experiments and evaluate the generalization and robustness of our method. The results demonstrate the effectiveness of our method and provide a comprehensive understanding of our method. The code is available at https://github.com/tanganke/weight-ensembling_MoE