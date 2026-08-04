---
title: "Inferring Change Points in High-Dimensional Linear Regression via Approximate Message Passing"
source: "https://proceedings.mlr.press/v235/arpino24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/arpino24a/arpino24a.pdf"
categories: ['sequential-change-detection-theory-and-algorithms', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['change-point-detection', 'high-dimensional-regression', 'approximate-message-passing', 'Bayesian-inference']
venue: "ICML 2024"
tldr: "Proposes an AMP algorithm for localizing change points in high-dimensional linear regression with exact asymptotic characterization."
---

# Inferring Change Points in High-Dimensional Linear Regression via Approximate Message Passing

**Source**: [https://proceedings.mlr.press/v235/arpino24a.html](https://proceedings.mlr.press/v235/arpino24a.html)

**TLDR**: Proposes an AMP algorithm for localizing change points in high-dimensional linear regression with exact asymptotic characterization.

## Abstract

We consider the problem of localizing change points in high-dimensional linear regression. We propose an Approximate Message Passing (AMP) algorithm for estimating both the signals and the change point locations. Assuming Gaussian covariates, we give an exact asymptotic characterization of its estimation performance in the limit where the number of samples grows proportionally to the signal dimension. Our algorithm can be tailored to exploit any prior information on the signal, noise, and change points. It also enables uncertainty quantification in the form of an efficiently computable approximate posterior distribution, whose asymptotic form we characterize exactly. We validate our theory via numerical experiments, and demonstrate the favorable performance of our estimators on both synthetic data and images.