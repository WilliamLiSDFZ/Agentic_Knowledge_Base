---
title: "Dynamic Facility Location in High Dimensional Euclidean Spaces"
source: "https://proceedings.mlr.press/v235/bhattacharya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bhattacharya24a/bhattacharya24a.pdf"
categories: ['dynamic-algorithms-and-complexity-theory', 'sampling-compression-and-dimensionality-reduction']
tags: ['facility-location', 'dynamic-algorithms', 'euclidean-spaces', 'high-dimensional']
venue: "ICML 2024"
tldr: "This paper studies dynamic facility location in high-dimensional Euclidean spaces, developing efficient algorithms that handle point insertions and deletions while maintaining solution quality and stability."
---

# Dynamic Facility Location in High Dimensional Euclidean Spaces

**Source**: [https://proceedings.mlr.press/v235/bhattacharya24a.html](https://proceedings.mlr.press/v235/bhattacharya24a.html)

**TLDR**: This paper studies dynamic facility location in high-dimensional Euclidean spaces, developing efficient algorithms that handle point insertions and deletions while maintaining solution quality and stability.

## Abstract

We study the facility location problem in the dynamic setting, where the goal is to efficiently process an intermixed sequence of point insertions and deletions while maintaining a high quality and stable solution. Although the problem has been studied in the context of general metrics and low-dimensional spaces, much remains unknown concerning dynamic facility location in high dimensional spaces. In this work, we present the first fully dynamic algorithm for facility location in high-dimensional spaces $\mathbb{R}^{d}$. For any $c \geq 1$, our algorithm achieves $O(c)$-approximation, supports point updates in $\tilde{O}(\mathrm{poly}(d)n^{1/c + o(1)})$ amortized time and incurs $O(1)$ amortized recourse. More generally, our result shows that despite the linear-time lower bound on the update time for general metrics, it is possible to achieve sub-linear update times for metric spaces that admit dynamic nearest neighbour oracles. Experiments on real datasets confirm that our algorithm achieves high-quality solutions with low running time, and incurs minimal recourse.