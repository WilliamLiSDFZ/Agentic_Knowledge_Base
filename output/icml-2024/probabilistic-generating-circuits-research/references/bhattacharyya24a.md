---
title: "Total Variation Distance Meets Probabilistic Inference"
source: "https://proceedings.mlr.press/v235/bhattacharyya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bhattacharyya24a/bhattacharyya24a.pdf"
categories: ['probabilistic-generating-circuits-research', 'sampling-compression-and-dimensionality-reduction']
tags: ['total-variation-distance', 'probabilistic-inference', 'graphical-models', 'reduction']
venue: "ICML 2024"
tldr: "This paper establishes a novel reduction from total variation distance estimation to probabilistic inference over directed graphical models."
---

# Total Variation Distance Meets Probabilistic Inference

**Source**: [https://proceedings.mlr.press/v235/bhattacharyya24a.html](https://proceedings.mlr.press/v235/bhattacharyya24a.html)

**TLDR**: This paper establishes a novel reduction from total variation distance estimation to probabilistic inference over directed graphical models.

## Abstract

In this paper, we establish a novel connection between total variation (TV) distance estimation and probabilistic inference. In particular, we present an efficient, structure-preserving reduction from relative approximation of TV distance to probabilistic inference over directed graphical models. This reduction leads to a fully polynomial randomized approximation scheme (FPRAS) for estimating TV distances between same-structure distributions over any class of Bayes nets for which there is an efficient probabilistic inference algorithm. In particular, it leads to an FPRAS for estimating TV distances between distributions that are defined over a common Bayes net of small treewidth. Prior to this work, such approximation schemes only existed for estimating TV distances between product distributions. Our approach employs a new notion of partial couplings of high-dimensional distributions, which might be of independent interest.