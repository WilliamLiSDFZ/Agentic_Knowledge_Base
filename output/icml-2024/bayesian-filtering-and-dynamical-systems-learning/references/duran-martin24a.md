---
title: "Outlier-robust Kalman Filtering through Generalised Bayes"
source: "https://proceedings.mlr.press/v235/duran-martin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/duran-martin24a/duran-martin24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['kalman-filtering', 'robust-inference', 'generalised-bayes', 'outlier-robustness', 'state-space-models']
venue: "ICML 2024"
tldr: "Proposes a provably robust closed-form Bayesian update rule for online filtering in state-space models that handles outliers and model misspecification."
---

# Outlier-robust Kalman Filtering through Generalised Bayes

**Source**: [https://proceedings.mlr.press/v235/duran-martin24a.html](https://proceedings.mlr.press/v235/duran-martin24a.html)

**TLDR**: Proposes a provably robust closed-form Bayesian update rule for online filtering in state-space models that handles outliers and model misspecification.

## Abstract

We derive a novel, provably robust, efficient, and closed-form Bayesian update rule for online filtering in state-space models in the presence of outliers and misspecified measurement models. Our method combines generalised Bayesian inference with filtering methods such as the extended and ensemble Kalman filter. We use the former to show robustness and the latter to ensure computational efficiency in the case of nonlinear models. Our method matches or outperforms other robust filtering methods (such as those based on variational Bayes) at a much lower computational cost. We show this empirically on a range of filtering problems with outlier measurements, such as object tracking, state estimation in high-dimensional chaotic systems, and online learning of neural networks.