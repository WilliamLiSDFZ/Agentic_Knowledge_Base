---
title: "Boosting Offline Optimizers with Surrogate Sensitivity"
source: "https://proceedings.mlr.press/v235/dao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dao24b/dao24b.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'optimization-algorithms-convergence-theory']
tags: ['offline-optimization', 'surrogate-models', 'sensitivity', 'material-design', 'black-box-optimization']
venue: "ICML 2024"
tldr: "Proposes incorporating surrogate sensitivity into offline optimization to improve the reliability and performance of surrogate-based black-box optimization."
---

# Boosting Offline Optimizers with Surrogate Sensitivity

**Source**: [https://proceedings.mlr.press/v235/dao24b.html](https://proceedings.mlr.press/v235/dao24b.html)

**TLDR**: Proposes incorporating surrogate sensitivity into offline optimization to improve the reliability and performance of surrogate-based black-box optimization.

## Abstract

Offline optimization is an important task in numerous material engineering domains where online experimentation to collect data is too expensive and needs to be replaced by an in silico maximization of a surrogate of the black-box function. Although such a surrogate can be learned from offline data, its prediction might not be reliable outside the offline data regime, which happens when the surrogate has narrow prediction margin and is (therefore) sensitive to small perturbations of its parameterization. This raises the following questions: (1) how to regulate the sensitivity of a surrogate model; and (2) whether conditioning an offline optimizer with such less sensitive surrogate will lead to better optimization performance. To address these questions, we develop an optimizable sensitivity measurement for the surrogate model, which then inspires a sensitivity-informed regularizer that is applicable to a wide range of offline optimizers. This development is both orthogonal and synergistic to prior research on offline optimization, which is demonstrated in our extensive experiment benchmark.