---
title: "Conformal prediction for multi-dimensional time series by ellipsoidal sets"
source: "https://proceedings.mlr.press/v235/xu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24m/xu24m.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'multivariate-time-series', 'ellipsoidal-sets']
venue: "ICML 2024"
tldr: "This work extends conformal prediction to multi-dimensional time series by constructing ellipsoidal prediction sets for joint uncertainty quantification."
---

# Conformal prediction for multi-dimensional time series by ellipsoidal sets

**Source**: [https://proceedings.mlr.press/v235/xu24m.html](https://proceedings.mlr.press/v235/xu24m.html)

**TLDR**: This work extends conformal prediction to multi-dimensional time series by constructing ellipsoidal prediction sets for joint uncertainty quantification.

## Abstract

Conformal prediction (CP) has been a popular method for uncertainty quantification because it is distribution-free, model-agnostic, and theoretically sound. For forecasting problems in supervised learning, most CP methods focus on building prediction intervals for univariate responses. In this work, we develop a sequential CP method called $\texttt{MultiDimSPCI}$ that builds prediction $\textit{regions}$ for a multivariate response, especially in the context of multivariate time series, which are not exchangeable. Theoretically, we estimate $\textit{finite-sample}$ high-probability bounds on the conditional coverage gap. Empirically, we demonstrate that $\texttt{MultiDimSPCI}$ maintains valid coverage on a wide range of multivariate time series while producing smaller prediction regions than CP and non-CP baselines.