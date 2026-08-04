---
title: "Adaptive Stabilization Based on Machine Learning for Column Generation"
source: "https://proceedings.mlr.press/v235/shen24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shen24e/shen24e.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['column-generation', 'stabilization', 'machine-learning-for-optimization']
venue: "ICML 2024"
tldr: "An adaptive machine learning-based stabilization method is proposed for column generation to improve convergence of large-scale linear programs."
---

# Adaptive Stabilization Based on Machine Learning for Column Generation

**Source**: [https://proceedings.mlr.press/v235/shen24e.html](https://proceedings.mlr.press/v235/shen24e.html)

**TLDR**: An adaptive machine learning-based stabilization method is proposed for column generation to improve convergence of large-scale linear programs.

## Abstract

Column generation (CG) is a well-established method for solving large-scale linear programs. It involves iteratively optimizing a subproblem containing a subset of columns and using its dual solution to generate new columns with negative reduced costs. This process continues until the dual values converge to the optimal dual solution to the original problem. A natural phenomenon in CG is the heavy oscillation of the dual values during iterations, which can lead to a substantial slowdown in the convergence rate. Stabilization techniques are devised to accelerate the convergence of dual values by using information beyond the state of the current subproblem. However, there remains a significant gap in obtaining more accurate dual values at an earlier stage. To further narrow this gap, this paper introduces a novel approach consisting of 1) a machine learning approach for accurate prediction of optimal dual solutions and 2) an adaptive stabilization technique that effectively capitalizes on accurate predictions. On the graph coloring problem, we show that our method achieves a significantly improved convergence rate compared to traditional methods.