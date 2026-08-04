---
title: "Accelerating Look-ahead in Bayesian Optimization: Multilevel Monte Carlo is All you Need"
source: "https://proceedings.mlr.press/v235/yang24aj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24aj/yang24aj.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['bayesian-optimization', 'multilevel-monte-carlo', 'look-ahead', 'nested-expectations']
venue: "ICML 2024"
tldr: "Multilevel Monte Carlo is applied to improve computational efficiency of multi-step look-ahead Bayesian optimization with nested expectations."
---

# Accelerating Look-ahead in Bayesian Optimization: Multilevel Monte Carlo is All you Need

**Source**: [https://proceedings.mlr.press/v235/yang24aj.html](https://proceedings.mlr.press/v235/yang24aj.html)

**TLDR**: Multilevel Monte Carlo is applied to improve computational efficiency of multi-step look-ahead Bayesian optimization with nested expectations.

## Abstract

We leverage multilevel Monte Carlo (MLMC) to improve the performance of multi-step look- ahead Bayesian optimization (BO) methods that involve nested expectations and maximizations. Often these expectations must be computed by Monte Carlo (MC). The complexity rate of naive MC degrades for nested operations, whereas MLMC is capable of achieving the canonical MC convergence rate for this type of problem, independently of dimension and without any smoothness assumptions. Our theoretical study focuses on the approximation improvements for two- and three-step look-ahead acquisition functions, but, as we discuss, the approach is generalizable in various ways, including beyond the context of BO. Our findings are verified numerically and the benefits of MLMC for BO are illustrated on several benchmark examples. Code is available at https://github.com/Shangda-Yang/MLMCBO.