---
title: "Optimal Acceleration for Minimax and Fixed-Point Problems is Not Unique"
source: "https://proceedings.mlr.press/v235/yoon24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yoon24b/yoon24b.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['minimax-optimization', 'anchoring', 'acceleration', 'fixed-point']
venue: "ICML 2024"
tldr: "The paper shows that optimal acceleration for minimax and fixed-point problems is not unique by presenting multiple optimal anchoring mechanisms."
---

# Optimal Acceleration for Minimax and Fixed-Point Problems is Not Unique

**Source**: [https://proceedings.mlr.press/v235/yoon24b.html](https://proceedings.mlr.press/v235/yoon24b.html)

**TLDR**: The paper shows that optimal acceleration for minimax and fixed-point problems is not unique by presenting multiple optimal anchoring mechanisms.

## Abstract

Recently, accelerated algorithms using the anchoring mechanism for minimax optimization and fixed-point problems have been proposed, and matching complexity lower bounds establish their optimality. In this work, we present the surprising observation that the optimal acceleration mechanism in minimax optimization and fixed-point problems is not unique. Our new algorithms achieve exactly the same worst-case convergence rates as existing anchor-based methods while using materially different acceleration mechanisms. Specifically, these new algorithms are dual to the prior anchor-based accelerated methods in the sense of H-duality. This finding opens a new avenue of research on accelerated algorithms since we now have a family of methods that empirically exhibit varied characteristics while having the same optimal worst-case guarantee.