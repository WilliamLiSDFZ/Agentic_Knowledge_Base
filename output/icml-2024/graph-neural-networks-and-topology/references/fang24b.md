---
title: "Exploring Correlations of Self-Supervised Tasks for Graphs"
source: "https://proceedings.mlr.press/v235/fang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fang24b/fang24b.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-self-supervised-learning', 'task-correlations', 'representation-learning']
venue: "ICML 2024"
tldr: "Systematically explores correlations among self-supervised tasks for graph representation learning."
---

# Exploring Correlations of Self-Supervised Tasks for Graphs

**Source**: [https://proceedings.mlr.press/v235/fang24b.html](https://proceedings.mlr.press/v235/fang24b.html)

**TLDR**: Systematically explores correlations among self-supervised tasks for graph representation learning.

## Abstract

Graph self-supervised learning has sparked a research surge in training informative representations without accessing any labeled data. However, our understanding of graph self-supervised learning remains limited, and the inherent relationships between various self-supervised tasks are still unexplored. Our paper aims to provide a fresh understanding of graph self-supervised learning based on task correlations. Specifically, we evaluate the performance of the representations trained by one specific task on other tasks and define correlation values to quantify task correlations. Through this process, we unveil the task correlations between various self-supervised tasks and can measure their expressive capabilities, which are closely related to downstream performance. By analyzing the correlation values between tasks across various datasets, we reveal the complexity of task correlations and the limitations of existing multi-task learning methods. To obtain more capable representations, we propose Graph Task Correlation Modeling (GraphTCM) to illustrate the task correlations and utilize it to enhance graph self-supervised training. The experimental results indicate that our method significantly outperforms existing methods across various downstream tasks.