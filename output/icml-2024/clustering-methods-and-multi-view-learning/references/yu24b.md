---
title: "Towards Resource-friendly, Extensible and Stable Incomplete Multi-view Clustering"
source: "https://proceedings.mlr.press/v235/yu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24b/yu24b.pdf"
categories: ['clustering-methods-and-multi-view-learning']
tags: ['incomplete-multi-view-clustering', 'scalability', 'stability', 'hyper-parameters']
venue: "ICML 2024"
tldr: "ToRES is a resource-friendly, extensible, and stable scheme for incomplete multi-view clustering with low overhead and deterministic results."
---

# Towards Resource-friendly, Extensible and Stable Incomplete Multi-view Clustering

**Source**: [https://proceedings.mlr.press/v235/yu24b.html](https://proceedings.mlr.press/v235/yu24b.html)

**TLDR**: ToRES is a resource-friendly, extensible, and stable scheme for incomplete multi-view clustering with low overhead and deterministic results.

## Abstract

Incomplete multi-view clustering (IMVC) methods typically encounter three drawbacks: (1) intense time and/or space overheads; (2) intractable hyper-parameters; (3) non-zero variance results. With these concerns in mind, we give a simple yet effective IMVC scheme, termed as ToRES. Concretely, instead of self-expression affinity, we manage to construct prototype-sample affinity for incomplete data so as to decrease the memory requirements. To eliminate hyper-parameters, besides mining complementary features among views by view-wise prototypes, we also attempt to devise cross-view prototypes to capture consensus features for jointly forming high-quality clustering representation. To avoid the variance, we successfully unify representation learning and clustering operation, and directly optimize the discrete cluster indicators from incomplete data. Then, for the resulting objective function, we provide two equivalent solutions from perspectives of feasible region partitioning and objective transformation. Many results suggest that ToRES exhibits advantages against 20 SOTA algorithms, even in scenarios with a higher ratio of incomplete data.