---
title: "Multi-group Learning for Hierarchical Groups"
source: "https://proceedings.mlr.press/v235/deng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deng24a/deng24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'fairness-aware-algorithmic-decision-making']
tags: ['multi-group-learning', 'hierarchical-groups', 'PAC-learning', 'fairness', 'subgroup-generalization']
venue: "ICML 2024"
tldr: "Extends multi-group PAC learning to hierarchically structured groups and provides efficient algorithms with improved sample complexity guarantees."
---

# Multi-group Learning for Hierarchical Groups

**Source**: [https://proceedings.mlr.press/v235/deng24a.html](https://proceedings.mlr.press/v235/deng24a.html)

**TLDR**: Extends multi-group PAC learning to hierarchically structured groups and provides efficient algorithms with improved sample complexity guarantees.

## Abstract

The multi-group learning model formalizes the learning scenario in which a single predictor must generalize well on multiple, possibly overlapping subgroups of interest. We extend the study of multi-group learning to the natural case where the groups are hierarchically structured. We design an algorithm for this setting that outputs an interpretable and deterministic decision tree predictor with near-optimal sample complexity. We then conduct an empirical evaluation of our algorithm and find that it achieves attractive generalization properties on real datasets with hierarchical group structure.