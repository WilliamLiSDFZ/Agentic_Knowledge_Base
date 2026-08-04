---
title: "High-dimensional Linear Bandits with Knapsacks"
source: "https://proceedings.mlr.press/v235/ma24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24p/ma24p.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['high-dimensional-bandits', 'contextual-bandits-with-knapsacks', 'sparsity']
venue: "ICML 2024"
tldr: "An online sparse learning approach exploiting sparsity to achieve improved regret for high-dimensional contextual bandits with knapsack constraints."
---

# High-dimensional Linear Bandits with Knapsacks

**Source**: [https://proceedings.mlr.press/v235/ma24p.html](https://proceedings.mlr.press/v235/ma24p.html)

**TLDR**: An online sparse learning approach exploiting sparsity to achieve improved regret for high-dimensional contextual bandits with knapsack constraints.

## Abstract

We study the contextual bandits with knapsack (CBwK) problem under the high-dimensional setting where the dimension of the feature is large. We investigate how to exploit the sparsity structure to achieve improved regret for the CBwK problem. To this end, we first develop an online variant of the hard thresholding algorithm that performs the optimal sparse estimation. We further combine our online estimator with a primal-dual framework, where we assign a dual variable to each knapsack constraint and utilize an online learning algorithm to update the dual variable, thereby controlling the consumption of the knapsack capacity. We show that this integrated approach allows us to achieve a sublinear regret that depends logarithmically on the feature dimension, thus improving the polynomial dependency established in the previous literature. We also apply our framework to the high-dimension contextual bandit problem without the knapsack constraint and achieve optimal regret in both the data-poor regime and the data-rich regime.