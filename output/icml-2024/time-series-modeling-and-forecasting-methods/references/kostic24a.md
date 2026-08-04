---
title: "Consistent Long-Term Forecasting of Ergodic Dynamical Systems"
source: "https://proceedings.mlr.press/v235/kostic24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kostic24a/kostic24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['ergodic-dynamical-systems', 'long-term-forecasting', 'Koopman-operators', 'transfer-operators', 'consistency']
venue: "ICML 2024"
tldr: "A consistent long-term forecasting method for ergodic dynamical systems using Koopman and transfer operator theory."
---

# Consistent Long-Term Forecasting of Ergodic Dynamical Systems

**Source**: [https://proceedings.mlr.press/v235/kostic24a.html](https://proceedings.mlr.press/v235/kostic24a.html)

**TLDR**: A consistent long-term forecasting method for ergodic dynamical systems using Koopman and transfer operator theory.

## Abstract

We study the problem of forecasting the evolution of a function of the state (observable) of a discrete ergodic dynamical system over multiple time steps. The elegant theory of Koopman and transfer operators can be used to evolve any such function forward in time. However, their estimators are usually unreliable in long-term forecasting. We show how classical techniques of eigenvalue deflation from operator theory and feature centering from statistics can be exploited to enhance standard estimators. We develop a novel technique to derive high probability bounds on powers of empirical estimators. Our approach, rooted in the stability theory of non-normal operators, allows us to establish uniform in time bounds for the forecasting error, which hold even on infinite time horizons. We further show that our approach can be seamlessly employed to forecast future state distributions from an initial one, with provably uniform error bounds. Numerical experiments illustrate the advantages of our approach in practice.