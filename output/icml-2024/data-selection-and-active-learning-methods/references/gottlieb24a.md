---
title: "Weighted distance nearest neighbor condensing"
source: "https://proceedings.mlr.press/v235/gottlieb24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gottlieb24a/gottlieb24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'data-selection-and-active-learning-methods']
tags: ['nearest-neighbor-condensing', 'weighted-distance', 'compression']
venue: "ICML 2024"
tldr: "This paper introduces weighted distance nearest neighbor condensing, assigning weights to condensed points to improve classification efficiency."
---

# Weighted distance nearest neighbor condensing

**Source**: [https://proceedings.mlr.press/v235/gottlieb24a.html](https://proceedings.mlr.press/v235/gottlieb24a.html)

**TLDR**: This paper introduces weighted distance nearest neighbor condensing, assigning weights to condensed points to improve classification efficiency.

## Abstract

The problem of nearest neighbor condensing has enjoyed a long history of study, both in its theoretical and practical aspects. In this paper, we introduce the problem of weighted distance nearest neighbor condensing, where one assigns weights to each point of the condensed set, and then new points are labeled based on their weighted distance nearest neighbor in the condensed set. We study the theoretical properties of this new model, and show that it can produce dramatically better condensing than the standard nearest neighbor rule, yet is characterized by generalization bounds almost identical to the latter. We then suggest a condensing heuristic for our new problem. We demonstrate Bayes consistency for this heuristic, and also show promising empirical results.