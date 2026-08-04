---
title: "Pruned Pivot: Correlation Clustering Algorithm for Dynamic, Parallel, and Local Computation Models"
source: "https://proceedings.mlr.press/v235/dalirrooyfard24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dalirrooyfard24a/dalirrooyfard24a.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['correlation-clustering', 'dynamic-algorithms', 'parallel-computation', 'local-computation', 'graph-clustering']
venue: "ICML 2024"
tldr: "Presents a pruned pivot algorithm for correlation clustering that achieves improved approximation guarantees across dynamic, parallel, and local computation models."
---

# Pruned Pivot: Correlation Clustering Algorithm for Dynamic, Parallel, and Local Computation Models

**Source**: [https://proceedings.mlr.press/v235/dalirrooyfard24a.html](https://proceedings.mlr.press/v235/dalirrooyfard24a.html)

**TLDR**: Presents a pruned pivot algorithm for correlation clustering that achieves improved approximation guarantees across dynamic, parallel, and local computation models.

## Abstract

Given a graph with positive and negative edge labels, the correlation clustering problem aims to cluster the nodes so to minimize the total number of between-cluster positive and within-cluster negative edges. This problem has many applications in data mining, particularly in unsupervised learning. Inspired by the prevalence of large graphs and constantly changing data in modern applications, we study correlation clustering in dynamic, parallel (MPC), and local computation (LCA) settings. We design an approach that improves state-of-the-art runtime complexities in all these settings. In particular, we provide the first fully dynamic algorithm that runs in an expected amortized constant time, without any dependence on the graph size. Moreover, our algorithm essentially matches the approximation guarantee of the celebrated Pivot algorithm.