---
title: "Dynamic Correlation Clustering in Sublinear Update Time"
source: "https://proceedings.mlr.press/v235/cohen-addad24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen-addad24d/cohen-addad24d.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['correlation-clustering', 'dynamic-graphs', 'sublinear-algorithms']
venue: "ICML 2024"
tldr: "Studies correlation clustering in dynamic vertex streams and achieves sublinear update time for continuously maintaining a near-optimal partition."
---

# Dynamic Correlation Clustering in Sublinear Update Time

**Source**: [https://proceedings.mlr.press/v235/cohen-addad24d.html](https://proceedings.mlr.press/v235/cohen-addad24d.html)

**TLDR**: Studies correlation clustering in dynamic vertex streams and achieves sublinear update time for continuously maintaining a near-optimal partition.

## Abstract

We study the classic problem of correlation clustering in dynamic vertex streams. In this setting, vertices are either added or randomly deleted over time, and each vertex pair is connected by a positive or negative edge. The objective is to continuously find a partition which minimizes the sum of positive edges crossing clusters and negative edges within clusters. We present an algorithm that maintains an $O(1)$-approximation with $O(\text{polylog} n)$ amortized update time. Prior to our work Behnezhad et al. in SODA 2023 achieved a $5$-approximation with $O(1)$ expected update time in edge streams which translates in vertex streams to an $O(D)$-update time where $D$ is the maximum possible degree. Finally we complement our theoretical analysis with experiments on real world data.