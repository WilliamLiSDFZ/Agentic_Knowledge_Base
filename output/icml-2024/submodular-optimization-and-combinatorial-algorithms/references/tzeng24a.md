---
title: "Matroid Semi-Bandits in Sublinear Time"
source: "https://proceedings.mlr.press/v235/tzeng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tzeng24a/tzeng24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['matroid-bandits', 'semi-bandits', 'sublinear-time']
venue: "ICML 2024"
tldr: "Develops sublinear-time algorithms for matroid semi-bandits achieving efficient per-round computation without sacrificing regret guarantees."
---

# Matroid Semi-Bandits in Sublinear Time

**Source**: [https://proceedings.mlr.press/v235/tzeng24a.html](https://proceedings.mlr.press/v235/tzeng24a.html)

**TLDR**: Develops sublinear-time algorithms for matroid semi-bandits achieving efficient per-round computation without sacrificing regret guarantees.

## Abstract

We study the matroid semi-bandits problem, where at each round the learner plays a subset of $K$ arms from a feasible set, and the goal is to maximize the expected cumulative linear rewards. Existing algorithms have per-round time complexity at least $\Omega(K)$, which becomes expensive when $K$ is large. To address this computational issue, we propose FasterCUCB whose sampling rule takes time sublinear in $K$ for common classes of matroids: $\mathcal{O}(D\text{ polylog}(K)\text{ polylog}(T))$ for uniform matroids, partition matroids, and graphical matroids, and $\mathcal{O}(D\sqrt{K}\text{ polylog}(T))$ for transversal matroids. Here, $D$ is the maximum number of elements in any feasible subset of arms, and $T$ is the horizon. Our technique is based on dynamic maintenance of an approximate maximum-weight basis over inner-product weights. Although the introduction of an approximate maximum-weight basis presents a challenge in regret analysis, we can still guarantee an upper bound on regret as tight as CUCB in the sense that it matches the gap-dependent lower bound by Kveton et al. (2014a) asymptotically.