---
title: "Accelerated Algorithms for Constrained Nonconvex-Nonconcave Min-Max Optimization and Comonotone Inclusion"
source: "https://proceedings.mlr.press/v235/cai24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24f/cai24f.pdf"
categories: ['optimization-algorithms-convergence-theory', 'time-series-modeling-and-forecasting-methods']
tags: ['min-max-optimization', 'nonconvex-nonconcave', 'comonotone', 'accelerated-algorithms']
venue: "ICML 2024"
tldr: "Extends Extra Anchored Gradient algorithms to constrained comonotone min-max optimization and comonotone inclusion with accelerated convergence guarantees."
---

# Accelerated Algorithms for Constrained Nonconvex-Nonconcave Min-Max Optimization and Comonotone Inclusion

**Source**: [https://proceedings.mlr.press/v235/cai24f.html](https://proceedings.mlr.press/v235/cai24f.html)

**TLDR**: Extends Extra Anchored Gradient algorithms to constrained comonotone min-max optimization and comonotone inclusion with accelerated convergence guarantees.

## Abstract

We study constrained comonotone min-max optimization, a structured class of nonconvex-nonconcave min-max optimization problems, and their generalization to comonotone inclusion. In our first contribution, we extend the Extra Anchored Gradient (EAG) algorithm, originally proposed by Yoon and Ryu (2021) for unconstrained min-max optimization, to constrained comonotone min-max optimization and comonotone inclusion, achieving an optimal convergence rate of $O\left(\frac{1}{T}\right)$ among all first-order methods. Additionally, we prove that the algorithm’s iterations converge to a point in the solution set. In our second contribution, we extend the Fast Extra Gradient (FEG) algorithm, as developed by Lee and Kim (2021), to constrained comonotone min-max optimization and comonotone inclusion, achieving the same $O\left(\frac{1}{T}\right)$ convergence rate. This rate is applicable to the broadest set of comonotone inclusion problems yet studied in the literature. Our analyses are based on simple potential function arguments, which might be useful for analyzing other accelerated algorithms.