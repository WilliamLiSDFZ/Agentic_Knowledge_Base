---
title: "$H$-Consistency Guarantees for Regression"
source: "https://proceedings.mlr.press/v235/mao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mao24c/mao24c.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['H-consistency', 'regression', 'surrogate-loss']
venue: "ICML 2024"
tldr: "A systematic study of H-consistency bounds for regression, generalizing existing tools and proving new results for common regression losses."
---

# $H$-Consistency Guarantees for Regression

**Source**: [https://proceedings.mlr.press/v235/mao24c.html](https://proceedings.mlr.press/v235/mao24c.html)

**TLDR**: A systematic study of H-consistency bounds for regression, generalizing existing tools and proving new results for common regression losses.

## Abstract

We present a detailed study of $H$-consistency bounds for regression. We first present new theorems that generalize the tools previously given to establish $H$-consistency bounds. This generalization proves essential for analyzing $H$-consistency bounds specific to regression. Next, we prove a series of novel $H$-consistency bounds for surrogate loss functions of the squared loss, under the assumption of a symmetric distribution and a bounded hypothesis set. This includes positive results for the Huber loss, all $\ell_p$ losses, $p \geq 1$, the squared $\epsilon$-insensitive loss, as well as a negative result for the $\epsilon$-insensitive loss used in Support Vector Regression (SVR). We further leverage our analysis of $H$-consistency for regression and derive principled surrogate losses for adversarial regression (Section 5). This readily establishes novel algorithms for adversarial regression, for which we report favorable experimental results in Section 6.