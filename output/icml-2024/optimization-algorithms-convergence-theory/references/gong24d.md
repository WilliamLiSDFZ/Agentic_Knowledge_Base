---
title: "A Nearly Optimal Single Loop Algorithm for Stochastic Bilevel Optimization under Unbounded Smoothness"
source: "https://proceedings.mlr.press/v235/gong24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24d/gong24d.pdf"
categories: ['optimization-algorithms-convergence-theory', 'large-language-model-alignment-and-capabilities']
tags: ['bilevel-optimization', 'unbounded-smoothness', 'meta-learning']
venue: "ICML 2024"
tldr: "This paper proposes a nearly optimal single-loop algorithm for stochastic bilevel optimization with nonconvex upper-level functions exhibiting potentially unbounded smoothness."
---

# A Nearly Optimal Single Loop Algorithm for Stochastic Bilevel Optimization under Unbounded Smoothness

**Source**: [https://proceedings.mlr.press/v235/gong24d.html](https://proceedings.mlr.press/v235/gong24d.html)

**TLDR**: This paper proposes a nearly optimal single-loop algorithm for stochastic bilevel optimization with nonconvex upper-level functions exhibiting potentially unbounded smoothness.

## Abstract

This paper studies the problem of stochastic bilevel optimization where the upper-level function is nonconvex with potentially unbounded smoothness and the lower-level function is strongly convex. This problem is motivated by meta-learning applied to sequential data, such as text classification using recurrent neural networks, where the smoothness constant of the upper-level loss function scales linearly with the gradient norm and can be potentially unbounded. Existing algorithm crucially relies on the nested loop design, which requires significant tuning efforts and is not practical. In this paper, we address this issue by proposing a Single Loop bIlevel oPtimizer (SLIP). The proposed algorithm first updates the lower-level variable by a few steps of stochastic gradient descent, and then simultaneously updates the upper-level variable by normalized stochastic gradient descent with momentum and the lower-level variable by stochastic gradient descent. Under standard assumptions, we show that our algorithm finds an $\epsilon$-stationary point within $\widetilde{O}(1/\epsilon^4)$[Here $\widetilde{O}(\cdot)$ compresses logarithmic factors of $1/\epsilon$ and $1/\delta$, where $\delta\in(0,1)$ denotes the failure probability.] oracle calls of stochastic gradient or Hessian-vector product, both in expectation and with high probability. This complexity result is nearly optimal up to logarithmic factors without mean-square smoothness of the stochastic gradient oracle. Our proof relies on (i) a refined characterization and control of the lower-level variable and (ii) establishing a novel connection between bilevel optimization and stochastic optimization under distributional drift. Our experiments on various tasks show that our algorithm significantly outperforms strong baselines in bilevel optimization.