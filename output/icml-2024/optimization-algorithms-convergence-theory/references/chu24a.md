---
title: "SPABA: A Single-Loop and Probabilistic Stochastic Bilevel Algorithm Achieving Optimal Sample Complexity"
source: "https://proceedings.mlr.press/v235/chu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chu24a/chu24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'privacy-preserving-federated-and-distributed-learning']
tags: ['bilevel-optimization', 'stochastic-optimization', 'sample-complexity']
venue: "ICML 2024"
tldr: "SPABA is a single-loop probabilistic bilevel optimization algorithm that achieves optimal sample complexity matching single-level stochastic methods."
---

# SPABA: A Single-Loop and Probabilistic Stochastic Bilevel Algorithm Achieving Optimal Sample Complexity

**Source**: [https://proceedings.mlr.press/v235/chu24a.html](https://proceedings.mlr.press/v235/chu24a.html)

**TLDR**: SPABA is a single-loop probabilistic bilevel optimization algorithm that achieves optimal sample complexity matching single-level stochastic methods.

## Abstract

While stochastic bilevel optimization methods have been extensively studied for addressing large-scale nested optimization problems in machine learning, it remains an open question whether the optimal complexity bounds for solving bilevel optimization are the same as those in single-level optimization. Our main result resolves this question: SPABA, an adaptation of the PAGE method for nonconvex optimization in (Li et al., 2021) to the bilevel setting, can achieve optimal sample complexity in both the finite-sum and expectation settings. We show the optimality of SPABA by proving that there is no gap in complexity analysis between stochastic bilevel and single-level optimization when implementing PAGE. Notably, as indicated by the results of (Dagréou et al., 2022), there might exist a gap in complexity analysis when implementing other stochastic gradient estimators, like SGD and SAGA. In addition to SPABA, we propose several other single-loop stochastic bilevel algorithms, that either match or improve the state-of-the-art sample complexity results, leveraging our convergence rate and complexity analysis. Numerical experiments demonstrate the superior practical performance of the proposed methods.