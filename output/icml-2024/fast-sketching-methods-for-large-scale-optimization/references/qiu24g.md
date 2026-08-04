---
title: "Gradient Compressed Sensing: A Query-Efficient Gradient Estimator for High-Dimensional Zeroth-Order Optimization"
source: "https://proceedings.mlr.press/v235/qiu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24g/qiu24g.pdf"
categories: ['fast-sketching-methods-for-large-scale-optimization', 'optimization-algorithms-convergence-theory']
tags: ['zeroth-order-optimization', 'compressed-sensing', 'sparse-gradients', 'query-complexity', 'high-dimensional']
venue: "ICML 2024"
tldr: "A query-efficient gradient estimator exploiting gradient sparsity for high-dimensional zeroth-order optimization."
---

# Gradient Compressed Sensing: A Query-Efficient Gradient Estimator for High-Dimensional Zeroth-Order Optimization

**Source**: [https://proceedings.mlr.press/v235/qiu24g.html](https://proceedings.mlr.press/v235/qiu24g.html)

**TLDR**: A query-efficient gradient estimator exploiting gradient sparsity for high-dimensional zeroth-order optimization.

## Abstract

We study nonconvex zeroth-order optimization (ZOO) in a high-dimensional space $\mathbb R^d$ for functions with approximately $s$-sparse gradients. To reduce the dependence on the dimensionality $d$ in the query complexity, high-dimensional ZOO methods seek to leverage gradient sparsity to design gradient estimators. The previous best method needs $O\big(s\log\frac ds\big)$ queries per step to achieve $O\big(\frac1T\big)$ rate of convergence w.r.t. the number T of steps. In this paper, we propose Gradient Compressed Sensing (GraCe), a query-efficient and accurate estimator for sparse gradients that uses only $O\big(s\log\log\frac ds\big)$ queries per step and still achieves $O\big(\frac1T\big)$ rate of convergence. To our best knowledge, we are the first to achieve a double-logarithmic dependence on $d$ in the query complexity under weaker assumptions. Our proposed GraCe generalizes the Indyk–Price–Woodruff (IPW) algorithm in compressed sensing from linear measurements to nonlinear functions. Furthermore, since the IPW algorithm is purely theoretical due to its impractically large constant, we improve the IPW algorithm via our dependent random partition technique together with our corresponding novel analysis and successfully reduce the constant by a factor of nearly $4300$. Our GraCe is not only theoretically query-efficient but also achieves strong empirical performance. We benchmark our GraCe against $12$ existing ZOO methods with $10000$-dimensional functions and demonstrate that GraCe significantly outperforms existing methods. Our code is publicly available at https://github.com/q-rz/ICML24-GraCe.