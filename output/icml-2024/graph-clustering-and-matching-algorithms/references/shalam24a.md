---
title: "The Balanced-Pairwise-Affinities Feature Transform"
source: "https://proceedings.mlr.press/v235/shalam24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shalam24a/shalam24a.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'clustering-methods-and-multi-view-learning']
tags: ['feature-transform', 'pairwise-affinities', 'matching-grouping']
venue: "ICML 2024"
tldr: "The Balanced-Pairwise-Affinities feature transform upgrades input item features to encode high-order relations, facilitating downstream matching and grouping tasks."
---

# The Balanced-Pairwise-Affinities Feature Transform

**Source**: [https://proceedings.mlr.press/v235/shalam24a.html](https://proceedings.mlr.press/v235/shalam24a.html)

**TLDR**: The Balanced-Pairwise-Affinities feature transform upgrades input item features to encode high-order relations, facilitating downstream matching and grouping tasks.

## Abstract

The Balanced-Pairwise-Affinities (BPA) feature transform is designed to upgrade the features of a set of input items to facilitate downstream matching or grouping related tasks. The transformed set encodes a rich representation of high order relations between the input features. A particular min-cost-max-flow fractional matching problem, whose entropy regularized version can be approximated by an optimal transport (OT) optimization, leads to a transform which is efficient, differentiable, equivariant, parameterless and probabilistically interpretable. While the Sinkhorn OT solver has been adapted extensively in many contexts, we use it differently by minimizing the cost between a set of features to itself and using the transport plan’s rows as the new representation.Empirically, the transform is highly effective and flexible in its use and consistently improves networks it is inserted into, in a variety of tasks and training schemes. We demonstrate state-of-the-art results in few-shot classification, unsupervised image clustering and person re-identification. Code is available at github.com/DanielShalam/BPA .