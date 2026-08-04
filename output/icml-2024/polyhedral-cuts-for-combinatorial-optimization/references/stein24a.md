---
title: "Partial Optimality in the Linear Ordering Problem"
source: "https://proceedings.mlr.press/v235/stein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stein24a/stein24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms', 'polyhedral-cuts-for-combinatorial-optimization']
tags: ['linear-ordering-problem', 'partial-optimality', 'combinatorial-optimization', 'NP-hard', 'polyhedral']
venue: "ICML 2024"
tldr: "Algorithms are introduced to efficiently solve subsets of the NP-hard linear ordering problem by determining partial optimal orderings."
---

# Partial Optimality in the Linear Ordering Problem

**Source**: [https://proceedings.mlr.press/v235/stein24a.html](https://proceedings.mlr.press/v235/stein24a.html)

**TLDR**: Algorithms are introduced to efficiently solve subsets of the NP-hard linear ordering problem by determining partial optimal orderings.

## Abstract

The linear ordering problem consists in finding a linear order $<$ on a finite set $A$ so as to minimize the sum of costs associated with pairs of elements $a, b$ for which $a < b$. The problem is NP-hard and APX-hard. We introduce algorithms for solving the problem partially by deciding efficiently for some pairs $(a,b)$ whether $a < b$ is in an optimal solution. To do so, we construct maps from the feasible set of orders to itself and establish efficiently testable conditions on the cost function of the problem for which these maps are improving. We examine the effectiveness and efficiency of these conditions and algorithms empirically, on two data sets.