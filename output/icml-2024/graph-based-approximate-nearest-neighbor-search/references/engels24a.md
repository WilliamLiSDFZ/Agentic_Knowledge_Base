---
title: "Approximate Nearest Neighbor Search with Window Filters"
source: "https://proceedings.mlr.press/v235/engels24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/engels24a/engels24a.pdf"
categories: ['graph-based-approximate-nearest-neighbor-search', 'information-retrieval-and-recommendation-systems']
tags: ['approximate-nearest-neighbor', 'window-search', 'semantic-search', 'filtering', 'indexing']
venue: "ICML 2024"
tldr: "Defines the c-approximate window search problem for nearest neighbor search with numeric label range constraints and provides efficient algorithmic solutions."
---

# Approximate Nearest Neighbor Search with Window Filters

**Source**: [https://proceedings.mlr.press/v235/engels24a.html](https://proceedings.mlr.press/v235/engels24a.html)

**TLDR**: Defines the c-approximate window search problem for nearest neighbor search with numeric label range constraints and provides efficient algorithmic solutions.

## Abstract

We define and investigate the problem of c-approximate window search: approximate nearest neighbor search where each point in the dataset has a numeric label, and the goal is to find nearest neighbors to queries within arbitrary label ranges. Many semantic search problems, such as image and document search with timestamp filters, or product search with cost filters, are natural examples of this problem. We propose and theoretically analyze a modular tree-based framework for transforming an index that solves the traditional c-approximate nearest neighbor problem into a data structure that solves window search. On standard nearest neighbor benchmark datasets equipped with random label values, adversarially constructed embeddings, and image search embeddings with real timestamps, we obtain up to a $75\times$ speedup over existing solutions at the same level of recall.