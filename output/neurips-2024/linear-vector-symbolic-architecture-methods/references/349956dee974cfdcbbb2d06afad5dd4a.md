---
title: "Non-parametric classification via expand-and-sparsify representation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/349956dee974cfdcbbb2d06afad5dd4a-Abstract-Conference.html"
categories: ['linear-vector-symbolic-architecture-methods', 'statistical-learning-theory-and-matrix-methods']
tags: ['expand-and-sparsify', 'non-parametric-classification', 'sparse-representation', 'random-projection', 'high-dimensional']
venue: "NeurIPS 2024"
tldr: "Analyzes non-parametric classification via expand-and-sparsify representations combining random expansion and sparsification on the hypersphere."
---

# Non-parametric classification via expand-and-sparsify representation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/349956dee974cfdcbbb2d06afad5dd4a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/349956dee974cfdcbbb2d06afad5dd4a-Abstract-Conference.html)

**TLDR**: Analyzes non-parametric classification via expand-and-sparsify representations combining random expansion and sparsification on the hypersphere.

## Abstract

In *expand-and-sparsify* (EaS) representation, a data point in $\mathcal{S}^{d-1}$ is first randomly mapped to higher dimension $\mathbb{R}^m$, where $m>d$, followed by a sparsification operation where the informative $k \ll m$ of the $m$ coordinates are set to one and the rest are set to zero. We propose two algorithms for non-parametric classification using such EaS representation. For our first algorithm, we use *winners-take-all* operation for the sparsification step and show that the proposed classifier admits the form of a locally weighted average classifier and establish its consistency via Stone's Theorem. Further, assuming that the conditional probability function $P(y=1|x)=\eta(x)$ is H\"{o}lder continuous and for optimal choice of $m$, we show that the convergence rate of this classifier is minimax-optimal. For our second algorithm, we use *empirical $k$-thresholding* operation for the sparsification step, and under the assumption that data lie on a low dimensional manifold of dimension $d_0\ll d$, we show that the convergence rate of this classifier depends only on $d_0$ and is again minimax-optimal. Empirical evaluations performed on real-world datasets corroborate our theoretical results.