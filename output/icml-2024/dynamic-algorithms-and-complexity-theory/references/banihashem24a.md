---
title: "A Dynamic Algorithm for Weighted Submodular Cover Problem"
source: "https://proceedings.mlr.press/v235/banihashem24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/banihashem24a/banihashem24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['submodular-cover', 'dynamic-algorithms', 'online-updates']
venue: "ICML 2024"
tldr: "The first dynamic algorithm for the weighted submodular cover problem under element insertions and deletions is introduced."
---

# A Dynamic Algorithm for Weighted Submodular Cover Problem

**Source**: [https://proceedings.mlr.press/v235/banihashem24a.html](https://proceedings.mlr.press/v235/banihashem24a.html)

**TLDR**: The first dynamic algorithm for the weighted submodular cover problem under element insertions and deletions is introduced.

## Abstract

We initiate the study of the submodular cover problem in a dynamic setting where the elements of the ground set are inserted and deleted. In the classical submodular cover problem, we are given a monotone submodular function $f : 2^{V} \to \mathbb{R}^{\ge 0}$ and the goal is to obtain a set $S \subseteq V$ that minimizes the cost subject to the constraint $f(S) = f(V)$. This is a classical problem in computer science and generalizes the Set Cover problem, 2-Set Cover, and dominating set problem among others. We consider this problem in a dynamic setting where there are updates to our set $V$, in the form of insertions and deletions of elements from a ground set $\mathcal{V}$, and the goal is to maintain an approximately optimal solution with low query complexity per update. For this problem, we propose a randomized algorithm that, in expectation, obtains a $(1-O(\epsilon), O(\epsilon^{-1}))$-bicriteria approximation using polylogarithmic query complexity per update.