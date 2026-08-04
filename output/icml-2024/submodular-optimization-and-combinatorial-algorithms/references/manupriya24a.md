---
title: "Submodular framework for structured-sparse optimal transport"
source: "https://proceedings.mlr.press/v235/manupriya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/manupriya24a/manupriya24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms', 'sampling-compression-and-dimensionality-reduction']
tags: ['optimal-transport', 'submodular-optimization', 'sparse-transport-plans']
venue: "ICML 2024"
tldr: "A submodular framework for learning structured sparse transport plans within the unbalanced optimal transport setting."
---

# Submodular framework for structured-sparse optimal transport

**Source**: [https://proceedings.mlr.press/v235/manupriya24a.html](https://proceedings.mlr.press/v235/manupriya24a.html)

**TLDR**: A submodular framework for learning structured sparse transport plans within the unbalanced optimal transport setting.

## Abstract

Unbalanced optimal transport (UOT) has recently gained much attention due to its flexible framework for handling un-normalized measures and its robustness properties. In this work, we explore learning (structured) sparse transport plans in the UOT setting, i.e., transport plans have an upper bound on the number of non-sparse entries in each column (structured sparse pattern) or in the whole plan (general sparse pattern). We propose novel sparsity-constrained UOT formulations building on the recently explored maximum mean discrepancy based UOT. We show that the proposed optimization problem is equivalent to the maximization of a weakly submodular function over a uniform matroid or a partition matroid. We develop efficient gradient-based discrete greedy algorithms and provide the corresponding theoretical guarantees. Empirically, we observe that our proposed greedy algorithms select a diverse support set and we illustrate the efficacy of the proposed approach in various applications.