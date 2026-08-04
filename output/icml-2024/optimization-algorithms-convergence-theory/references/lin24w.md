---
title: "Autonomous Sparse Mean-CVaR Portfolio Optimization"
source: "https://proceedings.mlr.press/v235/lin24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24w/lin24w.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['portfolio-optimization', 'CVaR', 'sparse-optimization']
venue: "ICML 2024"
tldr: "An autonomous sparse mean-CVaR portfolio optimization approach avoiding NP-hard combinatorial search through a novel reformulation."
---

# Autonomous Sparse Mean-CVaR Portfolio Optimization

**Source**: [https://proceedings.mlr.press/v235/lin24w.html](https://proceedings.mlr.press/v235/lin24w.html)

**TLDR**: An autonomous sparse mean-CVaR portfolio optimization approach avoiding NP-hard combinatorial search through a novel reformulation.

## Abstract

The $\ell_0$-constrained mean-CVaR model poses a significant challenge due to its NP-hard nature, typically tackled through combinatorial methods characterized by high computational demands. From a markedly different perspective, we propose an innovative autonomous sparse mean-CVaR portfolio model, capable of approximating the original $\ell_0$-constrained mean-CVaR model with arbitrary accuracy. The core idea is to convert the $\ell_0$ constraint into an indicator function and subsequently handle it through a tailed approximation. We then propose a proximal alternating linearized minimization algorithm, coupled with a nested fixed-point proximity algorithm (both convergent), to iteratively solve the model. Autonomy in sparsity refers to retaining a significant portion of assets within the selected asset pool during adjustments in pool size. Consequently, our framework offers a theoretically guaranteed approximation of the $\ell_0$-constrained mean-CVaR model, improving computational efficiency while providing a robust asset selection scheme.