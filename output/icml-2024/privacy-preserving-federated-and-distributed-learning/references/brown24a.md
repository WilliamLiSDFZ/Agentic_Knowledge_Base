---
title: "Private Gradient Descent for Linear Regression: Tighter Error Bounds and Instance-Specific Uncertainty Estimation"
source: "https://proceedings.mlr.press/v235/brown24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/brown24a/brown24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'linear-regression', 'gradient-descent', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "Improved analysis of differentially private gradient descent for linear regression with tighter error bounds and instance-specific uncertainty characterization."
---

# Private Gradient Descent for Linear Regression: Tighter Error Bounds and Instance-Specific Uncertainty Estimation

**Source**: [https://proceedings.mlr.press/v235/brown24a.html](https://proceedings.mlr.press/v235/brown24a.html)

**TLDR**: Improved analysis of differentially private gradient descent for linear regression with tighter error bounds and instance-specific uncertainty characterization.

## Abstract

We provide an improved analysis of standard differentially private gradient descent for linear regression under the squared error loss. Under modest assumptions on the input, we characterize the distribution of the iterate at each time step. Our analysis leads to new results on the algorithm’s accuracy: for a proper fixed choice of hyperparameters, the sample complexity depends only linearly on the dimension of the data. This matches the dimension-dependence of the (non-private) ordinary least squares estimator as well as that of recent private algorithms that rely on sophisticated adaptive gradient-clipping schemes (Varshney et al., 2022; Liu et al., 2023). Our analysis of the iterates’ distribution also allows us to construct confidence intervals for the empirical optimizer which adapt automatically to the variance of the algorithm on a particular data set. We validate our theorems through experiments on synthetic data.