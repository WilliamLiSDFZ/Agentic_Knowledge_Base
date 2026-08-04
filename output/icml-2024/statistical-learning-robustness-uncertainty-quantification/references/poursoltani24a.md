---
title: "Robust Data-driven Prescriptiveness Optimization"
source: "https://proceedings.mlr.press/v235/poursoltani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/poursoltani24a/poursoltani24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'optimization-algorithms-convergence-theory']
tags: ['prescriptive-optimization', 'robustness', 'side-information']
venue: "ICML 2024"
tldr: "A robust optimization framework for data-driven prescriptiveness that leverages side information with a universal performance measure."
---

# Robust Data-driven Prescriptiveness Optimization

**Source**: [https://proceedings.mlr.press/v235/poursoltani24a.html](https://proceedings.mlr.press/v235/poursoltani24a.html)

**TLDR**: A robust optimization framework for data-driven prescriptiveness that leverages side information with a universal performance measure.

## Abstract

The abundance of data has led to the emergence of a variety of optimization techniques that attempt to leverage available side information to provide more anticipative decisions. The wide range of methods and contexts of application have motivated the design of a universal unitless measure of performance known as the coefficient of prescriptiveness. This coefficient was designed to quantify both the quality of contextual decisions compared to a reference one and the prescriptive power of side information. To identify policies that maximize the former in a data-driven context, this paper introduces a distributionally robust contextual optimization model where the coefficient of prescriptiveness substitutes for the classical empirical risk minimization objective. We present a bisection algorithm to solve this model, which relies on solving a series of linear programs when the distributional ambiguity set has an appropriate nested form and polyhedral structure. Studying a contextual shortest path problem, we evaluate the robustness of the resulting policies against alternative methods when the out-of-sample dataset is subject to varying amounts of distribution shift.