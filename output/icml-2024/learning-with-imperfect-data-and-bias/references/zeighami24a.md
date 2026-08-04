---
title: "Theoretical Analysis of Learned Database Operations under Distribution Shift through Distribution Learnability"
source: "https://proceedings.mlr.press/v235/zeighami24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeighami24a/zeighami24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['learned-database-operations', 'distribution-shift', 'learnability-theory']
venue: "ICML 2024"
tldr: "Theoretical analysis of how distribution shift affects learned database operations like indexing and cardinality estimation using distribution learnability frameworks."
---

# Theoretical Analysis of Learned Database Operations under Distribution Shift through Distribution Learnability

**Source**: [https://proceedings.mlr.press/v235/zeighami24a.html](https://proceedings.mlr.press/v235/zeighami24a.html)

**TLDR**: Theoretical analysis of how distribution shift affects learned database operations like indexing and cardinality estimation using distribution learnability frameworks.

## Abstract

Use of machine learning to perform database operations, such as indexing, cardinality estimation, and sorting, is shown to provide substantial performance benefits. However, when datasets change and data distribution shifts, empirical results also show performance degradation for learned models, possibly to worse than non-learned alternatives. This, together with a lack of theoretical understanding of learned methods undermines their practical applicability, since there are no guarantees on how well the models will perform after deployment. In this paper, we present the first known theoretical characterization of the performance of learned models in dynamic datasets, for the aforementioned operations. Our results show novel theoretical characteristics achievable by learned models and provide bounds on the performance of the models that characterize their advantages over non-learned methods, showing why and when learned models can outperform the alternatives. Our analysis develops the distribution learnability framework and novel theoretical tools which build the foundation for the analysis of learned database operations in the future.