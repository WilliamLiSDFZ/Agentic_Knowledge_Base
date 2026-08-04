---
title: "Robust Graph Matching when Nodes are Corrupt"
source: "https://proceedings.mlr.press/v235/ameen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ameen24a/ameen24a.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'dynamic-algorithms-and-complexity-theory']
tags: ['graph-matching', 'node-corruption', 'correlated-graphs']
venue: "ICML 2024"
tldr: "This paper studies graph matching under node corruption and establishes fundamental limits and algorithms for recovering correct node correspondences."
---

# Robust Graph Matching when Nodes are Corrupt

**Source**: [https://proceedings.mlr.press/v235/ameen24a.html](https://proceedings.mlr.press/v235/ameen24a.html)

**TLDR**: This paper studies graph matching under node corruption and establishes fundamental limits and algorithms for recovering correct node correspondences.

## Abstract

Two models are introduced to study the problem of matching two correlated graphs when some of the nodes are corrupt. In the weak model, a random subset of nodes in one or both graphs can interact randomly with their network. For this model, it is shown that no estimator can correctly recover a positive fraction of the corrupt nodes. Necessary conditions for any estimator to correctly identify and match all the uncorrupt nodes are derived, and it is shown that these conditions are also sufficient for the k-core estimator. In the strong model, an adversarially selected subset of nodes in one or both graphs can interact arbitrarily with their network. For this model, detection of corrupt nodes is impossible. Even so, we show that if only one of the networks is compromised, then under appropriate conditions, the maximum overlap estimator can correctly match a positive fraction of nodes albeit without explicitly identifying them.