---
title: "Sample Average Approximation for Conditional Stochastic Optimization with Dependent Data"
source: "https://proceedings.mlr.press/v235/wang24bc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bc/wang24bc.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'optimization-algorithms-convergence-theory']
tags: ['conditional-stochastic-optimization', 'sample-average-approximation', 'dependent-data', 'finite-sample-guarantees']
venue: "ICML 2024"
tldr: "Extends sample average approximation theory for conditional stochastic optimization to dependent (non-i.i.d.) data settings with consistency and finite-sample guarantees."
---

# Sample Average Approximation for Conditional Stochastic Optimization with Dependent Data

**Source**: [https://proceedings.mlr.press/v235/wang24bc.html](https://proceedings.mlr.press/v235/wang24bc.html)

**TLDR**: Extends sample average approximation theory for conditional stochastic optimization to dependent (non-i.i.d.) data settings with consistency and finite-sample guarantees.

## Abstract

Conditional Stochastic Optimization (CSO) is a powerful modelling paradigm for optimization under uncertainty. The existing literature on CSO is mainly based on the independence assumption of data, which shows that the solution of CSO is asymptotically consistent and enjoys a finite sample guarantee. The independence assumption, however, does not typically hold in many important applications with dependence patterns, such as time series analysis, operational control, and reinforcement learning. In this paper, we aim to fill this gap and consider a Sample Average Approximation (SAA) for CSO with dependent data. Leveraging covariance inequalities and independent block sampling technique, we provide theoretical guarantees of SAA for CSO with dependent data. In particular, we show that SAA for CSO retains asymptotic consistency and a finite sample guarantee under mild conditions. In addition, we establish the sample complexity $O(d / \varepsilon^4)$ of SAA for CSO, which is shown to be of the same order as independent cases. Through experiments on several applications, we verify the theoretical results and demonstrate that dependence does not degrade the performance of the SAA approach in real data applications.