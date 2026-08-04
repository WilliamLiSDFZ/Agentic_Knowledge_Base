---
title: "Generalization Analysis of Stochastic Weight Averaging with General Sampling"
source: "https://proceedings.mlr.press/v235/wang24bl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bl/wang24bl.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['stochastic-weight-averaging', 'generalization', 'convergence-theory', 'non-convex-optimization']
venue: "ICML 2024"
tldr: "Provides theoretical generalization analysis of stochastic weight averaging beyond convex settings and i.i.d. sampling assumptions."
---

# Generalization Analysis of Stochastic Weight Averaging with General Sampling

**Source**: [https://proceedings.mlr.press/v235/wang24bl.html](https://proceedings.mlr.press/v235/wang24bl.html)

**TLDR**: Provides theoretical generalization analysis of stochastic weight averaging beyond convex settings and i.i.d. sampling assumptions.

## Abstract

Stochastic weight averaging (SWA) method has empirically proven its advantages compared to stochastic gradient descent (SGD). Despite it is widespread used, theoretical investigations have been limited, particularly in scenarios beyond the ideal setting of convex and sampling with replacement. However, non-convex cases and sampling without replacement are very practical in real-world applications. The main challenges under the above settings are two-folds: (i) All the historical gradient information introduced by SWA is considered, while the analysis of SGD using the tool of uniform stability requires only to bound the current gradient. (ii) The $(1+\alpha\beta)$-expansion property causes the boundary of each gradient step dependent on the previous step, making the boundary of each historical gradient in SWA nested and the theoretical analysis even harder. To address the theoretical challenges, we adopt mathematical induction to find a recursive representation that bounds the gradient at each step. Based on this, we establish stability bounds supporting sampling with and without replacement in the non-convex setting. Furthermore, the derived generalization bounds of SWA are sharper than SGD. At last, experimental results on several benchmarks verify our theoretical results.