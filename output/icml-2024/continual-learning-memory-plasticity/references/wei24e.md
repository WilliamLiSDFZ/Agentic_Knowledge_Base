---
title: "Task Groupings Regularization: Data-Free Meta-Learning with Heterogeneous Pre-trained Models"
source: "https://proceedings.mlr.press/v235/wei24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wei24e/wei24e.pdf"
categories: ['continual-learning-memory-plasticity']
tags: ['meta-learning', 'data-free', 'heterogeneous-models']
venue: "ICML 2024"
tldr: "Task Groupings Regularization is proposed to handle heterogeneous pre-trained models in data-free meta-learning for fast adaptation to new tasks."
---

# Task Groupings Regularization: Data-Free Meta-Learning with Heterogeneous Pre-trained Models

**Source**: [https://proceedings.mlr.press/v235/wei24e.html](https://proceedings.mlr.press/v235/wei24e.html)

**TLDR**: Task Groupings Regularization is proposed to handle heterogeneous pre-trained models in data-free meta-learning for fast adaptation to new tasks.

## Abstract

Data-Free Meta-Learning (DFML) aims to derive knowledge from a collection of pre-trained models without accessing their original data, enabling the rapid adaptation to new unseen tasks. Current methods often overlook the heterogeneity among pre-trained models, which leads to performance degradation due to task conflicts. In this paper, we empirically and theoretically identify and analyze the model heterogeneity in DFML. We find that model heterogeneity introduces a heterogeneity-homogeneity trade-off, where homogeneous models reduce task conflicts but also increase the overfitting risk. Balancing this trade-off is crucial for learning shared representations across tasks. Based on our findings, we propose Task Groupings Regularization, a novel approach that benefits from model heterogeneity by grouping and aligning conflicting tasks. Specifically, we embed pre-trained models into a task space to compute dissimilarity, and group heterogeneous models together based on this measure. Then, we introduce implicit gradient regularization within each group to mitigate potential conflicts. By encouraging a gradient direction suitable for all tasks, the meta-model captures shared representations that generalize across tasks. Comprehensive experiments showcase the superiority of our approach in multiple benchmarks, effectively tackling the model heterogeneity in challenging multi-domain and multi-architecture scenarios.