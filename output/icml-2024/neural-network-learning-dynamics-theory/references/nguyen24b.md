---
title: "A General Theory for Softmax Gating Multinomial Logistic Mixture of Experts"
source: "https://proceedings.mlr.press/v235/nguyen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24b/nguyen24b.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['mixture-of-experts', 'softmax-gating', 'multinomial-logistic']
venue: "ICML 2024"
tldr: "A general theory for softmax gating in multinomial logistic mixture of experts models is developed, explaining convergence and expert specialization behavior."
---

# A General Theory for Softmax Gating Multinomial Logistic Mixture of Experts

**Source**: [https://proceedings.mlr.press/v235/nguyen24b.html](https://proceedings.mlr.press/v235/nguyen24b.html)

**TLDR**: A general theory for softmax gating in multinomial logistic mixture of experts models is developed, explaining convergence and expert specialization behavior.

## Abstract

Mixture-of-experts (MoE) model incorporates the power of multiple submodels via gating functions to achieve greater performance in numerous regression and classification applications. From a theoretical perspective, while there have been previous attempts to comprehend the behavior of that model under the regression settings through the convergence analysis of maximum likelihood estimation in the Gaussian MoE model, such analysis under the setting of a classification problem has remained missing in the literature. We close this gap by establishing the convergence rates of density estimation and parameter estimation in the softmax gating multinomial logistic MoE model. Notably, when part of the expert parameters vanish, these rates are shown to be slower than polynomial rates owing to an inherent interaction between the softmax gating and expert functions via partial differential equations. To address this issue, we propose using a novel class of modified softmax gating functions which transform the input before delivering them to the gating functions. As a result, the previous interaction disappears and the parameter estimation rates are significantly improved.