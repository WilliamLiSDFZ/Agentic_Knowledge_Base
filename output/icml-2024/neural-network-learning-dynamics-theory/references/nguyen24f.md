---
title: "On Least Square Estimation in Softmax Gating Mixture of Experts"
source: "https://proceedings.mlr.press/v235/nguyen24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24f/nguyen24f.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['mixture-of-experts', 'softmax-gating', 'least-squares-estimation']
venue: "ICML 2024"
tldr: "Analyzes the statistical properties of least square estimation in softmax gating mixture of experts models."
---

# On Least Square Estimation in Softmax Gating Mixture of Experts

**Source**: [https://proceedings.mlr.press/v235/nguyen24f.html](https://proceedings.mlr.press/v235/nguyen24f.html)

**TLDR**: Analyzes the statistical properties of least square estimation in softmax gating mixture of experts models.

## Abstract

Mixture of experts (MoE) model is a statistical machine learning design that aggregates multiple expert networks using a softmax gating function in order to form a more intricate and expressive model. Despite being commonly used in several applications owing to their scalability, the mathematical and statistical properties of MoE models are complex and difficult to analyze. As a result, previous theoretical works have primarily focused on probabilistic MoE models by imposing the impractical assumption that the data are generated from a Gaussian MoE model. In this work, we investigate the performance of the least squares estimators (LSE) under a deterministic MoE model where the data are sampled according to a regression model, a setting that has remained largely unexplored. We establish a condition called strong identifiability to characterize the convergence behavior of various types of expert functions. We demonstrate that the rates for estimating strongly identifiable experts, namely the widely used feed forward networks with activation functions $\mathrm{sigmoid}(\cdot)$ and $\tanh(\cdot)$, are substantially faster than those of polynomial experts, which we show to exhibit a surprising slow estimation rate. Our findings have important practical implications for expert selection.