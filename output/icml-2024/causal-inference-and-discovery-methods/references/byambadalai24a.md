---
title: "Estimating Distributional Treatment Effects in Randomized Experiments: Machine Learning for Variance Reduction"
source: "https://proceedings.mlr.press/v235/byambadalai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/byambadalai24a/byambadalai24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['distributional-treatment-effects', 'regression-adjustment', 'randomized-experiments', 'variance-reduction']
venue: "ICML 2024"
tldr: "Proposes a machine-learning-based regression adjustment method for estimating distributional treatment effects in randomized experiments with reduced variance."
---

# Estimating Distributional Treatment Effects in Randomized Experiments: Machine Learning for Variance Reduction

**Source**: [https://proceedings.mlr.press/v235/byambadalai24a.html](https://proceedings.mlr.press/v235/byambadalai24a.html)

**TLDR**: Proposes a machine-learning-based regression adjustment method for estimating distributional treatment effects in randomized experiments with reduced variance.

## Abstract

We propose a novel regression adjustment method designed for estimating distributional treatment effect parameters in randomized experiments. Randomized experiments have been extensively used to estimate treatment effects in various scientific fields. However, to gain deeper insights, it is essential to estimate distributional treatment effects rather than relying solely on average effects. Our approach incorporates pre-treatment covariates into a distributional regression framework, utilizing machine learning techniques to improve the precision of distributional treatment effect estimators. The proposed approach can be readily implemented with off-the-shelf machine learning methods and remains valid as long as the nuisance components are reasonably well estimated. Also, we establish the asymptotic properties of the proposed estimator and present a uniformly valid inference method. Through simulation results and real data analysis, we demonstrate the effectiveness of integrating machine learning techniques in reducing the variance of distributional treatment effect estimators in finite samples.