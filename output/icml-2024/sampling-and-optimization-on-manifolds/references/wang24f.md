---
title: "Non-parametric Online Change Point Detection on Riemannian Manifolds"
source: "https://proceedings.mlr.press/v235/wang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24f/wang24f.pdf"
categories: ['sequential-change-detection-theory-and-algorithms', 'sampling-and-optimization-on-manifolds']
tags: ['change-point-detection', 'Riemannian-manifolds', 'non-parametric', 'streaming-data', 'online-detection']
venue: "ICML 2024"
tldr: "A non-parametric online change point detection method is proposed for streaming data lying on Riemannian manifolds."
---

# Non-parametric Online Change Point Detection on Riemannian Manifolds

**Source**: [https://proceedings.mlr.press/v235/wang24f.html](https://proceedings.mlr.press/v235/wang24f.html)

**TLDR**: A non-parametric online change point detection method is proposed for streaming data lying on Riemannian manifolds.

## Abstract

Non-parametric detection of change points in streaming time series data that belong to Euclidean spaces has been extensively studied in the literature. Nevertheless, when the data belongs to a Riemannian manifold, existing approaches are no longer applicable as they fail to account for the structure and geometry of the manifold. In this paper, we introduce a non-parametric algorithm for online change point detection in manifold-valued data streams. This algorithm monitors the generalized Karcher mean of the data, computed using stochastic Riemannian optimization. We provide theoretical bounds on the detection and false alarm rate performances of the algorithm, using a new result on the non-asymptotic convergence of the stochastic Riemannian gradient descent. We apply our algorithm to two different Riemannian manifolds. Experimental results with both synthetic and real data illustrate the performance of the proposed method.