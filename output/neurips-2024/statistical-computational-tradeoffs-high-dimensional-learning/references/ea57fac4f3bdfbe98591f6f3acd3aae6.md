---
title: "Semi-Random Matrix Completion via Flow-Based Adaptive Reweighting"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ea57fac4f3bdfbe98591f6f3acd3aae6-Abstract-Conference.html"
categories: ['statistical-learning-theory-and-matrix-methods', 'statistical-computational-tradeoffs-high-dimensional-learning']
tags: ['matrix-completion', 'semi-random-model', 'flow-based-reweighting']
venue: "NeurIPS 2024"
tldr: "Develops a flow-based adaptive reweighting algorithm for matrix completion under semi-random observation models with improved sample complexity guarantees."
---

# Semi-Random Matrix Completion via Flow-Based Adaptive Reweighting

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ea57fac4f3bdfbe98591f6f3acd3aae6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ea57fac4f3bdfbe98591f6f3acd3aae6-Abstract-Conference.html)

**TLDR**: Develops a flow-based adaptive reweighting algorithm for matrix completion under semi-random observation models with improved sample complexity guarantees.

## Abstract

We consider the well-studied problem of completing a rank-$r$, $\mu$-incoherent matrix $\mathbf{M} \in \mathbb{R}^{d \times d}$ from incomplete observations. We focus on this problem in the semi-random setting where each entry is independently revealed with probability at least $p = \frac{\textup{poly}(r, \mu, \log d)}{d}$. Whereas multiple nearly-linear time algorithms have been established in the more specialized fully-random setting where each entry is revealed with probablity exactly $p$, the only known nearly-linear time algorithm in the semi-random setting is due to [CG18], whose sample complexity has a polynomial dependence on the inverse accuracy and condition number and thus cannot achieve high-accuracy recovery. Our main result is the first high-accuracy nearly-linear time algorithm for solving semi-random matrix completion, and an extension to the noisy observation setting.Our result builds upon the recent short-flat decomposition framework of [KLLST23a, KLLST23b] and leverages fast algorithms for flow problems on graphs to solve adaptive reweighting subproblems efficiently.