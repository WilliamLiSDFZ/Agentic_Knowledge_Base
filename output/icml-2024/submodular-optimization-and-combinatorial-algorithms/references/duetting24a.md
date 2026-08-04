---
title: "Consistent Submodular Maximization"
source: "https://proceedings.mlr.press/v235/duetting24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/duetting24a/duetting24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms']
tags: ['submodular-maximization', 'streaming', 'consistency', 'dynamic-algorithms']
venue: "ICML 2024"
tldr: "An algorithm for consistent submodular maximization under cardinality constraints in a dynamic streaming setting with bounded element replacements."
---

# Consistent Submodular Maximization

**Source**: [https://proceedings.mlr.press/v235/duetting24a.html](https://proceedings.mlr.press/v235/duetting24a.html)

**TLDR**: An algorithm for consistent submodular maximization under cardinality constraints in a dynamic streaming setting with bounded element replacements.

## Abstract

Maximizing monotone submodular functions under cardinality constraints is a classic optimization task with several applications in data mining and machine learning. In this paper, we study this problem in a dynamic environment with consistency constraints: elements arrive in a streaming fashion, and the goal is maintaining a constant approximation to the optimal solution while having a stable solution (i.e., the number of changes between two consecutive solutions is bounded). In this setting, we provide algorithms with different trade-offs between consistency and approximation quality. We also complement our theoretical results with an experimental analysis showing the effectiveness of our algorithms in real-world instances.