---
title: "The Computational Complexity of Finding Second-Order Stationary Points"
source: "https://proceedings.mlr.press/v235/kontogiannis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kontogiannis24a/kontogiannis24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'dynamic-algorithms-and-complexity-theory']
tags: ['non-convex-optimization', 'second-order-stationarity', 'computational-complexity', 'NP-hard']
venue: "ICML 2024"
tldr: "Analyzes the computational complexity of finding second-order stationary points in non-convex optimization problems."
---

# The Computational Complexity of Finding Second-Order Stationary Points

**Source**: [https://proceedings.mlr.press/v235/kontogiannis24a.html](https://proceedings.mlr.press/v235/kontogiannis24a.html)

**TLDR**: Analyzes the computational complexity of finding second-order stationary points in non-convex optimization problems.

## Abstract

Non-convex minimization problems are universally considered hard, and even guaranteeing that a computed solution is locally minimizing is known to be NP-hard. In this general context, our paper focuses on the problem of finding stationary points that satisfy an approximate second-order optimality condition, which serves to exclude strict saddles and other non-minimizing stationary points. Our main result is that the problem of finding approximate second-order stationary points (SOSPs) is PLS-complete, i.e., of the same complexity as the problem of finding first-order stationary points (FOSPs), thus resolving an open question in the field. In particular, our results imply that, under the widely believed complexity conjecture that PLS $\neq$ FNP, finding approximate SOSPs in unconstrained domains is easier than in constrained domains, which is known to be NP-hard. This comes in stark contrast with earlier results which implied that, unless PLS = CLS, finding approximate FOSPs in unconstrained domains is harder than in constrained domains.