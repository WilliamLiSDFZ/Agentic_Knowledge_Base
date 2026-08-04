---
title: "Efficient Stochastic Approximation of Minimax Excess Risk Optimization"
source: "https://proceedings.mlr.press/v235/zhang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24d/zhang24d.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['minimax-optimization', 'excess-risk', 'distributionally-robust']
venue: "ICML 2024"
tldr: "An efficient stochastic approximation algorithm for minimax excess risk optimization with improved theoretical guarantees over standard DRO."
---

# Efficient Stochastic Approximation of Minimax Excess Risk Optimization

**Source**: [https://proceedings.mlr.press/v235/zhang24d.html](https://proceedings.mlr.press/v235/zhang24d.html)

**TLDR**: An efficient stochastic approximation algorithm for minimax excess risk optimization with improved theoretical guarantees over standard DRO.

## Abstract

While traditional distributionally robust optimization (DRO) aims to minimize the maximal risk over a set of distributions, Agarwal & Zhang (2022) recently proposed a variant that replaces risk with excess risk. Compared to DRO, the new formulation—minimax excess risk optimization (MERO) has the advantage of suppressing the effect of heterogeneous noise in different distributions. However, the choice of excess risk leads to a very challenging minimax optimization problem, and currently there exists only an inefficient algorithm for empirical MERO. In this paper, we develop efficient stochastic approximation approaches which directly target MERO. Specifically, we leverage techniques from stochastic convex optimization to estimate the minimal risk of every distribution, and solve MERO as a stochastic convex-concave optimization (SCCO) problem with biased gradients. The presence of bias makes existing theoretical guarantees of SCCO inapplicable, and fortunately, we demonstrate that the bias, caused by the estimation error of the minimal risk, is under-control. Thus, MERO can still be optimized with a nearly optimal convergence rate. Moreover, we investigate a practical scenario where the quantity of samples drawn from each distribution may differ, and propose a stochastic approach that delivers distribution-dependent convergence rates.